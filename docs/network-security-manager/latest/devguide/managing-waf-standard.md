

# Standard creation process for AWS WAF
<a name="managing-waf-standard"></a>

With the standard creation process, you create each AWS WAF component—rules, templates, policies, scopes, and deployments—individually for full control. Use this approach when you want to create reusable components and combine them as needed.

An AWS Network Security Manager AWS WAF policy can contain rules and templates. When you apply the policy, AWS Network Security Manager creates a web ACL in each in-scope account.

**To create a rule (console)**  


1. Sign in to the AWS Management Console using your AWS Network Security Manager administrator account, and then open the AWS Network Security Manager console at [https://console.aws.amazon.com/network-security-manager/](https://console.aws.amazon.com/network-security-manager/).
**Administrator account setup**  
For information about setting up an AWS Network Security Manager administrator account, see [Setting up AWS Network Security Manager](setting-up.md).

1. In the navigation pane, choose **AWS Network Security Manager**, then **Overview**.

1. In the **Overview** pane, choose **Create rule**. Enter a descriptive name, and then enter an optional **Description**.

1. In the **Rule definition** pane, for **Firewall type**, choose **AWS WAF**.

1. For **Type of rule**, choose either **Inspection** or **Configuration**.

   If you choose **Inspection**, a JSON editor pane named **Define rule group reference** appears with the following options:
   + **Insert template** – Select a JSON template for **First (pre-process)** rules or **Last (post-process)** rules. When you make a selection, AWS Network Security Manager inserts the corresponding JSON into the editor, along with warning icons if inputs are required to complete the template.
   + **Insert rule group** – Presents a selection list driven by three options:
     + **An AWS Managed Rules (AMR) rule group**
     + **An existing custom rule group**
     + **An AWS Marketplace rule group**

     AWS Network Security Manager presents the rule groups associated with your choice, and you can select a single instance for inclusion. After you make the selection, choose **Select rule group**. AWS Network Security Manager inserts references to the inspection rule with the correct syntax into the JSON editor.
   + **Insert with AI** – Opens an overlay window named **AI configuration generator**. Use this tool to describe your rule in plain language, and AWS Network Security Manager generates the associated JSON in the editor. You can then review the generated code and choose to accept, modify, or delete the output.

1. (Optional) After your JSON rule definition is complete, you can associate a tag with your rule. Choose **Add new tag**, and then enter a **Key** and an optional **Value**.

1. When you finish your definitions, choose either **Save draft** to save an inactive, potentially incomplete object, or **Create rule**.
**Web ACL names are permanent**  
You cannot change a web ACL name after you create it. If you update your policy's name, AWS Network Security Manager does not update the associated web ACL name. To have AWS Network Security Manager create a web ACL with a different name, you must create a new policy.

**To create a template (console)**  


A template assembles rules in priority order for evaluation within a policy. You can organize your rule types into groupings that align with your security goals. You can also let different teams build security control statements that align with their responsibilities and skills.

1. On the **Overview** page, in the **Overview** pane, choose **Create template**. On the **Create template** page, enter a **Template name**, enter an optional **Description**, and choose a **Firewall type** (in this case, **AWS WAF**).

1. When you choose a **Firewall type**, the **Rules** pane appears. Choose one of the two **Add rules** buttons to open a list of available rules. Select the check box to the left of a rule **Name** to add it to the template. To choose a specific version of a rule, select the **Version** field of the rule. If multiple versions are available, select the version you want, and then choose **Confirm**.

1. (Optional) Create a tag for the template. When you finish, choose either **Save draft** or **Create template**. To continue to create a policy, choose **Create template**.

**To create a policy (console)**  


This is the final step of policy definition and preparation for deployment.

1. On the **Overview** page, in the **Overview** pane, choose **Create policy**. On the **Create policy** page, enter a **Name** and an optional **Description**, and then choose a **Firewall type** (in this case, **AWS WAF**).

1. In the **Policy priority** pane, set the priority. AWS Network Security Manager evaluates policies according to their priority to resolve conflicts. Lower positions (lower integers) have a higher priority. To edit the priority, choose the **Position** value. Then increment it with the arrows, or enter a value directly. To confirm the selection, choose **Confirm**. To discard the change, choose **Cancel**.

1. In the **Policy configuration** pane, decide the automated actions that AWS Network Security Manager takes in the targeted scope:
   + **Remediation** applies the defined policy to any resources whose security state is not synchronized with the desired state that is described in AWS Network Security Manager.
   + **Resource cleanup** deletes the firewall that AWS Network Security Manager created for a resource when the deployment is removed, or when the account or resource is out of scope.
   + **Existing customer WebACL resolution** determines how to resolve conflicts between the policy that you are defining and what might already be deployed. From the menu, choose one of the following options:
     + **No remediation** skips remediation on any resources that already have a web ACL.
     + **Override association** replaces the existing web ACL with the AWS Network Security Manager created web ACL.
     + **Retrofit** retrofits its rules onto each existing web ACL and keeps the web ACL associated with the resource.

1. After these configuration settings are complete, select the rules and templates that you want to add to the policy. In the **Templates and rules** pane, choose **Add rules** or **Add templates** to populate the policy. Both processes open a window that operates the same way as the rule selection process described earlier in this section.

**To create a scope (console)**  


1. You can start this step from the **Overview** page or from other areas within the tool. In the **Scope details** pane, enter a **Scope name** and an optional **Description**.

1. 
**Multi-account mode only**  
This step applies to multi-account mode only. In multi-account mode, use the **Account and organizational unit selection** sub-pane to choose which accounts or OUs to include or exclude. In single-account mode, this sub-pane does not appear in the console, so skip this step.

   In the **Account and organizational unit selection** pane, choose one of three methods for controlling administrative scope:
   + **Scope to entire AWS Organization (all OUs and accounts)** – No further definition is required.
   + **Scope to entire AWS Organization but exclude specific OUs and accounts** – Two sub-panes appear, one for **Organizational units** and one for **Accounts**. Choose **Add OUs** to open the **Add OUs** window, select the organizational units you need from the organization tree, and then choose **Add OUs**. To add individual accounts, in the **Accounts** sub-pane, choose **Add accounts**, select the accounts from the organization tree, and then choose **Add accounts**.
   + **Do not scope to entire AWS Organization, only include specific OUs and accounts** – Use the same sub-panes to add OUs or accounts with the same mechanism described for the preceding option.

1. Next, select resources in the **Resources** sub-pane. In the **Resource types** selection box, select all or specific AWS WAF resource types. For AWS WAF, the options are any or all of the following:
   + **Application Load Balancer**
   + **Amazon API Gateway REST API**
   + **CloudFront Distribution**
**CloudFront Region requirement**  
To protect **CloudFront Distribution** resources, use the US East (N. Virginia) Region (`us-east-1`).
**Global and regional resource types**  
You can select the global resource type (**CloudFront Distribution**) or the regional resource types (**Application Load Balancer** and **Amazon API Gateway REST API**), but not both. After you select a resource type, you can't switch between **CloudFront Distribution** and the regional resource types when you update the configuration.
**Unmanaged CloudFront resources**  
AWS Network Security Manager doesn't manage CloudFront distributions that use the CloudFront flat-rate pricing plan or CloudFront staging distributions. These resources appear out of synchronization.

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

1. For an **Application Load Balancer**, an additional **Configuration** criterion appears. Within **Configuration**, you can set a **Scheme** with the options **Internet-facing** or **Internal**.

**To create a deployment (console)**  


A deployment binds your policies to a scope and activates enforcement, which causes AWS Network Security Manager to apply your AWS WAF rules to the in-scope resources.

1. On the **Overview** page, in the **Overview** pane, choose **Create deployment**. You can also start this step from other areas within the tool.

1. Choose the policy that you want to deploy.

1. Choose the scope that defines the accounts and resources where AWS Network Security Manager applies the policy.

1. For **Deployment name**, enter a name. (Optional) For **Description**, enter a description.

1. (Optional) To make the deployment visible to other accounts in your organization, select **Enable cross-account visibility for this deployment**.

1. (Optional) To add tags, choose **Add new tag**, and then enter **Key** and optional **Value** combinations.

1. Choose **Create and deploy**. The **Deployments** page appears, where you can see the details of what AWS Network Security Manager created.

**Deployments might incur charges**  
A deployment creates network security services and attaches them to a protected resource. AWS Network Security Manager charges for protected resources. The security services themselves protect the resource, which incurs additional charges. Before you deploy, review the [AWS Network Security Manager pricing page](https://aws.amazon.com/network-security-manager/pricing/) and the [AWS WAF pricing page](https://aws.amazon.com/waf/pricing/).