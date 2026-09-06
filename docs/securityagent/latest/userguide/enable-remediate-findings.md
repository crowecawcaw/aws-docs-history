

# Enable users to start remediation of penetration test and code review findings
<a name="enable-remediate-findings"></a>

In the AWS Management Console, you can enable automatic remediation so users of the AWS Security Agent web application can request fixes for a specific finding. AWS Security Agent delivers each fix as a GitHub pull request on the affected repository.

You enable remediation per repository from within an Agent Space. The **Penetration test** and **Code review** tabs open the same repository configuration wizard, so you can use either tab to manage the **Automatic remediation enabled** setting. Remediation applies to findings from both capabilities, so you only need to enable it once per repository.

## Prerequisites
<a name="_prerequisites"></a>

Before you begin, ensure you have:

1. Enabled penetration testing (see [Enable penetration test](enable-penetration-test.md)) or code review (see [Enable code review](enable-code-review-scan.md))

1. Installed and authorized the AWS Security Agent GitHub App for your GitHub organization (see [Connect AWS Security Agent to GitHub repositories](connect-github.md))

## Open the repository configuration wizard
<a name="_open_the_repository_configuration_wizard"></a>

Choose the entry point that matches how your repositories are set up.

### From the penetration test tab
<a name="_from_the_penetration_test_tab"></a>

Use this path to add GitHub repositories for penetration testing and configure remediation in the same pass.

1. Navigate to the Agent Space overview page.

1. Choose the **Penetration test** tab.

1. Select a GitHub registration that owns your repositories:

   1. If you haven’t associated any GitHub registration with the Agent Space, choose **Add** in the **Connect GitHub to AWS Security Agent** information box to select a registration.

   1. If one or more GitHub registrations are already associated, choose **Add** in the **Connected integrations** section to select another.

1. Choose **Next** to choose GitHub repositories.

1. Choose **Next** to configure repository capabilities.

### From the code review tab
<a name="_from_the_code_review_tab"></a>

Use this path when your repositories are already connected for code review.

1. Navigate to the Agent Space overview page.

1. Choose the **Code review** tab.

1. In the GitHub repositories table, choose **Edit** to open the repository configuration wizard.

## Enable automatic remediation and save
<a name="_enable_automatic_remediation_and_save"></a>

After you reach the repository capabilities step through either path above:

1. In the **Automatic remediation enabled** column, mark each repository you want remediated as **Enabled**.

1. Choose **Connect** to save the configuration.

Users of the web application can now start remediation for findings on these repositories, and AWS Security Agent opens pull requests with the proposed fixes.