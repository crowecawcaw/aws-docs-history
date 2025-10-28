# Create VPC interface endpoint and private

hosted zone

AWS IoT Core for LoRaWAN has two data plane endpoints, Configuration and Update Server (CUPS)
endpoint and LoRaWAN Network Server (LNS) endpoint. The setup process to establish a
privatelink connection to both endpoints is the same, so we can use the LNS endpoint
for illustration purposes.

For your data plane endpoints, the LoRa gateways first connect to your
AWS account in your Amazon VPC, which then connects to the VPC endpoint in the
AWS IoT Core for LoRaWAN VPC.

When connecting to the endpoints, the DNS names can be resolved within one VPC but
can't be resolved across multiple VPCs. To disable private DNS when creating the
endpoint, disable the **Enable DNS name** setting. You can use
private hosted zone to provide information about how you want Route 53 to respond to
DNS queries for your VPCs. To share your VPC with an on-premises environment, you
can use a
Route 53 Resolver
to facilitate hybrid DNS.

###### To complete this procedure, perform the following steps.

- [Create an Amazon VPC and subnet](#lns-create-vpc "#lns-create-vpc")
- [Create an Amazon VPC interface
  endpoint](#lns-create-vpc-endpoint "#lns-create-vpc-endpoint")
- [Configure private hosted zone](#create-phz-lns "#create-phz-lns")
- [Configure Route 53 inbound
  resolver](#configure-route53-resolver "#configure-route53-resolver")
- [Next steps](#lns-cups-next-steps "#lns-cups-next-steps")

## Create an Amazon VPC and subnet

You can reuse your Amazon VPC and subnet that you created when onboarding your
control plane endpoint. For information, see [Create your Amazon VPC and subnet](lorawan-onboard-control-endpoint.md#create-vpc "lorawan-onboard-control-endpoint.md#create-vpc").

## Create an Amazon VPC interface

endpoint

You can create a VPC endpoint for your VPC, which is similar to how you would
create one for your control plane endpoint.

1. Navigate to the [VPC](https://console.aws.amazon.com/vpc/home#/endpoints "https://console.aws.amazon.com/vpc/home#/endpoints")
   **Endpoints** console and choose **Create
   Endpoint**.
2. In the **Create Endpoint** page, specify the
   following information.
   - Choose **AWS services** for
     **Service category**.
   - For **Service Name**, search by entering the
     keyword `lns`. In the list of
     `lns` services displayed, choose the LNS data
     plane API endpoint for your Region. The endpoint will be of the
     format
     `com.amazonaws.`region`.lorawan.lns`.

   ###### Note

   If you're following this procedure for your CUPS endpoint,
   search for `cups`. The endpoint will be of the
   format
   `com.amazonaws.`region`.lorawan.cups`.
   - For **VPC** and **Subnets**,
     choose the VPC where you want to create the endpoint, and the
     Availability Zones (AZs) in which you want to create the
     endpoint network.

   ###### Note

   The `iotwireless` service might not support all
   Availability Zones.
   - For **Enable DNS name**, make sure that
     **Enable for this endpoint** is not
     selected.

   By not selecting this option, you can disable private DNS for
   the VPC endpoint and use private hosted zone instead.
   - For **Security group**, choose the security
     groups you want to associate with the endpoint network
     interfaces.
   - Optionally, you can add or remove tags. Tags are name-value
     pairs that you use to associate with your endpoint.

3. To create your VPC endpoint, choose **Create
   endpoint**.

## Configure private hosted zone

After you create the privatelink endpoint, in the **Details**
tab of your endpoint, you'll see a list of DNS names. You can use one of these
DNS names to configure your private hosted zone. The DNS name will be of the
format
`vpce-`xxxx`.lns.lorawan.`region`.vpce.amazonaws.com`.

###### Topics

- [Create the private hosted zone](#create-phz-how "#create-phz-how")
- [Create a record](#create-phz-record "#create-phz-record")

### Create the private hosted zone

To create the private hosted zone:

1. Navigate to the [Route 53](https://console.aws.amazon.com/route53/v2/hostedzones#/ "https://console.aws.amazon.com/route53/v2/hostedzones#/")
   **Hosted zones** console and choose **Create
   hosted zone**.
2. In the **Create hosted zone** page, specify the
   following information.
   - For **Domain name**, enter the full service
     name for your LNS endpoint,
     `lns.lorawan.region.amazonaws.com`.

   ###### Note

   If you're following this procedure for your CUPS endpoint,
   enter
   `cups.lorawan.region.amazonaws.com`.
   - For **Type**, choose **Private hosted
     zone**.
   - Optionally, you can add or remove tags to associate with your
     hosted zone.

3. To create your private hosted zone, choose **Create hosted
   zone**.

For more information, see [Creating a private hosted zone](../../../Route53/latest/DeveloperGuide/hosted-zone-private-creating.md "../../../Route53/latest/DeveloperGuide/hosted-zone-private-creating.md").

After you have created a private hosted zone, you can create a record that
tells the DNS how you want traffic to be routed to that domain.

### Create a record

After you have created a private hosted zone, you can create a record that
tells the DNS how you want traffic to be routed to that domain. How you create
the record depends on whether you want to route the traffic to an IPv4 or an
IPv6 address. When routing traffic to an IPv4 address, choose the record type
A. When routing traffic to an IPv6 address, choose the record type AAAA.

The following steps show how you how to create a record for both A and AAAA
record types.

###### Topics

- [Create record of type A (for IPv4 traffic)](#create-phz-record-typeA "#create-phz-record-typeA")
- [Create record of type AAAA (for IPv6 traffic)](#create-phz-record-typeAAAA "#create-phz-record-typeAAAA")

#### Create record of type A (for IPv4 traffic)

To create a record of type A, perform the following steps.

1. In the list of hosted zones displayed, choose the private hosted zone
   that you created earlier and choose **Create
   record**.
2. Use the wizard method to create the record. If the console presents
   you the **Quick create** method, choose
   **Switch to wizard**.
3. Choose **Simple Routing** for **Routing
   policy** and then choose **Next**.
4. In the **Configure records** page, choose
   **Define simple record**.
5. In the **Define simple record** page:
   - For **Record name**, enter the alias of your
     AWS account number. You get this value when onboarding your
     gateway or by using the [`GetServiceEndpoint`](../../../iotwireless/latest/apireference/API_GetServiceEndpoint.md "../../../iotwireless/latest/apireference/API_GetServiceEndpoint.md")
     REST API.
   - For **Record type**, keep the value as
     `A - Routes traffic to an IPv4 address and some AWS
resources`.
   - For **Value/Route traffic to**, choose
     **Alias to VPC endpoint**. Then choose your
     **Region** and then choose the endpoint
     that you created previously, as described in [Create an Amazon VPC interface
     endpoint](#lns-create-vpc-endpoint "#lns-create-vpc-endpoint") from the list of
     endpoints displayed.

6. Choose **Define simple record** to create your
   record.

#### Create record of type AAAA (for IPv6 traffic)

When you use the record type AAAA, you'll not be able to use the
**Alias to VPC endpoint** option for the
**Value/Route traffic to** field. Instead, you can perform the following
steps when creating a record of type AAAA.

1. Create an EC2 instance in a subnet that has access to the VPC
   endpoint.

###### Note

You must make sure that the VPC and subnet that you created
supports routing of IPv6 traffic. For information about the steps
to be performed, see [Create your Amazon VPC and subnet](lorawan-onboard-control-endpoint.md#create-vpc "lorawan-onboard-control-endpoint.md#create-vpc"). 2. Create an EC2 instance in a subnet that has access to the VPC endpoint.
For information about the steps to be performed, see [Launch an Amazon EC2 instance in your
subnet](lorawan-onboard-control-endpoint.md#launch-ec2-instance "lorawan-onboard-control-endpoint.md#launch-ec2-instance"). 3. Create an Amazon VPC interface endpoint for the VPC that you created.
For information about the steps to be performed, see [Create Amazon VPC interface endpoint](lorawan-onboard-control-endpoint.md#create-vpc-endpoint "lorawan-onboard-control-endpoint.md#create-vpc-endpoint"). 4. SSH into the EC2 instance and run the following command. In this command,
replace `<vpce_domain_name>` with the domain
name for your VPC interface endpoint. You can obtain this information from the
**DNS names** section in the details page of the endpoint that
you created.

```
nslookup `<vpce_domain_name>`
```

Running this command will generate information about the domain, such as
the IP address, DNS record, and nameservers. 5. In the response obtained from the `nslookup` command, copy
the IP address returned from the **Non-authoritative answer**
section. Store this information securely as you'll need to use it when creating
the record. 6. Go to the [Route 53](https://console.aws.amazon.com/route53/v2/hostedzones#/ "https://console.aws.amazon.com/route53/v2/hostedzones#/")**Hosted zones** console, and in the
list of hosted zones displayed, choose the private hosted zone
that you created earlier and choose **Create
record**. 7. Use the wizard method to create the record. If the console presents
you the **Quick create** method, choose
**Switch to wizard**. 8. Choose **Simple Routing** for **Routing
policy** and then choose
**Next**. 9. In the **Configure records** page, choose
**Define simple record**. 10. In the **Define simple record** page:

    * For **Record name**, enter the alias of your
     AWS account number. You get this value when onboarding your
     gateway or by using the [`GetServiceEndpoint`](../../../iotwireless/latest/apireference/API_GetServiceEndpoint.md "../../../iotwireless/latest/apireference/API_GetServiceEndpoint.md")
     REST API.
    * For **Record type**, keep the value as
     `AAAA - Routes traffic to an IPv6 address and some AWS
     resources`.
    * For **Value/Route traffic to**, choose
     **IP address or another value, depending on the record
     type** and then enter the IP address that you obtained
     using the `nslookup` command.

11. Choose **Define simple record** to create your
    record.

## Configure Route 53 inbound

resolver

To share a VPC endpoint to an on-premises environment, a Route 53 Resolver can be used to
facilitate hybrid DNS. The inbound resolver will enable you to route traffic
from the on-premises network to the data plane endpoints without going over the
public internet. To return the private IP address values for your service,
create the Route 53 Resolver in the same VPC as the VPC endpoint.

When you create the inbound resolver, you only have to specify your VPC and
the subnets that you created previously in your Availability Zones (AZs). The
Route 53 Resolver uses this information to automatically assigns an IP address to route
traffic to each of the subnets.

To create the inbound resolver:

1. Navigate to the [Route 53](https://console.aws.amazon.com/route53/v2/inbound-endpoints#/ "https://console.aws.amazon.com/route53/v2/inbound-endpoints#/")
   **Inbound endpoints** console and choose
   **Create inbound endpoint**.

###### Note

Make sure that you're using the same AWS Region that you used
when creating the endpoint and private hosted zone. 2. In the **Create inbound endpoint** page, specify the
following information.

    * Enter a name for **Endpoint name** (for
     example, `VPC_A_Test`).
    * For **VPC in the region**, choose the same
     VPC that you used when creating the VPC endpoint.
    * Configure the **Security group for this
     endpoint** to allow incoming traffic from the on
     premises network.
    * For IP address, choose **Use an IP address that is
     selected automatically.**

3. Choose **Submit** to create your inbound
   resolver.

For this eample, let's assume that the IP addresses `10.100.0.145`
and `10.100.192.10` were assigned for the inbound Route 53 Resolver for routing
traffic.

## Next steps

You've created the private hosted zone and an inbound resolver to route
traffic for your DNS entries. You can now use either a Site-to-Site VPN or a Client VPN
endpoint. For more information, see [Use VPN to connect LoRa gateways to
your AWS account](lorawan-vpc-vpn-connection.md "lorawan-vpc-vpn-connection.md").
