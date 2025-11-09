# Using the Access Policy Language in Amazon SNS

The following figure and table describe the general process of how access control works
with the access policy language.

![The six-step process of how access control works with the access policy language in AWS. It starts with writing a policy for your resource, adding it to the system, and then proceeds through the stages of a requester making a request, the AWS service evaluating the applicable policies, and finally, the service either granting or denying the request based on the evaluation.](images/AccessPolicyLanguage_Basic_Flow.gif)

Process for using access control with the Access Policy Language| 1 | You write a policy for your resource.<br>For example, you write a policy to specify permissions for your Amazon SNS<br>topics. |
| 2 | You upload your policy to AWS.<br>The AWS service itself provides an API you use to upload your policies. For<br>example, you use the Amazon SNS `SetTopicAttributes` action to upload a policy<br>for a particular Amazon SNS topic. |
| 3 | Someone sends a request to use your resource.<br>For example, a user sends a request to Amazon SNS to use one of your topics. |
| 4 | The AWS service determines which policies are applicable to the<br>request.<br>For example, Amazon SNS looks at all the available Amazon SNS policies and determines<br>which ones are applicable (based on what the resource is, who the requester is,<br>etc.). |
| 5 | The AWS service evaluates the policies.<br>For example, Amazon SNS evaluates the policies and determines if the requester is<br>allowed to use your topic or not. For information about the decision logic, see<br>[Evaluation logic](sns-access-policy-language-evaluation-logic.md "sns-access-policy-language-evaluation-logic.md"). |
| 6 | The AWS service either denies the request or continues to process it.<br>For example, based on the policy evaluation result, the service either returns<br>an "Access denied" error to the requester or continues to process the<br>request. |
