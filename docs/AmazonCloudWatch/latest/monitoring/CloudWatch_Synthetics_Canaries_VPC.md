# Running a canary on a VPC

You can run canaries on endpoints on a VPC and public internal endpoints. To run a
 canary on a VPC, you must have both the **DNS Resolution** and **DNS hostnames** options enabled on the VPC. For more information, see [Using DNS with Your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html").

When you run a canary on a VPC endpoint, you must provide a way for it to send its
 metrics to CloudWatch and its artifacts to Amazon S3. If the VPC is already enabled for internet
 access, there's nothing more for you to do. The canary executes in your VPC, but can access
 the internet to upload its metrics and artifacts.

If the VPC is not already enabled for internet access, you have two options:


* Enable IPv4 internet access to allow the canary to send metrics to CloudWatch and Amazon S3. For more information, see the following section
 [Giving internet access to your canary on a VPC](#CloudWatch_Synthetics_VPC_Internet "#CloudWatch_Synthetics_VPC_Internet").
* If you want to keep your VPC private, you can configure the canary to send its data
 to CloudWatch and Amazon S3 through private VPC endpoints. If you have not already done so, you must
 create a VPC endpoint for CloudWatch (com.amazonaws.`region`.monitoring) and a 
 gateway endpoint for Amazon S3. For more information, see 
 [Using CloudWatch, CloudWatch Synthetics, and CloudWatch Network
 Monitoring with interface VPC endpoints](cloudwatch-and-interface-VPC.md "cloudwatch-and-interface-VPC.md")
 and [Amazon VPC Endpoints for Amazon S3](https://docs.aws.amazon.com/glue/latest/dg/vpc-endpoints-s3.html "https://docs.aws.amazon.com/glue/latest/dg/vpc-endpoints-s3.html").

## Giving internet access to your canary on a VPC


Follow these steps to give internet access to your VPC canary, or to assign your canary a static IP address


###### To give internet access (IPv4) to a canary on a VPC

1. Create a NAT gateway in a public subnet on the VPC. For instructions, see
 [Create a NAT 
 gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-creating "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-creating").
2. Add a new route to the route table in the private subnet where the canary is launched. Specify the following:




	* For **Destination**, enter `0.0.0.0/0`
	* For **Target**, choose **NAT Gateway**, and then choose the 
	 ID of the NAT gateway that you created.
	* Choose **Save routes**.
For more information about adding the route to the route table, see [Add and remove routes from a route table](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithRouteTables.html#AddRemoveRoutes "https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithRouteTables.html#AddRemoveRoutes").

###### To give internet access (IPv6) to a canary on a VPC

1. Configure your VPC to have Dualstack subnets. You must add an Egress-Only Internet Gateway to the VPC, update the route tables to allow traffic to the Internet Gateway, and allow outbound access from the associated Security Groups. For more information, see [Add IPv6 support for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6-add.html "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6-add.html") .
2. Set the `Ipv6AllowedForDualstack`  in your canary VPC configuration using the `CreateCanary` or `UpdateCanary` API. For more information, see [VpcConfigInput](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_VpcConfigInput.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_VpcConfigInput.html").


To enable outbound IPv6 traffic from your canary, the VPC subnets attached to the canary must be enabled for Dualstack.

###### Note

Be sure that the routes to your NAT gateway are in an **active** status. If the NAT 
 gateway is deleted and you haven't updated the routes, they're in a black hole status. For more 
 information, see [Work with NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-working-with "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-working-with").
