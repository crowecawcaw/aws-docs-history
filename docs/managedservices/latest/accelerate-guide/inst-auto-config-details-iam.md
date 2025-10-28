# IAM permissions change details

Each managed instance must have an AWS Identity and Access Management role that includes the following managed policies:

- arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
- arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy
- arn:aws:iam::aws:policy/AMSInstanceProfileBasePolicy
  The first two are AWS-managed policies. The AMS-managed policy is:

**AMSInstanceProfileBasePolicy**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "secretsmanager:CreateSecret",
 "secretsmanager:UpdateSecret"
 ],
 "Resource": [
 "arn:aws:secretsmanager:*:*:secret:/ams/byoa/*"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "kms:Encrypt"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

If your instance already has an attached IAM role, but is missing any of these policies, then AMS
adds the missing policies to your IAM role. If your instance doesn't have an IAM role, then AMS
attaches the **AMSOSConfigurationCustomerInstanceProfile** IAM role. The **AMSOSConfigurationCustomerInstanceProfile** IAM role
has all policies that are required by AMS Accelerate.

###### Note

If the default instance profile limit of 10 is reached, then AMS increases the limit to 20, so that the required instance profiles can be attached.
