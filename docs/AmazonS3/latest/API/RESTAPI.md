# Making requests using the REST API

This section contains information on how to make requests to Amazon S3 endpoints by using the
 REST API. For a list of Amazon S3 endpoints, see
 [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/s3.html "https://docs.aws.amazon.com/general/latest/gr/s3.html") in the
 *AWS General Reference*.

## Constructing S3 hostnames for REST API
 requests


Amazon S3 endpoints follow the structure shown below:



```
s3.`Region`.amazonaws.com
```

Amazon S3 access points endpoints and dual-stack endpoints also follow the
 standard structure:



* **Amazon S3 access points**
 ‐`s3-accesspoint.`Region`.amazonaws.com`
* **Dual-stack** ‐
 `s3.dualstack.`Region`.amazonaws.com`

For a complete list of Amazon S3 Regions and endpoints, see [Amazon S3 endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html "https://docs.aws.amazon.com/general/latest/gr/s3.html") in the *Amazon Web Services General Reference*.


## Virtual hosted‐style and path‐style
 requests


When making requests by using the REST API, you can use virtual hosted–style or
 path-style URIs for the Amazon S3 endpoints. For more information, see [Path-style requests](../userguide/VirtualHosting.md#path-style-access "../userguide/VirtualHosting.md#path-style-access") .


###### Example Virtual hosted–Style request

Following is an example of a virtual hosted–style request to delete the
 `puppy.jpg` file from the bucket named
 `examplebucket` in the US West (Oregon) Region. For more information about
 virtual hosted-style requests, see [Path-style requests](../userguide/VirtualHosting.md#virtual-hosted-style-access "../userguide/VirtualHosting.md#virtual-hosted-style-access") .


```
DELETE /puppy.jpg HTTP/1.1
Host: examplebucket.s3.us-west-2.amazonaws.com
Date: Mon, 11 Apr 2016 12:00:00 GMT
x-amz-date: Mon, 11 Apr 2016 12:00:00 GMT
Authorization: `authorization string`
```

###### Example Path-style request

Following is an example of a path-style version of the same request.


```
DELETE /examplebucket/puppy.jpg HTTP/1.1
Host: s3.us-west-2.amazonaws.com
Date: Mon, 11 Apr 2016 12:00:00 GMT
x-amz-date: Mon, 11 Apr 2016 12:00:00 GMT
Authorization: `authorization string`
		
```
You will receive an HTTP response code 307 Temporary Redirect error 
 and a message indicating what the correct URI is for your resource if you try 
 to access a bucket outside the US East (N. Virginia) region with path-style syntax that uses either of the following:
 

For more information about path-style requests, see [Path-style requests](../userguide/VirtualHosting.md#path-style-access "../userguide/VirtualHosting.md#path-style-access") .

###### Important

Update (September 23, 2020) – To make sure that customers have the time that they need to transition to virtual-hosted–style URLs, 
we have decided to delay the deprecation of path-style URLs. For more information, 
see [Amazon S3 Path Deprecation Plan – The Rest of the Story](https://aws.amazon.com/blogs/aws/amazon-s3-path-deprecation-plan-the-rest-of-the-story/ "https://aws.amazon.com/blogs/aws/amazon-s3-path-deprecation-plan-the-rest-of-the-story/") in the *AWS News Blog*.


## Making requests to dual-stack endpoints by using the REST
 API


When using the REST API, you can directly access a dual-stack endpoint by using a virtual
 hosted–style or a path style endpoint name (URI). All Amazon S3 dual-stack endpoint
 names include the region in the name. Unlike the standard IPv4-only endpoints, both
 virtual hosted–style and a path-style endpoints use region-specific endpoint
 names. 


###### Example Virtual hosted–Style dual-stack endpoint request

You can use a virtual hosted–style endpoint in your REST request as shown in the
 following example that retrieves the `puppy.jpg` object from
 the bucket named `examplebucket` in the US West (Oregon)
 Region.


```
GET /puppy.jpg HTTP/1.1
Host: examplebucket.s3.dualstack.us-west-2.amazonaws.com
Date: Mon, 11 Apr 2016 12:00:00 GMT
x-amz-date: Mon, 11 Apr 2016 12:00:00 GMT
Authorization: `authorization string`
```

###### Example Path-style dual-stack endpoint request

Or you can use a path-style endpoint in your request as shown in the following
 example.


```
GET /examplebucket/puppy.jpg HTTP/1.1
Host: s3.dualstack.us-west-2.amazonaws.com
Date: Mon, 11 Apr 2016 12:00:00 GMT
x-amz-date: Mon, 11 Apr 2016 12:00:00 GMT
Authorization: `authorization string`
```

For more information about dual-stack endpoints,
 see [Using Amazon S3 dual-stack endpoints](dual-stack-endpoints.md "dual-stack-endpoints.md").


For more information about making requests using the REST API, see the topics below.

###### Topics

* [Request redirection and the REST API](RESTRedirect.md "RESTRedirect.md")
* [Request routing](UsingRouting.md "UsingRouting.md")
