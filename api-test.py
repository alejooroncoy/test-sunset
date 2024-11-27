import os
from dotenv import load_dotenv
import libsql_experimental as libsql

#url = os.getenv("TURSO_DATABASE_URL")
#auth_token = os.getenv("TURSO_AUTH_TOKEN")

url = 'libsql://testing-nicolas-alejooroncoy.turso.io'
auth_token = 'eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJpYXQiOjE3MzI2MjA1OTQsImlkIjoiNWRmNTdmMzktZGUyNC00M2M2LThlODgtZjQ5OTg3NWUyNzI4In0.NoF0-kkz8nq6YsF4mQ_8seqg2aLKWCtVZBN0z6CsMK88M8_C4wF37tt0q1pvypwoVAFBJCB2ZgJ2LPYixyfHBA'

conn = libsql.connect("testing-nicolas-alejooroncoy.db", sync_url=url, auth_token=auth_token)
conn.sync()



def create(table, data):
    data = input("Introduce los valores de la tupla (separados por comas): ")
    data = tuple(data.split(","))
    try:
        columns_query = f"PRAGMA table_info({table})"
        columns_result = conn.execute(columns_query)
        columns = [column[1] for column in columns_result.fetchall() if column[1] != 'id']
        
        placeholders = ', '.join(['?'] * len(columns))
        query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})"
        
        conn.execute(query, data) 
        conn.commit()
        print("Registro insertado con éxito.")
    except Exception as e:
        print(f"Error al insertar: {e}")


def read(table):
    try:
        query = f"SELECT * FROM {table}"
        result = conn.execute(query)
        
        columns = [description[0] for description in result.description]
        
        print(" | ".join(columns))
        print("-" * (len(columns) * 10))
        
        for row in result.fetchall():
            print(" | ".join(str(value) for value in row))
    except Exception as e:
        print(f"Error al leer: {e}")

def update(table):
    try:
        columns_query = f"PRAGMA table_info({table})"
        columns_result = conn.execute(columns_query)
        columns = [column[1] for column in columns_result.fetchall() if column[1] != 'id']  # Excluir 'id'
        
        print("Campos disponibles para actualizar:")
        for idx, col in enumerate(columns, 1):
            print(f"{idx}. {col}")
        
        column_choice = int(input(f"Elige el número del campo a modificar (1-{len(columns)}): ")) - 1
        if column_choice < 0 or column_choice >= len(columns):
            print("Selección inválida.")
            return
        
        col = columns[column_choice]
        
        row_id = input("Introduce el ID del registro a actualizar: ")
        
        new_value = input(f"Introduce el nuevo valor para {col}: ")
        
        query = f"UPDATE {table} SET {col} = ? WHERE id = ?"
        conn.execute(query, (new_value, row_id))
        conn.commit()
        print("Registro actualizado con éxito.")
    
    except Exception as e:
        print(f"Error al actualizar: {e}")

def delete(table):
    try:
        row_id = input("Introduce el ID del registro a eliminar: ")
        query = f"DELETE FROM {table} WHERE id = ?"
        conn.execute(query, (row_id,))
        conn.commit()
        print("Registro eliminado con éxito.")
    except Exception as e:
        print(f"Error al eliminar: {e}")


def comman(command):
    parts = command.split()
    
    if len(parts) < 2:
        print("Comando inválido.")
        return
    
    operation = parts[0].lower()
    table = parts[1]

    if operation == "post":
        create(table)
    elif operation == "get":
        read(table)
    elif operation == "put":
        update(table)
    elif operation == "delete":
        delete(table)
    else:
        print("Comando no reconocido. Usa 'post', 'get', 'put' o 'delete'.")

def terminal():
    print("Terminal (escribe 'exit' para salir)")

    while True:
        command = input(">>> ")
        
        if command.lower() == 'exit':
            print("Saliendo de la terminal...")
            break
        
        try:
            comman(command)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    terminal()