# Managing Elastic Beanstalk user policies

AWS Elastic Beanstalk provides two managed policies that enable you to assign full access or read-only access to all resources that Elastic Beanstalk manages. You can attach
the policies to AWS Identity and Access Management (IAM) users or groups, or to roles assumed by your users.

###### Managed user policies

- **AdministratorAccess-AWSElasticBeanstalk** – Gives the user full administrative permissions to create, modify,
  and delete Elastic Beanstalk applications, application versions, configuration settings, environments, and their underlying resources. To view the managed policy
  content, see the [AdministratorAccess-AWSElasticBeanstalk](../../../aws-managed-policy/latest/reference/AdministratorAccess-AWSElasticBeanstalk.md "../../../aws-managed-policy/latest/reference/AdministratorAccess-AWSElasticBeanstalk.md") page in the _AWS Managed Policy Reference Guide_.
- **AWSElasticBeanstalkReadOnly** – Allows the user to view applications and environments, but not to perform
  operations that modify them. It provides read-only access to all Elastic Beanstalk resources, and to other AWS resources that the Elastic Beanstalk console retrieves. Note
  that read-only access does not enable actions such as downloading Elastic Beanstalk logs so that you can read them. This is because the logs are staged in the Amazon S3
  bucket, where Elastic Beanstalk would require write permission. See the example at the end of this topic for information on how to enable access to Elastic Beanstalk logs. To
  view the managed policy content, see the [AWSElasticBeanstalkReadOnly](../../../aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.md "../../../aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.md") page in the _AWS Managed Policy Reference Guide_.

###### Important

Elastic Beanstalk managed policies don't provide granular permissions—they grant all permissions that are potentially needed for working with Elastic Beanstalk
applications. In some cases you may wish to restrict the permissions of our managed policies further. For an example of one use case, see [Preventing cross-environment Amazon S3 bucket access](AWSHowTo.iam.md "AWSHowTo.iam.md").

