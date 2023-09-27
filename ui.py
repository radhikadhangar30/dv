
import streamlit as st
import mysql.connector as mycon
db = mycon.connect(
    host='localhost', user='root',password = 'root', database = 'pydb'
)
print(db)
db_curr = db.cursor()


st.title('CRUD OPERATION')
tab1,tab2, tab3 = st.tabs(['Insert' , 'Update' , 'Delete'])

with tab1:
    no = st.number_input('Enter product No.:')
    name = st.text_input('Enter Product Name:')
    loc = st.text_input('Enter Product Location:')


    if st.button("Submit"):
        sql = "insert into dmart ( pro_no,pro_name,pro_loc )values(%s, %s,%s )"
        val = (no,name,loc )
        db_curr.execute(sql , val)
        db.commit()
        db_curr.execute('select * from dmart')
        st.table(db_curr.fetchall())
   
with tab2:
    st.header("Update")
    no1 = st.number_input('Update product No.:')
    name1 = st.text_input('Update Product Name.:')
    loc1 = st.text_input('Update Product Location.:')

    if st.button("Update"):
        sql = "UPDATE dmart SET pro_name = %s, pro_loc = %s WHERE pro_no = %s"
        val = (name1, loc1, no1)
        db_curr.execute(sql, val)
        db.commit()
        st.success("Data Updated Successfully!")

with tab3:
    st.header("Delete")
    delete_no = st.number_input('Enter product No. to delete:', key='delete_no')

    if st.button("Delete"):
        sql = "DELETE FROM dmart WHERE pro_no = %s"
        val = (delete_no,)
        db_curr.execute(sql, val)
        db.commit()
        st.success("Data Deleted Successfully!") 

db_curr.execute('SELECT * FROM dmart')
data = db_curr.fetchall()
st.table(data)


          
