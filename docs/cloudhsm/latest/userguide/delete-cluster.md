# Deleting an AWS CloudHSM cluster

Before you can delete a cluster, you must remove all HSMs from the cluster. For more
information, see [Removing an HSM from an AWS CloudHSM cluster](remove-hsm.md "remove-hsm.md").

After you remove all HSMs, you can delete a cluster by using the [AWS CloudHSM console](https://console.aws.amazon.com/cloudhsm/ "https://console.aws.amazon.com/cloudhsm/"), the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), or the AWS CloudHSM API.

###### To delete a cluster (console)

1. Open the AWS CloudHSM console at
   [https://console.aws.amazon.com/cloudhsm/home](https://console.aws.amazon.com/cloudhsm/home "https://console.aws.amazon.com/cloudhsm/home").
2. Choose the cluster that you are deleting. Then choose **Delete
   cluster**.
3. Confirm that you want to delete the cluster, then choose
   **Delete**.

###### To delete a cluster (AWS CLI)

- At a command prompt, issue the **[delete-cluster](../../../cli/latest/reference/cloudhsmv2/delete-cluster.md "../../../cli/latest/reference/cloudhsmv2/delete-cluster.md")** command,
  passing the ID of the cluster that you are deleting. If you don't know the cluster ID, issue
  the **[describe-clusters](../../../cli/latest/reference/cloudhsmv2/describe-clusters.md "../../../cli/latest/reference/cloudhsmv2/describe-clusters.md")** command.

````
`$` `aws cloudhsmv2 delete-cluster --cluster-id `<cluster ID>```{
 "Cluster": {
 "Certificates": {
 "ClusterCertificate": "`<certificate string>`"
 },
 "SourceBackupId": "backup-rtq2dwi2gq6",
 "SecurityGroup": "sg-40399d28",
 "CreateTimestamp": 1504903546.035,
 "SubnetMapping": {
 "us-east-2a": "subnet-f1d6e798",
 "us-east-2c": "subnet-0e358c43",
 "us-east-2b": "subnet-40ed9d3b"
 },
 "ClusterId": "cluster-kdmrayrc7gi",
 "VpcId": "vpc-641d3c0d",
 "State": "DELETE_IN_PROGRESS",
 "HsmType": "hsm1.medium",
 "StateMessage": "The cluster is being deleted.",
 "Hsms": [],
 "BackupPolicy": "DEFAULT"
 }
}`
````

###### To delete a cluster (AWS CloudHSM API)

- Send a [DeleteCluster](../APIReference/API_DeleteCluster.md "../APIReference/API_DeleteCluster.md") request, specifying the ID of the cluster that you are
  deleting.
