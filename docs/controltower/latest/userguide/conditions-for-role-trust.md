# Optional conditions for your role trust

relationships

To add additional layers of security to your AWS Control Tower environment, you can impose conditions in your role trust policies, to restrict the accounts and
resources that interact with certain roles in AWS Control Tower. For example, you can further
restrict access to the `AWSControlTowerAdmin` role, because it allows wide
access permissions.

To help prevent a threat actor from gaining access to your resources, manually edit your
AWS Control Tower trust policy to add at least one `aws:SourceArn` or
`aws:SourceAccount` conditional to the policy statement. As an additional security
best practice, you can add the `aws:SourceArn` condition,
because it is more specific than `aws:SourceAccount`, limiting access to a
specific account and a specific resource.

If you don't know the full ARN of the resource, or if you are specifying multiple
resources, you can use the `aws:SourceArn` condition with wildcards (\*) for
the unknown portions of the ARN. For example,
`arn:aws:controltower:*:123456789012:*` works if you don't wish to
specify a Region.

The following example demonstrates the use of the `aws:SourceArn` IAM
condition with your IAM role trust polices. Add the condition in your trust
relationship for the **AWSControlTowerAdmin** role, because the
AWS Control Tower service principal interacts with it.

As shown in the example, the source ARN is of the format:
`arn:aws:controltower:`${HOME_REGION}`:`${CUSTOMER_AWSACCOUNT_id}`:*`

Replace the strings `${HOME_REGION}` and
`${CUSTOMER_AWSACCOUNT_id}` with your own home Region and account ID of
the calling account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "controltower.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:controltower:us-west-2:012345678901:*"
 }
 }
 }
 ]
}`

```

In the example, the Source ARN designated as
`arn:aws:controltower:us-west-2:012345678901:*` is the only ARN allowed
to perform the `sts:AssumeRole` action. In other words, only users who can
sign in to the account ID `012345678901`, in the `us-west-2`
Region, are allowed to perform actions that require this specific role and trust
relationship for the AWS Control Tower service, designated as
`controltower.amazonaws.com`.

The next example shows the `aws:SourceAccount` and
`aws:SourceArn` conditions applied to the role trust policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "controltower.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "012345678901"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:controltower:us-west-2:012345678901:*"
 }
 }
 }
 ]
}`

```

The example illustrates the `aws:SourceArn` condition statement, with an
added `aws:SourceAccount` condition statement. For more information, see
[Prevent cross-service impersonation](prevent-confused-deputy.md "prevent-confused-deputy.md").

For general information about permission policies in AWS Control Tower see [Manage access to
resources](access-control-manage-access-intro.md "access-control-manage-access-intro.md").

**Recommendations:**

We recommend that you add conditions to the roles that AWS Control Tower creates, because those
roles are directly assumed by other AWS services. For more information, see the example
for **AWSControlTowerAdmin**, shown previously in this section. For the
AWS Config recorder role, we recommend adding the `aws:SourceArn` condition,
specifying the Config recorder ARN as the permitted source ARN.

For roles such as **AWSControlTowerExecution** or the [other programmatic roles that can be assumed](roles-how.md "roles-how.md") by the AWS Control Tower Audit
account in all managed accounts, we recommend that you add the
`aws:PrincipalOrgID` condition to the trust policy for these roles, which
validates that the principal accessing the resource belongs to an account in the correct
AWS organization. Do not add the `aws:SourceArn` condition statement,
because it will not work as expected.

###### Note

In case of drift, it is possible that an AWS Control Tower role may be reset under certain
circumstances. It is recommended that you re-check the roles periodically, if you
have customized them.
