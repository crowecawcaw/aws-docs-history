

# Service improvement for the AWS assistant
<a name="service-improvement"></a>

To help the AWS assistant provide the most relevant information, we may use certain content from the AWS assistant, such as questions that you ask the AWS assistant and its responses, for service improvement. This page explains what content we use and how to opt out.

## Free tier content used for service improvement
<a name="content-use"></a>

We may use certain content from the AWS assistant Free tier for service improvement. The AWS assistant may use this content, for example, to provide better responses to common questions, fix AWS assistant operational issues, for debugging, or for model training.

Content that AWS may use for service improvement includes, for example, your questions to the AWS assistant and the responses that the AWS assistant generates.

We do not use content from Amazon Q Developer Pro for service improvement.

## How to opt out
<a name="opt-out"></a>

To opt out of the AWS assistant Free tier using content for service improvement, configure an AI services opt-out policy in AWS Organizations. The AWS assistant uses the Amazon Q Developer opt-out setting (the `q` service name key in the policy). If you have already configured an opt-out policy for Amazon Q Developer (the `q` service name key), that policy also applies to the AWS assistant. You can also opt out of all AI services. The policy applies to the AWS Management Console and AWS Console Mobile Application. For more information, see [AI services opt-out policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html) in the *AWS Organizations User Guide*.