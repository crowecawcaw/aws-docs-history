# Managing Elastic Beanstalk service roles

To manage and monitor your environment, AWS Elastic Beanstalk performs actions on environment resources on your behalf. Elastic Beanstalk needs certain permissions to perform
these actions, and it assumes AWS Identity and Access Management (IAM) service roles to get these permissions.

Elastic Beanstalk needs to use temporary security credentials whenever it assumes a service role. To get these credentials, Elastic Beanstalk sends a request to AWS Security Token Service
(AWS STS) on a Region specific endpoint. For more information, see [Temporary Security Credentials](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md")
in the _IAM User Guide_.

###### Note

If the AWS STS endpoint for the Region where your environment is located is deactivated, Elastic Beanstalk sends the request on an alternative endpoint that can't
be deactivated. This endpoint is associated with a different Region. Therefore, the request is a cross-Region request. For more information, see [Activating and Deactivating AWS STS in an AWS Region](../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md "../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md") in the
_IAM User Guide_.

## Managing service roles using the Elastic Beanstalk console and EB CLI

You can use the Elastic Beanstalk console and EB CLI to set up service roles for your environment with a sufficient set of permissions. They create a default
service role and use managed policies in it.

### Managed service role policies

Elastic Beanstalk provides one managed policy for [enhanced health monitoring](health-enhanced.md "health-enhanced.md"), and another one with additional permissions
required for [managed platform updates](environment-platform-update-managed.md "environment-platform-update-managed.md"). The console and EB CLI assign both of these policies
to the default service role that they create for you. These policies should only be used for this default service role. They should not be used with
other users or roles in your accounts.

#### `AWSElasticBeanstalkEnhancedHealth`

This policy grants permissions for Elastic Beanstalk to monitor instance and environment health. It also includes Amazon SQS actions to allow Elastic Beanstalk to monitor queue
activity for worker environments. To view the content of this managed policy, see the [AWSElasticBeanstalkEnhancedHealth](../../../aws-managed-policy/latest/reference/AWSElasticBeanstalkEnhancedHealth.md "../../../aws-managed-policy/latest/reference/AWSElasticBeanstalkEnhancedHealth.md") page in the _AWS Managed
Policy Reference Guide_.

#### `AWSElasticBeanstalkManagedUpdatesCustomerRolePolicy`

This policy grants permissions for Elastic Beanstalk to update environments on your behalf to perform managed platform updates.
To view the content of this managed
policy, see the [AWSElasticBeanstalkManagedUpdatesCustomerRolePolicy](../../../aws-managed-policy/latest/reference/AWSElasticBeanstalkManagedUpdatesCustomerRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSElasticBeanstalkManagedUpdatesCustomerRolePolicy.md") page in the _AWS Managed Policy Reference Guide_.

**Service-level permission groupings**

This policy is grouped into statements based on the set of permissions provided.

- _`ElasticBeanstalkPermissions`_ – This group of permissions is for calling the Elastic Beanstalk service actions (Elastic Beanstalk
  APIs).
- _`AllowPassRoleToElasticBeanstalkAndDownstreamServices`_ – This group of permissions allows any role to be
  passed to Elastic Beanstalk and to other downstream services like CloudFormation.
- _`ReadOnlyPermissions`_ – This group of permissions is for collecting information about the running
  environment.
- *`*OperationPermissions`\* – Groups with this naming pattern are for calling the necessary operations to perform
  platform updates.
- *`*BroadOperationPermissions`\* – Groups with this naming pattern are for calling the necessary operations to
  perform platform updates. They also include broad permissions for supporting legacy environments.
- *`*TagResource`\* – Groups with this naming pattern are for calls that use the tag-on-create APIs to attach tags
  on resources that are being created in an Elastic Beanstalk environment.

To view the content of a managed policy, you can also use the [**Policies**
page](https://console.aws.amazon.com/iam/home#policies "https://console.aws.amazon.com/iam/home#policies") in the IAM console.

###### Important

Elastic Beanstalk managed policies don't provide granular permissions—they grant all permissions that are potentially needed for working with Elastic Beanstalk
applications. In some cases you may wish to restrict the permissions of our managed policies further. For an example of one use case, see [Preventing cross-environment Amazon S3 bucket access](AWSHowTo.iam.md "AWSHowTo.iam.md").

Our managed policies also don't cover permissions to custom resources that you might add to your solution, and that aren't managed by Elastic Beanstalk. To
implement more granular permissions, minimum required permissions, or custom resource permissions, use [custom
policies](AWSHowTo.iam.md#AWSHowTo.iam.policies "AWSHowTo.iam.md#AWSHowTo.iam.policies").

###### Deprecated managed policies

In the past, Elastic Beanstalk supported the **AWSElasticBeanstalkService** managed service role policy. This policy has been
replaced by **AWSElasticBeanstalkManagedUpdatesCustomerRolePolicy**. You might still be able to see and use the earlier policy in the IAM
console.

To view the managed policy content, see [AWSElasticBeanstalkService](../../../aws-managed-policy/latest/reference/AWSElasticBeanstalkService.md "../../../aws-managed-policy/latest/reference/AWSElasticBeanstalkService.md") in the _AWS Managed Policy Reference Guide_.

However, we recommend that you transition to using the new managed policy (**AWSElasticBeanstalkManagedUpdatesCustomerRolePolicy**). Add
custom policies to grant permissions to custom resources, if you have any.

### Using the Elastic Beanstalk console

When you launch an environment in the Elastic Beanstalk console, the console creates a default service role that's named
`aws-elasticbeanstalk-service-role`, and attaches managed policies with default permissions to this service role.

To allow Elastic Beanstalk to assume the `aws-elasticbeanstalk-service-role` role, the service role specifies Elastic Beanstalk as a trusted entity in the trust
relationship policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "elasticbeanstalk.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "sts:ExternalId": "elasticbeanstalk"
 }
 }
 }
 ]
}`

```

