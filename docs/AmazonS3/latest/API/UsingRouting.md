# Request routing

Programs that make requests against buckets created using the
 [CreateBucket](API_CreateBucket.md "API_CreateBucket.md")
 API that include a
 [CreateBucketConfiguration](API_CreateBucketConfiguration.md "API_CreateBucketConfiguration.md")
 must support redirects. Additionally, some clients
 that do not respect DNS TTLs might encounter issues.

This section describes routing and DNS issues to consider when designing your service or
 application for use with Amazon S3.


## Request redirection and the REST API


Amazon S3 uses the Domain Name System (DNS) to route requests to facilities that can process
 them. This system works effectively, but temporary routing errors can occur. If a request
 arrives at the wrong Amazon S3 location, Amazon S3 responds with a temporary redirect that tells the
 requester to resend the request to a new endpoint. If a request is incorrectly formed, Amazon S3
 uses permanent redirects to provide direction on how to perform the request
 correctly.


###### Important

To use this feature, you must have an application that can handle Amazon S3 redirect
 responses. The only exception is for applications that work exclusively with buckets
 that were created without `<CreateBucketConfiguration>`. For more
 information about location constraints, see [Accessing and listing an Amazon S3 bucket](../userguide/access-bucket-intro.md "../userguide/access-bucket-intro.md") .

For all Regions that launched after March 20, 2019, if a request arrives at the wrong Amazon S3
 location, Amazon S3 returns an HTTP 400 Bad Request error.

For more information about enabling or disabling an AWS Region, 
 see [AWS Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html "https://docs.aws.amazon.com/general/latest/gr/rande.html")
 in the *AWS General Reference*.


###### Topics

* [DNS routing](#DNSRouting "#DNSRouting")
* [Temporary request redirection](#TemporaryRedirection "#TemporaryRedirection")
* [Permanent request redirection](#RedirectsPermanentRedirection "#RedirectsPermanentRedirection")
* [Request redirection examples](#redirect-examples "#redirect-examples")

### DNS routing


DNS routing routes requests to appropriate Amazon S3 facilities. The following figure and
 procedure show an example of DNS routing.



![Diagram showing steps that occur when a DNS server routes requests from the client to facility B.](../../../images/AmazonS3/latest/API/images/DNS_virthost.png)

###### DNS routing request steps

1. The client makes a DNS request to get an object stored on Amazon S3.
2. The client receives one or more IP addresses for facilities that can process
 the request. In this example, the IP address is for Facility B.
3. The client makes a request to Amazon S3 Facility B.
4. Facility B returns a copy of the object to the client.

### Temporary request redirection


A temporary redirect is a type of error response that signals to the requester that
 they should resend the request to a different endpoint. Due to the distributed nature of
 Amazon S3, requests can be temporarily routed to the wrong facility. This is most likely to
 occur immediately after buckets are created or deleted.


For example, if you create a new bucket and immediately make a request to the bucket,
 you might receive a temporary redirect, depending on the location constraint of the
 bucket. If you created the bucket in the US East (N. Virginia) AWS Region, you will not see
 the redirect because this is also the default Amazon S3 endpoint.


However, if the bucket is created in any other Region, any requests for the bucket go
 to the default endpoint while the bucket's DNS entry is propagated. The default endpoint
 redirects the request to the correct endpoint with an HTTP 302 response. Temporary
 redirects contain a URI to the correct facility, which you can use to immediately resend
 the request.


###### Important

Don't reuse an endpoint provided by a previous redirect response. It might appear
 to work (even for long periods of time), but it might provide unpredictable results
 and will eventually fail without notice.


The following figure and procedure shows an example of a temporary redirect.



![Diagram showing steps that occur when a client sends a request to B and is redirected to C.](../../../images/AmazonS3/latest/API/images/DNS_virthost_redirect.png)

###### Temporary request redirection steps

1. The client makes a DNS request to get an object stored on Amazon S3.
2. The client receives one or more IP addresses for facilities that can process
 the request.
3. The client makes a request to Amazon S3 Facility B.
4. Facility B returns a redirect indicating the object is available from Location
 C.
5. The client resends the request to Facility C.
6. Facility C returns a copy of the object.

### Permanent request redirection


A permanent redirect indicates that your request addressed a resource inappropriately.
 For example, permanent redirects occur if you use a path-style request to access a
 bucket that was created using `<CreateBucketConfiguration>`. For more
 information, see [Accessing and listing an Amazon S3 bucket](../userguide/access-bucket-intro.md "../userguide/access-bucket-intro.md") .


To help you find these errors during development, this type of redirect does not
 contain a Location HTTP header that allows you to automatically follow the request to
 the correct location. Consult the resulting XML error document for help using the
 correct Amazon S3 endpoint.


### Request redirection examples


The following are examples of temporary request redirection responses.


#### REST API temporary
 redirect response



```

HTTP/1.1 307 Temporary Redirect
Location: http://awsexamplebucket1.s3-gztb4pa9sq.amazonaws.com/photos/puppy.jpg?rk=e2c69a31
Content-Type: application/xml
Transfer-Encoding: chunked
Date: Fri, 12 Oct 2007 01:12:56 GMT
Server: AmazonS3

<?xml version="1.0" encoding="UTF-8"?>
<Error>
  <Code>TemporaryRedirect</Code>
  <Message>Please re-send this request to the specified temporary endpoint.
  Continue to use the original request endpoint for future requests.</Message>
  <Endpoint>awsexamplebucket1.s3-gztb4pa9sq.amazonaws.com</Endpoint>
</Error>

```

#### SOAP API temporary
 redirect response


###### Note


 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on October 31, 2025. We recommend that you use either the REST API or the AWS SDKs.
 



```
<soapenv:Body>
  <soapenv:Fault>
    <Faultcode>soapenv:Client.TemporaryRedirect</Faultcode>
    <Faultstring>Please re-send this request to the specified temporary endpoint.
    Continue to use the original request endpoint for future requests.</Faultstring>
    <Detail>
      <Bucket>images</Bucket>
      <Endpoint>s3-gztb4pa9sq.amazonaws.com</Endpoint>
    </Detail>
  </soapenv:Fault>
</soapenv:Body>

```

## DNS considerations


 One of the design requirements of Amazon S3 is extremely high availability. One of the ways we
 meet this requirement is by updating the IP addresses associated with the Amazon S3 endpoint in DNS
 as needed. These changes are automatically reflected in short-lived clients, but not in some
 long-lived clients. Long-lived clients will need to take special action to re-resolve the Amazon S3
 endpoint periodically to benefit from these changes. For more information about virtual machines
 (VMs), refer to the following: 



* For Java, Sun's JVM caches DNS lookups forever by default; go to the "InetAddress
 Caching" section of [the InetAddress
 documentation](https://docs.oracle.com/javase/9/docs/api/java/net/InetAddress.html "https://docs.oracle.com/javase/9/docs/api/java/net/InetAddress.html") for information on how to change this behavior.
* For PHP, the persistent PHP VM that runs in the most popular deployment configurations
 caches DNS lookups until the VM is restarted. Go to [the getHostByName PHP
 docs.](http://us2.php.net/manual/en/function.gethostbyname.php "http://us2.php.net/manual/en/function.gethostbyname.php")
