from io import BytesIO
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from _tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog
import pyodbc
import qrcode.util
qrcode.util.OPTIMAL_ENCODING = 'iso-8859-1'
import json
import os


class Plant():
     
    
     def __init__(self, root):
        self.root = root
        self.root.title("Quản Lý Truy Xuất Nguồn Gốc")
          # Giảm 30 pixels để tránh che phủ taskbar
        root.geometry("1200x800+0+0")
        root.resizable(False, False)
        title = Label(self.root,text="Quản Lý Truy Xuất Nguồn Gốc" ,bd=9,relief=GROOVE, font=("Roboto",30,"bold"),bg="#57a1f8",fg="black")
        title.pack(side=TOP,fill=X)
        #============== All Variables db========================================
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.category_var = StringVar()
        self.plantingDate_var = StringVar()
        self.location_var = StringVar()
        

        self.search_by=StringVar()
        self.search_txt = StringVar()

        #==============Manageframe============================================
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="snow")
        Manage_Frame.place(x=20,y=100,width=400,height=650)

        m_title = Label(Manage_Frame,text="Thông tin", bg="snow",fg="black",font=("Roboto",20,"bold"))
        m_title.grid(row=0 ,columnspan=2,pady=20)

        lbl_roll = Label(Manage_Frame,text="ID", bg="snow",fg="black",font=("Roboto",10,"bold"))
        lbl_roll.grid(row=1 ,column=0,pady=10,padx=20,sticky="w")
        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("Roboto",10,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1 ,column=1,pady=10,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="snow", fg="black", font=("Roboto", 10, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(Manage_Frame,textvariable=self.name_var, font=("Roboto", 10, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_category = Label(Manage_Frame, text="Category",bg="snow", fg="black", font=("Roboto", 10, "bold"))
        lbl_category.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_category = Entry(Manage_Frame, textvariable=self.category_var,font=("Roboto", 10, "bold"), bd=5, relief=GROOVE)
        txt_category.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_plantingDate = Label(Manage_Frame, text="PlantingDate", bg="snow", fg="black", font=("Roboto", 10, "bold"))
        lbl_plantingDate.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        txt_plantingDate = Entry(Manage_Frame, textvariable=self.plantingDate_var,font=("Roboto", 10, "bold"), bd=5, relief=GROOVE)
        txt_plantingDate.grid(row=4, column=1, pady=10, padx=20, sticky="w")
        

        lbl_location = Label(Manage_Frame, text="Location",bg="snow", fg="black", font=("Roboto", 10, "bold"))
        lbl_location.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_location = Entry(Manage_Frame,textvariable=self.location_var, font=("Roboto", 10, "bold"), bd=5, relief=GROOVE)
        txt_location.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        
        btn_img = Button(Manage_Frame, text="Chọn ảnh", width=10, command=self.select_image)
        btn_img.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        self.img_label = Label(Manage_Frame)
        self.img_label.grid(row=6,column=0,pady= 10, padx=2,sticky="w")

        btn_qr = Button(Manage_Frame, text="Tạo mã QR", width=10, command=self.generate_qr_code).grid(row=7, column=1, padx=20, pady=10)
        self.qr_label = Label(Manage_Frame)
        self.qr_label.grid(row=6,column=1,pady= 10, padx=2,sticky="w")
       


   #=========Button Frame==================
        btn_Frame = Frame(Manage_Frame, bd=3, relief=RIDGE, bg="snow")
        btn_Frame.place(x=10, y=570, width=370)

        Addbtn = Button(btn_Frame,text="Add",width=10,command=self.add_SP).grid(row=0,column=0,padx=5,pady=5)
        updatebtn = Button(btn_Frame, text="Update", width=10,command=self.update_data).grid(row=0, column=1, padx=5, pady=5)
        deletebtn = Button(btn_Frame, text="Delete", width=10,command=self.delete_data).grid(row=0, column=2, padx=5, pady=5)
        Clearbtn = Button(btn_Frame, text="Clear", width=10,command=self.clear).grid(row=0, column=3, padx=5, pady=5)
       
   # =========2nd Detials  Frame==================
        Detials_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="snow")
        Detials_Frame.place(x=430, y=100, width=750, height=650)

        lbl_search = Label(Detials_Frame, text="Search By", bg="snow", fg="Black",font=("Roboto", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        self.combo_search = ttk.Combobox(Detials_Frame,textvariable=self.search_by,width=10, font=("Roboto", 13, "bold"), state='readonly')
        self.combo_search['values'] = ("name", "category", "planting_date", "location")
        self.combo_search.grid(row=0, column=1, padx=20, pady=10)

        self.txt_search= Entry(Detials_Frame,textvariable=self.search_txt,width=20, font=("Roboto", 10, "bold"), bd=5, relief=GROOVE)
        self.txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detials_Frame, text="Search", width=10,pady=5,command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Detials_Frame, text="Show All", width=10, pady=5,command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

#========== table frame ===========
        Table_Frame = Frame(Detials_Frame, bd=4, relief=RIDGE, bg="snow")
        Table_Frame.place(x=10, y=70, width=700, height=620)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)
        self.plant_table = ttk.Treeview(Table_Frame,column=("ID","name","category","plantingDate","location","name_image"),
                                          xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.plant_table.xview)
        scroll_y.config(command=self.plant_table.yview)
        self.plant_table.heading("ID",text="ID")
        self.plant_table.heading("name", text="Name")
        self.plant_table.heading("category", text="Category")
        self.plant_table.heading("plantingDate", text="PlantingDate")
        self.plant_table.heading("location", text="Location")
        self.plant_table.heading("name_image", text="Image")

        
        self.plant_table['show'] = 'headings'
        self.plant_table.column("ID",width=50)
        self.plant_table.column("name", width=100)
        self.plant_table.column("category", width=100)
        self.plant_table.column("plantingDate", width=100)
        self.plant_table.column("location", width=100)
        self.plant_table.column("name_image", width=100)


        self.plant_table.pack(fill=BOTH , expand=1)
        self.plant_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()
     def db_connect(self):
        try:
            conn = pyodbc.connect('DRIVER={SQL SERVER};'
                                  'SERVER=KASHI\KASHI;'
                                  'DATABASE=QuanLyTruyXuat;'
                                  )
            return conn
        except pyodbc.Error as e:
            messagebox.showerror("Lỗi", f"Lỗi kết nối cơ sở dữ liệu: {str(e)}")
            return None
     def add_SP(self):
       
        conn = self.db_connect()
        if conn:
            cursor = conn.cursor()
            try:
                if file_path:
                 with open(file_path, 'rb') as image_file:
                    image_binary = image_file.read()
                 image_name = self.name_var.get()+".png"    
                # Read the image file and convert it to binary
                 self.save_image_to_file(image_binary,image_name)
                 cursor.execute("INSERT INTO Plants_and_Livestock (name, category, planting_date, location, name_image, image) VALUES (?, ?, ?, ?, ?,?)",
                               (self.name_var.get(), self.category_var.get(), self.plantingDate_var.get(),
                                self.location_var.get(),image_name, image_binary))

                 conn.commit()
                 self.clear()
                 messagebox.showinfo("Thành công", "Record has been inserted")
                 self.fetch_data() 
            except pyodbc.Error as e:
                messagebox.showerror('Database Error', f'Error: {str(e)}')
            finally:
                conn.close()
     def fetch_data(self):
         
        conn = self.db_connect()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM Plants_and_Livestock")
                rows = cursor.fetchall()

                # Clear existing data in the Treeview
                for i in self.plant_table.get_children():
                    self.plant_table.delete(i)

                # Insert fetched data into the Treeview
                for row in rows:
                    row_list = list(row)
                    self.plant_table.insert('', 'end', values=row_list)

            except pyodbc.Error as e:
                messagebox.showerror('Database Error', f'Error: {str(e)}')
            finally:
                conn.close()
     def clear(self):
         self.Roll_No_var.set("")
         self.name_var.set("")
         self.category_var.set("")
         self.plantingDate_var.set("")
         self.location_var.set("")
         
         self.img_label.config(image="")
         self.img_label.image = ""
         self.qr_label.config(image="")
         self.qr_label.image = ""

     def get_cursor(self, ev):
        conn = self.db_connect()
        if conn:
            cursor = conn.cursor()
    # Get the item from the selection
        selected_item  = self.plant_table.selection()
        if selected_item :
    # Retrieve the values from the selected item
            selected_id  = self.plant_table.item(selected_item, 'values')[0]
            cursor.execute("SELECT id,name,category, planting_date,location,image,qr_image FROM Plants_and_Livestock WHERE id = ?",selected_id)
            row = cursor.fetchone()             
    # Populate the entry fields with the retrieved values
            if row:
                ID = row.id
                name = row.name
                category = row.category
                plantingDate = row.planting_date
                location = row.location              
                img_data = row.image
                qr_img = row.qr_image
            with open('temp_image.jpg', 'wb') as f:
                f.write(img_data)        
            self.display_image('temp_image.jpg',self.img_label)   
            if qr_img:    
                with open('temp1_image.jpg', 'wb') as f:
                    f.write(qr_img)        
                self.display_image('temp1_image.jpg',self.qr_label) 
            else:
                self.qr_label.config(image="")
                self.qr_label.image = None
            self.clear 
            self.Roll_No_var.set(ID)
            self.name_var.set(name)
            self.category_var.set(category)
            self.plantingDate_var.set(plantingDate)
            self.location_var.set(location)
     def update_data(self):
    # Get the values from the entry fields
        id_val = self.Roll_No_var.get()
        name_val = self.name_var.get()
        category_val = self.category_var.get()
        planting_date_val = self.plantingDate_var.get()
        location_val = self.location_var.get()
        
        
    # Check if an ID is selected
        if not id_val:
            messagebox.showwarning("Lỗi", "Chọn một bản ghi để cập nhật")
            return

    # Connect to the database
        conn = self.db_connect()
        if conn:
         cursor = conn.cursor()
         try:
            
            if file_path:               
                with open(file_path, 'rb') as image_file:
                    image_binary = image_file.read()
                image_name = file_path.split("/")[-1]    
            # Update the record in the database
            
                cursor.execute("UPDATE plants_and_livestock SET qr_image=NULL WHERE id=?", (id_val,))                                         
                cursor.execute("UPDATE plants_and_livestock SET name=?, category=?, planting_date=?, location=?,name_image=?, image=? WHERE id=?",
                           (name_val, category_val, planting_date_val, location_val,  image_name,image_binary, id_val))
            else: 
                cursor.execute("UPDATE plants_and_livestock SET qr_image=NULL WHERE id=?", (id_val,))                                         
                cursor.execute("UPDATE plants_and_livestock SET qr_image=NULL, name=?, category=?, planting_date=?, location=? WHERE id=?",
                               (name_val, category_val, planting_date_val, location_val, id_val))
            conn.commit()
            messagebox.showinfo("Thành công", "Dữ liệu đã được cập nhật")
            self.fetch_data()  # Update the displayed data in the Treeview
            self.generate_qr_code()
         except pyodbc.Error as e:
                messagebox.showerror('Lỗi cơ sở dữ liệu', f'Lỗi: {str(e)}')
         finally:
                conn.close()
     def delete_data(self):

        selected_id = self.Roll_No_var.get()

        if not selected_id:
            messagebox.showwarning("Lỗi", "Chọn một bản ghi để xóa")
            return

        conn = self.db_connect()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM plants_and_livestock WHERE id=?", (selected_id,))
                conn.commit()
                messagebox.showinfo("Thành công", "Dữ liệu đã được xóa")
                self.clear()  
                self.fetch_data()  

            except pyodbc.Error as e:
                 messagebox.showerror('Lỗi cơ sở dữ liệu', f'Lỗi: {str(e)}')
            finally:
              conn.close()
     def search_data(self):
        search_by = self.combo_search.get()
        search_text = self.txt_search.get()

        if not search_text:
            messagebox.showwarning("Lỗi", "Nhập dữ liệu cần tìm kiếm")
            return

       
        valid_search_fields = ["name", "category", "planting_date", "location"]
        if search_by not in valid_search_fields:
            messagebox.showwarning("Lỗi", "Chọn trường tìm kiếm hợp lệ")
            return

        conn = self.db_connect()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute(f"SELECT * FROM plants_and_livestock WHERE {search_by} LIKE ?", ('%' + search_text + '%',))
                rows = cursor.fetchall()

                
                for i in self.plant_table.get_children():
                    self.plant_table.delete(i)

                
                for row in rows:
                    row_list = list(row)
                    self.plant_table.insert('', 'end', values=row_list)

            except pyodbc.Error as e:
                messagebox.showerror('Database Error', f'Error: {str(e)}')
            finally:
                conn.close()
     def select_image(self):
        global file_path 
        file_path= filedialog.askopenfilename(title="Chọn ảnh", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:

            img = Image.open(file_path)
            img.thumbnail((150,150))
            img = ImageTk.PhotoImage(img)
            self.img_label.config(image=img)
            self.img_label.image = img
     def generate_qr_code(self):
        selected_id = self.Roll_No_var.get()
        if not selected_id:
         messagebox.showwarning("Lỗi", "Chọn một bản ghi để tạo mã QR")
         return
        
        conn = self.db_connect()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM plants_and_livestock WHERE id=?", (selected_id,))
                row = cursor.fetchone()
                data = {             
                "name": row[1],
                "category": row[2],
                "plantingDate": row[3],
                "location": row[4],
                "image":row[5]
                }
                json_data = json.dumps(data, indent=4)
                qr = qrcode.QRCode(version=1, box_size=10, border=5)
                qr.add_data(json_data)
                qr.make(fit=True)
                qr_image = qr.make_image(fill_color="black", back_color="white")
                product_name = data.get("name", "product_name")

            # Save the QR code image as a PNG
                qr_filename = f"project/img/qr_codes/{product_name}.png"
                qr_image.save(qr_filename)
                with open(qr_filename, 'rb') as qr_file:
                    qr_binary_data = qr_file.read()

            # Update the database to include the QR code image data
                cursor.execute("UPDATE plants_and_livestock SET qr_image=? WHERE id=?", (qr_binary_data, selected_id))
                conn.commit()
               
                messagebox.showinfo("Thành công", "Mã QR đã được tạo và lưu thành file JSON")

            except pyodbc.Error as e:
                messagebox.showerror('Database Error', f'Error: {str(e)}')
            finally:
                conn.close()    
     def display_image(self,file_path,label):
        img = Image.open(file_path)
        img.thumbnail((150, 150))
        img = ImageTk.PhotoImage(img)
        label.config(image=img)
        label.image = img 
     def save_image_to_file(self, image_binary, image_name):
        image_path = os.path.join("project/img/data", image_name)

        with open(image_path, 'wb') as image_file:
         image_file.write(image_binary)
     def main():
        root = Tk()
        app = Plant(root)
        root.mainloop()

         