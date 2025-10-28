# Creating the AWS Transform .NET job plan

After you create your workspace, on the **Jobs** tab, select **Create a job with AWS Transform**. Then follow the prompts from AWS Transform in the chat pane, using natural language. The following are the typical steps to creating a .NET modernization job.

1. AWS Transform will ask you which type of transformation job you would like to create. In the chat, enter _.NET modernization_.
2. AWS Transform will suggest a job name and ask you if you want to change the job name. If you would like to change the job name, let AWS Transform know using natural language, such as, _change the job name to ExampleCorpDotNet1_. Otherwise, in the chat, you can accept the suggested job name.
3. AWS Transform creates the transformation job.
   After you accept the job name, AWS Transform notifies you in the chat window that it is creating the job.

###### Components of the AWS Transform .NET job plan

The AWS Transform .NET job plan in the web app has a left side
bar that lists the phases of the job plan. It also has a right
pane that shows the details. These phases include:

###### Left pane

1. **Get resources to be transformed**
   In this phase, you create a connector to your code repository using AWS CodeConnections. Depending on your repository permissions, an admin of the code repository may need to approve the connector and give AWS Transform access to the repository.
2. **Discover resources for transformation**
   In this phase, AWS Transform assesses your repository.
3. **Prepare for transformation**
   In this phase, AWS Transform notifies you if any dependencies are missing from your repositories. You can upload the missing dependencies or ignore them. If you are not an admin for the repo, an admin may need to approve the final transformation plan.
4. **Transform**
   In this phase, AWS Transforms your repo and provides you the ongoing status during the transformation until it's completed.

###### Right pane

In the top right section, you can select the Region of the transformation job. Make sure that the job Region has the same Region as your AWS CodeConnections connector to your third party repository. For a list of supported Regions, see AWS Transform Regions.

You can also see the job status:

- Awaiting user input
- Time elapsed
- Running
  You can also see the following icons:

- A stop transformation icon
- A refresh icon
- A settings icon
  The right pane contains the following tabs:

###### Dashboard

The _Dashboard_ provides high level summary of the transformation. It shows metrics on number of jobs transformed, transformation applied, and estimated time to complete the transformation.

###### Collaboration

Use the _Collaboration_ tab to establish a connection to your source code repository. AWS Transform supports Bitbucket, GitHub, and GitLab repositories for .NET modernization. You can create only one code repository connector per transformation plan. You must specify the AWS account that you would like to use to access your code repository by using AWS CodeConnections.

###### Worklog

AWS Transform logs its actions in the _Worklog_ tab. The Worklog provides a detailed log of the actions AWS Transform takes, along with human input requests, and your responses to those requests.
