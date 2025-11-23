# Cross-region enabled AWS services

The following AWS services integrate with cross Region AWS PrivateLink. You can create an interface endpoint
to connect to these services in another AWS Region, privately, as if they were running in your own VPC.

Choose the link in the **AWS service** column to see the service
documentation. The **Service name** column contains the service name that you specify when you
create the interface endpoint.

| AWS service                                                                                                                                                       | Service name                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| [Amazon S3](../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md "../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md")        | com.amazonaws.`region`.s3               |
| [AWS Identity and Access Management (IAM)](IAM/latest/UserGuide/reference_interface_vpc_endpoints.md "IAM/latest/UserGuide/reference_interface_vpc_endpoints.md") | com.amazonaws.iam                       |
| [Amazon ECR](../../../AmazonECR/latest/userguide/vpc-endpoints.md "../../../AmazonECR/latest/userguide/vpc-endpoints.md")                                         | com.amazonaws.`region`.ecr.api          |
| com.amazonaws.`region`.ecr.dkr                                                                                                                                    |
| [AWS Key Management Service](../../../kms/latest/developerguide/kms-vpc-endpoint.md "../../../kms/latest/developerguide/kms-vpc-endpoint.md")                     | com.amazonaws.`region`.kms              |
| com.amazonaws.`region`.kms-fips                                                                                                                                   |
| [Amazon ECS](../../../AmazonECS/latest/developerguide/vpc-endpoints.md "../../../AmazonECS/latest/developerguide/vpc-endpoints.md")                               | com.amazonaws.`region`.ecs              |
| [AWS Lambda](../../../lambda/latest/dg/configuration-vpc-endpoints.md "../../../lambda/latest/dg/configuration-vpc-endpoints.md")                                 | com.amazonaws.`region`.lambda           |
| [Amazon Data Firehose](../../../firehose/latest/dev/vpc.md "../../../firehose/latest/dev/vpc.md")                                                                 | com.amazonaws.`region`.kinesis-firehose |
| [Amazon Managed Service for Apache Flink](../../../managed-flink/latest/java/vpc-internet.md "../../../managed-flink/latest/java/vpc-internet.md")                | com.amazonaws.`region`.kinesisanalytics |
| com.amazonaws.`region`.kinesisanalytics-fips                                                                                                                      |
| Amazon Route 53                                                                                                                                                   | com.amazonaws.route53                   |

## View available AWS service

names

You can use the [describe-vpc-endpoint-services](../../../cli/latest/reference/ec2/describe-vpc-endpoint-services.md "../../../cli/latest/reference/ec2/describe-vpc-endpoint-services.md") command to view cross Region enabled services.

The following example displays the AWS services that a user in the `us-east-1` Region can access over interface endpoints, to
the specified (`us-west-2`) service Region. The `--query` option limits the output to the service
names.

```
aws ec2 describe-vpc-endpoint-services \
  --filters Name=service-type,Values=Interface Name=owner,Values=amazon \
  --region `us-east-1` \
  --service-region `us-west-2` \
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

###### Note

You must use regional DNS. Zonal DNS is not supported when accessing AWS services in another Region.
For more information, see [View
and update DNS attributes](../userguide/vpc-dns.md#vpc-dns-updating "../userguide/vpc-dns.md#vpc-dns-updating") in the Amazon VPC User Guide.

## Permissions and Considerations

- By default, IAM entities don't have permission to access an AWS service in another Region. To grant the permissions
  required for cross Region access, an IAM administrator can create IAM policies that allow
  the `vpce:AllowMultiRegion` permission-only action.
- Ensure that your Service Control Policy (SCP) does not deny `vpce:AllowMultiRegion` permission-only action. To use AWS PrivateLink's cross-region connectivity feature, both your identity policy and your SCP must allow this action.
- To control the Regions that an IAM entity can specify as a service Region when creating
  a VPC endpoint, use the `ec2:VpceServiceRegion` condition key.
- A service consumer must opt in to an opt-in Region before selecting it as the service
  Region for an endpoint. Whenever possible, we recommend that service consumers access a
  service using intra-Region connectivity instead of cross-Region connectivity.
  Intra-Region connectivity provides lower latency and lower costs.
- You can use IAM's new `aws:SourceVpcArn` global condition key to secure which Regions, AWS accounts and VPCs your resources can be accessed from. This key helps implement data residency and region based access control.
- For high availability, create a cross Region enabled interface endpoint in at least two Availability Zones.
  In this case, providers and consumers are not required to use the same Availability Zones.
- With cross Region access, AWS PrivateLink manages failover between Availability Zones in both service and consumer Regions.
  It does not manage failover across Regions.
- Cross Region access is not supported for the following Availability Zones:
  `use1-az3`, `usw1-az2`, `apne1-az3`,
  `apne2-az2`, and `apne2-az4`.
- You can use AWS Fault Injection Service to simulate regional events and model failure scenarios for in-region and cross-region enabled interface endpoints. To learn more, see [AWS FIS documentation](../../../fis/latest/userguide/fis-actions-reference.md#network-actions-reference "../../../fis/latest/userguide/fis-actions-reference.md#network-actions-reference").

## Create an interface endpoint to an AWS service in another Region

To create an interface endpoint using the Console, see the [Create a VPC endpoint](../userguide/create-interface-endpoint.md#create-interface-endpoint-aws "../userguide/create-interface-endpoint.md#create-interface-endpoint-aws") section.

In the CLI, you can use the [create-vpc-endpoint](../../../cli/latest/reference/ec2/create-vpc-endpoint.md "../../../cli/latest/reference/ec2/create-vpc-endpoint.md") command to create a VPC endpoint to an AWS service in a different Region. The following example creates an interface endpoint to Amazon S3 in `us-west-2` from a VPC in `us-east-1`.

```
aws ec2 create-vpc-endpoint \
  --vpc-id `vpc-id` \
  --service-name com.amazonaws.us-west-2.s3 \
  --vpc-endpoint-type Interface \
  --subnet-ids `subnet-id-1 subnet-id-2` \
  --region us-east-1 \
  --service-region us-west-2

```
