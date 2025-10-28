# Step 2: Attach a cluster policy to the MSK cluster

The cluster owner can attach a cluster policy (also known as a [resource-based policy](security_iam_service-with-iam.md#security_iam_service-with-iam-resource-based-policies "security_iam_service-with-iam.md#security_iam_service-with-iam-resource-based-policies")) to the MSK cluster where you will turn on multi-VPC private connectivity. The cluster policy gives the clients permission to access the cluster from another account. Before you can edit the cluster policy, you need the account ID(s) for the accounts that should have permission to access the MSK cluster. See [How Amazon MSK works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").

The cluster owner must attach a cluster policy to the MSK cluster that authorizes the cross-account user in Account B to get bootstrap brokers for the cluster and to authorize the following actions on the MSK cluster in Account A:

- CreateVpcConnection
- GetBootstrapBrokers
- DescribeCluster
- DescribeClusterV2
  For reference, the following is an example of the JSON for a basic cluster policy, similar to the default policy shown in the MSK console IAM policy editor. The following policy grants permissions for cluster, topic, and group-level access.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "123456789012"
 },
 "Action": [
 "kafka:CreateVpcConnection",
 "kafka:GetBootstrapBrokers",
 "kafka:DescribeCluster",
 "kafka:DescribeClusterV2",
 "kafka-cluster:*"
 ],
 "Resource": "arn:aws:kafka:us-east-1:`111122223333`:cluster/testing/de8982fa-8222-4e87-8b20-9bf3cdfa1521-2"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "123456789012"
 },
 "Action": "kafka-cluster:*",
 "Resource": "arn:aws:kafka:us-east-1:`111122223333`:topic/testing/*"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "123456789012"
 },
 "Action": "kafka-cluster:*",
 "Resource": "arn:aws:kafka:us-east-1:`111122223333`:group/testing/*"
 }
 ]
}`

```

###### Attach a cluster policy to the MSK cluster

1. In the Amazon MSK console, under **MSK Clusters**, choose **Clusters**.
2. Scroll down to **Security settings** and select **Edit cluster** policy.
3. In the console, on the **Edit Cluster Policy**
   screen, select **Basic policy for multi-VPC
   connectivity**.
4. In the **Account ID** field, enter the account ID for each account that
   should have permission to access this cluster. As you type the ID, it is
   automatically copied over into the displayed policy JSON syntax. In our
   example cluster policy, the Account ID is `111122223333`.
5. Select **Save changes**.
   For information about cluster policy APIs, see [Amazon MSK resource-based policies](security_iam_service-with-iam.md#security_iam_service-with-iam-resource-based-policies "security_iam_service-with-iam.md#security_iam_service-with-iam-resource-based-policies").
