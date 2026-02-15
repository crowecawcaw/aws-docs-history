# Permissions required to track

seller issued license usage in License Manager

To get started with this feature, you need permission to call the following License Manager API
actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "license-manager:CreateLicense",
 "license-manager:CreateLicenseVersion",
 "license-manager:ListLicenses",
 "license-manager:ListLicenseVersions",
 "license-manager:GetLicense",
 "license-manager:DeleteLicense",
 "license-manager:CheckoutLicense",
 "license-manager:CheckInLicense",
 "license-manager:ExtendLicenseConsumption",
 "license-manager:GetLicenseUsage",
 "license-manager:CreateGrant",
 "license-manager:CreateGrantVersion",
 "license-manager:DeleteGrant",
 "license-manager:GetGrant",
 "license-manager:ListDistributedGrants"
 ],
 "Resource": "*"
 }
 ]
}`

```

If you will integrate with License Manager so customers without an AWS account can consume
licenses sold outside of AWS Marketplace, you must create an IAM role that enables your software
application to call the License Manager API.

If you use the AWS Management Console to distribute temporary credentials for customers without an
AWS account, License Manager will automatically create the
`AWSLicenseManagerConsumptionRole` on your behalf. For more
information, see [Get temporary credentials for ISV customers
without an AWS account](granting-temporary-credentials.md "granting-temporary-credentials.md"). To create this role from the AWS CLI,
use the AWS IAM [create-role](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-role.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-role.html")
command, as shown in the following example.

```
aws iam create-role
    --role-name AWSLicenseManagerConsumptionRole
    --description "Role used to consume licenses using AWS License Manager"
    --max-session-duration 3600
    --assume-role-policy-document file://trust-policy-document.json
```

The provided `trust-policy-document.json` file should look like the
following example, with your own AWS account ID substituted as the token issuer account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Federated": "openid-license-manager.amazonaws.com"
 },
 "Action": "sts:AssumeRoleWithWebIdentity",
 "Condition": {
 "ForAnyValue:StringLike": {
 "openid-license-manager.amazonaws.com:amr": "aws:license-manager:token-issuer-123456789012:`123456789012`"
 }
 }
 }
 ]
}`

```

Next, use the [attach-role-policy](../../../cli/latest/reference/iam/attach-role-policy.md "../../../cli/latest/reference/iam/attach-role-policy.md") command to add the
**AWSLicenseManagerConsumptionPolicy** AWS managed policy to the
**AWSLicenseManagerConsumptionRole** role.

```
aws iam attach-role-policy
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSLicenseManagerConsumptionPolicy
    --role-name AWSLicenseManagerConsumptionRole
```
