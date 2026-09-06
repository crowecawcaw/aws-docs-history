

# Manage security requirements
<a name="security-requirements"></a>

Organize the security requirements that AWS Security Agent uses to analyze your applications into security requirement packs. A pack is a collection of security requirements. You can enable AWS-managed packs, create your own custom packs, and generate requirements for a custom pack by uploading your security documentation.

## Overview
<a name="_overview"></a>

A security requirement defines a security standard or policy that AWS Security Agent evaluates your application against during design reviews and code reviews. Code reviews include full scans of your entire codebase and differential (diff) scans of only the changed code. When a design or code does not meet a requirement, AWS Security Agent reports a finding. Every security requirement belongs to a security requirement pack and is shared across all Agent Spaces.

 AWS Security Agent provides two types of packs, shown on separate tabs:
+  **Managed security requirements packs** – AWS-provided packs of security requirements based on industry standards and best practices. You can enable these packs instantly to evaluate against common security policies without custom configuration. The requirements in a managed pack are read-only. You can use an AWS-managed requirement as a template for a custom requirement. For the list of available managed packs, see [AWS managed security requirement packs](security-requirement-managed-packs.md).
+  **Custom security requirements packs** – Packs that you create to enforce your organization’s specific policies and standards. You build the requirements in a custom pack from scratch, customize AWS-managed requirements as a starting point, or generate them by uploading your security documentation.

**Note**  
The compliance framework packs are designed to help identify security requirements that may be relevant for compliance with certain frameworks. They do not assess your compliance or guarantee that you will pass an audit.

You enable and disable packs as a unit. When a pack is enabled, AWS Security Agent evaluates your applications against the requirements in that pack during design and code reviews.

**Note**  
Enabling or disabling a pack applies to new design reviews and code reviews. Existing reviews are not affected.

## Enable or disable a managed pack
<a name="_enable_or_disable_a_managed_pack"></a>

Enable an AWS-managed pack to evaluate your applications against a set of AWS-maintained security requirements. Disable it when you no longer need it.

1. In the AWS console, navigate to AWS Security Agent.

1. In the navigation pane, choose **Security requirements**.

1. Choose the **Managed security requirements packs** tab.

1. Select the pack you want to enable or disable.

1. Do one of the following:

   1. To enable the pack, choose **Enable pack**.

   1. To disable the pack, choose **Disable pack**.

**Tip**  
Choose a pack to view the security requirements it contains. Choose a requirement to view its full definition, including its applicability, compliance criteria, and remediation guidance.

## Create a custom pack
<a name="_create_a_custom_pack"></a>

Create a custom pack to group security requirements that are specific to your organization. After you create the pack, add requirements to it manually, customize an AWS-managed requirement, or upload documents to generate requirements.

1. In the AWS console, navigate to AWS Security Agent.

1. In the navigation pane, choose **Security requirements**.

1. Choose the **Custom security requirements packs** tab.

1. Choose **Create security requirements pack**.

1. Enter a **Security requirement pack name** and an optional description.

1. Choose **Create security requirement pack**.

**Note**  
After you create a pack, you can add or upload source documents to generate the security requirements for your pack.

## Add a security requirement manually
<a name="_add_a_security_requirement_manually"></a>

Add a security requirement to a custom pack to define a security standard that AWS Security Agent enforces.

1. In the AWS console, navigate to AWS Security Agent.

1. In the navigation pane, choose **Security requirements**.

1. Choose the **Custom security requirements packs** tab, and then choose the pack you want to add a requirement to.

1. Choose **Add requirement manually**.

1. Configure the following fields:

   1.  **Security requirement name** – Enter a descriptive name that identifies the security control, for example `enforce-encryption-at-rest` (maximum 80 characters).

   1.  **Description** – Provide a brief description of what this security requirement checks (maximum 500 characters).

   1.  **Applicability** – Describe the scenarios, system types, or conditions where this security requirement should be evaluated. Include the scenarios where the requirement should be marked NOT\_APPLICABLE (maximum 10,000 characters).

   1.  **Compliance criteria** – Define what constitutes compliance versus non-compliance for this security requirement. Provide the indicators, examples, and technical details that AWS Security Agent looks for when it evaluates compliance (maximum 10,000 characters).

   1.  **Remediation guidance** (Optional) – Provide guidance on how to fix violations, including links to your organization’s internal documentation or standards (maximum 10,000 characters).

1. Do one of the following:

   1. To create the requirement without enabling it, choose **Create security requirement**.

   1. To create the requirement and enable it, choose **Create and enable security requirement**.

**Note**  
A requirement is evaluated during security reviews only when the pack that contains it is enabled. To control whether a pack is evaluated, enable or disable the pack.

## Customize an AWS-managed security requirement
<a name="customize_an_shared_aws_managed_security_requirement"></a>

