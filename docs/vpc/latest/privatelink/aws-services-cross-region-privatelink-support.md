

# Cross-region enabled AWS services
<a name="aws-services-cross-region-privatelink-support"></a>

The following AWS services integrate with cross Region AWS PrivateLink. You can create an interface endpoint to connect to these services in another AWS Region, privately, as if they were running in your own VPC.

Choose the link in the **AWS service** column to see the service documentation. The **Service name** column contains the service name that you specify when you create the interface endpoint.



- ** [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html) **
  - com.amazonaws.{{region}}.s3

- ** [AWS Identity and Access Management (IAM)](IAM/latest/UserGuide/reference_interface_vpc_endpoints.html) **
  - com.amazonaws.iam

- ** [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/vpc-endpoints.html) **
  - com.amazonaws.{{region}}.ecr.api
  - com.amazonaws.{{region}}.ecr.dkr

- ** [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/kms-vpc-endpoint.html) **
  - com.amazonaws.{{region}}.kms
  - com.amazonaws.{{region}}.kms-fips

- ** [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/vpc-endpoints.html) **
  - com.amazonaws.{{region}}.ecs

- ** [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc-endpoints.html)**
  - com.amazonaws.{{region}}.lambda

- ** [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/vpc.html) **
  - com.amazonaws.{{region}}.kinesis-firehose

- ** [Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/vpc-internet.html) **
  - com.amazonaws.{{region}}.kinesisanalytics
  - com.amazonaws.{{region}}.kinesisanalytics-fips

- ** Amazon Route 53**
  - com.amazonaws.route53



## View available AWS service names
<a name="vpce-view-available-services"></a>

You can use the [describe-vpc-endpoint-services](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-endpoint-services.html) command to view cross Region enabled services.

The following example displays the AWS services that a user in the `us-east-1` Region can access over interface endpoints, to the specified (`us-west-2`) service Region. The `--query` option limits the output to the service names.

```
aws ec2 describe-vpc-endpoint-services \
  --filters Name=service-type,Values=Interface Name=owner,Values=amazon \ 
  --region {{us-east-1}} \
  --service-region {{us-west-2}} \
  --query ServiceNames
```

The following is example output. The complete output is not shown.

```
[
    "com.amazonaws.us-west-2.ecr.api",
    "com.amazonaws.us-west-2.ecr.dkr",
    "com.amazonaws.us-west-2.ecs",
    "com.amazonaws.us-west-2.ecs-fips",
    ...
    "com.amazonaws.us-west-2.s3"
]
```

**Note**  
You must use regional DNS. Zonal DNS is not supported when accessing AWS services in another Region. For more information, see [View and update DNS attributes](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-updating) in the Amazon VPC User Guide. 

## Permissions and Considerations
<a name="endpoint-aws-service-cross-region"></a>
+ By default, IAM entities don't have permission to access an AWS service in another Region. To grant the permissions required for cross Region access, an IAM administrator can create IAM policies that allow the `vpce:AllowMultiRegion` permission-only action.
+ Ensure that your Service Control Policy (SCP) does not deny `vpce:AllowMultiRegion` permission-only action. To use AWS PrivateLink's cross-region connectivity feature, both your identity policy and your SCP must allow this action.
+ To control the Regions that an IAM entity can specify as a service Region when creating a VPC endpoint, use the `ec2:VpceServiceRegion` condition key.
+ A service consumer must opt in to an opt-in Region before selecting it as the service Region for an endpoint. Whenever possible, we recommend that service consumers access a service using intra-Region connectivity instead of cross-Region connectivity. Intra-Region connectivity provides lower latency and lower costs.
+ You can use IAM's new `aws:SourceVpcArn` global condition key to secure which Regions, AWS accounts and VPCs your resources can be accessed from. This key helps implement data residency and region based access control.
+ For high availability, create a cross Region enabled interface endpoint in at least two Availability Zones. In this case, providers and consumers are not required to use the same Availability Zones.
+ With cross Region access, AWS PrivateLink manages failover between Availability Zones in both service and consumer Regions. It does not manage failover across Regions.
+ Cross Region access is not supported for the following Availability Zones: `use1-az3`, `usw1-az2`, `apne1-az3`, `apne2-az2`, and `apne2-az4`.
+ You can use AWS Fault Injection Service to simulate regional events and model failure scenarios for in-region and cross-region enabled interface endpoints. To learn more, see [AWS FIS documentation](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html#network-actions-reference). 

## Create an interface endpoint to an AWS service in another Region
<a name="create-cross-region-vpce"></a>

To create an interface endpoint using the Console, see the [Create a VPC endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/create-interface-endpoint.html#create-interface-endpoint-aws) section.

In the CLI, you can use the [create-vpc-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpc-endpoint.html) command to create a VPC endpoint to an AWS service in a different Region. The following example creates an interface endpoint to Amazon S3 in `us-west-2` from a VPC in `us-east-1`.

```
aws ec2 create-vpc-endpoint \
  --vpc-id {{vpc-id}} \ 
  --service-name com.amazonaws.us-west-2.s3 \
  --vpc-endpoint-type Interface \
  --subnet-ids {{subnet-id-1 subnet-id-2}} \ 
  --region us-east-1 \
  --service-region us-west-2
```