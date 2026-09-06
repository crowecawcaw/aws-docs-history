

# Internet access for VPC-connected workflows
<a name="workflows-vpc-internet"></a>

When you connect an AWS HealthOmics run to a VPC, the run can only access resources available within that VPC. To give your run access to the public internet or AWS services outside the VPC, you must configure your VPC with the appropriate networking resources.

This topic describes how to set up your VPC to provide internet access and efficient connectivity to AWS services for your VPC-connected runs. For information about connecting runs to a VPC, see [Connecting HealthOmics workflows to a VPC](workflows-vpc-networking.md).

**Important**  
Connecting a run to a public subnet does not give it internet access or a public IP address. Always use private subnets with NAT Gateway routes for runs requiring internet connectivity.

**Topics**
+ [Setting up a VPC with internet access](#vpc-internet-setup)
+ [VPC endpoints for AWS services](#vpc-endpoints)
+ [Security group configuration](#vpc-internet-security-groups)
+ [Route table configuration](#vpc-internet-route-tables)
+ [IAM permissions for AWS services](#vpc-iam-permissions)
+ [Testing VPC connectivity](#vpc-testing-connectivity)
+ [Examples](#vpc-internet-examples)
+ [Best practices](#vpc-internet-best-practices)

## Setting up a VPC with internet access
<a name="vpc-internet-setup"></a>

To give your VPC-connected runs access to the internet, create a VPC with private subnets that route outbound traffic through a NAT gateway.

This configuration provides:
+ Private subnets for HealthOmics workflow tasks
+ Public subnets with NAT gateways for outbound internet access

### Supported Regions and Availability Zones
<a name="vpc-internet-regions-azs"></a>

HealthOmics Workflows operates in the following Regions and Availability Zones. When creating your VPC, ensure that your subnets are in one or more of these Availability Zones.



- **us-west-2**
  - **Availability Zone Name:** us-west-2a / **Availability Zone ID:** usw2-az2
  - **Availability Zone Name:** us-west-2b / **Availability Zone ID:** usw2-az1
  - **Availability Zone Name:** us-west-2c / **Availability Zone ID:** usw2-az3
  - **Availability Zone Name:** us-west-2d / **Availability Zone ID:** usw2-az4

- **us-east-1**
  - **Availability Zone Name:** us-east-1a / **Availability Zone ID:** use1-az4
  - **Availability Zone Name:** us-east-1b / **Availability Zone ID:** use1-az6
  - **Availability Zone Name:** us-east-1c / **Availability Zone ID:** use1-az1
  - **Availability Zone Name:** us-east-1d / **Availability Zone ID:** use1-az2
  - **Availability Zone Name:** us-east-1f / **Availability Zone ID:** use1-az5

- **eu-west-1**
  - **Availability Zone Name:** eu-west-1a / **Availability Zone ID:** euw1-az2
  - **Availability Zone Name:** eu-west-1b / **Availability Zone ID:** euw1-az3
  - **Availability Zone Name:** eu-west-1c / **Availability Zone ID:** euw1-az1

- **eu-central-1**
  - **Availability Zone Name:** eu-central-1a / **Availability Zone ID:** euc1-az2
  - **Availability Zone Name:** eu-central-1b / **Availability Zone ID:** euc1-az3
  - **Availability Zone Name:** eu-central-1c / **Availability Zone ID:** euc1-az1

- **eu-west-2**
  - **Availability Zone Name:** eu-west-2a / **Availability Zone ID:** euw2-az2
  - **Availability Zone Name:** eu-west-2b / **Availability Zone ID:** euw2-az3
  - **Availability Zone Name:** eu-west-2c / **Availability Zone ID:** euw2-az1

- **ap-southeast-1**
  - **Availability Zone Name:** ap-southeast-1a / **Availability Zone ID:** apse1-az2
  - **Availability Zone Name:** ap-southeast-1b / **Availability Zone ID:** apse1-az1
  - **Availability Zone Name:** ap-southeast-1c / **Availability Zone ID:** apse1-az3

- **il-central-1**
  - **Availability Zone Name:** il-central-1a / **Availability Zone ID:** ilc1-az1
  - **Availability Zone Name:** il-central-1b / **Availability Zone ID:** ilc1-az2
  - **Availability Zone Name:** il-central-1c / **Availability Zone ID:** ilc1-az3

- **ap-northeast-2**
  - **Availability Zone Name:** ap-northeast-2a / **Availability Zone ID:** apne2-az1
  - **Availability Zone Name:** ap-northeast-2b / **Availability Zone ID:** apne2-az2
  - **Availability Zone Name:** ap-northeast-2c / **Availability Zone ID:** apne2-az3

- **ap-northeast-1**
  - **Availability Zone Name:** ap-northeast-1a / **Availability Zone ID:** apne1-az4
  - **Availability Zone Name:** ap-northeast-1c / **Availability Zone ID:** apne1-az1
  - **Availability Zone Name:** ap-northeast-1d / **Availability Zone ID:** apne1-az2

- **us-east-2**
  - **Availability Zone Name:** us-east-2a / **Availability Zone ID:** use2-az1
  - **Availability Zone Name:** us-east-2b / **Availability Zone ID:** use2-az2
  - **Availability Zone Name:** us-east-2c / **Availability Zone ID:** use2-az3



1. In the Amazon VPC console, choose **Create VPC**.

1. Select **VPC and more** to automatically create a VPC with public and private subnets.

1. Configure the following settings:
   + **Number of Availability Zones**: 2 or more
   + **Number of public subnets**: One per AZ. In this example, 2
   + **Number of private subnets**: One per AZ. In this example, 2
   + **NAT gateways**: 1 per AZ (for production) or 1 (for development/testing)
   + **VPC endpoints**: S3 Gateway endpoint (optional — in-Region Amazon S3 traffic is routed through the HealthOmics service VPC by default)

When you create your HealthOmics VPC configuration, specify the private subnets. The runs use the NAT gateway in the public subnet to reach the internet.

## VPC endpoints for AWS services
<a name="vpc-endpoints"></a>

You can configure VPC endpoints to allow runs to access AWS services without traversing the public internet. This improves security and can reduce data transfer costs.

**Important**  
If your workflow definition needs to access AWS services (such as Amazon Athena queries, Amazon DynamoDB operations, or other API calls), you must ensure that the required VPC endpoints are configured in your VPC. Without the appropriate endpoints, your workflow may fail with authentication or connectivity errors.

**Note**  
In-Region Amazon S3 traffic is routed through the HealthOmics service VPC by default. If you configure Amazon S3 interface endpoints, traffic is routed through your VPC instead. We recommend using Amazon S3 gateway endpoints for best performance and cost optimization. For more information, see [Gateway endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html) in the *AWS PrivateLink Guide*.

The following table lists commonly used VPC endpoints for HealthOmics runs:


| Service | Endpoint type | Endpoint name | 
| --- | --- | --- | 
| Amazon S3 | Gateway | com.amazonaws.{{region}}.s3 | 
| Amazon S3 Tables | Interface | com.amazonaws.{{region}}.s3tables | 
| Amazon ECR (API) | Interface | com.amazonaws.{{region}}.ecr.api | 
| Amazon ECR (Docker) | Interface | com.amazonaws.{{region}}.ecr.dkr | 
| SSM | Interface | com.amazonaws.{{region}}.ssm | 
| CloudWatch Logs | Interface | com.amazonaws.{{region}}.logs | 
| Amazon Athena | Interface | com.amazonaws.{{region}}.athena | 

The full list of services that you can access through AWS PrivateLink endpoints can be found in [AWS services that integrate with AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/aws-services-privatelink-support.html). For detailed endpoint setup instructions, see [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the *AWS PrivateLink Guide*.

### NAT Gateway requirements
<a name="vpc-nat-gateway-requirements"></a>

For runs requiring public internet access:
+ NAT Gateway must be deployed in a public subnet
+ Public subnet must have a route to an Internet Gateway
+ Private subnets (where runs execute) must have routes to the NAT Gateway

**Note**  
NAT Gateways incur hourly charges and data processing fees. For cost optimization, consider using VPC endpoints for AWS service access instead of routing through NAT Gateway.

## Security group configuration
<a name="vpc-internet-security-groups"></a>

Configure your security groups to allow outbound traffic to the destinations your runs need to access:
+ **Public internet access** — Allow outbound HTTPS (port 443) traffic. Add rules for other protocols as needed, such as HTTP (port 80).
+ **Specific services** — Configure rules based on your requirements.
+ **On-premises resources** — Allow traffic to your VPN or CIDR ranges.

The following example shows a security group rule for public internet access:


| Type | Protocol | Port range | Destination | Description | 
| --- | --- | --- | --- | --- | 
| HTTPS | TCP | 443 | 0.0.0.0/0 | Allow HTTPS to internet | 

## Route table configuration
<a name="vpc-internet-route-tables"></a>

Ensure that your private subnets have route table entries that direct internet-bound traffic to a NAT gateway:


| Destination | Target | 
| --- | --- | 
| 10.0.0.0/16 | local | 
| 0.0.0.0/0 | nat-xxxxxxxxx | 

For access to on-premises resources, configure routes to a virtual private gateway or gateway.

## IAM permissions for AWS services
<a name="vpc-iam-permissions"></a>

When your workflow tasks access AWS services such as Amazon Athena, AWS Glue, or Amazon DynamoDB in VPC networking mode, you must add the necessary permissions to the service role that you pass to the `StartRun` API. Without these permissions, your workflow tasks will fail with `AccessDeniedException` or `UnauthorizedException` errors.

**Important**  
The service role permissions are separate from VPC networking configuration. Even with properly configured VPC endpoints and security groups, your workflow will fail if the service role lacks the required IAM permissions.

If your workflow fails with permission errors, check the CloudWatch Logs logs for your workflow run. Common error messages include `AccessDeniedException: You are not authorized to perform: action on the resource` (the service role is missing the required IAM permission) or `UnrecognizedClientException: The security token included in the request is invalid` (the service role trust policy may be misconfigured, or the role ARN passed to `StartRun` is incorrect).

### Common service permissions
<a name="vpc-iam-common-services"></a>

The following examples show IAM permissions for commonly used AWS services in VPC mode workflows. Add these permissions to your service role policy based on which services your workflow accesses.

**Example permissions**  
For workflows that run queries:  

```
{
  "Effect": "Allow",
  "Action": [
    "athena:StartQueryExecution",
    "athena:GetQueryExecution",
    "athena:GetQueryResults",
    "athena:StopQueryExecution"
  ],
  "Resource": "arn:aws:athena:{{region}}:{{account-id}}:workgroup/{{workgroup-name}}"
}
```

**Example AWS Glue Data Catalog permissions**  
For workflows that access AWS Glue databases and tables (commonly used with Amazon Athena):  

```
{
  "Effect": "Allow",
  "Action": [
    "glue:GetDatabase",
    "glue:GetTable",
    "glue:GetPartitions",
    "glue:CreateTable",
    "glue:UpdateTable"
  ],
  "Resource": [
    "arn:aws:glue:{{region}}:{{account-id}}:catalog",
    "arn:aws:glue:{{region}}:{{account-id}}:database/{{database-name}}",
    "arn:aws:glue:{{region}}:{{account-id}}:table/{{database-name}}/*"
  ]
}
```
If you use AWS Lake Formation to manage permissions for your AWS Glue Data Catalog, you must also grant the appropriate Lake Formation permissions. For more information, see [Lake Formation permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/lake-formation-permissions.html) in the *AWS Lake Formation Developer Guide*.

**Example DynamoDB permissions**  
For workflows that read from or write to DynamoDB tables:  

```
{
  "Effect": "Allow",
  "Action": [
    "dynamodb:GetItem",
    "dynamodb:PutItem",
    "dynamodb:Query",
    "dynamodb:Scan"
  ],
  "Resource": "arn:aws:dynamodb:{{region}}:{{account-id}}:table/{{table-name}}"
}
```

**Example Amazon S3 Tables permissions**  
For workflows that read from or write to Amazon S3 Tables:  

```
{
  "Effect": "Allow",
  "Action": [
    "s3tables:GetTableData",
    "s3tables:PutTableData"
  ],
  "Resource": "arn:aws:s3tables:{{region}}:{{account-id}}:bucket/{{bucket-name}}/table/{{table-id}}"
}
```
Amazon S3 Tables uses a different endpoint than Amazon S3. You must configure a VPC endpoint for Amazon S3 Tables and ensure your security group allows outbound HTTPS traffic (port 443) to the Amazon S3 Tables service.

## Testing VPC connectivity
<a name="vpc-testing-connectivity"></a>

Before running production workflows, validate that your VPC configuration allows connectivity to required external services.

### Create a test workflow
<a name="vpc-test-workflow"></a>

Create a simple workflow that tests connectivity to your external service. For example, create a workflow that attempts a TCP connection to a target service endpoint.

### Run the test
<a name="vpc-run-test"></a>

```
aws omics start-run \
  --workflow-id {{test-workflow-id}} \
  --role-arn {{role-arn}} \
  --output-uri s3://{{bucket-name}}/test-outputs/ \
  --networking-mode VPC \
  --configuration-name {{configuration-name}} \
  --parameters file://test-parameters.json
```

### Verify results
<a name="vpc-verify-results"></a>

Check the workflow output to confirm successful connectivity:

```
{
  "connectivity_test.result": "Testing connection to external service...\nSUCCESS: Connection successful!\nTest completed"
}
```

If the test fails, verify the following:
+ Security group rules allow outbound traffic to the required ports and destinations.
+ Route tables direct traffic to a NAT gateway for internet access.
+ The external service is accessible from your network.
+ Sufficient ENIs are available in your account.
+ The NAT gateway is in a public subnet with a route to an internet gateway.

**Note**  
Network throughput begins at 10 Gbps per ENI and scales up to 100 Gbps over a 60-minute period with sustained traffic. For workflows with immediate high-throughput requirements, please contact AWS Support.

## Examples
<a name="vpc-internet-examples"></a>

### Accessing NCBI data with API authentication
<a name="vpc-example-ncbi"></a>

This example demonstrates how to access NCBI data using the NCBI Datasets API with authentication.

**Best practices for accessing NCBI resources**  
Customers should use REST API where possible, and utilize an API key provided by NCBI. Requests to access NCBI resources, such as HTTP and FTP requests for public data, will come from HealthOmics and will be throttled at the third party rate set by NCBI. You may experience run failures due to throttling errors during peak usage. We encourage users to obtain their own NCBI API key and utilize specialized APIs to allow higher concurrency and a better development experience.

To get your NCBI API key, visit the [ NCBI API Keys documentation](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/api/api-keys/).

**Example workflow definition:**

```
version 1.0
#WORKFLOW DEFINITION

# Meant to be used as integration test for public internet access via VPC tunnel
workflow TestFlow {
    input {
        String ncbi_api_url = "https://api.ncbi.nlm.nih.gov/datasets/v2/gene/accession/NM_021803.4?api_key=<YOUR_API_KEY>"
    }

    call DataProcessTask{
        input:
            ncbi_api_url = ncbi_api_url,
    }

    output {
        File output_file = DataProcessTask.output_file
    }

}

#Task Definitions
task DataProcessTask {
    input {
        String ncbi_api_url
    }

    command <<<
        set -eu
        # Download file from NCBI Datasets API with API key
        curl -fsSL "~{ncbi_api_url}" -o gene_data.json

        # Add data processing task here
        cat gene_data.json > processed_data.json

        # Echo the content to output file
        cat processed_data.json > outfile.txt
    >>>

    output {
        File output_file = "outfile.txt"
    }
}
```

**Key points:**
+ Replace `<YOUR_API_KEY>` with your actual NCBI API key
+ The workflow uses HTTPS to access the NCBI Datasets API
+ The API key is passed as a URL parameter
+ This approach provides higher rate limits (10 requests per second) compared to unauthenticated access (5 requests per second)

For more information about NCBI API keys and rate limits, see the [NCBI Datasets API documentation](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/api/api-keys/).

## Best practices
<a name="vpc-internet-best-practices"></a>

1. **Use VPC endpoints for AWS services.** Configure VPC endpoints for Amazon S3, Amazon ECR, and other AWS services to reduce NAT gateway costs and improve performance. For more information, see [VPC endpoints for AWS services](#vpc-endpoints).

1. **Monitor network costs.** VPC networking incurs costs for NAT gateways, data transfer, and ENIs. Monitor your usage with AWS Cost Explorer.

1. **Plan for Availability Zones.** Ensure that your subnets span the Availability Zones where HealthOmics operates to support workflow placement.

1. **Use NAT gateways in each AZ.** For production workloads, deploy a NAT gateway in each Availability Zone to provide redundancy.