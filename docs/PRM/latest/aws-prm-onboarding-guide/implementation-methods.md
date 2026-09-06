

# Implementation Methods
<a name="implementation-methods"></a>

Partner Revenue Measurement supports the following implementation methods. Choose the method that best fits your product type and architecture.

## Methods Overview
<a name="methods-overview"></a>


| Method | Description | Best For | 
| --- | --- | --- | 
| [AWS Marketplace Metering](marketplace-metering.md) | Zero-touch revenue attribution through AWS Marketplace product metadata | Amazon Machine Image (AMI) and Machine Learning (ML) products listed on AWS Marketplace | 
| [Resource Tagging](resource-tagging.md) | Tag AWS resources with your product code using the aws-apn-id tag key | SaaS, Professional Services, and any product type where you can tag AWS resources | 
| [User Agent String](user-agent-string.md) | Include a User Agent string in regular AWS API/CLI calls with your product code | Products with direct regular AWS API/CLI access; AMI/ML products seeking attribution beyond EC2/SageMaker | 

**Note**  
You can implement multiple methods simultaneously. For example, an AMI product can benefit from AWS Marketplace Metering for EC2 attribution and User Agent String for attribution on additional AWS services used by the product.

## Choosing the Right Method
<a name="choosing-method"></a>

The following table provides guidance on choosing the right method based on your scenario:


| Scenario | Use Resource Tagging when... | Use User Agent String when... | Marketplace Metering | 
| --- | --- | --- | --- | 
| Marketplace AMI/ML | — | — | Automatic | 
| Partner Account (SaaS) | Static infrastructure, deploy once and runs long-term | Partner solution makes frequent regular AWS API/CLI calls | — | 
| Customer Account (deploy/manage) | Deploy via IaC (CloudFormation, Terraform), customer allows tags | Partner solution makes ongoing regular AWS API/CLI calls, or customer has strict tag policies | — | 
| Customer Account (read/access only) | Customer willing to tag their resources | Your solution makes read API calls | — | 
| Hybrid (Partner \+ Customer) | Taggable resources in either account | Partner solution makes regular AWS API/CLI calls in either account | — | 

## Decision Tree
<a name="decision-tree"></a>

The following decision tree helps you determine the right implementation method:



![Partner Revenue Measurement decision tree for choosing between AWS Marketplace Metering, Resource Tagging, and User Agent String implementation methods](http://docs.aws.amazon.com/PRM/latest/aws-prm-onboarding-guide/images/PRM-decision-tree.png)




## Special Scenarios
<a name="special-scenarios"></a>


| Scenario | Use Resource Tagging when... | Use User Agent String when... | Marketplace Metering | 
| --- | --- | --- | --- | 
| Managed Services Provider (MSP) or Systems Integrator (SI/GSI) with limited access | Where write access allows. Provide IaC templates with tags embedded for customer to run | In management regular AWS API/CLI calls. Modify agents or installers to include UA strings | — | 
| Multi-partner on same AWS resource | Single aws-apn-id tag limit per resource — may conflict with other partners | Each partner uses own UA string in their respective regular AWS API/CLI calls, no conflicts | — | 
| Backfill existing resources | Bulk tag via Tag Editor or scripted bulk tagging for large-scale backfill. Revenue attribution will only be moving forward from the time tags are applied | Add UA to existing regular AWS API/CLI calls — often the lowest-effort path. Revenue attribution will only be moving forward from the time User Agent strings are implemented | — | 

## Key Considerations
<a name="key-considerations"></a>
+ **Resource Tagging:** Tags are key-value pairs applied to a resource to hold metadata about that resource, in this case a partner identifier. The tag type is a user-defined tag, and can be managed (updated or removed), and counts against the 50-tag-per-resource limit. Only one partner identifier is allowed per resource. Attribution is continuous while the tag is present.
+ **User Agent String:** Ephemeral, specific to the regular AWS API/CLI operation carried out on a specific AWS resource, and is read-only. Allows multiple partners to independently use their identifier within their respective regular AWS API/CLI calls. Visible in CloudTrail, enabling customers to govern partner-solution interactions within their AWS resources. Requires at least one regular AWS API/CLI call per resource per month for attribution.
+ **Multi-partner:** User Agent String avoids the single `aws-apn-id` tag-per-resource limitation when multiple partners operate on the same AWS resource.
+ **Production only:** Partner Revenue Measurement is intended to measure production workloads. Dev/test/staging environments can be used for validating your implementation before rolling out to production.