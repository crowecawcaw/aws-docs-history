# Enable users to start remediation of penetration test findings

In the AWS Management Console, you can enable the code remediation feature that allows users to remediate findings in the penetration test web app.

When you enable this functionality in the AWS Management Console, users of the AWS Security Agent web app can start code remediation for a specific finding. The remediation will be available as GitHub pull requests.

## Prerequisites

Before you begin, ensure you have:

1. Enabled penetration test (see [Enable penetration test](enable-penetration-test.md "enable-penetration-test.md"))
2. Installed and authorized the AWS Security Agent GitHub App for your GitHub organization (see [Connect AWS Security Agent to GitHub repositories](connect-github.md "connect-github.md"))

## Select repositories and enable code remediation capability

1. Navigate to the Agent Space overview page.
2. Choose **Penetration test** tab.
3. Select a GitHub registration that owns your GitHub repositories.
   1. If you haven’t associated any GitHub registration to the Agent Space, you can see a **Connect GitHub for penetration testing** information box. Click the **Add** button on its right side to select the GitHub registration.
   2. If you already associated some GitHub registration to the Agent Space, you can add more by clicking the **Add** button in the **Connected integrations** section.

4. Click **Next** to choose GitHub repositories.
5. Click **Next** to configure repositories capabilities. In the **Pentest remediation enabled** column, mark the repositories as **Enabled** to allow the Agent Space to remediate the code according to the penetration findings.
6. Click **Connect** to finish the configuration.
