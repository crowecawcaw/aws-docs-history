# Connecting Azure Resources

Azure Resources integration enables AWS DevOps Agent to discover and investigate resources in your Azure subscriptions during incident investigations. The agent uses Azure Resource Graph for resource discovery and can access metrics, logs, and configuration data across your Azure environment.

This integration follows a two-step process: register Azure at the AWS account level, then associate specific Azure subscriptions with individual Agent Spaces. You can create more than one Azure Resources registration in an account, and register the same Azure tenant in more than one AWS account. If you use App Registration, each registration must use a different application (client ID). For more information, see [Connecting Azure](configuring-integrations-and-knowledge-connecting-azure-index.md "configuring-integrations-and-knowledge-connecting-azure-index.md").

## Prerequisites

Before connecting Azure Resources, ensure you have:

- Access to the AWS DevOps Agent console
- An Azure account with access to the target subscription
- For Admin Consent method: an account with permission to perform admin consent in Microsoft Entra ID
- For App Registration method: an Entra application with permissions to configure federated identity credentials, and [Outbound Identity Federation](../../../IAM/latest/UserGuide/id_roles_providers_enable-federation.md "../../../IAM/latest/UserGuide/id_roles_providers_enable-federation.md") enabled in your AWS account

## Registering Azure Resources via Admin Consent

The Admin Consent method uses a consent-based flow with the AWS DevOps Agent managed application.

### Step 1: Start the registration

1. Sign in to the AWS Management Console and navigate to the AWS DevOps Agent console
2. Go to the **Capability Providers** page
3. Locate the **Azure Cloud** section and choose **Register**
4. Select the **Admin Consent** registration method

### Step 2: Complete Admin Consent

1. Review the permissions being requested
2. Choose to proceed — you are redirected to the Microsoft Entra admin consent page
3. Sign in with a user principal account that has permission to perform admin consent
4. Review and grant consent for the AWS DevOps Agent application

### Step 3: Complete user authorization

1. After admin consent, you are prompted for user authorization to verify your identity as a member of the authorized tenant
2. Sign in with an account belonging to the same Azure tenant
3. After authorization, you are redirected back to the AWS DevOps Agent console with a success status

### Step 4: Assign roles

