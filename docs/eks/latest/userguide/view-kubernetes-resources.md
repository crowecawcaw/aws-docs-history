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

To view the **Resources** tab and **Nodes** section on the **Compute** tab in the AWS Management Console, the [IAM principal](../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal "../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal") that you’re using must have specific minimum IAM and Kubernetes permissions. Complete the following steps to assign the required permissions to your IAM principals.

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

To view nodes in [connected clusters](eks-connector.md "eks-connector.md"), the [Amazon EKS connector IAM role](connector-iam-role.md "connector-iam-role.md") should be able to impersonate the principal in the cluster. This allows the [Amazon EKS Connector](eks-connector.md "eks-connector.md") to map the principal to a Kubernetes user. 2. Create a Kubernetes `rolebinding` or `clusterrolebinding` that is bound to a Kubernetes `role` or `clusterrole` that has the necessary permissions to view the Kubernetes resources. To learn more about Kubernetes roles and role bindings, see [Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/ "https://kubernetes.io/docs/reference/access-authn-authz/rbac/") in the Kubernetes documentation. You can apply one of the following manifests to your cluster that create a `role` and `rolebinding` or a `clusterrole` and `clusterrolebinding` with the necessary Kubernetes permissions:

View Kubernetes resources in all namespaces

    * The group name in the file is `eks-console-dashboard-full-access-group`. Apply the manifest to your cluster with the following command:



    ```
    kubectl apply -f https://s3.us-west-2.amazonaws.com/amazon-eks/docs/eks-console-full-access.yaml
    ```

View Kubernetes resources in a specific namespace

    * The namespace in this file is `default`. The group name in the file is `eks-console-dashboard-restricted-access-group`. Apply the manifest to your cluster with the following command:



    ```
    kubectl apply -f https://s3.us-west-2.amazonaws.com/amazon-eks/docs/eks-console-restricted-access.yaml
    ```

    If you need to change the Kubernetes group name, namespace, permissions, or any other configuration in the file, then download the file and edit it before applying it to your cluster:




    	1. Download the file with one of the following commands:



    	```
    	curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/docs/eks-console-full-access.yaml
    	```


    	```
    	curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/docs/eks-console-restricted-access.yaml
    	```
    	2. Edit the file as necessary.
    	3. Apply the manifest to your cluster with one of the following commands:



    	```
    	kubectl apply -f eks-console-full-access.yaml
    	```


    	```
    	kubectl apply -f eks-console-restricted-access.yaml
    	```

3. Map the [IAM principal](../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal "../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal") to the Kubernetes user or group in the `aws-auth`
   `ConfigMap`. You can use a tool such as `eksctl` to update the `ConfigMap` or you can update it manually by editing it.

###### Important

