

# Setting up the connector
<a name="setting-up-jira"></a>

**To install the connector**
**Note**  
 All of the following steps are performed in your Jira account, not in your AWS account. 

1.  Log in to your Jira account. 

1.  In the top navigation bar, choose **Apps**, then select **Explore more apps**. 

1. In the **Discover apps and integrations for Jira** page, enter AWS Well-Architected. Then, choose the **AWS Well-Architected Tool Connector for Jira**.

1. In the app page, choose **Get app**.

1.  In the **Add to Jira** pane, choose **Get it now**. 

1.  After the app installs, to complete setup, choose **Configure**. 

1.  In the **AWS Well-Architected Tool Configuration** page, choose **Connect a new AWS account**. 

1.  Enter your **AccessKeyId** and **Secret Key**. Optional: Enter your **Session Token**. Then, choose **Connect**. 
**Note**  
 Make sure your account has the permission `wellarchitected:ConfigureIntegration`. This permissions is required to add AWS accounts to Jira.   
 Multiple AWS accounts can be connected to AWS WA Tool. 
**Note**  
 As a security best practice, its highly recommended to use short-term IAM credentials. For detail on creating an **AccessKeyId** and **Secret Key** for your AWS account, see [Managing access keys (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey), and for detail on using short term credentials, see [Requesting temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html). 

1.  For **Regions**, select the AWS Regions you want to connect. Then, choose **Connect**. 

 

 **Jira project setup** 

 When using custom projects, make sure you have the following issue types in your project setup: 
+  **Scrum:** Epic, Story, Subtask 
+  **Kanban:** Epic, Task, Subtask 

 For detail on managing issue types, see [Atlassian Support \| Add, edit, and delete an issue type](https://support.atlassian.com/jira-cloud-administration/docs/add-edit-and-delete-an-issue-type/). 

 

**To check the status of the connector in AWS Well-Architected Tool**

1.  Log in to your AWS account and navigate to AWS Well-Architected Tool. 

1.  Select **Settings** in the left navigation pane. 

1.  In the **Jira account syncing** section, under **Jira app connection status**, check for the **Configured** status. 

 The connector is now set up and ready to be configured. To configure Jira sync settings at the account and workload level, see [Configuring the connector](configuring-jira.md). 