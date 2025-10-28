# The

difference between explicit and implicit denies

A request results in an explicit deny if an applicable policy includes a `Deny`
statement. If policies that apply to a request include an `Allow` statement and a
`Deny` statement, the `Deny` statement trumps the
`Allow` statement. The request is explicitly denied.

An implicit denial occurs when there is no applicable `Deny` statement but also
no applicable `Allow` statement. Because an IAM principal is denied access by
default, they must be explicitly allowed to perform an action. Otherwise, they are
implicitly denied access.

When you design your authorization strategy, you must create policies with
`Allow` statements to allow your principals to successfully make requests.
However, you can choose any combination of explicit and implicit denies.

For example, you can create the following policy that includes allowed actions, implicitly
denied actions, and explicitly denied actions. The `AllowGetList` statement
**allows** read-only access to IAM actions that begin
with the prefixes `Get` and `List`. All other actions in IAM, such
as `iam:CreatePolicy` are **implicitly denied**. The
`DenyReports` statement **explicitly denies**
access to IAM reports by denying access to actions that include the `Report`
suffix, such as `iam:GetOrganizationsAccessReport`. If someone adds another
policy to this principal to grant them access to IAM reports, such as
`iam:GenerateCredentialReport`, report-related requests are still denied
because of this explicit deny.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowGetList",
 "Effect": "Allow",
 "Action": [
 "iam:Get*",
 "iam:List*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "DenyReports",
 "Effect": "Deny",
 "Action": "iam:*Report",
 "Resource": "*"
 }
 ]
}`

```
