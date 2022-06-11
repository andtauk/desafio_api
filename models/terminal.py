class Terminal:
    """ """

    def __init__(self, terminal_name, id=None):
        self.id = id
        self.terminal_name = terminal_name

    def __dict__(self):
        return {
            "id": self.id,
            "terminal_name": self.terminal_name,
        }

    def __str__(self):
        return f"{self.id} {self.terminal_name}"

    def __repr__(self):
        return f"{self.id} {self.terminal_name}"


class TerminalCRUD:

    table_name_terminal = "terminal"
    column_id = "id"
    column_terminal_name = "terminal_name"

    def __init__(self, db):
        self.db = db

    def insert(self, terminal: Terminal):
        with self.db:
            sql = f""" INSERT INTO {self.table_name_terminal}({self.column_terminal_name})
                  VALUES(?) """
            c = self.db.cursor()
            c.execute(sql, (terminal.terminal_name,))

    def get_all(self):
        sql = f" SELECT * FROM {self.table_name_terminal} "
        c = self.db.cursor()
        terminal_output = c.execute(sql).fetchall()
        terminal_list = []
        for terminal in terminal_output:
            terminal = {
                self.column_id: terminal[0],
                self.column_terminal_name: terminal[1],
            }
            terminal_list.append(Terminal(**terminal))

        return terminal_list

    def get(self, id):
        sql = f" SELECT * FROM {self.table_name_terminal} WHERE {self.column_id} = ?"
        c = self.db.cursor()
        terminal_output = c.execute(sql, (id,)).fetchone()
        if terminal_output is None:
            return None
        terminal = {
            self.column_id: terminal_output[0],
            self.column_terminal_name: terminal_output[1],
        }
        return Terminal(**terminal)

    def update(self, terminal: Terminal):
        with self.db:
            sql = f""" UPDATE {self.table_name_terminal}
                      SET {self.column_terminal_name} = ?
                      WHERE {self.column_id} = ? """
            c = self.db.cursor()
            c.execute(sql, (terminal.terminal_name, terminal.id))
            
    def delete_all(self):
        with self.db:
            sql = f" DELETE FROM {self.table_name_terminal}"
            c = self.db.cursor()
            c.execute(sql)

    def delete(self, id):
        with self.db:
            sql = f" DELETE FROM {self.table_name_terminal} WHERE {self.column_id} = ?"
            c = self.db.cursor()
            c.execute(sql, (id,))

    @staticmethod
    def sql_string():
        return f"""
            CREATE TABLE IF NOT EXISTS {TerminalCRUD.table_name_terminal} (
                                        {TerminalCRUD.column_id} integer,
                                        {TerminalCRUD.column_terminal_name} text,
                                        PRIMARY KEY ({TerminalCRUD.column_id})
                                    );
        """
