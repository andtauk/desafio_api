<h1> Lista de Baterias: </h1>

<style>
table, th, td {
  border:1px solid black;
  padding: 5px;
}
</style>

<table>
  <tr>
    <th>Endereço MAC</th>
    <th>Corrente</th>
  </tr>

  % for bateria in lista_baterias:
  <tr>
    <td>{{ bateria.mac }}</td>
    <td>{{ bateria.corrente }}</td>
  </tr>
  % end
</table> 