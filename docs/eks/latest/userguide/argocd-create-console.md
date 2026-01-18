**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an Argo CD capability using the Console

This topic describes how to create an Argo CD capability using the AWS Management Console.

## Prerequisites

- **AWS Identity Center configured** – Argo CD requires AWS Identity Center for authentication. Local users are not supported. If you don’t have AWS Identity Center set up, see [Getting started with AWS Identity Center](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md") to create an Identity Center instance, and [Add users](../../../singlesignon/latest/userguide/addusers.md "../../../singlesignon/latest/userguide/addusers.md") and [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") to create users and groups for Argo CD access.

## Create the Argo CD capability

1. Open the Amazon EKS console at https://console.aws.amazon.com/eks/home#/clusters.
2. Select your cluster name to open the cluster detail page.
3. Choose the **Capabilities** tab.
4. In the left navigation, choose **Argo CD**.
5. Choose **Create Argo CD capability**.
6. For **IAM Capability Role**:
   - If you already have an IAM Capability Role, select it from the dropdown
   - If you need to create a role, choose **Create Argo CD role**

   This opens the IAM console in a new tab with pre-populated trust policy and full read access to Secrets Manager.
   No other permissions are added by default, but you can add them if needed.
   If you plan to use CodeCommit repositories or other AWS services, add the appropriate permissions before creating the role.

   After creating the role, return to the EKS console and the role will be automatically selected.

   ###### Note

   If you plan to use the optional integrations with AWS Secrets Manager or AWS CodeConnections, you’ll need to add permissions to the role.
   For IAM policy examples and configuration guidance, see [Manage application secrets with AWS Secrets Manager](integration-secrets-manager.md "integration-secrets-manager.md") and [Connect to Git repositories with AWS CodeConnections](integration-codeconnections.md "integration-codeconnections.md").

7. Configure AWS Identity Center integration:
   1. Select **Enable AWS Identity Center integration**.
   2. Choose your Identity Center instance from the dropdown.
   3. Configure role mappings for RBAC by assigning users or groups to Argo CD roles (ADMIN, EDITOR, or VIEWER)

8. Choose **Create**.

The capability creation process begins.

## Verify the capability is active

1. On the **Capabilities** tab, view the Argo CD capability status.
2. Wait for the status to change from `CREATING` to `ACTIVE`.
3. Once active, the capability is ready to use.

For information about capability statuses and troubleshooting, see [Working with capability resources](working-with-capabilities.md "working-with-capabilities.md").

## Access the Argo CD UI

After the capability is active, you can access the Argo CD UI:

1. On the Argo CD capability page, choose **Open Argo CD UI**.
2. The Argo CD UI opens in a new browser tab.
3. You can now create Applications and manage deployments through the UI.

## Next steps

- [Working with Argo CD](working-with-argocd.md "working-with-argocd.md") - Configure repositories, register clusters, and create Applications
- [Argo CD considerations](argocd-considerations.md "argocd-considerations.md") - Multi-cluster architecture and advanced configuration
- [Working with capability resources](working-with-capabilities.md "working-with-capabilities.md") - Manage your Argo CD capability resource
