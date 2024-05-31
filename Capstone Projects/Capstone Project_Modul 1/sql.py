import mysql.connector

# Membuat koneksi ke server MySQL
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="username",  
        password="password",  
        database="nama_database"  
    )

    if connection.is_connected():
        print("Koneksi berhasil!")

        cursor = connection.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS example_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50)
        )
        """
        cursor.execute(create_table_query)
        print("Tabel berhasil dibuat atau sudah ada sebelumnya.")

        cursor.close()
        connection.close()
        print("Koneksi ditutup.")

except mysql.connector.Error as error:
    print("Error:", error)

def sql_connect():
    pass