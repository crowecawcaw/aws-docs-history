

# AI services opt-out policies
<a name="orgs_manage_policies_ai-opt-out"></a>

AWS AI services may use and store customer content for service improvement, such as fixing operational issues, evaluating service performance, debugging, or model training. For this purpose, we might store such content in an AWS Region outside of the AWS Region where you are using the service. You can opt out of use of your content for service improvement by using the AWS Organizations opt-out policy.

You can create opt-out policies for an individual AI service, or for all services supported by AI services opt-out policies. You can also query the effective policy applicable to each account to see the effects of your setting choices.

For more detailed information, see [AWS Machine Learning and Artificial Intelligence Services](https://aws.amazon.com/service-terms) in the AWS Service Terms. For a list of services supported by AI services opt-out policies, see [List of supported AI services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out_all.html#ai-opt-out-all-list).

**Topics**
+ [Considerations](#orgs_manage_policies-ai-opt-out-considerations)
+ [Getting started](orgs_manage_policies-ai-opt-out_getting-started.md)
+ [Opt out from all AI services](orgs_manage_policies_ai-opt-out_all.md)
+ [AI services opt-out policy syntax and examples](orgs_manage_policies_ai-opt-out_syntax.md)

## Considerations when using AI services opt-out policies
<a name="orgs_manage_policies-ai-opt-out-considerations"></a>

**Opting out deletes all of the associated historical content**

When you opt out of content use by an AWS AI service, that service deletes all of the associated historical content that was shared with AWS before you set the option. This deletion is limited to content stored that is not required to provide service functions.

For example, when you use a service while opted in, that service might store copies of your content for service improvement. When you opt out, any copies that have been stored by the service for that purpose are deleted, but any content that is used to provide the service to you is not deleted.

### Your opt-out preference is recorded in every AWS Region
<a name="orgs_manage_policies-ai-opt-out-regions-metadata"></a>

When you set an AI services opt-out policy, AWS applies it across all AWS Regions where the supporting services operate, including AWS Regions that are disabled by default. To enforce your choice consistently, each AWS Region independently stores the metadata for your preference. This metadata includes your account identifier and opt-out selection, regardless of whether you have enabled or disabled that AWS Region.