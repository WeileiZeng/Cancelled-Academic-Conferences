


[Original page](https://docs.google.com/spreadsheets/d/1O3wnaFYSZCgY3Ih4yDw3EIH2SC_-vjhyHwrCQSy0J7M/htmlview?fbclid=IwAR3Z5VxuKicyB5h0dAIRhU5TtZq78dzFBZ45f8G7fI1sBhWEyFIj5rGibME#) by
[Anne Marie Gruber](https://twitter.com/amhgruber)

<!-- keys in yml file 'Acade','Annou','Dates','Locat','Notes' -->

| Conference | Announ- cement | Dates  | Location | Notes|{% for conference in  site.data.conferences %}
| {{ conference.Acade }} | [link]({{ conference.Annou }}) | {{ conference.Dates }}  | {{ conference.Locat }} | {{ conference.Notes }} |{% endfor %}

