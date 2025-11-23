# Elastic Beanstalk service role

A service role is the IAM role that Elastic Beanstalk assumes when calling other services on your
behalf. For example, Elastic Beanstalk uses a service role when it calls Amazon Elastic Compute Cloud (Amazon EC2), ELB, and
Amazon EC2 Auto Scaling APIs to gather information. The service role that Elastic Beanstalk uses is the one that you
specified when you create the Elastic Beanstalk environment.

There are two managed policies that are attached to the service role. These policies
provide the permissions that allow Elastic Beanstalk to access the required AWS resources to create and
manage your environments. One managed policy provides permissions for [enhanced health monitoring](health-enhanced.md "health-enhanced.md") and worker tier Amazon SQS support,
and another one provides additional permissions required for [managed platform updates](environment-platform-update-managed.md "environment-platform-update-managed.md").

## `AWSElasticBeanstalkEnhancedHealth`

This policy grants permissions for Elastic Beanstalk to monitor instance and environment health. It also includes Amazon SQS actions to allow Elastic Beanstalk to monitor queue
activity for worker environments. To view the content of this managed policy, see the [AWSElasticBeanstalkEnhancedHealth](../../../aws-managed-policy/latest/reference/AWSElasticBeanstalkEnhancedHealth.md "../../../aws-managed-policy/latest/reference/AWSElasticBeanstalkEnhancedHealth.md") page in the _AWS Managed
Policy Reference Guide_.

## `AWSElasticBeanstalkManagedUpdatesCustomerRolePolicy`

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

You may create an Elastic Beanstalk environment with any of the following approaches. Each section
describes how the approach handles the service role.

###### Elastic Beanstalk console

If you create an environment using the Elastic Beanstalk console, Elastic Beanstalk prompts you to create a
service role that's named `aws-elasticbeanstalk-service-role`. When created via
Elastic Beanstalk, this role includes a trust policy that allows Elastic Beanstalk to assume the service role. The
two managed policies described earlier in this topic are also attached to the role.

###### Elastic Beanstalk Command Line Interface (EB CLI)

You may create an environment using the [eb create](eb3-create.md "eb3-create.md") command of the
Elastic Beanstalk Command Line Interface (EB CLI). If you don't specify a service role through the
`--service-role` option. Elastic Beanstalk creates the same default service role
`aws-elasticbeanstalk-service-role`. If the default service role already
exists, Elastic Beanstalk uses it for the new environment. When created via Elastic Beanstalk, this role includes a
trust policy that allows Elastic Beanstalk to assume the service role. The two managed policies
described earlier in this topic are also attached to the role.

###### Elastic Beanstalk API

You may create an environment using the `CreateEnvironment` action of the
Elastic Beanstalk API. If you don't specify a service role, Elastic Beanstalk creates a monitoring service-linked
role. This is a unique type of service role that is predefined by Elastic Beanstalk to include all the
permissions that the service requires to call other AWS services on your behalf. The
service-linked role is associated with your account. Elastic Beanstalk creates it once, and then reuses
it when creating additional environments. You can also use IAM to create the monitoring
service-linked role for your account in advance. When your account has a monitoring
service-linked role, you can use it to create an environment using either the Elastic Beanstalk console,
the Elastic Beanstalk API, or the EB CLI. For instructions on how to use service-linked roles with Elastic Beanstalk
environments, see [Using service-linked roles for Elastic Beanstalk](using-service-linked-roles.md "using-service-linked-roles.md").

For more information about service roles, see [Managing Elastic Beanstalk service roles](iam-servicerole.md "iam-servicerole.md").
