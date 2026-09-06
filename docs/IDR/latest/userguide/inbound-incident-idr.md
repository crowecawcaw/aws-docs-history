

# Request an Incident Response
<a name="inbound-incident-idr"></a>

If a critical incident occurs on your workload that isn't detected by alarms monitored by AWS Incident Detection and Response, you can create a support case to request an Incident Response. You can request an Incident Response for any workload that's subscribed to AWS Incident Detection and Response, including workloads in the process of onboarding, using the AWS Support Center Console, AWS Support API, or AWS Support App in Slack.

The following diagram illustrates the end-to-end workflow for an AWS customer requesting incident assistance from the Incident Detection and Response team, detailing the steps from the initial request through investigation, mitigation, and resolution.

![End-to-end workflow diagram for an incident assistance request](http://docs.aws.amazon.com/IDR/latest/userguide/images/idr-incident-request-flow.png)


To request an Incident Response for an incident that's actively impacting your workload, create an Support case. After the support case is raised, AWS Incident Detection and Response engages you on a conference bridge with the AWS experts required to accelerate the recovery of your workload.

## Request an Incident Response using the AWS Support Center Console
<a name="idr-request-incident-response-console"></a>

To request an incident response, complete the following steps:

1. Open the [AWS Support Center Console](https://console.aws.amazon.com/support/home#/) to create a new support case.

1. For **Subject**, enter a brief summary of the incident. For example, `AWS Incident Detection and Response - Active Incident - workload_name`.

1. For **Description**, enter the details of the incident. We recommend that you include the following details in your support case:
   + Affected AWS resource ARN(s), workload name and its function
   + Description of impact to the business
   + (Optional) Your preferred conference bridge URL. If you don't provide bridge details, AWS Incident Detection and Response creates an AWS conference bridge and sends you an invitation with the bridge URL.

1. (Optional) Attach files that can help describe the incident, such as screenshots or log excerpts.

1. Configure the following case classification fields:
   + **Case type**: **Technical**
   + **Service**: **Incident Detection and Response**
   + **Category**: **Active Incident**
   + **Severity**: **Business-critical system down**

1. Provide additional context to help AWS Incident Detection and Response engage AWS experts faster, such as the impacted AWS service, impacted AWS Region, business impact, impact start time, and affected resources.

1. Choose **Submit**.

1. AWS Incident Detection and Response acknowledges your case within five minutes and engages you on a conference bridge with the appropriate AWS experts.

## Request an Incident Response using the AWS Support API
<a name="idr-request-incident-response-support-api"></a>

You can use the AWS Support API to programmatically create support cases. For more information, see [About the AWS Support API](https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html) in the *AWS Support User Guide*.

## Request an Incident Response using the AWS Support App in Slack
<a name="idr-request-incident-response-support-app-slack"></a>

To use the AWS Support App in Slack to request an Incident Response, complete the following steps:

1. Open the Slack channel that you configured the AWS Support App in Slack in. 

1. Enter the following command:

   ```
   /awssupport create
   ```  
![/awssupport create.](http://docs.aws.amazon.com/IDR/latest/userguide/images/command_supportcreate.png)

1. Enter a **Subject** for this incident. For example, enter **AWS Incident Detection and Response - Active Incident - workload\_name**.

1. Enter the **Problem Description** for this incident. Add the following details:

   **Technical Information:**

   Affected Service(s):

   Affected Resource(s):

   Affected Region(s):

   Workload Name:

   **Business Information:**

   Description of impact to the business:

   [Optional] Customer Bridge Details:

1. Choose **Next**.  
![Create a Support Case.](http://docs.aws.amazon.com/IDR/latest/userguide/images/create-support-case.png)

1. For **Issue Type**, choose **Technical support.**

1. For **Service**, choose **Incident Detection and Response**.

1. For **Category**, choose **Active Incident**.

1. For **Severity**, choose **Business-critical system down**.  
![Choose Support Case Severity.](http://docs.aws.amazon.com/IDR/latest/userguide/images/support-case-severity.png)

1. Optionally enter up to 10 additional contacts in the **Additional contacts to notify** field, separated by commas. These additional contacts receive copies of email correspondence about this incident.  
![Configure additional contacts.](http://docs.aws.amazon.com/IDR/latest/userguide/images/configure-additional-contacts.png)

1. Choose **Review**.

1. A new message that is only visible to you appears in the Slack channel. Review the case details, then choose **Create case**.   
![Review the private message in Slack.](http://docs.aws.amazon.com/IDR/latest/userguide/images/create-case-message.png)

1. Your Case ID is provided in a new message from the AWS Support App in Slack. 

1. Incident Detection and Response acknowledges your case within 5 minutes and engages you on a conference bridge with the appropriate AWS experts.

1. Correspondence from Incident Detection and Response is updated in the case thread.  
![Correspondence from Incident Detection and Response in Slack.](http://docs.aws.amazon.com/IDR/latest/userguide/images/idr-correspondence.jpg)