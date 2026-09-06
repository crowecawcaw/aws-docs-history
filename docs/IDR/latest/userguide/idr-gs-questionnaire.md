

# Workload onboarding questionnaire in Incident Detection and Response (exception path)
<a name="idr-gs-questionnaire"></a>

**Note**  
If you can't use the [IDR CLI](idr-gs-idrcli.md) to onboard your workload, use the following questionnaire for workload onboarding.

This topic provides the questionnaire you need to complete when onboarding a workload and configuring alarms to ingest to AWS Incident Detection and Response. The workload onboarding questionnaire covers general information about your workload, its architecture details, alarms, and contacts for incident response. In the alarm ingestion section of the questionnaire, you specify the critical alarms that trigger incident creation in Incident Detection and Response for your workload, as well as runbook information on who to contact and what actions to take. Properly completing this questionnaire is a key step in setting up monitoring and incident response processes for your AWS workloads.

Download the Workload onboarding questionnaire:
+ [English version](https://d3oc37omrta8ht.cloudfront.net/AWS-Incident-Detection-and-Response-Workload-Onboarding-Questionnaire.xlsx)
+ [Japanese version](https://d3oc37omrta8ht.cloudfront.net/JP_AWS-Incident-Detection-and-Response-Workload-Onboarding-Questionnaire.xlsx)

## Workload details - General questions
<a name="idr-gs-questions-general"></a>


**General questions**  

| Question | Example Response | 
| --- | --- | 
| Enterprise Name | Amazon Inc. | 
| Name of this workload (include any abbreviations) | Amazon Retail Operations (ARO) | 
| Primary end user and the function of this workload. | This workload is an e-commerce application that allows end users to purchase various items. This workload is the primary revenue generator for our business. | 

## Workload details - Architecture questions
<a name="idr-gs-questions-arch"></a>


**Architecture questions**  

| Question | Example Response | 
| --- | --- | 
| A list of AWS resource tags used to define resources that are part of this workload. AWS uses these tags to identify this workload's resources to expedite support during incidents.Tags are case sensitive. If you provide multiple tags, all resources used by this workload must have the same tags. | appName: Optimax<br />environment: Production | 
| A list of AWS service(s) utilized by this workload, the AWS account(s) and AWS Region(s) that they are in. | AWS services: Route 53, ALB, ECS, ...<br />Accounts: 123456789101, 123456789102, ...<br />Regions: US-EAST-1, US-WEST-2, ... | 

## Workload details - Alarm ingestion questions
<a name="idr-gs-alarm-questionnaire"></a>

For alarm ingestion questions, you specify the critical alarms for your workload that you want to engage AWS Incident Detection and Response, as well as the contacts you want an Incident Management Engineer to engage when these alarms trigger.

The alarm ingestion section is divided into the following sections:
+ **Contact section:** First, specify the primary contact(s) to be included on the Support Case created with AWS Incident Detection and Response when an alarm triggers, as well as your preferred conferencing application for incident bridges. If no bridge preference is provided, AWS Incident Detection and Response will create an incident bridge during incidents. Next, specify escalation contacts and time intervals to engage them when primary contacts are unreachable. Finally, list any contacts who should receive regular incident status updates through the support case for the duration of an incident.
+ **Alarm matrix:** List the set of alarms that will engage AWS Incident Detection and Response when triggered. See the "Critical Alarm Criteria" defined by AWS Incident Detection and Response when selecting alarms for onboarding. For more information, see [Alarm definition](idr-gs-alarm-definition.md).
  + **Amazon CloudWatch Alarms** (leave this section blank if you don't have Amazon CloudWatch alarms)
  + **Third party APM alarms** (leave this section blank if you don't have Third party APM alarms)
    + **EventBridge EventBus ARN:** This is the ARN of the custom EventBus ARN that you created in [Ingest Alarms from APMs with direct EventBridge integration](idr-gs-ingest_alarms_from_apm_to_eventbridge.md) or [Ingest alarms from APMs without direct integration with EventBridge](idr-gs-ingest-apm-webhooks.md).
    + **Alarm Identifiers:** Share the account number, region, and name of the APM alarm.

## Workload Engagement and Escalation Contacts - Runbook questions
<a name="idr-gs-questions-runbook"></a>


**Runbook questions**  

| Question | Example Response | 
| --- | --- | 
| AWS engages workload contacts through the Support case. Who is the primary contact when an alarm triggers for this workload?<br />Specify your preferred conferencing application and AWS will request these details during an incident.If a preferred conferencing application isn't provided, then AWS will reach out during an incident and provide a Chime bridge for you to join. | Application Team<br />app@example.com<br />\+61 2 3456 7890 | 
| If the primary contact is unavailable during an incident, please provide escalation contacts and timeline in the preferred communication order. | 1. After 10 minutes, if no response from Primary Contact, engage:<br />John Smith - Application Supervisor<br />john.smith@example.com<br />\+61 2 3456 7890<br />2. After 10 minutes, if no response from John Smith, contact:<br />Jane Smith - Operations Manager<br />jane.smith@example.com<br />\+61 2 3456 7890 | 

## Alarm matrix
<a name="idr-gs-questions-alarm-matrix"></a>

Provide the following information to identify the set of alarms that will engage AWS Incident Detection and Response to create incidents on behalf of your workload. Once engineers from AWS Incident Detection and Response have reviewed your alarms, additional onboarding steps will be delivered.

**AWS Incident Detection and Response Critical alarm criteria**:
+ AWS Incident Detection and Response alarms should only enter "Alarm" state upon significant business impact to the monitored workload (loss of revenue/degraded customer experience) that requires immediate operator attention.
+ AWS Incident Detection and Response alarms must also engage your resolvers for the workload at the same time or prior to engagement. AWS Incident Managers collaborate with your resolvers in the mitigation process, and do not serve as first-line responders who then escalate to you.
+ AWS Incident Detection and Response alarm thresholds must be set to an appropriate threshold and duration so that any time an alarm fires an investigation must take place. If an alarm is moving between the "Alarm" and "OK" state, sufficient impact is occurring to warrant operator response and attention.

**AWS Incident Detection and Response Policy for criteria violations**:

These criteria can only be evaluated on a case-by-case basis as events occur. The Incident Management team works with your technical account managers (TAMs) to adjust alarms and in rare cases disable monitoring if it is suspected that customer alarms do not adhere to this criteria and is engaging the Incident Management team unnecessarily at a regular rate.

**Important**  
Provide a group distribution email address when supplying contact addresses, so that you can control recipient additions and deletions without runbook updates.  
Provide the contact phone number for your site reliability engineering (SRE) team if you would like the AWS Incident Detection and Response team to call them after sending an initial engagement email.


**Alarm matrix table for CloudWatch alarms**  

|  |  |  | 
| --- |--- |--- |
| **CloudWatch alarm ARN** | **Primary contact for this alarm.**<br />**(If different from workload primary contact)** | **Specify the most relevant AWS service for this alarm to engage the right engineer. Enter N/A if not needed.** | 
| Example:<br />`arn:aws:cloudwatch:us-east-1:123456789012:alarm:ALB_5xx_Target_Response` | Example:<br />Sam Smith - Application Manager<br />sam.smith@example.com<br />\+61 2 3456 7890 | Example:<br />ECS | 


**Alarm matrix table for third-party APM alarms**  

<table>
<tbody>
  <tr><td colspan="2"><b>EventBridge Event Bus ARN</b><br /><b>(This is created as part of the third-party APM integration to route alerts to AWS Incident Detection and Response.)</b></td><td colspan="2">Example: (There will be an event bus per Account/Region combination)<br /><code>arn:aws:events:us-east-1:123456789012:event-bus/APMName-AWSIncidentDetectionResponse-EventBus</code><br /><code>arn:aws:events:us-west-1:123456789012:event-bus/APMName-AWSIncidentDetectionResponse-EventBus</code></td></tr>
  <tr><td><b>Alarm Identifier</b></td><td><b>What does this metric represent?</b><br /><b>Why is this alarm important?</b></td><td><b>Primary contact for this alarm.</b><br /><b>(If different from workload primary contact)</b></td><td><b>Specify the most relevant AWS service for this alarm to engage the right engineer. Enter N/A if not needed.</b></td></tr>
  <tr><td>Example:<br />ALB_5xx_Target_Response<br />Account ID: 123456789012<br />Region: us-east-1</td><td>Example:<br />This metric represents transaction responses from the targets behind the ALB. If 5XX errors exceeds threshold, it represents a critical failure to process business transactions.</td><td>Example:<br />Sam Smith - Application Manager<br />sam.smith@example.com<br />+61 2 3456 7890</td><td>Example:<br />ECS</td></tr>
</tbody>
</table>
