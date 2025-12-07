# Create a support interaction

A support interaction is how you begin your engagement with AWS Support. You first describe your issue using natural language and receive assistance tailored to you using AI-enhanced troubleshooting. Your initial interaction might include clarifying questions, contextual solutions, and automated problem resolution, without creating a support case. These interactions might resolve issues independently or serve as the foundation for a support case looping in a human engineer, if needed.

Support interactions differ from support cases in that support cases include engagement with a Cloud Support Engineer. You can choose to automatically generate a support case based on a prior support interaction. The support case maintains all context from the initial support interaction and includes additional AI-generated insights to assist the Cloud Support Engineer with resolving your issue. This powerful combination of AI-enhanced troubleshooting and assistance from AWS Cloud Support Engineers potentially lead to faster issue resolution and reduced down time.

###### Notes

- You can revert to the legacy method of case management by choosing **Use the old experience** in the banner at the top of the Support Center Console. For more information, see [Legacy experience: Creating support cases and case management](case-management-legacy.md "case-management-legacy.md").
- You can sign in to the Support Center Console as an AWS Identity and Access Management (IAM) user. For more information, see
  [Manage access to AWS Support Center](accessing-support.md "accessing-support.md").
- If you can't sign in to the Support Center Console and create a support case, you can use the
  [Contact Us](https://console.aws.amazon.com/console/contacts/one-support "https://console.aws.amazon.com/console/contacts/one-support") page
  instead. You can use this page to get help with billing and account
  issues.

###### To start a support interaction, complete the following steps:

1. Sign in to the [AWS Support Center Console](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support").

###### Tip

In the AWS Management Console, you can also choose the question mark icon (
![](images/questionmark.png)
) and then choose **Support Center**. 2. You have several options for starting your support interaction:

    * Enter details about the issues that you need assistance with. This is how you begin a new support interaction. Enter detailed information about your issue and any troubleshooting steps that you have already taken.
    * **Continue an existing support interaction:** Choose from a recent support interaction shown in the **Describe your issue or continue with** section. This section shows the two most recent support interactions. Access the **Viewing past support interactions** section to see additional past support interactions.
    * **Use a Amazon Q transcript:** Select the Amazon Q icon in the text field to see a list of recent Amazon Q conversations. The five most recent conversations from the AWS GovCloud (US-East) AWS Region are shown. Or, choose from a recent Amazon Q interaction shown in the **Describe your issue or continue with**. When you select a conversation, a summary of that conversation is generated and added to the text box. If you select an Amazon Q conversation, then you see a disclaimer regarding AWS Region and user accessibility.

3. Choose the **Send** icon in the bottom right of the text field.
4. AWS Support generative AI-powered troubleshooting analyzes your query along with your specific AWS environment. You might be prompted to provide additional information to assist with the analysis. If you see a prompt for additional information, enter the requested data, then choose **Submit**. If you don't know or don't have access to the requested information, then you can skip this step and receive a general guidance response instead. Keep in mind that a general guidance response isn't specific to your AWS environment.

When the analysis is complete, you see a summary of the findings, along with remediation steps. To view the sources used in the analysis and remediation steps, choose **Sources**. 5. If you need further assistance, you can complete one of the following options:

    * **Continue with AI-assisted support:** To further refine the AI-assisted analysis and generate a new response, choose **Add more details for a better response**. Enter information in the **Additional details** field, and then choose **Submit**. Keep in mind that this option is for additional context for the original issue. If you need to enter context for a new issue, select **Start new interaction** at the top or bottom of the screen.
    * **Create a support case:** To create a support case with AWS Support, choose **Create a case**. This option starts the case creation workflow. Many of the case details are auto-populated for you based on your support interaction. You can change this information as needed. Your support interaction, including details of any resolution steps provided, are added to the support case. For details on how to create a support case, see [Create a support case from a support interaction](create-support-case-from-interaction.md "create-support-case-from-interaction.md").

At any time throughout the support interaction, you can use the **Thumbs up** and **Thumbs down** icons to provide feedback on your experience.
