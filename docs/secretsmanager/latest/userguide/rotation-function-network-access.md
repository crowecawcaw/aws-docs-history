# Network access for AWS Lambda rotation function

For [Rotation by Lambda function](rotate-secrets_lambda.md "rotate-secrets_lambda.md"), when Secrets Manager uses a Lambda function to rotate a secret, the Lambda rotation function must be able to access the secret. If your secret contains credentials, then the Lambda function must also be able to access the source of those credentials, such as a database or service.

**To access a secret**

Your Lambda rotation function must be able to access a Secrets Manager endpoint. If your
Lambda function can access the internet, then you can use a public endpoint. To find an
endpoint, see [AWS Secrets Manager endpoints](asm_access.md#endpoints "asm_access.md#endpoints").

If your Lambda function runs in a VPC that doesn't have internet access, we
recommend you configure Secrets Manager service private endpoints within your VPC. Your VPC can
then intercept requests addressed to the public regional endpoint and redirect them to
the private endpoint. For more information, see [VPC endpoints
(AWS PrivateLink)](vpc-endpoint-overview.md "vpc-endpoint-overview.md").

Alternatively, you can enable your Lambda function to access a Secrets Manager public endpoint
by adding a [NAT gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") or an [internet gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md") to your VPC, which allows traffic from your VPC to reach the
public endpoint. This exposes your VPC to more risk because an IP address for the
gateway can be attacked from the public Internet.

**(Optional) To access the database or service**

For secrets such as API keys, there is no source database or service that you need to update along with the secret.

If your database or service is running on an Amazon EC2 instance in a VPC, we recommend
that you configure your Lambda function to run in the same VPC. Then the rotation
function can communicate directly with your service. For more information, see [Configuring VPC access](../../../lambda/latest/dg/configuration-vpc.md#vpc-configuring "../../../lambda/latest/dg/configuration-vpc.md#vpc-configuring").

To allow the Lambda function to access the database or service, you must make
sure that the security groups attached to your Lambda rotation function allow
outbound connections to the database or service. You must also make sure that
the security groups attached to your database or service allow inbound
connections from the Lambda rotation function.
