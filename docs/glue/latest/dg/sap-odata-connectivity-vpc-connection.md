

# Connectivity / VPC Connection
<a name="sap-odata-connectivity-vpc-connection"></a>

Steps for VPC Connection:

1. Use existing VPC connection or create a new connection by following the [Amazon VPC documentation](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html).

1. Make sure you have NAT Gateway which routes the traffic to internet.

1. Choose VPC endpoint as Amazon S3 Gateway to create connection.

1. Enable DNS resolution and DNS hostname to use AWS provided DNS Services.

1. Go to created VPC and add necessary endpoints for different services like STS, AWS Glue, Secret Managers.

   1. Choose Create Endpoint.

   1. For Service Category, choose AWS Services.

   1. For Service Name, choose the service that you are connecting to.

   1. Choose VPC and Enable DNS Name.

   1. VCP Endpoints required for VPC connection:

      1. [STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sts_vpc_endpoint_create.html)

      1. [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/vpc-interface-endpoints.html)

      1. [Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/vpc-endpoint-overview.html)

## Security Group Configuration
<a name="sap-odata-security-group-configuration"></a>

Security group must allow traffic to its listening port from AWS Glue VPC for AWS Glue to be able to connect to it. It is a good practice to restrict the range of source IP addresses as much as possible. 

AWS Glue requires special security group that allows all inbound traffic from itself. You can create a self-referencing rule that allows all traffic originating from the security group. You can modify an existing security group and specify the security group as source.

Open the communication from the HTTPS ports of the URL endpoint (either NLB or SAP instance).

## Connectivity options
<a name="sap-odata-connectivity-options"></a>
+ HTTPS connection with internal and external NLB, SSL certificate from certificate authority (CA), not self-signed SSL certificate
+ HTTPS connection with SAP instance SSL certificate from certificate authority (CA), not self-signed SSL certificate