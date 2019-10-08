{% extends "base.html" %}

{% block innihald %}
		
		<a href="/popKarfa">Eyða Körfunni</a>
		<a href="/">Heim</a>
		<h1>Karfa:</h1>

		{% for i in valdarvorur %}
			<section> <img src="/static/fott{{nr+i}}.jpg"></section>
			<h5> {{ vorur[i][1] }} {{ vorur[i][2] }} </h5>
		{% endfor%}
		<h3>Heildarverð:{{hv}}</h3>
		<h2><a href="/info">Kaupa Vörur</a></h2>
{% endblock %}
