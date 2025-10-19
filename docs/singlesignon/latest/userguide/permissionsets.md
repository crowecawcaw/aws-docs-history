# Create, manage, and delete permission sets

Permission sets define the level of access that users and groups have to an
 AWS account. Permission sets are stored in IAM Identity Center and can be provisioned to one or
 more AWS accounts. You can assign more than one permission set to a user. For more
 information about permission sets and how they are used in IAM Identity Center, see [Manage AWS accounts with permission
 sets](permissionsetsconcept.md "permissionsetsconcept.md").

###### Note

You can search and sort permission sets by name in the IAM Identity Center console.

Keep the following considerations in mind when creating permissions sets:


* **Organization instance**


To use permission sets, you'll need to use an Organization instance of
 IAM Identity Center. For more information, see [Organization and account instances of IAM Identity Center](identity-center-instances.md "identity-center-instances.md").
* **Start with a predefined permission set**



With a predefined permission set, which uses [predefined permissions](permissionsetpredefined.md "permissionsetpredefined.md"), you
 choose a single AWS managed policy from a list of available policies. Each
 policy grants a specific level of access to AWS services and resources or
 permissions for a common job function. For information about each of these
 policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html"). After you have
 collected usage data you can refine the permission set to be more
 restrictive.
* **Limit management session duration to reasonable work
 periods**



When users federate into their AWS account and use the AWS Management Console or the
 AWS Command Line Interface (AWS CLI), IAM Identity Center uses the session duration
 setting on the permission set to control the duration of the session. When
 the user session reaches the session duration they are signed out of the
 console and asked to sign in again. As a security best practice, we
 recommend that you do not set the session duration length longer than is
 needed to perform the role. By default, the value for **Session
 duration** is one hour. You can specify a maximum value of 12
 hours. For more information, see [Set session duration for
 AWS accounts](howtosessionduration.md "howtosessionduration.md").
* **Limit workforce user portal session
 duration**



Workforce users use portal sessions to choose roles and access
 applications. By default, the value for **Maximum session
 duration**, which determines the length of time that a
 workforce user can be signed in to the AWS access portal before they must
 re-authenticate, is eight hours. You can specify a maximum value of 90 days.
 For more information, see [Configure the session duration in IAM Identity Center](configure-user-session.md "configure-user-session.md").
* **Use the role that provides least-privilege
 permissions** 


Each permission set that you create and assign to your user appears as an
 available role in the AWS access portal. When you sign in to the portal as
 that user, choose the role that corresponds to the most restrictive
 permission set that you can use to perform tasks in the account, rather than
 `AdministratorAccess`. Test your permission sets to verify
 they provide the necessary access before sending the user invitation.
###### Note

You can also use [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/AWS_SSO.md "../../../AWSCloudFormation/latest/UserGuide/AWS_SSO.md") to create and assign permission sets and assign users to
 those permission sets.

###### Topics

* [Create a permission set](howtocreatepermissionset.md "howtocreatepermissionset.md")
* [View and change a permission
 set](howtoviewandchangepermissionset.md "howtoviewandchangepermissionset.md")
* [Delegate permission set
 administration](permissionsetdelegation.md "permissionsetdelegation.md")
* [Use IAM policies in permission sets](howtocmp.md "howtocmp.md")
* [Remove permission sets in
 IAM Identity Center](howtoremovepermissionset.md "howtoremovepermissionset.md")
* [Delete permission sets in
 IAM Identity Center](howtodeletepermissionset.md "howtodeletepermissionset.md")
