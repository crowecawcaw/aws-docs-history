# Choose how CloudFront serves HTTPS
 requests

If you want your viewers to use HTTPS and to use alternate domain names for your
 files, choose one of the following options for how CloudFront serves HTTPS
 requests:


* Use [Server Name
 Indication (SNI)](https://en.wikipedia.org/wiki/Server_Name_Indication "https://en.wikipedia.org/wiki/Server_Name_Indication") – Recommended
* Use a dedicated IP address in each edge location
This section explains how each option works.


## Use SNI to serve HTTPS requests (works for most
 clients)


[Server Name Indication
 (SNI)](https://en.wikipedia.org/wiki/Server_Name_Indication "https://en.wikipedia.org/wiki/Server_Name_Indication") is an extension to the TLS protocol that is supported by browsers
 and clients released after 2010. If you configure CloudFront to serve HTTPS requests
 using SNI, CloudFront associates your alternate domain name with an IP address for
 each edge location. When a viewer submits an HTTPS request for your content, DNS
 routes the request to the IP address for the correct edge location. The IP
 address to your domain name is determined during the SSL/TLS handshake
 negotiation; the IP address isn't dedicated to your distribution.


The SSL/TLS negotiation occurs early in the process of establishing an HTTPS
 connection. If CloudFront can't immediately determine which domain the request is for,
 it drops the connection. When a viewer that supports SNI submits an HTTPS
 request for your content, here's what happens:



1. The viewer automatically gets the domain name from the request URL and adds it to the SNI extension of the TLS client hello message.
2. When CloudFront receives the TLS client hello, it uses the domain name in the SNI extension to find the matching CloudFront distribution and sends back the associated TLS certificate.
3. The viewer and CloudFront perform SSL/TLS negotiation.
4. CloudFront returns the requested content to the viewer.

For a current list of the browsers that support SNI, see the Wikipedia entry
 [Server Name
 Indication](https://en.wikipedia.org/wiki/Server_Name_Indication "https://en.wikipedia.org/wiki/Server_Name_Indication").


If you want to use SNI but some of your users' browsers don't support SNI, you
 have several options:



* Configure CloudFront to serve HTTPS requests by using dedicated IP addresses
 instead of SNI. For more information, see [Use a dedicated IP address to
 serve HTTPS requests (works for all clients)](#cnames-https-dedicated-ip "#cnames-https-dedicated-ip").
* Use the CloudFront SSL/TLS certificate instead of a custom certificate. This
 requires that you use the CloudFront domain name for your distribution in the
 URLs for your files, for example,
 `https://d111111abcdef8.cloudfront.net/logo.png`.


If you use the default CloudFront certificate, viewers must support the SSL
 protocol TLSv1 or later. CloudFront doesn't support SSLv3 with the default
 CloudFront certificate.


You also must change the SSL/TLS certificate that CloudFront is using from a
 custom certificate to the default CloudFront certificate:




	+ If you haven't used your distribution to distribute your
	 content, you can just change the configuration. For more
	 information, see [Update a distribution](HowToUpdateDistribution.md "HowToUpdateDistribution.md").
	+ If you have used your distribution to distribute your content,
	 you must create a new CloudFront distribution and change the URLs for
	 your files to reduce or eliminate the amount of time that your
	 content is unavailable. For more information, see [Revert from a custom SSL/TLS
	 certificate to the default CloudFront certificate](cnames-and-https-revert-to-cf-certificate.md "cnames-and-https-revert-to-cf-certificate.md").
* If you can control which browser your users use, have them upgrade
 their browser to one that supports SNI.
* Use HTTP instead of HTTPS.

## Use a dedicated IP address to
 serve HTTPS requests (works for all clients)


Server Name Indication (SNI) is one way to associate a request with a domain.
 Another way is to use a dedicated IP address. If you have users who can't
 upgrade to a browser or client released after 2010, you can use a dedicated IP
 address to serve HTTPS requests. For a current list of the browsers that support
 SNI, see the Wikipedia entry [Server Name
 Indication](https://en.wikipedia.org/wiki/Server_Name_Indication "https://en.wikipedia.org/wiki/Server_Name_Indication"). 


###### Important

If you configure CloudFront to serve HTTPS requests using dedicated IP
 addresses, you incur an additional monthly charge. The charge begins when
 you associate your SSL/TLS certificate with a distribution and you enable
 the distribution. For more information about CloudFront pricing, see [Amazon CloudFront Pricing](https://aws.amazon.com/cloudfront/pricing "https://aws.amazon.com/cloudfront/pricing"). In
 addition, see [Using the Same Certificate for Multiple CloudFront Distributions](cnames-and-https-limits.md#cnames-and-https-same-certificate-multiple-distributions "cnames-and-https-limits.md#cnames-and-https-same-certificate-multiple-distributions").


When you configure CloudFront to serve HTTPS requests by using dedicated IP addresses, CloudFront
 associates your certificate with a dedicated IP address in each CloudFront edge
 location. When a viewer submits an HTTPS request for your content, here's what
 happens:



1. DNS routes the request to the IP address for your distribution in the
 applicable edge location.
2. If a client request provides the SNI extension in the
 `ClientHello` message, CloudFront searches for a distribution
 that is associated with that SNI.




	* If there's a match, CloudFront responds to the request with the
	 SSL/TLS certificate.
	* If there's no match, CloudFront uses the IP address instead to
	 identify your distribution and to determine which SSL/TLS
	 certificate to return to the viewer.
3. The viewer and CloudFront perform SSL/TLS negotiation using your SSL/TLS
 certificate.
4. CloudFront returns the requested content to the viewer.

This method works for every HTTPS request, regardless of the browser or other
 viewer that the user is using. 


###### Note

Dedicated IPs are not static IPs and can change over time. The IP address that is returned for the edge location is allocated dynamically from the IP address ranges of the [CloudFront edge servers list](LocationsOfEdgeServers.md "LocationsOfEdgeServers.md").

The IP address ranges for CloudFront edge servers are subject to change. To be notified of IP address changes, [subscribe to AWS Public IP Address Changes via Amazon SNS](https://aws.amazon.com/blogs/aws/subscribe-to-aws-public-ip-address-changes-via-amazon-sns/ "https://aws.amazon.com/blogs/aws/subscribe-to-aws-public-ip-address-changes-via-amazon-sns/").


## Request permission
 to use three or more dedicated IP SSL/TLS certificates


If you need permission to permanently associate three or more SSL/TLS
 dedicated IP certificates with CloudFront, perform the following procedure. For more
 details about HTTPS requests, see [Choose how CloudFront serves HTTPS
 requests](cnames-https-dedicated-ip-or-sni.md "cnames-https-dedicated-ip-or-sni.md").


###### Note

This procedure is for using three or more dedicated IP certificates across
 your CloudFront distributions. The default value is 2. Keep in mind you cannot
 bind more than one SSL certificate to a distribution.

You can only associate a single SSL/TLS certificate to a CloudFront distribution
 at a time. This number is for the total number of dedicated IP SSL
 certificates you can use across all of your CloudFront distributions.


###### To request
 permission to use three or more certificates with a CloudFront
 distribution

1. Go to the [Support Center](https://console.aws.amazon.com/support/home?#/case/create?issueType=service-limit-increase&limitType=service-code-cloudfront-distributions "https://console.aws.amazon.com/support/home?#/case/create?issueType=service-limit-increase&limitType=service-code-cloudfront-distributions") and create a case.
2. Indicate how many certificates you need permission to use, and
 describe the circumstances in your request. We'll update your account as
 soon as possible.
3. Continue with the next procedure.
