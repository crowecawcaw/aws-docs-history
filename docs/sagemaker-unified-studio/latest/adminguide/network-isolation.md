# Network isolation in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio can be configured to limit from where your data is accessed and exposure of that data over the public internet. You can interact with Amazon SageMaker Unified Studio, and dependent AWS services, directly through [interface endpoints](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in your Amazon VPC instead of connecting over the internet. When using Amazon VPC interface endpoints, communication between your Amazon VPC and Amazon SageMaker Unified Studio happens within the AWS network.

This topic discusses how customers can isolate their Amazon SageMaker Unified Studio portal experience by restricting Amazon SageMaker Unified Studio network traffic to stay within the AWS network.

## Prerequisites

Before implementing these solutions, ensure you have:

- Working knowledge of [Amazon SageMaker Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/ "https://aws.amazon.com/sagemaker/unified-studio/")
- Experience with [Amazon VPC](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/") and [subnet](../../../vpc/latest/userguide/configure-subnets.md "../../../vpc/latest/userguide/configure-subnets.md") configuration
- Administrator access to [IAM](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")
- Understanding of VPC [interface](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") and [gateway](../../../vpc/latest/privatelink/gateway-endpoints.md "../../../vpc/latest/privatelink/gateway-endpoints.md") endpoints
- Understanding of [Security best practices for your Amazon VPC](https://aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html "https://aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html")
- AWS CLI or AWS Console access with appropriate permissions

## Restrict Amazon SageMaker Unified Studio network traffic to within the AWS network

Your Amazon SageMaker Unified Studio domain and the data within can be configured to limit all traffic to only use the AWS network - and not pass through the public internet. With [AWS PrivateLink](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md"), AWS service endpoints can be provisioned within your Amazon VPC, keeping customer data within the AWS network.

This level of network isolation means:

- Customers can only use Amazon SageMaker Unified Studio within a configured Amazon VPC. AWS services, accessed through Amazon SageMaker Unified Studio, that support AWS PrivateLink do not send customer data over the public internet.
- Customer access to Amazon SageMaker Unified Studio and other AWS services from outside the Amazon VPC is denied. Customers cannot use Amazon SageMaker Unified Studio outside of the Amazon VPC. This includes denying access from the public internet.
- Access to the public internet is denied from the Amazon VPC. All network traffic must be served within the Amazon VPC, there is no access to the public internet. Access to public internet for non-customer data for items such as Amazon SageMaker Unified Studio web clients and client operations may be required.

###### Important

Amazon Athena for Apache Spark does not currently support Amazon VPC. If you require Amazon VPC connectivity for your Spark workloads, use Amazon EMR or AWS Glue instead.

###### Disable Amazon Athena Spark in Amazon VPC-enabled domains

If your organization requires all compute traffic to stay within the Amazon VPC, you can disable Amazon Athena Spark by using the following controls.

- **Account or organization-level SCP** — Apply a service control policy (SCP) that denies `athena:StartSession` and `athena:UpdateSession`.

The following IAM policy denies these actions for all Amazon Athena workgroups.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyAthenaSparkStartSession",
            "Effect": "Deny",
            "Action": [
                "athena:StartSession",
                "athena:UpdateSession"
            ],
            "Resource": [
                "arn:aws:athena:*:*:workgroup/*"
            ]
        }
    ]
}
```

The wildcard ARN `arn:aws:athena:*:*:workgroup/*` applies to all Regions and accounts. You can scope the policy to specific Regions, accounts, or workgroups by replacing the wildcards.

- **Tooling blueprint configuration** — Disable the Amazon Athena flag in tooling blueprints to prevent Amazon Athena (SQL) and Amazon Athena Spark from being provisioned in new projects.
- **Project-level policy updates** — Remove Amazon Athena Spark permissions from individual project IAM policies to restrict access at the project level.

If Amazon VPC endpoints are missing or misconfigured, network calls to Amazon SageMaker Unified Studio and other AWS services route over the public internet when that network path is available.

###### Step 1 - Deploy Amazon VPC endpoints

The Amazon SageMaker Unified Studio portal calls the following AWS services, each of which supports AWS PrivateLink Amazon VPC endpoints. The network traffic between the Amazon SageMaker Unified Studio portal and AWS services stays within the AWS network when the Amazon VPC endpoints are created in the Amazon VPC.

Create the Amazon VPC endpoint for each required AWS service API and any optional AWS service APIs from the tables below. To create a Amazon VPC endpoint see, [Access an AWS service using an interface Amazon VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md").

For the list of AWS Services with support for AWS PrivateLink see, [AWS services that integrate with AWS PrivateLink](../../../vpc/latest/privatelink/aws-services-privatelink-support.md "../../../vpc/latest/privatelink/aws-services-privatelink-support.md").

Amazon VPC endpoint considerations:

- For high availability it is recommended that Amazon VPC endpoints be deployed to multiple Availability Zones (AZ). The recommended minimum number of Availability Zones is two.
- Refer to [AWS PrivateLink pricing](https://aws.amazon.com/privatelink/pricing/ "https://aws.amazon.com/privatelink/pricing/") to understand the costs associated with Amazon VPC endpoints across Availability Zones.

###### Required Amazon VPC endpoints

These Amazon VPC endpoints are required for Amazon SageMaker Unified Studio and supporting services to function correctly.

| AWS service name              | Amazon VPC endpoint service name (API endpoint)                                                                                                                                |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Amazon Athena                 | com.amazonaws.<region>.athena                                                                                                                                                  |
| Amazon DataZone               | com.amazonaws.<region>.datazone<br>com.amazonaws.<region>.datazone-fips                                                                                                        |
| Amazon EC2                    | com.amazonaws.<region>.ec2<br>com.amazonaws.<region>.ec2-fips<br>com.amazonaws.<region>.ec2messages                                                                            |
| Amazon Q Developer            | com.amazonaws.<region>.q<br>com.amazonaws.us-east-1.codewhisperer<br>NoteAvailable only in us-east-1 region. Domains in different regions will use this endpoint.              |
| Amazon Simple Storage Service | com.amazonaws.<region>.s3                                                                                                                                                      |
| Amazon SageMaker AI           | com.amazonaws.<region>.sagemaker.api<br>com.amazonaws.<region>.sagemaker.runtime<br>com.amazonaws.<region>.sagemaker.api-fips<br>com.amazonaws.<region>.sagemaker.runtime-fips |
| AWS Glue                      | com.amazonaws.<region>.glue                                                                                                                                                    |
| AWS KMS                       | com.amazonaws.<region>.kms<br>com.amazonaws.<region>.kms-fips                                                                                                                  |
| AWS Secrets Manager           | com.amazonaws.<region>.secretsmanager                                                                                                                                          |
| AWS Security Token Service    | com.amazonaws.<region>.sts<br>com.amazonaws.<region>.sts-fips                                                                                                                  |
| AWS Systems Manager           | com.amazonaws.<region>.ssm<br>com.amazonaws.<region>.ssmmessages                                                                                                               |

###### Optional Amazon VPC endpoints

Create these Amazon VPC endpoints if you plan to deploy Amazon SageMaker Unified Studio projects that include blueprints using the services listed below.

| AWS service name              | Amazon VPC endpoint service name (API endpoint)                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon Bedrock                | com.amazonaws.<region>.bedrock-agent<br>com.amazonaws.<region>.bedrock-agent-runtime<br>com.amazonaws.<region>.bedrock-runtime                                                                                                                                                                                                                                                                    |
| Amazon Athena Spark           | com.amazonaws.<region>.athena.sessions<br>com.amazonaws.<region>.athena.dashboard<br>com.amazonaws.<region>.athena.persistent-dashboard                                                                                                                                                                                                                                                           |
| AWS Glue Interactive Sessions | com.amazonaws.<region>.glue.sessions                                                                                                                                                                                                                                                                                                                                                              |
| Amazon CloudWatch             | com.amazonaws.<region>.logs                                                                                                                                                                                                                                                                                                                                                                       |
| Amazon EMR                    | com.amazonaws.<region>.elasticmapreduce<br>com.amazonaws.<region>.elasticmapreduce-services<br>com.amazonaws.<region>.emr-serverless<br>com.amazonaws.<region>.emr-serverless-services.livy<br>com.amazonaws.<region>.emr-serverless-services.sessions<br>com.amazonaws.<region>.emr-serverless.dashboard<br>com.amazonaws.<region>.emr-dashboard<br>com.amazonaws.<region>.elasticmapreduce-fips |
| Amazon EMR on Amazon EKS      | com.amazonaws.<region>.emr-containers                                                                                                                                                                                                                                                                                                                                                             |
| Amazon RDS                    | com.amazonaws.<region>.rds<br>com.amazonaws.<region>.rds-fips                                                                                                                                                                                                                                                                                                                                     |
| Amazon Redshift               | com.amazonaws.<region>.redshift<br>com.amazonaws.<region>.redshift-data<br>com.amazonaws.<region>.redshift-serverless<br>com.amazonaws.<region>.redshift-fips<br>com.amazonaws.<region>.redshift-data-fips<br>com.amazonaws.<region>.redshift-serverless-fips                                                                                                                                     |
| Portal Query Editors          | com.amazonaws.<region>.sqlworkbench<br>com.amazonaws.<region>.sqlworkbench-v2                                                                                                                                                                                                                                                                                                                     |
| AWS CodeCommit                | com.amazonaws.<region>.codecommit<br>com.amazonaws.<region>.git-codecommit<br>com.amazonaws.<region>.codecommit-fips<br>com.amazonaws.<region>.git-codecommit-fips                                                                                                                                                                                                                                |
| AWS CodeConnections           | com.amazonaws.<region>.codeconnections.api<br>com.amazonaws.<region>.codestar-connections.api                                                                                                                                                                                                                                                                                                     |

###### Step 2: Create an IAM policy

Create an IAM policy that only allows the Amazon SageMaker Unified Studio Portal web client to call AWS service APIs through VPC endpoints deployed in an allowed VPC(s). The global context condition key [aws:SourceVpc](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcevpc "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcevpc") in the IAM policy can be used to enforce this access for AWS service callers ([Amazon SageMaker domain execution role](AmazonSageMakerDomainExecution.md "AmazonSageMakerDomainExecution.md"), IAM user or role), and [AWS Organizations service control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md").

This policy denies the Amazon SageMaker Unified Studio portal's access to all AWS service APIs when the API calls do not originate from within an allowed Amazon VPC. The `Deny` policy is applied when all of the three policy `Conditions` evaluate to `true`. You will need to replace the example VPC ID with your VPC ID or VPC ID list.

This policy may need to be modified if the domain execution role credentials are used in other contexts, or if this policy is applied to a role other than the domain execution role.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyUserAccessFromUnauthorizedVPCs",
            "Effect": "Deny",
            "Action": "*",
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "aws:SourceVpc": [
                        "vpc-1234567890abcdef0"
                    ]
                },
                "StringLike": {
                    "aws:userid": "*:user-*"
                },
                "BoolIfExists": {
                    "aws:ViaAWSService": "false"
                }
            }
        }
    ]
}
```

The following are details about the policy conditions:

```
"StringNotEquals": {
    "aws:SourceVpc": [
        "vpc-1234567890abcdef0"
    ]
}
```

This condition evaluates to `true` when the API call originates from a network location other than a VPC endpoint deployed in one of the allowed source Amazon VPC IDs.

```
"StringLike": { "aws:userid": "*:user-*" }
```

This condition evaluates to `true` for the domain execution role credentials issued to the Amazon SageMaker Unified Studio portal, so that the `Deny` policy is only applied for portal users. For example, the condition evaluates to `false` and the `Deny` policy is not applied when the Amazon SageMaker Unified Studio catalog service executes tasks that use the domain execution role.

```
"BoolIfExists": { "aws:ViaAWSService": "false" }
```

This condition evaluates to `true` when the API caller is not an AWS service (`aws:ViaAWSService` is `false`), which is the case for the Amazon SageMaker Unified Studio portal. When an AWS service calls another AWS service on behalf of the original caller, `aws:ViaAWSService` is `true` and the condition evaluates to `false` - allowing the AWS service call to another AWS service to succeed.

###### Step 3: Attach the custom policy

Attach the new custom policy to the SageMaker AI domain execution role. If SageMaker AI created this role for you it will be called [AmazonSageMakerDomainExecution](AmazonSageMakerDomainExecution.md "AmazonSageMakerDomainExecution.md"). The Amazon SageMaker Unified Studio portal uses the domain execution role for the Amazon SageMaker Unified Studio domain to call all AWS services. When a DENY by source Amazon VPC policy is added to the domain execution role, Amazon SageMaker Unified Studio portal calls to AWS service APIs from outside the allowed Amazon VPC will fail with `Access denied`. This policy can also be applied to an IAM user, IAM role or to an AWS Organizations service control policy.

## Public internet access

Public internet access is required to load Amazon SageMaker Unified Studio clients and for client operations that do not handle customer data.

###### Public internet access for Amazon SageMaker Unified Studio portal

Running the Amazon SageMaker Unified Studio portal web client requires public internet access to download client assets (portal web application, plugins, and user interface components) and to call client management APIs. Customer data is not transmitted through these calls. These endpoints are used by the Amazon SageMaker Unified Studio portal.

| Action                                                                                               | Endpoint                                                                                                                                                                                                                                                                                                               |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Portal asset delivery                                                                                | https://<domain\_id>.sagemaker.<region>.on.aws<br>NoteThe Amazon SageMaker Unified Studio portal URL for your domain.<br>https://\*.cdn.console.awsstatic.com<br>https://\*.cdn.uis.awsstatic.com<br>https://\*.shortbread.aws.dev<br>https://public.lotus.awt.aws.a2z.com                                             |
| Portal client APIs (Cookie management, customer feedback, UI business and operational metrics, etc.) | https://\*.console.api.aws<br>https://\*.console.aws.a2z.com<br>https://\*.execute-api.<region>.amazonaws.com<br>https://\*.sagemaker.aws<br>https://\*.sagemaker.aws.dev<br>https://agent.datazone.<region>.api.aws<br>https://monitoring.<region>.amazonaws.com<br>https://sagemaker-unified-studio.<region>.api.aws |

###### Public internet access for IAM Identity Center login to Amazon SageMaker Unified Studio portal

When the Amazon SageMaker Unified Studio portal web client logs into a domain using AWS Identity and Access Management Identity Center (IDC) Single Sign-On (IAM Identity Center), public internet access is required. These endpoints are used by the Amazon SageMaker Unified Studio portal.

| Action                                                                                         | Endpoint                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS Identity and Access Management Identity Center (IDC), Single Sign-On (IAM Identity Center) | https://assets.sso-portal.<region>.amazonaws.com<br>https://d35uxhjf90umnp.cloudfront.net<br>https://oidc.<region>.amazonaws.com<br>https://d-12345abcde.awsapps.com<br>NoteIDC IAM Identity Center application URL for the Amazon SageMaker Unified Studio domain<br>https://portal.sso.<region>.amazonaws.com<br>https://log.sso-portal.<region>.amazonaws.com<br>https://<region>.signin.aws |

###### Public internet access for Amazon SageMaker Unified Studio on AWS console

Running the Amazon SageMaker Unified Studio console web client requires public internet access to download client assets (console web application, plugins, and user interface components) and to call AWS console platform APIs. Customer data is not transmitted through these calls. These endpoints are used by the AWS console.

| Action                                                  | Endpoint                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Console asset delivery                                  | https://console.aws.amazon.com<br>https://\*.console.aws.amazon.com<br>https://\*.cdn.console.awsstatic.com<br>https://cdn.1.as2.amazonaws.com<br>https://cdn.2.as2.amazonaws.com<br>https://cdn.assets.as2.amazonaws.com<br>https://\*.cloudfront.net<br>NoteOne distribution endpoint needed for each region.                                                        |
| Sign-in                                                 | https://signin.aws.amazon.com<br>https://\*.signin.aws.amazon.com                                                                                                                                                                                                                                                                                                      |
| Console Control Service (console management / settings) | https://\*.ccs.amazonaws.com                                                                                                                                                                                                                                                                                                                                           |
| AWS User Notifications<br>• AWS Health category         | https://health.aws.amazon.com<br>https://phd.aws.amazon.com<br>https://\*.ctrl.prod.os.notifications.aws.dev                                                                                                                                                                                                                                                           |
| AWS User Experience Customization (UXC)                 | https://uxc.us-east-1.api.aws<br>NoteEndpoint is in us-east-1 only.                                                                                                                                                                                                                                                                                                    |
| Amazon Q for console                                    | https://conversational-experience-worker.widget.console.aws.amazon.com                                                                                                                                                                                                                                                                                                 |
| Console unified search                                  | https://unifiedsearch.amazonaws.com/<br>https://\*.unifiedsearch.amazonaws.com                                                                                                                                                                                                                                                                                         |
| Console platform APIs                                   | https://account.\*.api.aws<br>https://\*.console.api.aws<br>https://\*.console-api.aws.amazon.com<br>https://\*.console.aws.a2z.com<br>https://freetier.us-east-1.api.aws<br>NoteEndpoint is in us-east-1 only.<br>NoteFor regions in the [AWS Regions (partition)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md") |

###### Public internet access for IAM login to Amazon SageMaker Unified Studio portal

Amazon SageMaker Unified Studio domains that use IAM login for the Portal web client require the Amazon SageMaker Unified Studio Console. See the public internet access requirements for the Amazon SageMaker Unified Studio on AWS console above.

## Amazon VPC troubleshooting

This section helps you diagnose and resolve common Amazon VPC configuration issues that affect notebook connectivity in Amazon SageMaker Unified Studio. Use the following table to identify your subnet configuration and determine the appropriate recovery action.

| Scenario (Subnet 1 type, Subnet 2 type) | Expected behavior              | Recovery action                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Private with NAT + Private with NAT     | Works as expected              | No action needed                                                                                                                                                                                                                                                                                                                                                     |
| Private no NAT + Private no NAT         | Only local Python kernel works | Add NAT ([Add a NAT gateway to a private subnet](#vpc-troubleshoot-add-nat "#vpc-troubleshoot-add-nat")) or add Amazon VPC endpoints ([Add Amazon VPC endpoints](#vpc-troubleshoot-add-vpce "#vpc-troubleshoot-add-vpce"))                                                                                                                                           |
| Public + Public                         | Only local Python kernel works | Convert to private ([Convert a public subnet to a private subnet](#vpc-troubleshoot-convert-public "#vpc-troubleshoot-convert-public")) or add Amazon VPC endpoints ([Add Amazon VPC endpoints](#vpc-troubleshoot-add-vpce "#vpc-troubleshoot-add-vpce"))                                                                                                            |
| Private with NAT + Public               | Works as expected              | No action needed                                                                                                                                                                                                                                                                                                                                                     |
| Private no NAT + Public                 | Only local Python kernel works | Convert to private ([Convert a public subnet to a private subnet](#vpc-troubleshoot-convert-public "#vpc-troubleshoot-convert-public")), add NAT ([Add a NAT gateway to a private subnet](#vpc-troubleshoot-add-nat "#vpc-troubleshoot-add-nat")), or add Amazon VPC endpoints ([Add Amazon VPC endpoints](#vpc-troubleshoot-add-vpce "#vpc-troubleshoot-add-vpce")) |

### Convert a public subnet to a private subnet

A public subnet has a route to an internet gateway (IGW), which allows resources in the subnet to communicate directly with the internet. To convert a public subnet to a private subnet, remove the IGW route and disable auto-assign public IP.

###### Note

Existing instances in the subnet retain their public IP addresses after you make this change. Any services that rely on inbound internet access stop working. To maintain outbound access for package installations and AWS API calls, set up a NAT gateway or Amazon VPC endpoints before converting the subnet.

###### To convert a public subnet to a private subnet

1. Open the Amazon Virtual Private Cloud console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Route tables**.
3. Select the route table associated with your public subnet.
4. Choose the **Routes** tab.
5. Choose **Edit routes**.
6. Choose **Remove** for the route with destination `0.0.0.0/0` that targets an internet gateway (`igw-xxx`).
7. Choose **Save changes**.

###### To disable auto-assign public IP

1. In the navigation pane, choose **Subnets**.
2. Select your subnet.
3. Choose **Actions**, **Edit subnet settings**.
4. Clear the **Enable auto-assign public IPv4 address** checkbox.
5. Choose **Save**.

(Optional) If instances in the subnet need outbound internet access, add a NAT gateway route. For instructions, see [Add a NAT gateway to a private subnet](#vpc-troubleshoot-add-nat "#vpc-troubleshoot-add-nat").

###### To verify the conversion

1. In the navigation pane, choose **Subnets**.
2. Select your subnet and choose the **Route table** tab.
3. Confirm that no route with destination `0.0.0.0/0` targets an internet gateway.

### Add a NAT gateway to a private subnet

A NAT gateway allows instances in a private subnet to connect to the internet for outbound traffic while preventing unsolicited inbound connections. You must have a public subnet with an internet gateway route before you create a NAT gateway.

###### To create a NAT gateway

1. Open the Amazon Virtual Private Cloud console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **NAT gateways**.
3. Choose **Create NAT gateway**.
4. For **Subnet**, select a public subnet that has a route to an internet gateway.
5. For **Connectivity type**, select **Public**.
6. Choose **Allocate Elastic IP** to assign a new Elastic IP address to the NAT gateway.
7. Choose **Create NAT gateway**.

###### To update the private subnet route table

1. In the navigation pane, choose **Route tables**.
2. Select the route table associated with your private subnet.
3. Choose the **Routes** tab.
4. Choose **Edit routes**.
5. Choose **Add route**. For **Destination**, enter `0.0.0.0/0`. For **Target**, select the NAT gateway that you created.
6. Choose **Save changes**.

###### To verify the NAT gateway

1. In the navigation pane, choose **NAT gateways**.
2. Confirm that the NAT gateway status is **Available**.
3. In the navigation pane, choose **Route tables** and select the private subnet route table.
4. Confirm that the `0.0.0.0/0` route targets the NAT gateway.

### Add Amazon VPC endpoints

Amazon VPC endpoints allow resources in your private subnets to communicate with AWS services without requiring internet access. There are two types of Amazon VPC endpoints:

- **Gateway endpoints** – For Amazon Simple Storage Service and Amazon DynamoDB. Gateway endpoints are free of charge.
- **Interface endpoints** – For other AWS services such as AWS Security Token Service, Amazon CloudWatch, Amazon ECR, and AWS Systems Manager. Interface endpoints cost approximately $0.01 per hour per Availability Zone, plus data processing charges.

The following are common endpoints to add for Amazon SageMaker Unified Studio notebook connectivity:

- Amazon Simple Storage Service (gateway)
- Amazon DynamoDB (gateway)
- AWS Security Token Service (interface)
- Amazon ECR – `ecr.api` and `ecr.dkr` (interface)
- Amazon CloudWatch Logs (interface)
- AWS Systems Manager (interface)

###### To create a gateway endpoint

1. Open the Amazon Virtual Private Cloud console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Choose **Create endpoint**.
4. For **Service category**, select **AWS services**.
5. Search for and select the gateway service (for example, `com.amazonaws.<region>.s3` with type **Gateway**).
6. For **VPC**, select your Amazon VPC.
7. For **Route tables**, select the route tables associated with your private subnets.
8. Choose **Create endpoint**.

###### To create an interface endpoint

1. Open the Amazon Virtual Private Cloud console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Choose **Create endpoint**.
4. For **Service category**, select **AWS services**.
5. Search for and select the interface service (for example, `com.amazonaws.<region>.sts`).
6. For **VPC**, select your Amazon VPC.
7. For **Subnets**, select the subnets in your private subnet Availability Zones.
8. For **Security groups**, select a security group that allows inbound traffic on port 443 (HTTPS).
9. Select **Enable DNS name** to turn on private DNS for the endpoint.
10. Choose **Create endpoint**.

###### To verify Amazon VPC endpoints

1. In the navigation pane, choose **Endpoints**.
2. Confirm that each endpoint status is **Available**.
3. For gateway endpoints, choose **Route tables** in the navigation pane and confirm that the route table includes a route for the endpoint.
