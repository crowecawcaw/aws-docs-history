# Testing CORS

To test your CORS configuration, a CORS preflight request can be sent with the `OPTIONS` method so that the server can respond if it is acceptable to send the request. When Amazon S3 receives a preflight request, S3 evaluates the CORS configuration for the bucket and uses the first `CORSRule` rule that matches the incoming request to enable a cross-origin request.
For a rule to match, the following conditions must be met:

- The `Origin` header in a CORS request to your bucket must match the origins in the `AllowedOrigins` element in your CORS configuration.
- The HTTP methods that are specified in the `Access-Control-Request-Method` in a CORS request to your bucket must match the method or methods listed in the `AllowedMethods` element in your CORS configuration.
- The headers listed in the `Access-Control-Request-Headers` header in a preflight request must match the headers in the `AllowedHeaders` element in your CORS configuration.
  The following is an example of a CORS configuration. To create a CORS Configuration, see [Configuring CORS](enabling-cors-examples.md "enabling-cors-examples.md"). For more examples of a CORS configuration, see
  [Elements of a CORS configuration](ManageCorsUsing.md "ManageCorsUsing.md").

For guidance on configuring and troubleshooting CORS rules, see [How do I configure CORS in Amazon S3 and confirm the CORS rules using cURL?](https://repost.aws/knowledge-center/s3-configure-cors "https://repost.aws/knowledge-center/s3-configure-cors") in the AWS re:Post Knowledge Center.

JSON

```
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET",
            "PUT",
            "POST",
            "DELETE"
        ],
        "AllowedOrigins": [
            "http://www.example1.com"
        ],
        "ExposeHeaders":  [
             "x-amz-meta-custom-header"
        ]

    }
]
```

To test the CORS configuration, you can send a preflight `OPTIONS` check by using the
following CURL command. CURL is a command-line tool that can be used to interact with S3.
For more information, see [CURL](https://curl.se/ "https://curl.se/").

```
 curl -v -X OPTIONS \
  -H "Origin: http://www.example1.com" \
  -H "Access-Control-Request-Method: PUT" \
  -H "Access-Control-Request-Headers: Authorization" \
  -H "Access-Control-Expose-Headers: x-amz-meta-custom-header"\
     "http://bucket_name.s3.amazonaws.com/object_prefix_name"
```

In the above example, the `curl -v -x OPTIONS` command is used to send a
preflight request to S3 to inquire if it is allowed by S3 to send a `PUT` request
on an object from the cross origin `http://www.example1.com`. The headers
`Access-Control-Request-Headers` and
`Access-Control-Expose-Headers` are optional.

- In response to the `Access-Control-Request-Method` header in the
  preflight `OPTIONS` request, Amazon S3 returns the list of allowed
  methods if the requested methods match.
- In response to the `Access-Control-Request-Headers` header in the
  preflight `OPTIONS` request, Amazon S3 returns the list of allowed
  headers if the requested headers match.
- In response to the `Access-Control-Expose-Headers` header in the preflight `OPTIONS` request, Amazon S3 returns a list of allowed headers if the requested headers match the allowed headers that can be accessed by scripts running in the browser.

###### Note

When sending a preflight request, if any of the CORS request headers are not allowed, none of the response CORS headers are returned.

In response to this preflight `OPTIONS` request, you will receive a
`200 OK` response. For common error codes received when testing CORS and more
information to solve CORS related issues, see [Troubleshooting CORS](cors-troubleshooting.md "cors-troubleshooting.md").

```
< HTTP/1.1 200 OK
< Date: Fri, 12 Jul 2024 00:23:51 GMT
< Access-Control-Allow-Origin: http://www.example1.com
< Access-Control-Allow-Methods: GET, PUT, POST, DELETE
< Access-Control-Allow-Headers: Authorization
< Access-Control-Expose-Headers: x-amz-meta-custom-header
< Access-Control-Allow-Credentials: true
< Vary: Origin, Access-Control-Request-Headers, Access-Control-Request-Method
< Server: AmazonS3
< Content-Length: 0
```
