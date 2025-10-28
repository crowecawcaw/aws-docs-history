# Use a connection shared with another account

You can create and manage a shared connection using AWS RAM. This allows connections to be
shared between AWS accounts for access to third-party repositories. This allows a single
connection to be used in CodePipeline pipelines across accounts while reducing the need for users
to manage and administer separate connections in each account.

To use shared connections in CodePipeline, do the following.

- Create a connection using the Developer Tools console under
  **Settings**. See [Create
  a Connection](../../../dtconsole/latest/userguide/connections-create.md "../../../dtconsole/latest/userguide/connections-create.md").
- Set up the resource share using AWS RAM. See [Share
  connections with AWS accounts](../../../dtconsole/latest/userguide/connections-share.md "../../../dtconsole/latest/userguide/connections-share.md").
- When you use the CodePipeline console **Create pipeline** wizard or
  **Edit action** page to choose the connection provider, such as
  the **Bitbucket** provider option, you can choose the connection
  that has been shared with the target account.
