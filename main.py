import cx_Oracle
from prettytable import PrettyTable

# Creating connection
connection = cx_Oracle.connect("<username>/<password>@<host>/<SID>")


def using_queries(dpt_id=60):
    """Function by default receiving 60 IT_PROG department."""
    print("Oracle", connection.version)  # Show Oracle version

    cursor = connection.cursor()
    cursor.execute("""SELECT first_name, job_id, salary FROM employees WHERE department_id = :d_id""", d_id=dpt_id)

    # Beautifying the way to show data
    table = PrettyTable(["first_name", "job_id", "salary"])
    for f_name, j_id, salary in cursor:
        table.add_row([f_name, j_id, salary])
    print(table)

    connection.close()


if __name__ == "__main__":
    using_queries()
