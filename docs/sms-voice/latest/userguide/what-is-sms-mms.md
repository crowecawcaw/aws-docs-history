# What is AWS End User Messaging SMS?

###### Note

The SMS, MMS, and voice (text to speech) features of Amazon Pinpoint are now called AWS End User
Messaging.

[AWS End User Messaging SMS](https://aws.amazon.com/end-user-messaging/sms/ "https://aws.amazon.com/end-user-messaging/sms/") is an application-to-person (A2P) SMS, MMS, and voice messaging service which
provides the global scale, resiliency, and flexibility required to deliver SMS messaging in any
web, mobile, or business applications. SMS messages are used for their most important and urgent
communications as SMS proves to be the most effective and ubiquitous communication channel
available. Customers prioritize time critical and must-deliver use-cases such as one-time password
(OTP) login and authentication, marketing messages, citizen outreach, delivery status updates, or
appointment reminders to name a few.

Multimedia messaging service (MMS) is an extension of SMS that provides the ability to send media
messages to a mobile phone which includes image, audio, text, or video files. You can use MMS to
improve engagement through a variety of branding, workflow, and marketing use cases.

The information in this user guide is intended for all AWS End User Messaging SMS users, including
marketers, business users, and developers. This guide contains information that's especially
helpful for users who mainly interact with AWS End User Messaging SMS by using the AWS Management Console.

###### Note

AWS End User Messaging SMS uses the `pinpoint-sms-voice-v2` API namespace.

There are several other documents that are companions to this document. The following documents provide reference information related to the AWS End User Messaging SMS APIs:

- [AWS End User Messaging SMS and Voice v2 API](../../../pinpoint/latest/apireference_smsvoicev2/Welcome.md "../../../pinpoint/latest/apireference_smsvoicev2/Welcome.md")
- [AWS End User Messaging SMS and Voice v2 AWS CLI reference](../../../cli/latest/reference/pinpoint-sms-voice-v2.md "../../../cli/latest/reference/pinpoint-sms-voice-v2.md")
  AWS End User Messaging SMS includes an API (called the AWS End User Messaging SMS and Voice v2 API) that was designed for sending SMS,
  MMS and voice messages. While the Amazon Pinpoint API is focused on sending messages through scheduled and
  event-driven campaigns and journeys, the AWS End User Messaging SMS and Voice v2 API provides dedicated features and
  capabilities for sending SMS, MMS, and voice messages directly to individual recipients. You can
  use AWS End User Messaging SMS and Voice API v2 independently of the Amazon Pinpoint campaign and journey features, or you can use
  both at the same time to accommodate different use cases. If you already use Amazon Pinpoint to send SMS,
  MMS, or voice messages, your account is already configured to use this API. Here are some key
  feature differences between the two APIs.

| APIs                  | Amazon Pinpoint API                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | AWS End User Messaging SMS and Voice v2 API                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Features              | 1. *Projects<br>• – a project is a collection of recipient information, segments, campaigns,<br>and journeys.<br>2. *Multichannel<br>• – a channel represents the platform through which you engage<br>your audience segment with messages.<br>3. *Segments<br>• – a segment is a group of your customers<br>that share certain attributes.<br>4. *Campaigns<br>• – a campaign is a messaging initiative that<br>engages a specific audience segment.<br>5. *Journeys<br>• – a journey is a customized, multi-step<br>engagement experience.<br>6. *Analytics<br>• – using the analytics that Amazon Pinpoint provides, you<br>can gain insight into your user base by viewing trends related to user engagement, campaign<br>outreach, revenue, and more. | 1. *Phone pool<br>• – a phone pool is a collection of phone numbers<br>and sender IDs that share the same settings that you can use to send messages and provide<br>failover if a number in the pool fails.<br>2. *Phone number<br>• – a phone number, also called originator number, is a numeric string of numbers that identifies the sender.<br>3. *Sender ID<br>• – a sender ID is an alphanumeric name that identifies the sender of an SMS message.<br>4. *Configuration sets<br>• – a configuration set is a set of rules that are applied when you send a message.<br>5. *Opt-out lists<br>• – an opt-out list is list of destination identities that should not have messages sent to them.<br>6. *Registrations<br>• – some countries require phone numbers and sender IDs<br>to be registered for use in the country. In AWS End User Messaging SMS you can manage your registrations.<br>7. *Multimedia messaging service (MMS)<br>• – send media messages to a mobile phone which includes image, audio, text, or video files.<br>8. *Protect configurations<br>• – to build a list of country rules that<br>allow or block messages to each destination country in the world. |
| Number of AWS Regions | 13 AWS Regions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 30 AWS Regions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

This API is a good solution for users who have a multi-tenant architecture, such as
Independent Software Vendors (ISVs). This API can be used to establish that event data,
origination phone numbers, and opt-out lists are separated for different tenants.

When you use the SMS and Voice v2 API, we recommend that you set up phone pools,
configuration sets and event destinations. The SMS and Voice v2 API doesn't automatically emit
event data for the messages that you send. Setting up event destinations to capture important
event data, such as message delivery and failure events.

Version 2 of this API was preceded by Version 1. If you currently use Version 1 of this
API, it will continue to be available, and you can continue to use it. However, if you
migrate to Version 2, you will gain additional features, such as the ability to create pools
of phone numbers, request new phone numbers programmatically, and enable or disable certain
capabilities of phone numbers.

###### Topics

- [Are you a first-time AWS End User Messaging SMS user?](#first-time-user "#first-time-user")
- [Features of AWS End User Messaging SMS](#servicename-feature-overview "#servicename-feature-overview")
- [Accessing AWS End User Messaging SMS](#acessing-servicename "#acessing-servicename")
- [Regional availability](#sms-regions "#sms-regions")
- [How does SMS messaging work](what-is-sms.md "what-is-sms.md")
- [AWS End User Messaging SMS concepts](what-is-concepts.md "what-is-concepts.md")

## Are you a first-time AWS End User Messaging SMS user?

If you're using AWS End User Messaging SMS for the first time, we recommend that you first read the following
sections:

- [How Short Message Service (SMS) works](what-is-sms.md "what-is-sms.md")
- [Tutorial for sending a message using AWS End User Messaging SMS](getting-started-tutorial.md "getting-started-tutorial.md")

## Features of AWS End User Messaging SMS

AWS End User Messaging SMS provides the following features and capabilities:

**Global application-to-person messaging**
Application-to-person messaging provides SMS and MMS messaging to mobile phone
numbers.

**Registration of origination identities**
Use AWS End User Messaging SMS to register your phone numbers or sender IDs and track the registration
status.

**SMS simulator**

Use the SMS simulator to test your messaging environment.

## Accessing AWS End User Messaging SMS

You can request and manage your AWS End User Messaging SMS origination identities (phone number or sender ID)
using the following interfaces:

**AWS End User Messaging SMS console**
The web interface where you create and manage AWS End User Messaging SMS resources. If you've signed up for an
AWS account, you can access the AWS End User Messaging SMS console from the AWS Management Console.

**AWS Command Line Interface**
Interact with AWS services using commands in your command line shell. The AWS Command Line Interface is
supported on Windows, macOS, and Linux. For more information about the AWS CLI, see
[AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md"). You can find the AWS End User Messaging SMS commands in the [AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md").

**AWS SDKs**

If you're a software developer that prefers to build applications using language-specific
APIs instead of submitting a request over HTTP or HTTPS, AWS provides libraries, sample
code, tutorials, and other resources. These libraries provide basic functions that automate
tasks, such as cryptographically signing your requests, retrying requests, and handling error
responses. These functions help make it more efficient for you to get started. For more
information, see [Tools to Build on
AWS](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").

## Regional availability

AWS End User Messaging SMS is available in several AWS Regions in North America, Europe, Asia, and Oceania. In
each Region, AWS maintains multiple Availability Zones. These Availability Zones are physically
isolated from each other, but are united by private, low-latency, high-throughput, and highly
redundant network connections. These Availability Zones are used to provide very high levels of
availability and redundancy, while also minimizing latency.

To learn more about AWS Regions, see [Specify which
AWS Regions your account can use](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md") in the _Amazon Web Services General Reference_. For a list of all the Regions where AWS End User Messaging SMS is currently available
and the endpoint for each Region, see [Endpoints and quotas](../../../general/latest/gr/end-user-messaging.md "../../../general/latest/gr/end-user-messaging.md") for AWS End User Messaging SMS and Voice v2 API and [AWS service endpoints](../../../general/latest/gr/rande.md#pinpoint_region "../../../general/latest/gr/rande.md#pinpoint_region") in the _Amazon Web Services General Reference_ or the following table. To learn more about the
number of Availability Zones that are available in each Region, see [AWS global
infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

| Region availability       | Region name    | Region                                                                              | Endpoint | Supports SMS/MMS channel | Supports voice channel |
| ------------------------- | -------------- | ----------------------------------------------------------------------------------- | -------- | ------------------------ | ---------------------- |
| US East (N. Virginia)     | us-east-1      | sms-voice.us-east-1.amazonaws.com<br>sms-voice-fips.us-east-1.amazonaws.com         | Yes      | Yes                      |
| US East (Ohio)            | us-east-2      | sms-voice.us-east-2.amazonaws.com<br>sms-voice-fips.us-east-2.amazonaws.com         | Yes      | Yes                      |
| US West (N. California)   | us-west-1      | sms-voice.us-west-1.amazonaws.com<br>sms-voice-fips.us-west-1.amazonaws.com         | Yes      | Yes                      |
| US West (Oregon)          | us-west-2      | sms-voice.us-west-2.amazonaws.com<br>sms-voice-fips.us-west-2.amazonaws.com         | Yes      | Yes                      |
| Africa (Cape Town)        | af-south-1     | sms-voice.af-south-1.amazonaws.com                                                  | Yes      | Yes                      |
| Asia Pacific (Hyderabad)  | ap-south-2     | sms-voice.ap-south-2.amazonaws.com                                                  | Yes      | No                       |
| Asia Pacific (Jakarta)    | ap-southeast-3 | sms-voice.ap-southeast-3.amazonaws.com                                              | Yes      | No                       |
| Asia Pacific (Melbourne)  | ap-southeast-4 | sms-voice.ap-southeast-4.amazonaws.com                                              | Yes      | No                       |
| Asia Pacific (Mumbai)     | ap-south-1     | sms-voice.ap-south-1.amazonaws.com                                                  | Yes      | Yes                      |
| Asia Pacific (Osaka)      | ap-northeast-3 | sms-voice.ap-northeast-3.amazonaws.com                                              | Yes      | Yes                      |
| Asia Pacific (Seoul)      | ap-northeast-2 | sms-voice.ap-northeast-2.amazonaws.com                                              | Yes      | Yes                      |
| Asia Pacific (Singapore)  | ap-southeast-1 | sms-voice.ap-southeast-1.amazonaws.com                                              | Yes      | Yes                      |
| Asia Pacific (Sydney)     | ap-southeast-2 | sms-voice.ap-southeast-2.amazonaws.com                                              | Yes      | Yes                      |
| Asia Pacific (Tokyo)      | ap-northeast-1 | sms-voice.ap-northeast-1.amazonaws.com                                              | Yes      | Yes                      |
| AWS GovCloud (US-East)    | us-gov-east-1  | sms-voice.us-gov-east-1.amazonaws.com<br>sms-voice-fips.us-gov-east-1.amazonaws.com | Yes      | No                       |
| AWS GovCloud (US-West)    | us-gov-west-1  | sms-voice.us-gov-west-1.amazonaws.com<br>sms-voice-fips.us-gov-west-1.amazonaws.com | Yes      | Yes                      |
| Canada (Central)          | ca-central-1   | sms-voice.ca-central-1.amazonaws.com<br>sms-voice-fips.ca-central-1.amazonaws.com   | Yes      | Yes                      |
| Canada West (Calgary)     | ca-west-1      | sms-voice.ca-west-1.amazonaws.com<br>sms-voice-fips.ca-west-1.amazonaws.com         | Yes      | No                       |
| Europe (Frankfurt)        | eu-central-1   | sms-voice.eu-central-1.amazonaws.com                                                | Yes      | Yes                      |
| Europe (Ireland)          | eu-west-1      | sms-voice.eu-west-1.amazonaws.com                                                   | Yes      | Yes                      |
| Europe (London)           | eu-west-2      | sms-voice.eu-west-2.amazonaws.com                                                   | Yes      | Yes                      |
| Europe (Milan)            | eu-south-1     | sms-voice.eu-south-1.amazonaws.com                                                  | Yes      | No                       |
| Europe (Paris)            | eu-west-3      | sms-voice.eu-west-3.amazonaws.com                                                   | Yes      | Yes                      |
| Europe (Spain)            | eu-south-2     | sms-voice.eu-south-2.amazonaws.com                                                  | Yes      | No                       |
| Europe (Stockholm)        | eu-north-1     | sms-voice.eu-north-1.amazonaws.com                                                  | Yes      | Yes                      |
| Europe (Zurich)           | eu-central-2   | sms-voice.eu-central-2.amazonaws.com                                                | Yes      | No                       |
| Israel (Tel Aviv)         | il-central-1   | sms-voice.il-central-1.amazonaws.com                                                | Yes      | No                       |
| Middle East (Bahrain)     | me-south-1     | sms-voice.me-south-1.amazonaws.com                                                  | Yes      | Yes                      |
| Middle East (UAE)         | me-central-1   | sms-voice.me-central-1.amazonaws.com                                                | Yes      | No                       |
| South America (São Paulo) | sa-east-1      | sms-voice.sa-east-1.amazonaws.com                                                   | Yes      | Yes                      |
