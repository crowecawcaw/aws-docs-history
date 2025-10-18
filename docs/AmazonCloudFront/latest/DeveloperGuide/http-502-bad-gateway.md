# HTTP 502 status code (Bad Gateway)

CloudFront returns a HTTP 502 status code (Bad Gateway) when CloudFront wasn't able to serve
 the requested object because it couldn't connect to the origin server. 

If you're using Lambda@Edge, the issue might be a Lambda validation error. If you
 receive an HTTP 502 error with the `NonS3OriginDnsError` error code,
 there's likely a DNS configuration problem that's preventing CloudFront from connecting to
 the origin.

###### Topics

* [SSL/TLS negotiation failure between
 CloudFront and a custom origin server](#ssl-negotitation-failure "#ssl-negotitation-failure")
* [Origin
 is not responding with supported ciphers/protocols](#origin-not-responding-with-supported-ciphers-protocols "#origin-not-responding-with-supported-ciphers-protocols")
* [SSL/TLS certificate on the origin is
 expired, invalid, self-signed, or the certificate chain is in the wrong
 order](#ssl-certificate-expired "#ssl-certificate-expired")
* [Origin is not
 responding on specified ports in origin settings](#origin-not-responding-on-specified-ports "#origin-not-responding-on-specified-ports")
* [Lambda validation
 error](#http-502-lambda-validation-error "#http-502-lambda-validation-error")
* [CloudFront function
 validation error](#http-502-cloudfront-function-validation-error "#http-502-cloudfront-function-validation-error")
* [DNS error
 (NonS3OriginDnsError)](#http-502-dns-error "#http-502-dns-error")
* [Application Load Balancer origin 502 error](#cloudfront-alb-502-error "#cloudfront-alb-502-error")
* [API Gateway origin 502
 error](#cloudfront-api-gateway-502-error "#cloudfront-api-gateway-502-error")

## SSL/TLS negotiation failure between
 CloudFront and a custom origin server


If you use a custom origin that requires HTTPS between CloudFront and your origin,
 mismatched domain names might cause errors. The SSL/TLS certificate on your
 origin *must* include a domain name that matches either the
 **Origin Domain** that you specified for the CloudFront
 distribution or the `Host` header of the origin request.


If the domain names don't match, the SSL/TLS handshake fails, and CloudFront returns
 an HTTP status code 502 (Bad Gateway) and sets the `X-Cache` header
 to `Error from cloudfront`.


To determine whether domain names in the certificate match the
 **Origin Domain** in the distribution or the
 `Host` header, you can use an online SSL checker or OpenSSL. If
 the domain names don't match, you have two options:



* Get a new SSL/TLS certificate that includes the applicable domain
 names. 


If you use AWS Certificate Manager (ACM), see [Requesting a public certificate](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html "https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html") in the
 *AWS Certificate Manager User Guide* to request a new
 certificate.
* Change the distribution configuration so CloudFront no longer tries to use
 SSL to connect with your origin.

### Online SSL checker


To find an SSL test tool, search the internet for "online ssl checker."
 Typically, you specify the name of your domain, and the tool returns a
 variety of information about your SSL/TLS certificate. Confirm that the
 certificate contains your domain name in the **Common
 Name** or **Subject Alternative Names**
 fields.


### OpenSSL


To help troubleshoot HTTP 502 errors from CloudFront, you can use OpenSSL to try
 to make an SSL/TLS connection to your origin server. If OpenSSL is not able
 to make a connection, that can indicate a problem with your origin server's
 SSL/TLS configuration. If OpenSSL is able to make a connection, it returns
 information about the origin server's certificate, including the
 certificate's common name (`Subject CN` field) and subject
 alternative name (`Subject Alternative Name` field).


Use the following OpenSSL command to test the connection to your origin
 server (replace `origin domain` with your origin
 server's domain name, such as example.com):


`openssl s_client -connect `origin domain
 name`:443`


If the following are true:



* Your origin server supports multiple domain names with multiple
 SSL/TLS certificates
* Your distribution is configured to forward the `Host`
 header to the origin

Then add the `-servername` option to the OpenSSL command, as in
 the following example (replace `CNAME` with the
 CNAME that's configured in your distribution):


`openssl s_client -connect `origin domain
 name`:443 -servername
 `CNAME``


## Origin
 is not responding with supported ciphers/protocols


CloudFront connects to origin servers using ciphers and protocols. For a list of the
 ciphers and protocols that CloudFront supports, see [Supported
 protocols and ciphers between CloudFront and the origin](secure-connections-supported-ciphers-cloudfront-to-origin.md "secure-connections-supported-ciphers-cloudfront-to-origin.md"). If
 your origin does not respond with one of these ciphers or protocols in the
 SSL/TLS exchange, CloudFront fails to connect. You can validate that your origin
 supports the ciphers and protocols by using an online tool such as [SSL Labs](https://www.ssllabs.com/ssltest "https://www.ssllabs.com/ssltest"). Type the domain name
 of your origin in the **Hostname** field, and then choose
 **Submit**. Review the **Common
 names** and **Alternative names**
 fields from the test to see if they match your origin's domain name. After the
 test is finished, find the **Protocols** and **Cipher
 Suites** sections in the test results to see which ciphers or
 protocols are supported by your origin. Compare them with the list of [Supported
 protocols and ciphers between CloudFront and the origin](secure-connections-supported-ciphers-cloudfront-to-origin.md "secure-connections-supported-ciphers-cloudfront-to-origin.md").


## SSL/TLS certificate on the origin is
 expired, invalid, self-signed, or the certificate chain is in the wrong
 order


If the origin server returns the following, CloudFront drops the TCP connection,
 returns HTTP status code 502 (Bad Gateway), and sets the `X-Cache`
 header to `Error from cloudfront`:



* An expired certificate
* Invalid certificate
* Self-signed certificate
* Certificate chain in the wrong order

###### Note

If the full chain of certificates, including the intermediate certificate,
 is not present, CloudFront drops the TCP connection.


For information about installing an SSL/TLS certificate on your custom origin
 server, see [Require HTTPS for communication
 between CloudFront and your custom origin](using-https-cloudfront-to-custom-origin.md "using-https-cloudfront-to-custom-origin.md").


## Origin is not
 responding on specified ports in origin settings


When you create an origin on your CloudFront distribution, you can set the ports
 that CloudFront connects to the origin with for HTTP and HTTPS traffic. By default,
 these are TCP 80/443. You have the option to modify these ports. If your origin
 is rejecting traffic on these ports for any reason, or if your backend server
 isn't responding on the ports, CloudFront will fail to connect.


To troubleshoot these issues, check any firewalls running in your
 infrastructure and validate that they are not blocking the supported IP ranges.
 For more information, see [AWS IP address ranges](https://docs.aws.amazon.com/vpc/latest/userguide/aws-ip-ranges.html "https://docs.aws.amazon.com/vpc/latest/userguide/aws-ip-ranges.html") in the
 *Amazon VPC User Guide*. Additionally, verify whether your web
 server is running on the origin.


## Lambda validation
 error


If you're using Lambda@Edge, an HTTP 502 status code can indicate that your
 Lambda function response was incorrectly formed or included invalid content. For
 more information about troubleshooting Lambda@Edge errors, see [Test and debug Lambda@Edge
 functions](lambda-edge-testing-debugging.md "lambda-edge-testing-debugging.md").


## CloudFront function
 validation error


If you're using CloudFront functions, an HTTP 502 status code can indicate that the
 CloudFront function is trying to add, delete, or change a read-only header. This error
 does not show up during testing, but will show up after you deploy the function
 and run the request. To resolve this error, check and update your CloudFront function.
 For more information, see [Update functions](update-function.md "update-function.md").


## DNS error
 (`NonS3OriginDnsError`)


An HTTP 502 error with the `NonS3OriginDnsError` error code
 indicates that there's a DNS configuration problem that prevents CloudFront from
 connecting to the origin. If you get this error from CloudFront, make sure that the
 origin's DNS configuration is correct and working.


When CloudFront receives a request for an object that's expired or is not in its
 cache, it makes a request to the origin to get the object. To make a successful
 request to the origin, CloudFront performs a DNS resolution on the origin domain. If
 the DNS service for your domain is experiencing issues, CloudFront can't resolve the
 domain name to get the IP address, which results in an HTTP 502 error
 (`NonS3OriginDnsError`). To fix this problem, contact your DNS
 provider, or, if you are using Amazon Route 53, see [Why can't I access my website that uses Route 53 DNS services?](https://aws.amazon.com/premiumsupport/knowledge-center/route-53-dns-website-unreachable/ "https://aws.amazon.com/premiumsupport/knowledge-center/route-53-dns-website-unreachable/")


To further troubleshoot this issue, ensure that the [authoritative name servers](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-concepts.html#route-53-concepts-authoritative-name-server "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-concepts.html#route-53-concepts-authoritative-name-server") of your origin's
 root domain or zone apex (such as `example.com`) are functioning
 correctly. You can use the following commands to find the name servers for your
 apex origin, with a tool such as [dig](https://en.wikipedia.org/wiki/Dig_(command) "https://en.wikipedia.org/wiki/Dig_(command)") or [nslookup](https://en.wikipedia.org/wiki/Nslookup "https://en.wikipedia.org/wiki/Nslookup"):



```
dig `OriginAPEXDomainName` NS +short
```


```
nslookup -query=NS `OriginAPEXDomainName`
```

When you have the names of your name servers, use the following commands to
 query the domain name of your origin against them to make sure that each
 responds with an answer:



```
dig `OriginDomainName` `@NameServer`
```


```
nslookup `OriginDomainName` `NameServer`
```

###### Important

Make sure that you perform this DNS troubleshooting using a computer
 that's connected to the public internet. CloudFront resolves the origin domain
 using public DNS on the internet, so it's important to troubleshoot in a
 similar context.


If your origin is a subdomain whose DNS authority is delegated to a different
 name server than the root domain, make sure that the name server
 (`NS`) and start of authority (`SOA`) records are
 configured correctly for the subdomain. You can check for these records using
 commands similar to the preceding examples.


For more information about DNS, see [Domain Name System (DNS) concepts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-concepts.html#route-53-concepts-domain-name-system-dns "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-concepts.html#route-53-concepts-domain-name-system-dns") in the Amazon Route 53
 documentation.


## Application Load Balancer origin 502 error


If you use Application Load Balancer as your origin and receive a 502 error, see [How do I troubleshoot Application Load Balancer HTTP 502 errors?](https://repost.aws/knowledge-center/elb-alb-troubleshoot-502-errors "https://repost.aws/knowledge-center/elb-alb-troubleshoot-502-errors").


## API Gateway origin 502
 error


If you use API Gateway and receive a 502 error, see [How do I
 resolve HTTP 502 errors from API Gateway REST APIs with Lambda proxy
 integration?](https://repost.aws/knowledge-center/malformed-502-api-gateway "https://repost.aws/knowledge-center/malformed-502-api-gateway").
