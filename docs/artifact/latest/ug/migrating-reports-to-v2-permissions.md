# Migrating reports to fine-grained permissions for AWS Artifact

You can now use fine-grained permissions for AWS Artifact. Through these fine-grained permissions, you have granular control on providing access to features such as accepting terms and downloading reports.

To access reports through the fine-grained permissions, you can utilize the
[AWSArtifactReportsReadOnlyAccess](security-iam-awsmanpol.md "security-iam-awsmanpol.md") Managed Policy or update your permissions as per the below recommendation.

###### Note

The IAM action `artifact:Get` was deprecated in the AWS partition on March 3, 2025 and in the AWS GovCloud (US) partition on July 1, 2025.

## Migrating reports to new permissions

**Migrate non-resource specific permissions**

Replace your existing policy containing legacy permissions with a policy containing
fine-grained permissions.

Legacy policy:

AWS

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "artifact:Get"
 ],
 "Resource": [
 "arn:aws:artifact:::report-package/*"
 ]
 }]
}`

```

AWS GovCloud (US)

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "artifact:Get"
 ],
 "Resource": [
 "arn:aws-us-gov:artifact:::report-package/*"
 ]
 }]
}`

```

New policy with fine-grained permissions:

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "artifact:ListReports",
 "artifact:GetReportMetadata",
 "artifact:GetReport",
 "artifact:GetTermForReport"
 ],
 "Resource": "*"
 }]
}`

```

**Migrate resource-specific permissions**

Replace your existing policy containing legacy permissions with a policy containing
fine-grained permissions. Report resource wildcard permissions have been replaced with
[condition
keys](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md").

Legacy policy:

AWS

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "artifact:Get"
 ],
 "Resource": [
 "arn:aws:artifact:::report-package/Certifications and Attestations/SOC/*",
 "arn:aws:artifact:::report-package/Certifications and Attestations/PCI/*",
 "arn:aws:artifact:::report-package/Certifications and Attestations/ISO/*"
 ]
 }]
}`

```

AWS GovCloud (US)

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "artifact:Get"
 ],
 "Resource": [
 "arn:aws-us-gov:artifact:::report-package/Certifications and Attestations/SOC/*",
 "arn:aws-us-gov:artifact:::report-package/Certifications and Attestations/PCI/*",
 "arn:aws-us-gov:artifact:::report-package/Certifications and Attestations/ISO/*"
 ]
 }]
}`

```

New policy with fine-grained permissions and [condition
keys](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md"):

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "artifact:ListReports"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "artifact:GetReportMetadata",
 "artifact:GetReport",
 "artifact:GetTermForReport"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "artifact:ReportSeries": [
 "SOC",
 "PCI",
 "ISO"
 ],
 "artifact:ReportCategory": [
 "Certifications and Attestations"
 ]
 }
 }
 }
 ]
}`

```
