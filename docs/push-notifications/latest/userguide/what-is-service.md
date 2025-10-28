# What is AWS End User Messaging Push?

###### Note

The Push notification features of Amazon Pinpoint are now called AWS End User Messaging.

With AWS End User Messaging Push, you can engage users of your apps by sending push notifications through a push
notification channel. We support Apple Push Notification Service (APNs), Firebase Cloud Messaging (FCM), Amazon Device Messaging (ADM), and Baidu Push.

###### Topics

- [Are you a first-time AWS End User Messaging Push user?](#first-time-user "#first-time-user")
- [Features of AWS End User Messaging Push](#servicename-feature-overview "#servicename-feature-overview")
- [Accessing AWS End User Messaging Push](#acessing-servicename "#acessing-servicename")
- [Regional availability](#sms-regions "#sms-regions")

## Are you a first-time AWS End User Messaging Push user?

If you are a first-time user of AWS End User Messaging Push, we recommend that you begin by reading the following
sections:

- [Setting up an AWS account](setting-up.md "setting-up.md")
- [Getting started with AWS End User Messaging Push](getting-started.md "getting-started.md")
- [Creating an application and enabling push channels](procedure-enable-push.md "procedure-enable-push.md")

## Features of AWS End User Messaging Push

You can send push notifications to your apps using separate channels
for the following push notification services:

- Firebase Cloud Messaging (FCM)
- Apple Push Notification service (APNs)

###### Note

You can use APNs to send messages to iOS devices such as iPhones and iPads,
as well as to the Safari browser on macOS devices, such as Mac laptops and
desktops.

- Baidu Cloud Push
- Amazon Device Messaging (ADM)

## Accessing AWS End User Messaging Push

Briefly explain the different ways to gain access to the service, whether by console, CLI, or API.

You can manage AWS End User Messaging Push using the following interfaces:

**AWS End User Messaging Push console**
The web interface where you create and manage AWS End User Messaging Push resources. If you've signed up for an
AWS account, you can access the AWS End User Messaging Push console from the AWS Management Console.

**AWS Command Line Interface**
Interact with AWS services using commands in your command line shell. The AWS Command Line Interface is
supported on Windows, macOS, and Linux. For more information about the AWS CLI, see
[AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md"). You can find the AWS End User Messaging Push commands in the [AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md").

**AWS SDKs**

If you're a software developer that prefers to build applications using language-specific
APIs instead of submitting a request over HTTP or HTTPS, AWS provides libraries, sample
code, tutorials, and other resources. These libraries provide basic functions that automate
tasks, such as cryptographically signing your requests, retrying requests, and handling error
responses. These functions help make it more efficient for you to get started. For more
information, see [Tools to Build on
AWS](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").

## Regional availability

AWS End User Messaging Push is available in several AWS Regions in North America, Europe, Asia, and Oceania. In
each Region, AWS maintains multiple Availability Zones. These Availability Zones are physically
isolated from each other, but are united by private, low-latency, high-throughput, and highly
redundant network connections. These Availability Zones are used to provide very high levels of
availability and redundancy, while also minimizing latency.

To learn more about AWS Regions, see [Specify which
AWS Regions your account can use](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md") in the _Amazon Web Services General Reference_. For a list of all the Regions where AWS End User Messaging Push is currently
available and the endpoint for each Region, see [Endpoints and quotas](../../../general/latest/gr/pinpoint.md "../../../general/latest/gr/pinpoint.md") for Amazon Pinpoint API and [AWS service endpoints](../../../general/latest/gr/rande.md#pinpoint_region "../../../general/latest/gr/rande.md#pinpoint_region") in the _Amazon Web Services General Reference_. To learn more about the number of Availability
Zones that are available in each Region, see [AWS global
infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").
