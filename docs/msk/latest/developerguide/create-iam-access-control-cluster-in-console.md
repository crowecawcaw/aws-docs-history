# Create a Amazon MSK cluster that uses IAM access control

This section explains how you can use the AWS Management Console, the API, or the AWS CLI to
create a Amazon MSK cluster that uses IAM access control. For information about how to turn
on IAM access control for an existing cluster, see [Update security settings of a Amazon MSK cluster](msk-update-security.md "msk-update-security.md").

###### Use the AWS Management Console to create a cluster that uses IAM access control

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/ "https://console.aws.amazon.com/msk/").
2. Choose **Create cluster**.
3. Choose **Create cluster with custom settings**.
4. In the **Authentication** section, choose **IAM
   access control**.
5. Complete the rest of the workflow for creating a cluster.

###### Use the API or the AWS CLI to create a cluster that uses IAM access control

- To create a cluster with IAM access control enabled, use the [CreateCluster](../../1.0/apireference/clusters.md#CreateCluster "../../1.0/apireference/clusters.md#CreateCluster") API or the [create-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/create-cluster.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/create-cluster.html") CLI command, and pass the following JSON for the
  `ClientAuthentication` parameter: `"ClientAuthentication": {
"Sasl": {
"Iam": {
"Enabled": true
}
}`.
