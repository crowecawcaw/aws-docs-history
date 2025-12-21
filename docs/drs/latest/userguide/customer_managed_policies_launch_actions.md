# Launch Actions Policy -

AWSElasticDisasterRecoveryLaunchActionsPolicy

This policy allows you to use Amazon SSM and additional services required permissions to run
post-launch actions in AWS Elastic Disaster Recovery (AWS DRS). Attach this policy to your IAM roles or users.

**Permissions details**

This policy includes the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "LaunchActionsPolicy1",
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeInstanceInformation"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": [
 "drs.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "LaunchActionsPolicy2",
 "Effect": "Allow",
 "Action": [
 "ssm:SendCommand",
 "ssm:StartAutomationExecution"
 ],
 "Resource": [
 "arn:aws:ssm:*:*:document/*",
 "arn:aws:ssm:*:*:automation-execution/*"
 ],
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": [
 "drs.amazonaws.com"
 ]
 },
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "LaunchActionsPolicy3",
 "Effect": "Allow",
 "Action": [
 "ssm:SendCommand",
 "ssm:StartAutomationExecution"
 ],
 "Resource": [
 "arn:aws:ssm:*::document/AWS-*",
 "arn:aws:ssm:*::document/AWSCodeDeployAgent-*",
 "arn:aws:ssm:*::document/AWSConfigRemediation-*",
 "arn:aws:ssm:*::document/AWSConformancePacks-*",
 "arn:aws:ssm:*::document/AWSDisasterRecovery-*",
 "arn:aws:ssm:*::document/AWSDistroOTel-*",
 "arn:aws:ssm:*::document/AWSDocs-*",
 "arn:aws:ssm:*::document/AWSEC2-*",
 "arn:aws:ssm:*::document/AWSEC2Launch-*",
 "arn:aws:ssm:*::document/AWSFIS-*",
 "arn:aws:ssm:*::document/AWSFleetManager-*",
 "arn:aws:ssm:*::document/AWSIncidents-*",
 "arn:aws:ssm:*::document/AWSKinesisTap-*",
 "arn:aws:ssm:*::document/AWSMigration-*",
 "arn:aws:ssm:*::document/AWSNVMe-*",
 "arn:aws:ssm:*::document/AWSNitroEnclavesWindows-*",
 "arn:aws:ssm:*::document/AWSObservabilityExporter-*",
 "arn:aws:ssm:*::document/AWSPVDriver-*",
 "arn:aws:ssm:*::document/AWSQuickSetupType-*",
 "arn:aws:ssm:*::document/AWSQuickStarts-*",
 "arn:aws:ssm:*::document/AWSRefactorSpaces-*",
 "arn:aws:ssm:*::document/AWSResilienceHub-*",
 "arn:aws:ssm:*::document/AWSSAP-*",
 "arn:aws:ssm:*::document/AWSSAPTools-*",
 "arn:aws:ssm:*::document/AWSSQLServer-*",
 "arn:aws:ssm:*::document/AWSSSO-*",
 "arn:aws:ssm:*::document/AWSSupport-*",
 "arn:aws:ssm:*::document/AWSSystemsManagerSAP-*",
 "arn:aws:ssm:*::document/AmazonCloudWatch-*",
 "arn:aws:ssm:*::document/AmazonCloudWatchAgent-*",
 "arn:aws:ssm:*::document/AmazonECS-*",
 "arn:aws:ssm:*::document/AmazonEFSUtils-*",
 "arn:aws:ssm:*::document/AmazonEKS-*",
 "arn:aws:ssm:*::document/AmazonInspector-*",
 "arn:aws:ssm:*::document/AmazonInspector2-*",
 "arn:aws:ssm:*::document/AmazonInternal-*",
 "arn:aws:ssm:*::document/AwsEnaNetworkDriver-*",
 "arn:aws:ssm:*::document/AwsVssComponents-*",
 "arn:aws:ssm:*:*:automation-execution/*"
 ],
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": [
 "drs.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "LaunchActionsPolicy4",
 "Effect": "Allow",
 "Action": [
 "ssm:SendCommand"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:instance/*"
 ],
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": [
 "drs.amazonaws.com"
 ]
 },
 "Null": {
 "aws:ResourceTag/AWSElasticDisasterRecoveryManaged": "false"
 }
 }
 },
 {
 "Sid": "LaunchActionsPolicy5",
 "Effect": "Allow",
 "Action": [
 "ssm:SendCommand"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:instance/*"
 ],
 "Condition": {
 "StringEquals": {
 "ec2:ResourceTag/AWSDRS": "AllowLaunchingIntoThisInstance"
 },
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": [
 "drs.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "LaunchActionsPolicy6",
 "Effect": "Allow",
 "Action": [
 "ssm:ListDocuments",
 "ssm:ListCommandInvocations"
 ],
 "Resource": "*"
 },
 {
 "Sid": "LaunchActionsPolicy7",
 "Effect": "Allow",
 "Action": [
 "ssm:ListDocumentVersions",
 "ssm:GetDocument",
 "ssm:DescribeDocument"
 ],
 "Resource": "arn:aws:ssm:*:*:document/*"
 },
 {
 "Sid": "LaunchActionsPolicy8",
 "Effect": "Allow",
 "Action": [
 "ssm:GetAutomationExecution"
 ],
 "Resource": "arn:aws:ssm:*:*:automation-execution/*",
 "Condition": {
 "Null": {
 "aws:ResourceTag/AWSElasticDisasterRecoveryManaged": "false"
 }
 }
 },
 {
 "Sid": "LaunchActionsPolicy9",
 "Effect": "Allow",
 "Action": [
 "ssm:GetParameters"
 ],
 "Resource": "arn:aws:ssm:*:*:parameter/ManagedByAWSElasticDisasterRecoveryService-*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": "ssm.amazonaws.com"
 }
 }
 },
 {
 "Sid": "LaunchActionsPolicy10",
 "Effect": "Allow",
 "Action": [
 "ssm:GetParameter",
 "ssm:PutParameter"
 ],
 "Resource": "arn:aws:ssm:*:*:parameter/ManagedByAWSElasticDisasterRecoveryService-*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "LaunchActionsPolicy11",
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": [
 "arn:aws:iam::*:role/service-role/AWSElasticDisasterRecoveryRecoveryInstanceWithLaunchActionsRole"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "ec2.amazonaws.com"
 },
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": "drs.amazonaws.com"
 }
 }
 }
 ]
}`

```
