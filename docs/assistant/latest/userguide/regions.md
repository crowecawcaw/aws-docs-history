

# Supported AWS Regions for the AWS assistant
<a name="regions"></a>

This topic lists the AWS Regions where you can use the AWS assistant. For more information about Regions, see [Specify which AWS Regions your account can use](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html) in the *AWS Account Management Reference Guide*.

Your requests might be processed in a different Region from the Region where you use the AWS assistant. For more information, see [Cross-Region processing in the AWS assistant](cross-region-processing.md). For information about where data is stored, see [Data storage in the AWS assistant](data-storage.md).

**Note**  
If a request needs information from an [opt-in Region (Region that is disabled by default)](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#optinregion) that isn't listed on this page, the AWS assistant can call that Region. To control which Regions the AWS assistant can call, see [Allow the AWS assistant to perform actions in specific Regions](security-iam-examples.md#iam-example-some-regions).

## Regions that are enabled by default
<a name="default-regions"></a>

You can use the AWS assistant in the AWS Management Console and AWS Console Mobile Application in the following Regions. You don't need to enable these Regions before you use them. Some features might not be available in every Region. Check the topic for each feature.
+ US East (Ohio) (`us-east-2`)
+ US East (N. Virginia) (`us-east-1`)
+ US West (N. California) (`us-west-1`)
+ US West (Oregon) (`us-west-2`)
+ Asia Pacific (Mumbai) (`ap-south-1`)
+ Asia Pacific (Osaka) (`ap-northeast-3`)
+ Asia Pacific (Seoul) (`ap-northeast-2`)
+ Asia Pacific (Singapore) (`ap-southeast-1`)
+ Asia Pacific (Sydney) (`ap-southeast-2`)
+ Asia Pacific (Tokyo) (`ap-northeast-1`)
+ Canada (Central) (`ca-central-1`)
+ Europe (Frankfurt) (`eu-central-1`)
+ Europe (Ireland) (`eu-west-1`)
+ Europe (London) (`eu-west-2`)
+ Europe (Paris) (`eu-west-3`)
+ Europe (Stockholm) (`eu-north-1`)
+ South America (São Paulo) (`sa-east-1`)

## Regions that are disabled by default
<a name="opt-in-regions"></a>

You can use the AWS assistant in the following opt-in Regions at the Free tier only. You must enable an opt-in Region for your AWS account before you can use it. For more information, see [Opt-in Region](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#optinregion) in the *AWS Glossary*.
+ Africa (Cape Town) (`af-south-1`)
+ Asia Pacific (Hong Kong) (`ap-east-1`)
+ Asia Pacific (Hyderabad) (`ap-south-2`)
+ Asia Pacific (Jakarta) (`ap-southeast-3`)
+ Asia Pacific (Malaysia) (`ap-southeast-5`)
+ Asia Pacific (Melbourne) (`ap-southeast-4`)
+ Asia Pacific (Thailand) (`ap-southeast-7`)
+ Canada West (Calgary) (`ca-west-1`)
+ Europe (Milan) (`eu-south-1`)
+ Europe (Spain) (`eu-south-2`)
+ Europe (Zurich) (`eu-central-2`)
+ Mexico (Central) (`mx-central-1`)
+ Middle East (Bahrain) (`me-south-1`)
+ Middle East (UAE) (`me-central-1`)
+ Israel (Tel Aviv) (`il-central-1`)

## Administration Regions
<a name="administration-regions"></a>

Administrators manage Pro tier subscriptions in the Amazon Q Developer console with an Amazon Q Developer profile. The console and profile are supported in the following Regions:
+ US East (N. Virginia) (`us-east-1`)
+ Europe (Frankfurt) (`eu-central-1`)

This limitation doesn't restrict the Regions where you can use the AWS assistant.

If your profile is in the Europe (Frankfurt) Region, you can't use the following features at the Pro tier:
+ [Contacting AWS Support](support.md)
+ [Troubleshoot resources](resources.md#troubleshoot-resources)
+ AWS assistant in the AWS Console Mobile Application