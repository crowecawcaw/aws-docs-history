# Interactive sessions with IAM

These sections describe security considerations for AWS Glue interactive sessions.

###### Topics

- [IAM principals used with interactive sessions](#glue-is-security-iam-principals "#glue-is-security-iam-principals")
- [Setting up a client principal](#glue-is-client-principals "#glue-is-client-principals")
- [Setting up a runtime role](#glue-is-runtime-role "#glue-is-runtime-role")
- [Make your session private with TagOnCreate](#glue-is-tagoncreate "#glue-is-tagoncreate")
- [IAM policy considerations](#glue-is-security-iam-managed-policy "#glue-is-security-iam-managed-policy")

## IAM principals used with interactive sessions

You use two IAM principals used with AWS Glue interactive sessions.

- **Client principal**: The client principal (either a user or a role) authorizes API
  operations for interactive sessions from an AWS Glue client that's configured with the
  principal's identity-based credentials. For example, this could be an IAM role that you typically use to
  access the AWS Glue console. This could also be a role given to a user in IAM whose
  credentials are used for the AWS Command Line Interface, or an AWS Glue client used by the interactive sessions
  Jupyter kernel.
- **Runtime role**: The runtime role is an IAM role that the client principal passes to interactive sessions API operations.
  AWS Glue uses this role to run statements in your session. For example, this role could be the one used for
  running AWS Glue ETL jobs.

For more information, see
[Setting up a runtime role](#glue-is-runtime-role "#glue-is-runtime-role").

## Setting up a client principal

You must attach an identity policy to the client principal to allow it to call
the interactive sessions API. This role must have `iam:PassRole` access to the
execution role that you would pass to the interactive sessions API, such as
`CreateSession`. For example, you can attach the
**AWSGlueConsoleFullAccess** managed policy to an IAM role which allows
users in your account with the policy attached to access all
the sessions created in your account (such as runtime statement or cancel statement).

If you would like to protect your session and make it private only to certain IAM roles, such as ones
associated with the user who created the session then you can use AWS Glue Interactive
Session's Tag Based Authorization Control called TagOnCreate. For more information, see [Make your session private with TagOnCreate](#glue-is-tagoncreate "#glue-is-tagoncreate") on how an owner tag-based scoped down
managed policy can make your session private with TagOnCreate. For more information on identity-based policies,
see [Identity-based policies for AWS Glue](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies").

## Setting up a runtime role

You must pass an IAM role to the CreateSession API operation in order to allow AWS Glue to assume and run
statements in interactive sessions. The role should have the same IAM permissions as those required to run a typical
AWS Glue job. For example, you can create a service role using the **AWSGlueServiceRole** policy that
allows AWS Glue to call AWS services on your behalf. If you use the AWS Glue console, it will automatically
create a service role on your behalf or use an existing one. You can also create your own IAM role and attach your own IAM policy
to allow similar permissions.

If you would like to protect your session and make it private only to the user who created the session then you can use
AWS Glue Interactive Session's Tag Based Authorization Control called TagOnCreate.
For more information, see
[Make your session private with TagOnCreate](#glue-is-tagoncreate "#glue-is-tagoncreate")
on
how an owner tag-based scoped down managed policy can make your session private with TagOnCreate.
For more information on identity-based policies, see [Identity-based
policies for AWS Glue](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies").
If you are creating the execution role by yourself from the IAM console and you want to make your service
private with TagOnCreate feature then follow the steps below.

1. Create an IAM role with role type set to `Glue`.
2. Attach this AWS Glue managed policy: _AwsGlueSessionUserRestrictedServiceRole_
3. Prefix the role name with the policy name _AwsGlueSessionUserRestrictedServiceRole_. For example,
   you can create a role with name _AwsGlueSessionUserRestrictedServiceRole-myrole_ and attach
   AWS Glue managed policy _AwsGlueSessionUserRestrictedServiceRole_.
4. Attach a trust policy like following to allow AWS Glue to assume the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "glue.amazonaws.com"
 ]
 },
 "Action": [
 "sts:AssumeRole"
 ]
 }
 ]
}`

```

For an interactive sessions Jupyter kernel, you can specify the `iam_role` key in your AWS Command Line Interface profile. For more information,
see
[Configuring sessions with ~/.aws/config](../ug/interactive-sessions-magics.md#interactive-sessions-named-profiles "../ug/interactive-sessions-magics.md#interactive-sessions-named-profiles") .
If you're interacting with interactive sessions using an AWS Glue notebook, then you can pass the execution role
in the `%iam_role` magic in the first cell that you run.

##

Make your session private with TagOnCreate

AWS Glue interactive sessions supports tagging and Tag Based Authorization (TBAC) for interactive sessions as a named resource.
In addition to TBAC using TagResource and UntagResource APIs, AWS Glue interactive sessions supports
the TagOnCreate feature to 'tag' a session with a given tag only during session creation with CreateSession operation.
This also means those tags will be removed on DeleteSession, aka UntagOnDelete.

TagOnCreate offers a powerful security mechanism to make your session private to the creator of the session.
For example, you can attach an IAM policy with "owner" RequestTag and value of ${aws:userId} to a client principal (such as an user)
in order to allow creating a session only if an "owner" tag with matching value of the callers userId is provided as userId tag in
CreateSession request. This policy allows AWS Glue interactive sessions to create a session resource and tag the session with
the userId tag only during session creation time. In addition to it you can scope down the access (like running statements) to your
session only to the creator (aka owner tag with value ${aws:userId}) of the session by attaching an IAM policy with "owner"
ResourceTag to the execution role you passed in during CreateSession.

In order to make it easier for you to use TagOnCreate feature to make a session private to the session
creator, AWS Glue provides specialized managed policies and service roles.

If you want to create a AWS Glue Interactive Session using an IAM AssumeRole principal (that is, using credential vended
by assuming an IAM role) and you want to make the session private to the creator, then use policies similar to the **AWSGlueSessionUserRestrictedNotebookPolicy**
and **AWSGlueSessionUserRestrictedNotebookServiceRole**
respectively. These policies allow AWS Glue to use ${aws:PrincipalTag} to extract the owner tag value.
This requires you to pass a userId tag with value ${aws:userId} as SessionTag in the assume role credential. See
[ID session tags](../../../IAM/latest/UserGuide/id_session-tags.md "../../../IAM/latest/UserGuide/id_session-tags.md") .
If you are using an Amazon EC2 instance with an instance profile vending the credential and you want to create a session or
interact with the session from within the Amazon EC2 instance , then you would require to pass a userId tag with value ${aws:userId} as
SessionTag in the assume role credential.

For example, If you are creating a session using an IAM AssumeRole principal credential and you want to make
your service private with TagOnCreate feature then follow the steps below.

1. Create a runtime role yourself from the IAM console. Please attach this AWS Glue managed policy
   _AwsGlueSessionUserRestrictedNotebookServiceRole_ and prefix the role name with the policy name
   _AwsGlueSessionUserRestrictedNotebookServiceRole_. For example, you can create a role with name
   _AwsGlueSessionUserRestrictedNotebookServiceRole-myrole_ and attach AWS Glue managed policy
   _AwsGlueSessionUserRestrictedNotebookServiceRole_.
2. Attach a trust policy like below to allow AWS Glue to assume the above role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "glue.amazonaws.com"
 ]
 },
 "Action": [
 "sts:AssumeRole"
 ]
 }
 ]
}`

```

