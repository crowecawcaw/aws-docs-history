# Internet access for VPC-connected workflows

When you connect an AWS HealthOmics run to a VPC, the run can only access resources available within that
VPC. To give your run access to the public internet or AWS services outside the VPC, you must configure your
VPC with the appropriate networking resources.

This topic describes how to set up your VPC to provide internet access and efficient connectivity to AWS
services for your VPC-connected runs. For information about connecting runs to a VPC, see
[Connecting HealthOmics workflows to a VPC](workflows-vpc-networking.md "workflows-vpc-networking.md").

###### Important

Connecting a run to a public subnet does not give it internet access or a public IP address. Always
use private subnets with NAT Gateway routes for runs requiring internet connectivity.

###### Topics

- [Setting up a VPC with internet access](#vpc-internet-setup "#vpc-internet-setup")
- [VPC endpoints for AWS services](#vpc-endpoints "#vpc-endpoints")
- [Security group configuration](#vpc-internet-security-groups "#vpc-internet-security-groups")
- [Route table configuration](#vpc-internet-route-tables "#vpc-internet-route-tables")
- [Testing VPC connectivity](#vpc-testing-connectivity "#vpc-testing-connectivity")
- [Examples](#vpc-internet-examples "#vpc-internet-examples")
- [Best practices](#vpc-internet-best-practices "#vpc-internet-best-practices")

## Setting up a VPC with internet access

To give your VPC-connected runs access to the internet, create a VPC with private subnets that route
outbound traffic through a NAT gateway.

This configuration provides:

- Private subnets for HealthOmics workflow tasks
- Public subnets with NAT gateways for outbound internet access

### Supported Regions and Availability Zones

HealthOmics Workflows operates in the following Regions and Availability Zones. When creating your VPC, ensure
that your subnets are in one or more of these Availability Zones.

| Region          | Availability Zone Name | Availability Zone ID |
| --------------- | ---------------------- | -------------------- |
| us-west-2       | us-west-2a             | usw2-az2             |
| us-west-2b      | usw2-az1               |
| us-west-2c      | usw2-az3               |
| us-east-1       | us-east-1a             | use1-az4             |
| us-east-1b      | use1-az6               |
| us-east-1c      | use1-az1               |
| us-east-1d      | use1-az2               |
| eu-west-1       | eu-west-1a             | euw1-az2             |
| eu-west-1b      | euw1-az3               |
| eu-west-1c      | euw1-az1               |
| eu-central-1    | eu-central-1a          | euc1-az2             |
| eu-central-1b   | euc1-az3               |
| eu-central-1c   | euc1-az1               |
| eu-west-2       | eu-west-2a             | euw2-az2             |
| eu-west-2b      | euw2-az3               |
| eu-west-2c      | euw2-az1               |
| ap-southeast-1  | ap-southeast-1a        | apse1-az2            |
| ap-southeast-1b | apse1-az1              |
| ap-southeast-1c | apse1-az3              |
| il-central-1    | il-central-1a          | ilc1-az1             |
| il-central-1b   | ilc1-az2               |
| il-central-1c   | ilc1-az3               |
| ap-northeast-2  | ap-northeast-2a        | apne2-az1            |
| ap-northeast-2b | apne2-az2              |
| ap-northeast-2c | apne2-az3              |

1. In the Amazon VPC console, choose **Create VPC**.
2. Select **VPC and more** to automatically create a VPC with public and private
   subnets.
3. Configure the following settings:
   - **Number of Availability Zones**: 2 or more
   - **Number of public subnets**: One per AZ. In this example,
     2
   - **Number of private subnets**: One per AZ. In this example,
     2
   - **NAT gateways**: 1 per AZ (for production) or 1 (for
     development/testing)
   - **VPC endpoints**: S3 Gateway endpoint (optional —
     in-Region Amazon S3 traffic is routed through the HealthOmics service VPC by default)

When you create your HealthOmics VPC configuration, specify the private subnets. The runs use the NAT gateway
in the public subnet to reach the internet.

## VPC endpoints for AWS services

You can configure VPC endpoints to allow runs to access AWS services without traversing the public
internet. This improves security and can reduce data transfer costs.

###### Note

In-Region Amazon S3 traffic is routed through the HealthOmics service VPC by default. If you configure Amazon S3
interface endpoints, traffic is routed through your VPC instead. We recommend using Amazon S3 gateway endpoints for
best performance and cost optimization. For more information, see [Gateway endpoints for Amazon S3](../../../vpc/latest/privatelink/vpc-endpoints-s3.md "../../../vpc/latest/privatelink/vpc-endpoints-s3.md") in the
_AWS PrivateLink Guide_.

The following table lists commonly used VPC endpoints for HealthOmics runs:

| Service             | Endpoint type | Endpoint name                  |
| ------------------- | ------------- | ------------------------------ |
| Amazon S3           | Gateway       | com.amazonaws.`region`.s3      |
| Amazon ECR (API)    | Interface     | com.amazonaws.`region`.ecr.api |
| Amazon ECR (Docker) | Interface     | com.amazonaws.`region`.ecr.dkr |
| SSM                 | Interface     | com.amazonaws.`region`.ssm     |
| CloudWatch Logs     | Interface     | com.amazonaws.`region`.logs    |

### NAT Gateway requirements

For runs requiring public internet access:

- NAT Gateway must be deployed in a public subnet
- Public subnet must have a route to an Internet Gateway
- Private subnets (where runs execute) must have routes to the NAT Gateway

###### Note

NAT Gateways incur hourly charges and data processing fees. For cost optimization, consider using
VPC endpoints for AWS service access instead of routing through NAT Gateway.

## Security group configuration

Configure your security groups to allow outbound traffic to the destinations your runs need to
access:

- **Public internet access** — Allow outbound HTTPS (port 443)
  traffic. Add rules for other protocols as needed, such as HTTP (port 80).
- **Specific services** — Configure rules based on your
  requirements.
- **On-premises resources** — Allow traffic to your VPN or
  CIDR ranges.

The following example shows a security group rule for public internet access:

| Type  | Protocol | Port range | Destination | Description             |
| ----- | -------- | ---------- | ----------- | ----------------------- |
| HTTPS | TCP      | 443        | 0.0.0.0/0   | Allow HTTPS to internet |

## Route table configuration

Ensure that your private subnets have route table entries that direct internet-bound traffic to a NAT
gateway:

| Destination | Target        |
| ----------- | ------------- |
| 10.0.0.0/16 | local         |
| 0.0.0.0/0   | nat-xxxxxxxxx |

For access to on-premises resources, configure routes to a virtual private gateway or
gateway.

## Testing VPC connectivity

Before running production workflows, validate that your VPC configuration allows connectivity to required
external services.

### Create a test workflow

Create a simple workflow that tests connectivity to your external service. For example, create a workflow
that attempts a TCP connection to a target service endpoint.

### Run the test

```
aws omics start-run \
  --workflow-id `test-workflow-id` \
  --role-arn `role-arn` \
  --output-uri s3://`bucket-name`/test-outputs/ \
  --networking-mode VPC \
  --configuration-name `configuration-name` \
  --parameters file://test-parameters.json
```

### Verify results

Check the workflow output to confirm successful connectivity:

```
{
  "connectivity_test.result": "Testing connection to external service...\nSUCCESS: Connection successful!\nTest completed"
}
```

If the test fails, verify the following:

- Security group rules allow outbound traffic to the required ports and
  destinations.
- Route tables direct traffic to a NAT gateway for internet access.
- The external service is accessible from your network.
- Sufficient ENIs are available in your account.
- The NAT gateway is in a public subnet with a route to an internet gateway.

###### Note

Network throughput begins at 10 Gbps per ENI and scales up to 100 Gbps over a 60-minute period with
sustained traffic. For workflows with immediate high-throughput requirements, please contact AWS
Support.

## Examples

### Accessing NCBI data with API authentication

This example demonstrates how to access NCBI data using the NCBI Datasets API with authentication.

###### Best practices for accessing NCBI resources

Customers should use REST API where possible, and utilize an API key provided by NCBI. Requests to access
NCBI resources, such as HTTP and FTP requests for public data, will come from HealthOmics and will be throttled at
the third party rate set by NCBI. You may experience run failures due to throttling errors during peak usage.
We encourage users to obtain their own NCBI API key and utilize specialized APIs to allow higher concurrency
and a better development experience.

To get your NCBI API key, visit the [NCBI API Keys documentation](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/api/api-keys/ "https://www.ncbi.nlm.nih.gov/datasets/docs/v2/api/api-keys/").

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
        # Download file from NCBI Datasets API with API key
        wget "~{ncbi_api_url}" -O gene_data.json

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

- Replace `<YOUR_API_KEY>` with your actual NCBI API key
- The workflow uses HTTPS to access the NCBI Datasets API
- The API key is passed as a URL parameter
- This approach provides higher rate limits (10 requests per second) compared to unauthenticated
  access (5 requests per second)

For more information about NCBI API keys and rate limits, see the
[NCBI Datasets API documentation](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/api/api-keys/ "https://www.ncbi.nlm.nih.gov/datasets/docs/v2/api/api-keys/").

## Best practices

1. **Use VPC endpoints for AWS services.** Configure VPC endpoints for
   Amazon S3, Amazon ECR, and other AWS services to reduce NAT gateway costs and improve performance. For more
   information, see [VPC endpoints for AWS services](#vpc-endpoints "#vpc-endpoints").
2. **Monitor network costs.** VPC networking incurs costs for NAT
   gateways, data transfer, and ENIs. Monitor your usage with AWS Cost Explorer.
3. **Plan for Availability Zones.** Ensure that your subnets span the
   Availability Zones where HealthOmics operates to support workflow placement.
4. **Use NAT gateways in each AZ.** For production workloads, deploy a
   NAT gateway in each Availability Zone to provide redundancy.
