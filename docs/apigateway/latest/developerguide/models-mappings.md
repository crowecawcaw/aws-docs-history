# Mapping template transformations for REST APIs in API Gateway

A mapping template transformation uses a mapping template to modify your integration request or integration
response. A _mapping template_ is a script expressed in [Velocity Template Language (VTL)](https://velocity.apache.org/engine/devel/vtl-reference.html "https://velocity.apache.org/engine/devel/vtl-reference.html") and
applied to a payload using [JSONPath](https://goessner.net/articles/JsonPath/ "https://goessner.net/articles/JsonPath/") based on the
`Content-type` header. You use mapping templates when you use mapping template transformations. This section describes conceptual
information related to mapping templates.

The following diagram shows the request lifecycle for a `POST /pets` resource that has an integration
with a PetStore integration endpoint. In this API, a user sends data about a pet and the
integration endpoint returns the adoption fee associated with a pet. In this request lifecycle, mapping template transformations filter the
request body to the integration endpoint and filter the response body from the integration endpoint.

![Example request lifecycle](images/mapping-template-transforms.png)
The following sections explain the request and response lifecycle.

## Method request and integration request

In the previous example, if this is the request body sent to the method request:

```
POST /pets
    HTTP/1.1
    Host:abcd1234.us-west-2.amazonaws.com
    Content-type: application/json

  {
    "id": 1,
    "type": "dog",
    "Age": 11,
  }

```

This request body is not in the correct format to be used by the integration endpoint, so API Gateway performs a
mapping template transformation. API Gateway only performs a mapping template transformation because there is a mapping
template defined for the Content-Type `application/json`. If you don't define a mapping template for
the Content-Type, by default, API Gateway passes the body through the integration request to the integration endpoint.
To modify this behavior, see [Method request behavior for payloads without mapping
templates for REST APIs in API Gateway](integration-passthrough-behaviors.md "integration-passthrough-behaviors.md").

The following mapping template transforms the method request data in the integration request before it's sent to
the integration endpoint:

```
#set($inputRoot = $input.path('$'))
  {
    "dogId" : "dog_"$elem.id,
    "Age": $inputRoot.Age
  }
```

1. The `$inputRoot` variable represents the root
   object in the original JSON data from the previous section. Directives begin with the `#` symbol.
2. The `dog` is a concatenation of the user's `id` and a string value.
3. `Age` is from the method request body.

Then, the following output is forwarded to the integration endpoint:

```
{
    "dogId" : "dog_1",
    "Age": 11
  }
```

## Integration response and method response

After the successful request to the integration endpoint, the endpoint sends a response to API Gateway's integration
response. The following is the example output data from the integration endpoint:

```
{
    "dogId" : "dog_1",
    "adoptionFee": 19.95,
}
```

The method response expects a different payload than what is returned by the integration response. API Gateway
performs a mapping template transformation. API Gateway only performs a mapping template transformation because there is
a mapping template defined for the Content-Type `application/json`. If you don't define a mapping
template for the Content-Type, by default, API Gateway passes the body through the integration response to the method
response. To modify this behavior, see [Method request behavior for payloads without mapping
templates for REST APIs in API Gateway](integration-passthrough-behaviors.md "integration-passthrough-behaviors.md").

```
#set($inputRoot = $input.path('$'))
  {
    "adoptionFee" : $inputRoot.adoptionFee,
  }

```

The following output is sent to the method response:

```
{"adoptionFee": 19.95}
```

This completes the example mapping template transformation. We recommend that when possible, instead of using
mapping template transformations, you use a proxy integration to transform your data. For more information, see [Choose an API Gateway API integration
type](api-gateway-api-integration-types.md "api-gateway-api-integration-types.md").
