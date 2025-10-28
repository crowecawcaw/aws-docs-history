# AWS Service Catalog deployment errors

For AWS Service Catalog deployments completed prior to February 7, 2022,
perform the following steps to remove the
`AmazonLambdaRolePolicyForLaunchWizardSAP` policy from the
`AmazonLambdaRoleForLaunchWizard` role, and add a new inline policy.
Deployments completed after February 7, 2022 do not require you to perform these
steps.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Roles** from the left navigation pane.
3. Search for the `AmazonLambdaRoleForLaunchWizard`. Select the policy
   to view the attached permissions.
4. Check whether the `AmazonLambdaRolePolicyForLaunchWizardSAP` policy
   is attached to this role. If it is attached, remove the policy by selecting the
   check box next to it, and choose **Remove**.
5. Add the following inline policy by choosing **Add
   permissions**>**Create inline policy**, and
   entering the policy in the **JSON** tab of the **Create
   policy** wizard.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:GetParameter"
 ],
 "Resource": "arn:aws:ssm:*::parameter/LaunchWizard*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:GetDocument",
 "ssm:sendCommand"
 ],
 "Resource": "arn:aws:ssm:*::document/AWS-RunShellScript"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:SendCommand"
 ],
 "Resource": [
 "arn:aws:ec2:*:`111122223333`:instance/*"
 ],
 "Condition": {
 "StringLike": {
 "ssm:resourceTag/LaunchWizardApplicationType": "*"
 }
 }
 }
 ]
}`

```

6. Choose **Review policy**, enter a name for the policy, and
   choose **Create policy**.