3. Create another role named with a prefix _AwsGlueSessionUserRestrictedNotebookPolicy_ and attach the
   AWS Glue managed policy _AwsGlueSessionUserRestrictedNotebookPolicy_ to make the session private.
   In addition to the managed policy please attach the following inline policy to allow iam:PassRole to the role you created in step 1.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/AwsGlueSessionUserRestrictedNotebookServiceRole*"
 ],
 "Condition": {
 "StringLike": {
 "iam:PassedToService": [
 "glue.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

4. Attach a trust policy like following to the above IAM AWS Glue to assume the role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "glue.amazonaws.com"
 ]
 },
 "Action": [
 "sts:AssumeRole",
 "sts:TagSession"
 ]
 }
 ]
}`

```

###### Note

Optionally, you can use a single role (for example, notebook role) and attach both of the above managed policies
_AwsGlueSessionUserRestrictedNotebookServiceRole_ and
_AwsGlueSessionUserRestrictedNotebookPolicy_. Also attach the additional inline policy to allow
`iam:passrole` of your role to AWS Glue. And finally attach the above trust policy to allow
`sts:AssumeRole` and `sts:TagSession`.

###

AWSGlueSessionUserRestrictedNotebookPolicy

The AWSGlueSessionUserRestrictedNotebookPolicy provides access to create a AWS Glue Interactive Session from a notebook
only if a tag key "owner" and value matching the AWS user id of the principal (user or Role). For more information, see
[Where you can use policy
variables](../../../IAM/latest/UserGuide/reference_policies_variables.md#policy-vars-infotouse "../../../IAM/latest/UserGuide/reference_policies_variables.md#policy-vars-infotouse") . This policy is attached to the principal (User or role) that creates AWS Glue Interactive Session notebooks
from AWS Glue Studio. This policy also permits sufficient access to the AWS Glue Studio notebook to interact with the
AWS Glue Studio Interactive Session resources that are created with the "owner" tag value matching the AWS user ID of the principal.
This policy denies permission to change or remove "owner" tag from a AWS Glue session resource after the session is created.

###

AWSGlueSessionUserRestrictedNotebookServiceRole

The **AWSGlueSessionUserRestrictedNotebookServiceRole** provides sufficient access to the AWS Glue Studio notebook to
interact with the
AWS Glue Interactive Session resources that are created with the "owner" tag value matching the AWS user ID of the principal
(user or role) of the notebook creator. For more information, see
[Where you can use policy
variables](../../../IAM/latest/UserGuide/reference_policies_variables.md#policy-vars-infotouse "../../../IAM/latest/UserGuide/reference_policies_variables.md#policy-vars-infotouse") .
This service-role policy is attached to the role that is passed as magic to a notebook or passed
as execution role to the CreateSession API. This policy also permits to create a AWS Glue Interactive Session from a notebook only
if a tag key "owner" and value matching the AWS user ID of the principal. This policy denies permission to change or remove "owner" tag from
an AWS Glue session resource after the session is created. This policy also includes permissions for writing and reading from
Amazon S3 buckets, writing CloudWatch logs, creating and deleting tags for Amazon EC2 resources used by AWS Glue.

### Make your session private with user policies

You can attach the **AWSGlueSessionUserRestrictedPolicy** to IAM roles attached to
each of the users in your account to restrict them from creating a session only with an owner tag with a value
matching their own ${aws:userId}. Instead of using the
**AWSGlueSessionUserRestrictedNotebookPolicy** and
**AWSGlueSessionUserRestrictedNotebookServiceRole** you need to use policies similar to the
**AWSGlueSessionUserRestrictedPolicy** and
**AWSGlueSessionUserRestrictedServiceRole** respectively. For more information, see [Using-identity based
policies](using-identity-based-policies.md "using-identity-based-policies.md") . This policy scopes down the access to a session only to the creator, the ${aws:userId}
of the user who created the session with an owner tag bearing their own ${aws:userId}. If you have created
the execution role yourself using the IAM console by following the steps in [Setting up a runtime role](#glue-is-runtime-role "#glue-is-runtime-role"), then in
addition to attaching the **AwsGlueSessionUserRestrictedPolicy** managed policy, also attach the
following inline policy to each of the users in your account to allow `iam:PassRole` for the
execution role you created earlier.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/AwsGlueSessionUserRestrictedServiceRole*"
 ],
 "Condition": {
 "StringLike": {
 "iam:PassedToService": [
 "glue.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

#### AWSGlueSessionUserRestrictedPolicy

The **AWSGlueSessionUserRestrictedPolicy** provides access to create an
AWS Glue Interactive Session using the CreateSession API only if a tag key "owner" and value
matching their AWS user ID is provided. This identity policy is attached to the user that invokes
the CreateSession API. This policy also permits to interact with the AWS Glue Interactive
Session resources that were created with a "owner" tag and value matching their AWS user id. This policy
denies permission to change or remove "owner" tag from a AWS Glue session resource after the
session is created.

#### AWSGlueSessionUserRestrictedServiceRole

The **AWSGlueSessionUserRestrictedServiceRole** provides full access to all
AWS Glue resources except for sessions and allows users to create and use only the interactive
sessions that are associated with the user. This policy also includes other permissions needed by
AWS Glue to manage Glue resources in other AWS services. The policy also allows adding tags to
AWS Glue resources in other AWS services.

## IAM policy considerations

Interactive sessions are IAM resources in AWS Glue. Because they are IAM resources, access and interaction to
a session is governed by IAM policies. Based on the IAM policies attached to a client principal or execution role configured
by an admin, a client principal (user or role) will be able to create new sessions and interact with its own sessions and other sessions.

If an admin has attached an IAM policy such as
AWSGlueConsoleFullAccess or AWSGlueServiceRole that allows access to all
AWS Glue resources in that account, a client principal will be able to collaborate with each other. For example, one
user will be able to interact with sessions that are created by other users if policies allow this.

If you'd like to configure a policy tailored to your specific needs, see
[IAM documentation about configuring resources for a policy](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md") .
For example, in order to isolate sessions that belong to an user,
you can use the TagOnCreate feature supported by AWS Glue Interactive sessions.
See [Make your session private with TagOnCreate](#glue-is-tagoncreate "#glue-is-tagoncreate") .

Interactive sessions supports limiting session creation based on certain VPC conditions. See
[Control policies
that control settings using condition keys](security_iam_id-based-policy-examples.md#glue-identity-based-policy-condition-key-vpc "security_iam_id-based-policy-examples.md#glue-identity-based-policy-condition-key-vpc").
