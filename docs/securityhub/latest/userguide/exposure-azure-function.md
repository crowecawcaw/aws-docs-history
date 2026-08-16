# Remediating exposures for Azure Function apps

AWS Security Hub can generate exposure findings for Azure Function apps.

On the Security Hub console, the Azure Function app involved in an exposure finding and its identifying information are listed in
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

- [Misconfiguration traits for Azure Function apps](exposure-azure-function.md#azure-functions-misconfiguration "exposure-azure-function.md#azure-functions-misconfiguration")

  - [The Azure Function app is deployed outside a VNet](exposure-azure-function.md#deployed-outside-vnet "exposure-azure-function.md#deployed-outside-vnet")
  - [The role associated with the Azure Function app has an administrative access role assignment](exposure-azure-function.md#administrative-access-policy "exposure-azure-function.md#administrative-access-policy")

- [Reachability traits for Azure Function apps](exposure-azure-function.md#azure-functions-reachability "exposure-azure-function.md#azure-functions-reachability")

  - [The Azure Function app allows anonymous HTTP trigger invocation](exposure-azure-function.md#publicly-invocable "exposure-azure-function.md#publicly-invocable")

- [Vulnerability traits for Azure Function apps](exposure-azure-function.md#vulnerability "exposure-azure-function.md#vulnerability")

  - [The Azure Function app has network-exploitable software vulnerabilities with a high likelihood of exploitation](exposure-azure-function.md#high-priority-vulnerability "exposure-azure-function.md#high-priority-vulnerability")
  - [The Azure Function app has software vulnerabilities](exposure-azure-function.md#low-priority-vulnerability "exposure-azure-function.md#low-priority-vulnerability")
  - [The Azure Function app has malicious software packages](exposure-azure-function.md#malicious-package "exposure-azure-function.md#malicious-package")

## Misconfiguration traits for Azure Function apps

Here are misconfiguration traits for Azure Function apps and suggested remediation steps.

### The Azure Function app is deployed outside a VNet

When a Function app is not integrated with a virtual network, its endpoints and outbound traffic traverse the public network rather than your private network boundary.
When the Function app is not integrated with a virtual network, you cannot apply network-level controls such as private endpoints, network security groups, and restricted outbound access. This gap increases the app's exposure.
Following standard security principles, integrate the Function app with a virtual network and use private endpoints where your hosting plan supports it.

###### Remediation

Take one or more of the following actions to address this exposure:

###### Integrate the Function app with a virtual network

Enable virtual network integration for the Function app. Where supported by your hosting plan (Flex Consumption, Elastic Premium, or Dedicated), use private endpoints so the app is reachable only from within your network. For more information, see [Azure Functions networking options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options "https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options") in the Microsoft Azure documentation.

###### Restrict inbound access

On hosting plans that do not support private endpoints, use access restrictions to allow inbound traffic only from trusted IP address ranges, and disable public network access where it is not required. For more information, see [Set up access restrictions](https://learn.microsoft.com/en-us/azure/app-service/app-service-ip-restrictions "https://learn.microsoft.com/en-us/azure/app-service/app-service-ip-restrictions") in the Microsoft Azure documentation.

### The role associated with the Azure Function app has an administrative access role assignment

You can assign a managed identity to an Azure Function app and grant it Azure role-based access control (Azure RBAC) role assignments to access other Azure resources.
When the associated identity has an administrative role assignment (such as `Owner` or `Contributor`) at a broad scope, it typically grants permissions far beyond what the app requires.
If the Function app is compromised, an attacker can use these excessive permissions to move laterally across your environment, access data, or manipulate resources.
Following standard security principles, grant least privilege by assigning only the permissions the app needs.

###### Remediation

Take one or more of the following actions to address this exposure:

###### Review and identify administrative role assignments

In the Azure portal, review the role assignments for the identity associated with the Function app. Look for privileged administrator roles such as `Owner`, `Contributor`, or `User Access Administrator`, and for custom roles that use a wildcard (`*`) in their `Actions`. For more information, see [List Azure role assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-portal "https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-portal") in the Microsoft Azure documentation.

###### Implement least privilege access

Replace administrative role assignments with the least-privileged built-in role that grants only the permissions the app requires, and assign it at the narrowest scope that meets your needs. Use a managed identity instead of stored secrets for connections to other Azure services. For more information, see [Best practices for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices "https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices") in the Microsoft Azure documentation.

## Reachability traits for Azure Function apps

Here are reachability traits for Azure Function apps and suggested remediation steps.

### The Azure Function app allows anonymous HTTP trigger invocation

An HTTP-triggered function whose authorization level is set to `anonymous` can be invoked over the internet without any access key or authentication.
Anonymous HTTP triggers expose your function logic to unauthenticated callers, which can lead to abuse, data exposure, or denial-of-wallet through uncontrolled invocation.
Following standard security principles, require authentication or access keys for HTTP-triggered functions unless anonymous access is explicitly required.

###### Remediation

Take one or more of the following actions to address this exposure:

###### Require authorization for HTTP triggers

Raise the HTTP trigger authorization level from `anonymous` to `function` or `admin` so that requests must include a valid access key, and require HTTPS. For stronger protection, enable App Service Authentication/Authorization or front the app with Azure API Management. For more information, see [Securing Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/security-concepts "https://learn.microsoft.com/en-us/azure/azure-functions/security-concepts") in the Microsoft Azure documentation.

###### Require authentication with a managed identity provider

Because access keys are an authorization control rather than authentication, enable App Service Authentication (Easy Auth) with Microsoft Entra ID so that callers must present a valid identity. Also disable the administrative endpoints (the `/admin` routes) when they are not needed. For more information, see [Securing Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/security-concepts "https://learn.microsoft.com/en-us/azure/azure-functions/security-concepts") in the Microsoft Azure documentation.

## Vulnerability traits for Azure Function apps

Here are vulnerability traits for Azure Function apps and suggested remediation steps.

### The Azure Function app has network-exploitable software vulnerabilities with a high likelihood of exploitation

Common Vulnerabilities and Exposures (CVEs) can affect software packages and dependencies in your Function app.
A high-priority vulnerability is network-exploitable with a high likelihood of exploitation, which represents an immediate security threat because exploit code might already be publicly available and actively used by attackers.
Patch these vulnerabilities promptly to protect your Function app.

###### Remediation

Take one or more of the following actions to address this exposure:

###### Update affected dependencies

Review the affected CVEs in the finding, then update the vulnerable packages and dependencies to their latest secure versions and redeploy the app. Keep the Function app on a supported runtime so that platform security updates continue to apply. For more information, see [Microsoft Defender for App Service](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-app-service-introduction "https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-app-service-introduction") in the Microsoft Azure documentation.

###### Future considerations

To prevent future occurrences, integrate dependency and vulnerability scanning into your build and deployment pipeline, and use Microsoft Defender for Cloud to monitor your app for configuration and vulnerability findings. For more information, see [Microsoft Defender for App Service](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-app-service-introduction "https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-app-service-introduction") in the Microsoft Azure documentation.

### The Azure Function app has software vulnerabilities

Common Vulnerabilities and Exposures (CVEs) can affect software packages and dependencies in your Function app.
Noncritical vulnerabilities represent security weaknesses with lower severity or exploitability than high-priority vulnerabilities. Although they pose less immediate risk, attackers can still exploit unpatched vulnerabilities to compromise the confidentiality, integrity, or availability of data, or to access other systems.
Following security best practices, patch these vulnerabilities to protect your Function app.

###### Remediation: Update affected dependencies

Update the vulnerable packages and dependencies to their latest secure versions and redeploy the app. If an update is not available, consider removing or disabling the vulnerable component until a patch is released. For more information, see [Microsoft Defender for App Service](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-app-service-introduction "https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-app-service-introduction") in the Microsoft Azure documentation.

### The Azure Function app has malicious software packages

Malicious packages are software components that contain harmful code designed to compromise the confidentiality, integrity, and availability of your systems and data.
Malicious packages pose an active and critical threat to your Function app, because attackers can execute the malicious code automatically without exploiting a separate vulnerability.
Following security best practices, remove malicious packages to protect your Function app from potential attacks.

###### Remediation: Investigate and remove malicious packages

Review the finding details to identify the affected packages, remove them from your project dependencies, rebuild from a trusted source, and redeploy the app. After remediation, audit your dependency supply chain to confirm no related malicious components remain. For more information, see [Microsoft Defender for App Service](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-app-service-introduction "https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-app-service-introduction") in the Microsoft Azure documentation.