When you enable [managed platform updates](environment-platform-update-managed.md "environment-platform-update-managed.md") for your environment, Elastic Beanstalk assumes a separate
managed-updates service role to perform managed updates. By default, the Elastic Beanstalk console uses the same generated service role,
`aws-elasticbeanstalk-service-role`, for the managed-updates service role. If you change your default service role, the console sets the
managed-updates service role to use the managed-updates service-linked role, `AWSServiceRoleForElasticBeanstalkManagedUpdates`. For more
information about service-linked roles, see [Using service-linked roles](#iam-servicerole-slr "#iam-servicerole-slr").

###### Note

Because of permission issues, the Elastic Beanstalk service doesn't always successfully create this service-linked role for you. Therefore, the console tries
to explicitly create it. To ensure your account has this service-linked role, create an environment at least once using the console, and configure
managed updates to be enabled before you create the environment.

### Using the EB CLI

If you launch an environment using the [eb create](eb3-create.md "eb3-create.md") command of the Elastic Beanstalk Command Line Interface (EB CLI) and don't specify a service
role through the `--service-role` option, Elastic Beanstalk creates the default service role `aws-elasticbeanstalk-service-role`. If the
default service role already exists, Elastic Beanstalk uses it for the new environment. The Elastic Beanstalk console also performs similar actions in these situations.

Unlike in the console, you can't specify a managed-updates service role when using an EB CLI command option. If you enable managed updates for your
environment, you must set the managed-updates service role though configuration options. The following example enables managed updates and uses the
default service role as a managed-updates service role.

###### Example .ebextensions/managed-platform-update.config

```
option_settings:
  aws:elasticbeanstalk:managedactions:
    ManagedActionsEnabled: true
    PreferredStartTime: "Tue:09:00"
    ServiceRoleForManagedUpdates: "aws-elasticbeanstalk-service-role"
  aws:elasticbeanstalk:managedactions:platformupdate:
    UpdateLevel: patch
    InstanceRefreshEnabled: true
```

## Managing service roles using the Elastic Beanstalk API

When you use the `CreateEnvironment` action of the Elastic Beanstalk API to create an environment, specify a service role using the
`ServiceRole` configuration option in the `aws:elasticbeanstalk:environment` namespace. For more information about using enhanced health monitoring with the Elastic Beanstalk API, see [Using enhanced health reporting with the Elastic Beanstalk
API](health-enhanced-api.md "health-enhanced-api.md").

In addition, if you enable [managed platform updates](environment-platform-update-managed.md "environment-platform-update-managed.md") for your environment, you can specify a
managed-updates service role using the `ServiceRoleForManagedUpdates` option of the `aws:elasticbeanstalk:managedactions` namespace.

## Using service-linked roles

A service-linked role is a unique type of service role that's predefined by Elastic Beanstalk to include all the permissions that the service requires to call
other AWS services on your behalf. The service-linked role is associated with your account. Elastic Beanstalk creates it once, then reuses it when creating
additional environments. For more information about using service-linked roles with Elastic Beanstalk environments, see [Using service-linked roles for Elastic Beanstalk](using-service-linked-roles.md "using-service-linked-roles.md").

If you create an environment by using the Elastic Beanstalk API and don't specify a service role, Elastic Beanstalk creates a [monitoring service-linked role](using-service-linked-roles-monitoring.md "using-service-linked-roles-monitoring.md") for your account, if one doesn't already exist. Elastic Beanstalk uses this
role for the new environment. You can also use IAM to create a monitoring service-linked role for your account in advance. After your account has this
role, you can use it to create an environment using the Elastic Beanstalk API, the Elastic Beanstalk console, or the EB CLI.

If you enable [managed platform updates](environment-platform-update-managed.md "environment-platform-update-managed.md") for the environment and specify
`AWSServiceRoleForElasticBeanstalkManagedUpdates` as the value for the `ServiceRoleForManagedUpdates` option of the `aws:elasticbeanstalk:managedactions` namespace, Elastic Beanstalk creates a [managed-updates service-linked role](using-service-linked-roles-managedupdates.md "using-service-linked-roles-managedupdates.md") for your account, if one doesn't already exist. Elastic Beanstalk
uses the role to perform managed updates for the new environment.

###### Note

When Elastic Beanstalk tries to create the monitoring and managed-updates service-linked roles for your account when you create an environment, you must have
the `iam:CreateServiceLinkedRole` permission. If you don't have this permission, environment creation fails, and a message explaining the
issue is displayed.

As an alternative, another user with permission to create service-linked roles can use IAM to create the service linked-role in advance. Using
this method, you don't need the `iam:CreateServiceLinkedRole` permission to create your environment.

## Verifying the default service role permissions

The permissions granted by your default service role can vary based on when they were created, the last time you launched an environment, and which
client you used. In the IAM console, you can verify the permissions granted by the default service role.

###### To verify the default service role's permissions

1. In the IAM console, open the [**Roles** page](https://console.aws.amazon.com/iam/home#roles "https://console.aws.amazon.com/iam/home#roles").
2. Choose **aws-elasticbeanstalk-service-role**.
3. On the **Permissions** tab, review the list of policies attached to the role.
4. To view the permissions that a policy grants, choose the policy.

## Updating an out-of-date default service role

If the default service role lacks the required permissions, you can update it by [creating a new
environment](using-features.md "using-features.md") in the Elastic Beanstalk environment management console.

Alternatively, you can manually add the managed policies to the default service role.

###### To add managed policies to the default service role

1. In the IAM console, open the [**Roles** page](https://console.aws.amazon.com/iam/home#roles "https://console.aws.amazon.com/iam/home#roles") .
2. Choose **aws-elasticbeanstalk-service-role**.
3. On the **Permissions** tab, choose **Attach policies**.
4. Enter `AWSElasticBeanstalk` to filter the policies.
5. Select the following policies, and then choose **Attach policy**:
   - `AWSElasticBeanstalkEnhancedHealth`
   - `AWSElasticBeanstalkManagedUpdatesCustomerRolePolicy`

## Adding permissions to the default service role

If your application includes configuration files that refer to AWS resources that permissions aren't included in the default service role for, Elastic Beanstalk
might need additional permissions. These additional permissions are needed to resolve these references when it processes the configuration files during a
managed update. If the permissions are missing, the update fails, and Elastic Beanstalk returns a message indicating which permissions it needs. Follow these steps to
add permissions for additional services to the default service role in the IAM console.

###### To add additional policies to the default service role

1. In the IAM console, open the [**Roles** page](https://console.aws.amazon.com/iam/home#roles "https://console.aws.amazon.com/iam/home#roles").
2. Choose **aws-elasticbeanstalk-service-role**.
3. On the **Permissions** tab, choose **Attach policies**.
4. Select the managed policy for the additional services that your application uses. For example, `AmazonAPIGatewayAdministrator` or
   `AmazonElasticFileSystemFullAccess`.
5. Choose **Attach policy**.

## Creating a service role

If you can't use the default service role, create a service role.

###### To create a service role

1. In the IAM console, open the [**Roles** page](https://console.aws.amazon.com/iam/home#roles "https://console.aws.amazon.com/iam/home#roles").
2. Choose **Create role**.
3. Under **AWS service**, choose **AWS Elastic Beanstalk**, and then select your use case.
4. Choose **Next: Permissions**.
5. Attach the `AWSElasticBeanstalkManagedUpdatesCustomerRolePolicy` and `AWSElasticBeanstalkEnhancedHealth` managed policies and any additional
   policies that provide permissions that your application needs.
6. Choose **Next: Tags**.
7. (Optional) Add tags to the role.
8. Choose **Next: Review**.
9. Enter a name for the role.
10. Choose **Create role**.

Apply your custom service role when you create an environment either using the [environment creation
wizard](environments-create-wizard.md "environments-create-wizard.md") or with the `--service-role` option for the `eb create` command.
