# Review findings from a code review

After a code review run completes, review the run summary and security findings to understand vulnerabilities in your source code. Each finding contains a description, severity rating, code locations, risk reasoning, and suggested fixes to help you prioritize and address security issues.

## Prerequisites

Before you begin, ensure you have:

- A completed or in-progress code review run
- Access to the AWS Security Agent web application

## Step 1: Access the code review run

Navigate to your completed code review run to view the summary and findings.

1. Log in to the AWS Security Agent web application.
2. In the left sidebar, choose **Code reviews**.
3. Select the code review you want to examine.
4. In the **All runs** table, select the completed run by clicking its start time link. Alternatively, choose **Monitor run** to view the latest run.

## Step 2: Monitor run progress

Track the progress of your code review run using the step indicator.

1. Locate the horizontal step indicator below the page header.
2. Review the status of each phase:

   - **Preflight** – Validates access to your source code and sets up the scanning environment. Checks include service infrastructure setup, S3 source access validation, and testing environment setup, which includes GitHub access checks.
   - **Static analysis** – Scans your source code for security vulnerabilities and requirement violations.
   - **Simulated validation** (optional) – When enabled, provisions a simulated environment and attempts to exploit discovered vulnerabilities against the running application.
   - **Finalizing** – Compiles findings and generates the results summary.

###### Note

Each step displays a status indicator (Completed or In progress). The run is complete when all phases show Completed. The simulated validation step only appears when you enable simulated validation during code review creation.

## Step 3: Review the run summary

Navigate to the **Code review run** tab to view the high-level results.

1. Select the **Code review run** tab.
2. The **Run summary** section provides run status, duration and other high level details. It also provides a dashboard of security findings categorized by severity level and risk-types.
3. Application overview by AWS Security Agent provides a summary of the code review scan when the run is completed

## Step 4: Review preflight results

Navigate to the **Preflight** tab to verify that all source access checks passed.

1. Select the **Preflight** tab.
2. Review the **Preflight progress** indicator showing the number of checks completed.
3. Verify that each check shows a success status:

   - **Service infrastructure setup** – Confirms the testing environment is ready
   - **S3 Source Access Validation** – Confirms access to S3 source code (if applicable)
   - **Setup Testing Environment** – Confirms the analysis environment is configured

###### Note

If any preflight check fails, the run will not proceed to static analysis. Review the check details to identify and resolve access issues, then start a new run.

## Step 5: Review code review logs

Navigate to the **Code review logs** tab to view the tasks AWS Security Agent performed during analysis.

1. Select the **Code review logs** tab.
2. Browse the list of tasks in the left panel.
3. Select a task to view its detailed log in the right panel.

###### Tip

Use the search field to filter tasks by name. The logs provide insight into what AWS Security Agent examined and how it reached its conclusions.

## Step 6: Navigate to findings

Select the **Findings** tab to view all security findings from the run.

###### Note

###### Default confidence filter

By default, you see only findings with **High** agent confidence. To also show findings with **Medium** or **Low** agent confidence and false positives, turn off the **Hiding unverified findings** toggle.

1. Select the **Findings** tab.
2. The findings display in a split view with the findings list on the left and the selected finding’s details on the right.
3. Review the information displayed on each finding card:

   - **Finding title** – A descriptive name summarizing the security issue
   - **Severity badge** – Color-coded risk level (Critical, High, Medium, or Low). For what each level means, see [Severity ratings and CVSS metrics](severity-and-cvss.md "severity-and-cvss.md").
   - **Last updated** – Timestamp of when the finding was last updated

## Step 7: Review finding details

Select individual findings to view comprehensive information about each vulnerability.

1. Select a finding in the left panel to display its details in the right panel.
2. Review the available actions:

   - **Resolve finding** – Mark the finding as resolved after you’ve addressed it
   - **Remediate code** – Generate a pull request with a fix (available for GitHub sources)

3. Provide feedback using **Was this finding accurate?** – Select **Yes** or **No** to help improve future analysis accuracy.
4. Review the key attributes in the **Overview** section:

   - **Agent confidence** – The confidence level AWS Security Agent has in this finding
   - **Severity** – The risk level with a color-coded badge
   - **Risk Type** – The category of security risk
   - **Validation status** – When simulated validation is enabled, indicates whether the finding was confirmed exploitable in a running environment:

     - **Confirmed** – The vulnerability was successfully exploited in the simulated environment
     - **Not reproduced** – The vulnerability could not be exploited in the target runtime
     - **Validation failed** – The validation attempt was inconclusive due to an error
     - **Not validated** – Simulated validation was not performed for this finding. This occurs when validation is not enabled or the validation step timed out before reaching this finding.

   - **Resolved** – Whether the finding has been resolved (Yes/No)
   - **Last updated** – Timestamp of the most recent update

5. Expand the **Description** section to read:

   - A detailed explanation of the security issue
   - How the vulnerability could be exploited
   - The potential impact on your application
   - Verification steps the agent performed to confirm the finding

6. Expand the **Code locations** section to view:

   - Specific file paths where the issue was identified
   - A brief description of what was found at each location
   - Line number badges linking to the relevant code

7. Expand the **Evidence** section to review:

   - The specific code, configuration, or observations that support the finding
   - A short explanation of why each item demonstrates the vulnerability
   - The affected files and line numbers for each piece of evidence

8. Expand the **Suggested fix** section to view:

   - The changes AWS Security Agent recommends to remediate the finding
   - Example code or configuration for each recommended change

###### Tip

Use the code locations to quickly navigate to the affected files in your repository. Each location includes enough context to understand the issue without reading the entire file.

## Step 8: Prioritize and address findings

Validate and take action on findings to remediate vulnerabilities and improve your application’s security posture.

For **High** severity findings with **High** agent confidence:

1. Review the Description and Code locations sections thoroughly.
2. Use **Remediate code** to generate a pull request with a fix, or review automatic remediation PRs if you enabled that option.
3. Plan a follow-up code review run to verify the fix is effective.

For **Medium** severity findings with **High** agent confidence:

1. Prioritize based on your risk tolerance and business context.
2. Include remediation tasks in your regular development sprint planning.
3. Consider whether multiple medium-severity findings together create higher risk.

For **Medium** or **Low** confidence findings:

1. Review the Description and Code locations sections to validate the assumptions and conditions under which the vulnerability occurs.
2. If vulnerability is valid, prioritize based on severity and risk tolerance and consider remediation tasks.

## Step 9: Track remediation progress

Use the findings interface and re-runs to track which vulnerabilities have been addressed.

1. As you implement fixes, use **Resolve finding** to mark findings as addressed.
2. Run a new code review to verify that fixes resolve the findings and don’t introduce new issues.
3. Review the **All runs** table on the code review detail page to compare findings across runs over time.

###### Tip

After merging remediation pull requests, start a new run of the same code review to confirm the vulnerabilities are resolved. Compare the findings count between runs to track your progress.

## Next steps

After reviewing your code review findings:

- Prioritize high-severity findings with high confidence for immediate remediation
- Use **Remediate code** to generate automated fixes for GitHub-sourced findings (see [Remediate code review findings](remediate-code-scan-findings.md "remediate-code-scan-findings.md"))
- Run additional code reviews after implementing fixes to verify remediation
- Adjust your code review sources or settings as your codebase evolves (see [Enable code review](enable-code-review-scan.md "enable-code-review-scan.md"))
