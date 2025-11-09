Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Grant access to project AWS resources with IAM roles

CodeCatalyst can access AWS resources by connecting your AWS account to a CodeCatalyst space.
You can then create the following service roles and associate them when you connect your
account.

For more information about the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

- To access resources in an AWS account for your CodeCatalyst projects and
  workflows, you must first grant permission for CodeCatalyst to access those resources on your
  behalf. To do so, you must create a service role in a connected AWS account that CodeCatalyst
  can assume on behalf of users and projects in the space. You can either choose to
  create and use the **CodeCatalystWorkflowDevelopmentRole-`spaceName`** service role, or you can create customized service roles and
  configure these IAM policies and roles manually. As a best practice, assign these roles
  the least amount of permissions necessary.

###### Note

For customized service roles, the CodeCatalyst service principal is required. For more
information about the CodeCatalyst service principal and trust model, see [Understanding the CodeCatalyst trust model](trust-model.md "trust-model.md").

- To manage support for a space through the connected AWS account, you can choose to
  create and use the **AWSRoleForCodeCatalystSupport** service role that allows CodeCatalyst users to access
  support. For more information about support for a CodeCatalyst space, see [Support for Amazon CodeCatalyst](support.md "support.md").

## Understanding the **CodeCatalystWorkflowDevelopmentRole-`spaceName`** service role

