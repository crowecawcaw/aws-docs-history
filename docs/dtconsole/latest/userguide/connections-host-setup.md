

# Set up a pending host
<a name="connections-host-setup"></a>

A host created through the AWS Command Line Interface (AWS CLI) or SDK is in `Pending` status by default. After you create a connection with the console, AWS CLI, or the SDK, use the console to set up the host to make its status `Available`.

You must have already created a host. For more information, see [Create a host](connections-host-create.md).<a name="proc-host-setup-steps"></a>

**To set up a pending host**

After your host is created, it is in a **Pending** status. To move the host from **Pending** to **Available**, complete these steps. This process performs a handshake with the third-party provider to register the AWS connection app on the host.

1. After your host reaches **Pending** status on the AWS Developer Tools console, choose **Set up host**.

1. If you are creating a host for GitLab self-managed, a **Set up** page displays. In **Provide personal access token**, provide your GitLab PAT with the `api` scope. If Admin Mode is enabled on your GitLab instance, the PAT must also include the `admin_mode` scope. For more information, see [Access token scopes](https://docs.gitlab.com/security/tokens/access_token_scopes/) on the GitLab website.

1. On the third-party installed provider login page, such as the **GitHub Enterprise Server** login page, log in with your account credentials if prompted.

1. On the app install page, in **GitHub App name**, enter a name for the app you want to install for your host. Choose **Create GitHub App**.

1. After your host is successfully registered, the host details page appears and shows that the host status is **Available**.  
![Console screenshot showing the host setup is complete and in Available status.](http://docs.aws.amazon.com/dtconsole/latest/userguide/images/connections-create-host-register-complete.png)

1. You can continue with creating your connection after the host is available. On the success banner, choose **Create connection**. Complete the steps in [Create a connection](connections-create-gheserver-console.md).