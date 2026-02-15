# Using AWS Supply Chain console

Using the console is the easiest way to manage your service resources and configurations. The console provides an intuitive web-based interface where you can view, create, modify, and monitor your resources. This section shows you how to access and navigate the console to perform common management tasks.

###### Note

If your AWS account is a member account of an AWS organization and includes a Service Control Policy (SCP), make sure the organization's SCP grants the following permissions to the member account.
If the following permissions are not included in the organization's SCP policy, AWS Supply Chain instance creation will fail.

To access the AWS Supply Chain console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the AWS Supply Chain resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

The following permissions are needed by the Console Admin to create and update
AWS Supply Chain instances successfully.

JSON

```


```

`key_arn` specifies the key you would like to use for the AWS Supply Chain instance. For best practices and to restrict access to only the keys you would like to use for AWS Supply Chain,
see [Specifying KMS keys in IAM policy statements](../../../kms/latest/developerguide/cmks-in-iam-policies.md "../../../kms/latest/developerguide/cmks-in-iam-policies.md"). To represent all KMS keys, use a wildcard character alone ("\*").
