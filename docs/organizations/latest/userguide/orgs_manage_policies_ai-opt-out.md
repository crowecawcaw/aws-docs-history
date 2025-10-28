# AI services opt-out policies

AWS AI services may use and store customer content for service improvement, such as fixing
operational issues, evaluating service performance, debugging, or model training. For this
purpose, we might store such content in an AWS Region outside of the AWS Region where you
are using the service. You can opt out of use of your content for service improvement by
using the AWS Organizations opt-out policy.

You can create opt-out policies for an individual AI service, or for all services
supported by AI services opt-out policies. You can also query the effective policy
applicable to each account to see the effects of your setting choices.

For more detailed information, see [AWS
Machine Learning and Artificial Intelligence Services](https://aws.amazon.com/service-terms "https://aws.amazon.com/service-terms") in the AWS Service
Terms. For a list of services supported by AI services opt-out policies, see [List of supported AI services](orgs_manage_policies_ai-opt-out_all.md#ai-opt-out-all-list "orgs_manage_policies_ai-opt-out_all.md#ai-opt-out-all-list").

###### Topics

- [Considerations](#orgs_manage_policies-ai-opt-out-considerations "#orgs_manage_policies-ai-opt-out-considerations")
- [Getting started](orgs_manage_policies-ai-opt-out_getting-started.md "orgs_manage_policies-ai-opt-out_getting-started.md")
- [Opt out from all AI services](orgs_manage_policies_ai-opt-out_all.md "orgs_manage_policies_ai-opt-out_all.md")
- [AI services opt-out policy syntax and
  examples](orgs_manage_policies_ai-opt-out_syntax.md "orgs_manage_policies_ai-opt-out_syntax.md")

## Considerations when

using AI services opt-out policies

**Opting out deletes all of the associated historical
content**

When you opt out of content use by an AWS AI service, that service deletes all of
the associated historical content that was shared with AWS before you set the option.
This deletion is limited to content stored that is not required to provide service
functions.

For example, when you use a service while opted in, that service might store copies of
your content for service improvement. When you opt out, any copies that have been stored by
the service for that purpose are deleted, but any content that is used to provide
the service to you is not deleted.
