

# Create an AWS supported case
<a name="create-an-aws-supported-case"></a>

 You can create an AWS supported case for AWS Security Incident Response through the Console, the API, or the AWS Command Line Interface. AWS supported cases allow you to receive support from Security Incident Response engineers. 

**Important**  
 Demo/simulation-cases are closing after a period of 90 days. 

**Note**  
 AWS Security Incident Response engineers will respond to your case within 15 minutes. Response time is for a first response from AWS Security Incident Response engineers. AWS Security Incident Response makes every reasonable effort to respond to your initial request within this time frame. This response time does not apply to subsequent responses. 

**Note**  
 You can create AWS supported cases not only for active security incidents and investigations, but also for inquiries about AWS Security Incident Response capabilities. This includes questions about GuardDuty suppression rules, alert triaging configurations, proactive response workflows, and general guidance on security posture. Select the **Investigations and Inquiries** case type for these purposes. 

 The following example covers use of the console. 

1.  Sign into AWS Security Incident Response via the AWS Management Console. 

1.  Choose **Create Case** 

1.  Choose **Resolve case with AWS** 

1.  Select the type of request 

   1.  **Active Security Incident**: This type is for urgent incident response support and services. 

   1.  **Investigations and Inquiries**: Use this type for perceived security incidents where AWS Security Incident Response engineers can support in log analysis and secondary confirmation of incident response investigation. You can also use this type for inquiries about GuardDuty findings, suppression rules, alert triaging configurations, proactive response workflows, and general security posture questions related to AWS Security Incident Response capabilities. 

1.  Set the start date estimate to the date of your earliest indicator of the incident. For example, when you experienced abnormal behavior for the first time or when you received the first related security alert. 

1.  Define a title for the case 

1. Provide a detailed description of the case.  Consider the following aspects which can help incident responders with the case resolution:

   1.  What happened? 

   1.  Who discovered and reported the incident? 

   1.  Who is affected by the case? 

   1.  What is the known impact? 

   1.  What is the urgency for this case? 

   1.  Add one or multiple AWS account IDs that are in scope of the case. 

1.  Add optional case details: 

   1.  Select the main services that are impacted from the drop-down list. 

   1.  Select the main regions that are impacted from the drop-down list. 

   1.  Add one or many threat actor IP addresses that you identified as part of this case.  

1.  Add optional additional incident responders to the case that will receive notifications. To add an individual, do the following: 

   1.  Add an email address. 

   1.  Add an optional first and last name. 

   1.  Choose **Add new** to add another individual. 

   1.  To remove an individual, choose the **Remove** option for an individual. 

   1.  Choose **Add** to add all listed individuals to the case. 

      1.  You can select multiple individuals and choose **Remove** to delete them from the list. 

1.  Add optional tags to the case. 

   1.  To add a tag, do the following: 

   1.  Choose **Add new tag**. 

   1.  For **Key**, enter the name of the tag. 

   1.  For **Value**, enter the value of the tag. 

   1.  To remove a tag, choose the **Remove** option for that tag. 

 After a AWS supported case has been created, the AWS Security Incident Response engineers and your incident response team are immediately notified. 

**To create an AWS-supported case with AI investigation**

1. Open the AWS Security Incident Response console at [console.aws.amazon.com/](https://console.aws.amazon.com/).

1. Choose **Cases** from the navigation pane.

1. Choose **Create case**.

1. For **Case type**, select **AWS-supported case**.

1. Provide case details including title, incident start date, and affected AWS account ID.

1. In the **Describe the security event** section, provide a thorough description of the incident.

1. Provide additional information about affected AWS services, regions, and other relevant details.

1. Choose **Create case**.

 After case creation, both the Security Incident Response engineers and AI agent begin working simultaneously. 

**To respond to AI clarifying questions (optional)**

1. Navigate to the **Investigation** tab in your case.

1. Review any clarifying questions presented by the AI agent.

1. Respond to the questions or choose **Skip** if you prefer not to answer.

1. Choose **Submit** to continue. All fields are optional.

**Responsible AI disclosure**

 Investigation summaries are generated using AWS Generative AI capabilities. You are responsible for evaluating AI-generated recommendations in your specific context, implementing appropriate oversight mechanisms, verifying findings independently, and maintaining human oversight of all security decisions. 