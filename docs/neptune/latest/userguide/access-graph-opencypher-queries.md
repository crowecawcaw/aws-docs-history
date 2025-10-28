# The Amazon Neptune OpenCypher HTTPS endpoint

###### Topics

- [OpenCypher read and write queries on the HTTPS endpoint](#access-graph-opencypher-queries-read-write "#access-graph-opencypher-queries-read-write")
- [The default OpenCypher JSON results format](#access-graph-opencypher-queries-results-simple-JSON "#access-graph-opencypher-queries-results-simple-JSON")
- [Optional HTTP trailing headers for multi-part OpenCypher responses](#optional-http-trailing-headers "#optional-http-trailing-headers")

## OpenCypher read and write queries on the HTTPS endpoint

The OpenCypher HTTPS endpoint supports read and update queries using both the
`GET` and the `POST` method. The `DELETE` and
`PUT` methods are not supported.

The following instructions walk you through connecting to the OpenCypher endpoint using the
`curl` command and HTTPS. You must follow these instructions from an Amazon EC2 instance
in the same virtual private cloud (VPC) as your Neptune DB instance.

The syntax is:

```
HTTPS://`(the server)`:`(the port number)`/openCypher
```

Here are sample read queries, one that uses `POST` and one that
uses `GET`:

1. Using `POST`:

```
curl HTTPS://`server`:`port`/openCypher \
  -d "query=MATCH (n1) RETURN n1;"
```

2. Using `GET` (the query string is URL-encoded):

```
curl -X GET \
  "HTTPS://`server`:`port`/openCypher?query=MATCH%20(n1)%20RETURN%20n1"
```

Here are sample write/update queries, one that uses `POST`
and one that uses `GET`:

1. Using `POST`:

```
curl HTTPS://`server`:`port`/openCypher \
  -d "query=CREATE (n:Person { age: 25 })"
```

2. Using `GET` (the query string is URL-encoded):

```
curl -X GET \
  "HTTPS://`server`:`port`/openCypher?query=CREATE%20(n%3APerson%20%7B%20age%3A%2025%20%7D)"
```

## The default OpenCypher JSON results format

The following JSON format is returned by default, or by setting the request header
explicitly to `Accept: application/json`. This format is designed to be easily
parsed into objects using native-language features of most libraries.

The JSON document that is returned contains one field, `results`, which
contains the query return values. The examples below show the JSON formatting for
common values.

**Value response example:**

```
{
  "results": [
    {
      "count(a)": 121
    }
  ]
}
```

**Node response example:**

```
{
  "results": [
    {
      "a": {
        "~id": "22",
        "~entityType": "node",
        "~labels": [
          "airport"
        ],
        "~properties": {
          "desc": "Seattle-Tacoma",
          "lon": -122.30899810791,
          "runways": 3,
          "type": "airport",
          "country": "US",
          "region": "US-WA",
          "lat": 47.4490013122559,
          "elev": 432,
          "city": "Seattle",
          "icao": "KSEA",
          "code": "SEA",
          "longest": 11901
        }
      }
    }
  ]
}
```

**Relationship response example:**

```
{
  "results": [
    {
      "r": {
        "~id": "7389",
        "~entityType": "relationship",
        "~start": "22",
        "~end": "151",
        "~type": "route",
        "~properties": {
          "dist": 956
        }
      }
    }
  ]
}
```

**Path response example:**

```
{
  "results": [
    {
      "p": [
        {
          "~id": "22",
          "~entityType": "node",
          "~labels": [
            "airport"
          ],
          "~properties": {
            "desc": "Seattle-Tacoma",
            "lon": -122.30899810791,
            "runways": 3,
            "type": "airport",
            "country": "US",
            "region": "US-WA",
            "lat": 47.4490013122559,
            "elev": 432,
            "city": "Seattle",
            "icao": "KSEA",
            "code": "SEA",
            "longest": 11901
          }
        },
        {
          "~id": "7389",
          "~entityType": "relationship",
          "~start": "22",
          "~end": "151",
          "~type": "route",
          "~properties": {
            "dist": 956
          }
        },
        {
          "~id": "151",
          "~entityType": "node",
          "~labels": [
            "airport"
          ],
          "~properties": {
            "desc": "Ontario International Airport",
            "lon": -117.600997924805,
            "runways": 2,
            "type": "airport",
            "country": "US",
            "region": "US-CA",
            "lat": 34.0559997558594,
            "elev": 944,
            "city": "Ontario",
            "icao": "KONT",
            "code": "ONT",
            "longest": 12198
          }
        }
      ]
    }
  ]
}
```

## Optional HTTP trailing headers for multi-part OpenCypher responses

This feature is available starting with Neptune engine release
[1.4.5.0](../../../releases/release-1.4.5.0.md "../../../releases/release-1.4.5.0.md").

The HTTP response to OpenCypher queries and updates is typically returned in multiple chunks. When failures
occur after the initial response chunks have been sent (with an HTTP status code of 200), it can be challenging
to diagnose the issue. By default, `Neptune reports such failures by appending an error message to the message
body, which may be corrupted due to the streaming nature of the response.

###### Using trailing headers

To improve error detection and diagnosis, you can enable trailing headers by including a transfer-encoding (TE)
trailers header (te: trailers)in your request. Doing this will cause Neptune to include two new header fields
within the trailing headers of the response chunks:

- `X-Neptune-Status` – contains the response code followed by a short name. For instance, in case of
  success the trailing header would be: `X-Neptune-Status: 200 OK`. In the case of failure, the response
  code would be a Neptune engine error code such as `X-Neptune-Status: 500 TimeLimitExceededException`.
- `X-Neptune-Detail` – is empty for successful requests. In the case of errors, it contains the JSON error
  message. Because only ASCII characters are allowed in HTTP header values, the JSON string is URL encoded. The error
  message is also still appended to the response message body.

For more information, see the
[MDN page about TE request headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/TE "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/TE").

###### OpenCypher trailing headers usage example

This example demonstrates how trailing headers help diagnose a query that exceeds its time limit:

```
curl --raw 'https://your-neptune-endpoint:port/openCypher' \
-H 'TE: trailers' \
-d 'query=MATCH(n) RETURN n.firstName'


Output:
< HTTP/1.1 200 OK
< transfer-encoding: chunked
< trailer: X-Neptune-Status, X-Neptune-Detail
< content-type: application/json;charset=UTF-8
<
<
{
  "results": [{
      "n.firstName": "Hossein"
    }, {
      "n.firstName": "Jan"
    }, {
      "n.firstName": "Miguel"
    }, {
      "n.firstName": "Eric"
    },
{"detailedMessage":"Operation terminated (deadline exceeded)",
"code":"TimeLimitExceededException",
"requestId":"a7e9d2aa-fbb7-486e-8447-2ef2a8544080",
"message":"Operation terminated (deadline exceeded)"}
0
X-Neptune-Status: 500 TimeLimitExceededException
X-Neptune-Detail: %7B%22detailedMessage%22%3A%22Operation+terminated+%28deadline+exceeded%29%22%2C%22code%22%3A%22TimeLimitExceededException%22%2C%22requestId%22%3A%22a7e9d2aa-fbb7-486e-8447-2ef2a8544080%22%2C%22message%22%3A%22Operation+terminated+%28deadline+exceeded%29%22%7D
```

###### Response breakdown:

The previous example shows how an OpenCypher response with trailing headers can help diagnose query failures. Here
we see four sequential parts: (1) initial headers with a 200 OK status indicating streaming begins, (2) partial (broken)
JSON results successfully streamed before the failure, (3) the appended error message showing the timeout, and (4)
trailing headers containing the final status (500 TimeLimitExceededException) and detailed error information.
