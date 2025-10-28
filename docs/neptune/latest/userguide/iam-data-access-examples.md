# Creating IAM data-access policies in Amazon Neptune

The following examples show how to create custom IAM policies that use fine-grained
access control of data-plane APIs and actions, introduced in Neptune [engine release version 1.2.0.0](engine-releases-1.2.0.md "engine-releases-1.2.0.md").

## Policy example allowing

unrestricted access to the data in a Neptune DB cluster

The following example policy allows an IAM user to connect to a Neptune DB cluster
using IAM database authentication, and uses the "`*`" character to match
all available actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "neptune-db:*",
 "Resource": "arn:aws:neptune-db:`us-east-1`:`123456789012`:`cluster-ABCD1234EFGH5678IJKL90MNOP`/*"
 }
 ]
}`

```

The preceding example includes a resource ARN in a format that is particular to
Neptune IAM authentication. To construct the ARN, see [Specifying data resources](iam-data-resources.md "iam-data-resources.md"). Note that the ARN used
for an IAM authorization `Resource` is not the same as the ARN assigned
to the cluster on creation.

## Policy example allowing

read-only access to a Neptune DB cluster

The following policy grants permission for full read-only access to data in
a Neptune DB cluster:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect": "Allow",
 "Action": [
 "neptune-db:Read*",
 "neptune-db:Get*",
 "neptune-db:List*"
 ],
 "Resource": "arn:aws:neptune-db:`us-east-1`:`123456789012`:`cluster-ABCD1234EFGH5678IJKL90MNOP`/*"
 }
 ]
}`

```

## Policy example denying all access to a Neptune DB cluster

The default IAM action is to deny access to a DB cluster unless an `Allow`
_Effect_ is granted. However, the following policy
denies all access to a DB cluster for a particular AWS account and Region, which
then takes precedence over any `Allow` effect.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "neptune-db:*",
 "Resource": "arn:aws:neptune-db:`us-east-1`:`123456789012`:`cluster-ABCD1234EFGH5678IJKL90MNOP`/*"
 }
 ]
}`

```

## Policy example granting read access through queries

The following policy only grants permission to read from a Neptune DB cluster
using a query:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "neptune-db:ReadDataViaQuery",
 "Resource": "arn:aws:neptune-db:`us-east-1`:`123456789012`:`cluster-ABCD1234EFGH5678IJKL90MNOP`/*"
 }
 ]
}`

```

## Policy example that only allows Gremlin queries

The following policy uses the `neptune-db:QueryLanguage` condition key to grant
permission to query Neptune only using the Gremlin query language:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "neptune-db:ReadDataViaQuery",
 "neptune-db:WriteDataViaQuery",
 "neptune-db:DeleteDataViaQuery"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "neptune-db:QueryLanguage": "Gremlin"
 }
 }
 }
 ]
}`

```

## Policy example allowing all access except to Neptune ML model management

The following policy grants full access to Neptune graph operations except for
the Neptune ML model-management features:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect": "Allow",
 "Action": [
 "neptune-db:CancelLoaderJob",
 "neptune-db:CancelQuery",
 "neptune-db:DeleteDataViaQuery",
 "neptune-db:DeleteStatistics",
 "neptune-db:GetEngineStatus",
 "neptune-db:GetLoaderJobStatus",
 "neptune-db:GetQueryStatus",
 "neptune-db:GetStatisticsStatus",
 "neptune-db:GetStreamRecords",
 "neptune-db:ListLoaderJobs",
 "neptune-db:ManageStatistics",
 "neptune-db:ReadDataViaQuery",
 "neptune-db:ResetDatabase",
 "neptune-db:StartLoaderJob",
 "neptune-db:WriteDataViaQuery"
 ],
 "Resource": "arn:aws:neptune-db:`us-east-1`:`123456789012`:`cluster-ABCD1234EFGH5678IJKL90MNOP`/*"
 }
 ]
}`

```

## Policy example allowing access to Neptune ML model management

This policy grants access to the Neptune ML model-management features:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect": "Allow",
 "Action": [
 "neptune-db:CancelMLDataProcessingJob",
 "neptune-db:CancelMLModelTrainingJob",
 "neptune-db:CancelMLModelTransformJob",
 "neptune-db:CreateMLEndpoint",
 "neptune-db:DeleteMLEndpoint",
 "neptune-db:GetMLDataProcessingJobStatus",
 "neptune-db:GetMLEndpointStatus",
 "neptune-db:GetMLModelTrainingJobStatus",
 "neptune-db:GetMLModelTransformJobStatus",
 "neptune-db:ListMLDataProcessingJobs",
 "neptune-db:ListMLEndpoints",
 "neptune-db:ListMLModelTrainingJobs",
 "neptune-db:ListMLModelTransformJobs",
 "neptune-db:StartMLDataProcessingJob",
 "neptune-db:StartMLModelTrainingJob",
 "neptune-db:StartMLModelTransformJob"
 ],
 "Resource": "arn:aws:neptune-db:`us-east-1`:`123456789012`:`cluster-ABCD1234EFGH5678IJKL90MNOP`/*"
 }
 ]
}`

```

## Policy example granting full query access

The following policy grants full access to Neptune graph query operations, but not
to features like fast reset, streams, the bulk loader, Neptune ML model management, and
so forth:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect": "Allow",
 "Action": [
 "neptune-db:ReadDataViaQuery",
 "neptune-db:WriteDataViaQuery",
 "neptune-db:DeleteDataViaQuery",
 "neptune-db:GetEngineStatus",
 "neptune-db:GetQueryStatus",
 "neptune-db:CancelQuery"
 ],
 "Resource": "arn:aws:neptune-db:`us-east-1`:`123456789012`:`cluster-ABCD1234EFGH5678IJKL90MNOP`/*"
 }
 ]
}`

```

## Policy example granting full access for Gremlin queries only

The following policy grants full access to Neptune graph query operations using
the Gremlin query language, but not to queries in other languages, and not to features
like fast reset, streams, the bulk loader, Neptune ML model management, and so on:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect": "Allow",
 "Action": [
 "neptune-db:ReadDataViaQuery",
 "neptune-db:WriteDataViaQuery",
 "neptune-db:DeleteDataViaQuery",
 "neptune-db:GetEngineStatus",
 "neptune-db:GetQueryStatus",
 "neptune-db:CancelQuery"
 ],
 "Resource": [
 "arn:aws:neptune-db:`us-east-1`:`123456789012`:`cluster-ABCD1234EFGH5678IJKL90MNOP`/*"
 ],
 "Condition": {
 "StringEquals": {
 "neptune-db:QueryLanguage":"Gremlin"
 }
 }
 }
 ]
}`

```

## Policy example granting full access except for fast reset

The following policy grants full access to a Neptune DB cluster except
for using fast reset:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "neptune-db:*",
 "Resource": "arn:aws:neptune-db:`us-east-1`:`123456789012`:`cluster-ABCD1234EFGH5678IJKL90MNOP`/*"
 },
 {
 "Effect": "Deny",
 "Action": "neptune-db:ResetDatabase",
 "Resource": "arn:aws:neptune-db:`us-east-1`:`123456789012`:`cluster-ABCD1234EFGH5678IJKL90MNOP`/*"
 }
 ]
}`

```
