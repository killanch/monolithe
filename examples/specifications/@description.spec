{
  "apis": {
    "children": {
      "/lists": {
        "RESTName": "list",
        "resourceName": "lists",
        "entityName": "List",
        "operations": [
          { "availability": null, "method": "GET" },
          { "availability": null, "method": "POST" }
        ]
      }
    },
    "parents": {},
    "self": {}
  },
  "model": {
    "extends": "@name",
    "attributes": {
      "description": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "The description",
        "exposed": true,
        "filterable": true,
        "format": null,
        "maxLength": 2048,
        "maxValue": null,
        "minLength": 1,
        "minValue": null,
        "orderable": true,
        "readOnly": false,
        "required": false,
        "transient": false,
        "type": "string",
        "unique": true
      }
    }
  }
}