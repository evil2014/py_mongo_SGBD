<!DOCTYPE html>
<html>
<head>
	<title>Banco de San Pedro</title>
</head>
<body>
	<center>
		<font size="7">Banco San Pedro</font>
		<img src="http://hayeshomes.ca/wp-content/uploads/2014/07/pigy-bank-calculator-426x260.jpg", width="200">
	</center>
	<p><p><p>
    %usuario = datos['nombre']
    <div style ="width:900px;background:#F9EECF;border:1px dotted black;">
      %if "cuentas" in datos:
      <b> Su estado bacario, {{usuario}}</b><br>
      <ul>
	%for c in datos['cuentas']:
	%cuentas = 'Cuenta:'+c['num']+'. Saldo ' +str(c['saldo'])
	<li> {{cuentas}}</li><br>
	%end
      </ul>

      %else:
      <b> lo sentimos, {{usuario}}, en esre momento no tienes ninguna cuenta con nosotros</b>
      %end
    </div>
</body>
</html>
