

# Rollingback your bulk migration policy changes
<a name="migrate-console-rollback"></a>

You can rollback all policy changes you make during the bulk migration process safely, using the steps provided in the bulk migration tool. The rollback feature works at an account-level. You can rollback policy updates for all accounts, or specific groups of migrated accounts. However, you can't rollback changes for specific policies in an account.

**To rollback bulk migration changes**

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/).

1. In the search bar at the top of the page, enter **Bulk Policy Migrator**.

1. On the **Manage new IAM actions** page, choose the **Rollback changes** tab.

1. Select any accounts to rollback. The accounts must have `Migrated` showing in the **Rollback status** column.

1. Choose **Rollback changes** button.

1. Remain on the console page until rollback is complete.