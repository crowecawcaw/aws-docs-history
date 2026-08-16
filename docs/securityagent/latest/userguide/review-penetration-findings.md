# Review findings from a penetration test

Monitor penetration test execution in real time on the Penetration Test Logs page after AWS Security Agent starts a penetration test. AWS Security Agent logs every action during the penetration test. After completion, review the penetration test summary, which includes application overview, coverage with identified endpoints, and risk assessment of security findings.

Evaluate security findings to address application vulnerabilities. Each finding contains impact assessment, severity rating, supporting evidence and remediation pull request details (when automatic code remediation is enabled).

## Prerequisites

Before you begin, ensure you have:

- A completed or in-progress penetration test run
- Access to the AWS Security Agent web application

## Step 1: Access the penetration test run

Navigate to your penetration test run to view overview, logs and findings pages.

1. Log in to the AWS Security Agent web application.
2. Navigate to the **Penetration tests** section.
3. Select the penetration test run you want to examine from the list.

###### Tip

The penetration test details page displays a summary of test status, completion date, and the number of findings identified.

## Step 2: Monitor test progress

Track the progress of your penetration test run using the step indicator.

1. Locate the horizontal step indicator below the page header.
2. Review the status of each testing phase:

   - **Preflight** – Initial setup and connectivity checks
   - **Static analysis** – Code and configuration analysis
   - **Pentests** – Runtime testing and vulnerability scanning
   - **Finalizing** – Final validation and report generation

###### Note

Each step displays a status indicator (Complete, In progress, or Pending). Findings are discovered and validated throughout the testing process, with new vulnerabilities appearing as each phase completes.

## Step 3: Navigate to the penetration test run overview tab

1. Run Summary section provides test status, duration and other high level details. It also provides a dashboard of security findings categorized by severity level and risk-types
2. Application overview by AWS Security Agent provides a summary of the penetration test run
3. Discovered endpoints by AWS Security Agent provides a list of all endpoints discovered and tested by the AWS Security agent during the penetration test run

## Step 4: Navigate to the penetration test logs tab

Access detailed logs of all actions AWS Security Agent executed during the penetration test.

1. The actions are categorized by action type and risk-types.
2. Select a specific action to view detailed logs:

   - **Testing Summary** – High-level summary of the agent actions and results
   - **Penetration test logs** – Detailed logs of all testing activities

Each task reports its own duration and task hours. For more information, see [Pricing and billing](pricing.md "pricing.md").

###### Note

Validator actions provide logs that validate findings in each category

###### Note

The Findings tab displays a split view with the findings list on the left and selected finding details on the right.

## Step 5: Navigate to the findings

Each finding in the list displays key information to help you quickly assess its importance.

###### Note

###### Default confidence filter

By default, you see only findings with **High** agent confidence. To also show findings with **Medium** or **Low** agent confidence and false positives, turn off the **Hiding unverified findings** toggle.

Review the information displayed on each finding card:

- **Finding name** – The title and identifier for the vulnerability
- **Confidence badge** – Indicates the agent’s confidence level in the finding (High, Medium, or Low)
- **Severity badge** – Shows the color-coded risk level (Critical, High, Medium, Low, or Informational). For what each level means, see [Severity ratings and CVSS metrics](severity-and-cvss.md "severity-and-cvss.md").
- **Last update timestamp** – Shows when the finding was last modified or validated
- **Description preview** – Brief summary of the vulnerability

###### Important

Prioritize findings with **Critical** or **High** severity badges and **High** confidence levels, as these represent validated vulnerabilities requiring immediate remediation.

## Step 6: Review finding details

Select individual findings to view comprehensive information about each vulnerability.

1. Select a finding name in the left panel to display its details in the right panel.
2. Review the validation status:

###### Note

If a finding displays the Unknown "This finding is not validated by AWS Security Agent yet," it means the vulnerability detection is still being confirmed. These findings may require manual verification. 3. Review the key attributes displayed at the top:

    * **Agent confidence** – The confidence level AWS Security Agent has in this finding
    * **Severity** – The risk level with a color-coded badge
    * **Finding logs** – Choose "Trace actions & logs" to view detailed execution logs and evidence
    * **Risk type** – The category or type of security risk (e.g., Authentication Bypass, SQL Injection)