Our managed policies also don't cover permissions to custom resources that you might add to your solution, and that aren't managed by Elastic Beanstalk. To
implement more granular permissions, minimum required permissions, or custom resource permissions, use [custom
policies](#AWSHowTo.iam.policies "#AWSHowTo.iam.policies").

###### Deprecated managed policies

Previously, Elastic Beanstalk supported two other managed user policies, **AWSElasticBeanstalkFullAccess** and **AWSElasticBeanstalkReadOnlyAccess**. We plan on retiring these previous policies. You might still be able to see and use them in the IAM
console. Nevertheless, we
recommend that you transition to using the new managed user policies, and add custom policies to grant permissions to custom resources, if you have
any.

## Policies for integration with other services

We also provide more granular policies that allow you to integrate your environment with other services, if you prefer to use those.

- AWSElasticBeanstalkRoleCWL – Allows an environment to manage Amazon CloudWatch Logs log groups.
- AWSElasticBeanstalkRoleRDS – Allows an environment to integrate an Amazon RDS instance.
- AWSElasticBeanstalkRoleWorkerTier – Allows a worker environment tier to create an Amazon DynamoDB table and an
  Amazon SQS queue.
- AWSElasticBeanstalkRoleECS – Allows a multicontainer Docker environment to manage Amazon ECS clusters.
- AWSElasticBeanstalkRoleCore – Allows core operations of a web service environment.
- AWSElasticBeanstalkRoleSNS – Allows an environment to enable Amazon SNS topic integration.

To see the JSON source for a specific managed policy, see the [_AWS Managed Policy Reference Guide_](../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md "../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md").

## Controlling access with managed policies

You can use managed policies to grant full access or read-only access to Elastic Beanstalk. Elastic Beanstalk updates these policies automatically when additional permissions
are required to access new features.

###### To apply a managed policy to IAM users or groups

1. Open the [**Policies** page](https://console.aws.amazon.com/iam/home#policies "https://console.aws.amazon.com/iam/home#policies") in the IAM console.
2. In the search box, type `AWSElasticBeanstalk` to filter the policies.
3. In the list of policies, select the check box next to **AWSElasticBeanstalkReadOnly** or
   **AdministratorAccess-AWSElasticBeanstalk**.
4. Choose **Policy actions**, and then choose **Attach**.
5. Select one or more users and groups to attach the policy to. You can use the **Filter** menu and the search box to filter the
   list of principal entities.
6. Choose **Attach policy**.

## Creating a custom user policy

You can create your own IAM policy to allow or deny specific Elastic Beanstalk API actions on specific Elastic Beanstalk resources, and to control access to custom
resources that aren't managed by Elastic Beanstalk. For more information about attaching a policy to a user or group, see [Working with Policies](../../../IAM/latest/UserGuide/ManagingPolicies.md "../../../IAM/latest/UserGuide/ManagingPolicies.md") in the _IAM User Guide_. For details about creating a
custom policy, see [Creating IAM Policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the
_IAM User Guide_.

###### Note

While you can restrict how a user interacts with Elastic Beanstalk APIs, there is not currently an effective way to prevent users who have permission to create
the necessary underlying resources from creating other resources in Amazon EC2 and other services.

Think of these policies as an effective way to distribute Elastic Beanstalk responsibilities, not as a way to secure all underlying resources.

###### Important

If you have custom policies assigned to an Elastic Beanstalk service role, it's important that you assign it the proper permissions for launch templates.
Otherwise you may not have the required permissions to update an environment or launch a new one. For more information, see [Required
permissions for launch templates](environments-cfg-autoscaling-launch-templates.md#environments-cfg-autoscaling-launch-templates-permissions "environments-cfg-autoscaling-launch-templates.md#environments-cfg-autoscaling-launch-templates-permissions").

An IAM policy contains policy statements that describe the permissions that you want to grant. When you create a policy statement for Elastic Beanstalk, you
need to understand how to use the following four parts of a policy statement:

- **Effect** specifies whether to allow or deny the actions in the statement.
- **Action** specifies the [API operations](../api/API_Operations.md "../api/API_Operations.md") that you want to
  control. For example, use `elasticbeanstalk:CreateEnvironment` to specify the `CreateEnvironment` operation. Certain operations,
  such as creating an environment, require additional permissions to perform those actions. For more information, see [Resources and conditions for Elastic Beanstalk actions](AWSHowTo.iam.policies.md "AWSHowTo.iam.policies.md").

###### Note

To use the [`UpdateTagsForResource`](../api/API_UpdateTagsForResource.md "../api/API_UpdateTagsForResource.md") API operation, specify one of the
following two virtual actions (or both) instead of the API operation name:

`elasticbeanstalk:AddTags`

Controls permission to call `UpdateTagsForResource` and pass a list of tags to add in the `TagsToAdd`
parameter.

`elasticbeanstalk:RemoveTags`

Controls permission to call `UpdateTagsForResource` and pass a list of tag keys to remove in the `TagsToRemove`
parameter.

- **Resource** specifies the resources that you want to control access to. To specify Elastic Beanstalk resources, list the [Amazon Resource Name](AWSHowTo.iam.policies.md "AWSHowTo.iam.policies.md") (ARN) of each resource.
- (optional) **Condition** specifies restrictions on the permission granted in the statement. For more information, see
  [Resources and conditions for Elastic Beanstalk actions](AWSHowTo.iam.policies.md "AWSHowTo.iam.policies.md").

The following sections demonstrate a few cases in which you might consider a custom user policy.

### Enabling limited Elastic Beanstalk environment creation

The policy in the following example enables a user to call the `CreateEnvironment` action to create an environment whose name begins with
`Test` with the specified application and application version.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid":"CreateEnvironmentPerm",
 "Action": [
 "elasticbeanstalk:CreateEnvironment"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My First Elastic Beanstalk Application/Test*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My First Elastic Beanstalk Application"],
 "elasticbeanstalk:FromApplicationVersion": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:applicationversion/My First Elastic Beanstalk Application/First Release"]
 }
 }
 },
 {
 "Sid":"AllNonResourceCalls",
 "Action":[
 "elasticbeanstalk:CheckDNSAvailability",
 "elasticbeanstalk:CreateStorageLocation"
 ],
 "Effect":"Allow",
 "Resource":[
 "*"
 ]
 }
 ]
}`

```

