from models.bateria import BateriaCRUD
from models.terminal import TerminalCRUD


class Terminal_Bateria(object):
    def __init__(self, terminal_id, bateria_id, id=None):
        self.id = id
        self.terminal_id = terminal_id
        self.bateria_id = bateria_id

    def __dict__(self):
        return {
            self.column_id: self.id,
            self.column_terminal_id: self.terminal_id,
            self.column_bateria_id: self.bateria_id,
        }

    def __str__(self):
        return f"{self.id} {self.terminal_id} {self.bateria_id}"

    def __repr__(self):
        return f"{self.id} {self.terminal_id} {self.bateria_id}"


class Terminal_BateriaCRUD:
    table_name_terminal_bateria = "terminal_bateria"
    column_id = "id"
    column_terminal_id = "terminal_id"
    column_bateria_id = "bateria_id"

    def __init__(self, db):
        self.db = db

    def insert(self, terminal_bateria: Terminal_Bateria):
        with self.db:
            sql = f""" INSERT INTO {self.table_name_terminal_bateria}
                ({self.column_terminal_id}, {self.column_bateria_id})
                VALUES(?,?) """
            c = self.db.cursor()
            c.execute(sql, (terminal_bateria.terminal_id, terminal_bateria.bateria_id))

    def get_all(self):
        sql = f" SELECT * FROM {self.table_name_terminal_bateria} "
        c = self.db.cursor()
        terminal_bateria_output = c.execute(sql).fetchall()
        terminal_bateria_list = []
        for terminal_bateria in terminal_bateria_output:
            terminal_bateria = {
                self.column_id: terminal_bateria[0],
                self.column_terminal_id: terminal_bateria[1],
                self.column_bateria_id: terminal_bateria[2],
            }
            terminal_bateria_list.append(Terminal_Bateria(**terminal_bateria))

        return terminal_bateria_list

    def get(self, id):
        sql = f" SELECT * FROM {self.table_name_terminal_bateria} WHERE {self.column_id} = ?"
        c = self.db.cursor()
        terminal_bateria_output = c.execute(sql, (id,)).fetchone()
        terminal_bateria = {
            self.column_id: terminal_bateria_output[0],
            self.column_terminal_id: terminal_bateria_output[1],
            self.column_bateria_id: terminal_bateria_output[2],
        }
        return Terminal_Bateria(**terminal_bateria)

    def update(self, terminal_bateria: Terminal_Bateria):
        with self.db:
            sql = f""" UPDATE {self.table_name_terminal_bateria}
                  SET {self.column_terminal_id} = ?, {self.column_bateria_id} = ?
                  WHERE {self.column_id} = ?"""
            c = self.db.cursor()
            c.execute(
                sql,
                (
                    terminal_bateria.terminal_id,
                    terminal_bateria.bateria_id,
                    terminal_bateria.id,
                ),
            )

    def delete_all(self):
        with self.db:
            sql = f" DELETE FROM {self.table_name_terminal_bateria}"
            c = self.db.cursor()
            c.execute(sql)

    def delete(self, id):
        with self.db:
            sql = f" DELETE FROM {self.table_name_terminal_bateria} WHERE {self.column_id} = ?"
            c = self.db.cursor()
            c.execute(sql, (id,))

    @staticmethod
    def sql_string():
        return f"""
        CREATE TABLE IF NOT EXISTS {Terminal_BateriaCRUD.table_name_terminal_bateria} (
                      {Terminal_BateriaCRUD.column_id} integer,
                      {Terminal_BateriaCRUD.column_terminal_id} integer,
                      {Terminal_BateriaCRUD.column_bateria_id} integer,
                      PRIMARY KEY ({Terminal_BateriaCRUD.column_id}),
                      FOREIGN KEY ({Terminal_BateriaCRUD.column_terminal_id}) REFERENCES {
                          TerminalCRUD.table_name_terminal} ({TerminalCRUD.column_id}),
                      FOREIGN KEY ({Terminal_BateriaCRUD.column_bateria_id}) REFERENCES {
                          BateriaCRUD.table_name_bateria} ({BateriaCRUD.column_id})
          );"""
