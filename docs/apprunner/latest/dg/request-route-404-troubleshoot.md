# HTTP/HTTPS request routing error

This section covers how you can troubleshoot and resolve errors that you might run into when routing HTTP/HTTPS traffic to your App Runner service endpoints.

## 404 Not found error when sending HTTP/HTTPS traffic to App Runner service endpoints

- Verify that the `Host Header` is pointing to the service URL in the HTTP request as App Runner uses the host header information to route requests.
  Most clients, like `cURL`, and web browsers automatically point the host header to the service URL. If your client doesn't set the
  service URL as the `Host Header`, you receive a `404 Not Found` error.

###### Example Incorrect host header

```
$ ~ curl -I -H "host: foobar.com" https://testservice.awsapprunner.com/
HTTP/1.1 404 Not Found
transfer-encoding: chunked
```

###### Example Correct host header

```
$ ~ curl -I -H "host: testservice.awsapprunner.com" https://testservice.awsapprunner.com/
HTTP/1.1 200 OK
content-length: 11772
content-type: text/html; charset=utf-8
```

- Verify that your client is correctly setting the server name indicator (SNI) for requests routing to public or private services.
  For TLS termination and request routing, App Runner uses the SNI set in HTTPS connection.
