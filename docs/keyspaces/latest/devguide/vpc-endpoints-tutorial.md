

# Tutorial: Connect to Amazon Keyspaces using an interface VPC endpoint
<a name="vpc-endpoints-tutorial"></a>

This tutorial walks you through setting up and using an interface VPC endpoint for Amazon Keyspaces. 

*Interface VPC endpoints* enable private communication between your virtual private cloud (VPC) running in Amazon VPC and Amazon Keyspaces. Interface VPC endpoints are powered by AWS PrivateLink, which is an AWS service that enables private communication between VPCs and AWS services. For more information, see [Using Amazon Keyspaces with interface VPC endpoints](vpc-endpoints.md).

**Topics**
+ [Tutorial prerequisites and considerations](vpc-endpoints-tutorial.before-you-begin.md)
+ [Step 1: Launch an Amazon EC2 instance](vpc-endpoints-tutorial.launch-ec2-instance.md)
+ [Step 2: Configure your Amazon EC2 instance](vpc-endpoints-tutorial.configure-ec2-instance.md)
+ [Step 3: Create a VPC endpoint for Amazon Keyspaces](vpc-endpoints-tutorial.create-endpoint.md)
+ [Step 4: Configure permissions for the VPC endpoint connection](vpc-endpoints-tutorial.permissions.md)
+ [Step 5: Configure monitoring with CloudWatch](vpc-endpoints-tutorial.monitoring.md)
+ [Step 6: (Optional) Best practices to configure the connection pool size for your application](vpc-endpoints-tutorial.connections.md)
+ [Step 7: (Optional) Clean up](vpc-endpoints-tutorial.clean-up.md)