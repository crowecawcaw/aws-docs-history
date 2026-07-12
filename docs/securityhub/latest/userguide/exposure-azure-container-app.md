# Remediating exposures for Azure Container apps

AWS Security Hub can generate exposure findings for Azure Container apps.

On the Security Hub console, the Azure Container app involved in an exposure finding and its identifying information are listed in
the **Resources** section of the finding details. Programmatically, you can retrieve resource
details with the [GetFindingsV2](../../1.0/APIReference/API_GetFindingsV2.md "../../1.0/APIReference/API_GetFindingsV2.md") operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it.
Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential,
follow these recommended remediation steps to help mitigate the risk. The remediation topics are
divided based on the type of trait.

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down
its severity level by addressing just one remediation topic. Your approach to risk remediation
depends on your organizational requirements and workloads.

###### Note

The remediation guidance provided in this topic might require additional consultation in other Microsoft Azure resources.

###### Contents

- [Misconfiguration traits for Azure Container apps](exposure-azure-container-app.md#misconfiguration "exposure-azure-container-app.md#misconfiguration")

  - [The Azure Container app has cleartext credentials in environment variables](exposure-azure-container-app.md#cleartext-credentials-present "exposure-azure-container-app.md#cleartext-credentials-present")
  - [The Azure Container app has an open network security group](exposure-azure-container-app.md#open-security-group "exposure-azure-container-app.md#open-security-group")
  - [The Azure Container app has a managed identity that does not follow least privilege](exposure-azure-container-app.md#managed-identity-over-privileged "exposure-azure-container-app.md#managed-identity-over-privileged")
  - [The role associated with the Azure Container app has an administrative access role assignment](exposure-azure-container-app.md#administrative-access-policy "exposure-azure-container-app.md#administrative-access-policy")

- [Reachability traits for Azure Container apps](exposure-azure-container-app.md#reachability "exposure-azure-container-app.md#reachability")

  - [The Azure Container app is reachable over the internet](exposure-azure-container-app.md#aca-internet-reachable "exposure-azure-container-app.md#aca-internet-reachable")

## Misconfiguration traits for Azure Container apps

Here are misconfiguration traits for Azure Container apps and suggested remediation steps.

### The Azure Container app has cleartext credentials in environment variables

The Container app passes secret data, such as connection strings, API keys, or passwords, to the container as plaintext environment variables.
Configuration, logs, or a compromised container can expose cleartext credentials in environment variables, which lets an attacker reuse them to access other systems.
Following standard security principles, we recommend that you store sensitive values as secrets and reference them rather than embedding them in plaintext.

###### Move credentials to secrets

Replace plaintext environment variable values with Container app secrets, or reference secrets stored in Azure Key Vault. Update the container to read the values from those secret references. Rotate any credentials that were previously exposed in plaintext. For more information, see [Manage secrets in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets "https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets") in the Microsoft Azure documentation.

###### Use a managed identity where possible

For connections to Azure services that support it, use the Container app's managed identity instead of storing a secret at all. For more information, see [Managed identities in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/managed-identity "https://learn.microsoft.com/en-us/azure/container-apps/managed-identity") in the Microsoft Azure documentation.

### The Azure Container app has an open network security group

The network security group protecting the Container app's environment contains rules that allow unrestricted access from any source (for example, a source of `Any` or `0.0.0.0/0`).
An open network security group exposes the Container app's environment to unauthorized access from the internet.
Following standard security principles, we recommend that you restrict network security group rules to only the specific IP addresses, ports, and protocols that your workload requires.

###### Restrict network security group rules

Review the network security group associated with the Container app environment's subnet, and modify or remove rules that allow unrestricted access. Replace a broad source such as `Any` with the specific trusted ranges your workload requires. For more information, see [Networking in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/networking "https://learn.microsoft.com/en-us/azure/container-apps/networking") in the Microsoft Azure documentation.

###### Set IP ingress restrictions

In addition to network security group rules on the environment subnet, configure IP ingress restrictions on the container app itself to allow or deny inbound traffic by IP address range. For more information, see [Set up IP ingress restrictions in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/ip-restrictions "https://learn.microsoft.com/en-us/azure/container-apps/ip-restrictions") in the Microsoft Azure documentation.

### The Azure Container app has a managed identity that does not follow least privilege

The Container app has a managed identity that is granted more access than the workload requires.
An over-privileged managed identity widens the blast radius if the Container app is compromised, because an attacker can act with all of the identity's permissions.
Following standard security principles, we recommend that you grant the identity only the permissions the workload needs, at the narrowest scope.

###### Scope the managed identity to least privilege

Review the role assignments granted to the Container app's managed identity and remove any that aren't required. Assign the least-privileged built-in role at the narrowest scope (resource or resource group) that meets your needs. For more information, see [Best practices for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices "https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices") in the Microsoft Azure documentation.

### The role associated with the Azure Container app has an administrative access role assignment

The managed identity associated with the Container app has an administrative role assignment (such as `Owner` or `Contributor`) at a broad scope. This assignment typically grants permissions far beyond what the workload requires.
If the Container app is compromised, an attacker can use these excessive permissions to move laterally across your environment, access data, or manipulate resources.
Following standard security principles, we recommend that you grant least privilege by assigning only the permissions the app needs.

###### Review and identify administrative role assignments

In the Azure portal, review the role assignments for the identity associated with the Container app. Look for privileged administrator roles such as `Owner`, `Contributor`, or `User Access Administrator`, and for custom roles that use a wildcard (`*`) in their `Actions`. For more information, see [List Azure role assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-portal "https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-portal") in the Microsoft Azure documentation.

###### Implement least privilege access

Replace administrative role assignments with the least-privileged built-in role that grants only the permissions the app requires, and assign it at the narrowest scope that meets your needs. For more information, see [Best practices for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices "https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices") in the Microsoft Azure documentation.

## Reachability traits for Azure Container apps

Here are reachability traits for Azure Container apps and suggested remediation steps.

### The Azure Container app is reachable over the internet

The Container app is reachable from the public internet, either because external ingress is enabled (`ingress.external` is set to `true`) or because its environment has a public IP address.
Public reachability increases the attack surface of the Container app and exposes it to unauthorized requests.
Following standard security principles, we recommend that you disable external ingress where it isn't required, use an internal environment, or place the app behind a controlled, authenticated ingress point.

###### Restrict or remove external ingress

Set ingress to internal if the app only needs to be reached from within your virtual network or environment. If public access is required, restrict it with ingress IP restrictions. Front the app with a gateway such as Azure Application Gateway or Azure Front Door. These gateways provide authentication and a web application firewall. For more information, see [Ingress in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/ingress-overview "https://learn.microsoft.com/en-us/azure/container-apps/ingress-overview") in the Microsoft Azure documentation.

###### Use an internal environment

To avoid assigning a public IP address, deploy the Container app into an internal (virtual network–integrated) environment that uses a private IP address, and expose only the endpoints that must be public through a controlled ingress point. For more information, see [Networking in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/networking "https://learn.microsoft.com/en-us/azure/container-apps/networking") in the Microsoft Azure documentation.

###### Require HTTPS and authentication for public ingress

When ingress must remain public, disable insecure connections (set `allowInsecure` to `false`) so that traffic is served only over HTTPS. Enable the built-in authentication feature with Microsoft Entra ID so that unauthenticated requests are rejected. For more information, see [Authentication and authorization in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/authentication "https://learn.microsoft.com/en-us/azure/container-apps/authentication") in the Microsoft Azure documentation.
