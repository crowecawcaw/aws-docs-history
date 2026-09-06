

# Amazon Route 53 in AWS GovCloud (US)
<a name="govcloud-r53"></a>

 Route 53 is a highly available and scalable Domain Name System (DNS) web service. In the AWS GovCloud (US), you can use Route 53 public and private DNS and health checking.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Amazon Route 53 differs
<a name="govcloud-r53-diffs"></a>

The following differences apply to Amazon Route 53:

 **Public Hosted Zones** 
+ DNS queries will be answered from within FedRAMP boundary.
+ When creating alias records, you can now choose alias targets in the AWS GovCloud (US) Regions, but you cannot choose alias targets in global AWS Regions. Currently, we support alias targets for API Gateway, Elastic Beanstalk, Application Load Balancer, Classic Load Balancer, Network Load Balancer, Amazon S3 website endpoint, and VPC endpoint. The other alias targets are not available.
+ The customer managed key that you use with DNSSEC signing must be in AWS GovCloud (US-West).
+ The CloudWatch Logs log group for query logging must be in AWS GovCloud (US-West).
+  CloudWatch metrics like DNSQueries can be found in AWS GovCloud (US-West).
+ Route 53 [Traffic Flow](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/traffic-flow.html) is supported as follows:
  + You can create traffic policies using all routing policy types.
  + You can’t use CloudFront distributions as alias targets in traffic policies.
+ DNS query checking tool on the console, and `TestDNSAnswer` API are not available.

 **Private Hosted Zones** 
+ You can create private hosted zones in the AWS GovCloud (US). In general, the functionality is the same as for private hosted zones in the commercial version of Route 53.
+ Latency based, geolocation, and geoproximity routing types are not available in private hosted zones.
+ You cannot use IP-based routing policy for records in a private hosted zone.
+  Route 53 Resolver delegation is not available.

 **Health Checking** 
+ You can create health checks that monitor endpoints in the AWS GovCloud, and you can create health checks that monitor the status of other health checks.
+ As in other AWS Regions, if you create a health check that monitors an endpoint in the AWS GovCloud, you must make the endpoint available on the public internet. Route 53 health checkers send health checking requests over the public internet.
+ You can restrict access to your endpoints by allowlisting the IP addresses of Route 53 health checkers in the AWS GovCloud:
  + 160.1.56.0/25
  + 160.1.55.0/25
  + 160.1.55.128/25
  + 18.253.167.128/25
  + 18.253.168.0/25
  + 18.253.167.0/25
+ All Amazon Route 53 API actions have a token bucket maximum capacity of 40 and a bucket refill rate of 5, at both the account level and the individual API level.
+ Change throughput limiting is not available.

The control plane for Route 53 in the AWS GovCloud (US) is in the AWS GovCloud (US-West).

## Documentation
<a name="govcloud-r53-docs"></a>
+  [Amazon Route 53 documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) 

## Export-controlled content
<a name="govcloud-r53-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ This service can generate metadata from customer-defined configurations. AWS suggests customers do not enter export-controlled information in console fields, descriptions, resource names, and tagging information.