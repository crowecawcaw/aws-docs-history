

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an Argo CD capability using the Console
<a name="argocd-create-console"></a>

Create an Argo CD capability on your Amazon EKS cluster using the AWS Management Console.

## Prerequisites
<a name="_prerequisites"></a>
+  ** AWS Identity Center configured** – Argo CD requires AWS Identity Center for authentication. Local users are not supported. If you don’t have AWS Identity Center set up, see [Getting started with AWS Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html) to create an Identity Center instance, and [Add users](https://docs.aws.amazon.com/singlesignon/latest/userguide/addusers.html) and [Add groups](https://docs.aws.amazon.com/singlesignon/latest/userguide/addgroups.html) to create users and groups for Argo CD access.
+  **At least one user or group in AWS Identity Center** – You must have at least one user or group configured in your Identity Center instance to assign Argo CD RBAC role mappings and provide access to the Argo CD UI.

## Create the Argo CD capability
<a name="_create_the_argo_cd_capability"></a>

1. Open the Amazon EKS console at https://console.aws.amazon.com/eks/home\#/clusters.

1. Select your cluster name to open the cluster detail page.

1. Choose the **Capabilities** tab.

1. In the left navigation, choose **Argo CD**.

1. Choose **Create Argo CD capability**.

1. For **IAM Capability Role**:
   + If you already have an IAM Capability Role, select it from the dropdown
   + If you need to create a role, choose **Create Argo CD role** 

     This opens the IAM console in a new tab with pre-populated trust policy and full read access to Secrets Manager. No other permissions are added by default, but you can add them if needed. If you plan to use CodeCommit repositories or other AWS services, add the appropriate permissions before creating the role.

     After creating the role, return to the EKS console and the role will be automatically selected.
**Note**  
If you plan to use the optional integrations with AWS Secrets Manager or AWS CodeConnections, you’ll need to add permissions to the role. For IAM policy examples and configuration guidance, see [Manage application secrets with AWS Secrets Manager](integration-secrets-manager.md) and [Connect to Git repositories with AWS CodeConnections](integration-codeconnections.md).

1. Configure AWS Identity Center integration:

   1. Select **Enable AWS Identity Center integration**.

   1. Choose your Identity Center instance from the dropdown.

   1. Configure role mappings for RBAC by assigning users or groups to Argo CD roles (ADMIN, EDITOR, or VIEWER)

1.  **(Optional) Configure private endpoint**:

   By default, the Argo CD UI and API endpoint are publicly accessible over the internet. If you need to restrict access, you can configure a VPC endpoint. This is recommended for environments with strict network security requirements.

   1. Before creating the capability, create an interface VPC endpoint for the `com.amazonaws.<region>.eks-capabilities` service in your VPC. The VPC endpoint should:
      + Be associated with subnets in different Availability Zones for high availability
      + Have a security group that allows inbound HTTPS (port 443) traffic from the networks that need to access the Argo CD UI and API
      + For more details on creating and customizing VPC endpoints, see [Create a VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the AWS PrivateLink Guide.

   1. In the **Argo CD endpoint access - *optional* ** section of the Argo CD capability creation page, select **Private**.

   1. Choose the VPC endpoint you created from the dropdown.
**Note**  
When private endpoint is enabled, the Argo CD UI and API are only accessible through the VPC endpoint. Users must be connected to the VPC (or a peered network) to access the Argo CD interface.

1. Choose **Create**.

The capability creation process begins.

## Verify the capability is active
<a name="_verify_the_capability_is_active"></a>

1. On the **Capabilities** tab, view the Argo CD capability status.

1. Wait for the status to change from `CREATING` to `ACTIVE`.

1. Once active, the capability is ready to use.

For information about capability statuses and troubleshooting, see [Working with capability resources](working-with-capabilities.md).

## Access the Argo CD UI
<a name="_access_the_argo_cd_ui"></a>

After the capability is active, you can access the Argo CD UI:

1. On the Argo CD capability page, choose **Open Argo CD UI**.

1. The Argo CD UI opens in a new browser tab.

1. You can now create Applications and manage deployments through the UI.

## Next steps
<a name="_next_steps"></a>
+  [Working with Argo CD](working-with-argocd.md) - Configure repositories, register clusters, and create Applications
+  [Argo CD considerations](argocd-considerations.md) - Multi-cluster architecture and advanced configuration
+  [Working with capability resources](working-with-capabilities.md) - Manage your Argo CD capability resource