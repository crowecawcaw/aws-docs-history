

# Elastic Load Balancing in AWS GovCloud (US)
<a name="govcloud-elb"></a>

 Elastic Load Balancing automatically distributes your incoming application traffic across multiple targets, such as EC2 instances. It monitors the health of registered targets and routes traffic only to the healthy targets.

 Elastic Load Balancing supports the following types of load balancers: Application Load Balancers, Network Load Balancers, Gateway Load Balancers, and Classic Load Balancers. All four types of load balancers are supported.

**Note**  
Some features of Elastic Load Balancing (ELB) TLS do not support FIPS 140-3 requirements by default. When using the Classic or Network Load Balancer, you can pass TCP traffic and terminate TLS on your target (for example, web server), that is configured to support FIPS 140-3 requirements. Application Load Balancer (ALB) supports selecting FIPS algorithms.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Elastic Load Balancing differs
<a name="govcloud-elb-diffs"></a>

The following differences apply to Elastic Load Balancing:
+ When using the legacy bucket policy, specify the following AWS account IDs in the policy to grant Elastic Load Balancing permission to write logs to your S3 bucket:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-elb.html)
+ Export data must be encrypted in transit outside of the export boundary. Because Elastic Load Balancing uses global DNS servers, export traffic across Elastic Load Balancing must be encrypted.
+ Cognito authentication is not available.

## Documentation
<a name="govcloud-elb-docs"></a>
+  [Elastic Load Balancing documentation](https://docs.aws.amazon.com/documentation/elastic-load-balancing/) 

## Export-controlled content
<a name="govcloud-elb-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ All customer parameters provided as input to Elastic Load Balancing (via console, APIs, or other mechanism) are not permitted to contain export-controlled data. Examples include the names of load balancers and the names of load balancer policies.
+ Do not enter export-controlled data in the following fields:
  + Resource tags

If you are processing export-controlled data with this service, use the SSL (HTTPS) endpoint to maintain export compliance. For more information, see [Service Endpoints](using-govcloud-endpoints.md).