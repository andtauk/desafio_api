class Bateria(object):
    cor_verde = "green"
    cor_vermelho = "red"

    def __init__(self, mac, corrente, limiar_bateria=5, id=None):
        self.id = id
        self.mac = mac
        self.corrente = corrente
        self.limiar_bateria = limiar_bateria

        if self.corrente > self.limiar_bateria:
            cor = self.cor_verde
        else:
            cor = self.cor_vermelho
        self.cor = cor

    def __str__(self):
        return f"{self.id} {self.mac} {self.corrente}"

    def __repr__(self):
        return f"{self.id} {self.mac} {self.corrente}"


class BateriaCRUD:
    table_name_bateria = "bateria"
    column_id = "id"
    column_mac = "mac"
    column_corrente = "corrente"

    def __init__(self, db):
        self.db = db

    def __dict__(self):
        return {
            self.column_id: self.id,
            self.column_mac: self.mac,
            self.column_corrente: self.corrente,
        }

    def insert(self, bateria: Bateria):
        with self.db:
            sql = f""" INSERT INTO {self.table_name_bateria}(
                {self.column_mac},{self.column_corrente})
                  VALUES(?,?) """
            c = self.db.cursor()
            c.execute(sql, (bateria.mac, bateria.corrente))

    def get_all(self):
        sql = f" SELECT * FROM {self.table_name_bateria} "
        c = self.db.cursor()
        bateria_output = c.execute(sql).fetchall()
        bateria_list = []
        for bateria in bateria_output:
            bateria = {
                self.column_id: bateria[0],
                self.column_mac: bateria[1],
                self.column_corrente: bateria[2],
            }
            bateria_list.append(Bateria(**bateria))

        return bateria_list

    def get(self, id):
        sql = f" SELECT * FROM {self.table_name_bateria} WHERE {self.column_id} = ?"
        c = self.db.cursor()
        bateria_output = c.execute(sql, (id,)).fetchone()
        bateria = {
            self.column_id: bateria_output[0],
            self.column_mac: bateria_output[1],
            self.column_corrente: bateria_output[2],
        }
        return Bateria(**bateria)

    def update(self, bateria: Bateria):
        with self.db:
            sql = f""" UPDATE {self.table_name_bateria}
                    SET {self.column_mac} = ?, {self.column_corrente} = ?
                    WHERE {self.column_id} = ? """
            c = self.db.cursor(sql, (bateria.mac, bateria.corrente))
            c.execute(sql, (bateria.mac, bateria.corrente, bateria.id))

    def delete_all(self):
        with self.db:
            sql = f" DELETE FROM {self.table_name_bateria}"
            c = self.db.cursor()
            c.execute(sql)

    def delete(self, id):
        with self.db:
            sql = f" DELETE FROM {self.table_name_bateria} WHERE {self.column_id} = ?"
            c = self.db.cursor()
            c.execute(sql, (id,))

    @staticmethod
    def sql_string():
        return f"""CREATE TABLE IF NOT EXISTS {BateriaCRUD.table_name_bateria} (
                                              {BateriaCRUD.column_id} integer unique,
                                              {BateriaCRUD.column_mac} text,
                                              {BateriaCRUD.column_corrente} real,
                                              PRIMARY KEY ({BateriaCRUD.column_id})
                                          );"""
