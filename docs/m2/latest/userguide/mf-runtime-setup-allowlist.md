AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Request the allowlist update for the account

Work with your AWS representative to have your account allowlisted for the AWS Mainframe Modernization AMIs.
Please provide the following information:

- The AWS account ID.
- The AWS Region where the Amazon VPC endpoint was created.
- The Amazon VPC Amazon S3 endpoint ID created in [Create the Amazon VPC endpoint for Amazon S3](mf-runtime-setup-vpc.md "mf-runtime-setup-vpc.md").
  This is the `vpce-xxxxxxxxxxxxxxxxx` id for the **com.amazonaws.[region].s3 Gateway** endpoint.
- The number of licenses required across all Rocket Software Enterprise Suite AMI Amazon EC2
  instances.

One license is required per CPU core (per 2 vCPUs for most Amazon EC2 instances).

For more information, see [Optimize CPU options](../../../AWSEC2/latest/UserGuide/instance-optimize-cpu.md#cpu-options-compute-optimized "../../../AWSEC2/latest/UserGuide/instance-optimize-cpu.md#cpu-options-compute-optimized").

The requested number can be adjusted in the future by AWS.

###### Note

Reach out to your AWS representative or AWS Support who will open the support ticket for
the Allowlist request on your behalf. It can't be requested directly by you and the request may
take several days to complete.
