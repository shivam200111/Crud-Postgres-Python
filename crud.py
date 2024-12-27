import psycopg2
import psycopg2.extras

# local postgres configuration
hostname = 'localhost'
database = 'learn1'
username = 'postgres'
pwd = 'roots'
port_id = 5432

conn = None

def perform_operation(choice, cur):
    if choice == 1:  # Drop and Create Table
        cur.execute('DROP TABLE IF EXISTS employee')
        create_script = '''CREATE TABLE IF NOT EXISTS employee(
                                id SERIAL PRIMARY KEY,
                                name VARCHAR(100) NOT NULL,
                                salary INTEGER NOT NULL)'''
        cur.execute(create_script)
        print("Table created successfully.")

    elif choice == 2:  # Insert Records
        insert_script = '''INSERT INTO employee(id, name, salary) VALUES(%s, %s, %s)'''
        insert_values = [(1, 'Shivam', 50000), (2, 'Dhruv', 60000), 
                         (3, 'Neeraj', 50000), (4, 'Manish', 60000),
                         (5, 'Rahul', 55000), (6, 'Rohit', 65000)]
        for record in insert_values:
            cur.execute(insert_script, record)
        print("Records inserted successfully.")

    elif choice == 3:  # Update Records
        update_script = '''UPDATE employee SET salary = salary + (salary * 0.2) WHERE name = 'Shivam' '''
        update_record = ('shivam',)  # Replace with the desired name
        cur.execute(update_script, update_record)
        print("Record updated successfully.")

    elif choice == 4:  # Delete Records
        delete_script = '''DELETE FROM employee WHERE name = %s'''
        delete_record = ('',)  # Replace with the desired name
        cur.execute(delete_script, delete_record)
        print("Record deleted successfully.")

    elif choice == 5:  # View Records
        cur.execute('SELECT * FROM employee')
        for record in cur.fetchall():
            print(record[0], record[1], record[2])

try:
    with psycopg2.connect(host=hostname, database=database, user=username, password=pwd, port=port_id) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            print("Choose an operation:")
            print("1. Create Table")
            print("2. Insert Records")
            print("3. Update Records")
            print("4. Delete Records")
            print("5. View Records")
            
            choice = int(input("Enter your choice (1-5): "))
            perform_operation(choice, cur)

except Exception as error:
    print("Error:", error)
finally:
    if conn is not None:
        conn.close()
