

# Connect to your workspace
<a name="connect-to-workspace"></a>

Before you can use your Amazon Managed Grafana workspace you must connect to it by signing in with the identity provider that you have set up. If you have not set up an authentication method via some identity provider, see [Authenticate users in Amazon Managed Grafana workspaces](authentication-in-AMG.md) for more information.

**Note**  
If you are trying to connect to your workspace programmatically, you must use API tokens. For more information, see [Authenticate with service accounts](v12-authenticating-grafana-apis.md).

**To sign in to your Grafana workspace**

1. Open the Amazon Managed Grafana console at [https://console.aws.amazon.com/grafana/](https://console.aws.amazon.com/grafana/home/), and sign in.

1. In the upper left corner of the page, choose the menu icon and then choose **All workspaces**.

1. Choose the name of the workspace you want to sign into.

1. In the workspace details page, choose the URL displayed under **Grafana workspace URL**.

1. Choosing the workspace URL takes you to the landing page for the Grafana workspace console. Choose **Sign in with AWS IAM Identity Center**, and enter the email address and password.
**Note**  
The sign in button will have different text and requirements if you have set up authentication with an identity provider.