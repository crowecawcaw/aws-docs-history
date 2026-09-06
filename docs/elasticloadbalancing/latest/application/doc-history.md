

# Document history for Application Load Balancers
<a name="doc-history"></a>

The following table describes the releases for Application Load Balancers.

| Change | Description | Date | 
| --- |--- |--- |
| [Access token validation](#doc-history) | This release adds support for the load balancer to validate JSON Web Tokens (JWT) provided by clients for secure service-to-service (S2S) or machine-to-machine (M2M) communications. | November 21, 2025 | 
| [Transforms](#doc-history) | This release adds support to transform host headers and URLs for incoming requests before the load balancer routes the traffic to a target. | October 15, 2025 | 
| [Bucket policies for access logs and connection logs](#doc-history) | Prior to this release, the bucket policy that you used depended on whether the Region was available before or after August 2022. With this release, the newer bucket policy is supported in all Regions. Note that the legacy bucket policy is still supported. | September 10, 2025 | 
| [HTTP header modification](#doc-history) | This release adds support for HTTP header modification for all response codes. Previously, this feature was limited to response codes 2xx and 3xx. | February 28, 2025 | 
| [Capacity Unit reservation](#doc-history) | This release adds support to set a minimum capacity for your load balancer. | November 20, 2024 | 
| [Resource map](#doc-history) | This release adds support to view your load balancer resources and relationships in a visual format. | March 8, 2024 | 
| [One click WAF](#doc-history) | This release adds support for configuring the behavior of your load balancer if it integrates with one click AWS WAF. | February 6, 2024 | 
| [Mutual TLS](#doc-history) | This release adds support for mutual TLS authentication. | November 26, 2023 | 
| [Automatic Target Weights](#doc-history) | This release adds support for the automatic target weights algorithm. | November 26, 2023 | 
| [FIPS 140-3 TLS termination](#doc-history) | This release adds security policies that use FIPS 140-3 crypotographic modules when terminating TLS connections. | November 20, 2023 | 
| [Register targets using IPv6](#doc-history) | This release adds support to register instances as targets when addressed by IPv6. | October 2, 2023 | 
| [Security policies supporting TLS 1.3](#doc-history) | This release adds support for TLS 1.3 predefined security policies. | March 22, 2023 | 
| [Zonal shift](#doc-history) | This release adds support to route traffic away from a single impaired Availability Zone through integration with the Amazon Application Recovery Controller (ARC). | November 28, 2022 | 
| [Turn off cross-zone load balancing](#doc-history) | This release adds support to turn off cross-zone load balancing. | November 28, 2022 | 
| [Target group health](#doc-history) | This release adds support to configure the minimum count or percentage of targets that must be healthy, and what actions the load balancer takes when the threshold is not met. | November 28, 2022 | 
| [Cross-zone load balancing](#doc-history) | This release adds support to configure cross-zone load balancing at the target group level. | November 17, 2022 | 
| [IPv6 target groups](#doc-history) | This release adds support to configure IPv6 target groups for Application Load Balancers. | November 23, 2021 | 
| [IPv6 internal load balancers](#doc-history) | This release adds support to configure IPv6 target groups for Application Load Balancers. | November 23, 2021 | 
| [AWS PrivateLink and static IP addresses](#doc-history) | This release adds support to use AWS PrivateLink and expose static IP addresses by forwarding traffic directly from Network Load Balancers to Application Load Balancers. | September 27, 2021 | 
| [Client port preservation](#doc-history) | This release adds an attribute to preserve the source port that the client used to connect to the load balancer. | July 29, 2021 | 
| [TLS headers](#doc-history) | This release adds an attribute to indicate that the TLS headers, which contain information about the negotiated TLS version and cipher suite, are added to the client request before sending it to the target. | July 21, 2021 | 
| [Additional ACM certificates](#doc-history) | This release supports RSA certificates with 2048, 3072, and 4096-bit key lengths, and all ECDSA certificates. | July 14, 2021 | 
| [Application-based stickiness](#doc-history) | This release adds an application-based cookie to support sticky sessions for your load balancer. | February 8, 2021 | 
| [Security policy for FS supporting TLS version 1.2](#doc-history) | This release adds a security policy for Forward Secrecy (FS) supporting TLS version 1.2. | November 24, 2020 | 
| [WAF fail open support](#doc-history) | This release adds support for configuring the behavior of your load balancer if it integrates with AWS WAF. | November 13, 2020 | 
| [gRPC and HTTP/2 support](#doc-history) | This release adds support for gRPC workloads and end-to-end HTTP/2. | October 29, 2020 | 
| [Outpost support](#doc-history) | You can provision an Application Load Balancer on your AWS Outposts. | September 8, 2020 | 
| [Desync mitigation mode](#doc-history) | This release adds support for desync mitigation mode. | August 17, 2020 | 
| [Least outstanding requests](#doc-history) | This release adds support for the least outstanding requests algorithm. | November 25, 2019 | 
| [Weighted target groups](#doc-history) | This release adds support for forward actions with multiple target groups. Requests are distributed to these target groups based on the weight you specify for each target group. | November 19, 2019 | 
| [New attribute](#doc-history) | This release adds support for the routing.http.drop\_invalid\_header\_fields.enabled attribute. | November 15, 2019 | 
| [Security policies for FS](#doc-history) | This release adds support for three additional predefined forward secrecy security policies. | October 8, 2019 | 
| [Advanced request routing](#doc-history) | This release adds support for additional condition types for your listener rules. | March 27, 2019 | 
| [Lambda functions as a target](#doc-history) | This release adds support for registering Lambda functions as a target. | November 29, 2018 | 
| [Redirect actions](#doc-history) | This release adds support for the load balancer to redirect requests to a different URL. | July 25, 2018 | 
| [Fixed-response actions](#doc-history) | This release adds support for the load balancer to return a custom HTTP response. | July 25, 2018 | 
| [Security policies for FS and TLS 1.2](#doc-history) | This release adds support for two additional predefined security policies. | June 6, 2018 | 
| [User authentication](#doc-history) | This release adds support for the load balancer to authenticate users of your applications using their corporate or social identities before routing requests. | May 30, 2018 | 
| [Resource-level permissions](#doc-history) | This release adds support for resource-level permissions and tagging condition keys. | May 10, 2018 | 
| [Slow start mode](#doc-history) | This release adds support for slow start mode, which gradually increases the share of requests the load balancer sends to a newly registered target while it warms up. | March 24, 2018 | 
| [SNI support](#doc-history) | This release adds support for Server Name Indication (SNI). | October 10, 2017 | 
| [IP addresses as targets](#doc-history) | This release adds support for registering IP addresses as targets. | August 31, 2017 | 
| [Host-based routing](#doc-history) | This release adds support for routing requests based on the host names in the host header. | April 5, 2017 | 
| [Security policies for TLS 1.1 and TLS 1.2](#doc-history) | This release adds security policies for TLS 1.1 and TLS 1.2. | February 6, 2017 | 
| [IPv6 support](#doc-history) | This release adds support for IPv6 addresses. | January 25, 2017 | 
| [Request tracing](#doc-history) | This release adds support for request tracing. | November 22, 2016 | 
| [Percentiles support for the TargetResponseTime metric](#doc-history) | This release adds support for the new percentile statistics supported by Amazon CloudWatch. | November 17, 2016 | 
| [New load balancer type](#doc-history) | This release of Elastic Load Balancing introduces Application Load Balancers. | August 11, 2016 | 