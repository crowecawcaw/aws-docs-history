

# Conformance Packs for AWS Config

A conformance pack is a collection of AWS Config rules and remediation actions that can be deployed as a single entity. AWS Config supports managed conformance packs and custom conformance packs.
+ AWS managed conformance packs are predefined and maintained by AWS. You can deploy an AWS managed conformance pack to an account and an AWS Region without creating or maintaining a conformance pack template.
+ Custom conformance packs are created by authoring a YAML template that contains a list of AWS Config managed or custom rules and remediation actions. Custom conformance packs can be deployed to an account and an AWS Region or across an organization in AWS Organizations. You can also use AWS Systems Manager documents (SSM documents) to store your custom conformance pack templates on AWS and directly deploy conformance packs using SSM document names. You can deploy the template by using the AWS Config console or the AWS CLI.

To get started, you can deploy a [managed conformance pack](managed-conformance-packs.md) or create your own [custom conformance pack](custom-conformance-packs.md). AWS Config also provides [sample conformance pack templates](conformancepack-sample-templates.md) that you can use as a starting point for creating your own conformance packs.

**Topics**
+ [Prerequisites](cpack-prerequisites.md)
+ [Conformance Pack Dashboard](conformance-pack-dashboard.md)
+ [Region Support](#conformance-packs-regions)
+ [Process Checks](process-checks.md)
+ [Managed Conformance Packs](managed-conformance-packs.md)
+ [Custom Conformance Packs](custom-conformance-packs.md)
+ [Deploying Conformance Packs](conformance-pack-deploy.md)
+ [Editing Conformance Packs](conformance-pack-edit.md)
+ [Deleting Conformance Packs](conformance-pack-delete.md)
+ [Viewing Conformance Packs](conformance-pack-view.md)
+ [Viewing Compliance History](compliance-history-conformance-pack.md)
+ [Querying Compliance History](querying-compliance-history-conformance-pack.md)
+ [Managing Organizational Conformance Packs](conformance-pack-organization-apis.md)
+ [Troubleshooting](troubleshooting-conformance-pack.md)

## Region Support
<a name="conformance-packs-regions"></a>

Conformance packs are supported in the following Regions.


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 |  config.us-east-2.amazonaws.com  | HTTPS | 
| US East (N. Virginia) | us-east-1 |  config.us-east-1.amazonaws.com  | HTTPS | 
| US West (N. California) | us-west-1 |  config.us-west-1.amazonaws.com  | HTTPS | 
| US West (Oregon) | us-west-2 |  config.us-west-2.amazonaws.com  | HTTPS | 
| Africa (Cape Town) | af-south-1 |  config.af-south-1.amazonaws.com  | HTTPS | 
| Asia Pacific (Hong Kong) | ap-east-1 |  config.ap-east-1.amazonaws.com  | HTTPS | 
| Asia Pacific (Hyderabad) | ap-south-2 |  config.ap-south-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Jakarta) | ap-southeast-3 |  config.ap-southeast-3.amazonaws.com  | HTTPS | 
| Asia Pacific (Malaysia) | ap-southeast-5 |  config.ap-southeast-5.amazonaws.com  | HTTPS | 
| Asia Pacific (Melbourne) | ap-southeast-4 |  config.ap-southeast-4.amazonaws.com  | HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 |  config.ap-south-1.amazonaws.com  | HTTPS | 
| Asia Pacific (New Zealand) | ap-southeast-6 |  config.ap-southeast-6.amazonaws.com  | HTTPS | 
| Asia Pacific (Osaka) | ap-northeast-3 |  config.ap-northeast-3.amazonaws.com  | HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 |  config.ap-northeast-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 |  config.ap-southeast-1.amazonaws.com  | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 |  config.ap-southeast-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Taipei) | ap-east-2 |  config.ap-east-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Thailand) | ap-southeast-7 |  config.ap-southeast-7.amazonaws.com  | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 |  config.ap-northeast-1.amazonaws.com  | HTTPS | 
| Canada (Central) | ca-central-1 |  config.ca-central-1.amazonaws.com  | HTTPS | 
| Canada West (Calgary) | ca-west-1 |  config.ca-west-1.amazonaws.com  | HTTPS | 
| Europe (Frankfurt) | eu-central-1 |  config.eu-central-1.amazonaws.com  | HTTPS | 
| Europe (Ireland) | eu-west-1 |  config.eu-west-1.amazonaws.com  | HTTPS | 
| Europe (London) | eu-west-2 |  config.eu-west-2.amazonaws.com  | HTTPS | 
| Europe (Milan) | eu-south-1 |  config.eu-south-1.amazonaws.com  | HTTPS | 
| Europe (Paris) | eu-west-3 |  config.eu-west-3.amazonaws.com  | HTTPS | 
| Europe (Spain) | eu-south-2 |  config.eu-south-2.amazonaws.com  | HTTPS | 
| Europe (Stockholm) | eu-north-1 |  config.eu-north-1.amazonaws.com  | HTTPS | 
| Europe (Zurich) | eu-central-2 |  config.eu-central-2.amazonaws.com  | HTTPS | 
| Israel (Tel Aviv) | il-central-1 |  config.il-central-1.amazonaws.com  | HTTPS | 
| Mexico (Central) | mx-central-1 |  config.mx-central-1.amazonaws.com  | HTTPS | 
| Middle East (Bahrain) | me-south-1 |  config.me-south-1.amazonaws.com  | HTTPS | 
| Middle East (UAE) | me-central-1 |  config.me-central-1.amazonaws.com  | HTTPS | 
| South America (São Paulo) | sa-east-1 |  config.sa-east-1.amazonaws.com  | HTTPS | 
|  AWS GovCloud (US-East) | us-gov-east-1 |  config.us-gov-east-1.amazonaws.com  | HTTPS | 
|  AWS GovCloud (US-West) | us-gov-west-1 |  config.us-gov-west-1.amazonaws.com  | HTTPS | 

