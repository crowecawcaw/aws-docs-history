

AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md)

# Regions and quotas for Amazon Q Developer in chat applications

Although most AWS Regions are active by default for your AWS account, certain Regions are activated only when you manually select them. This document refers to those Regions as *opt-in Regions*. In contrast, Regions that are active by default, as soon as your AWS account is created, are referred to as *commercial Regions*, or simply, *Regions*.

## Supported Regions for Amazon Q Developer in chat applications
<a name="region-info"></a>

Supported Regions include:
+ US East (Ohio)
+ US East (N. Virginia)
+ US West (N. California)
+ US West (Oregon)
+ Asia Pacific (Mumbai)
+ Asia Pacific (Osaka)
+ Asia Pacific (Seoul)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)
+ Asia Pacific (Tokyo)
+ Canada (Central)
+ Europe (Frankfurt)
+ Europe (Ireland)
+ Europe (London)
+ Europe (Paris)
+ Europe (Stockholm)
+ South America (São Paulo)

You can combine Amazon SNS topics from multiple Regions in a single Amazon Q Developer in chat applications configuration.

### Data residency in Amazon Q Developer in chat applications
<a name="chatbot-data-residency"></a>

Amazon Q Developer in chat applications is a global service. Service resources are stored and replicated across four AWS Regions: US East (Ohio), US West (Oregon), Asia Pacific (Singapore), and Europe (Ireland). Amazon Q Developer in chat applications delivers notifications to chat channels, which can be processed in any of the four supported Regions.

The control plane APIs for Amazon Q Developer in chat applications are available in all four preceding Regions. The AWS Management Console for Amazon Q Developer in chat applications is available only in the US East (Ohio) Region.

To answer natural language questions in your chat channels, Amazon Q Developer in chat applications uses the AWS assistant. For information about how the AWS assistant stores and processes your data, see [Data storage in the AWS assistant](https://docs.aws.amazon.com/assistant/latest/userguide/data-storage.html) and [Cross-Region processing in the AWS assistant](https://docs.aws.amazon.com/assistant/latest/userguide/cross-region-processing.html) in the *AWS assistant User Guide*.

For more information about how Amazon Q Developer in chat applications protects your data, see [Data protection in Amazon Q Developer in chat applications](security.md#per-service-security).

### Opt-in Regions
<a name="opt-in-Regions"></a>

Opt-in Regions aren't enabled by default. You must manually enable these Regions to use them with Amazon Q Developer in chat applications. For more information about AWS Regions, see [Managing AWS Regions](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html). The following opt-in Regions are supported:
+ Africa (Cape Town)
+ Asia Pacific (Hong Kong)
+ Asia Pacific (Hyderabad)
+ Asia Pacific (Jakarta)
+ Asia Pacific (Malaysia)
+ Asia Pacific (Melbourne)
+ Asia Pacific (Thailand)
+ Canada West (Calgary)
+ Europe (Milan)
+ Europe (Spain)
+ Europe (Zurich)
+ Israel (Tel Aviv)
+ Middle East (Bahrain)
+ Middle East (UAE)
+ Mexico (Central)

## Endpoints and quotas for Amazon Q Developer in chat applications
<a name="chatbot-quotas"></a>

Amazon Q Developer in chat applications currently supports service endpoints, however there are no adjustable quotas. For more information about Amazon Q Developer in chat applications endpoints and quotas, see [Amazon Q Developer in chat applications endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/chatbot.html).