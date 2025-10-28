# Configuration options for retrieving

sensitive data samples with Macie

You can optionally configure and use Amazon Macie to retrieve and reveal samples of sensitive
data that Macie reports in individual findings. If you retrieve and reveal sensitive data
samples for a finding, Macie uses data in the corresponding [sensitive data discovery result](discovery-results-repository-s3.md "discovery-results-repository-s3.md") to
locate occurrences of sensitive data in the affected Amazon Simple Storage Service (Amazon S3) object. Macie then
extracts samples of those occurrences from the affected object. Macie encrypts the extracted
data with an AWS Key Management Service (AWS KMS) key that you specify, temporarily stores the encrypted data
in a cache, and returns the data in your results for the finding. Soon after extraction and
encryption, Macie permanently deletes the data from the cache unless additional retention is
temporarily required to resolve an operational issue.

Macie doesn't use the [Macie service-linked
role](service-linked-roles.md "service-linked-roles.md") for your account to locate, retrieve, encrypt, or reveal sensitive data
samples for affected S3 objects. Instead, Macie uses settings and resources that you
configure for your account. When you configure the settings in Macie, you specify how to
access affected S3 objects. You also specify which AWS KMS key to use to encrypt the
samples. You can configure the settings in all the AWS Regions where Macie is currently
available except the Asia Pacific (Osaka) and Israel (Tel Aviv) Regions.

To access affected S3 objects and retrieve sensitive data samples from them, you have two
options. You can configure Macie to use AWS Identity and Access Management (IAM) user credentials or assume an
IAM role:

- Use IAM user credentials – With this
  option, each user of your account uses their individual IAM identity to locate,
  retrieve, encrypt, and reveal the samples. This means that a user can retrieve and
  reveal sensitive data samples for a finding if they're allowed to access the
  requisite resources and data, and perform the requisite actions.
- Assume an IAM role – With this option, you
  create an IAM role that delegates access to Macie. You also ensure that the trust
  and permissions policies for the role meet all requirements for Macie to assume the
  role. Macie then assumes the role when a user of your account chooses to locate,
  retrieve, encrypt, and reveal sensitive data samples for a finding.
  You can use either configuration with any type of Macie account—the delegated
  Macie administrator account for an organization, a Macie member account in an organization, or a
  standalone Macie account.

