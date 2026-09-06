

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an ACK capability using the Console
<a name="ack-create-console"></a>

Create an ACK capability on your Amazon EKS cluster using the AWS Management Console.

## Create the ACK capability
<a name="_create_the_ack_capability"></a>

1. Open the Amazon EKS console at https://console.aws.amazon.com/eks/home\#/clusters.

1. Select your cluster name to open the cluster detail page.

1. Choose the **Capabilities** tab.

1. In the left navigation, choose ** AWS Controllers for Kubernetes (ACK)**.

1. Choose **Create AWS Controllers for Kubernetes capability**.

1. For **IAM Capability Role**:
   + If you already have an IAM Capability Role, select it from the dropdown
   + If you need to create a role, choose **Create admin role** 

     This opens the IAM console in a new tab with pre-populated trust policy and the `AdministratorAccess` managed policy. You can unselect this policy and add other permissions if you prefer.

     After creating the role, return to the EKS console and the role will be automatically selected.
**Important**  
The suggested `AdministratorAccess` policy grants broad permissions and is intended to streamline getting started. For production use, replace this with a custom policy that grants only the permissions needed for the specific AWS services you plan to manage with ACK. For guidance on creating least-privilege policies, see [Configure ACK permissions](ack-permissions.md) and [Security considerations for EKS Capabilities](capabilities-security.md).

1. Choose **Create**.

The capability creation process begins.

## Verify the capability is active
<a name="_verify_the_capability_is_active"></a>

1. On the **Capabilities** tab, view the ACK capability status.

1. Wait for the status to change from `CREATING` to `ACTIVE`.

1. Once active, the capability is ready to use.

For information about capability statuses and troubleshooting, see [Working with capability resources](working-with-capabilities.md).

## Verify custom resources are available
<a name="_verify_custom_resources_are_available"></a>

After the capability is active, verify that ACK custom resources are available in your cluster.

 **Using the console** 

1. Navigate to your cluster in the Amazon EKS console

1. Choose the **Resources** tab

1. Choose **Extensions** 

1. Choose **CustomResourceDefinitions** 

You should see a number of CRDs listed for AWS resources.

 **Using kubectl** 

```
kubectl api-resources | grep services.k8s.aws
```

You should see a number of APIs listed for AWS resources.

**Note**  
The capability for AWS Controllers for Kubernetes will install a number of CRDs for a variety of AWS resources.

## Next steps
<a name="_next_steps"></a>
+  [ACK concepts](ack-concepts.md) - Understand ACK concepts and get started
+  [Configure ACK permissions](ack-permissions.md) - Configure IAM permissions for other AWS services
+  [Working with capability resources](working-with-capabilities.md) - Manage your ACK capability resource