# IAM Identity Center Region data storage and operations

Learn how IAM Identity Center handles data storage and operations across AWS Regions.


## Understand how IAM Identity Center stores data


When you enable IAM Identity Center, all the data that you configure in IAM Identity Center is stored in the Region
 where you configured it. This data includes directory configurations, permission sets,
 application instances, and user assignments to AWS account applications. If you are using
 the IAM Identity Center identity store, all users and groups that you create in IAM Identity Center are also stored in the
 same Region. 


## Cross-Region emails with Amazon SES


 IAM Identity Center uses [Amazon Simple Email Service (Amazon SES)](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html "https://docs.aws.amazon.com/ses/latest/dg/Welcome.html") to send emails to end users when they
 attempt to sign-in with one-time password (OTP) as a second authentication factor. These
 emails are also sent for certain identity and credential management events, such as when the
 user is invited to set up an initial password, to verify an email address, and reset their
 password. Amazon SES is available in a subset of AWS Regions that IAM Identity Center supports. 


 IAM Identity Center calls Amazon SES local endpoints when Amazon SES is available locally in an AWS Region.
 When Amazon SES isn't available locally, IAM Identity Center calls Amazon SES endpoints in a different
 AWS Region, as indicated in the following table. 




| IAM Identity Center Region code | IAM Identity Center Region name | Amazon SES Region code | Amazon SES Region name |
| --- | --- | --- | --- |
| ap-east-1 | Asia Pacific (Hong Kong) | ap-northeast-2 | Asia Pacific (Seoul) |
| ap-south-2 | Asia Pacific (Hyderabad) | ap-south-1 | Asia Pacific (Mumbai) |
| ap-southeast-4 | Asia Pacific (Melbourne) | ap-southeast-2 | Asia Pacific (Sydney) |
| ap-southeast-5 | Asia Pacific (Malaysia) | ap-southeast-1 | Asia Pacific (Singapore) |
| ap-southeast-7 | Asia Pacific (Thailand) | ap-northeast-3 | Asia Pacific (Osaka) |
| ca-west-1 | Canada West (Calgary) | ca-central-1 | Canada (Central) |
| eu-south-2 | Europe (Spain) | eu-west-3 | Europe (Paris) |
| eu-central-2 | Europe (Zurich) | eu-central-1 | Europe (Frankfurt) |
| mx-central-1 | Mexico (Central) | us-east-2 | US East (Ohio) |
| me-central-1 | Middle East (UAE) | eu-central-1 | Europe (Frankfurt) |
| us-gov-east-1 | AWS GovCloud (US-East) | us-gov-west-1 | AWS GovCloud (US-West) | In these cross-Region calls, IAM Identity Center might send the following user attributes: <br>• Email address <br>• First name <br>• Last name <br>• Account in AWS Organizations <br>• AWS access portal URL <br>• Username <br>• Directory ID <br>• User ID ## Managing IAM Identity Center in an opt-in Region (Region that is disabled by default) Most AWS Regions are enabled for operations in all AWS services by default, but you must enable the following [opt-in Regions](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html?icmpid=docs_homepage_addtlrcs#optinregion "https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html?icmpid=docs_homepage_addtlrcs#optinregion") if you want to use IAM Identity Center: <br>• Africa (Cape Town) <br>• Asia Pacific (Hong Kong) <br>• Asia Pacific (Hyderabad) <br>• Asia Pacific (Jakarta) <br>• Asia Pacific (Melbourne) <br>• Asia Pacific (Malaysia) <br>• Asia Pacific (Thailand) <br>• Canada West (Calgary) <br>• Europe (Milan) <br>• Europe (Spain) <br>• Europe (Zurich) <br>• Israel (Tel Aviv) <br>• Mexico (Central) <br>• Middle East (Bahrain) <br>• Middle East (UAE) If you deploy IAM Identity Center in an opt-in Region, then you must enable this Region in all the accounts for which you want to manage access to IAM Identity Center. All accounts need this configuration, whether or not you'll create resources in that Region. You can enable a Region for the current accounts in your organization and you must repeat this action when you add new accounts. For instructions, see [Enable or disable a Region in your organization](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html#manage-acct-regions-enable-organization "https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html#manage-acct-regions-enable-organization") in the *AWS Organizations User Guide*. To avoid repeating these additional steps, you can choose to deploy your IAM Identity Center in a [Region enabled by default](#regions-enabled-by-default "#regions-enabled-by-default"). ###### Note Your AWS member account must be opted into the same Region as the opt-in Region where your IAM Identity Center instance is located, so you can access the AWS member account from the AWS access portal. ###### Metadata stored in opt-in Regions When you enable IAM Identity Center for a management account in an opt-in AWS Region, the following IAM Identity Center metadata for any member accounts is stored in the Region. <br>• Account ID <br>• Account name <br>• Account email <br>• Amazon Resource Names (ARNs) of the IAM roles that IAM Identity Center creates in the member account ## AWS Regions that are enabled by default The following Regions are enabled by default and you can enable IAM Identity Center in these Regions. <br>• US East (Ohio) <br>• US East (N. Virginia) <br>• US West (Oregon) <br>• US West (N. California) <br>• Europe (Paris) <br>• South America (São Paulo) <br>• Asia Pacific (Mumbai) <br>• Europe (Stockholm) <br>• Asia Pacific (Seoul) <br>• Asia Pacific (Tokyo) <br>• Europe (Ireland) <br>• Europe (Frankfurt) <br>• Europe (London) <br>• Asia Pacific (Singapore) <br>• Asia Pacific (Sydney) <br>• Canada (Central) <br>• Asia Pacific (Osaka)