The following topics explain options, requirements, and considerations that can help you
determine how to configure the settings and resources for your account. This includes the
trust and permissions policies to attach to an IAM role. For additional recommendations
and examples of policies that you might use to retrieve and reveal sensitive data samples,
see the following blog post on the _AWS Security Blog_:
[How to
use Amazon Macie to preview sensitive data in S3 buckets](https://aws.amazon.com/blogs/security/how-to-use-amazon-macie-to-preview-sensitive-data-in-s3-buckets/ "https://aws.amazon.com/blogs/security/how-to-use-amazon-macie-to-preview-sensitive-data-in-s3-buckets/").

###### Topics

- [Determining which access method
  to use](#findings-retrieve-sd-options-s3access "#findings-retrieve-sd-options-s3access")
- [Using IAM user
  credentials to access affected S3 objects](#findings-retrieve-sd-options-s3access-user "#findings-retrieve-sd-options-s3access-user")
- [Assuming an IAM role to
  access affected S3 objects](#findings-retrieve-sd-options-s3access-role "#findings-retrieve-sd-options-s3access-role")
- [Configuring
  an IAM role to access affected S3 objects](#findings-retrieve-sd-options-s3access-role-configuration "#findings-retrieve-sd-options-s3access-role-configuration")
- [Decrypting affected S3
  objects](#findings-retrieve-sd-options-decrypt "#findings-retrieve-sd-options-decrypt")

## Determining which access method

to use

When determining which configuration is best for your AWS environment, a key
consideration is whether your environment includes multiple Amazon Macie accounts that are
centrally managed as an organization. If you’re the delegated Macie administrator for an
organization, configuring Macie to assume an IAM role can streamline retrieval of
sensitive data samples from affected S3 objects for accounts in your organization. With
this approach, you create an IAM role in your administrator account. You also create
an IAM role in each applicable member account. The role in your administrator account
delegates access to Macie. The role in a member account delegates cross-account access
to the role in your administrator account. If implemented, you can then use role
chaining to access affected S3 objects for your member accounts.

Also consider who has direct access to individual findings by default. To retrieve and
reveal sensitive data samples for a finding, a user must first have access to the
finding:

- Sensitive data discovery jobs – Only the
  account that creates a job can access findings that the job produces. If you
  have a Macie administrator account, you can configure a job to analyze objects in S3
  buckets for any account in your organization. Therefore, your jobs can produce
  findings for objects in buckets that your member accounts own. If you have a
  member account or a standalone Macie account, you can configure a job to analyze
  objects only in buckets that your account owns.
- Automated sensitive data discovery – Only the
  Macie administrator account can access findings that automated discovery produces for accounts in their
  organization. Member accounts can’t access these findings. If you have a
  standalone Macie account, you can access findings that automated discovery produces only for
  your own account.

If you plan to access affected S3 objects by using an IAM role, also consider the
following:

- To locate occurrences of sensitive data in an object, the corresponding
  sensitive data discovery result for a finding must be stored in an S3 object
  that Macie signed with a Hash-based Message Authentication Code (HMAC)
  AWS KMS key. Macie must be able to verify the integrity and authenticity of
  the sensitive data discovery result. Otherwise, Macie doesn't assume the IAM
  role to retrieve sensitive data samples. This is an additional guardrail for
  restricting access to data in S3 objects for an account.
- To retrieve sensitive data samples from an object that's encrypted with a
  customer managed AWS KMS key, the IAM role must be allowed to decrypt data
  with the key. More specifically, the key's policy must allow the role to perform
  the `kms:Decrypt` action. For other types of server-side encryption,
  no additional permissions or resources are required to decrypt an affected
  object. For more information, see [Decrypting affected S3
  objects](#findings-retrieve-sd-options-decrypt "#findings-retrieve-sd-options-decrypt").
- To retrieve sensitive data samples from an object for another account, you
  must currently be the delegated Macie administrator for the account in the applicable
  AWS Region. In addition:
  - Macie must currently be enabled for the member account in the
    applicable Region.
  - The member account must have an IAM role that delegates
    cross-account access to an IAM role in your Macie administrator account. The name
    of the role must be the same in your Macie administrator account and the member
    account.
  - The trust policy for the IAM role in the member account must include
    a condition that specifies the correct external ID for your
    configuration. This ID is a unique alphanumeric string that Macie
    generates automatically after you configure the settings for your
    Macie administrator account. For information about using external IDs in trust
    policies, see [Access to AWS accounts owned by third parties](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") in the _AWS Identity and Access Management User Guide_.
  - If the IAM role in the member account meets all Macie requirements,
    the member account doesn't need to configure and enable Macie settings
    for you to retrieve sensitive data samples from objects for their
    account. Macie uses only the settings and IAM role in your
    Macie administrator account and the IAM role in the member account.

  ###### Tip

  If your account is part of a large organization, consider using an
  AWS CloudFormation template and stack set to provision and manage the IAM roles for
  member accounts in your organization. For information about creating and
  using templates and stack sets, see the [AWS CloudFormation User
  Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md").

  To review and optionally download a CloudFormation template that can
  serve as a starting point, you can use the Amazon Macie console. In the
  navigation pane on the console, under **Settings**,
  choose **Reveal samples**. Choose
  **Edit**, and then choose **View member
  role permissions and CloudFormation template**.

Subsequent topics in this section provide additional details and considerations for
each type of configuration. For IAM roles, this includes the trust and permissions
policies to attach to a role. If you’re not sure which type of configuration is best for
your environment, ask your AWS administrator for assistance.

## Using IAM user

credentials to access affected S3 objects

If you configure Amazon Macie to retrieve sensitive data samples by using IAM user
credentials, each user of your Macie account uses their IAM identity to locate,
retrieve, encrypt, and reveal samples for individual findings. This means that a user
can retrieve and reveal sensitive data samples for a finding if their IAM identity is
allowed to access the requisite resources and data, and perform the requisite actions.
All the requisite actions are [logged in
AWS CloudTrail](macie-cloudtrail.md "macie-cloudtrail.md").

To retrieve and reveal sensitive data samples for a particular finding, a user must be
allowed to access the following data and resources: the finding, the corresponding
sensitive data discovery result, the affected S3 bucket, and the affected S3 object.
They must also be allowed to use the AWS KMS key that was used to encrypt the
affected object, if applicable, and the AWS KMS key that you configure Macie to use
to encrypt sensitive data samples. If any IAM policies, resource policies, or other
permissions settings deny the requisite access, the user won’t be able to retrieve and
reveal samples for the finding.

To set up this type of configuration, complete the following general tasks:

1. Verify that you configured a repository for your sensitive data discovery
   results.
2. Configure the AWS KMS key to use for encryption of sensitive data
   samples.
3. Verify your permissions for configuring the settings in Macie.
4. Configure and enable the settings in Macie.

For information about performing these tasks, see [Configuring Macie to retrieve sensitive data
samples](findings-retrieve-sd-configure.md "findings-retrieve-sd-configure.md").

## Assuming an IAM role to

access affected S3 objects

To configure Amazon Macie to retrieve sensitive data samples by assuming an IAM role,
start by creating an IAM role that delegates access to Amazon Macie. Ensure that the
trust and permissions policies for the role meet all requirements for Macie to assume
the role. When a user of your Macie account then chooses to retrieve and reveal
sensitive data samples for a finding, Macie assumes the role to retrieve the samples
from the affected S3 object. Macie assumes the role only when a user chooses to retrieve
and reveal samples for a finding. To assume the role, Macie uses the [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") operation of the AWS Security Token Service (AWS STS) API. All the requisite
actions are [logged in AWS CloudTrail](macie-cloudtrail.md "macie-cloudtrail.md").

To retrieve and reveal sensitive data samples for a particular finding, a user must be
allowed to access the finding, the corresponding sensitive data discovery result, and
the AWS KMS key that you configure Macie to use to encrypt sensitive data samples.
The IAM role must allow Macie to access the affected S3 bucket and the affected S3
object. The role must also be allowed to use the AWS KMS key that was used to encrypt
the affected object, if applicable. If any IAM policies, resource policies, or other
permissions settings deny the requisite access, the user won’t be able to retrieve and
reveal samples for the finding.

To set up this type of configuration, complete the following general tasks. If you
have a member account in an organization, work with your Macie administrator to determine
whether and how to configure the settings and resources for your account.

1. Define the following:
   - The name of the IAM role that you want Macie to assume. If your
     account is part of an organization, this name must be same for the
     delegated Macie administrator account and each applicable member account in the
     organization. Otherwise, the Macie administrator won't be able to access
     affected S3 objects for an applicable member account.
   - The name of the IAM permissions policy to attach to the IAM role.
     If your account is part of an organization, we recommend that you use
     the same policy name for each applicable member account in the
     organization. This can streamline provisioning and managing the role in
     member accounts.

2. Verify that you configured a repository for your sensitive data discovery
   results.
3. Configure the AWS KMS key to use for encryption of sensitive data
   samples.
4. Verify your permissions for creating IAM roles and configuring the settings
   in Macie.
5. If you're the delegated Macie administrator for an organization or you have a
   standalone Macie account:
   1. Create and configure the IAM role for your account. Ensure that the
      trust and permissions policies for the role meet all requirements for
      Macie to assume the role. For details about these requirements, see the
      [next topic](#findings-retrieve-sd-options-s3access-role-configuration "#findings-retrieve-sd-options-s3access-role-configuration").
   2. Configure and enable the settings in Macie. Macie then generates an
      external ID for the configuration. If you’re the Macie administrator for an
      organization, note this ID. The trust policy for the IAM role in each
      of your applicable member accounts must specify this ID.

6. If you have a member account in an organization:
   1. Ask your Macie administrator for the external ID to specify in the trust
      policy for the IAM role in your account. Also verify the name of the
      IAM role and permissions policy to create.
   2. Create and configure the IAM role for your account. Ensure that the
      trust and permissions policies for the role meet all requirements for
      your Macie administrator to assume the role. For details about these
      requirements, see the [next topic](#findings-retrieve-sd-options-s3access-role-configuration "#findings-retrieve-sd-options-s3access-role-configuration").
   3. (Optional) If you want to retrieve and reveal sensitive data samples
      from affected S3 objects for your own account, configure and enable the
      settings in Macie. If you want Macie to assume an IAM role to retrieve
      the samples, start by creating and configuring an additional IAM role
      in your account. Ensure that the trust and permissions policies for this
      additional role meet all requirements for Macie to assume the role. Then
      configure the settings in Macie and specify the name of this additional
      role. For details about the policy requirements for the role, see the
      [next topic](#findings-retrieve-sd-options-s3access-role-configuration "#findings-retrieve-sd-options-s3access-role-configuration").

For information about performing these tasks, see [Configuring Macie to retrieve sensitive data
samples](findings-retrieve-sd-configure.md "findings-retrieve-sd-configure.md").

## Configuring

an IAM role to access affected S3 objects

To access affected S3 objects by using an IAM role, start by creating and
configuring a role that delegates access to Amazon Macie. Ensure that the trust and
permissions policies for the role meet all requirements for Macie to assume the role.
How you do this depends on the type of Macie account that you have.

The following sections provide details about the trust and permissions policies to
attach to the IAM role for each type of Macie account. Choose the section for the type
of account that you have.

###### Note

If you have a member account in an organization, you might need to create and
configure two IAM roles for your account:

- To allow your Macie administrator to retrieve and reveal sensitive data samples
  from affected S3 objects for your account, create and configure a role that
  your administrator's account can assume. For these details, choose the
  **Macie member account** section.
- To retrieve and reveal sensitive data samples from affected S3 objects for
  your own account, create and configure a role that Macie can assume. For
  these details, choose the **Standalone Macie account**
  section.
  Before you create and configure either IAM role, work with your Macie administrator to
  determine the appropriate configuration for your account.

For detailed information about using IAM to create the role, see [Creating a role using custom trust policies](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md") in the _AWS Identity and Access Management User Guide_.

If you're the delegated Macie administrator for an organization, start by using the
IAM policy editor to create the permissions policy for the IAM role. The
policy should be as follows.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RetrieveS3Objects",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "AssumeMacieRevealRoleForCrossAccountAccess",
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRole"
 ],
 "Resource": "arn:aws:iam::*:role/`IAMRoleName`"
 }
 ]
}`

```

Where `IAMRoleName` is the name of the IAM role for
Macie to assume when retrieving sensitive data samples from affected S3 objects
for your organization's accounts. Replace this value with the name of the role
that you're creating for your account, and planning to create for applicable
member accounts in your organization. This name must be the same for your
Macie administrator account and each applicable member account.

###### Note

In the preceding permissions policy, the `Resource` element in
the first statement uses a wildcard character (`*`). This allows
an attached IAM entity to retrieve objects from all the S3 buckets that
your organization owns. To allow this access only for specific buckets,
replace the wildcard character with the Amazon Resource Name (ARN) of each
bucket. For example, to allow access only to objects in a bucket named
_amzn-s3-demo-bucket1_,
change the element to:

`"Resource": "arn:aws:s3:::amzn-s3-demo-bucket1/*"`

You can also restrict access to objects in specific S3 buckets for
individual accounts. To do this, specify bucket ARNs in the
`Resource` element of the permissions policy for the IAM
role in each applicable account. For more information and examples, see
[IAM JSON policy elements: Resource](../../../IAM/latest/UserGuide/reference_policies_elements_resource.md "../../../IAM/latest/UserGuide/reference_policies_elements_resource.md") in the _AWS Identity and Access Management User Guide_.

After you create the permissions policy for the IAM role, create and
configure the role. If you do this by using the IAM console, choose
**Custom trust policy** as the **Trusted entity
type** for the role. For the trust policy that defines trusted
entities for the role, specify the following.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowMacieReveal",
 "Effect": "Allow",
 "Principal": {
 "Service": "reveal-samples.macie.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 }
 }
 }
 ]
}`

```

Where `111122223333` is the account ID for
your AWS account. Replace this value with your 12-digit account ID.

In the preceding trust policy:

- The `Principal` element specifies the service principal
  that Macie uses when retrieving sensitive data samples from affected S3
  objects, `reveal-samples.macie.amazonaws.com`.
- The `Action` element specifies the action that the service
  principal is allowed to perform, the [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md")
  operation of the AWS Security Token Service (AWS STS) API.
- The `Condition` element defines a condition that uses the
  [aws:SourceAccount](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context key. This
  condition determines which account can perform the specified action. In
  this case, it allows Macie to assume the role only for the specified
  account. The condition helps prevent Macie from being used as a [confused deputy](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") during transactions with AWS STS.
  After you define the trust policy for the IAM role, attach the permissions
  policy to the role. This should be the permissions policy that you created
  before you started creating the role. Then complete the remaining steps in IAM
  to finish creating and configuring the role. When you finish, [configure and enable the settings
  in Macie](findings-retrieve-sd-configure.md "findings-retrieve-sd-configure.md").

If you have a Macie member account and you want to allow your Macie administrator to
retrieve and reveal sensitive data samples from affected S3 objects for your
account, start by asking your Macie administrator for the following information:

- The name of the IAM role to create. The name must be same for your
  account and the Macie administrator account for your organization.
- The name of the IAM permissions policy to attach to the role.
- The external ID to specify in the trust policy for the role. This ID
  must be the external ID that Macie generated for your Macie
  administrator's configuration.
  After you receive this information, use the IAM policy editor to create the
  permissions policy for the role. The policy should be as follows.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RetrieveS3Objects",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

The preceding permissions policy allows an attached IAM entity to retrieve
objects from all the S3 buckets for your account. This is because the
`Resource` element in the policy uses a wildcard character
(`*`). To allow this access only for specific buckets, replace
the wildcard character with the Amazon Resource Name (ARN) of each bucket. For
example, to allow access only to objects in a bucket named _amzn-s3-demo-bucket2_, change the
element to:

`"Resource": "arn:aws:s3:::amzn-s3-demo-bucket2/*"`

For more information and examples, see [IAM
JSON policy elements: Resource](../../../IAM/latest/UserGuide/reference_policies_elements_resource.md "../../../IAM/latest/UserGuide/reference_policies_elements_resource.md") in the _AWS Identity and Access Management User Guide_.

After you create the permissions policy for the IAM role, create the role.
If you create the role by using the IAM console, choose **Custom trust
policy** as the **Trusted entity type** for the
role. For the trust policy that defines trusted entities for the role, specify
the following.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowMacieAdminRevealRoleForCrossAccountAccess",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`IAMRoleName`"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "sts:ExternalId": "`externalID`",
 "aws:PrincipalOrgID": "${aws:ResourceOrgID}"
 }
 }
 }
 ]
}`

```

In the preceding policy, replace the placeholder values with the correct
values for your AWS environment, where:

- `111122223333` is the 12-digit
  account ID for your Macie administrator's account.
- `IAMRoleName` is the name of the IAM role
  in your Macie administrator's account. It should be the name that you
  received from your Macie administrator.
- `externalID` is the external ID that you
  received from your Macie administrator.
  In general, the trust policy allows your Macie administrator to assume the role to
  retrieve and reveal sensitive data samples from affected S3 objects for your
  account. The `Principal` element specifies the ARN of an IAM role
  in your Macie administrator's account. This is the role that your Macie administrator uses to
  retrieve and reveal sensitive data samples for your organization's accounts. The
  `Condition` block defines two conditions that further determine
  who can assume the role:

- The first condition specifies an external ID that's unique to your
  organization's configuration. To learn more about external IDs, see
  [Access to AWS accounts owned by third parties](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") in the
  _AWS Identity and Access Management User Guide_.
- The second condition uses the [aws:PrincipalOrgID](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgid "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgid") global condition context key. The value
  for the key is a dynamic variable that represents the unique identifier
  for an organization in AWS Organizations (`${aws:ResourceOrgID}`). The
  condition restricts access to only those accounts that are part of the
  same organization in AWS Organizations. If you joined your organization by
  accepting an invitation in Macie, remove this condition from the
  policy.
  After you define the trust policy for the IAM role, attach the permissions
  policy to the role. This should be the permissions policy that you created
  before you started creating the role. Then complete the remaining steps in IAM
  to finish creating and configuring the role. Do not configure and enter settings
  for the role in Macie.

If you have a standalone Macie account or a Macie member account and you want
to retrieve and reveal sensitive data samples from affected S3 objects for your
own account, start by using the IAM policy editor to create the permissions
policy for the IAM role. The policy should be as follows.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RetrieveS3Objects",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

In the preceding permissions policy, the `Resource` element uses a
wildcard character (`*`). This allows an attached IAM entity to
retrieve objects from all the S3 buckets for your account. To allow this access
only for specific buckets, replace the wildcard character with the Amazon
Resource Name (ARN) of each bucket. For example, to allow access only to objects
in a bucket named _amzn-s3-demo-bucket3_, change the element
to:

`"Resource": "arn:aws:s3:::amzn-s3-demo-bucket3/*"`

For more information and examples, see [IAM
JSON policy elements: Resource](../../../IAM/latest/UserGuide/reference_policies_elements_resource.md "../../../IAM/latest/UserGuide/reference_policies_elements_resource.md") in the _AWS Identity and Access Management User Guide_.

After you create the permissions policy for the IAM role, create the role.
If you create the role by using the IAM console, choose **Custom trust
policy** as the **Trusted entity type** for the
role. For the trust policy that defines trusted entities for the role, specify
the following.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowMacieReveal",
 "Effect": "Allow",
 "Principal": {
 "Service": "reveal-samples.macie.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`999999999999`"
 }
 }
 }
 ]
}`

```

Where `999999999999` is the account ID for
your AWS account. Replace this value with your 12-digit account ID.

In the preceding trust policy:

- The `Principal` element specifies the service principal
  that Macie uses when retrieving and revealing sensitive data samples
  from affected S3 objects,
  `reveal-samples.macie.amazonaws.com`.
- The `Action` element specifies the action that the service
  principal is allowed to perform, the [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md")
  operation of the AWS Security Token Service (AWS STS) API.
- The `Condition` element defines a condition that uses the
  [aws:SourceAccount](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context key. This
  condition determines which account can perform the specified action. It
  allows Macie to assume the role only for the specified account. The
  condition helps prevent Macie from being used as a [confused deputy](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") during transactions with AWS STS.
  After you define the trust policy for the IAM role, attach the permissions
  policy to the role. This should be the permissions policy that you created
  before you started creating the role. Then complete the remaining steps in IAM
  to finish creating and configuring the role. When you finish, [configure and enable the settings
  in Macie](findings-retrieve-sd-configure.md "findings-retrieve-sd-configure.md").

## Decrypting affected S3

objects

Amazon S3 supports multiple encryption options for S3 objects. For most of these options,
no additional resources or permissions are required for an IAM user or role to decrypt
and retrieve sensitive data samples from an affected object. This is the case for an
object that's encrypted using server-side encryption with an Amazon S3 managed key or an
AWS managed AWS KMS key.

However, if an S3 object is encrypted with a customer managed AWS KMS key,
additional permissions are required to decrypt and retrieve sensitive data samples from
the object. More specifically, the key policy for the KMS key must allow the IAM
user or role to perform the `kms:Decrypt` action. Otherwise, an error occurs
and Amazon Macie doesn't retrieve any samples from the object. To learn how to provide this
access for an IAM user, see [KMS key access and
permissions](../../../kms/latest/developerguide/control-access.md "../../../kms/latest/developerguide/control-access.md") in the _AWS Key Management Service Developer Guide_.

How to provide this access for an IAM role depends on whether the account that owns
the AWS KMS key also owns the role:

- If the same account owns the KMS key and the role, a user of the account has
  to update the key's policy.
- If one account owns the KMS key and a different account owns the role, a
  user of the account that owns the key has to allow cross-account access to the
  key.

This topic describes how to perform these tasks for an IAM role that you created to
retrieve sensitive data samples from S3 objects. It also provides examples for both
scenarios. For information about allowing access to customer managed AWS KMS keys for
other scenarios, see [KMS key access and
permissions](../../../kms/latest/developerguide/control-access.md "../../../kms/latest/developerguide/control-access.md") in the _AWS Key Management Service Developer Guide_.

### Allowing same-account

access to a customer managed key

If the same account owns both the AWS KMS key and the IAM role, a user of the
account has to add a statement to the key's policy. The additional statement must
allow the IAM role to decrypt data by using the key. For detailed information
about updating a key policy, see [Changing a key
policy](../../../kms/latest/developerguide/key-policy-modifying.md "../../../kms/latest/developerguide/key-policy-modifying.md") in the _AWS Key Management Service Developer Guide_.

In the statement:

- The `Principal` element must specify the Amazon Resource Name
  (ARN) of the IAM role.
- The `Action` array must specify the `kms:Decrypt`
  action. This is the only AWS KMS action that the IAM role must be allowed to
  perform to decrypt an object that's encrypted with the key.

The following is an example of the statement to add to the policy for a KMS key.

```
{
    "Sid": "Allow the Macie reveal role to use the key",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::`123456789012`:role/`IAMRoleName`"
    },
    "Action": [
        "kms:Decrypt"
    ],
    "Resource": "*"
}
```

In the preceding example:

- The `AWS` field in the `Principal` element
  specifies the ARN of the IAM role in the account. It allows the role to
  perform the action specified by the policy statement.
  `123456789012` is an example account
  ID. Replace this value with the account ID for the account that owns the
  role and the KMS key. `IAMRoleName` is an example
  name. Replace this value with the name of the IAM role in the
  account.
- The `Action` array specifies the action that the IAM role is
  allowed to perform using the KMS key—decrypt ciphertext that's
  encrypted with the key.

Where you add this statement to a key policy depends on the structure and elements
that the policy currently contains. When you add the statement, ensure that the
syntax is valid. Key policies use JSON format. This means that you have to also add
a comma before or after the statement, depending on where you add the statement to
the policy.

### Allowing

cross-account access to a customer managed key

If one account owns the AWS KMS key (_key
owner_) and a different account owns the IAM role (_role owner_), the key owner has to provide the role
owner with cross-account access to the key. One way to do this is by using a grant.
A _grant_ is a policy instrument that allows AWS
principals to use KMS keys in cryptographic operations if the conditions specified
by the grant are met. To learn about grants, see [Grants in AWS KMS](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") in the
_AWS Key Management Service Developer Guide_.

With this approach, the key owner first ensures that the key's policy allows the
role owner to create a grant for the key. The role owner then creates a grant for
the key. The grant delegates the relevant permissions to the IAM role in their
account. It allows the role to decrypt S3 objects that are encrypted with the
key.

###### Step 1: Update the key policy

In the key policy, the key owner should ensure that the policy includes a
statement that allows the role owner to create a grant for the IAM role in
their (the role owner's) account. In this statement, the `Principal`
element must specify the ARN of the role owner's account. The
`Action` array must specify the `kms:CreateGrant`
action. A `Condition` block can filter access to the specified
action. The following is an example of this statement in the policy for a
KMS key.

```
{
    "Sid": "Allow a role in an account to create a grant",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::`111122223333`:root"
    },
    "Action": [
        "kms:CreateGrant"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:GranteePrincipal": "arn:aws:iam::`111122223333`:role/`IAMRoleName`"
        },
        "ForAllValues:StringEquals": {
            "kms:GrantOperations": "Decrypt"
        }
    }
}
```

In the preceding example:

- The `AWS` field in the `Principal` element specifies
  the ARN of the role owner's account. It allows the account to perform the
  action specified by the policy statement.
  `111122223333` is an example account
  ID. Replace this value with the account ID for the role owner's
  account.
- The `Action` array specifies the action that the role owner is
  allowed to perform on the KMS key—create a grant for the
  key.
- The `Condition` block uses [condition operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md") and the following condition keys to filter
  access to the action that the role owner is allowed to perform on the
  KMS key:
  - [kms:GranteePrincipal](../../../kms/latest/developerguide/conditions-kms.md#conditions-kms-grantee-principal "../../../kms/latest/developerguide/conditions-kms.md#conditions-kms-grantee-principal") – This condition allows the
    role owner to create a grant only for the specified grantee
    principal, which is the ARN of the IAM role in their account. In
    that ARN, `111122223333` is an
    example account ID. Replace this value with the account ID for the
    role owner's account. `IAMRoleName` is an
    example name. Replace this value with the name of the IAM role in
    the role owner's account.
  - [kms:GrantOperations](../../../kms/latest/developerguide/conditions-kms.md#conditions-kms-grant-operations "../../../kms/latest/developerguide/conditions-kms.md#conditions-kms-grant-operations") – This condition allows the
    role owner to create a grant only to delegate permission to perform
    the AWS KMS `Decrypt` action (decrypt ciphertext that's
    encrypted with the key). It prevents the role owner from creating
    grants that delegate permissions to perform other actions on the
    KMS key. The `Decrypt` action is the only AWS KMS action
    that the IAM role must be allowed to perform to decrypt an object
    that's encrypted with the key.

Where the key owner adds this statement to the key policy depends on the structure
and elements that the policy currently contains. When the key owner adds the
statement, they should ensure that the syntax is valid. Key policies use JSON
format. This means that the key owner has to also add a comma before or after the
statement, depending on where they add the statement to the policy. For detailed
information about updating a key policy, see [Changing a key
policy](../../../kms/latest/developerguide/key-policy-modifying.md "../../../kms/latest/developerguide/key-policy-modifying.md") in the _AWS Key Management Service Developer Guide_.

###### Step 2: Create a grant

After the key owner updates the key policy as necessary, the role owner
creates a grant for the key. The grant delegates the relevant permissions to the
IAM role in their (the role owner's) account. Before the role owner creates
the grant, they should verify that they're allowed to perform the
`kms:CreateGrant` action. This action allows them to add a grant
to an existing, customer managed AWS KMS key.

To create the grant, the role owner can use the [CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") operation
of the AWS Key Management Service API. When the role owner creates the grant, they should specify the
following values for the required parameters:

- `KeyId` – The ARN of the KMS key. For cross-account
  access to a KMS key, this value must be an ARN. It can't be a key
  ID.
- `GranteePrincipal` – The ARN of the IAM role in their
  account. This value should be
  `arn:aws:iam::`111122223333`:role/`IAMRoleName``,
where `111122223333`is the account ID
for the role owner's account and`IAMRoleName` is
  the name of the role.
- `Operations` – The AWS KMS decrypt action
  (`Decrypt`). This is the only AWS KMS action that the IAM
  role must be allowed to perform to decrypt an object that's encrypted with
  the KMS key.

If the role owner is using the AWS Command Line Interface (AWS CLI), they can run the [create-grant](../../../cli/latest/reference/kms/create-grant.md "../../../cli/latest/reference/kms/create-grant.md") command to create the grant. The following example shows
how. The example is formatted for Microsoft Windows and it uses the caret (^)
line-continuation character to improve readability.

```
`C:\>` `aws kms create-grant ^
--key-id `arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab` ^
--grantee-principal `arn:aws:iam::111122223333:role/`IAMRoleName`` ^
--operations "Decrypt"`
```

Where:

- `key-id` specifies the ARN of the KMS key to apply the grant
  to.
- `grantee-principal` specifies the ARN of the IAM role that's
  allowed to perform the action specified by the grant. This value should
  match the ARN specified by the `kms:GranteePrincipal` condition
  in the key policy.
- `operations` specifies the action that the grant allows the
  specified principal to perform—decrypt ciphertext that's encrypted
  with the key.

If the command runs successfully, you receive output similar to the
following.

```
`{
 "GrantToken": "<grant token>",
 "GrantId": "1a2b3c4d2f5e69f440bae30eaec9570bb1fb7358824f9ddfa1aa5a0dab1a59b2"
}`
```

Where `GrantToken` is a unique, non-secret, variable-length,
base64-encoded string that represents the grant that was created, and
`GrantId` is the unique identifier for the grant.
