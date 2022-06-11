import random
import sqlite3
from sqlite3 import Error
from metodo.metodos import generate_random_mac_address
from models.bateria import Bateria, BateriaCRUD
from models.terminal import Terminal, TerminalCRUD
from models.terminal_bateria import Terminal_Bateria, Terminal_BateriaCRUD


def create_connection(db_file):

    db = None
    try:
        db = sqlite3.connect(db_file)
        return db
    except Error as e:
        print(e)

    return db


def create_table(db, create_table_sql):
    """create a table from the create_table_sql statement
    :param db: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = db.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def generate_database(database_path):

    database = database_path

    sql_create_bateria_table = BateriaCRUD.sql_string()

    sql_create_terminal_table = TerminalCRUD.sql_string()

    sql_create_terminal_bateria_table = Terminal_BateriaCRUD.sql_string()

    # create a database connection
    db = create_connection(database)

    # create tables
    if db is not None:
        # create projects table
        create_table(db, sql_create_terminal_table)

        # create tasks table
        create_table(db, sql_create_bateria_table)

        # create tasks table
        create_table(db, sql_create_terminal_bateria_table)
    else:
        print("Error! cannot create the database connection.")

    ##adicionar dados há tabela bateria, terminal e terminal_bateria
    num_baterias = len(BateriaCRUD(db).get_all())
    if num_baterias == 0:
      for _ in range(0, 10):
          dic = {
              BateriaCRUD.column_mac: generate_random_mac_address(),
              BateriaCRUD.column_corrente: random.randrange(0, 100) / 10,
          }
          bateria = Bateria(**dic)
          BateriaCRUD(db).insert(bateria)

    bateria_list = BateriaCRUD(db).get_all()

    if len(TerminalCRUD(db).get_all()) == 0:
      dic = {TerminalCRUD.column_terminal_name: "Test"}
      terminal1 = Terminal(**dic)
      TerminalCRUD(db).insert(terminal1)

    terminal_list = TerminalCRUD(db).get_all()

    if len(Terminal_BateriaCRUD(db).get_all()) == 0:
        dic = {
            Terminal_BateriaCRUD.column_terminal_id: terminal_list[0].id,
            Terminal_BateriaCRUD.column_bateria_id: bateria_list[0].id,
        }
        terminal_bateria = Terminal_Bateria(**dic)
        Terminal_BateriaCRUD(db).insert(terminal_bateria)

    db.close()
