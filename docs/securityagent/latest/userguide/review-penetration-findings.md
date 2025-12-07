# Review findings from a penetration test

Monitor pentest execution in real time on the Penetration Test Logs page after AWS Security Agent starts a pentest. AWS Security Agent logs every action during the pentest. After completion, review the pentest summary, which includes application overview, coverage with identified endpoints, and risk assessment of security findings.

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

Track the progress of your penetration test run using the step indicator at the top of the page.

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
3. Discovered endpoints by AWS Security Agent provides a list of all endpoints discovered and tested by the AWS Security agent during the pentest run

## Step 4: Navigate to the penetration test logs tab

Access detailed logs of all actions AWS Security Agent executed during the pentest.

1. The actions are categorized by action type and risk-types.
2. Click on a specific action to view detailed logs:
   - **Testing Summary** – High-level summary of the agent actions and results
   - **Penetration test logs** – Detailed logs of all testing activities

###### Note

Validator actions provide logs that validate findings in each category

###### Note

The Findings tab displays a split view with the findings list on the left and selected finding details on the right.

## Step 5: Navigate to the findings

Each finding in the list displays key information to help you quickly assess its importance.

###### Note

Findings with Low agent confidence and False Positives are hidden by default. You can view them by disabling the toggle **Hide False Positives**.

Review the information displayed on each finding card:

- **Finding name** – The title and identifier for the vulnerability
- **Confidence badge** – Indicates the agent’s confidence level in the finding (High, Medium, or Low)
- **Severity badge** – Shows the risk level with color coding:
  - **Critical** (red) – Requires immediate action; exploitation could lead to system compromise
  - **High** (red) – Requires prompt attention; exploitation could result in significant security impact
  - **Medium** (orange) – Should be addressed in a reasonable timeframe; contributes to overall security risk
  - **Low** (yellow) – Can be addressed as part of regular maintenance; minimal immediate risk
  - **Informational** (blue) – For informational purposes; minimal to no immediate risk

- **Last update timestamp** – Shows when the finding was last modified or validated
- **Description preview** – Brief summary of the vulnerability

###### Important

Prioritize findings with **Critical** or **High** severity badges and **High** confidence levels, as these represent validated vulnerabilities requiring immediate remediation.

## Step 6: Review finding details

Select individual findings to view comprehensive information about each vulnerability.

1. Click on a finding name in the left panel to display its details in the right panel.
2. Review the validation status at the top of the details panel:

###### Note

If a finding displays the Unknown "This finding is not validated by AWS Security Agent yet," it means the vulnerability detection is still being confirmed. These findings may require manual verification. 3. Review the key attributes displayed at the top:

    * **Agent confidence** – The confidence level AWS Security Agent has in this finding
    * **Severity** – The risk level with a color-coded badge
    * **Finding logs** – Click "Trace actions & logs" to view detailed execution logs and evidence
    * **Risk type** – The category or type of security risk (e.g., Authentication Bypass, SQL Injection)

4. Expand the **Description** section to read:
   - A detailed explanation of the vulnerability
   - How the vulnerability works
   - Why it represents a security risk
   - The potential impact on your application

5. Expand the **Risk Reasoning** section to understand the severity calculation:
   - CVSS (Common Vulnerability Scoring System) metrics breakdown
   - Attack Vector (AV) – How the vulnerability can be exploited
   - Attack Complexity (AC) – How difficult the exploit is
   - Privileges Required (PR) – What access level is needed
   - User Interaction (UI) – Whether user action is required
   - Scope (S) – Whether the vulnerability affects other components
   - Confidentiality, Integrity, and Availability impacts

6. Expand the **Steps to reproduce** section to view:
   - Detailed technical steps to recreate the vulnerability
   - Request and response examples
   - Specific parameters or conditions that trigger the issue

###### Tip

Use the "Trace actions & logs" link to access the complete evidence package, including HTTP requests, responses, and exploitation attempts that demonstrate the vulnerability.

## Step 7: Interpret CVSS metrics

Understanding CVSS metrics helps you assess the true severity and prioritize remediation efforts.

When reviewing the **Reasoning** section, pay attention to these key metrics:

- **Attack Vector (Network/Adjacent/Local/Physical)** – Indicates how remotely the attack can be executed
- **Attack Complexity (Low/High)** – Shows whether specialized conditions are required to exploit
- **Privileges Required (None/Low/High)** – Identifies what access level an attacker needs
- **User Interaction (None/Required)** – Determines if the exploit needs user involvement
- **Confidentiality/Integrity/Availability Impact (None/Low/High)** – Measures the impact on your system’s security

###### Important

Findings with Network attack vector, Low complexity, and High confidentiality/integrity impact represent the most dangerous vulnerabilities requiring immediate attention.

## Step 8: Prioritize and address findings

Take action on findings to remediate vulnerabilities and improve your application’s security posture.

For **Critical** and **High** severity findings with **High** confidence:

1. Review the Description and Steps to reproduce sections thoroughly.
2. Access the detailed logs via the "Trace actions & logs" link to gather complete evidence.
3. Access ready-to-implement code fixes through one of these methods:
   - For automatic remediation: Use the pull request link in the remediation section
   - For manual requests: Click 'Remediation Code' on the findings page to request a pull request
     **Prerequisites:**
   - Admin must enable code remediation for GitHub repositories in the AWS Security Agent console
   - Repositories must be included in your pentest configuration

4. Plan for a follow-up penetration test to verify the fix is effective.

For **Medium** and **Low** severity findings:

1. Prioritize based on your risk tolerance and business context.
2. Include remediation tasks in your regular development sprint planning.
3. Consider whether multiple low-severity findings together create higher risk.
4. Document any accepted risks with appropriate justification.

###### Important

Do not ignore low-severity findings. Multiple low-severity vulnerabilities can often be chained together to create more serious exploits, especially when combined with social engineering or physical access.

## Step 9: Track remediation progress

Use the findings interface to track which vulnerabilities have been addressed and which require further action.

1. As you work on remediation, refer back to the Steps to reproduce section to verify your fixes.
2. Document your remediation approach for each finding for future reference and compliance audits.

###### Tip

Maintain a remediation log that maps each finding to its resolution, including the code changes, configuration updates, or architectural decisions made to address the vulnerability.

## Next steps

After reviewing your penetration test findings:

- Prioritize critical and high-severity findings with high confidence for immediate remediation
- Create tracking tickets in your issue management system with links to finding details and evidence
- Implement fixes and security controls to address identified vulnerabilities
- Monitor the penetration test run progress indicator for newly discovered vulnerabilities
- Schedule a follow-up penetration test to verify that vulnerabilities have been properly remediated
- Update your application security testing process and threat model based on findings
- Review CVSS metrics to understand your application’s overall security posture

For more information about performing penetration tests, see [Create a penetration test](perform-penetration-test.md "perform-penetration-test.md").

For more information about understanding the Security Agent lifecycle, see [Understand the resource hierarchy and lifecycle](understand-lifecycle.md "understand-lifecycle.md").