The above policy shows how to grant limited access to Elastic Beanstalk operations. In order to actually launch an environment, the user must have permission to
create the AWS resources that power the environment as well. For example, the following policy grants access to the default set of resources for a web
server environment:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:*",
 "ecs:*",
 "elasticloadbalancing:*",
 "autoscaling:*",
 "cloudwatch:*",
 "s3:*",
 "sns:*",
 "cloudformation:*",
 "sqs:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Enabling access to Elastic Beanstalk logs stored in Amazon S3

The policy in the following example enables a user to pull Elastic Beanstalk logs, stage them in Amazon S3, and retrieve them.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:DeleteObject",
 "s3:GetObjectAcl",
 "s3:PutObjectAcl"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:s3:::elasticbeanstalk-*"
 }
 ]
}`

```

###### Note

To restrict these permissions to only the logs path, use the following resource format.

```
"arn:aws:s3:::elasticbeanstalk-`us-east-2`-`123456789012`/resources/environments/logs/*"
```

### Enabling management of a specific Elastic Beanstalk application

The policy in the following example enables a user to manage environments and other resources within one specific Elastic Beanstalk application. The policy
denies Elastic Beanstalk actions on resources of other applications, and also denies creation and deletion of Elastic Beanstalk applications.

###### Note

The policy doesn't deny access to any resources through other services. It demonstrates an effective way to distribute responsibilities for
managing Elastic Beanstalk applications among different users, not as a way to secure the underlying resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "elasticbeanstalk:CreateApplication",
 "elasticbeanstalk:DeleteApplication"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Deny",
 "Action": [
 "elasticbeanstalk:CreateApplicationVersion",
 "elasticbeanstalk:CreateConfigurationTemplate",
 "elasticbeanstalk:CreateEnvironment",
 "elasticbeanstalk:DeleteApplicationVersion",
 "elasticbeanstalk:DeleteConfigurationTemplate",
 "elasticbeanstalk:DeleteEnvironmentConfiguration",
 "elasticbeanstalk:DescribeApplicationVersions",
 "elasticbeanstalk:DescribeConfigurationOptions",
 "elasticbeanstalk:DescribeConfigurationSettings",
 "elasticbeanstalk:DescribeEnvironmentResources",
 "elasticbeanstalk:DescribeEnvironments",
 "elasticbeanstalk:DescribeEvents",
 "elasticbeanstalk:DeleteEnvironmentConfiguration",
 "elasticbeanstalk:RebuildEnvironment",
 "elasticbeanstalk:RequestEnvironmentInfo",
 "elasticbeanstalk:RestartAppServer",
 "elasticbeanstalk:RetrieveEnvironmentInfo",
 "elasticbeanstalk:SwapEnvironmentCNAMEs",
 "elasticbeanstalk:TerminateEnvironment",
 "elasticbeanstalk:UpdateApplicationVersion",
 "elasticbeanstalk:UpdateConfigurationTemplate",
 "elasticbeanstalk:UpdateEnvironment",
 "elasticbeanstalk:RetrieveEnvironmentInfo",
 "elasticbeanstalk:ValidateConfigurationSettings"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringNotEquals": {
 "elasticbeanstalk:InApplication": [
 "arn:aws:elasticbeanstalk:us-east-2:123456789012:application/myapplication"
 ]
 }
 }
 }
 ]
}`

```