You can add an IAM role for your space that CodeCatalyst can use to create and access
resources in a connected AWS account. This is called a [service
role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role"). The simplest way to create a service role is to add one when you create the
space and to choose the **CodeCatalystWorkflowDevelopmentRole-`spaceName`** option for that role. This not only creates the service
role with the `AdministratorAccess` attached, but it also creates the trust policy
that allows CodeCatalyst to assume the role on behalf of users in projects in the space. The
service role is scoped to the space, not to individual projects. To create this role, see
[Creating the CodeCatalystWorkflowDevelopmentRole-spaceName role for your account
and space](#ipa-iam-roles-service-create "#ipa-iam-roles-service-create").
You can only create one role for each space in each account.

###### Note

This role is only recommended for use with development accounts and uses the
`AdministratorAccess` AWS managed policy, giving it full access to create new
policies and resources in this AWS account.

The policy attached to the **CodeCatalystWorkflowDevelopmentRole-`spaceName`** role is designed to work with projects created with
blueprints in the space. It allows users in those projects to develop, build, test, and
deploy code using resources in the connected AWS account. For more information, see [Creating a
role for an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md").

The policy attached to the **CodeCatalystWorkflowDevelopmentRole-`spaceName`** role is the `AdministratorAccess` managed
policy in AWS. This is a policy that grants full access to all AWS actions and resources.
To view the JSON policy document in the IAM console, see [AdministratorAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AdministratorAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AdministratorAccess").

The following trust policy allows CodeCatalyst to assume the **CodeCatalystWorkflowDevelopmentRole-`spaceName`** role. For more
information about the CodeCatalyst trust model, see [Understanding the CodeCatalyst trust model](trust-model.md "trust-model.md").

```

"Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
             "Principal": {
                "Service": [
                    "codecatalyst-runner.amazonaws.com",
                    "codecatalyst.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:codecatalyst:::space/spaceId/project/*"
                }
            }
        }
    ]

```

## Creating the **CodeCatalystWorkflowDevelopmentRole-`spaceName`** role for your account

and space

Follow these steps to create the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role that will be used for workflows in
your space. For each account that you want to have IAM roles for use in projects, to
your space, you must add a role such as the developer role.

Before you begin, you must have administrative privileges for your AWS account or be
able to work with your administrator. For more information about how AWS accounts and IAM
roles are used in CodeCatalyst, see [Allowing access to AWS resources with connected
AWS accounts](ipa-connect-account.md "ipa-connect-account.md").

###### To create and add the CodeCatalyst **CodeCatalystWorkflowDevelopmentRole-`spaceName`**

1. Before you start in the CodeCatalyst console, open the AWS Management Console, and then make sure you are
   logged in with the same AWS account for your space.
2. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
3. Navigate to your CodeCatalyst space. Choose **Settings**, and then choose
   **AWS accounts**.
4. Choose the link for the AWS account where you want to create the role. The
   **AWS account details** page displays.
5. Choose **Manage roles from AWS Management Console**.

The **Add IAM role to Amazon CodeCatalyst space** page opens in the
AWS Management Console. This is the **Amazon CodeCatalyst spaces** page. You might need to log in
to access the page. 6. Choose **Create CodeCatalyst development administrator role in IAM**. This
option creates a service role that contains the permissions policy and trust policy for the
development role. The role will have a name `CodeCatalystWorkflowDevelopmentRole-`spaceName``. For more information about the
role and role policy, see [Understanding the CodeCatalystWorkflowDevelopmentRole-spaceName service role](#ipa-iam-roles-service-role "#ipa-iam-roles-service-role").

###### Note

This role is only recommended for use with developer accounts and uses the
`AdministratorAccess` AWS managed policy, giving it full access to create new
policies and resources in this AWS account. 7. Choose **Create development role**. 8. On the connections page, under **IAM roles available to CodeCatalyst**, view
the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role in the list of IAM roles added to your account. 9. To return to your space, choose **Go to Amazon CodeCatalyst**.

## Understanding the **AWSRoleForCodeCatalystSupport** service

role

You can add an IAM role for your space that CodeCatalyst users in a space can use to
create and access support cases. This is called a [service
role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") for support.The simplest way to create a service role for support is to add one
when you create the space and to choose the `AWSRoleForCodeCatalystSupport` option for that
role. This not only creates the policy and the role, but it also creates the trust policy that
allows CodeCatalyst to assume the role on behalf of users in projects in the space. The service
role is scoped to the space, not to individual projects. To create this role, see [Creating the AWSRoleForCodeCatalystSupport role for your
account and space](#ipa-iam-roles-support-create "#ipa-iam-roles-support-create").

The policy attached to the `AWSRoleForCodeCatalystSupport` role is managed policy that provides
access to support permissions. For more information, see [AWS managed policy: AmazonCodeCatalystSupportAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonCodeCatalystSupportAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonCodeCatalystSupportAccess").

The trust role for the policy allows CodeCatalyst to assume the role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "codecatalyst.amazonaws.com",
 "codecatalyst-runner.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

## Creating the **AWSRoleForCodeCatalystSupport** role for your

account and space

Follow these steps to create the `AWSRoleForCodeCatalystSupport` role that will be used for
support cases in your space. The role must be added to the designated billing account for
the space.

Before you begin, you must have administrative privileges for your AWS account or be
able to work with your administrator. For more information about how AWS accounts and IAM
roles are used in CodeCatalyst, see [Allowing access to AWS resources with connected
AWS accounts](ipa-connect-account.md "ipa-connect-account.md").

###### To create and add the CodeCatalyst **AWSRoleForCodeCatalystSupport**

1. Before you start in the CodeCatalyst console, open the AWS Management Console, and then make sure you are
   logged in with the same AWS account for your space.
2. Navigate to your CodeCatalyst space. Choose **Settings**, and then choose
   **AWS accounts**.
3. Choose the link for the AWS account where you want to create the role. The
   **AWS account details** page displays.
4. Choose **Manage roles from AWS Management Console**.

The **Add IAM role to Amazon CodeCatalyst space** page opens in the
AWS Management Console. This is the **Amazon CodeCatalyst Spaces** page. You might need to sign in
to access the page. 5. Under **CodeCatalyst space details**, choose **Add CodeCatalyst Support
role**. This option creates a service role that contains the permissions policy and
trust policy for the preview development role. The role will have a name **AWSRoleForCodeCatalystSupport**
with a unique identifier appended. For more information about the role and role policy, see
[Understanding the AWSRoleForCodeCatalystSupport service
role](#ipa-iam-roles-support-role "#ipa-iam-roles-support-role"). 6. On the **Add role for CodeCatalyst Support** page, leave the default selected,
and then choose **Create role**. 7. Under **IAM roles available to CodeCatalyst**, view the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role
in the list of IAM roles added to your account. 8. To return to your space, choose **Go to Amazon CodeCatalyst**.

## Configuring IAM roles for workflow actions in

CodeCatalyst

This section details IAM roles and policies that you can create to use with your CodeCatalyst
account. For instructions to create example roles, see [Creating roles manually for workflow actions](#ipa-iam-roles-actions "#ipa-iam-roles-actions"). After you create your IAM role, copy the role ARN
to add the IAM role to your account connection and associate it with your project
environment. To learn more, see [Adding IAM roles to account
connections](ipa-connect-account-addroles.md "ipa-connect-account-addroles.md").

### CodeCatalyst build role for Amazon S3 access

For CodeCatalyst workflow build actions, you can use the default **CodeCatalystWorkflowDevelopmentRole-`spaceName`** service role, or
you can create an IAM role named **CodeCatalystBuildRoleforS3Access**. This role uses a policy with scoped permissions
that CodeCatalyst needs to run tasks on AWS CloudFormation resources in your AWS account.

This role gives permissions to do the following:

- Write to Amazon S3 buckets.
- Support building of resources with AWS CloudFormation. This requires Amazon S3 access.

This role uses the following policy:

###### Note

The first time the role is used to run workflow actions, use the wildcard in the
resource policy statement and then scope down the policy with the resource name after it
is available.

```
"Resource": "*"
```

### CodeCatalyst build role for

AWS CloudFormation

For CodeCatalyst workflow build actions, you can use the default **CodeCatalystWorkflowDevelopmentRole-`spaceName`** service role, or
you can create an IAM role with the necessary permissions. This role uses a policy with
scoped permissions that CodeCatalyst needs to run tasks on AWS CloudFormation resources in your AWS account.

This role gives permissions to do the following:

- Support building of resources with AWS CloudFormation. This is required along with the CodeCatalyst
  build role for Amazon S3 access and the CodeCatalyst deploy role for AWS CloudFormation.

The following AWS managed policies should be attached to this role:

- **AWSCloudFormationFullAccess**
- **IAMFullAccess**
- **AmazonS3FullAccess**
- **AmazonAPIGatewayAdministrator**
- **AWSLambdaFullAccess**

### CodeCatalyst build role for CDK

For CodeCatalyst workflows that run CDK build actions, such as Modern three-tier web application, you can
use the default **CodeCatalystWorkflowDevelopmentRole-`spaceName`** service role, or you can create an IAM role with the necessary
permissions. This role uses a policy with scoped permissions that CodeCatalyst needs to bootstrap
and run CDK build commands for AWS CloudFormation resources in your AWS account.

This role gives permissions to do the following:

- Write to Amazon S3 buckets.
- Support building of CDK constructs and AWS CloudFormation resource stacks. This requires access
  to Amazon S3 for artifact storage, Amazon ECR for image repository support, and SSM for system
  governance and monitoring for virtual instances.

This role uses the following policy:

###### Note

The first time the role is used to run workflow actions, use the wildcard in the
resource policy statement and then scope down the policy with the resource name after it
is available.

```
"Resource": "*"
```

### CodeCatalyst deploy role for

AWS CloudFormation

For CodeCatalyst workflow deploy actions that use AWS CloudFormation, you can use the default **CodeCatalystWorkflowDevelopmentRole-`spaceName`**
service role, or you can use a policy with scoped permissions that CodeCatalyst needs to run tasks
on AWS CloudFormation resources in your AWS account.

This role gives permissions to do the following:

- Allow CodeCatalyst to invoke a Λ function to perform blue/green deployment through
  AWS CloudFormation.
- Allow CodeCatalyst to create and update stacks and changesets in AWS CloudFormation.

This role uses the following policy:

```
{"Action": [
        "cloudformation:CreateStack",
        "cloudformation:DeleteStack",
        "cloudformation:Describe*",
        "cloudformation:UpdateStack",
        "cloudformation:CreateChangeSet",
        "cloudformation:DeleteChangeSet",
        "cloudformation:ExecuteChangeSet",
        "cloudformation:SetStackPolicy",
        "cloudformation:ValidateTemplate",
        "cloudformation:List*",
        "iam:PassRole"
    ],
    "Resource": "`resource_ARN`",
    "Effect": "Allow"
}
```

###### Note

The first time the role is used to run workflow actions, use the wildcard in the
resource policy statement and then scope down the policy with the resource name after it
is available.

```
"Resource": "*"
```

### CodeCatalyst deploy role for Amazon EC2

CodeCatalyst workflow deploy actions use an IAM role with the necessary permissions. This
role uses a policy with scoped permissions that CodeCatalyst needs to run tasks on Amazon EC2 resources
in your AWS account. The default policy for the **CodeCatalystWorkflowDevelopmentRole-`spaceName`** role does not
include permissions for Amazon EC2 or Amazon EC2 Auto Scaling.

This role gives permissions to do the following:

- Create Amazon EC2 deployments.
- Read the tags on an instance or identify an Amazon EC2 instance by Auto Scaling group
  names.
- Read, create, update, and delete Amazon EC2 Auto Scaling groups, lifecycle hooks, and
  scaling policies.
- Publish information to Amazon SNS topics.
- Retrieve information about CloudWatch alarms.
- Read and update Elastic Load Balancing.

This role uses the following policy:

###### Note

The first time the role is used to run workflow actions, use the wildcard in the
resource policy statement and then scope down the policy with the resource name after it
is available.

```
"Resource": "*"
```

### CodeCatalyst deploy role for Amazon ECS

For CodeCatalyst workflow actions, you can create an IAM role with the necessary
permissions. You can use the default **CodeCatalystWorkflowDevelopmentRole-`spaceName`** service role, or you can create an IAM role
for CodeCatalyst deploy actions to use for Lambda deployments. This role uses a policy with scoped
permissions that CodeCatalyst needs to run tasks on Amazon ECS resources in your AWS account.

This role gives permissions to do the following:

- Initiate rolling Amazon ECS deployment on behalf of a CodeCatalyst user, in an account
  specified in the CodeCatalyst connection.
- Read, update, and delete Amazon ECS task sets.
- Update Elastic Load Balancing target groups, listeners, and rules.
- Invoke Lambda functions.
- Access revision files in Amazon S3 buckets.
- Retrieve information about CloudWatch alarms.
- Publish information to Amazon SNS topics.

This role uses the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Action":[
 "ecs:DescribeServices",
 "ecs:CreateTaskSet",
 "ecs:DeleteTaskSet",
 "ecs:ListClusters",
 "ecs:RegisterTaskDefinition",
 "ecs:UpdateServicePrimaryTaskSet",
 "ecs:UpdateService",
 "elasticloadbalancing:DescribeTargetGroups",
 "elasticloadbalancing:DescribeListeners",
 "elasticloadbalancing:ModifyListener",
 "elasticloadbalancing:DescribeRules",
 "elasticloadbalancing:ModifyRule",
 "lambda:InvokeFunction",
 "lambda:ListFunctions",
 "cloudwatch:DescribeAlarms",
 "sns:Publish",
 "sns:ListTopics",
 "s3:GetObject",
 "s3:GetObjectVersion",
 "codedeploy:CreateApplication",
 "codedeploy:CreateDeployment",
 "codedeploy:CreateDeploymentGroup",
 "codedeploy:GetApplication",
 "codedeploy:GetDeployment",
 "codedeploy:GetDeploymentGroup",
 "codedeploy:ListApplications",
 "codedeploy:ListDeploymentGroups",
 "codedeploy:ListDeployments",
 "codedeploy:StopDeployment",
 "codedeploy:GetDeploymentTarget",
 "codedeploy:ListDeploymentTargets",
 "codedeploy:GetDeploymentConfig",
 "codedeploy:GetApplicationRevision",
 "codedeploy:RegisterApplicationRevision",
 "codedeploy:BatchGetApplicationRevisions",
 "codedeploy:BatchGetDeploymentGroups",
 "codedeploy:BatchGetDeployments",
 "codedeploy:BatchGetApplications",
 "codedeploy:ListApplicationRevisions",
 "codedeploy:ListDeploymentConfigs",
 "codedeploy:ContinueDeployment"
 ],
 "Resource":"*",
 "Effect":"Allow"
},{"Action":[
 "iam:PassRole"
 ],
 "Effect":"Allow",
 "Resource":"*",
 "Condition":{"StringLike":{"iam:PassedToService":[
 "ecs-tasks.amazonaws.com",
 "codedeploy.amazonaws.com"
 ]
 }
 }
}]
}`

```

###### Note

The first time the role is used to run workflow actions, use the wildcard in the
resource policy statement and then scope down the policy with the resource name after it
is available.

```
"Resource": "*"
```

### CodeCatalyst deploy role for Lambda

For CodeCatalyst workflow actions, you can create an IAM role with the necessary permissions.
You can use the default **CodeCatalystWorkflowDevelopmentRole-`spaceName`** service role, or or you create an IAM role for CodeCatalyst
deploy actions to use for Lambda deployments. This role uses a policy with scoped permissions
that CodeCatalyst needs to run tasks on Lambda resources in your AWS account.

This role gives permissions to do the following:

- Read, update, and invoke Lambda functions and aliases.
- Access revision files in Amazon S3 buckets.
- Retrieve information about CloudWatch Events alarms.
- Publish information to Amazon SNS topics.

This role uses the following policy:

###### Note

The first time the role is used to run workflow actions, use the wildcard in the
resource policy statement and then scope down the policy with the resource name after it
is available.

```
"Resource": "*"
```

### CodeCatalyst deploy role for Lambda

For CodeCatalyst workflow actions, you can use the default **CodeCatalystWorkflowDevelopmentRole-`spaceName`** service role, or you can
create an IAM role with the necessary permissions. This role uses a policy with scoped
permissions that CodeCatalyst needs to run tasks on Lambda resources in your AWS account.

This role gives permissions to do the following:

- Read, update, and invoke Lambda functions and aliases.
- Access revision files in Amazon S3 buckets.
- Retrieve information about CloudWatch alarms.
- Publish information to Amazon SNS topics.

This role uses the following policy:

###### Note

The first time the role is used to run workflow actions, use the wildcard in the
resource policy statement and then scope down the policy with the resource name after it
is available.

```
"Resource": "*"
```

### CodeCatalyst deploy role for AWS SAM

For CodeCatalyst workflow actions, you can use the default **CodeCatalystWorkflowDevelopmentRole-`spaceName`** service role, or you can
create an IAM role with the necessary permissions. This role uses a policy with scoped
permissions that CodeCatalyst needs to run tasks on AWS SAM and AWS CloudFormation resources in your AWS account.

This role gives permissions to do the following:

- Allow CodeCatalyst to invoke a Lambda function to perform deployment of serverless and
  AWS SAM CLI applications.
- Allow CodeCatalyst to create and update stacks and changesets in AWS CloudFormation.

This role uses the following policy:

###### Note

The first time the role is used to run workflow actions, use the wildcard in the
resource policy statement and then scope down the policy with the resource name after it
is available.

```
"Resource": "*"
```

### CodeCatalyst read only role for Amazon EC2

For CodeCatalyst workflow actions, you can create an IAM role with the necessary
permissions. This role uses a policy with scoped permissions that CodeCatalyst needs to run tasks
on Amazon EC2 resources in your AWS account. The **CodeCatalystWorkflowDevelopmentRole-`spaceName`** service role does not
include permissions for Amazon EC2 or the described actions for Amazon CloudWatch.

This role gives permissions to do the following:

- Get status of Amazon EC2 instances.
- Get CloudWatch metrics for Amazon EC2 instances.

This role uses the following policy:

###### Note

The first time the role is used to run workflow actions, use the wildcard in the
resource policy statement and then scope down the policy with the resource name after it
is available.

```
"Resource": "*"
```

### CodeCatalyst read only role for Amazon ECS

For CodeCatalyst workflow actions, you can create an IAM role with the necessary
permissions. This role uses a policy with scoped permissions that CodeCatalyst needs to run tasks
on Amazon ECS resources in your AWS account.

This role gives permissions to do the following:

- Read Amazon ECS task sets.
- Retrieve information about CloudWatch alarms.

This role uses the following policy:

###### Note

The first time the role is used to run workflow actions, use the wildcard in the
resource policy statement and then scope down the policy with the resource name after it
is available.

```
"Resource": "*"
```

### CodeCatalyst read only role for Lambda

For CodeCatalyst workflow actions, you can create an IAM role with the necessary
permissions. This role uses a policy with scoped permissions that CodeCatalyst needs to run tasks
on Lambda resources in your AWS account.

This role gives permissions for the following:

- Read Lambda functions and aliases.
- Access revision files in Amazon S3 buckets.
- Retrieve information about CloudWatch alarms.

This role uses the following policy.

###### Note

The first time the role is used to run workflow actions, use the wildcard in the
resource policy statement and then scope down the policy with the resource name after it
is available.

```
"Resource": "*"
```

## Creating roles manually for workflow actions

CodeCatalyst workflow actions use IAM roles that you create called the **build role**, the **deploy role**, and the **stack role**.

Follow these steps to create these roles in IAM.

###### To create a deploy role

1. Create a policy for the role, as follows:
   1. Sign in to AWS.
   2. Open the IAM console at
      [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   3. In the navigation pane, choose **Policies**.
   4. Choose **Create policy**.
   5. Choose the **JSON** tab.
   6. Delete the existing code.
   7. Paste the following code:

   ###### Note

   The first time the role is used to run workflow actions, use the wildcard
   in the resource policy statement and then scope down the policy with the
   resource name after it is available.

   ```
   "Resource": "*"
   ```

   8. Choose **Next: Tags**.
   9. Choose **Next: Review**.
   10. In **Name**, enter:

   ```
   `codecatalyst-deploy-policy`
   ```

   11. Choose **Create policy**.

   You have now created a permissions policy.

2. Create the deploy role, as follows:
   1. In the navigation pane, choose **Roles**, and then choose
      **Create role**.
   2. Choose **Custom trust policy**.
   3. Delete the existing custom trust policy.
   4. Add the following custom trust policy:
   5. Choose **Next**.
   6. In **Permissions policies**, search for `codecatalyst-deploy-policy` and select its check box.
   7. Choose **Next**.
   8. For **Role name**, enter:

   ```
   `codecatalyst-deploy-role`
   ```

   9. For **Role description**, enter:

   ```
   `CodeCatalyst deploy role`
   ```

   10. Choose **Create role**.You have now created a deploy role with a trust policy and permissions policy.

3. Obtain the deploy role ARN, as follows:
   1. In the navigation pane, choose **Roles**.
   2. In the search box, enter the name of the role you just created
      (`codecatalyst-deploy-role`).
   3. Choose the role from the list.

   The role's **Summary** page appears. 4. At the top, copy the **ARN** value.You have now created the deploy role with the appropriate permissions, and obtained
   its ARN.

###### To create a build role

1. Create a policy for the role, as follows:
   1. Sign in to AWS.
   2. Open the IAM console at
      [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   3. In the navigation pane, choose **Policies**.
   4. Choose **Create policy**.
   5. Choose the **JSON** tab.
   6. Delete the existing code.
   7. Paste the following code:

   ###### Note

   The first time the role is used to run workflow actions, use the wildcard
   in the resource policy statement and then scope down the policy with the
   resource name after it is available.

   ```
   "Resource": "*"
   ```

   8. Choose **Next: Tags**.
   9. Choose **Next: Review**.
   10. In **Name**, enter:

   ```
   `codecatalyst-build-policy`
   ```

   11. Choose **Create policy**.

   You have now created a permissions policy.

2. Create the build role, as follows:
   1. In the navigation pane, choose **Roles**, and then choose
      **Create role**.
   2. Choose **Custom trust policy**.
   3. Delete the existing custom trust policy.
   4. Add the following custom trust policy:
   5. Choose **Next**.
   6. In **Permissions policies**, search for
      `codecatalyst-build-policy` and select its check box.
   7. Choose **Next**.
   8. For **Role name**, enter:

   ```
   `codecatalyst-build-role`
   ```

   9. For **Role description**, enter:

   ```
   `CodeCatalyst build role`
   ```

   10. Choose **Create role**.You have now created a build role with a trust policy and permissions policy.

3. Obtain the build role ARN, as follows:
   1. In the navigation pane, choose **Roles**.
   2. In the search box, enter the name of the role you just created
      (`codecatalyst-build-role`).
   3. Choose the role from the list.

   The role's **Summary** page appears. 4. At the top, copy the **ARN** value.You have now created the build role with the appropriate permissions, and obtained its
   ARN.

###### To create a stack role

###### Note

You don't have to create a stack role, although doing so is recommended for security
reasons. If you don't create the stack role, you'll need to add the permissions policies
described further on in this procedure to the deploy role.

1. Sign in to AWS using the account where you want to deploy your stack.
2. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
3. In the navigation pane, choose **Roles**. and then choose
   **Create role**.
4. At the top, choose **AWS service**.
5. From the list of services, choose **CloudFormation**.
6. Choose **Next: Permissions**.
7. In the search box, add any policies that are required to access the resources in your
   stack. For example, if your stack includes an AWS Lambda function, you need to add a
   policy that grants access to Lambda.

###### Tip

If you're unsure which policies to add, you can omit them for now. When you test
the action, if you don't have the right permissions, AWS CloudFormation generates errors that
show which permissions you need to add. 8. Choose **Next: Tags**. 9. Choose **Next: Review**. 10. For **Role name**, enter:

```
`codecatalyst-stack-role`
```

11. Choose **Create role**.
12. To obtain the stack role's ARN, do the following:
    1.  In the navigation pane, choose **Roles**.
    2.  In the search box, enter the name of the role you just created
        (`codecatalyst-stack-role`).
    3.  Choose the role from the list.
    4.  On the **Summary** page, copy the **Role
        ARN** value.

## Using AWS CloudFormation to create policies and roles in

IAM

You can choose to create and use AWS CloudFormation templates to create the policies and roles you
need to access resources in an AWS account for your CodeCatalyst projects and
workflows. AWS CloudFormation is a service that helps you model and set up your AWS resources so that you
can spend less time managing those resources and more time focusing on your applications that
run on AWS. If you intend to create roles in multiple AWS accounts, creating
a template can help you perform this task more quickly.

The following example template creates a deploy action role and policy.

```
Parameters:
  CodeCatalystAccountId:
    Type: String
    Description: Account ID from the connections page
  ExternalId:
    Type: String
    Description: External ID from the connections page
Resources:
  CrossAccountRole:
    Type: 'AWS::IAM::Role'
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              AWS:
                - !Ref CodeCatalystAccountId
            Action:
              - 'sts:AssumeRole'
            Condition:
              StringEquals:
                sts:ExternalId: !Ref ExternalId
      Path: /
      Policies:
        - PolicyName: CodeCatalyst-CloudFormation-action-policy
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Action:
                  - 'cloudformation:CreateStack'
                  - 'cloudformation:DeleteStack'
                  - 'cloudformation:Describe*'
                  - 'cloudformation:UpdateStack'
                  - 'cloudformation:CreateChangeSet'
                  - 'cloudformation:DeleteChangeSet'
                  - 'cloudformation:ExecuteChangeSet'
                  - 'cloudformation:SetStackPolicy'
                  - 'cloudformation:ValidateTemplate'
                  - 'cloudformation:List*'
                  - 'iam:PassRole'
                Resource: '*'
```

## Creating the role manually for the web

application blueprint

The CodeCatalyst web application blueprint uses IAM roles that you create called the **build role for CDK**, the **deploy role**,
and the **stack role**.

Follow these steps to create the role in IAM.

###### To create a build role

1. Create a policy for the role, as follows:
   1. Sign in to AWS.
   2. Open the IAM console at
      [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   3. In the navigation pane, choose **Policies**.
   4. Choose **Create Policy**.
   5. Choose the **JSON** tab.
   6. Delete the existing code.
   7. Paste the following code:

   ###### Note

   The first time the role is used to run workflow actions, use the wildcard in the
   resource policy statement and then scope down the policy with the resource name
   after it is available.

   ```
   "Resource": "*"
   ```

   8. Choose **Next: Tags**.
   9. Choose **Next: Review**.
   10. In **Name**, enter:

   ```
   `codecatalyst-webapp-build-policy`
   ```

   11. Choose **Create policy**.

   You have now created a permissions policy.

2. Create the build role, as follows:
   1. In the navigation pane, choose **Roles**, and then choose
      **Create role**.
   2. Choose **Custom trust policy**.
   3. Delete the existing custom trust policy.
   4. Add the following custom trust policy:
   5. Choose **Next**.
   6. Attach the permissions policy to the build role. On the **Add
      permissions** page, in the **Permissions policies**
      section, search for
      `codecatalyst-webapp-build-policy` and
      select its check box.
   7. Choose **Next**.
   8. For **Role name**, enter:

   ```
   `codecatalyst-webapp-build-role`
   ```

   9. For **Role description**, enter:

   ```
   `CodeCatalyst Web app build role`
   ```

   10. Choose **Create role**.You have now created a build role with a trust policy and permissions policy.

3. Attach the permissions policy to the build role, as follows:
   1. In the navigation pane, choose **Roles**, and then search for
      `codecatalyst-webapp-build-role`.
   2. Choose `codecatalyst-webapp-build-role`
      to display its details.
   3. In the **Permissions** tab, choose **Add
      permissions**, and then choose **Attach policies**.
   4. Search for
      `codecatalyst-webapp-build-policy`,
      select its check box, and then choose **Attach policies**.

   You have now attached the permissions policy to the build role. The build role now
   has two policies: a permissions policy and a trust policy.

4. Obtain the build role ARN, as follows:
   1. In the navigation pane, choose **Roles**.
   2. In the search box, enter the name of the role you just created
      (`codecatalyst-webapp-build-role`).
   3. Choose the role from the list.

   The role's **Summary** page appears. 4. At the top, copy the **ARN** value.You have now created the build role with the appropriate permissions, and obtained its
   ARN.

## Creating roles manually for the SAM

blueprint

The CodeCatalyst SAM blueprint uses IAM roles that you create called the **build role for CloudFormation** and the **deploy role for
SAM**.

Follow these steps to create the roles in IAM.

###### To create a build role for CloudFormation

1. Create a policy for the role, as follows:
   1. Sign in to AWS.
   2. Open the IAM console at
      [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   3. In the navigation pane, choose **Policies**.
   4. Choose **Create Policy**.
   5. Choose the **JSON** tab.
   6. Delete the existing code.
   7. Paste the following code:

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "s3:*",
    "cloudformation:*"
    ],
    "Resource": "*"
    }
    ]
   }`

   ```

   ###### Note

   The first time the role is used to run workflow actions, use the wildcard in the
   resource policy statement and then scope down the policy with the resource name
   after it is available.

   ```
   "Resource": "*"
   ```

   8. Choose **Next: Tags**.
   9. Choose **Next: Review**.
   10. In **Name**, enter:

   ```
   `codecatalyst-SAM-build-policy`
   ```

   11. Choose **Create policy**.

   You have now created a permissions policy.

2. Create the build role, as follows:
   1. In the navigation pane, choose **Roles**, and then choose
      **Create role**.
   2. Choose **Custom trust policy**.
   3. Delete the existing custom trust policy.
   4. Add the following custom trust policy:
   5. Choose **Next**.
   6. Attach the permissions policy to the build role. On the **Add
      permissions** page, in the **Permissions policies**
      section, search for
      `codecatalyst-SAM-build-policy` and
      select its check box.
   7. Choose **Next**.
   8. For **Role name**, enter:

   ```
   `codecatalyst-SAM-build-role`
   ```

   9. For **Role description**, enter:

   ```
   `CodeCatalyst SAM build role`
   ```

   10. Choose **Create role**.You have now created a build role with a trust policy and permissions policy.

3. Attach the permissions policy to the build role, as follows:
   1. In the navigation pane, choose **Roles**, and then search for
      `codecatalyst-SAM-build-role`.
   2. Choose `codecatalyst-SAM-build-role` to
      display its details.
   3. In the **Permissions** tab, choose **Add
      permissions**, and then choose **Attach policies**.
   4. Search for
      `codecatalyst-SAM-build-policy`, select
      its check box, and then choose **Attach policies**.

   You have now attached the permissions policy to the build role. The build role now
   has two policies: a permissions policy and a trust policy.

4. Obtain the build role ARN, as follows:
   1. In the navigation pane, choose **Roles**.
   2. In the search box, enter the name of the role you just created
      (`codecatalyst-SAM-build-role`).
   3. Choose the role from the list.

   The role's **Summary** page appears. 4. At the top, copy the **ARN** value.You have now created the build role with the appropriate permissions, and obtained its
   ARN.

###### To create a deploy role for SAM

1. Create a policy for the role, as follows:
   1. Sign in to AWS.
   2. Open the IAM console at
      [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   3. In the navigation pane, choose **Policies**.
   4. Choose **Create Policy**.
   5. Choose the **JSON** tab.
   6. Delete the existing code.
   7. Paste the following code:

   ###### Note

   The first time the role is used to run workflow actions, use the wildcard in the
   resource policy statement and then scope down the policy with the resource name
   after it is available.

   ```
   "Resource": "*"
   ```

   8. Choose **Next: Tags**.
   9. Choose **Next: Review**.
   10. In **Name**, enter:

   ```
   `codecatalyst-SAM-deploy-policy`
   ```

   11. Choose **Create policy**.

   You have now created a permissions policy.

2. Create the build role, as follows:
   1. In the navigation pane, choose **Roles**, and then choose
      **Create role**.
   2. Choose **Custom trust policy**.
   3. Delete the existing custom trust policy.
   4. Add the following custom trust policy:
   5. Choose **Next**.
   6. Attach the permissions policy to the build role. On the **Add
      permissions** page, in the **Permissions policies**
      section, search for
      `codecatalyst-SAM-deploy-policy` and
      select its check box.
   7. Choose **Next**.
   8. For **Role name**, enter:

   ```
   `codecatalyst-SAM-deploy-role`
   ```

   9. For **Role description**, enter:

   ```
   `CodeCatalyst SAM deploy role`
   ```

   10. Choose **Create role**.You have now created a build role with a trust policy and permissions policy.

3. Attach the permissions policy to the build role, as follows:
   1. In the navigation pane, choose **Roles**, and then search for
      `codecatalyst-SAM-deploy-role`.
   2. Choose `codecatalyst-SAM-deploy-role`
      to display its details.
   3. In the **Permissions** tab, choose **Add
      permissions**, and then choose **Attach policies**.
   4. Search for
      `codecatalyst-SAM-deploy-policy`,
      select its check box, and then choose **Attach policies**.

   You have now attached the permissions policy to the build role. The build role now
   has two policies: a permissions policy and a trust policy.

4. Obtain the build role ARN, as follows:
   1. In the navigation pane, choose **Roles**.
   2. In the search box, enter the name of the role you just created
      (`codecatalyst-SAM-deploy-role`).
   3. Choose the role from the list.

   The role's **Summary** page appears. 4. At the top, copy the **ARN** value.You have now created the build role with the appropriate permissions, and obtained its
   ARN.
