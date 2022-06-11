<h2>Terminal: {{ terminal.terminal_name }}</h2>

% if len(lista_baterias) == 0:
  <h3>Não há baterias neste terminal.</h3>
%end

<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
}

/* Create three equal columns that floats next to each other */
.column {
  float: left;
  width: 150px;
  padding: 10px;
  height: 150px;
  border: 2px solid black;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}
</style>
</head>
<body>

% count = 0
% for i in range(len(lista_indices_n_colunas)):
  <div class="row">
    % for j in lista_indices_n_colunas[i]:
      % count += 1
      % bat = [x for x in lista_baterias if x.id == j][0]
      % cor = bat.cor
      % corrente = bat.corrente
      % mac = bat.mac
      <div class="column" style="background-color:{{ cor }};">
      <h3>Slot: {{ count }}</h3>
      <p>Corrente: {{ corrente }}</p>
      <p>mac: {{ mac }}</p>
    </div>
    % end 
  </div>

% end
</body>