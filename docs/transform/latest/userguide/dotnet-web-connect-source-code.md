# Connect to source code

After [Create a .NET modernization job](dotnet-web-create-job.md "dotnet-web-create-job.md"),
on the **Job Plan** tab, the left pane of the AWS Transform window lists the phases
of the transformation job. The first phase is _Connect source
code_. In this phase, you connect to your source code. You can connect to a source code repository or provide code in a zip file. You have 4 options for connecting to source code:

- [Code Connection](#dotnet-connect-codeconnections "#dotnet-connect-codeconnections"): Connect to source code repository using AWS CodeConnections (GitHub, GitLab, Bitbucket, Azure DevOps).
- [PAT](#connect-with-pat "#connect-with-pat"): Connect to source code repository using a Personal Access Token stored in AWS Secrets Manager.
- [S3](#s3-source-code "#s3-source-code"): Provide an Amazon S3 URI to a code archive zip file (for example, `s3://my-bucket/repos.zip`).
- **Direct Upload**: Drag and drop a code archive zip file into the chat pane.
  Select a code connection method and the agent will guide you through set up.

## Connect to a repository with AWS CodeConnections

If you choose the Code Connection option, the AWS Transform agent uses [AWS CodeConnections](../../../dtconsole/latest/userguide/welcome-connections.md "../../../dtconsole/latest/userguide/welcome-connections.md") to download your .NET codebase from Azure Repos, Bitbucket, GitHub, or GitLab. Transformed code is written to a new writable branch.
You must set up AWS CodeConnections in the same Region as your AWS Transform job.

###### Note

If you have an existing source code repository connector, AWS Transform will notify you. Select **Use existing connector** to use this connector.
If you do not wish to use the existing connector, see [Deleting an existing connector](#deleting-existing-connector "#deleting-existing-connector") before [Adding a new connector](#adding-new-connector "#adding-new-connector"). You can only have one source repository connector per job.

### Adding a new connector

To create a new source code repository connector:

1. Enter the AWS account number that you would like to use for the AWS CodeConnections connector.
2. If you have not set up AWS CodeConnections for the same AWS account, [Set up AWS CodeConnections](../../../dtconsole/latest/userguide/setting-up-connections.md "../../../dtconsole/latest/userguide/setting-up-connections.md").
3. Use the [AWS Developer Tools Console](https://console.aws.amazon.com/codesuite/settings/connections "https://console.aws.amazon.com/codesuite/settings/connections") to create a connection to your [Bitbucket](../../../dtconsole/latest/userguide/connections-create-bitbucket.md "../../../dtconsole/latest/userguide/connections-create-bitbucket.md"), [GitHub](../../../dtconsole/latest/userguide/connections-create-github.md "../../../dtconsole/latest/userguide/connections-create-github.md"),
   [GitHub Enterprise
   Server](../../../dtconsole/latest/userguide/connections-create-gheserver.md "../../../dtconsole/latest/userguide/connections-create-gheserver.md"), [GitLab](../../../dtconsole/latest/userguide/connections-create-gitlab.md "../../../dtconsole/latest/userguide/connections-create-gitlab.md"), or
   [AzureDevOps](../../../dtconsole/latest/userguide/connections-create-azure.md "../../../dtconsole/latest/userguide/connections-create-azure.md")
   repository.
4. Copy the Amazon Resource Name (ARN) of the connection you created.
5. Return to AWS Transform, and paste the ARN of the connection you created.
6. Enter a name for the connector.

###### Note

Do not enter personal information as part of the connector name. 7. Select **Initiate connector creation.** 8. AWS Transform makes the request to create a connector for AWS account you entered, in the same Region as the current transformation job, and notifies you that an approval request is ready to be approved by your AWS administrator in the AWS Management Console. Select **Copy the verification link**. 9. If you are the AWS administrator, sign into the AWS account and go to the verification link to approve the connection request. If you are not the AWS administrator, provide the verification link to your AWS administrator. 10. After the AWS administrator approves the connector request, select **Finalize connector** to complete the connector creation process. Should you wish to use a different connector, select **Restart**, to restart the connector creation process.

The Collaboration tab also includes details about your connector, which include:

- Status -- Approved or Pending approval
- AWS account ID
- AWS Region
- Connection ARN

### Deleting an existing connector

###### Note

If you have an existing source code repository connector, AWS Transform will notify you. Select either **Use existing connector** or **Delete and create a new connector**.

If you choose to delete an existing source code repository connect, AWS Transform will warn you before actually deleting the connector.

1. You can delete an existing connector a couple of ways:

   1. If AWS Transform prompts you to, you can select **Delete and create a new connector**.
   2. You can also select **restart** in the prompt, **To modify this connector, you must restart**.

2. AWS Transform warns you that restarting will delete the connector. To delete the connector, select **Restart** again.
3. AWS Transform warns you again that deleting the connector will remove the connection to your third party repository, such as Bitbucket, GitHub, and GitLab. Also, any AWS Transform jobs that are using this connector will fail if the connector is deleted. To confirm deletion, type _delete_ and select **Delete**.
4. To add a new source code repository connector, see [Adding a new connector](#adding-new-connector "#adding-new-connector").

## Connect to a repository with a Personal Access Token

You can connect to a repository using a Personal Access Token (PAT). Follow these steps:

1. When the agent prompts for a source code connection, choose **PAT** in the chat pane.
2. Read the displayed instructions about generating a PAT and storing it in AWS Secrets Manager.
3. Generate a PAT from your source control.
4. Store your PAT in AWS Secrets Manager and record the Amazon Resource Name (ARN). For example, a GitHub token is formatted like this:

```
github_pat_XXXXXXXXXXXXXXX
```

5. In chat, choose the **Set up connector** link to open a connector form.
6. In the connector form, enter a connector name, your AWS account ID, the secret ARN, and optionally a KMS key ARN. Then submit the form.
7. The agent provides an approval link. Copy the link and send to an administrator to approve the connection. After approval, continue with the agent.

## Connect to source code in Amazon S3

You can connect AWS Transform to source code in Amazon S3 as an alternative to [connecting a source code repository](#dotnet-connect-codeconnections "#dotnet-connect-codeconnections").

### S3 bucket organization

Original source code and transformed code are stored in a common S3 bucket, organized as shown below. You must set up your S3 bucket in the same region as your AWS Transform job. Upload your source code to the bucket as a zip file at root level. The zip file must contain a top level folder for each repository.

During transformation, AWS Transform creates a transform-output folder, and stores the transformation results in that folder. Transformation creates a zip file named _transformed-code.zip_ containing the transformed code. This includes a code differences report file name diff.txt that highlights file changes at a project level.

```

<customer-bucket>/
├── source-code.zip
         ├── repo 1
         ├── repo 2
         ├── ......
         ├── repo n
└── transform-output/
      ├── transformed-code.zip

```

### Adding a new S3 Connector

To create a new S3 source code repository connector:

1. In the AWS console, create an S3 bucket.
2. Upload your source code as a zip file to the S3 bucket.
3. In the AWS Transform web app, start a .NET transformation job. In the **Connect a source code repository** step, select **Connect your source code in S3 bucket** and choose **Save**.
4. On the next page, enter your S3 bucket details and choose **Submit**.

   1. Connector name
   2. AWS Account ID
   3. S3 Bucket Arn
   4. S3 Bucket Encryption Key (optional)

5. Approve the connector:

   1. On the next page, copy the verification link.
   2. Have an approver browse to the link to reach the AWS Transform connector creation request page.
   3. Choose to create a new role or use an existing role.
   4. After reviewing the request, choose **Save** and **Approve** to approve it.

6. Specify the S3 zip file location:

   1. In the AWS Transform web app, wait for status to show **Approved**.
   2. On the **Specify asset location** page, enter an S3 URL for the code zip file in the format `s3://bucket-name/zip-file-name` and choose **Send to AWS Transform**.
   3. The job proceeds to the **Discovery** step to continue the transformation.

### Deleting an S3 Connector

To delete an existing S3 connector:

1. In the AWS Transform web app, select **Manage connectors** at the top right.
2. In the **Manage connectors** window, select the connector.
3. Choose **Delete**.
