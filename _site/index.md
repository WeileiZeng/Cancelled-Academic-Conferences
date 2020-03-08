{% include navigation.md %}

<!-- keys in yml file 'Acade','Annou','Dates','Locat','Notes' -->

{% assign conferences_by_name = site.data.conferences | sort: "Acade" %}

| Academic_Conference_Name  | Dates  | Location | Notes|{% for conference in  conferences_by_name  %}
| [{{ conference.Acade }}]({{ conference.Annou }}) | {{ conference.Dates }}  | {{ conference.Locat }} | {{ conference.Notes }} | {% endfor %}

