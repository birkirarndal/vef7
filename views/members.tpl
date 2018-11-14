<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="/static/style.css">
	<title>Félagaskrá</title>
</head>
<body>
	<h2>Félagaskrá</h2>
	<p>The members are as follows:</p>
	<table border="1">
		%for row in rows:
		<tr>
			%for col in row:
			<td>{{col}}</td>
			%end
		</tr>
		%end
	</table>
	<br>
	<a href="/">Aftur á skráningarsíðu</a>
</body>
</html>