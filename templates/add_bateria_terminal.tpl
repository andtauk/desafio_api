<h2> Adicionar Bateria ao terminal: {{ terminal.terminal_name }}</h2>

% if len(lista_baterias) == 0:
  <p>Não há baterias disponíveis para adicionar ao terminal</p>
% else:
  <form action="/add_bateria" method= "post">
    <label for="id">Selecione uma bateria para adicionar ao terminal:</label>
    <select name="id" id="id">
      % for bateria in lista_baterias:
        <option value="{{ bateria.id }}">{{ bateria.mac }}</option>
      % end
    </select>
    <br><br>
    <input type="submit" value="Submit">
  </form>
% end