We recommend using `eksctl`, or another tool, to edit the `ConfigMap`. For information about other tools you can use, see [Use tools to make changes to the aws-authConfigMap](https://aws.github.io/aws-eks-best-practices/security/docs/iam/#use-tools-to-make-changes-to-the-aws-auth-configmap "https://aws.github.io/aws-eks-best-practices/security/docs/iam/#use-tools-to-make-changes-to-the-aws-auth-configmap") in the Amazon EKS best practices guides. An improperly formatted `aws-auth`
`ConfigMap` can cause you to lose access to your cluster.

### Edit with eksctl

1. You need version `0.215.0` or later of the `eksctl` command line tool installed on your device or AWS CloudShell. To install or update `eksctl`, see [Installation](https://eksctl.io/installation "https://eksctl.io/installation") in the `eksctl` documentation.
2. View the current mappings in the `ConfigMap`. Replace `my-cluster` with the name of your cluster. Replace `region-code` with the AWS Region that your cluster is in.

```
eksctl get iamidentitymapping --cluster my-cluster --region=region-code
```

An example output is as follows.

```
ARN                                                                                             USERNAME                                GROUPS                          ACCOUNT
arn:aws:iam::111122223333:role/eksctl-my-cluster-my-nodegroup-NodeInstanceRole-1XLS7754U3ZPA    system:node:{{EC2PrivateDNSName}}       system:bootstrappers,system:nodes
```

3. Add a mapping for a role. This example assume that you attached the IAM permissions in the first step to a role named `my-console-viewer-role`. Replace `111122223333` with your account ID.

```
eksctl create iamidentitymapping \
    --cluster my-cluster \
    --region=region-code \
    --arn arn:aws:iam::111122223333:role/my-console-viewer-role \
    --group eks-console-dashboard-full-access-group \
    --no-duplicate-arns
```

###### Important

The role ARN can’t include a path such as `role/my-team/developers/my-role`. The format of the ARN must be `arn:aws:iam::`111122223333`:role/`my-role``. In this example, `my-team/developers/` needs to be removed.

An example output is as follows.

```
[...]
2022-05-09 14:51:20 [ℹ]  adding identity "arn:aws:iam::111122223333:role/my-console-viewer-role" to auth ConfigMap
```

4. Add a mapping for a user. [IAM best practices](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md") recommend that you grant permissions to roles instead of users. This example assume that you attached the IAM permissions in the first step to a user named `my-user`. Replace `111122223333` with your account ID.

```
eksctl create iamidentitymapping \
    --cluster my-cluster \
    --region=region-code \
    --arn arn:aws:iam::111122223333:user/my-user \
    --group eks-console-dashboard-restricted-access-group \
    --no-duplicate-arns
```

An example output is as follows.

```
[...]
2022-05-09 14:53:48 [ℹ]  adding identity "arn:aws:iam::111122223333:user/my-user" to auth ConfigMap
```

5. View the mappings in the `ConfigMap` again.

```
eksctl get iamidentitymapping --cluster my-cluster --region=region-code
```

An example output is as follows.

```
ARN                                                                                             USERNAME                                GROUPS                                  ACCOUNT
arn:aws:iam::111122223333:role/eksctl-my-cluster-my-nodegroup-NodeInstanceRole-1XLS7754U3ZPA    system:node:{{EC2PrivateDNSName}}       system:bootstrappers,system:nodes
arn:aws:iam::111122223333:role/my-console-viewer-role                                                                                   eks-console-dashboard-full-access-group
arn:aws:iam::111122223333:user/my-user                                                                                                  eks-console-dashboard-restricted-access-group
```

### Edit ConfigMap manually

For more information about adding users or roles to the `aws-auth`
`ConfigMap`, see [Add IAM principals to your Amazon EKS cluster](auth-configmap.md#aws-auth-users "auth-configmap.md#aws-auth-users").

1. Open the `aws-auth`
   `ConfigMap` for editing.

```
kubectl edit -n kube-system configmap/aws-auth
```

2.  Add the mappings to the `aws-auth`
    `ConfigMap`, but don’t replace any of the existing mappings. The following example adds mappings between [IAM principals](../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal "../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal") with permissions added in the first step and the Kubernetes groups created in the previous step:

        * The `my-console-viewer-role` role and the `eks-console-dashboard-full-access-group`.
        * The `my-user` user and the `eks-console-dashboard-restricted-access-group`.


        These examples assume that you attached the IAM permissions in the first step to a role named `my-console-viewer-role` and a user named `my-user`. Replace `111122223333` with your AWS account ID.



        ```
        apiVersion: v1
        data:
        mapRoles: |
          - groups:
            - eks-console-dashboard-full-access-group
            rolearn: arn:aws:iam::111122223333:role/my-console-viewer-role
            username: my-console-viewer-role
        mapUsers: |
          - groups:
            - eks-console-dashboard-restricted-access-group
            userarn: arn:aws:iam::111122223333:user/my-user
            username: my-user
        ```

        ###### Important

        The role ARN can’t include a path such as `role/my-team/developers/my-console-viewer-role`. The format of the ARN must be `arn:aws:iam::`111122223333`:role/`my-console-viewer-role``. In this example, `my-team/developers/` needs to be removed.

3.  Save the file and exit your text editor.
