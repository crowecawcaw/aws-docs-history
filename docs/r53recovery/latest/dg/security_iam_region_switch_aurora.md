# Aurora Global Database execution block sample policy

The following is a sample policy to attach if you add execution blocks to a Region switch plan for Aurora databases.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "rds:DescribeGlobalClusters",
 "rds:DescribeDBClusters"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "rds:FailoverGlobalCluster",
 "rds:SwitchoverGlobalCluster"
 ],
 "Resource": [
 "arn:aws:rds::123456789012:global-cluster:app-global-db",
 "arn:aws:rds:us-east-1:123456789012:cluster:app-db-primary",
 "arn:aws:rds:us-west-2:123456789012:cluster:app-db-secondary"
 ]
 }
 ]
}`

```
