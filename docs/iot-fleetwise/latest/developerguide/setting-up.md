

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Set up AWS IoT FleetWise
<a name="setting-up"></a>

Before you use AWS IoT FleetWise for the first time, complete the steps in the following sections.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Set up your AWS account](#setting-up-create-iam-user)
+ [Get started in the console](#console-get-started)
+ [Configure your AWS IoT FleetWise settings](configure-settings.md)
+ [Making requests to AWS IoT FleetWise using IPv6](fleetwise-ipv6-access.md)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Set up your AWS account
<a name="setting-up-create-iam-user"></a>

**Note**  
You can use a service-linked role with AWS IoT FleetWise. Service-linked roles are predefined by AWS IoT FleetWise and include the permissions that AWS IoT FleetWise needs to send metrics to Amazon CloudWatch. For more information, see [Using service-linked roles for AWS IoT FleetWise](using-service-linked-roles.md).

## Get started in the console
<a name="console-get-started"></a>

If you aren't already signed in to your AWS account, sign in, then open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise/). To get started with AWS IoT FleetWise, create a vehicle model. A vehicle model standardizes the format of your vehicles.

1. <a name="fleetwise-open-console"></a>Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise).

1. In **Get started with AWS IoT FleetWise**, choose **Get started**.

For more information about creating a vehicle model, see [Create an AWS IoT FleetWise vehicle model](create-vehicle-model.md).