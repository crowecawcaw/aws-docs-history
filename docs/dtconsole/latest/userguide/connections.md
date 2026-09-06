

# Working with connections
<a name="connections"></a>

*Connections* are configurations that you use to connect AWS resources to external code repositories. Each connection is a resource that can be given to services such as AWS CodePipeline to connect to a third-party repository such as Bitbucket. For example, you can add the connection in CodePipeline so that it triggers your pipeline when a code change is made to your third-party code repository. You can also connect your AWS resources to an installed provider type such as GitHub Enterprise Server.

**Note**  
For organizations in GitHub or GitHub Enterprise Server, you cannot install a GitHub App into multiple GitHub Organizations. The app to GitHub Organization mapping is a 1:1 mapping. One organization can only have one app at a time; however, you can have multiple connections pointing to the same app. For more detail, see [How connections in AWS CodeConnections work with organizations](welcome-connections-how-it-works-github-organizations.md).

If you want to create a connection to an installed provider type, such as GitHub Enterprise Server, the console creates a host for you. A host is a resource that you create to represent the server where your provider is installed. For more information, see [Working with hosts](connections-hosts.md).

When you create a connection, you use a wizard in the console to install the connections app with your third-party provider and associate it with a new connection. If you have already installed the app, you can use it.

**Note**  
To use connections in the Europe (Milan) AWS Region, you must:   
Install a Region-specific app
Enable the Region
This Region-specific app supports connections in the Europe (Milan) Region. It is published on the third-party provider site, and it is separate from the existing app supporting connections for other Regions. By installing this app, you authorize third-party providers to share your data with the service for this Region only, and you can revoke the permissions at any time by uninstalling the app.  
The service will not process or store your data unless you enable the Region. By enabling this Region, you grant our service permissions to process and store your data.  
Even if the Region is not enabled, third-party providers can still share your data with our service if the Region-specific app remains installed, so make sure to uninstall the app once you disable the Region. For more information, see [ Enabling a Region](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-enable).

For more information about connections, see the [AWS CodeConnections API reference](https://docs.aws.amazon.com/codeconnections/latest/APIReference/Welcome.html). For more information about the CodePipeline source action for Bitbucket, see [CodestarConnectionSource](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodestarConnectionSource.html) in the *AWS CodePipeline User Guide*.

To create or attach a policy to your AWS Identity and Access Management (IAM) user or role with the permissions required to use connections, see [AWS CodeConnections permissions reference](security-iam.md#permissions-reference-connections). Depending on when your CodePipeline service role was created, you might need to update its permissions to support AWS CodeConnections. For instructions, see [Update the service role](https://docs.aws.amazon.com/codepipeline/latest/userguide/how-to-update-role-new-services.html) in the *AWS CodePipeline User Guide*.

**Topics**
+ [Create a connection](connections-create.md)
+ [Create a connection to Azure DevOps](connections-create-azure.md)
+ [Create a connection to Bitbucket](connections-create-bitbucket.md)
+ [Create a connection to GitHub](connections-create-github.md)
+ [Create a connection to GitHub Enterprise Server](connections-create-gheserver.md)
+ [Create a connection to GitLab](connections-create-gitlab.md)
+ [Create a connection to GitLab self-managed](connections-create-gitlab-managed.md)
+ [Update a pending connection](connections-update.md)
+ [List connections](connections-list.md)
+ [Delete a connection](connections-delete.md)
+ [Tag connections resources](connections-tag.md)
+ [View connection details](connections-view-details.md)
+ [Share connections with AWS accounts](connections-share.md)