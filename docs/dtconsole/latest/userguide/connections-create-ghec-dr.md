

# Create a connection to GitHub Enterprise Cloud with data residency

You can use the AWS Management Console or the AWS Command Line Interface (AWS CLI) to create a connection to repositories in an enterprise on GitHub Enterprise Cloud with data residency. Each enterprise on GitHub Enterprise Cloud with data residency has its own subdomain on GHE.com, such as `https://my-enterprise.ghe.com`.

Before you begin:
+ You must have an enterprise on GitHub Enterprise Cloud with data residency. Its URL must have the form `https://{{subdomain}}.ghe.com` and must use HTTPS.
+ You must have at least one organization set up in your enterprise.
+ You must be an organization owner of the organization where you install the AWS Connector for GitHub app. You don't need to be an enterprise owner.
+ You must install the app on an organization, not on a personal account. For more information, see [Abilities and restrictions of managed user accounts](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/abilities-and-restrictions-of-managed-user-accounts) in the GitHub documentation.

**Note**  
The AWS Connector for GitHub app is already available on GitHub Enterprise Cloud with data residency. You don't need to register or create a GitHub App in your enterprise.

**Note**  
Connection resource is replicated across AWS Regions within a partition to provide cross-region connection sharing. If you need further isolation, use opt-in region or non-commercial partitions.

**Note**  
CodeConnections supports connections to GitHub Enterprise Cloud with data residency (\*.ghe.com) tenants. Not every AWS service that uses CodeConnections supports this provider type yet. Before you use a GitHub Enterprise Cloud with data residency connection with another AWS service, check that service's documentation to confirm it supports the provider type.

