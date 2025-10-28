# Give Inference Recommender Jobs Access to Resources in Your

Amazon VPC

###### Note

Inference Recommender requires you to register your model with Model Registry. Note that Model Registry
doesn't allow your model artifacts or Amazon ECR image to be VPC restricted.

Inference Recommender also has a requirement that your sample payload Amazon S3 object is not VPC restricted.
For inference recommendation jobs, you can't create a custom policy that allows only requests from your private VPC to access to your Amazon S3 buckets.

To specify subnets and security groups in your private VPC, use the `RecommendationJobVpcConfig`
request parameter of the [CreateInferenceRecommendationsJob](../APIReference/API_CreateInferenceRecommendationsJob.md "../APIReference/API_CreateInferenceRecommendationsJob.md")
API, or specify your subnets and security groups when you create a recommendation job in the SageMaker AI console.

Inference Recommender uses this information to create endpoints. When provisioning endpoints, SageMaker AI creates network interfaces
and attaches them to your endpoints. The network interfaces provide your endpoints with a network connection to your VPC.
The following is an example of the `VpcConfig` parameter that you include in a call to `CreateInferenceRecommendationsJob`:

```
VpcConfig: {
      "Subnets": [
          "subnet-0123456789abcdef0",
          "subnet-0123456789abcdef1",
          "subnet-0123456789abcdef2"
          ],
      "SecurityGroupIds": [
          "sg-0123456789abcdef0"
          ]
       }
```

Refer to the following topics for more information on configuring your Amazon VPC for use with Inference Recommender jobs.

###### Topics

- [Ensure that subnets have enough IP addresses](#inference-recommender-vpc-access-subnets "#inference-recommender-vpc-access-subnets")
- [Create an Amazon S3 VPC endpoint](#inference-recommender-vpc-access-endpoint "#inference-recommender-vpc-access-endpoint")
- [Add permissions for Inference Recommender jobs running in an Amazon VPC to custom IAM policies](#inference-recommender-vpc-access-permissions "#inference-recommender-vpc-access-permissions")
- [Configure route tables](#inference-recommender-vpc-access-route-tables "#inference-recommender-vpc-access-route-tables")
- [Configure the VPC security group](#inference-recommender-vpc-access-security-group "#inference-recommender-vpc-access-security-group")

## Ensure that subnets have enough IP addresses

Your VPC subnets should have at least two private IP addresses for each instance in an inference recommendation job.
For more information about subnets and private IP addresses, see
[How Amazon VPC works](../../../AmazonVPC/latest/UserGuide/VPC_Subnets.md#vpc-sizing-ipv4 "../../../AmazonVPC/latest/UserGuide/VPC_Subnets.md#vpc-sizing-ipv4")
in the _Amazon VPC User Guide_.

## Create an Amazon S3 VPC endpoint

If you configure your VPC to block access to the internet, Inference Recommender can't connect to the Amazon S3 buckets that contain
your models unless you create a VPC endpoint that allows access. By creating a VPC endpoint, you allow your SageMaker AI
inference recommendation jobs to access the buckets where you store your data and model artifacts.

To create an Amazon S3 VPC endpoint, use the following procedure:

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**, and then choose **Create Endpoint**.
3. For **Service Name**, search for `com.amazonaws.`region`.s3`,
   where `region` is the name of the Region where your VPC resides.
4. Choose the **Gateway type**.
5. For **VPC**, choose the VPC you want to use for this endpoint.
6. For **Configure route tables**, select the route tables to be used by the endpoint.
   The VPC service automatically adds a route to each route table you select that points any Amazon S3 traffic to the new endpoint.
7. For **Policy**, choose **Full Access** to allow full access to the
   Amazon S3 service by any user or service within the VPC.

## Add permissions for Inference Recommender jobs running in an Amazon VPC to custom IAM policies

The `AmazonSageMakerFullAccess` managed policy includes the permissions that you need to use models configured for Amazon VPC access with an endpoint.
These permissions allow Inference Recommender to create an elastic network interface and attach it to the inference recommendation job running in an Amazon VPC.
If you use your own IAM policy, you must add the following permissions to that policy to use models configured for Amazon VPC access.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {"Effect": "Allow",
 "Action": [
 "ec2:DescribeVpcEndpoints",
 "ec2:DescribeDhcpOptions",
 "ec2:DescribeVpcs",
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DeleteNetworkInterfacePermission",
 "ec2:DeleteNetworkInterface",
 "ec2:CreateNetworkInterfacePermission",
 "ec2:CreateNetworkInterface",
 "ec2:ModifyNetworkInterfaceAttribute"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Configure route tables

Use the default DNS settings for your endpoint route table, so that standard Amazon S3 URLs (for example:
`http://s3-aws-region.amazonaws.com/amzn-s3-demo-bucket`) resolve.
If you don't use the default DNS settings, ensure that the URLs that you use to specify the locations of the data
in your inference recommendation jobs resolve by configuring the endpoint route tables. For information about
VPC endpoint route tables, see [Routing gateway endpoints](../../../AmazonVPC/latest/UserGuide/vpce-gateway.md#vpc-endpoints-routing "../../../AmazonVPC/latest/UserGuide/vpce-gateway.md#vpc-endpoints-routing") in the _Amazon VPC User Guide_.

## Configure the VPC security group

In your security group for the inference recommendation job, you must allow outbound communication to your Amazon S3
VPC endpoints and the subnet CIDR ranges used for the inference recommendation job. For information, see
[Security Group Rules](../../../AmazonVPC/latest/UserGuide/VPC_SecurityGroups.md#SecurityGroupRules "../../../AmazonVPC/latest/UserGuide/VPC_SecurityGroups.md#SecurityGroupRules")
and [Control access to services with Amazon VPC endpoints](../../../AmazonVPC/latest/UserGuide/vpc-endpoints-access.md "../../../AmazonVPC/latest/UserGuide/vpc-endpoints-access.md")
in the _Amazon VPC User Guide_.
