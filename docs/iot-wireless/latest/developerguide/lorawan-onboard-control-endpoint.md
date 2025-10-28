# Onboard AWS IoT Core for LoRaWAN control plane

API endpoint

You can use AWS IoT Core for LoRaWAN control plane API endpoints to interact with the
AWS IoT Wireless APIs. For example, you can use this endpoint to run the [SendDataToWirelessDevice](../../2020-11-22/apireference/API_SendDataToWirelessDevice.md "../../2020-11-22/apireference/API_SendDataToWirelessDevice.md") API to send data from AWS IoT to your LoRaWAN
device. For more information, see [AWS IoT Core for LoRaWAN Control Plane API Endpoints](../../../general/latest/gr/iot-core.md#iot-core.html#iot-wireless-control-plane-endpoints "../../../general/latest/gr/iot-core.md#iot-core.html#iot-wireless-control-plane-endpoints").

You can use the client hosted in your Amazon VPC to access the control plane endpoints that
are powered by AWS PrivateLink. You use these endpoints to connect to the
AWS IoT Wireless API through an interface endpoint in your Virtual Private Cloud (VPC)
instead of connecting over the public internet.

###### To onboard the control plane endpoint:

- [Create your Amazon VPC and subnet](#create-vpc "#create-vpc")
- [Launch an Amazon EC2 instance in your
  subnet](#launch-ec2-instance "#launch-ec2-instance")
- [Create Amazon VPC interface endpoint](#create-vpc-endpoint "#create-vpc-endpoint")
- [Test your connection to the interface
  endpoint](#connect-vpc-endpoint "#connect-vpc-endpoint")

## Create your Amazon VPC and subnet

Before you can connect to the interface endpoint, you must create a VPC and
subnet. You'll then launch an EC2 instance in your subnet, which you can use to
connect to the interface endpoint.

To create your VPC:

1. Navigate to the [VPCs](https://console.aws.amazon.com/vpc/home#/vpcs "https://console.aws.amazon.com/vpc/home#/vpcs") page of the Amazon VPC console and choose **Create
   VPC**.
2. On the **Create VPC** page:
   - Enter a name for **VPC Name tag - optional** (for
     example, `VPC-A`).
   - Enter an IPv4 address range for your VPC in the **IPv4 CIDR**
     (for example, `10.100.0.0/16`).
   - If you want to create dualstack VPC endpoints in your VPC, choose
     **Amazon-provided IPv6 CIDR block** for **IPv6
     CIDR block**.

3. Keep the default values for other fields and choose **Create
   VPC**.

To create your subnet:

1. Navigate to the [Subnets](https://console.aws.amazon.com/vpc/home#/subnets "https://console.aws.amazon.com/vpc/home#/subnets") page of the Amazon VPC console and choose **Create
   subnet**.
2. On the **Create subnet** page:
   - For **VPC ID**, choose the VPC that you created
     earlier (for example, `VPC-A`).
   - Enter a name for **Subnet name** (for example,
     `Private subnet`).
   - Choose the **Availability Zone** for your
     subnet.
   - Enter your subnet's IP address block in the **IPv4
     subnet CIDR block** in CIDR format (for example,
     `10.100.0.0/24`).
   - If you want to create dualstack endpoints, choose the **IPv6
     VPC CIDR block** for your VPC. Optionally, you can customize the
     **IPv6 subnet CIDR block**.

3. To create your subnet and add it to your VPC, choose **Create
   subnet**.

For more information, see [Work with VPCs and
subnets](../../../vpc/latest/userguide/working-with-vpcs.md "../../../vpc/latest/userguide/working-with-vpcs.md").

## Launch an Amazon EC2 instance in your

subnet

To launch your EC2 instance:

1. Navigate to the [Amazon EC2](https://console.aws.amazon.com/ec2/home#/ "https://console.aws.amazon.com/ec2/home#/") console and choose **Launch
   Instance**.
2. For AMI, choose **Amazon Linux 2 AMI (HVM), SSD Volume
   Type** and then choose the **t2 micro**
   instance type. To configure the instance details, choose
   **Next**.
3. In the **Configure Instance Details** page:
   - For **Network**, choose the VPC that you created
     earlier (for example, `VPC-A`).
   - For **Subnet**, choose the subnet that you
     created earlier (for example, `Private
subnet`).

   ###### Note

   If you provided an IPv6 CIDR block for your VPC and subnet,
   you can optionally choose to auto-assign an IPv6 IP address
   for your EC2 instance.
   - For **IAM role**, choose the role
     **AWSIoTWirelessFullAccess** to grant
     AWS IoT Core for LoRaWAN full access policy. For more information, see [`AWSIoTWirelessFullAccess` policy
     summary](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSIoTWirelessFullAccess$serviceLevelSummary "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSIoTWirelessFullAccess$serviceLevelSummary").
   - For **Assume Private IP**, use an IP address, for
     example, **10.100.0.42**.

4. Choose **Next: Add Storage** and then choose
   **Next: Add Tags**. You can optionally add any tags
   to associate with your EC2 instance. Choose **Next: Configure
   Security Group**.
5. In the **Configure Security Group** page, configure the
   security group to allow:
   - Open **All TCP** for Source as
     `10.200.0.0/16`.
   - Open **All ICMP - IPV4** for Source as
     `10.200.0.0/16`.

6. To review the instance details and launch your EC2 instance, choose
   **Review and Launch**.

For more information, see [Get started with Amazon EC2 Linux
instances](../../../AWSEC2/latest/userguide/EC2_GetStarted.md "../../../AWSEC2/latest/userguide/EC2_GetStarted.md").

## Create Amazon VPC interface endpoint

You can create a VPC endpoint for your VPC, which can then be accessed by the EC2
API. To create the endpoint:

1. Navigate to the [VPC](https://console.aws.amazon.com/vpc/home#/endpoints "https://console.aws.amazon.com/vpc/home#/endpoints")
   **Endpoints** console and choose **Create
   Endpoint**.
2. In the **Create Endpoint** page, specify the following
   information.
   - Choose **AWS services** for **Service
     category**.
   - For **Service Name**, search by entering the
     keyword `iotwireless`. In the list of
     `iotwireless` services displayed, choose the control
     plane API endpoint for your Region. The endpoint will be in the
     format
     `com.amazonaws.`region`.iotwireless.api`.
   - For **VPC** and **Subnets**,
     choose the VPC where you want to create the endpoint, and the
     Availability Zones (AZs) in which you want to create the endpoint
     network.

   ###### Note

   The `iotwireless` service might not support all
   Availability Zones.
   - For **Enable DNS name**, choose **Enable
     for this endpoint**.

   Choosing this option will automatically resolve the DNS and create
   a route in Amazon Route 53 Public Data Plane so that the APIs you use later to
   test the connection will go through the privatelink
   endpoints.
   - For **Security group**, choose the security
     groups you want to associate with the endpoint network
     interfaces.
   - Optionally, you can add or remove tags. Tags are name-value pairs
     that you use to associate with your endpoint.

3. To create your VPC endpoint, choose **Create
   endpoint**.

## Test your connection to the interface

endpoint

You can use an SSH to access your Amazon EC2 instance and then use the AWS CLI to connect
to the privatelink interface endpoints.

Before you connect to the interface endpoint, download the most recent AWS CLI
version by following the instructions described in [Installing, updating, and uninstalling AWS CLI version 2 on Linux](../../../cli/latest/userguide/install-cliv2-linux.md "../../../cli/latest/userguide/install-cliv2-linux.md").

The following examples show how you can test your connection to the interface
endpoint using the CLI.

```
aws iotwireless create-service-profile \
    --endpoint-url https://api.iotwireless.`region`.amazonaws.com  \
    --name='test-privatelink'
```

The following shows a sample response of running the command.

```
{
    "Arn": "arn:aws:iotwireless:`region`:`acct_number`:ServiceProfile/1a2345ba-4c5d-67b0-ab67-e0c8342f2857",
    "Id": "1a2345ba-4c5d-67b0-ab67-e0c8342f2857"
}
```

Similarly, you can run the following commands to get the service profile
information or list all service profiles.

```
aws iotwireless get-service-profile \
    --endpoint-url https://api.iotwireless.`region`.amazonaws.com
    --id="1a2345ba-4c5d-67b0-ab67-e0c8342f2857"
```

The following shows an example for the list-device-profiles command.

```
aws iotwireless list-device-profiles \
    --endpoint-url https://api.iotwireless.`region`.amazonaws.com
```
