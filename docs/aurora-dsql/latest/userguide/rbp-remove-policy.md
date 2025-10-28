# Removing resource-based policies

You can remove resource-based policies from clusters to change access controls.

###### Important

When you remove all resource-based policies from a cluster, access will be controlled entirely by IAM identity-based policies.

###### To remove a resource-based policy

1. Sign in to the AWS Management Console and open the Aurora DSQL console at [https://console.aws.amazon.com/dsql/](https://console.aws.amazon.com/dsql "https://console.aws.amazon.com/dsql").
2. Choose your cluster from the cluster list to open the cluster details page.
3. Choose the **Permissions** tab.
4. In the **Resource-based policy** section, choose **Delete**.
5. In the confirmation dialog, type `confirm` to confirm the deletion.
6. Choose **Delete**.
   Use the `delete-cluster-policy` command to remove a policy from a cluster:

```
aws dsql delete-cluster-policy --identifier `your_cluster_id`
```

Python

```
import boto3

client = boto3.client('dsql')

response = client.delete_cluster_policy(
    identifier='your_cluster_id'
)

print("Policy deleted successfully")
```

Java

```
import software.amazon.awssdk.services.dsql.DsqlClient;
import software.amazon.awssdk.services.dsql.model.DeleteClusterPolicyRequest;

DsqlClient client = DsqlClient.create();

DeleteClusterPolicyRequest request = DeleteClusterPolicyRequest.builder()
    .identifier("your_cluster_id")
    .build();

client.deleteClusterPolicy(request);
System.out.println("Policy deleted successfully");
```
