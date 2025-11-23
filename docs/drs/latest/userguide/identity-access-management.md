# Identity and access management for

AWS Elastic Disaster Recovery

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control
access to AWS resources. IAM administrators control who can be authenticated (signed
in) and authorized (have permissions) to use AWS resources. IAM allows you to create
users and groups under your AWS account. You control the permissions that users have to
perform tasks using AWS resources. You can use IAM for no additional charge.

By default, IAM users don't have permissions for AWS Elastic Disaster Recovery (AWS DRS) resources and
operations. To allow IAM users to manage AWS DRS resources, you must create an IAM
policy that explicitly grants them permissions, and attach the policy to the users or
groups that require those permissions.

When you attach a policy to a user or group of users, it allows or denies the users
permission to perform the specified tasks on the specified resources. For more information,
see [Policies and Permissions](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the
_IAM User Guide_
guide.

## Federated identity

As a best practice, require human users to use federation with an identity provider to access AWS services using temporary credentials.

A _federated identity_ is a user from your enterprise directory, web identity provider, or Directory Service that accesses AWS services using credentials from an identity source. Federated identities assume roles that provide temporary credentials.

For centralized access management, we recommend AWS IAM Identity Center. For more information, see [What is IAM Identity Center?](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") in the _AWS IAM Identity Center User Guide_.

## Policy structure

An IAM policy is a JSON document that consists of one or more statements. Each
statement is structured as follows:

```
{
	"Statement": [
		{
			"Effect": "`effect`",
			"Action": "`action`",
			"Resource": "`arn`",
			"Condition": {
				"`condition`": {
					"`key`": "`value`"
				}
			}
		}
	]
}

```

There are various elements that make up a statement:

- **Effect:** The effect can be `Allow` or
  `Deny`. By default, IAM users don't have permission to use
  resources and API actions, so all requests are denied. An explicit allow
  overrides the default. An explicit deny overrides any allows.
- **Action**: The action is the specific AWS Elastic Disaster Recovery API
  action for which you are granting or denying permission.
- **Resource**: The resource that's affected by the action.
  For AWS Elastic Disaster Recovery, you must specify "\*" as the resource.
- **Condition**: Conditions are optional. They can be
  used to control when your policy is in effect.
