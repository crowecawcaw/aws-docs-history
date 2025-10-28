# Routing traffic to an Amazon EC2 instance

Amazon EC2 provides scalable computing capacity in the AWS Cloud. You can launch an EC2 virtual
computing environment (an instance) using a preconfigured template (an Amazon Machine
Image or AMI). When you launch an EC2 instance, EC2 automatically installs the operating
system (Linux or Microsoft Windows) and additional software included in the AMI, such as
web server or database software.

You can route traffic for your domain, such as example.com, to your server by using
Amazon Route 53, if you're hosting a website or running a web application on an EC2 instance.

## Prerequisites

To get started, you need the following:

- An Amazon EC2 instance. For information about launching an EC2 instance, see the following documentation:
  - **Linux** – See
    [Getting started with Amazon EC2 Linux instances](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md") in the
    _Amazon EC2 User Guide_
  - **Microsoft Windows** – See
    [Getting started with Amazon EC2 Windows instances](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md") in the
    _Amazon EC2 User Guide_

###### Important

We recommend that you also create an [Elastic IP address](../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md "../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md") and associate it with your EC2
instance. An Elastic IP address ensures that the IP address of your Amazon EC2 instance will never change. For information related
to pricing, see [Pricing for Elastic IP
addresses](https://aws.amazon.com/ec2/pricing/on-demand/#Elastic_IP_Addresses "https://aws.amazon.com/ec2/pricing/on-demand/#Elastic_IP_Addresses").

- A registered domain name. You can use Amazon Route 53 as your domain registrar or you can use a
  different registrar.
- Route 53 as the DNS service for the domain. If you register your domain name by using Route 53, we automatically
  configure Route 53 as the DNS service for the domain.

For information about using Route 53 as the DNS service provider for your domain, see
[Making Amazon Route 53 the DNS service for an existing domain](MigratingDNS.md "MigratingDNS.md").

## Configuring Amazon Route 53 to route traffic to an Amazon EC2 instance

To configure Amazon Route 53 to route traffic to an EC2 instance, perform the following procedure.

###### To route traffic to an Amazon EC2 instance

1. Get the IP address for the Amazon EC2 instance:
   1. Sign in to the AWS Management Console and open the Amazon EC2 console at
      [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
   2. In the Regions list in the upper right corner of the console, choose the Region that you
      launched the instance in.
   3. In the navigation pane, choose **Instances**.
   4. In the table, choose the instance that you want to route traffic to.
   5. In the bottom pane, on the **Description** tab, get the value of
      **Elastic IPs**.

   If you didn't associate an Elastic IP with the instance, get the value of **IPv4 Public IP**.

2. Open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
3. In the navigation pane, choose **Hosted zones**.
4. Choose the name of the hosted zone that matches the name of the domain that you want to route traffic for.
5. Choose **Create record**.
6. Specify the following values:

**Routing policy**

Choose the applicable routing policy. For more information, see [Choosing a routing policy](routing-policy.md "routing-policy.md").

**Record name**

Enter the domain name that you want to use to route traffic to your EC2 instance. The default value is the name of the
hosted zone.

For example, if the name of the hosted zone is example.com and you want to use acme.example.com to route traffic to your
EC2 instance, enter **acme**.

**Value/Route traffic to**

Choose **IP address or another value depending on the record type**. Enter the IP address that you got in
step 1.

**Record type**

Choose **A – IPv4 address**.

**TTL (seconds)**

Accept the default value of **300**. 7. Choose **Create records**.

Changes generally propagate to all Route 53 servers within 60 seconds. When propagation is
done, you'll be able to route traffic to your EC2 instance by using the name
of the record that you created in this procedure.

###### Important

If you release the elastic IP, make sure you also delete the DNS record pointing to it. If you
don't, you will have a dangling DNS record that can be taken over by an
unauthorized user.
