

# Creating a ticket for a Jira Cloud integration
<a name="jiracloud-create-ticket"></a>

 After you create an integration with Jira Cloud, you can create a ticket for a finding. 

**Note**  
 A finding will always be associated with a single ticket through its entire lifecycle. Security Hub sends all subsequent updates to a finding to the same ticket after initial creation. If a connector associated with an automation rule is changed, the updated connector is used only for new and incoming findings that match the rule criteria. 

**To create a ticket for a finding**

1.  Sign in to your AWS account with your credentials, and open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home?region=us-east-1](https://console.aws.amazon.com/securityhub/v2/home?region=us-east-1). 

1.  From the navigation pane, under **Inventory**, choose **Findings**. 

1.  Choose a finding. In the finding, choose **Create ticket**. 

1.  For **Integration**, open the dropdown menu, and choose an integration. This integration is the integration you previously created when you configured the Jira Cloud project. Choose the integration where you want findings sent. 

1.  Choose **Create**. 