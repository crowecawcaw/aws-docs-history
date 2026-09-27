

# Quick Create for AWS Shield Advanced
<a name="managing-shield-quick-create"></a>

With Quick Create, you define and deploy AWS Shield Advanced protections in a single guided workflow. Use Quick Create when you want to set up DDoS protection from policies through deployment in one session.

To define and deploy an AWS Shield Advanced protection with Quick Create, complete the following procedures in order.

**To create the policy and configure protections**  


Complete the following steps:

1. Open the AWS Network Security Manager console at [https://console.aws.amazon.com/network-security-manager/](https://console.aws.amazon.com/network-security-manager/).

1. In the navigation pane, choose **Overview**.

1. On the **Overview** page, choose **Quick create and deploy**. The **Quick create and deploy** page appears with multiple panes.

1. In the **Policy details** pane, for **Name**, enter a policy name. (Optional) For **Description**, enter a description.

1. In the **Define protections** pane, choose the firewall type that you want to work with. Select **AWS Shield Advanced**.

1. Under **Policy configuration** in the **Define protections** pane, decide the automated actions that AWS Network Security Manager takes in the targeted scope:
   + **Remediation** applies the defined policy to any resources whose security state does not match the desired state that AWS Network Security Manager describes.
   + **Resource cleanup** deletes the DDoS protection that AWS Network Security Manager created for a resource when the deployment is removed, or when the account or resource is out of scope.
   + **Existing customer DDoS resolution** determines how to resolve conflicts between the policy that you are defining and what might already be deployed. From the menu, choose one of the following options:
     + **No remediation** skips remediation on any resources that already have a DDoS protection.
     + **Override association** replaces the existing DDoS protection with the AWS Network Security Manager created DDoS protection.
     + **Retrofit** retrofits its rules onto each existing DDoS protection and keeps the DDoS protection associated with the resource.

1. In the **Policy priority** pane, set the priority. AWS Network Security Manager evaluates policies according to their priority to resolve conflicts. Lower positions (lower integers) have a higher priority.

   To edit the priority, choose the **Position** value. Then increment it with the arrows, or enter a value directly. To confirm the selection, choose **Confirm**. To discard the change, choose **Cancel**.

**To set the scope**  


Complete the following steps:

1. In the **Set the scope** pane, define the set of assets that the policies apply to. For **Scope name**, enter a name. (Optional) For **Description**, enter a description.

1. 
**Multi-account mode only**  
This step applies to multi-account mode only. In multi-account mode, use the **Account and organizational unit selection** sub-pane to choose which accounts or OUs to include or exclude. In single-account mode, this sub-pane does not appear in the console, so skip this step.

   In the account and organizational unit selection sub-pane, select one of the following options:
   + Scope to the entire AWS Organization. No further definition is required.
   + Scope to the entire AWS Organization but exclude specific OUs and accounts. An **Organizational units** sub-pane and an **Accounts** sub-pane appear. To exclude organizational units, choose **Add OUs**. Select the organizational units in the organization tree, and then choose **Add OUs**. To exclude individual accounts, choose **Add accounts**. Select the accounts in the organization tree, and then choose **Add accounts**.
   + Do not scope to the entire AWS Organization, and only include specific OUs and accounts. Use the same **Add OUs** and **Add accounts** mechanism to include the organizational units and accounts that you want.

1. In the **Resources** sub-pane, for **Resource types**, select all or specific AWS Shield Advanced resource types. The options are one or more of the following:
   + **Application Load Balancer**
   + **CloudFront Distribution**
   + **Classic Load Balancer**
   + **Elastic IP address**

1. For each selected resource type, choose one of the following mutually exclusive options:
   + **Include all resources**
   + **Include specific resources**
   + **Exclude specific resources**

1. If you choose **Include specific resources**, choose one of the following expression types, and then build the appropriate combinations of tags or ARNs:
   + **Single criteria**
   + **Match all criteria (AND)**
   + **Match any criteria (OR)**
   + **NOT**

   All resource types have the **Tag** and **ARN** inclusion criteria. If you choose **Tag**, enter a **Key** and an optional **Value**. You can identify multiple tags.

**CloudFront Region requirement**  
To protect **CloudFront Distribution** resources, use the US East (N. Virginia) Region (`us-east-1`).

**To review and deploy the policy**  


Complete the following steps:

1. In the **Review and deploy** pane, for **Deployment name**, enter a name. (Optional) For **Description**, enter a description. To determine whether the content of your deployment is visible to other accounts in your organization, select **Enable cross-account visibility for this deployment**.

1. (Optional) To add tags to your resource, choose **Add new tag**, and then enter **Key** and optional **Value** combinations.

1. To create and deploy the policy and scope, choose **Create and deploy**. When the process is complete, the **Deployments** page appears, where you can see the details of what AWS Network Security Manager created.

**Deployments might incur charges**  
A deployment creates network security services and attaches them to a protected resource. AWS Network Security Manager charges for protected resources. The security services themselves protect the resource, which incurs additional charges. Before you deploy, review the [AWS Network Security Manager pricing page](https://aws.amazon.com/network-security-manager/pricing/) and the [AWS Shield Advanced pricing page](https://aws.amazon.com/shield/pricing/).