# XML helpers in $util.xml

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please
consider using the APPSYNC_JS runtime and its guides [here](resolver-reference-js-version.md "resolver-reference-js-version.md").

`$util.xml` contains helper methods that can make it easier to translate XML
responses to JSON or a Dictionary.

## $util.xml utils list

\***\*`$util.xml.toMap(String) :
 Map`\*\***

Converts an XML string to a Dictionary.

```
Input:

<?xml version="1.0" encoding="UTF-8"?>
<posts>
<post>
  <id>1</id>
  <title>Getting started with GraphQL</title>
</post>
</posts>

Output (JSON representation):

{
  "posts":{
    "post":{
      "id":1,
      "title":"Getting started with GraphQL"
    }
  }
}


Input:

<?xml version="1.0" encoding="UTF-8"?>
<posts>
<post>
  <id>1</id>
  <title>Getting started with GraphQL</title>
</post>
<post>
  <id>2</id>
  <title>Getting started with AWS AppSync</title>
</post>
</posts>

Output (JSON representation):

{
  "posts":{
    "post":[
        {
          "id":1,
          "title":"Getting started with GraphQL"
        },
        {
          "id":2,
          "title":"Getting started with AWS AppSync"
        }
    ]
  }
}
```

\***\*`$util.xml.toJsonString(String) :
 String`\*\***

Converts an XML string to a JSON string. This is similar to _toMap_, except that the output is a
string. This is useful if you want to directly convert and return the XML
response from an HTTP object to JSON.

\***\*`$util.xml.toJsonString(String, Boolean) :
 String`\*\***

Converts an XML string to a JSON string with an optional Boolean
parameter to determine if you want to string-encode the JSON.
