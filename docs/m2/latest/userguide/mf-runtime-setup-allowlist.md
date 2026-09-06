

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Request the allowlist update for the account
<a name="mf-runtime-setup-allowlist"></a>

Work with your AWS representative to have your account allowlisted for the AWS Mainframe Modernization AMIs. Please provide the following information:
+ The AWS account ID.
+ The AWS Region where the Amazon VPC endpoint was created.
+ The Amazon VPC Amazon S3 endpoint ID created in [Create the Amazon VPC endpoint for Amazon S3](mf-runtime-setup-vpc.md). This is the `vpce-xxxxxxxxxxxxxxxxx` id for the **com.amazonaws.[region].s3 Gateway** endpoint.
+ The number of licenses required across all Rocket Software Enterprise Suite AMI Amazon EC2 instances.

  One license is required per CPU core (per 2 vCPUs for most Amazon EC2 instances).

  For more information, see [Optimize CPU options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html#cpu-options-compute-optimized).

  The requested number can be adjusted in the future by AWS.

**Note**  
Reach out to your AWS representative or AWS Support who will open the support ticket for the Allowlist request on your behalf. It can't be requested directly by you and the request may take several days to complete.