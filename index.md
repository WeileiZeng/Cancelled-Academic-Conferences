{% include navigation.md %}

<!-- keys in yml file 'Acade','Annou','Dates','Locat','Notes' -->


<!-- old head
| Academic_Conference_Name  | Dates  | Location | Notes|
-->

{% assign section = "Acade" %}
<a name="{{ section }}">
{% assign conferences_by_name = site.data.conferences | sort: section  %}
{% include table-header.md %}{% for conference in  conferences_by_name  %}
| [{{ conference.Acade }}]({{ conference.Annou }}) | {{ conference.Dates }}  | {{ conference.Locat }} | {{ conference.Notes }} | {% endfor %}



{% assign section = "Dates" %}
<a name="{{ section }}">
{% assign conferences_by_name = site.data.conferences | sort: section  %}
{% include table-header.md %}{% for conference in  conferences_by_name  %}
| [{{ conference.Acade }}]({{ conference.Annou }}) | {{ conference.Dates }}  | {{ conference.Locat }} | {{ conference.Notes }} | {% endfor %}

{% assign section = "Locat" %}
<a name="{{ section }}">
{% assign conferences_by_name = site.data.conferences | sort: section  %}
{% include table-header.md %}{% for conference in  conferences_by_name  %}
| [{{ conference.Acade }}]({{ conference.Annou }}) | {{ conference.Dates }}  | {{ conference.Locat }} | {{ conference.Notes }} | {% endfor %}

{% assign section = "Notes" %}
<a name="{{ section }}">
{% assign conferences_by_name = site.data.conferences | sort: section  %}
{% include table-header.md %}{% for conference in  conferences_by_name  %}
| [{{ conference.Acade }}]({{ conference.Annou }}) | {{ conference.Dates }}  | {{ conference.Locat }} | {{ conference.Notes }} | {% endfor %}