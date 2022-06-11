import bottle
import bottle.ext.sqlite
from database.sqlite_db import generate_database
from metodo.metodos import separar_lista_em_n_colunas
from models.bateria import BateriaCRUD
from models.terminal import TerminalCRUD
from models.terminal_bateria import Terminal_Bateria, Terminal_BateriaCRUD


app = bottle.Bottle()

batabase_name = "database/app.db"
plugin = bottle.ext.sqlite.Plugin(dbfile=batabase_name)
app.install(plugin)

generate_database()

@app.route("/")
def list_of_links():
    return bottle.template(
        "templates/list_of_links.tpl",
        links=[
            {"url": "/baterias"},
            {"url": "/terminal"},
            {"url": "/add_bateria"},
            {"url": "/remover_baterias"},
        ],
    )


@app.route("/add_bateria")
def add_bateria_terminal(db):
    lista_terminal_bateria = Terminal_BateriaCRUD(db).get_all()
    lista_baterias = BateriaCRUD(db).get_all()
    lista_indices_terminal_bateria = [x.bateria_id for x in lista_terminal_bateria]

    nova_lista_baterias = []
    for bateria in lista_baterias:
        if bateria.id not in lista_indices_terminal_bateria:
            nova_lista_baterias.append(bateria)

    terminal = TerminalCRUD(db).get(1)
    if terminal is None:
        return bottle.template("templates/erro.tpl", mensagem="Terminal não encontrado")

    return bottle.template(
        "templates/add_bateria_terminal.tpl",
        lista_baterias=nova_lista_baterias,
        terminal=terminal,
    )


@app.route("/add_bateria", method="POST")
def add_bateria_terminal_on_db(db):
    bateria_id = int(bottle.request.forms.get("id"))

    list_terminal_baterias = Terminal_BateriaCRUD(db).get_all()
    list_indices_terminal_baterias = [x.bateria_id for x in list_terminal_baterias]

    if bateria_id in list_indices_terminal_baterias:
        return bottle.template("templates/erro.tpl", mensagem="Bateria já existe no terminal")

    terminal_bateria = Terminal_Bateria(terminal_id=1, bateria_id=bateria_id)
    Terminal_BateriaCRUD(db).insert(terminal_bateria)
    return "Bateria adicionada com sucesso"


@app.route("/baterias")
def mostrar_baterias(db):
    lista_baterias = BateriaCRUD(db).get_all()
    return bottle.template("templates/mostrar_baterias.tpl", lista_baterias=lista_baterias)


@app.route("/terminal")
def mostrar_terminal(db, id_terminal=1):

    terminal = TerminalCRUD(db).get(id_terminal)
    if terminal is None:
        return bottle.template("templates/erro.tpl", mensagem="Terminal não encontrado")

    lista_terminal_bateria = Terminal_BateriaCRUD(db).get_all()
    lista_terminal_bateria = [
        x for x in lista_terminal_bateria if x.terminal_id == id_terminal
    ]

    lista_baterias = []
    for terminal_bateria in lista_terminal_bateria:
        bateria_id = terminal_bateria.bateria_id
        bateria = BateriaCRUD(db).get(bateria_id)
        lista_baterias.append(bateria)

    lista_indices_bateria = [x.id for x in lista_baterias]
    lista_indices_n_colunas = separar_lista_em_n_colunas(lista_indices_bateria, 3)
    return bottle.template(
        "templates/mostrar_terminal.tpl",
        lista_indices=lista_indices_bateria,
        lista_baterias=lista_baterias,
        lista_indices_n_colunas=lista_indices_n_colunas,
        terminal=terminal,
    )


@app.route("/remover_baterias")
def remover_baterias(db):
    Terminal_BateriaCRUD(db).delete_all()
    return "ok"


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True, reloader=True)