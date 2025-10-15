# Website endpoints

When you configure your bucket as a static website, the website is available at the
 AWS Region-specific website endpoint of the bucket. Website endpoints are different
 from the endpoints where you send REST API requests. For more information about the
 differences between the endpoints, see [Key differences between a website endpoint
 and a REST API endpoint](#WebsiteRestEndpointDiff "#WebsiteRestEndpointDiff").

Depending on your Region, your Amazon S3 website endpoint follows one of these two formats.


* **s3-website dash (-) Region** ‐ `http://`bucket-name`.s3-website-`Region`.amazonaws.com`
* **s3-website dot (.) Region** ‐ `http://`bucket-name`.s3-website.`Region`.amazonaws.com`
These URLs return the default index document that you configure for the website. For a complete list of Amazon S3 website endpoints, see [Amazon S3 Website
 Endpoints](https://docs.aws.amazon.com/general/latest/gr/s3.html#s3_website_region_endpoints "https://docs.aws.amazon.com/general/latest/gr/s3.html#s3_website_region_endpoints").

###### Note

To augment the security of your Amazon S3 static websites, the Amazon S3 website endpoint domains (for example, *s3-website-us-east-1.amazonaws.com* or *s3-website.ap-south-1.amazonaws.com*)
 are registered in the [Public Suffix
 List (PSL)](https://publicsuffix.org/ "https://publicsuffix.org/"). For further security, we recommend that you use cookies with
 a `__Host-` prefix if you ever need to set sensitive cookies in the
 domain name for your Amazon S3 static websites. This practice will help to
 defend your domain against cross-site request forgery attempts (CSRF). For more
 information see the [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes") page in the Mozilla Developer Network.

If you want your website to be public, you must make all your content publicly
 readable for your customers to be able to access it at the website endpoint. For more
 information, see [Setting permissions for website
 access](WebsiteAccessPermissionsReqd.md "WebsiteAccessPermissionsReqd.md"). 

###### Important


* Amazon S3 website endpoints do not support HTTPS or access points. If you want
 to use HTTPS, you can do one of the following: 




	+ (Recommended) Use [AWS Amplify
	 Hosting](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html.html "https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html.html") to host static website content stored on S3.
	 Amplify Hosting is a fully managed service that makes it easy to
	 deploy your websites on a globally available content delivery
	 network (CDN) powered by Amazon CloudFront, allowing secure static
	 website hosting. 
	
	
	With AWS Amplify Hosting, you can select the location of your
	 objects within your general purpose bucket, deploy your content to a
	 managed CDN, and generate a public HTTPS URL for your website to be
	 accessible anywhere. For more information about Amplify Hosting, see
	 [Deploying a static website to AWS Amplify Hosting from an S3
	 general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/website-hosting-amplify "https://docs.aws.amazon.com/AmazonS3/latest/userguide/website-hosting-amplify") and [Deploying a static website from S3 using the Amplify
	 console](https://docs.aws.amazon.com/amplify/latest/userguide/deploy--from-amplify-console.html "https://docs.aws.amazon.com/amplify/latest/userguide/deploy--from-amplify-console.html") in the *AWS Amplify Console User
	 Guide*.
	+ Use Amazon CloudFront to serve a static website hosted on Amazon S3. For more
	 information, see [How do I use CloudFront to serve HTTPS requests for my Amazon S3
	 bucket?](https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-https-requests-s3 "https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-https-requests-s3") To use HTTPS with a custom domain, see [Configuring a static website using a custom domain registered
	 with Route 53](website-hosting-custom-domain-walkthrough.md "website-hosting-custom-domain-walkthrough.md").
* Requester Pays buckets do not allow access
 through a website endpoint. Any request to such a bucket receives a
 **`403 Access Denied`** response. For more information,
 see [Using Requester Pays general purpose buckets for storage
 transfers and usage](RequesterPaysBuckets.md "RequesterPaysBuckets.md").
###### Topics

* [Website endpoint examples](#website-endpoint-examples "#website-endpoint-examples")
* [Adding a DNS CNAME](#website-endpoint-dns-cname "#website-endpoint-dns-cname")
* [Using a custom domain with Route 53](#custom-domain-s3-endpoint "#custom-domain-s3-endpoint")
* [Key differences between a website endpoint
 and a REST API endpoint](#WebsiteRestEndpointDiff "#WebsiteRestEndpointDiff")

## Website endpoint examples


The following examples show how you can access an Amazon S3 bucket that is configured
 as a static website.


###### Example — Requesting an object at the root level

To request a specific object that is stored at the root level in the bucket,
 use the following URL structure.


```
http://`bucket-name`.s3-website.`Region`.amazonaws.com/`object-name`
```
For example, the following URL requests the `photo.jpg` object that
 is stored at the root level in the bucket.


```
http://example-bucket.s3-website.us-west-2.amazonaws.com/photo.jpg
```

###### Example — Requesting an object in a prefix

To request an object that is stored in a folder in your bucket, use this URL
 structure.


```
http://`bucket-name`.s3-website.`Region`.amazonaws.com/`folder-name`/`object-name`
```
The following URL requests the `docs/doc1.html` object in your
 bucket. 


```
http://example-bucket.s3-website.us-west-2.amazonaws.com/docs/doc1.html
```

## Adding a DNS CNAME


If you have a registered domain, you can add a DNS CNAME entry to point to the
 Amazon S3 website endpoint. For example, if you registered the domain
 `www.example-bucket.com`, you could create a bucket
 `www.example-bucket.com`, and add a DNS CNAME record that points to
 `www.example-bucket.com.s3-website.`Region`.amazonaws.com`.
 All requests to `http://www.example-bucket.com` are routed to
 `www.example-bucket.com.s3-website.`Region`.amazonaws.com`. 


For more information, see [Customizing Amazon S3 URLs with CNAME
 records](VirtualHosting.md#VirtualHostingCustomURLs "VirtualHosting.md#VirtualHostingCustomURLs"). 


## Using a custom domain with Route 53


Instead of accessing the website using an Amazon S3 website endpoint, you can use your
 own domain registered with Amazon Route 53 to serve your content—for example,
 `example.com`. You can use Amazon S3 with Route 53 to host a website at the
 root domain. For example, if you have the root domain `example.com` and
 you host your website on Amazon S3, your website visitors can access the site from their
 browser by entering either `http://www.example.com` or
 `http://example.com`. 


For an example walkthrough, see [Tutorial: Configuring a static website using a
 custom domain registered with Route 53](website-hosting-custom-domain-walkthrough.md "website-hosting-custom-domain-walkthrough.md"). 


## Key differences between a website endpoint
 and a REST API endpoint


An Amazon S3 website endpoint is optimized for access from a web browser. The following
 table summarizes the key differences between a REST API endpoint and a website
 endpoint. 




| Key difference | REST API endpoint | Website endpoint |
| --- | --- | --- |
| Access control | Supports both public and private content | Supports only publicly readable content  |
| Error message handling | Returns an XML-formatted error response | Returns an HTML document |
| Redirection support | Not applicable | Supports both object-level and bucket-level redirects |
| Requests supported  | Supports all bucket and object operations | Supports only `GET` and `HEAD` requests on objects |
| Responses to `GET` and `HEAD` requests at the root of a
 bucket | Returns a list of the object keys in the bucket | Returns the index document that is specified in the website
 configuration |
| Secure Sockets Layer (SSL) support | Supports SSL connections | Does not support SSL connections |


For a complete list of Amazon S3 endpoints, see [Amazon S3 endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html "https://docs.aws.amazon.com/general/latest/gr/s3.html") in the
 *AWS General Reference*.
