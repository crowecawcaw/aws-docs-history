# Examples using variables for mapping template transformations for API Gateway

The following examples show how to use `$context`, `input`, and `util`
variables in mapping templates. You can use a mock integration or a Lambda non-proxy integration that returns the
input event back to API Gateway. For a list of all supported variables for data transformations, see
[Variables for data transformations for API Gateway](api-gateway-mapping-template-reference.md "api-gateway-mapping-template-reference.md").

## Example 1: Pass multiple `$context`

variables to the integration endpoint

The following example shows a mapping template that maps incoming
`$context` variables to backend variables with slightly different names
in an integration request payload:

```
{
    "stage" : "$context.stage",
    "request_id" : "$context.requestId",
    "api_id" : "$context.apiId",
    "resource_path" : "$context.resourcePath",
    "resource_id" : "$context.resourceId",
    "http_method" : "$context.httpMethod",
    "source_ip" : "$context.identity.sourceIp",
    "user-agent" : "$context.identity.userAgent",
    "account_id" : "$context.identity.accountId",
    "api_key" : "$context.identity.apiKey",
    "caller" : "$context.identity.caller",
    "user" : "$context.identity.user",
    "user_arn" : "$context.identity.userArn"
}
```

The output of this mapping template should look like the following:

```
{
  stage: 'prod',
  request_id: 'abcdefg-000-000-0000-abcdefg',
  api_id: 'abcd1234',
  resource_path: '/',
  resource_id: 'efg567',
  http_method: 'GET',
  source_ip: '192.0.2.1',
  user-agent: 'curl/7.84.0',
  account_id: '111122223333',
  api_key: 'MyTestKey',
  caller: 'ABCD-0000-12345',
  user: 'ABCD-0000-12345',
  user_arn: 'arn:aws:sts::111122223333:assumed-role/Admin/carlos-salazar'
}
```

One of the variables is an API key. This example assumes that the method requires an API key.

## Example 2: Pass all request parameters to

the integration endpoint via a JSON payload

The following example passes all request parameters, including
`path`, `querystring`, and `header` parameters, through to
the integration endpoint via a JSON payload:

```
#set($allParams = $input.params())
{
  "params" : {
    #foreach($type in $allParams.keySet())
    #set($params = $allParams.get($type))
    "$type" : {
      #foreach($paramName in $params.keySet())
      "$paramName" : "$util.escapeJavaScript($params.get($paramName))"
      #if($foreach.hasNext),#end
      #end
    }
    #if($foreach.hasNext),#end
    #end
  }
}
```

If a request has the following input parameters:

- A path parameter named `myparam`
- Query string parameters `querystring1=value1,value2`
- Headers `"header1" : "value1"`.

The output of this mapping template should look like the following:

```
{"params":{"path":{"example2":"myparamm"},"querystring":{"querystring1":"value1,value2"},"header":{"header1":"value1"}}}

```

## Example 3: Pass a subsection of a method request to the

integration endpoint

The following example uses the input parameter `name` to retrieve only the `name`
parameter and the input parameter `input.json('$')` to retrieve the entire body of the method
request:

```
{
    "name" : "$input.params('name')",
    "body" : $input.json('$')
}
```

For a request that includes the query string parameters `name=Bella&type=dog` and the following body:

```
{
    "Price" : "249.99",
    "Age": "6"
}
```

The output of this mapping template should look like the following:

```
{
    "name" : "Bella",
    "body" : {"Price":"249.99","Age":"6"}
}
```

This mapping template removes the query string parameter `type=dog`.

If the JSON input contains unescaped characters that cannot be parsed by
JavaScript, API Gateway might return a 400 response. Apply
`$util.escapeJavaScript($input.json('$'))` to ensure the
JSON input can be parsed properly.

The previous example with `$util.escapeJavaScript($input.json('$'))` applied is as follows:

```
{
    "name" : "$input.params('name')",
    "body" : "$util.escapeJavaScript($input.json('$'))"
}
```

In this case, the output of this mapping template should look like the following:

```
{
    "name" : "Bella",
    "body": {"Price":"249.99","Age":"6"}
}
```

## Example 4: Use JSONPath expression to pass a subsection of

a method request to the integration endpoint

The following example uses the JSONPath expressions to retrieve only the input parameter
`name` and the `Age` from the request body:

```
{
    "name" : "$input.params('name')",
    "body" : $input.json('$.Age')
}
```

For a request that includes the query string parameters `name=Bella&type=dog` and the following body:

```
{
    "Price" : "249.99",
    "Age": "6"
}
```

The output of this mapping template should look like the following:

```
{
    "name" : "Bella",
    "body" : "6"
}
```

This mapping template removes the query string parameter `type=dog` and the
`Price` field from the body.

If a method request payload contains unescaped characters that cannot be parsed
by JavaScript, API Gateway might return a `400` response. Apply
`$util.escapeJavaScript()` to ensure the
JSON input can be parsed properly.

The previous example with `$util.escapeJavaScript($input.json('$.Age'))` applied is as follows:

```
{
    "name" : "$input.params('name')",
    "body" : "$util.escapeJavaScript($input.json('$.Age'))"
}
```

In this case, the output of this mapping template should look like the following:

```
{
    "name" : "Bella",
    "body": "\"6\""
}
```

## Example 5: Use a JSONPath expression to pass information

about a method request to the integration endpoint

The following example uses `$input.params()`, `$input.path()`, and
`$input.json()` to send information about a method request to the integration endpoint. This mapping
template uses the `size()` method to provide the number of elements in a list.

```
{
    "id" : "$input.params('id')",
    "count" : "$input.path('$.things').size()",
    "things" : $input.json('$.things')
}
```

For a request that includes the path parameter `123` and the following body:

```
{
      "things": {
            "1": {},
            "2": {},
            "3": {}
      }
}
```

The output of this mapping template should look like the following:

```
{"id":"123","count":"3","things":{"1":{},"2":{},"3":{}}}
```

If a method request payload contains unescaped characters that cannot be parsed
by JavaScript, API Gateway might return a `400` response. Apply
`$util.escapeJavaScript()` to ensure the
JSON input can be parsed properly.

The previous example with `$util.escapeJavaScript($input.json('$.things'))` applied is as follows:

```
{
     "id" : "$input.params('id')",
     "count" : "$input.path('$.things').size()",
     "things" : "$util.escapeJavaScript($input.json('$.things'))"
}
```

The output of this mapping template should look like the following:

```
{"id":"123","count":"3","things":"{\"1\":{},\"2\":{},\"3\":{}}"}
```