Create a custom security requirement that uses an AWS-managed requirement as its starting point. AWS Security Agent pre-populates the requirement details from the managed requirement, and you edit them to fit your organization.

1. In the AWS console, navigate to AWS Security Agent.

1. In the navigation pane, choose **Security requirements**.

1. Choose the **Custom security requirements packs** tab, and then choose the custom pack to add the requirement to.

1. Choose **Create custom security requirement**.

1. To pre-populate the form, in the **Customize an AWS-managed security requirement** section, search for and select an AWS-managed requirement to use as a template.

1. Edit any of the fields to fit your organization’s needs.

1. Do one of the following:

   1. To create the requirement without enabling it, choose **Create security requirement**.

   1. To create and immediately enable the requirement, choose **Create and enable security requirement**.

**Note**  
Customizing an AWS-managed requirement creates an independent custom security requirement. Later changes to the AWS-managed requirement do not affect your custom version.

## Generate requirements by uploading documents
<a name="_generate_requirements_by_uploading_documents"></a>

Generate the security requirements for a custom pack from your existing security documentation instead of writing each requirement by hand. AWS Security Agent reads the documents you upload, identifies the security-relevant content, and generates structured requirements that you can review and edit. For the full procedure, see [Generate security requirements from documents](import-security-requirements.md). For guidance on what to include in the documents you upload, see [Prepare documents for requirement generation](prepare-import-documents.md).

**Important**  
Uploading new source documents regenerates all requirements for the pack. Any existing requirements, including ones you added manually, are replaced.

## Edit a custom security requirement
<a name="_edit_a_custom_security_requirement"></a>

Modify a custom security requirement to update its definition, criteria, or remediation guidance. You cannot edit the requirements in an AWS-managed pack.

1. In the AWS console, navigate to AWS Security Agent.

1. In the navigation pane, choose **Security requirements**.

1. Choose the **Custom security requirements packs** tab, and then choose the pack that contains the requirement.

1. Select the requirement you want to edit, and then choose **Edit custom security requirement**.

1. Update the requirement fields as needed. The security requirement name cannot be changed after creation.

1. Choose **Update security requirement**.

**Note**  
Changes to a security requirement apply to new design reviews and code reviews. Existing reviews are not affected.

## Enable or disable a pack
<a name="_enable_or_disable_a_pack"></a>

Enable or disable a security requirement pack to control whether AWS Security Agent evaluates the requirements it contains. You enable and disable packs as a unit.

1. In the AWS console, navigate to AWS Security Agent.

1. In the navigation pane, choose **Security requirements**.

1. Choose the tab for the type of pack, and then select the pack.

1. Do one of the following:

   1. To enable the pack, choose **Enable pack**.

   1. To disable the pack, choose **Disable pack**.

**Note**  
When a pack is enabled, the requirements in the pack are evaluated during security reviews. When a pack is disabled, its requirements are not evaluated.

## Delete a custom security requirement
<a name="_delete_a_custom_security_requirement"></a>

Delete a custom security requirement when you no longer want AWS Security Agent to evaluate it.

1. In the AWS console, navigate to AWS Security Agent.

1. In the navigation pane, choose **Security requirements**.

1. Choose the **Custom security requirements packs** tab, and then choose the pack that contains the requirement.

1. Select one or more security requirements, and then choose **Delete security requirement**.

1. Confirm the deletion.

**Note**  
When you delete security requirements, they are no longer evaluated in future reviews. The requirements remain visible in past reviews as read-only results.

## Best practices for defining security requirements
<a name="_best_practices_for_defining_security_requirements"></a>

When you create a security requirement, follow these guidelines to help AWS Security Agent evaluate your applications accurately and provide actionable findings.

 **Security requirement name** – Use a clear, specific name that identifies the security control. Avoid generic terms that do not convey the requirement’s purpose.

 **Description** – Explain what the control checks and the risk it mitigates. This helps users understand why the requirement matters.

 **Applicability** – Describe the workloads, system types, or conditions where the requirement should be evaluated. State when the requirement should be marked NOT\_APPLICABLE, with specific scenarios, to avoid false positives. Phrases such as "This control applies to ALL workloads that…​" and "Mark as NOT\_APPLICABLE if…​" set clear scope boundaries.

 **Compliance criteria** – Structure this in two parts: what demonstrates compliance and what indicates non-compliance. Be specific with technical indicators and include edge cases. Start with "A design is compliant if it demonstrates…​" followed by technical details, then "A design is non-compliant if it…​" with the patterns that indicate a violation.

 **Remediation guidance** – Provide guidance with technical details and configuration examples. Include links to your organization’s internal documentation so that developers have the resources they need to fix violations.

## Next steps
<a name="_next_steps"></a>

After you configure your security requirement packs:
+ Create a design review or code review to evaluate your application against the packs you enabled.
+ Enable penetration testing to complement your design and code reviews.
+ Grant users access to the AWS Security Agent web application.