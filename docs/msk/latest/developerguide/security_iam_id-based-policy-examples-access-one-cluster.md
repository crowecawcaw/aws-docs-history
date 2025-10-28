# Accessing one

Amazon MSK cluster

In this example, you want to grant an IAM user in your Amazon Web Services account access to one
of your clusters, `purchaseQueriesCluster`. This policy allows the user
to describe the cluster, get its bootstrap brokers, list its broker nodes, and
update it.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"UpdateCluster",
 "Effect":"Allow",
 "Action":[
 "kafka:Describe*",
 "kafka:Get*",
 "kafka:List*",
 "kafka:Update*"
 ],
 "Resource":"arn:aws:kafka:us-east-1:012345678012:cluster/purchaseQueriesCluster/abcdefab-1234-abcd-5678-cdef0123ab01-2"
 }
 ]
}`

```
