# Manage AWS accounts with permission
 sets

A permission set is a template that you create and maintain that defines a collection
 of one or more [IAM
 policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html"). Permission sets simplify the assignment of AWS account access
 for users and groups in your organization. For example, you can create a *Database Admin* permission set that includes policies for
 administering AWS RDS, DynamoDB, and Aurora services, and use that single permission set
 to grant access to a list of target AWS accounts within your [AWS Organization](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/") for your
 database administrators.

IAM Identity Center assigns access to a user or group in one or more AWS accounts with permission
 sets. When you assign a permission set, IAM Identity Center creates corresponding IAM Identity Center-controlled
 IAM roles in each account, and attaches the policies specified in the permission set
 to those roles. IAM Identity Center manages the role, and allows the authorized users you’ve defined
 to assume the role, by using the IAM Identity Center User Portal or AWS CLI.  As you modify the
 permission set, IAM Identity Center ensures that the corresponding IAM policies and roles are
 updated accordingly.

You can add [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies"), [customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies"), [inline policies](https://docs.aws.amazon.com/https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#inline-policies "https://docs.aws.amazon.com/https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#inline-policies"), 
 and [AWS managed policies
 for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html") to your permission sets. You can also assign an AWS
 managed policy or a customer managed policy as a [permissions
 boundary](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html").

To create a permission set, see [Create, manage, and delete permission sets](permissionsets.md "permissionsets.md").


## Create a permission set that applies least-privilege permissions


To follow the best practice of applying least-privilege permissions, after you
 create an administrative permission set, you create a more restrictive permission
 set and assign it to one or more users. The permission sets created in the previous
 procedure provide a starting point for you to assess the amount of access to
 resources your users need. To switch to least privilege permissions, you can run
 IAM Access Analyzer to monitor principals with AWS managed policies. After learning
 which permissions they are using, then you can write a custom policy or generate a
 policy with only the required permissions for your team. 


With IAM Identity Center, you can assign multiple permission sets to the same user. Your
 administrative user should also be assigned additional, more restrictive, permission
 sets. That way, they can access your AWS account with only the permissions that
 required, rather than always using their administrative permissions.


For example, if you're a developer, after you create your administrative user in
 IAM Identity Center, you can create a new permission set that grants `PowerUserAccess`
 permissions, and then assign that permission set to yourself. Unlike the
 administrative permission set, which uses `AdministratorAccess`
 permissions, the `PowerUserAccess`  permission set doesn't allow
 management of IAM users and groups. When you sign into the AWS access portal to
 access your AWS account, you can choose `PowerUserAccess` rather than
 the `AdministratorAccess` to perform development tasks in the
 account.


Keep the following considerations in mind:



* **To get started quickly with creating a more
 restrictive permission set, use a predefined permission set rather than
 a custom permission set.**



With a predefined permission set, which uses [predefined permissions](permissionsetpredefined.md "permissionsetpredefined.md"), you
 choose a single AWS managed policy from a list of available policies. Each
 policy grants a specific level of access to AWS services and resources or
 permissions for a common job function. For information about each of these
 policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html").
* **You can configure the session duration for a
 permission set to control the length of time that a user is signed into
 an AWS account.**



When users federate into their AWS account and use the AWS Management
 Console or the AWS Command Line Interface (AWS CLI), IAM Identity Center uses the
 session duration setting on the permission set to control the duration of
 the session. By default, the value for **Session
 duration**, which determines the length of time that a user can be
 signed into an AWS account before AWS signs the user out of the session,
 is set to one hour. You can specify a maximum value of 12 hours. For more
 information, see [Set session duration for
 AWS accounts](howtosessionduration.md "howtosessionduration.md").
* **You can also configure the AWS access portal
 session duration to control the length of time that a workforce user is
 signed into the portal.**



By default, the value for **Maximum session duration**,
 which determines the length of time that a workforce user can be signed in
 to the AWS access portal before they must re-authenticate, is eight hours.
 You can specify a maximum value of 90 days. For more information, see [Configure the session duration in IAM Identity Center](configure-user-session.md "configure-user-session.md").
* **When you sign into the AWS access portal, choose
 the role that provides least-privilege permissions.** 


Each permission set that you create and assign to your user appears as an
 available role in the AWS access portal. When you sign in to the portal as
 that user, choose the role that corresponds to the most restrictive
 permission set that you can use to perform tasks in the account, rather than
 `AdministratorAccess`.
* **You can add other users to IAM Identity Center and assign existing
 or new permission sets to those users.**


For information, see, [Assign user or group access to AWS accounts](assignusers.md "assignusers.md").

###### Topics

* [Predefined permissions for
 AWS managed policies](permissionsetpredefined.md "permissionsetpredefined.md")
* [Custom permissions for AWS managed and
 customer managed policies](permissionsetcustom.md "permissionsetcustom.md")
* [Create, manage, and delete permission sets](permissionsets.md "permissionsets.md")
* [Configure permission set properties](permproperties.md "permproperties.md")
