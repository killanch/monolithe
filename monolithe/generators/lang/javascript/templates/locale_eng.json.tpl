{ {% for rest_name, specification in specifications.items() %}
   "{{ specification.rest_name }}": {
       "entity": {
           "title": "{{ specification.userlabel }}",
           "description": "{{ specification.description}}"
       },
       {%- for attribute in specification.attributes %}
       "{{ attribute.name }}":{
           "label": "{{ attribute.userlabel }}",
           "tooltip": "{{ attribute.description }}"
       },{% endfor %}
   },{% endfor %}
}