4. Expand the **Description** section to read:

    * A detailed explanation of the vulnerability
    * How the vulnerability works
    * Why it represents a security risk
    * The potential impact on your application

5. Expand the **Risk Reasoning** section to see the CVSS metrics breakdown that shows how the severity was calculated. For what each metric means, see [Severity ratings and CVSS metrics](severity-and-cvss.md "severity-and-cvss.md"). 6. Expand the **Steps to reproduce** section to view:

    * Detailed technical steps to recreate the vulnerability
    * Request and response examples
    * Specific parameters or conditions that trigger the issue

7. The Verification Script section provides an executable way to reproduce the finding. Expand this section (when available) to view:

    * **Instructions** – How to set up and run the verification script
    * **Environment variables** – Lists the required variables you must configure before running the script. Sensitive values are redacted for security.
    * **Download Script** – Choose to download the executable verification script


    ###### Note

    Verification scripts are available only for confirmed vulnerabilities. The agent must have successfully generated and validated an executable reproduction script.


    ###### Note

    Verification scripts are generated using generative AI. Review the script before execution and run it only against systems you are authorized to test. For guidance on testing AI-generated scripts responsibly, see the [AWS Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/ "https://aws.amazon.com/ai/responsible-ai/policy/").


    ###### Tip

    The verification script provides an executable way to reproduce the finding independently. Set the required environment variables with your own credentials, then run the script against your target system to confirm the vulnerability exists.

###### Tip

Use the "Trace actions & logs" link to access the complete evidence package, including HTTP requests, responses, and exploitation attempts that demonstrate the vulnerability.

### Edit findings

You can edit any finding to correct its details or refine the agent’s assessment. The following fields are editable:

- **name** — The title of the finding
- **description** — Detailed description of the security vulnerability
- **status** — Current status of the finding
- **riskType** — Type of security risk identified
- **riskLevel** — Severity level (CRITICAL, HIGH, MEDIUM, LOW, INFORMATIONAL)
- **riskScore** — Numeric risk score
- **reasoning** — Justification for the assigned risk score
- **attackScript** — Proof-of-concept code demonstrating the vulnerability
- **customerNote** — Optional note explaining your rationale for the edit

To edit a finding:

1. Navigate to the finding detail page.
2. Choose the edit icon to modify any of the fields in the preceding list.
3. Save your changes.

###### Note

Your edits are saved immediately and reflected in the finding. If Findings Personalization is enabled, all editable fields you change will be used to refine the agent’s preferences for future runs.

### View the original agent version

When you edit a finding, a **Version selector** appears in the finding details header. This allows you to view the original agent assessment:

1. Locate the **Version selector** in the finding details header.
2. Select **Original** to view the finding as it was originally produced by the agent.
3. Select **Latest** to return to the current version with your edits applied.

### Review personalized findings

