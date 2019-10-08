{% extends "base.html" %}

{% block innihald %}
	<a href="/">Heim</a>
	<a href="/karfa">Karfa</a>

	{% for i in valdarvorur %}
		<h5> {{ vorur[i][1] }} {{ vorur[i][2] }} </h5>
	{% endfor%}
	<h3>Heildarverð:{{hv}}</h3>
	<form action="/info" method="post">
    Nafn:<br>
    <input type="text" name="name" required="">
    <br>
	Netfangið:<br>
    <input type="email" name="email" required="">
    <br>
    Símanúmer:<br>
    <input type="text" name="phone" requierd="">
    <br>
    <br>
    <input type="submit" value="Skrá">
    </form> 
{% endblock %}