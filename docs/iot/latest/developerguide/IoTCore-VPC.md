# Using AWS IoT Core with interface VPC endpoints

With AWS IoT Core, you can create [IoT
control plane endpoints](connect-to-iot.md#iot-service-endpoint-intro "connect-to-iot.md#iot-service-endpoint-intro") and [IoT data endpoints](iot-connect-devices.md "iot-connect-devices.md")
within your virtual private cloud (VPC) by using [interface VPC
endpoints](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint"). Interface VPC endpoints are powered by AWS PrivateLink, an AWS
technology that you can use to access services running on AWS by using private IP
addresses. For more information, see [Amazon Virtual Private
Cloud](../../../AmazonVPC/latest/UserGuide/VPC_Introduction.md "../../../AmazonVPC/latest/UserGuide/VPC_Introduction.md").

To connect devices in the field on remote networks, such as a corporate network to your
Amazon VPC, refer to the options listed in the [Network-to-Amazon VPC connectivity matrix](../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md "../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md").

###### Contents

- [Creating VPC endpoints for AWS IoT Core control
  plane](#Create-VPC-endpoints-CP "#Create-VPC-endpoints-CP")
- [Creating VPC endpoints for AWS IoT Core data
  plane](#Create-VPC-endpoints "#Create-VPC-endpoints")
- [Creating VPC endpoints for
  AWS IoT Core credential provider](#Create-VPC-endpoints-credential-provider "#Create-VPC-endpoints-credential-provider")
- [Creating an Amazon VPC interface
  endpoint](#Create-VPC-endpoints-core-create-vpc "#Create-VPC-endpoints-core-create-vpc")
- [Configure a private hosted
  zone](#connect-iot-core-create-phz-lns "#connect-iot-core-create-phz-lns")
- [Controlling Access to AWS IoT Core over VPC
  endpoints](#Control-VPC-access "#Control-VPC-access")
- [Limitations](#VPC-limitations "#VPC-limitations")
- [Scaling VPC endpoints with AWS IoT Core](#Scaling-VPC-endpoints "#Scaling-VPC-endpoints")
- [Using custom domains with VPC endpoints](#VPC-custom-domains "#VPC-custom-domains")
- [Availability of VPC endpoints for AWS IoT Core](#VPC-availability "#VPC-availability")
- [Using AWS IoT Device Management secure tunneling with interface VPC
  endpoints](IoTCore-ST-VPC.md "IoTCore-ST-VPC.md")

## Creating VPC endpoints for AWS IoT Core control

plane

You can create a VPC endpoint for AWS IoT Core control plane API to connect your devices to
AWS IoT services and other AWS services. To get started with VPC endpoints, [create
an interface VPC endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint") and select AWS IoT Core as the AWS service. If you
are using the CLI, first call [describe-vpc-endpoint-services](../../../cli/latest/reference/ec2/describe-vpc-endpoint-services.md "../../../cli/latest/reference/ec2/describe-vpc-endpoint-services.md") to ensure that you are choosing an
Availability Zone where AWS IoT Core is present in your particular AWS Region. For
example, in us-east-1, this command would look like:

```
aws ec2 describe-vpc-endpoint-services --service-name com.amazonaws.us-east-1.iot.api
```

See the detailed instructions below to [Create an Amazon VPC interface
endpoint](#Create-VPC-endpoints-core-create-vpc "#Create-VPC-endpoints-core-create-vpc") for AWS IoT Core control plane.

## Creating VPC endpoints for AWS IoT Core data

plane

You can create a VPC endpoint for AWS IoT Core data plane API to connect your devices to
AWS IoT services and other AWS services. To get started with VPC endpoints, [create
an interface VPC endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint") and select AWS IoT Core as the AWS service. If you
are using the CLI, first call [describe-vpc-endpoint-services](../../../cli/latest/reference/ec2/describe-vpc-endpoint-services.md "../../../cli/latest/reference/ec2/describe-vpc-endpoint-services.md") to ensure that you are choosing an
Availability Zone where AWS IoT Core is present in your particular AWS Region. For
example, in us-east-1, this command would look like:

```
aws ec2 describe-vpc-endpoint-services --service-name com.amazonaws.us-east-1.iot.data
```

###### Note

The VPC feature for automatically creating a DNS record is disabled. To connect to
these endpoints, you must manually create a Private DNS record. For more information
about Private VPC DNS records, see [Private DNS
for interface endpoints](../../../vpc/latest/privatelink/vpce-interface.md#vpce-private-dns "../../../vpc/latest/privatelink/vpce-interface.md#vpce-private-dns"). For more information about AWS IoT Core VPC
limitations, see [Limitations](#VPC-limitations "#VPC-limitations")
.

To connect MQTT clients to the VPC endpoint interfaces:

- You must manually create DNS records in a private hosted zone that is attached
  to your VPC. To get started, see [Creating a private hosted zone](../../../Route53/latest/DeveloperGuide/hosted-zone-private-creating.md "../../../Route53/latest/DeveloperGuide/hosted-zone-private-creating.md").

- Within your private hosted zone, create an alias record for each elastic
  network interface IP for the VPC endpoint. If you have multiple network
  interface IPs for multiple VPC endpoints, create weighted DNS records with equal
  weights across all the weighted records. These IP addresses are available from
  the [DescribeNetworkInterfaces](../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md "../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md") API call when filtered by the VPC
  endpoint ID in the description field.

See the detailed instructions below to [Create an Amazon VPC interface
endpoint](#Create-VPC-endpoints-core-create-vpc "#Create-VPC-endpoints-core-create-vpc") and [Configure
private hosted zone](#connect-iot-core-create-phz-lns "#connect-iot-core-create-phz-lns") for AWS IoT Core data plane.

## Creating VPC endpoints for

AWS IoT Core credential provider

You can create a VPC endpoint for AWS IoT Core [credential
provider](authorizing-direct-aws.md "authorizing-direct-aws.md") to connect devices using client certificate-based authentication
and get temporary AWS credentials in [AWS Signature Version 4
format](../../../IAM/latest/UserGuide/reference_aws-signing.md "../../../IAM/latest/UserGuide/reference_aws-signing.md"). To get started with VPC endpoints for AWS IoT Core credential provider,
run the [create-vpc-endpoint](../../../cli/latest/reference/ec2/create-vpc-endpoint.md "../../../cli/latest/reference/ec2/create-vpc-endpoint.md")
CLI command to [create
an interface VPC endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint") and select AWS IoT Core credential provider as the
AWS service. To ensure that you are choosing an Availability Zone where AWS IoT Core is
present in your particular AWS Region, your first run the [describe-vpc-endpoint-services](../../../cli/latest/reference/ec2/describe-vpc-endpoint-services.md "../../../cli/latest/reference/ec2/describe-vpc-endpoint-services.md") command. For example, in us-east-1, this
command would look like:

```
aws ec2 describe-vpc-endpoint-services --service-name com.amazonaws.us-east-1.iot.credentials
```

###### Note

The VPC feature for automatically creating a DNS record is disabled. To connect to
these endpoints, you must manually create a Private DNS record. For more information
about Private VPC DNS records, see [Private DNS
for interface endpoints](../../../vpc/latest/privatelink/vpce-interface.md#vpce-private-dns "../../../vpc/latest/privatelink/vpce-interface.md#vpce-private-dns"). For more information about AWS IoT Core VPC
limitations, see [Limitations](#VPC-limitations "#VPC-limitations")
.

To connect HTTP clients to the VPC endpoint interfaces:

- You must manually create DNS records in a private hosted zone that is attached
  to your VPC. To get started, see [Creating A private hosted zone](../../../Route53/latest/DeveloperGuide/hosted-zone-private-creating.md "../../../Route53/latest/DeveloperGuide/hosted-zone-private-creating.md").

- Within your private hosted zone, create an alias record for each elastic
  network interface IP for the VPC endpoint. If you have multiple network
  interface IPs for multiple VPC endpoints, create weighted DNS records with equal
  weights across all the weighted records. These IP addresses are available from
  the [DescribeNetworkInterfaces](../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md "../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md") API call when filtered by the VPC
  endpoint ID in the description field.

See the detailed instructions below to [Create an Amazon VPC interface
endpoint](#Create-VPC-endpoints-core-create-vpc "#Create-VPC-endpoints-core-create-vpc") and [Configure
private hosted zone](#connect-iot-core-create-phz-lns "#connect-iot-core-create-phz-lns") for AWS IoT Core credential provider.

## Creating an Amazon VPC interface

endpoint

You can create an interface VPC endpoint to connect to AWS services powered by
AWS PrivateLink. Use the following procedure to create an interface VPC endpoint that
connects to AWS IoT Core data plane or AWS IoT Core credential provider. For more information,
see [Access an AWS service
using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md").

###### Note

The processes to create an Amazon VPC interface endpoint for AWS IoT Core data plane and
AWS IoT Core credential provider are similar, but you must make endpoint specific
changes to make the connection work.

**To create an interface VPC endpoint using [VPC](https://console.aws.amazon.com/vpc/home#/endpoints "https://console.aws.amazon.com/vpc/home#/endpoints")
**Endpoints** console**

1. Navigate to the [VPC](https://console.aws.amazon.com/vpc/home#/endpoints "https://console.aws.amazon.com/vpc/home#/endpoints")
   **Endpoints** console, under **Virtual private
   cloud** on the left menu, choose **Endpoints**
   then **Create Endpoint**.
2. In the **Create endpoint** page, specify the following
   information.
   - Choose **AWS services** for **Service
     category**.
   - For **Service Name**, search by entering the keyword
     `iot`. In the list of `iot` services
     displayed, choose the endpoint.

   If you create a VPC endpoint for AWS IoT Core control plane, choose the
   AWS IoT Core control plane API endpoint for your AWS Region. The endpoint
   will be of the format
   `com.amazonaws.`region`.iot.api`.

   If you create a VPC endpoint for AWS IoT Core data plane, choose the
   AWS IoT Core data plane API endpoint for your Region. The endpoint will be
   of the format
   `com.amazonaws.`region`.iot.data`.

   If you create a VPC endpoint for AWS IoT Core credential provider, choose
   the AWS IoT Core credential provider endpoint for your Region. The endpoint
   will be of the format
   `com.amazonaws.`region`.iot.credentials`.

   If you create a VPC endpoint for Federal Information Processing
   Standard (FIPS) regions, choose the FIPS API endpoint for your
   AWS Region. The endpoint will be of the format
   `com.amazonaws.`region`.iot-fips.api`. This is only for control plane.

   ###### Note

   The service name for AWS IoT Core data plane in China Region will be
   of the format
   `cn.com.amazonaws.`region`.iot.data`.
   The service name for AWS IoT Core control plane in China Region will be
   of the format
   `com.amazonaws.`region`.iot.api`.
   - For **VPC** and **Subnets**, choose
     the VPC where you want to create the endpoint, and the Availability
     Zones (AZs) in which you want to create the endpoint network.
   - For **Enable DNS name**, make sure that
     **Enable for this endpoint** is not selected for
     AWS IoT Core data plane and AWS IoT Core credential provider. Neither
     AWS IoT Core data plane nor AWS IoT Core credential provider supports private
     DNS names yet.

   For AWS IoT Core control plane, **Enable DNS name** is
   selected by default. This ensures that any requests to the AWS IoT Core
   control plane public endpoints will route through the VPC endpoints
   instead. When this is enabled, you do not need to configure a privated
   hosted zone.
   - For **Security group**, choose the security groups
     you want to associate with the endpoint network interfaces.
   - Optionally, you can add or remove tags. Tags are name-value pairs that
     you use to associate with your endpoint.

3. To create your VPC endpoint, choose **Create
   endpoint**.

After you create the AWS PrivateLink endpoint, in the **Details** tab
of your endpoint, you'll see a list of DNS names. You can use one of these DNS names you
created in this section to [configure
your private hosted zone](#connect-iot-core-create-phz-lns "#connect-iot-core-create-phz-lns"). If you are using AWS IoT Core control plane, you do
not need to configure a private hosted zone.

## Configure a private hosted

zone

###### Note

If you are using AWS IoT Core control plane and have **Enable DNS
name** selected, you do not need to configure a private hosted zone. If
you disable it, you must follow this procedure to configure a private hosted
zone.

You can use one of these DNS names you created in the previous section to configure
your private hosted zone.

**For AWS IoT Core data plane**

The DNS name must be your domain configuration name or your `IoT:Data-ATS`
endpoint. An example DNS name can be:
``xxx`-ats.data.iot.`region`.amazonaws.com`.

**For AWS IoT Core credential provider**

The DNS name must be your `iot:CredentialProvider` endpoint. An example DNS
name can be:
``xxxx`.credentials.iot.`region`.amazonaws.com`.

**For AWS IoT Core control plane**

The DNS name must be your AWS IoT Core control plane endpoint. An example DNS name for
AWS IoT Core control plane is
``xxxx`.api.iot.`region`.amazonaws.com`.

###### Note

The processes to configure private hosted zone for AWS IoT Core data plane and
AWS IoT Core credential provider are similar, but you must make endpoint specific
changes to make the connection work.

### Create a

private hosted zone

**To create a private hosted zone using Route 53
console**

1. Navigate to the [Route 53](https://console.aws.amazon.com/route53/v2/hostedzones#/ "https://console.aws.amazon.com/route53/v2/hostedzones#/")
   **Hosted zones** console and choose **Create
   hosted zone**.
2. In the **Create hosted zone** page, specify the following
   information.
   - For **Domain name**, enter the endpoint address
     for your `iot:Data-ATS` or
     `iot:CredentialProvider` endpoint. The following
     AWS CLI command shows how to get the endpoint through a public
     network: `aws iot describe-endpoint --endpoint-type
iot:Data-ATS`, or `aws iot describe-endpoint
--endpoint-type iot:CredentialProvider`.

   ###### Note

   If you're using custom domains, see [Using custom domains with VPC endpoints](IoTCore-VPC.md#VPC-custom-domains "IoTCore-VPC.md#VPC-custom-domains"). Custom
   domains are not supported for AWS IoT Core credential
   provider.
   - For **Type**, choose **Private hosted
     zone**.
   - Optionally, you can add or remove tags to associate with your
     hosted zone.

3. To create your private hosted zone, choose **Create hosted
   zone**.

For more information, see [Creating a
private hosted zone](../../../Route53/latest/DeveloperGuide/hosted-zone-private-creating.md "../../../Route53/latest/DeveloperGuide/hosted-zone-private-creating.md").

### Create a

record

After you have created a private hosted zone, you can create a record that tells
the DNS how you want traffic to be routed to that domain.

**To create a record**

1. In the list of hosted zones displayed, choose the private hosted
   zone that you created earlier and choose **Create
   record**.
2. Use the wizard method to create the record. If the console
   presents you the **Quick create** method, choose
   **Switch to wizard**.
3. Choose **Simple Routing** for **Routing policy**
   and then choose **Next**.
4. In the **Configure records** page, choose **Define
   simple record**.
5. In the **Define simple record** page:
   - For **Record name**, enter `iot:Data-ATS`
     endpoint or `iot:CredentialProvider` endpoint. This must
     be the same as the private hosted zone name.
   - For **Record type**, if you want only IPv4
     support, keep the value as `A - Routes traffic to an IPv4
address and some AWS resources`. If you want only IPv6
     support, keep the value as `AAAA - Routes traffic to an IPv6
address and some AWS resources`. If you want dual-stack
     support (both IPv4 and IPv6), create two records (`A` and
     `AAAA` in the hosted zone with the same
     **Record name** and **Value/Route
     traffic to**.
   - For **Value/Route traffic to**, choose
     **Alias to VPC endpoint**. Then choose your
     **Region** and then choose the endpoint that
     you created previously, as described in [Creating an Amazon VPC interface
     endpoint](#Create-VPC-endpoints-core-create-vpc "#Create-VPC-endpoints-core-create-vpc")
     from the list
     of endpoints displayed.

6. Choose **Define simple record** to create your
   record.

## Controlling Access to AWS IoT Core over VPC

endpoints

You can restrict device access to AWS IoT Core to be allowed only through VPC endpoint by
using VPC [condition context
keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md"). AWS IoT Core supports the following VPC related context keys:

- [SourceVpc](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcevpc "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcevpc")
- [SourceVpce](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcevpce "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcevpce")
- [VPCSourceIp](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-vpcsourceip "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-vpcsourceip")

###### Note

AWS IoT Core doesn't support [Endpoints policies for VPC endpoints](../../../vpc/latest/privatelink/vpc-endpoints-access.md#vpc-endpoint-policies "../../../vpc/latest/privatelink/vpc-endpoints-access.md#vpc-endpoint-policies").

For example, the following policy grants permission to connect to AWS IoT Core using a
client ID that matches the thing name, and to publish to any topic prefixed by the thing
name, conditional on the device connecting to a VPC endpoint with a particular VPC
Endpoint ID. This policy would deny connection attempts to your public IoT data
endpoint.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iot:Connect"
 ],
 "Resource": [
 "arn:aws:iot:us-east-1:123456789012:client/${iot:Connection.Thing.ThingName}"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceVpce": "vpce-1a2b3c4d"
 }
 }

 },
 {
 "Effect": "Allow",
 "Action": [
 "iot:Publish"
 ],
 "Resource": [
 "arn:aws:iot:us-east-1:123456789012:topic/${iot:Connection.Thing.ThingName}/*"
 ]
 }
 ]
}`

```

## Limitations

VPC endpoints are currently supported for [AWS IoT Core control plane endpoints](connect-to-iot.md#iot-service-endpoint-intro "connect-to-iot.md#iot-service-endpoint-intro"), [AWS IoT Core data endpoints](iot-connect-devices.md#iot-connect-device-endpoints "iot-connect-devices.md#iot-connect-device-endpoints"), and [AWS IoT Core credential
provider](authorizing-direct-aws.md "authorizing-direct-aws.md") endpoints. VPC endpoints are only supported for [Federal
Information Processing Standard (FIPS) endpoints](iot-connect-fips.md "iot-connect-fips.md") when using the AWS IoT Core
control plane.

### Limitations of IoT control plane VPC

endpoints

This section covers the limitations of IoT control plane VPC endpoints.

- VPC endpoints will serve ATS certificates only.
- Custom domains are not supported for control plane endpoints.
- For information regarding FIPS security policies, see [FIPS security policies](../../../elasticloadbalancing/latest/application/describe-ssl-policies.md#fips-security-policies "../../../elasticloadbalancing/latest/application/describe-ssl-policies.md#fips-security-policies").

### Limitations of IoT data VPC

endpoints

This section covers the limitations of IoT data VPC endpoints.

- MQTT keep alive periods are limited to 230 seconds. Keep alive periods longer
  than that will be automatically reduced to 230 seconds.
- Each VPC endpoint supports 100,000 total concurrent connected devices. If you
  require more connections see [Scaling VPC endpoints with AWS IoT Core](#Scaling-VPC-endpoints "#Scaling-VPC-endpoints")
  .
- VPC endpoints will serve [ATS
  certificates](server-authentication.md "server-authentication.md") only, except for custom domains.
- [VPC endpoint
  policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") are not supported.
- For VPC endpoints that are created for the AWS IoT Core data plane, AWS IoT Core
  doesn't support using zonal or regional public DNS records.

### Limitations of credential

provider endpoints

This section covers the limitations of credential provider VPC endpoints.

- VPC endpoints will serve [ATS
  certificates](server-authentication.md "server-authentication.md") only.
- [VPC endpoint
  policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") are not supported.
- Custom domains are not supported for credential provider endpoints.
- For VPC endpoints that are created for the AWS IoT Core credential provider,
  AWS IoT Core doesn't support using zonal or regional public DNS records.

## Scaling VPC endpoints with AWS IoT Core

AWS IoT Core Interface VPC endpoints are limited to 100,000 connected devices over a
single interface endpoint. If your use case calls for more concurrent connections to the
broker, then we recommend using multiple VPC endpoints and manually routing your devices
across your interface endpoints. When creating private DNS records to route traffic to
your VPC endpoints, make sure to create as many weighted records as you have VPC
endpoints to distribute traffic across your multiple endpoints.

## Using custom domains with VPC endpoints

If you want to use custom domains with VPC endpoints, you must create your custom
domain name records in a private hosted zone and create routing records in Route53. For
more information, see [Creating A
private hosted zone](../../../Route53/latest/DeveloperGuide/hosted-zone-private-creating.md "../../../Route53/latest/DeveloperGuide/hosted-zone-private-creating.md").

###### Note

Custom domains are only supported for AWS IoT Core data endpoints.

## Availability of VPC endpoints for AWS IoT Core

AWS IoT Core Interface VPC endpoints are available in all [AWS IoT Core
supported regions](https://aws.amazon.com//about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com//about-aws/global-infrastructure/regional-product-services/"). AWS IoT Core Interface VPC endpoints for AWS IoT Core
credential provider are not supported in China Region and AWS GovCloud (US) Regions.
