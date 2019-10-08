{% extends "base.html" %}

{% block innihald %}
		<a href="/karfa">Karfa</a>
		<h1>Vörulistinn:</h1>

		{% for i in v %}
			<section> <img src="/static/fott{{i[0]}}.jpg"></section>
			<h5> {{ i[1] }}<a href="/kaupa/{{ i[0] }}">{{ i[2] }}</a></h5>
		{% endfor%}

{% endblock %}
