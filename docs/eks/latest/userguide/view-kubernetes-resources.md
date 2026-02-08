**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# View Kubernetes resources in the AWS Management Console

You can view the Kubernetes resources deployed to your cluster with the AWS Management Console. You can’t view Kubernetes resources with the AWS CLI or [eksctl](https://eksctl.io/ "https://eksctl.io/"). To view Kubernetes resources using a command-line tool, use [kubectl](install-kubectl.md "install-kubectl.md").

###### Note

To view the **Resources** tab and **Nodes** section on the **Compute** tab in the AWS Management Console, the [IAM principal](../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal "../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal") that you’re using must have specific IAM and Kubernetes permissions. For more information, see [Required permissions](#view-kubernetes-resources-permissions "#view-kubernetes-resources-permissions").

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. In the **Clusters** list, select the cluster that contains the Kubernetes resources that you want to view.
3. Select the **Resources** tab.
4. Select a **Resource type** group that you want to view resources for, such as **Workloads**. You see a list of resource types in that group.
5. Select a resource type, such as **Deployments**, in the **Workloads** group. You see a description of the resource type, a link to the Kubernetes documentation for more information about the resource type, and a list of resources of that type that are deployed on your cluster. If the list is empty, then there are no resources of that type deployed to your cluster.
6. Select a resource to view more information about it. Try the following examples:
   - Select the **Workloads** group, select the **Deployments** resource type, and then select the **coredns** resource. When you select a resource, you are in **Structured view**, by default. For some resource types, you see a **Pods** section in **Structured view**. This section lists the Pods managed by the workload. You can select any Pod listed to view information about the Pod. Not all resource types display information in **Structured View**. If you select **Raw view** in the top right corner of the page for the resource, you see the complete JSON response from the Kubernetes API for the resource.
   - Select the **Cluster** group and then select the **Nodes** resource type. You see a list of all nodes in your cluster. The nodes can be any [Amazon EKS node type](eks-compute.md "eks-compute.md"). This is the same list that you see in the **Nodes** section when you select the **Compute** tab for your cluster. Select a node resource from the list. In **Structured view**, you also see a **Pods** section. This section shows you all Pods running on the node.

## Required permissions

To view the **Resources** tab and **Nodes** section on the **Compute** tab in the AWS Management Console, the [IAM principal](../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal "../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal") that you’re using must have specific minimum IAM and Kubernetes permissions. You must have both IAM and Kubernetes RBAC permissions configured correctly. Complete the following steps to assign the required permissions to your IAM principals.

1. Make sure that the `eks:AccessKubernetesApi`, and other necessary IAM permissions to view Kubernetes resources, are assigned to the IAM principal that you’re using. For more information about how to edit permissions for an IAM principal, see [Controlling access for principals](../../../IAM/latest/UserGuide/access_controlling.md#access_controlling-principals "../../../IAM/latest/UserGuide/access_controlling.md#access_controlling-principals") in the IAM User Guide. For more information about how to edit permissions for a role, see [Modifying a role permissions policy (console)](../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md#roles-modify_permissions-policy "../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md#roles-modify_permissions-policy") in the IAM User Guide.

The following example policy includes the necessary permissions for a principal to view Kubernetes resources for all clusters in your account. Replace `111122223333` with your AWS account ID.

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "eks:ListFargateProfiles",
                "eks:DescribeNodegroup",
                "eks:ListNodegroups",
                "eks:ListUpdates",
                "eks:AccessKubernetesApi",
                "eks:ListAddons",
                "eks:DescribeCluster",
                "eks:DescribeAddonVersions",
                "eks:ListClusters",
                "eks:ListIdentityProviderConfigs",
                "iam:ListRoles"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "ssm:GetParameter",
            "Resource": "arn:aws:ssm:*:111122223333:parameter/*"
        }
    ]
}
```

To view nodes in [connected clusters](eks-connector.md "eks-connector.md"), the [Amazon EKS connector IAM role](connector-iam-role.md "connector-iam-role.md") should be able to impersonate the principal in the cluster. This allows the [Amazon EKS Connector](eks-connector.md "eks-connector.md") to map the principal to a Kubernetes user. 2. Configure Kubernetes RBAC permissions using EKS access entries.

**What are EKS Access Entries?**

EKS access entries are a streamlined way to grant IAM principals (users and roles) access to your Kubernetes cluster. Instead of manually managing Kubernetes RBAC resources and the `aws-auth` ConfigMap, access entries automatically handle the mapping between IAM and Kubernetes permissions using managed policies provided by AWS. For detailed information about access entries, see [Grant IAM users access to Kubernetes with EKS access entries](access-entries.md "access-entries.md"). For information about available access policies and their permissions, see [Access policy permissions](access-policy-permissions.md "access-policy-permissions.md").

You can attach Kubernetes permissions to access entries in two ways:

    * **Use an access policy:** Access policies are pre-defined Kubernetes permissions templates maintained by AWS. These provide standardized permission sets for common use cases.
    * **Reference a Kubernetes group:** If you associate an IAM identity with a Kubernetes group, you can create Kubernetes resources that grant the group permissions. For more information, see [Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/ "https://kubernetes.io/docs/reference/access-authn-authz/rbac/") in the Kubernetes documentation.




    	1. Create an access entry for your IAM principal using the AWS CLI. Replace `my-cluster` with the name of your cluster. Replace `111122223333` with your account ID.



    	```
    	aws eks create-access-entry \
    	    --cluster-name my-cluster \
    	    --principal-arn arn:aws:iam::111122223333:role/my-console-viewer-role
    	```

    	An example output is as follows.



    	```
    	{
    	    "accessEntry": {
    	        "clusterName": "my-cluster",
    	        "principalArn": "arn:aws:iam::111122223333:role/my-console-viewer-role",
    	        "kubernetesGroups": [],
    	        "accessEntryArn": "arn:aws:eks:region-code:111122223333:access-entry/my-cluster/role/111122223333/my-console-viewer-role/abc12345-1234-1234-1234-123456789012",
    	        "createdAt": "2024-03-15T10:30:45.123000-07:00",
    	        "modifiedAt": "2024-03-15T10:30:45.123000-07:00",
    	        "tags": {},
    	        "username": "arn:aws:iam::111122223333:role/my-console-viewer-role",
    	        "type": "STANDARD"
    	    }
    	}
    	```
    	2. Associate a policy with the access entry. For viewing Kubernetes resources, use the `AmazonEKSViewPolicy`:



    	```
    	aws eks associate-access-policy \
    	    --cluster-name my-cluster \
    	    --principal-arn arn:aws:iam::111122223333:role/my-console-viewer-role \
    	    --policy-arn arn:aws:eks::aws:cluster-access-policy/AmazonEKSViewPolicy \
    	    --access-scope type=cluster
    	```

    	An example output is as follows.



    	```
    	{
    	    "clusterName": "my-cluster",
    	    "principalArn": "arn:aws:iam::111122223333:role/my-console-viewer-role",
    	    "associatedAt": "2024-03-15T10:31:15.456000-07:00"
    	}
    	```

    	For namespace-specific access, you can scope the policy to specific namespaces:



    	```
    	aws eks associate-access-policy \
    	    --cluster-name my-cluster \
    	    --principal-arn arn:aws:iam::111122223333:role/my-console-viewer-role \
    	    --policy-arn arn:aws:eks::aws:cluster-access-policy/AmazonEKSViewPolicy \
    	    --access-scope type=namespace,namespaces=default,kube-system
    	```
    	3. Verify the access entry was created successfully:



    	```
    	aws eks describe-access-entry \
    	    --cluster-name my-cluster \
    	    --principal-arn arn:aws:iam::111122223333:role/my-console-viewer-role
    	```
    	4. List the associated policies to confirm the policy association:



    	```
    	aws eks list-associated-access-policies \
    	    --cluster-name my-cluster \
    	    --principal-arn arn:aws:iam::111122223333:role/my-console-viewer-role
    	```

    	An example output is as follows.



    	```
    	{
    	    "associatedAccessPolicies": [
    	        {
    	            "policyArn": "arn:aws:eks::aws:cluster-access-policy/AmazonEKSViewPolicy",
    	            "accessScope": {
    	                "type": "cluster"
    	            },
    	            "associatedAt": "2024-03-15T10:31:15.456000-07:00",
    	            "modifiedAt": "2024-03-15T10:31:15.456000-07:00"
    	        }
    	    ]
    	}
    	```

## CloudTrail visibility

When viewing Kubernetes resources, you will see the following operation name in your CloudTrail logs:

- `AccessKubernetesApi` - When reading or viewing resources

This CloudTrail event provides an audit trail of read access to your Kubernetes resources.

###### Note

This operation name appears in CloudTrail logs for auditing purposes only. It is not an IAM action and cannot be used in IAM policy statements. To control read access to Kubernetes resources through IAM policies, use the `eks:AccessKubernetesApi` permission as shown in the [Required permissions](#view-kubernetes-resources-permissions "#view-kubernetes-resources-permissions") section.
