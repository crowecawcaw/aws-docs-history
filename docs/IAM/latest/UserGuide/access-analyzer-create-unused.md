# Create an IAM Access Analyzer unused access

analyzer

## Create an unused access analyzer

for the current account

Use the following procedure to create an unused access analyzer for a single
AWS account. For unused access, findings for the analyzer do not change based on
Region. Creating an analyzer in each Region where you have resources is not
required.

IAM Access Analyzer charges for unused access analysis based on the number of IAM roles
and users analyzed per month per analyzer. For more details about pricing, see [IAM Access Analyzer
pricing](https://aws.amazon.com/iam/access-analyzer/pricing "https://aws.amazon.com/iam/access-analyzer/pricing").

###### Note

After you create or update an analyzer, it can take time for findings to be
available.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Under **Access analyzer**, choose **Analyzer
   settings**.
3. Choose **Create analyzer**.
4. In the **Analysis** section, choose **Principal
   analysis - Unused access**.
5. Enter a name for the analyzer.
6. For **Tracking period**, enter the number of days for
   analysis. The analyzer will only evaluate permissions for IAM entities within
   the selected account that have existed for the entire tracking period. For
   example, if you set a tracking period of 90 days, only permissions that are at
   least 90 days old will be analyzed, and findings will be generated if they show
   no usage during this period. You can enter a value between 1 and 365
   days.
7. In the **Analyzer details** section, confirm that the Region
   displayed is the Region where you want to enable IAM Access Analyzer.
8. For **Selected accounts**, choose **Current
   account**.

###### Note

If your account is not the AWS Organizations management account or [delegated
administrator](access-analyzer-delegated-administrator.md "access-analyzer-delegated-administrator.md") account, you can create only one analyzer with your
account as the selected account. 9. Optional. In the **Exclude IAM users and roles with tags**
section, you can specify key-value pairs for IAM users and roles to exclude
from unused access analysis. Findings will not be generated for excluded
IAM users and roles that match the key-value pairs. For the **Tag
key**, enter a value that is 1 to 128 characters in length and not
prefixed with `aws:`. For the **Value**, you can
enter a value that is 0 to 256 characters in length. If you don't enter a
**Value**, the rule is applied to all principals with the
specified **Tag key**. Choose **Add new
exclusion** to add additional key-value pairs to exclude. 10. Optional. Add any tags that you want to apply to the analyzer. 11. Choose **Create analyzer**.

When you create an unused access analyzer to enable IAM Access Analyzer, a service-linked
role named `AWSServiceRoleForAccessAnalyzer` is created in your account.

## Create an unused access

analyzer with the current organization

Use the following procedure to create an unused access analyzer for an organization to
centrally review all AWS accounts in an organization. For unused access analysis,
findings for the analyzer do not change based on Region. Creating an analyzer in each
Region where you have resources is not required.

IAM Access Analyzer charges for unused access analysis based on the number of IAM roles
and users analyzed per month per analyzer. For more details about pricing, see [IAM Access Analyzer
pricing](https://aws.amazon.com/iam/access-analyzer/pricing "https://aws.amazon.com/iam/access-analyzer/pricing").

###### Note

If a member account is removed from the organization, the unused access analyzer
will stop generating new findings and updating existing findings for that account
after 24 hours. Findings associated with the member account that is removed from the
organization will be removed permanently after 90 days.

1.  Open the IAM console at
    [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2.  Under **Access analyzer**, choose **Analyzer
    settings**.
3.  Choose **Create analyzer**.
4.  In the **Analysis** section, choose **Principal
    analysis - Unused access**.
5.  Enter a name for the analyzer.
6.  For **Tracking period**, enter the number of days for
    analysis. The analyzer will only evaluate permissions for IAM entities within
    the accounts of the selected organization that have existed for the entire
    tracking period. For example, if you set a tracking period of 90 days, only
    permissions that are at least 90 days old will be analyzed, and findings will be
    generated if they show no usage during this period. You can enter a value
    between 1 and 365 days.
7.  In the **Analyzer details** section, confirm that the Region
    displayed is the Region where you want to enable IAM Access Analyzer.
8.  For **Selected accounts**, choose **Current
    organization**.
9.  Optional. In the **Exclude AWS accounts from analysis**
    section, you can choose AWS accounts in your organization to exclude from
    unused access analysis. Findings will not be generated for excluded
    accounts.
    1.  To specify individual account IDs to exclude, choose **Specify
        AWS account ID** and enter the account IDs separated by
        commas in the **AWS account ID** field. Choose
        **Exclude**. The accounts are then listed in the
        **AWS accounts to exclude** table.
    2.  To choose from a list of accounts in your organization to exclude,
        choose **Choose from organization**.

            1. You can search for accounts by name, email, and account ID in
             the **Exclude accounts from organization**
             field.
            2. Choose **Hierarchy** to view your accounts by
             organizational unit or choose **List** to view
             a list of all individual accounts in your organization.
            3. Choose **Exclude all current accounts** to
             exclude all accounts in an organizational unit or choose
             **Exclude** to exclude individual
             accounts.The accounts are then listed in the **AWS accounts to

        exclude\*\* table.

###### Note

Excluded accounts cannot include the organization analyzer owner account.
When new accounts are added to your organization, they are not excluded from
analysis, even if you previously excluded all current accounts within an
organizational unit. For more information on excluding accounts after
creating an unused access analyzer, see [Manage an IAM Access Analyzer unused access
analyzer](access-analyzer-manage-unused.md "access-analyzer-manage-unused.md"). 10. Optional. In the **Exclude IAM users and roles with tags**
section, you can specify key-value pairs for IAM users and roles to exclude
from unused access analysis. Findings will not be generated for excluded
IAM users and roles that match the key-value pairs. For the **Tag
key**, enter a value that is 1 to 128 characters in length and not
prefixed with `aws:`. For the **Value**, you can
enter a value that is 0 to 256 characters in length. If you don't enter a
**Value**, the rule is applied to all principals with the
specified **Tag key**. Choose **Add new
exclusion** to add additional key-value pairs to exclude. 11. Optional. Add any tags that you want to apply to the analyzer. 12. Choose **Create analyzer**.

When you create an unused access analyzer to enable IAM Access Analyzer, a service-linked
role named `AWSServiceRoleForAccessAnalyzer` is created in your account.
