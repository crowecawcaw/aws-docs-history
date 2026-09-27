

# Standard creation process for AWS Shield Advanced
<a name="managing-shield-standard"></a>

With the standard creation process, you set up each AWS Shield Advanced component—policies, scopes, and deployments—individually for full control. Use this approach when you want to create reusable components and combine them as needed.

An AWS Shield Advanced policy is simple and does not contain rules, rule groups, or templates. When you apply the policy, AWS Network Security Manager creates an AWS Shield Advanced DDoS protection in each in-scope account. For information about how AWS Network Security Manager works, see [How AWS Network Security Manager works](concepts.md).

**To create a policy (console)**  


Complete the following steps:

1. Sign in to the AWS Management Console using your AWS Network Security Manager administrator account, and then open the AWS Network Security Manager console at [https://console.aws.amazon.com/network-security-manager/](https://console.aws.amazon.com/network-security-manager/).
**Administrator account setup**  
For information about setting up an AWS Network Security Manager administrator account, see [Setting up AWS Network Security Manager](setting-up.md).

1. In the navigation pane, choose **AWS Network Security Manager**, then **Overview**.

1. In the **Overview** pane, choose **Create policy**. Enter a **Name** and an optional **Description**, and then choose a **Firewall type** (in this case, **AWS Shield Advanced**).

1. In the **Policy priority** pane, set the priority. AWS Network Security Manager evaluates policies according to their priority to resolve conflicts. Lower positions (lower integers) have a higher priority.

   To edit the priority, choose the **Position** value. Then increment it with the arrows, or enter a value directly. To confirm the selection, choose **Confirm**. To discard the change, choose **Cancel**.

1. In the **Policy configuration** pane, decide the automated actions that AWS Network Security Manager takes in the targeted scope:
   + **Remediation** applies the defined policy to any resources whose security state does not match the desired state that AWS Network Security Manager describes.
   + **Resource cleanup** deletes the DDoS protection that AWS Network Security Manager created for a resource when the deployment is removed, or when the account or resource is out of scope.
   + **Existing customer DDoS resolution** determines how to resolve conflicts between the policy that you are defining and what might already be deployed. From the menu, choose one of the following options:
     + **No remediation** skips remediation on any resources that already have a DDoS protection.
     + **Override association** replaces the existing DDoS protection with the AWS Network Security Manager created DDoS protection.
     + **Retrofit** retrofits its rules onto each existing DDoS protection and keeps the DDoS protection associated with the resource.

**To create a scope (console)**  


Complete the following steps:

1. In the **Scope details** pane, enter a **Scope name** and an optional **Description**.

1. 
**Multi-account mode only**  
This step applies to multi-account mode only. In multi-account mode, use the **Account and organizational unit selection** sub-pane to choose which accounts or OUs to include or exclude. In single-account mode, this sub-pane does not appear in the console, so skip this step.

   In the **Account and organizational unit selection** pane, choose one of three methods for controlling administrative scope:
   + **Scope to entire AWS Organization (all OUs and accounts)** – No further definition is required.
   + **Scope to entire AWS Organization but exclude specific OUs and accounts** – Two sub-panes appear, one for **Organizational units** and one for **Accounts**. Choose **Add OUs** to open the **Add OUs** window, select the organizational units you need, and then choose **Add OUs**. To add individual accounts, in the **Accounts** sub-pane, choose **Add accounts**, select the accounts, and then choose **Add accounts**.
   + **Do not scope to entire AWS Organization, only include specific OUs and accounts** – Use the same sub-panes to add OUs or accounts.

1. Next, select resources in the **Resources** sub-pane. In the **Resource types** selection box, select all or specific AWS Shield Advanced resource types. For AWS Shield Advanced, the options are any or all of the following:
   + **Application Load Balancer**
   + **CloudFront Distribution**
   + **Classic Load Balancer**
   + **Elastic IP address**

1. For each selected resource type, choose one of the following mutually exclusive options:
   + **Include all resources**
   + **Include specific resources**
   + **Exclude specific resources**

1. If you choose **Include specific resources**, select one of the following expression types:
   + **Single criteria**
   + **Match all criteria (AND)**
   + **Match any criteria (OR)**
   + **NOT**

1. Each expression type supports single or multiple inclusion criteria and ARNs, so you can build combinations of tags or ARNs. All resource types support the **Tag** and **ARN** inclusion criteria. If you choose **Tag**, identify a **Key** and an optional **Value**. You can identify multiple tags.

**CloudFront Region requirement**  
To protect **CloudFront Distribution** resources, use the US East (N. Virginia) Region (`us-east-1`).

**To create a deployment (console)**  


A deployment binds your policies to a scope and activates enforcement. AWS Network Security Manager then applies your AWS Shield Advanced DDoS protections to the in-scope resources.

Complete the following steps:

1. On the **Overview** page, in the **Overview** pane, choose **Create deployment**.

1. Choose the policy that you want to deploy.

1. Choose the scope that defines the accounts and resources where AWS Network Security Manager applies the policy.

1. For **Deployment name**, enter a name. (Optional) For **Description**, enter a description.

1. (Optional) To make the deployment visible to other accounts in your organization, select **Enable cross-account visibility for this deployment**.

1. (Optional) To add tags, choose **Add new tag**, and then enter **Key** and optional **Value** combinations.

1. Choose **Create and deploy**. The **Deployments** page appears, where you can see the details of what AWS Network Security Manager created.

**Deployments might incur charges**  
A deployment creates network security services and attaches them to a protected resource. AWS Network Security Manager charges for protected resources. The security services themselves protect the resource, which incurs additional charges. Before you deploy, review the [AWS Network Security Manager pricing page](https://aws.amazon.com/network-security-manager/pricing/) and the [AWS Shield Advanced pricing page](https://aws.amazon.com/shield/pricing/).