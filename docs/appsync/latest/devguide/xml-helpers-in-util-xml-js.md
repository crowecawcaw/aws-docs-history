# XML helpers in util.xml

`util.xml` contains methods to help with XML string conversion.

## util.xml utils list

**`util.xml.toMap(String) :
 Object`**

Converts a XML string to a dictionary.

**Example 1:**

```
Input:

<?xml version="1.0" encoding="UTF-8"?>
<posts>
<post>
    <id>1</id>
    <title>Getting started with GraphQL</title>
</post>
</posts>

Output (object):

{
    "posts":{
      "post":{
        "id":1,
        "title":"Getting started with GraphQL"
      }
    }
}
```

**Example 2:**

```
Input:

<?xml version="1.0" encoding="UTF-8"?>
<posts>
<post>
  <id>1</id>
  <title>Getting started with GraphQL</title>
</post>
<post>
  <id>2</id>
  <title>Getting started with AppSync</title>
</post>
</posts>

Output (JavaScript object):

{
    "posts":{
    "post":[
        {
            "id":1,
            "title":"Getting started with GraphQL"
        },
        {
            "id":2,
            "title":"Getting started with AppSync"
        }
    ]
    }
}
```

**`util.xml.toJsonString(String, Boolean?) :
 String`**

Converts a XML string to a JSON string. This is similar to
`toMap`, except that the output is a string. This is useful if
you want to directly convert and return the XML response from an HTTP object
to JSON. You can set an optional boolean parameter to determine if you want
to string-encode the JSON.
