# Remediate a penetration test finding

When viewing the findings for a penetration test, you can request AWS Security Agent attempt to remediate a finding. AWS Security Agent will open a GitHub pull request for a finding.

You must enable finding remediation in the AWS Management Console. (See [Enable users to start remediation of penetration test findings](enable-remediate-findings.md "enable-remediate-findings.md").) Users can start remediation for a specific finding from the AWS Security Agent Web App.

## Procedure

## Prerequisites

Before you begin, ensure you have:

- A completed or in-progress penetration test run
- Access to the AWS Security Agent web application
- Familiarity with your application’s architecture and security requirements

## Configure code remediation

You can configure code remediation options when you create or modify a penetration test.

## Step 1: Enable or disable automatic remediation

If you enable automatic remediation, AWS Security Agent will automatically attempt to remediate the associated GitHub repositories if the Agent confirms a finding during the pentest. You can also manually start code remediation.
. In the view to edit **Penetration test details**, in the **Automatic code remediation** section, enable or disable code remediation.

## Step 2: Select repositories for code remediation

1. Click **Next** all the way to the last step **Additional learning resources**.
2. Choose **Select from resources**.
3. Choose **GitHub repositories**.
4. Select the repositories that you want for code remediation.
5. Save the penetration test.
6. You can see the successfully associated repositories under the **Penetration test learning resources** tab.

## Step 3: Start a penetration test and view findings

Run the penetration test to detect findings. For more information, see [Review findings from a penetration test](review-penetration-findings.md "review-penetration-findings.md").

## Step 4: Start and view code remediation

1. Navigate to the finding.
2. If you’ve enabled automatic code remediation, a code remediation will be started once AWS Security Agent confirms a finding.
3. If you want to manually start a code remediation, click the **Remediate code** button.
4. In the **Code Remediation** section of the finding, you can view the code remediation status and links to the pull requests.
