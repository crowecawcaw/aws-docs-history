# RPC Responses

Amazon Route 53 responses are just standard HTTP responses. Some of the Route 53 actions return special information specific to Route 53
in the form of an HTTP header or JSON in the body of the response. The specific details are covered in the documentation for the action.

Each response contains a request ID that you can use if you need to troubleshoot a request with Route 53. The ID is contained in an HTTP header
called `x-amz-request-id`. An example of a request ID is `647cd254-e0d1-44a9-af61-1d6d86ea6b77`.

The following example shows a response to a request to check the availability of a specified domain name. The
`Availability` element indicates whether the domain that you specified in the request is available.

###### Example Response

```
HTTP/1.1 200
Content-Length:number of characters in the JSON string
{
   "Availability":"308c56712-faa4-40fe-94c8-b423069de3f6"
}
```

## Error Responses

If an RPC request results in an error, the HTTP response has:

- An error document in JSON format as the response body
- Content-Type header: text/xml
- An appropriate 3xx, 4xx, or 5xx HTTP status code

Following is an example of the JSON error document in an RPC error response.

```
{
 "__type": "com.amazon.coral.service#UnrecognizedClientException",
 "message": "The security token included in the request is invalid."
}
```
