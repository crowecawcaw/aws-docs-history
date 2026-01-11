**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create a kro capability using the Console

This topic describes how to create a kro (Kube Resource Orchestrator) capability using the AWS Management Console.

## Create the kro capability

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home#/clusters](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. Select your cluster name to open the cluster detail page.
3. Choose the **Capabilities** tab.
4. In the left navigation, choose **kro (Kube Resource Orchestrator)**.
5. Choose **Create kro capability**.
6. For **IAM Capability Role**:
   - If you already have an IAM Capability Role, select it from the dropdown
   - If you need to create a role, choose **Create kro role**

   This opens the IAM console in a new tab with pre-populated trust policy.
   The role requires no additional IAM permissions since kro operates entirely within your cluster.

   After creating the role, return to the EKS console and the role will be automatically selected.

   ###### Note

   Unlike ACK and Argo CD, kro does not require additional IAM permissions beyond the trust policy.
   kro operates entirely within your cluster and does not make AWS API calls.

7. Choose **Create**.

The capability creation process begins.

## Verify the capability is active

1. On the **Capabilities** tab, view the kro capability status.
2. Wait for the status to change from `CREATING` to `ACTIVE`.
3. Once active, the capability is ready to use.

For information about capability statuses and troubleshooting, see [Working with capability resources](working-with-capabilities.md "working-with-capabilities.md").

## Grant permissions to manage Kubernetes resources

When you create a kro capability, an EKS Access Entry is automatically created with the `AmazonEKSKROPolicy`, which allows kro to manage ResourceGraphDefinitions and their instances.
However, no permissions are granted by default to create the underlying Kubernetes resources (like Deployments, Services, ConfigMaps, etc.) defined in your ResourceGraphDefinitions.

This intentional design follows the principle of least privilege—different ResourceGraphDefinitions require different permissions.
You must explicitly configure the permissions kro needs based on the resources your ResourceGraphDefinitions will manage.

For getting started quickly, testing, or development environments, use `AmazonEKSClusterAdminPolicy`:

1. In the EKS console, navigate to your cluster’s **Access** tab.
2. Under **Access entries**, find the entry for your kro capability role (it will have the role ARN you created earlier).
3. Choose the access entry to open its details.
4. In the **Access policies** section, choose **Associate access policy**.
5. Select `AmazonEKSClusterAdminPolicy` from the policy list.
6. For **Access scope**, select **Cluster**.
7. Choose **Associate**.

###### Important

The `AmazonEKSClusterAdminPolicy` grants broad permissions to create and manage all Kubernetes resources, including the ability to create any resource type across all namespaces.
This is convenient for development and POCs but should not be used in production.
For production, create custom RBAC policies that grant only the permissions needed for the specific resources your ResourceGraphDefinitions will manage.
For guidance on configuring least-privilege permissions, see [Configure kro permissions](kro-permissions.md "kro-permissions.md") and [Security considerations for EKS Capabilities](capabilities-security.md "capabilities-security.md").

## Verify custom resources are available

After the capability is active, verify that kro custom resources are available in your cluster.

**Using the console**

1. Navigate to your cluster in the Amazon EKS console
2. Choose the **Resources** tab
3. Choose **Extensions**
4. Choose **CustomResourceDefinitions**

You should see the `ResourceGraphDefinition` resource type listed.

**Using kubectl**

```
kubectl api-resources | grep kro.run
```

You should see the `ResourceGraphDefinition` resource type listed.

## Next steps

- [kro concepts](kro-concepts.md "kro-concepts.md") - Understand kro concepts and resource composition
- [kro concepts](kro-concepts.md "kro-concepts.md") - Learn about SimpleSchema, CEL expressions, and composition patterns
- [Working with capability resources](working-with-capabilities.md "working-with-capabilities.md") - Manage your kro capability resource
