# EDI customer account access

###### Important

During the EDI account onboarding and deployment, ECO requests root user permission.

When you first create an AWS account, you begin with one sign-in identity that has complete access to all AWS services
and resources in the account. This identity is called the AWS account _root user_ and is accessed by
signing in with the email address and password that you used to create the account.

###### Important

We strongly recommend that you don't use the root user for your everyday tasks. Safeguard your root user credentials and use them to
perform the tasks that only the root user can perform. For the complete list of tasks that require you to sign in as the root user, see [Tasks that require root user credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks") in the _IAM User Guide_.

ECO uses a predefined access model to access your EDI account. For more information, see
[How AMS accesses your account](../../../managedservices/latest/accelerate-guide/acc-access-operator.md "../../../managedservices/latest/accelerate-guide/acc-access-operator.md").

For more information about ECO customer account access, see
[Why and when AMS accesses your account](../../../managedservices/latest/accelerate-guide/access-justification.md "../../../managedservices/latest/accelerate-guide/access-justification.md").
