# Connectivity / VPC Connection

Steps for VPC Connection:

1. Use existing VPC connection or create a new connection by following the [Amazon VPC documentation](../../../vpc/latest/userguide/create-vpc.md "../../../vpc/latest/userguide/create-vpc.md").
2. Make sure you have NAT Gateway which routes the traffic to internet.
3. Choose VPC endpoint as Amazon S3 Gateway to create connection.
4. Enable DNS resolution and DNS hostname to use AWS provided DNS Services.
5. Go to created VPC and add necessary endpoints for different services like STS, AWS Glue, Secret Managers.
   1. Choose Create Endpoint.
   2. For Service Category, choose AWS Services.
   3. For Service Name, choose the service that you are connecting to.
   4. Choose VPC and Enable DNS Name.
   5. VCP Endpoints required for VPC connection:
      1. [STS](../../../IAM/latest/UserGuide/reference_sts_vpc_endpoint_create.md "../../../IAM/latest/UserGuide/reference_sts_vpc_endpoint_create.md")
      2. [AWS Glue](vpc-interface-endpoints.md "vpc-interface-endpoints.md")
      3. [Secrets Manager](../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md "../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md")

## Security Group Configuration

Security group must allow traffic to its listening port from AWS Glue VPC for AWS Glue to be able to connect to it. It is a good practice to restrict the range of source IP addresses as much as possible.

AWS Glue requires special security group that allows all inbound traffic from itself. You can create a self-referencing rule that allows all traffic originating from the security group. You can modify an existing security group and specify the security group as source.

Open the communication from the HTTPS ports of the URL endpoint (either NLB or SAP instance).

## Connectivity options

- HTTPS connection with internal and external NLB, SSL certificate from certificate authority (CA), not self-signed SSL certificate
- HTTPS connection with SAP instance SSL certificate from certificate authority (CA), not self-signed SSL certificate
