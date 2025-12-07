# Creating a ticket for a Jira Cloud integration

After you create an integration with Jira Cloud, you can create a ticket for a finding.

###### Note

A finding will always be associated with a single ticket through its entire lifecycle.
All subsequent updates to a finding after initial creation will be sent to the same ticket.
If a connector associated with an automation rule is changed, the updated connector will only be used for new and incoming findings that match the rule criteria.

###### To create a ticket for a finding

1. Sign in to your AWS account with your credentials, and open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home?region=us-east-1](https://console.aws.amazon.com/securityhub/v2/home?region=us-east-1 "https://console.aws.amazon.com/securityhub/v2/home?region=us-east-1").
2. From the navigation pane, under **Inventory**, choose **Findings**.
3. Choose a finding.
   In the finding, choose **Create ticket**.
4. For **Integration**, open the dropdown menu, and choose an integration.
   This integration is the integration you previously created when you configured the Jira Cloud project.
   Choose the integration where you want findings sent.
5. Choose **Create**.