Deploying conformance packs across member accounts in an AWS Organization is supported in the following Regions.


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 |  config.us-east-2.amazonaws.com  | HTTPS | 
| US East (N. Virginia) | us-east-1 |  config.us-east-1.amazonaws.com  | HTTPS | 
| US West (N. California) | us-west-1 |  config.us-west-1.amazonaws.com  | HTTPS | 
| US West (Oregon) | us-west-2 |  config.us-west-2.amazonaws.com  | HTTPS | 
| Africa (Cape Town) | af-south-1 |  config.af-south-1.amazonaws.com  | HTTPS | 
| Asia Pacific (Hong Kong) | ap-east-1 |  config.ap-east-1.amazonaws.com  | HTTPS | 
| Asia Pacific (Hyderabad) | ap-south-2 |  config.ap-south-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Jakarta) | ap-southeast-3 |  config.ap-southeast-3.amazonaws.com  | HTTPS | 
| Asia Pacific (Malaysia) | ap-southeast-5 |  config.ap-southeast-5.amazonaws.com  | HTTPS | 
| Asia Pacific (Melbourne) | ap-southeast-4 |  config.ap-southeast-4.amazonaws.com  | HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 |  config.ap-south-1.amazonaws.com  | HTTPS | 
| Asia Pacific (New Zealand) | ap-southeast-6 |  config.ap-southeast-6.amazonaws.com  | HTTPS | 
| Asia Pacific (Osaka) | ap-northeast-3 |  config.ap-northeast-3.amazonaws.com  | HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 |  config.ap-northeast-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 |  config.ap-southeast-1.amazonaws.com  | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 |  config.ap-southeast-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Taipei) | ap-east-2 |  config.ap-east-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Thailand) | ap-southeast-7 |  config.ap-southeast-7.amazonaws.com  | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 |  config.ap-northeast-1.amazonaws.com  | HTTPS | 
| Canada (Central) | ca-central-1 |  config.ca-central-1.amazonaws.com  | HTTPS | 
| Canada West (Calgary) | ca-west-1 |  config.ca-west-1.amazonaws.com  | HTTPS | 
| Europe (Frankfurt) | eu-central-1 |  config.eu-central-1.amazonaws.com  | HTTPS | 
| Europe (Ireland) | eu-west-1 |  config.eu-west-1.amazonaws.com  | HTTPS | 
| Europe (London) | eu-west-2 |  config.eu-west-2.amazonaws.com  | HTTPS | 
| Europe (Milan) | eu-south-1 |  config.eu-south-1.amazonaws.com  | HTTPS | 
| Europe (Paris) | eu-west-3 |  config.eu-west-3.amazonaws.com  | HTTPS | 
| Europe (Spain) | eu-south-2 |  config.eu-south-2.amazonaws.com  | HTTPS | 
| Europe (Stockholm) | eu-north-1 |  config.eu-north-1.amazonaws.com  | HTTPS | 
| Europe (Zurich) | eu-central-2 |  config.eu-central-2.amazonaws.com  | HTTPS | 
| Israel (Tel Aviv) | il-central-1 |  config.il-central-1.amazonaws.com  | HTTPS | 
| Mexico (Central) | mx-central-1 |  config.mx-central-1.amazonaws.com  | HTTPS | 
| Middle East (Bahrain) | me-south-1 |  config.me-south-1.amazonaws.com  | HTTPS | 
| Middle East (UAE) | me-central-1 |  config.me-central-1.amazonaws.com  | HTTPS | 
| South America (São Paulo) | sa-east-1 |  config.sa-east-1.amazonaws.com  | HTTPS | 
|  AWS GovCloud (US-East) | us-gov-east-1 |  config.us-gov-east-1.amazonaws.com  | HTTPS | 
|  AWS GovCloud (US-West) | us-gov-west-1 |  config.us-gov-west-1.amazonaws.com  | HTTPS | 