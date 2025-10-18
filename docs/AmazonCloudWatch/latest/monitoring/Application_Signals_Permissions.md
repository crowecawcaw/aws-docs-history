# Permissions required for Application
 Signals

This section explains the permissions necessary for you to enable, manage, and operate
 Application Signals.


## Permissions to enable and
 manage Application Signals


To manage Application Signals, you must be signed on with the required permissions. To view the contents of the **CloudWatchApplicationSignalsFullAccess** policy, see [CloudWatchApplicationSignalsFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchApplicationSignalsFullAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchApplicationSignalsFullAccess.html"). 



To enable Application Signals on Amazon EC2, or custom
 architectures, see [Enable Application Signals on Amazon EC2](CloudWatch-Application-Signals-Enable-EC2Main.md "CloudWatch-Application-Signals-Enable-EC2Main.md"). To enable and manage
 Application Signals on Amazon EKS using the [Amazon CloudWatch Observability EKS
 add-on](install-CloudWatch-Observability-EKS-addon.md "install-CloudWatch-Observability-EKS-addon.md"), you need the following permissions.


###### Important

These permissions include `iam:PassRole` with `Resource "*”`
 and `eks:CreateAddon` with `Resource “*”`. These are powerful
 permissions and you should use caution in granting them.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "CloudWatchApplicationSignalsEksAddonManagementPermissions",
 "Effect": "Allow",
 "Action": [
 "eks:AccessKubernetesApi",
 "eks:CreateAddon",
 "eks:DescribeAddon",
 "eks:DescribeAddonConfiguration",
 "eks:DescribeAddonVersions",
 "eks:DescribeCluster",
 "eks:DescribeUpdate",
 "eks:ListAddons",
 "eks:ListClusters",
 "eks:ListUpdates",
 "iam:ListRoles",
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "eks.amazonaws.com",
 "application-signals.cloudwatch.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "CloudWatchApplicationSignalsEksCloudWatchObservabilityAddonManagementPermissions",
 "Effect": "Allow",
 "Action": [
 "eks:DeleteAddon",
 "eks:UpdateAddon"
 ],
 "Resource": "arn:aws:eks:*:*:addon/*/amazon-cloudwatch-observability/*"
 }
 ]
 }`

```





The Application Signals dashboard shows the AWS Service Catalog AppRegistry
 applications that your SLOs are associated with. To see these applications in the SLO
 pages, you must have the following permissions:



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "CloudWatchApplicationSignalsTaggingReadPermissions",
 "Effect": "Allow",
 "Action": "tag:GetResources",
 "Resource": "*"
 }
 ]
}`

```





## Operating Application
 Signals


Service operators who are using Application Signals to monitor services and SLOs must
 be signed on to an account with read only permissions. To view the contents of the **CloudWatchApplicationSignalsReadOnlyAccess** policy, 
 see [CloudWatchApplicationSignalsReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchApplicationSignalsReadOnlyAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchApplicationSignalsReadOnlyAccess.html").


To see which AWS Service Catalog AppRegistry Applications that your SLOs are
 associated within the Application Signals dashboard, you must have the following
 permissions:



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "CloudWatchApplicationSignalsTaggingReadPermissions",
 "Effect": "Allow",
 "Action": "tag:GetResources",
 "Resource": "*"
 }
 ]
}`

```





To check if Application Signals on Amazon EKS using the [Amazon CloudWatch Observability EKS
 add-on](install-CloudWatch-Observability-EKS-addon.md "install-CloudWatch-Observability-EKS-addon.md") is enabled, you need to have the following permissions:



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "CloudWatchApplicationSignalsEksReadPermissions",
 "Effect": "Allow",
 "Action": [
 "eks:ListAddons",
 "eks:ListClusters"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CloudWatchApplicationSignalsEksDescribeAddonReadPermissions",
 "Effect": "Allow",
 "Action": [
 "eks:DescribeAddon"
 ],
 "Resource": "arn:aws:eks:*:*:addon/*/amazon-cloudwatch-observability/*"
 }
 ]
}`

```
