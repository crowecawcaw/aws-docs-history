

# Incident management in ECO
<a name="incident-mgmt"></a>

In ECO, you can use the AWS Support Center Console to create incidents. Incidents are EDI performance issues that affect your managed environment, as determined by ECO or you. An incident that the ECO team identiﬁes is ﬁrst received as an "event," which is a change in the system state that monitoring captures. If a conﬁgured threshold is exceeded, then the event initiates an alarm, also called an alert. The ECO team determines if the event is non-impacting, an incident, or a problem. The ECO team also receives incidents that you programmatically create using the AWS Support API with the `service-ams-operations-report-incident` service code.

## What is incident management?
<a name="incident-mgmt-what-is"></a>

Incident management is the process that ECO uses to record, act on, communicate the progress of, and provide notiﬁcation of active incidents. The incident management process quickly restores operations for EDI on AWS, minimizes business impact, and keeps concerned parties informed.

The following issues are examples of incidents that ECO manages:
+ Loss or degradation of network connectivity
+ An unresponsive process or API
+ A scheduled task that isn't being performed, such as a failed backup 

The following graphic shows the workﬂow of an incident reported by you to ECO.

![ECO incidents reported by you.](http://docs.aws.amazon.com/EDI/latest/eco-support-guide/images/ecoIncidentMgmt.png)


The following graphic shows the workﬂow of an incident reported by ECO to you.

![ECO incidents reported to you by ECO.](http://docs.aws.amazon.com/EDI/latest/eco-support-guide/images/ecoIncidentMgmt2.png)


## Incident priority
<a name="incident-mgmt-priority"></a>

Incidents that you create in AWS Support Center or AWS Support API have different classiﬁcations from incidents that you create in the AMS console.

The following classifications define the priority level for AWS or EDI related services and applications:
+ **Low** – Non-critical functions of your business service or application are impacted.
+ **Medium** – A business service or application is available but isn't performing according to the applicable service description.
+ **High** – Your business is signiﬁcantly impacted. Critical functions of your application or resources are unavailable. The **High** priority level is reserved for the most critical outages that affect production systems.

**Note**  
The AWS Support Center Console offers five levels of incident priority that we modified to the preceding three levels of priority.

## Incident resolution
<a name="incident-resolution"></a>

ECO uses IT service management (ITSM) incident management best practices to restore service as quickly as possible. We provide all day and night, all week, all year, follow-the-sun support through operations centers around the world with dedicated operators that actively watch monitoring dashboards and incident queues.

**Note**  
For incident response times, see [Incident management response time](eco-sd.md#incident-response-time)

Our operations engineers use internal incident tracking tools to identify, log, categorize, prioritize, diagnose, resolve, and close incidents. We provide you with updates on all the activities through the AWS Support Center and the AWS Support API. Our operators are deeply familiar with EDI supported infrastructure and have expert-level technical skills to address identiﬁed issues. If ECO operators need assistance, they contact the AWS Support and AWS service teams.

After the ECO team receives your incident, they validate the priority and classiﬁcation and work with you if they require clariﬁcations. For example, if the incident report is better classiﬁed as a service request, they reclassify it, the ECO service request team takes over, and you're notiﬁed. ECO operators consult internal documentation to quickly resolve the incident. If an operator can't resolve the incident, they escalate it to other support teams. After it's resolved, the ECO team documents the incident and resolution for future use.

In cases where critical severity incidents are impacting your crucial workloads, ECO might recommend a restore. The risks of a restore and the impact from the required service downtime help determine whether the ECO team restores from a known functional backup. If the issue is urgent, then ECO can initiate a restore. If a restore is too risky, then ECO will help you troubleshoot the issue.

## Working with incidents in the Support Center
<a name="incident-work-with"></a>

You can perform the following tasks in the AWS Support Center:
+ Report and update an incident.
+ Get a list of and detailed information about your submitted incidents.
+ Narrow your search for incidents by status and other ﬁlters.
+ Add communications and ﬁle attachments to your incidents and add email recipients for case correspondence.
+ Initiate a live chat or request a callback on your incident.
+ Resolve incidents.
+ Rate incident communications.

After you submit an incident, the ECO team works with you to resolve the incident according to the incident response time matrix.

## Submitting EDI incidents
<a name="incident-submit"></a>

To report an incident, follow these steps:

1. Sign in to [Support Center Console](https://console.aws.amazon.com/support/home#/).

1. Choose **Create case** and then **Create incident report**. The **Technical** support issue type auto-selects.  
![ECO incident submit page.](http://docs.aws.amazon.com/EDI/latest/eco-support-guide/images/ecoSubmitIncident-crop.png)

1. Choose options from the following menus:

   1. **Service** – AMS Operations – Report Incident is selected by default

   1. For **Category** – select Energy Data Insights (EDI) – Application Issues

   1. **Severity** – as appropriate

   Choose **Next step: Additional information**. The **Additional information** page opens.

1. Include information about your incident and then choose **Next step: Solve now or contact us**. The **Solve now or contact us** page opens to the **Solve now** tab by default.

1. The **Solve now** tab offers AI generated suggestions for your incident. Choose **Next**. The **Contact us** tab opens.

1. On the **Contact us** tab, ensure that **English** is your preferred language because EDI supports only English for incident reports. Choose a contact method:
   + **Web**, selected by default – An ECO representative emails your configured contact.
   + **Phone** – An ECO representative calls you back. Enter your AWS Region, phone number, and extension if applicable.
   + **Chat** – Chat online with an ECO representative. This option adds you to the chat queue.

   Use the **Additional contacts** option to add email addresses you want copied on your incident report.

1. Choose **Submit**. A case details page opens with information on the incident and a **Correspondence** area that includes the description of the report that you created. To provide additional details or updates in status, choose **Reply**. For cases that include a lot of correspondence, choose **Load More** to view all communication.

1. After the incident has been resolved, choose **Resolve Case**. Be sure to rate the service through the 1-5 star rating to let the ECO team know how we're doing.

**Note**  
Make your description as detailed as possible. Include relevant resource information, along with anything else that might help us understand your issue. For example, to troubleshoot performance, include timestamps and logs. For feature requests or general guidance questions, include a description of your environment and purpose. In all cases, follow the Description Guidance that appears on your case submission form. When you provide as much detail as possible, you increase the chances that ECO can quickly resolve your case. You can use the AWS Support API with the `service-ams-operations-report-incident` service code to report an incident.

For more information about how to use the AWS Support Center Console to report an incident, see [Creating support cases and case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html) in the *AWS Support User Guide*.