# Using IAM condition keys for AWS Artifact reports

You can use IAM condition keys to provide fine-grained access to reports on AWS Artifact, based on specific
report categories and series.

The following example policies show permissions that you can assign to IAM users
based on specific report categories and series.

###### Example policies to manage AWS reports read access

AWS Artifact reports are denoted by the IAM resource,
`report`.

The following policy grants permission to read all AWS Artifact reports under the
`Certifications and Attestations` category.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:ListReports"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "artifact:GetReport",
 "artifact:GetReportMetadata",
 "artifact:GetTermForReport"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "artifact:ReportCategory": "Certifications and Attestations"
 }
 }
 }
 ]
}`

```

The following policy lets you grant permission to read all AWS Artifact reports under the
`SOC` series.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:ListReports"
 ],
 "Resource": "*"
 },{
 "Effect": "Allow",
 "Action": [
 "artifact:GetReport",
 "artifact:GetReportMetadata",
 "artifact:GetTermForReport"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "artifact:ReportSeries": "SOC",
 "artifact:ReportCategory": "Certifications and Attestations"
 }
 }
 }
 ]
}`

```

The following policy lets you grant permission to read all AWS Artifact reports under the
`Certifications and Attestations` category, and `SOC` series.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:ListReports"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "artifact:GetReport",
 "artifact:GetReportMetadata",
 "artifact:GetTermForReport"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "artifact:ReportSeries": "SOC",
 "artifact:ReportCategory": "Certifications and Attestations"
 }
 }
 }
 ]
}`

```