**Topics**
+ [Create a connection to GitHub Enterprise Cloud with data residency (console)](#connections-create-ghec-dr-console)
+ [Create a connection to GitHub Enterprise Cloud with data residency (CLI)](#connections-create-ghec-dr-cli)

## Create a connection to GitHub Enterprise Cloud with data residency (console)
<a name="connections-create-ghec-dr-console"></a>

In the following procedure, you choose the GitHub Enterprise Cloud with data residency provider and enter the URL of your enterprise on GHE.com. The connection is created in **Pending** status.

**To create the connection**

1. Sign in to the AWS Management Console.

1. Open the Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/connections](https://console.aws.amazon.com/codesuite/settings/connections).

1. On the **Connections** page, choose **Create connection**.

1. On the **Create a connection** page, under **Select a provider**, select **GitHub Enterprise Cloud** with data residency.  
![The GitHub Enterprise Cloud with data residency provider tile selected, with Connection name and URL entered.](https://docs.aws.amazon.com/dtconsole/latest/userguide/images/connections-create-ghec-dr-provider.png)

1. Enter the details for the connection:
   + Under **Connection Settings**, in **Connection name**, enter the name for the connection that you want to create.
   + Under **Connection Settings**, in **URL**, enter the URL of your enterprise on GHE.com, such as `https://my-enterprise.ghe.com`.
   + (Optional) Under **Tags**, add tags for the connection.

1. At the bottom of the page, choose **Connect to GitHub Enterprise Cloud**.

   The connection details page for your connection opens, and a message confirms that you created the connection.

1. Under **Connection settings**, confirm that **Status** shows **Pending**, **Provider** shows **GitHub Enterprise Cloud**, and **Endpoint** shows the URL of your enterprise. The **Finish creating your connection** banner contains the **Update pending connection** button that you use in the next procedure.  
![Connection details where Status shows Pending, and the Finish creating your connection banner has Update pending connection.](https://docs.aws.amazon.com/dtconsole/latest/userguide/images/connections-create-ghec-dr-pending.png)

Your connection now exists in **Pending** status. To continue, complete the procedure *To complete the connection*.

In the following procedure, you authorize the AWS Connector for GitHub app, install it on an organization in your enterprise, and complete the connection. Complete all the steps in one session. If you leave before you finish, start again from **Update pending connection**. When you complete the connection, its status changes to **Available**, and you can use the connection.

**To complete the connection**

1. If the connection details page for your connection isn't open, open the Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/connections](https://console.aws.amazon.com/codesuite/settings/connections). On the **Connections** page, select the connection that you created, and then choose **View details**.

1. On the connection details page, in the **Finish creating your connection** banner, choose **Update pending connection**. If you aren't already signed in to your enterprise on GHE.com, sign in with your credentials.

1. On the **Select user to authorize AWS Connector for GitHub** page, for the account that you're signed in as, choose **Continue**. To use another listed account, choose **Select** for that account. To use an account that isn't listed, choose **Use a different account**.
**Note**  
On GHE.com, the developer of the AWS Connector for GitHub app appears as `github-third-party-apps-owner` instead of AWS CodeConnections. This is expected.  
![Select user to authorize AWS Connector for GitHub, with Continue for the signed-in account and Select for another account.](https://docs.aws.amazon.com/dtconsole/latest/userguide/images/connections-create-ghec-dr-select-user.png)

   The **Connect to GitHub Enterprise Cloud** page opens in the console.

1. On the **Connect to GitHub Enterprise Cloud** page, under **GitHub Apps**, do one of the following:
   + If the AWS Connector for GitHub app isn't installed on the organization that you want to use, choose **Install a new app**. You install the app once for each organization.
   + If the app is already installed on the organization, select the existing installation from the list, choose **Connect**, and then go to the last step of this procedure.  
![Under GitHub Apps, the installation list is open next to Install a new app, with the Connect button at the lower right.](https://docs.aws.amazon.com/dtconsole/latest/userguide/images/connections-create-ghec-dr-github-apps.png)

1. On the **Install AWS Connector for GitHub** page in your enterprise, under **Where do you want to install AWS Connector for GitHub?**, choose the organization where you want to install the app.  
![Install AWS Connector for GitHub lists four organizations in the enterprise, with redacted names, to choose from.](https://docs.aws.amazon.com/dtconsole/latest/userguide/images/connections-create-ghec-dr-app-install-org.png)
**Note**  
If you receive an insufficient permissions error when you install the app, see [Unable to install the app for a GitHub Enterprise Cloud with data residency connection because of insufficient permissions](troubleshooting-connections.md#troubleshooting-connections-ghec-dr-install-permissions).

1. On the **Install & Authorize AWS Connector for GitHub** page, under **for these repositories**, select **All repositories** or **Only select repositories**. If you select **Only select repositories**, select at least one repository.

1. Under **with these permissions**, review the read and write access that the app requests, and then choose **Install & Authorize**.  
![The first repository access option is selected by default, and text under Install & Authorize shows the redirect URL.](https://docs.aws.amazon.com/dtconsole/latest/userguide/images/connections-create-ghec-dr-app-install-authorize.png)

1. On the **Connect to GitHub Enterprise Cloud** page, under **GitHub Apps**, your new installation is selected. Choose **Connect**.  
![Under GitHub Apps, the search box contains the redacted ID of the new installation, with the Connect button below it.](https://docs.aws.amazon.com/dtconsole/latest/userguide/images/connections-create-ghec-dr-connect.png)

1. On the connection details page, under **Connection settings**, confirm that **Status** shows **Available**. Your connection is ready to use.  
![Connection details where Status shows Available, with no banner above the Connection settings panel.](https://docs.aws.amazon.com/dtconsole/latest/userguide/images/connections-create-ghec-dr-available.png)

## Create a connection to GitHub Enterprise Cloud with data residency (CLI)
<a name="connections-create-ghec-dr-cli"></a>

You can use the AWS Command Line Interface (AWS CLI) to create a connection to GitHub Enterprise Cloud with data residency.

To do this, use the **create-connection** command.

**Important**  
A connection created through the AWS CLI is in `PENDING` status by default. After you create a connection with the AWS CLI, use the console to edit the connection to make its status `AVAILABLE`.

The following procedure creates a connection to GitHub Enterprise Cloud with data residency in `PENDING` status. You then use the console to authorize and install the AWS Connector for GitHub app on an organization and make the connection `AVAILABLE`.

**To create a connection to GitHub Enterprise Cloud with data residency**

1. Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run the **create-connection** command, specifying the `--provider-type`, `--provider-endpoint`, and `--connection-name` for your connection. In this example, the third-party provider name is `GitHubEnterpriseCloudDataResidency`, the provider endpoint is the URL of the enterprise, `https://my-enterprise.ghe.com`, and the specified connection name is `MyConnection`.

   ```shell
   aws codeconnections create-connection --provider-type GitHubEnterpriseCloudDataResidency --provider-endpoint "https://my-enterprise.ghe.com" --connection-name MyConnection
   ```

   If successful, this command returns the connection ARN information similar to the following.

   ```
   {
       "ConnectionArn": "arn:aws:codeconnections:us-west-2:{{account_id}}:connection/aEXAMPLE-8aad-4d5d-8878-dfcab0bc441f"
   }
   ```

1. Use the console at [https://console.aws.amazon.com/codesuite/settings/connections](https://console.aws.amazon.com/codesuite/settings/connections) to authorize and install the AWS Connector for GitHub app and complete the connection. Follow the procedure *To complete the connection* in [Create a connection to GitHub Enterprise Cloud with data residency (console)](#connections-create-ghec-dr-console).