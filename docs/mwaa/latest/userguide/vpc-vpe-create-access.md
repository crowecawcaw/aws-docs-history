# Creating the required VPC service endpoints in an Amazon VPC with private routing

An existing Amazon VPC network without internet access needs additional VPC service endpoints (AWS PrivateLink) to use Apache Airflow on Amazon Managed Workflows for Apache Airflow. This page describes the VPC endpoints required for the AWS services used by Amazon MWAA, the VPC endpoints required for Apache Airflow, and how to create and attach the VPC endpoints to an existing Amazon VPC with private routing.

###### Contents

- [Pricing](vpc-vpe-create-access.md#vpc-vpe-create-pricing "vpc-vpe-create-access.md#vpc-vpe-create-pricing")
- [Private network and private routing](vpc-vpe-create-access.md#vpc-vpc-create-onconsole "vpc-vpe-create-access.md#vpc-vpc-create-onconsole")
- [(Required) VPC endpoints](vpc-vpe-create-access.md#vpc-vpe-create-view-endpoints-examples "vpc-vpe-create-access.md#vpc-vpe-create-view-endpoints-examples")
- [Attaching the required VPC endpoints](vpc-vpe-create-access.md#vpc-vpe-create-view-endpoints-attach-all "vpc-vpe-create-access.md#vpc-vpe-create-view-endpoints-attach-all")
  - [VPC endpoints required for AWS services](vpc-vpe-create-access.md#vpc-vpe-create-view-endpoints-attach-services "vpc-vpe-create-access.md#vpc-vpe-create-view-endpoints-attach-services")
  - [VPC endpoints required for Apache Airflow](vpc-vpe-create-access.md#vpc-vpe-create-view-endpoints-attach-aa "vpc-vpe-create-access.md#vpc-vpe-create-view-endpoints-attach-aa")

- [(Optional) Enable private IP addresses for your Amazon S3 VPC interface endpoint](vpc-vpe-create-access.md#vpc-vpe-create-view-endpoints-s3-exception "vpc-vpe-create-access.md#vpc-vpe-create-view-endpoints-s3-exception")
  - [Using Route 53](vpc-vpe-create-access.md#vpc-vpe-create-view-endpoints-s3-exception-route53 "vpc-vpe-create-access.md#vpc-vpe-create-view-endpoints-s3-exception-route53")
  - [VPCs with custom DNS](vpc-vpe-create-access.md#vpc-vpe-create-view-endpoints-s3-exception-customdns "vpc-vpe-create-access.md#vpc-vpe-create-view-endpoints-s3-exception-customdns")

## Pricing

- [AWS PrivateLink Pricing](https://aws.amazon.com/privatelink/pricing/ "https://aws.amazon.com/privatelink/pricing/")

## Private network and private routing

![This image displays the architecture for an Amazon MWAA environment with a private webserver.](images/mwaa-private-web-server.png)

The private network access mode limits access to the Apache Airflow UI to users _within your Amazon VPC_ who have been granted access to the
[IAM policy for your environment](access-policies.md "access-policies.md").

When you create an environment with private webserver access, you must package all of your dependencies in a Python wheel archive (`.whl`), then
reference the `.whl` in your `requirements.txt`. For instructions on packaging and installing your dependencies
using wheel, refer to [Managing dependencies using Python wheel](best-practices-dependencies.md#best-practices-dependencies-python-wheels "best-practices-dependencies.md#best-practices-dependencies-python-wheels").

The following image depicts where to find the **Private network** option on the Amazon MWAA console.

![This image depicts where to find the Private network option on the Amazon MWAA console.](images/mwaa-console-private-network.png)

- **Private routing**. An [Amazon VPC without internet access](networking-about.md "networking-about.md")
  limits network traffic within the VPC. This page assumes your Amazon VPC does not have internet access and requires VPC endpoints for each AWS
  service used by your environment, and VPC endpoints for Apache Airflow in the same AWS Region and Amazon VPC as your Amazon MWAA environment.

## (Required) VPC endpoints

The following section displays the required VPC endpoints needed for an Amazon VPC without internet access. It lists the VPC endpoints for each AWS service used by Amazon MWAA, including the VPC endpoints needed for Apache Airflow.

```
com.amazonaws.`us-east-1`.s3
com.amazonaws.`us-east-1`.monitoring
com.amazonaws.`us-east-1`.logs
com.amazonaws.`us-east-1`.sqs
com.amazonaws.`us-east-1`.kms
```

###### Note

When using Transit Gateway or any other routing that does not go directly to the
AWS API endpoints, we recommend you to add AWS PrivateLink to your Amazon MWAA private
subnets for the following services:

- Amazon S3
- Amazon SQS
- CloudWatch Logs
- CloudWatch metrics
- AWS KMS (if applicable)
  This ensures that your Amazon MWAA environment can securely and efficiently communicate
  with these services without routing traffic through the public internet, thereby
  improving security and performance.

## Attaching the required VPC endpoints

This section describes the steps to attach the required VPC endpoints for an Amazon VPC with private routing.

### VPC endpoints required for AWS services

The following section displays the steps to attach the VPC endpoints for the AWS services used by an environment to an existing Amazon VPC.

###### To attach VPC endpoints to your private subnets

1. Open the [Endpoints page](https://console.aws.amazon.com/vpc/home#Endpoints:sort=vpcEndpointType "https://console.aws.amazon.com/vpc/home#Endpoints:sort=vpcEndpointType") on the Amazon VPC console.
2. Select your AWS Region.
3. Create the endpoint for Amazon S3:
   1. Choose **Create Endpoint**.
   2. In the _Filter by attributes or search by keyword_ text field, type: `.s3`, then press _Enter_ on your keyboard.
   3. We recommend choosing the service endpoint listed for the **Gateway** type.

   For example, `com.amazonaws.us-west-2.s3 amazon Gateway` 4. Choose your environment's Amazon VPC in **VPC**. 5. Ensure that your two private subnets in different Availability Zones are selected, and that that private DNS is enabled by selecting **Enable DNS name**. 6. Choose your environment's Amazon VPC security groups. 7. Choose **Full Access** in **Policy**. 8. Choose **Create endpoint**.

4. Create the endpoint for CloudWatch Logs:
   1. Choose **Create Endpoint**.
   2. In the _Filter by attributes or search by keyword_ text field, type: `.logs`, then press _Enter_ on your keyboard.
   3. Select the service endpoint.
   4. Choose your environment's Amazon VPC in **VPC**.
   5. Ensure that your two private subnets in different Availability Zones are selected, and that **Enable DNS name** is enabled.
   6. Choose your environment's Amazon VPC security groups.
   7. Choose **Full Access** in **Policy**.
   8. Choose **Create endpoint**.

5. Create the endpoint for CloudWatch Monitoring:
   1. Choose **Create Endpoint**.
   2. In the _Filter by attributes or search by keyword_ text field, type: `.monitoring`, then press _Enter_ on your keyboard.
   3. Select the service endpoint.
   4. Choose your environment's Amazon VPC in **VPC**.
   5. Ensure that your two private subnets in different Availability Zones are selected, and that **Enable DNS name** is enabled.
   6. Choose your environment's Amazon VPC security groups.
   7. Choose **Full Access** in **Policy**.
   8. Choose **Create endpoint**.

6. Create the endpoint for Amazon SQS:
   1. Choose **Create Endpoint**.
   2. In the _Filter by attributes or search by keyword_ text field, type: `.sqs`, then press _Enter_ on your keyboard.
   3. Select the service endpoint.
   4. Choose your environment's Amazon VPC in **VPC**.
   5. Ensure that your two private subnets in different Availability Zones are selected, and that **Enable DNS name** is enabled.
   6. Choose your environment's Amazon VPC security groups.
   7. Choose **Full Access** in **Policy**.
   8. Choose **Create endpoint**.

7. Create the endpoint for AWS KMS:
   1. Choose **Create Endpoint**.
   2. In the _Filter by attributes or search by keyword_ text field, type: `.kms`, then press _Enter_ on your keyboard.
   3. Select the service endpoint.
   4. Choose your environment's Amazon VPC in **VPC**.
   5. Ensure that your two private subnets in different Availability Zones are selected, and that **Enable DNS name** is enabled.
   6. Choose your environment's Amazon VPC security groups.
   7. Choose **Full Access** in **Policy**.
   8. Choose **Create endpoint**.

### VPC endpoints required for Apache Airflow

The following section displays the steps to attach the VPC endpoints for Apache Airflow to an existing Amazon VPC.

###### To attach VPC endpoints to your private subnets

1. Open the [Endpoints page](https://console.aws.amazon.com/vpc/home#Endpoints:sort=vpcEndpointType "https://console.aws.amazon.com/vpc/home#Endpoints:sort=vpcEndpointType") on the Amazon VPC console.
2. Select your AWS Region.
3. Create the endpoint for the Apache Airflow API:
   1. Choose **Create Endpoint**.
   2. In the _Filter by attributes or search by keyword_ text field, type: `.airflow.api`, then press _Enter_ on your keyboard.
   3. Select the service endpoint.
   4. Choose your environment's Amazon VPC in **VPC**.
   5. Ensure that your two private subnets in different Availability Zones are selected, and that **Enable DNS name** is enabled.
   6. Choose your environment's Amazon VPC security groups.
   7. Choose **Full Access** in **Policy**.
   8. Choose **Create endpoint**.

4. Create the first endpoint for the Apache Airflow environment:
   1. Choose **Create Endpoint**.
   2. In the _Filter by attributes or search by keyword_ text field, type: `.airflow.env`, then press _Enter_ on your keyboard.
   3. Select the service endpoint.
   4. Choose your environment's Amazon VPC in **VPC**.
   5. Ensure that your two private subnets in different Availability Zones are selected, and that **Enable DNS name** is enabled.
   6. Choose your environment's Amazon VPC security groups.
   7. Choose **Full Access** in **Policy**.
   8. Choose **Create endpoint**.

5. Create the second endpoint for Apache Airflow operations:
   1. Choose **Create Endpoint**.
   2. In the _Filter by attributes or search by keyword_ text field, type: `.airflow.ops`, then press _Enter_ on your keyboard.
   3. Select the service endpoint.
   4. Choose your environment's Amazon VPC in **VPC**.
   5. Ensure that your two private subnets in different Availability Zones are selected, and that **Enable DNS name** is enabled.
   6. Choose your environment's Amazon VPC security groups.
   7. Choose **Full Access** in **Policy**.
   8. Choose **Create endpoint**.

## (Optional) Enable private IP addresses for your Amazon S3 VPC interface endpoint

Amazon S3 **Interface** endpoints don't support private DNS. The S3 endpoint requests still resolves to a _public_ IP address. To resolve the S3 address to a _private_ IP address, you need to add a [private hosted zone in Route 53](../../../Route53/latest/DeveloperGuide/hosted-zones-private.md "../../../Route53/latest/DeveloperGuide/hosted-zones-private.md") for the S3 regional endpoint.

### Using Route 53

This section describes the steps to enable private IP addresses for an S3 **Interface** endpoint using Route 53.

1. Create a Private Hosted Zone for your Amazon S3 VPC interface endpoint (such as, s3.eu-west-1.amazonaws.com) and associate it with your Amazon VPC.
2. Create an ALIAS A record for your Amazon S3 VPC interface endpoint (such as, s3.eu-west-1.amazonaws.com) that resolves to your VPC Interface Endpoint DNS name.
3. Create an ALIAS A wildcard record for your Amazon S3 interface endpoint (such as, \*.s3.eu-west-1.amazonaws.com) that resolves to the VPC Interface Endpoint DNS name.

### VPCs with custom DNS

If your Amazon VPC uses custom DNS routing, you need to make the changes in your DNS resolver (not Route 53, typically an EC2 instance running a DNS server) by creating a CNAME record. For example:

```
Name: s3.us-west-2.amazonaws.com
Type: CNAME
Value:  *.vpce-0f67d23e37648915c-e2q2e2j3.s3.us-west-2.vpce.amazonaws.com
```