See [Assigning Azure roles](#assigning-azure-roles "#assigning-azure-roles") below. Search for **AWS DevOps Agent** when selecting members.

## Registering Azure Resources via App Registration

The App Registration method uses your own Entra application with federated identity credentials.

### Step 1: Start the registration

1. In the AWS DevOps Agent console, go to the **Capability Providers** page
2. Locate the **Azure Cloud** section and choose **Register**
3. Select the **App Registration** method

### Step 2: Create and configure your Entra application

Follow the instructions displayed in the console to:

1. Enable Outbound Identity Federation in your AWS account (in the IAM console, go to **Account settings** → **Outbound Identity Federation**)
2. Create an Entra application in your Microsoft Entra ID, or use an existing one
3. Configure federated identity credentials on the application

### Step 3: Provide registration details

Fill in the registration form with:

- **Tenant ID** – Your Azure tenant identifier
- **Tenant Name** – A display name for the tenant
- **Client ID** – The application (client) ID of the Entra application you created
- **Audience** – The audience identifier for the federated credential

### Step 4: Create the IAM role

An IAM role will be automatically created when you submit the registration through the console. It permits AWS DevOps Agent to assume credentials and invoke `sts:GetWebIdentityToken`.

### Step 5: Assign roles

See [Assigning Azure roles](#assigning-azure-roles "#assigning-azure-roles") below. Search for the Entra application you created when selecting members.

### Step 6: Complete the registration

1. Confirm the configuration in the AWS DevOps Agent console
2. Choose **Submit** to complete the registration

## Assigning Azure roles

After registration, grant the application read access to your Azure subscription. This step is the same for both the Admin Consent and App Registration methods.

1. In the Azure Portal, navigate to your target subscription
2. Go to **Access Control (IAM)**
3. Choose **Add** > **Add role assignment**
4. Select the **Reader** role and choose **Next**
5. Choose **Select members**, search for the application (either **AWS DevOps Agent** for Admin Consent, or your own Entra application for App Registration)
6. Select the application and choose **Review + assign**
7. (Optional) To enable the agent to access Azure Kubernetes Service (AKS) clusters, complete the following AKS access setup.

### AKS access setup (optional)

#### Step 1: Azure Resource Manager (ARM) level access

Assign **Azure Kubernetes Service Cluster User Role** to the application.

In the Azure Portal, go to **Subscriptions** → select subscription → **Access Control (IAM)** → **Add role assignment** → select **Azure Kubernetes Service Cluster User Role** → assign to the application (either **AWS DevOps Agent** for Admin Consent, or your own Entra application for App Registration).

This covers all AKS clusters in the subscription. To scope to specific clusters, assign at the resource group or individual cluster level instead.

#### Step 2: Kubernetes API access

Choose one option based on your cluster's authentication configuration:

**Option A: Azure Role-Based Access Control (RBAC) for Kubernetes (recommended)**

1. Enable Azure RBAC on the cluster if not already enabled: Azure Portal → AKS cluster → **Settings** → **Security configuration** → **Authentication and authorization** → select **Azure RBAC**
2. Assign read-only role: Azure Portal → **Subscriptions** → select subscription → **Access Control (IAM)** → **Add role assignment** → select **Azure Kubernetes Service RBAC Reader** → assign to the application

This covers all AKS clusters in the subscription.

**Option B: Azure Active Directory (Azure AD) + Kubernetes RBAC**

Use this if your cluster already uses the default Azure AD authentication configuration and you prefer not to enable Azure RBAC. This requires per-cluster `kubectl` setup.

1. Save the following manifest as `devops-agent-reader.yaml`:

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: devops-agent-reader
rules:
  - apiGroups: [""]
    resources: ["namespaces", "pods", "pods/log", "services", "events", "nodes"]
    verbs: ["get", "list"]
  - apiGroups: ["apps"]
    resources: ["deployments", "replicasets", "statefulsets", "daemonsets"]
    verbs: ["get", "list"]
  - apiGroups: ["metrics.k8s.io"]
    resources: ["pods", "nodes"]
    verbs: ["get", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: devops-agent-reader-binding
subjects:
  - kind: User
    name: "<SERVICE_PRINCIPAL_OBJECT_ID>"
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: devops-agent-reader
  apiGroup: rbac.authorization.k8s.io
```

1. Replace `<SERVICE_PRINCIPAL_OBJECT_ID>` with your service principal's Object ID. To find it: Azure Portal → Entra ID → Enterprise Applications → search for the application name (either **AWS DevOps Agent** for Admin Consent, or your own Entra application for App Registration).
2. Apply to each cluster:

```
az aks get-credentials --resource-group <rg> --name <cluster-name>
kubectl apply -f devops-agent-reader.yaml
```

### Least-privileged custom role (optional)

For tighter access control, you can create a custom Azure role scoped to only the resource providers AWS DevOps Agent uses, instead of the broad Reader role:

```
{
  "Name": "AWS DevOps Agent - Azure Reader",
  "Description": "Least-privilege read-only access for AWS DevOps Agent incident investigations.",
  "Actions": [
    "Microsoft.AlertsManagement/*/read",
    "Microsoft.Compute/*/read",
    "Microsoft.ContainerRegistry/*/read",
    "Microsoft.ContainerService/*/read",
    "Microsoft.ContainerService/managedClusters/commandResults/read",
    "Microsoft.DocumentDB/*/read",
    "Microsoft.Insights/*/read",
    "Microsoft.KeyVault/vaults/read",
    "Microsoft.ManagedIdentity/*/read",
    "Microsoft.Monitor/*/read",
    "Microsoft.Network/*/read",
    "Microsoft.OperationalInsights/*/read",
    "Microsoft.ResourceGraph/resources/read",
    "Microsoft.ResourceHealth/*/read",
    "Microsoft.Resources/*/read",
    "Microsoft.Sql/*/read",
    "Microsoft.Storage/*/read",
    "Microsoft.Web/*/read"
  ],
  "NotActions": [],
  "DataActions": [],
  "NotDataActions": [],
  "AssignableScopes": [
    "/subscriptions/{your-subscription-id}"
  ]
}
```

## Associating a subscription with an Agent Space

After registering Azure at the account level, associate specific subscriptions with your Agent Spaces:

1. In the AWS DevOps Agent console, select your Agent Space
2. Go to the **Capabilities** tab
3. In the **Secondary sources** section, choose **Add**
4. Choose the **Azure** registration that contains the subscription you want to use.
5. Provide the **Subscription ID** for the Azure subscription you want to associate
6. Choose **Add** to complete the association

You can associate multiple subscriptions with the same Agent Space, including subscriptions from different registrations, to give the agent visibility across your Azure environment. To associate another subscription, repeat these steps.

## Managing Azure Resources connections

- **Viewing connected subscriptions** – In the **Capabilities** tab, the **Secondary sources** section lists all connected Azure subscriptions.
- **Removing a subscription** – To disconnect a subscription from an Agent Space, select it in the **Secondary sources** list and choose **Remove**. This does not affect the account-level registration.
- **Removing the registration** – To remove the Azure Cloud registration entirely, go to the **Capability Providers** page and delete the registration. All Agent Space associations must be removed first.
