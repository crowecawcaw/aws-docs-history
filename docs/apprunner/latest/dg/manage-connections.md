# Managing App Runner connections

When you [create a service](manage-create.md "manage-create.md") in AWS App Runner, you configure an application source—a container image or a source
repository that's stored with a provider. App Runner has to establish an authenticated and authorized connection with the provider. Then, App Runner can read your
repository and deploy it to your service. App Runner doesn't require connection establishment when you create a service that accesses code stored in your
AWS account.

App Runner maintains connection information in a resource called a _connection_. The App Runner console and this guide also refer to
connections as _connected accounts_. App Runner requires a connection resource when you create a service that needs third-party
connection information. The following is some important information about connections:

- Providers – App Runner currently requires connection resources with [GitHub](https://github.com/ "https://github.com/") or
  [Bitbucket](https://bitbucket.org/ "https://bitbucket.org/").
- Shared – You can use a connection resource to create multiple App Runner services that use the same repository
  provider account.
- Resource management – In App Runner, you can create and delete connections. However, you can't modify an existing
  connection.
- Resource quota – Connection resources have a set quota that's associated with your AWS account in each
  AWS Region. If you reach this quota, you might need to delete a connection before you can connect to a new provider account. You can delete a
  connection using the App Runner console or API as described in the following section, [Manage connections](#manage-connections.manage "#manage-connections.manage"). For more information, see
  [App Runner resource quotas](architecture.md#architecture.quotas "architecture.md#architecture.quotas").

## Manage connections

Manage your App Runner connections using one of the following methods:

App Runner console
When you use the App Runner console to [create a service](manage-create.md "manage-create.md"), you provide connection details. You don't have to
explicitly create a connection resource. In the console, you can choose to connect to a GitHub or Bitbucket account that you've connected to before,
or connect to a new account. When necessary, App Runner creates a connection resource for you. For a new connection, some providers require you to
complete an authentication handshake before you can use the connection. The console takes you through this process.

The console also has a page for managing your existing connections. You can complete the authentication handshake for a connection if you didn't
do it when you created your service. You can also delete connections that you're no longer using. The following procedure shows how you can manage
repository provider connections.

###### To manage connections in your account

1. Open the [App Runner console](https://console.aws.amazon.com/apprunner "https://console.aws.amazon.com/apprunner"), and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Connected accounts**.

The console then displays a list of repository provider connections in your account.

![App Runner Connected accounts page](images/console-connections-github.png) 3. You can now do one of the following actions with any connection on the list:

    * *Open GitHub/Bitbucket account or organization* – Choose the name of the connection.
    * *Complete authentication handshake* – Select the connection, and then from the **Actions** menu choose **Complete handshake**. The console takes you through the authentication handshake
     process.
    * *Delete connection* – Select the connection, and then from the **Actions** menu
     choose **Delete**. Follow the instructions on the deletion prompt.

App Runner API or AWS CLI
You can use the following App Runner API actions to manage your connections.

- [CreateConnection](../api/API_CreateConnection.md "../api/API_CreateConnection.md") – Creates a connection to a repository provider account.
  After the connection is created, you must manually complete the authentication handshake using the App Runner console. This process is explained in
  the previous section.
- [ListConnections](../api/API_ListConnections.md "../api/API_ListConnections.md") – Returns a list of App Runner connections associated with your
  AWS account.
- [DeleteConnection](../api/API_DeleteConnection.md "../api/API_DeleteConnection.md") – Deletes a connection. You might need to delete
  unnecessary connections if you reach the connection quota for your AWS account.