When Findings Personalization is enabled, AWS Security Agent learns from your edits to findings. The agent applies those preferences to similar findings in future penetration test runs. When a finding has been adjusted based on your previous edits, the details panel displays a **Personalization changes** section. For information about enabling this feature, see [Enable or disable Findings Personalization](#enable-or-disable-findings-personalization "#enable-or-disable-findings-personalization").

1. Locate the **Personalization changes** section in the finding details panel.

###### Note

The **Personalization changes** section appears only on findings that AWS Security Agent aligned to your previous edits. Findings that match no learned preference are shown exactly as the agent produced them, without this section. 2. Review the summary of what changed and why. The summary lists each adjusted attribute with its original agent-produced value, the personalized value, and the reasoning. For example:

_Based on your previous edits the following changes have been made to the finding originally produced by the system: Risk level changed from MEDIUM to CRITICAL; Risk score changed from 5.3 to 9.5; Reasoning: Upgraded severity to reflect full exposure of application source code through publicly accessible source maps._

1. Review the summary to understand how the finding was adjusted before deciding how to act on it.
2. To override a personalized finding, edit it again as you would any other finding (for example, change the severity or risk score). Your most recent edit always takes precedence: AWS Security Agent learns from it and applies the updated preference on the next run, replacing the earlier rule.

###### Note

Personalization changes adjust finding attributes such as riskLevel, riskScore, name, description, reasoning, and attackScript to reflect the standards AWS Security Agent learned from your edits. Any field you have previously edited may be adjusted on similar findings in future runs.

### How personalization learns from your edits

When Findings Personalization is enabled, AWS Security Agent learns from all edits you make to findings and applies similar adjustments to future runs. Any field you edit (as listed in the preceding [Edit findings](#edit-findings "#edit-findings") section) will be used to refine the agent’s learned preferences.

###### Note

For the **status** field, only marking a finding as **FALSE\_POSITIVE** is treated as a learnable preference. Changes to other status values do not trigger learning.

On the next penetration test run, the agent evaluates new findings against your learned preferences and applies adjustments where applicable. A **Personalization changes** section appears on any finding that was adjusted, explaining what was changed.

###### Note

Personalization only learns from edits made in the most recent completed penetration test run. The feature must be enabled at the time the penetration test starts for learning to occur. If you edit the same finding in a later run, the most recent edit takes precedence — the agent updates its preferences to reflect your latest decision.

### Enable or disable Findings Personalization

Findings Personalization is enabled by default. To disable or re-enable it:

1. Navigate to your penetration test configuration.
2. Locate the **Findings Personalization** toggle.
3. To enable Findings Personalization, turn on the toggle. To disable, turn it off.

When disabled, findings appear in their raw agent-produced state with no personalization applied. Previously learned preferences are preserved and will be applied again if the feature is re-enabled.

## Step 7: Prioritize and address findings

Take action on findings to remediate vulnerabilities and improve your application’s security posture.

For **Critical** and **High** severity findings with **High** confidence:

1. Review the Description and Steps to reproduce sections thoroughly.
2. Access the detailed logs via the "Trace actions & logs" link to gather complete evidence.
3. Access ready-to-implement code fixes through one of these methods:

   - For automatic remediation: Use the pull request link in the remediation section
   - For manual requests: Choose 'Remediation Code' on the findings page to request a pull request
     **Prerequisites:**
   - Admin must enable code remediation for GitHub repositories in the AWS Security Agent console
   - Repositories must be included in your penetration test configuration

4. Plan for a follow-up penetration test to verify the fix is effective.

For **Medium** and **Low** severity findings:

1. Prioritize based on your risk tolerance and business context.
2. Include remediation tasks in your regular development sprint planning.
3. Consider whether multiple low-severity findings together create higher risk.
4. Document any accepted risks with appropriate justification.

###### Important

Do not ignore low-severity findings. Multiple low-severity vulnerabilities can often be chained together to create more serious exploits, especially when combined with social engineering or physical access.

## Step 8: Track remediation progress

Use the findings interface to track which vulnerabilities have been addressed and which require further action.

1. As you work on remediation, refer back to the Steps to reproduce section to verify your fixes.
2. Document your remediation approach for each finding for future reference and compliance audits.

###### Tip

Maintain a remediation log that maps each finding to its resolution, including the code changes, configuration updates, or architectural decisions made to address the vulnerability.

## Next steps

After reviewing your penetration test findings:

- Prioritize critical and high-severity findings with high confidence for immediate remediation
- Download, review, and run verification scripts in your test environment to test the scripts and identify vulnerabilities
- Create tracking tickets in your issue management system with links to finding details and evidence
- Implement fixes and security controls to address identified vulnerabilities
- Monitor the penetration test run progress indicator for newly discovered vulnerabilities
- Revalidate a finding after you deploy a fix to confirm whether it is still exploitable. See [Revalidate penetration test findings](revalidate-findings.md "revalidate-findings.md").
- Schedule a follow-up penetration test to verify that broader changes have not introduced new vulnerabilities
- Update your application security testing process and threat model based on findings
- Review CVSS metrics to understand your application’s overall security posture

For more information about performing penetration tests, see [Create a penetration test](perform-penetration-test.md "perform-penetration-test.md").

For more information about understanding the Security Agent lifecycle, see [Understand the resource hierarchy and lifecycle](understand-lifecycle.md "understand-lifecycle.md").
