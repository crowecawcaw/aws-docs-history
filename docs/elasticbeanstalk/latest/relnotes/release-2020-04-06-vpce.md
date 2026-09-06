

# Release: Elastic Beanstalk adds support for interface VPC endpoints on April 6, 2020
<a name="release-2020-04-06-vpce"></a>

AWS Elastic Beanstalk added support for interface VPC endpoints to allow all service traffic to stay within the Amazon network.

**Release date:** April 6, 2020

## Changes
<a name="release-2020-04-06-vpce.changes"></a>

Until now, your application and other code running on environment instances had to send requests to the Elastic Beanstalk service on the service's public endpoint, `elasticbeanstalk.{{region}}.amazonaws.com`. If your application needed to send such requests, the application's Elastic Beanstalk environment instances had to be in a Amazon Virtual Private Cloud (Amazon VPC) with at least one public subnet. A public subnet has public internet access.

With today's release, you can limit your application's direct exposure to the internet by setting up an *interface VPC endpoint*. It allows you to privately connect instances in your VPC to the Elastic Beanstalk service without requiring public IP addresses. Instances send requests to the interface endpoint, `com.amazonaws.{{region}}.elasticbeanstalk`. Traffic between your VPC and Elastic Beanstalk doesn't leave the Amazon network. Similarly, you can set up another interface endpoint to the Elastic Beanstalk enhanced health service, to keep enhanced health traffic from your instances within the Amazon network. Using interface endpoints lets you use a completely private VPC, while still allowing your application to communicate with Elastic Beanstalk.

To restrict access of your VPC to Elastic Beanstalk through the interface endpoint, you can also attach an *endpoint policy* to the endpoint.

For more information, see [Using Elastic Beanstalk with VPC Endpoints](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/vpc-vpce.html) in the *AWS Elastic Beanstalk Developer Guide*.

**Note**  
Today we're adding support for interface VPC endpoints in all AWS Regions except for: China (Beijing), China (Ningxia), AWS GovCloud (US-East), AWS GovCloud (US-West).  
We're working to extend support to more AWS Regions in the near future.