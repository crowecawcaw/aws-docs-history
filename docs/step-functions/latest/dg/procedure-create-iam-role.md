# Creating an IAM role for your state machine in Step Functions

AWS Step Functions can execute code and access AWS resources (such as invoking an AWS Lambda
function). To maintain security, you must grant Step Functions access to those resources by using an
IAM role.

The [Tutorials for learning Step Functions](learning-resources.md#tutorials "learning-resources.md#tutorials") in this guide enable you to take advantage of automatically generated IAM
roles that are valid for the AWS Region in which you create the state machine. However, you can create your own IAM role for a state
machine.

When creating an IAM policy for your state machines to use, the policy should include the permissions that you would like the
state machines to assume. You can use an existing AWS managed policy as an example or you can create a custom policy from
scratch that meets your specific needs. For more information, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the
_IAM User Guide_

To create your own IAM role for a state machine, follow the steps in this section.

In this example, you create an IAM role with permission to invoke a Lambda
function.

## Create a role for Step Functions

1. Sign in to the [IAM
   console](https://console.aws.amazon.com/iam/home "https://console.aws.amazon.com/iam/home"), and then choose **Roles**,
   **Create role**.
2. On the **Select trusted entity** page, under **AWS
   service**, select **Step Functions** from the
   list, and then choose **Next: Permissions**.
3. On the **Attached permissions policy** page, choose
   **Next: Review**.
4. On the **Review** page, enter
   `StepFunctionsLambdaRole` for **Role Name**, and
   then choose **Create role**.

The IAM role appears in the list of roles.

For more information about IAM permissions and policies, see [Access Management](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md")
in the _IAM User Guide_.

## Prevent cross-service confused deputy issue

The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action. In AWS, cross-service impersonation can result in the confused deputy problem. Cross-service impersonation can occur when one service (the _calling
service_) calls another service (the _called service_). This type of
impersonation can happen cross-account and cross-service. The calling service can be manipulated to use
its permissions to act on another customer's resources in a way it should not otherwise have permission to access.

To prevent confused deputies, AWS provides tools that help you protect your data for all services with service principals that
have been given access to resources in your account. This section focuses on cross-service confused deputy prevention specific
to AWS Step Functions; however, you can learn more about this topic in the [confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") section of the
_IAM User Guide_.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource policies to limit the permissions that Step Functions gives another service to access your resources. Use `aws:SourceArn` if you want only one resource to be associated with the cross-service access. Use `aws:SourceAccount` if you want to allow any resource in that account to be associated with the cross-service use.

The most effective way to protect against the confused deputy problem is to use the `aws:SourceArn` global condition
context key with the full ARN of the resource. If you don’t know the full ARN of the resource, or if you're specifying multiple resources, use the
`aws:SourceArn` global context condition key with wildcard characters (`*`) for the unknown portions of the ARN. For
example, `arn:aws:states:*:111122223333:*`.

Here's an example of a _trusted policy_ that shows how you can use `aws:SourceArn` and
`aws:SourceAccount` with Step Functions to prevent the confused deputy issue.

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":[
 "states.amazonaws.com"
 ]
 },
 "Action":"sts:AssumeRole",
 "Condition":{
 "ArnLike":{
 "aws:SourceArn":"arn:aws:states:`us-east-1`:`111122223333`:stateMachine:*"
 },
 "StringEquals":{
 "aws:SourceAccount":"111122223333"
 }
 }
 }
 ]
}`

```

## Attach an Inline Policy

Step Functions can control other services directly in a `Task` state. Attach inline policies
to allow Step Functions to access the API actions of the services you need to control.

1. Open the [IAM console](https://console.aws.amazon.com/iam/home "https://console.aws.amazon.com/iam/home"),
   choose **Roles**, search for your Step Functions role, and select that
   role.
2. Select **Add inline policy**.
3. Use the **Visual editor** or the
   **JSON** tab to create policies for your role.

For more information about how AWS Step Functions can control other AWS services, see
[Integrating services with Step Functions](integrate-services.md "integrate-services.md").

###### Note

For examples of IAM policies created by the Step Functions console, see [How Step Functions generates IAM policies for integrated
services](service-integration-iam-templates.md "service-integration-iam-templates.md").
