# Manage security requirements

Configure security requirements that AWS Security Agent uses to analyze your applications during design reviews and code reviews. You can enable AWS-managed requirements, customize them to fit your organization’s standards, or create custom requirements from scratch.

## Overview

Security requirements define the security standards and policies that AWS Security Agent enforces when analyzing your applications. When you conduct design reviews or code reviews, AWS Security Agent evaluates your application against these requirements and identifies potential compliance issues.

AWS Security Agent provides two types of security requirements:

- **Managed security requirements** – AWS-provided requirements based on industry standards and best practices. These requirements are ready to use and maintained by AWS.
- **Custom security requirements** – Requirements you define and maintain to address your organization’s specific security policies and standards.

You can customize managed requirements by creating a copy that you can modify, or create entirely new requirements tailored to your needs.

###### Tip

Click on any managed security requirement to view its full definition, including applicability criteria, compliance evaluation details, and remediation guidance.

## Enable or disable managed security requirements

Enable AWS-managed security requirements to enforce industry-standard security policies in your design and code reviews. You can enable multiple requirements at once and disable them when they’re no longer needed.

1. In the AWS console, navigate to AWS Security Agent.
2. In the navigation pane, choose **Security requirements**.
3. Choose the **Managed security requirements** tab.
4. Select the checkbox next to one or more security requirements you want to enable or disable.
5. Do one of the following:
   1. To enable the selected requirements, choose **Enable**.
   2. To disable the selected requirements, choose **Disable**.

6. Verify the change in the **Status** column, which displays **Enabled** or **Disabled**.

###### Note

Enabled security requirements are immediately applied to new design reviews and code reviews. Existing reviews are not affected.

## Customize a managed security requirement

Create a customized copy of an AWS-managed security requirement when you want to modify it to match your organization’s specific standards. The customized requirement becomes a custom security requirement that you can edit and maintain.

1. In the AWS console, navigate to AWS Security Agent.
2. In the navigation pane, choose **Security requirements**.
3. Choose the **Managed security requirements** tab.
4. Select the checkbox next to the security requirement you want to customize.

###### Tip

You can only customize one requirement at a time. To customize multiple requirements, repeat this procedure for each one. 5. Choose **Customize**. 6. AWS Security Agent opens a **Create custom security requirement** form pre-populated with the managed requirement’s content. 7. (Optional) Edit any fields to customize the requirement for your organization’s needs. 8. Do one of the following:

    1. To create the requirement without enabling it, choose **Create security requirement**.
    2. To create and immediately enable the requirement for all future security reviews, choose **Create and enable security requirement**.

###### Note

Customizing a managed requirement creates an independent custom security requirement. Changes to the original managed requirement by AWS do not affect your custom version. Both the managed requirement and your custom version can be enabled simultaneously.

## Create a custom security requirement

Create a custom security requirement from scratch to enforce security policies unique to your organization that aren’t covered by AWS-managed requirements.

1. In the AWS console, navigate to AWS Security Agent.
2. In the navigation pane, choose **Security requirements**.
3. Choose the **Custom security requirements** tab.
4. Choose **Create security requirement**.
5. (Optional) To use a managed requirement as a template, in the **Customize a managed security requirement** section, search for and select a managed requirement.

###### Tip

Selecting a managed requirement pre-populates the form fields with that requirement’s details, which you can then modify to fit your needs. 6. In the **Security requirement details** section, configure the following fields:

    1. **Security requirement name** – Enter a descriptive name that clearly identifies the security control (maximum 80 characters).
    2. **Description** – Provide a concise summary of what this security requirement enforces and why it matters (maximum 500 characters).
    3. **Applicability** – Define when this requirement applies by specifying the types of workloads, systems, or conditions where it’s relevant. Include specific scenarios where the requirement should be marked NOT\_APPLICABLE (maximum 10,000 characters).
    4. **Compliance criteria** – Define what makes a design or code compliant versus non-compliant. Provide specific indicators, examples, and technical details that AWS Security Agent should look for when evaluating compliance (maximum 10,000 characters).
    5. **Remediation guidance** (Optional) – Provide step-by-step instructions for fixing violations, including specific technical details, configuration examples, and links to your organization’s internal documentation or standards (maximum 10,000 characters).

7. Do one of the following:
   1. To create the requirement without enabling it, choose **Create security requirement**.
   2. To create and immediately enable the requirement for all future security reviews, choose **Create and enable security requirement**.

###### Note

If you choose **Create security requirement** without enabling, the requirement appears in the Custom security requirements tab with a disabled status. You must manually enable it through the Custom security requirements tab before AWS Security Agent applies it to design and code reviews.

## Edit a custom security requirement

Modify an existing custom security requirement to update its definition, criteria, or remediation guidance.

1. In the AWS console, navigate to AWS Security Agent.
2. In the navigation pane, choose **Security requirements**.
3. Choose the **Custom security requirements** tab.
4. Select the custom security requirement you want to edit.
5. From the _Actions_ menu, select **Edit**.
6. Update any of the security requirement fields as needed.
7. Choose **Update security requirement**.

###### Note

Changes to custom security requirements are immediately applied to new design reviews and code reviews. Existing reviews are not affected.

## Enable or disable custom security requirements

Enable or disable your custom security requirements to control which policies AWS Security Agent enforces during security reviews.

1. In the AWS console, navigate to AWS Security Agent.
2. In the navigation pane, choose **Security requirements**.
3. Choose the **Custom security requirements** tab.
4. Select the checkbox next to one or more custom security requirements you want to enable or disable.
5. Do one of the following:
   1. To enable the selected requirements, from _Actions_ choose **Enable**.
   2. To disable the selected requirements, from _Actions_ choose **Disable**.

6. Verify the change in the **Status** column, which displays **Enabled** or shows disabled requirements.

## Best practices for defining security requirements

When creating or customizing security requirements, follow these guidelines to help AWS Security Agent accurately evaluate your applications and provide actionable findings.

**Security requirement name** – Use clear, specific names that identify the security control being enforced. Avoid generic terms that don’t convey the requirement’s purpose.

**Description** – Explain what the security control enforces and why it matters. Focus on the control’s purpose and the risk it mitigates to help users understand the requirement’s importance.

**Applicability** – Specify what types of workloads or systems this applies to and define the conditions that trigger evaluation. Clearly state when the requirement should be marked NOT_APPLICABLE with specific scenarios to avoid false positives. Use phrases like "This control applies to ALL workloads that…​" and "Mark as NOT_APPLICABLE if…​" to provide clear scope boundaries and handle edge cases.

**Compliance criteria** – Structure this in two parts: what demonstrates compliance and what indicates non-compliance. Be specific with technical indicators and include edge cases to help AWS Security Agent accurately evaluate your applications. Start with "A design is compliant if it demonstrates…​" followed by specific technical details, then "A design is clearly non-compliant if it…​" with patterns that indicate violations. This structure helps AWS Security Agent distinguish between compliant and non-compliant implementations.

**Remediation guidance** – Provide step-by-step instructions with specific technical details and configuration examples. Include links to your organization’s internal documentation or standards to give developers the resources they need to fix violations.

## Next steps

After configuring your security requirements:

- Enable penetration testing to complement your design and code reviews
- Configure the Agent Web App to provide users access to security capabilities
- Assign users to your agent through IAM Identity Center
