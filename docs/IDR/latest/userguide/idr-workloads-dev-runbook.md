# Develop runbooks and response plans for responding to an incident in Incident Detection and Response

AWS Incident Detection and Response uses information captured during your workload onboarding to develop runbooks
for the management of incidents affecting your workloads. Runbooks
document steps Incident Managers take when responding to an incident. A response plan is
mapped to at least one of your workloads. The incident management team creates these
templates from the information provided by you during [workload onboarding](getting-started-idr.md#workload-onboarding "getting-started-idr.md#workload-onboarding").

**Key outputs:**

- Completion of your workload definition on AWS Incident Detection and Response.
- Completion of alarms and runbooks on AWS Incident Detection and Response.
  You can also download an AWS Incident Detection and Response Runbook example: [aws-idr-runbook-example.zip](samples/aws-idr-runbook-example.zip.md "samples/aws-idr-runbook-example.zip.md").

###### Example runbook

###### Description

This document is intended for [CustomerName] - [WorkloadName].

###### Step: Priority

**Priority actions**

1. Send the first correspondence on the Support case to the customer as below.

```
Hello,

This is <<Engineer's name>> from AWS Incident Detection and Response. An alarm has triggered for your workload <<Application_Name>>. I am currently investigating and will update you in a few minutes once I have finished initial investigation.

Alarm Identifier - <insert_CloudWatch_Alarm_ARN_or_APM_Response_Identifier>
```

###### Step: Information

**Engagement plans**

This section describes the engagement plans applicable to this runbook and only contains contact details. Engagement plans will be referenced in the step-by-step **Communication Plans**.

- **Initial engagement**

AWS Incident Detection and Response Team adds customer stakeholder addresses below to the Support case. AWS stakeholders are for additional stakeholders that might need to be made aware of any issues.

    + *Customer Stakeholders*: customeremail1; customeremail2; mobile1
    + *AWS Stakeholders*: aws-idr-oncall@amazon.com; tam-team-email; etc.
    + *One Time Only Contacts*: [These are email contacts that are included on only the first communication. Remove these contacts after the first communication has gone out. These could be customer paging email addresses such as pager-duty that must not be paged for every correspondence. Explicitly add instructions in "Priority" section, "Communication plans" on how to use these only if *One Time Only Contacts* is available.]

- **Incident call setup**

Indicate if the customer requires AWS Incident Detection and Response to create a bridge, if the customer uses a static bridge or if the customer will provide a bridge when an incident is opened.

(Choose one option based on customer preference)

    + AWS Incident Detection and Response create a Amazon Chime/Zoom Bridge
    + Customer's provided static Bridge




    	- Conference Number: < Insert Conference number >
    + Customer provides bridge details for every incident by responding to communication sent out by AWS Incident Detection and Response Team.
    + Other - Specify details.

- **Engagement Escalation**

AWS Incident Detection and Response will reach out to the following contacts when the contacts from the **Initial engagement** plan do not respond to incidents.

For each Escalation Contact indicate if they must be added to the Support case, phoned or both.

    + Make sure that you have called Initial Engagement contact, if applicable, before escalating.
    + *First Escalation Contact*: [escalationEmailAddress#1] / [PhoneNumber] - Wait XX Minutes before escalating to this contact.




    	- [Add contact to Case / Phone] this contact.
    + *Second Escalation Contact*: [escalationEmailAddress#2] / [PhoneNumber] - Wait XX Minutes before escalating to this contact.




    	- [Add Contact to Case / Phone] this contact.
    + etc.

**Communication plans**

This section describes how Incident Management Engineers communicate with designated stakeholders outside the incident call and communication channels.

- **Impact Communication plan**

This plan is initiated when AWS Incident Detection and Response have determined from step **Triage** that an alert indicates potential impact to a customer.

AWS Incident Detection and Response will request the customer to join the predetermined bridge as indicated in **Engagement plans - Incident call setup**.

(Choose one depending on whether _One Time Only Contacts_ is available or not.)

    1. Ensure *Customer Stakeholders* from **Engagement plans - Initial engagement** are added to the case CC.

OR

    1. Ensure *Customer Stakeholders* and *One Time Only Contacts* from **Engagement plans - Initial engagement** are added to the case CC.
    2. Send the engagement notification to the customer based on the following template:


    (Choose one)


    *Impact Template - Amazon Chime Bridge*



    ```
    The following alarm has engaged AWS Incident Detection and Response to an Incident bridge:
        Alarm Identifier - <insert_CloudWatch_Alarm_ARN_or_APM_Response_Identifier>
        Alarm State Change Reason - <insert_state_change_reason>
        Alarm Start Time - <Example: 1 January 2025, 3:30 PM UTC>
    Please join the Amazon Chime Bridge below so we can start the steps outlined in your Runbook:
        Amazon Chime Meeting ID: <insert_Meeting_ID_here>
        Link to Amazon Chime Bridge: <insert_Link_here>
        International dial-in numbers: https://chime.aws/dialinnumbers/
    ```

    *Impact Template - Customer Provided Bridge*



    ```
    The following alarm has engaged AWS Incident Detection and Response:
        Alarm Identifier - <insert_CloudWatch_Alarm_ARN_or_APM_Response_Identifier>
        Alarm State Change Reason - <insert_state_change_reason>
        Alarm Start Time - <Example: 1 January 2025 3:30 PM UTC>
    Please respond with your internal bridge details so we can join and start the steps outlined in your Runbook.
    ```

    *Impact Template - Customer Static Bridge*



    ```
    The following alarm has engaged AWS Incident Detection and Response to an Incident bridge:
        Alarm Identifier - <insert CloudWatch Alarm ARN or APM Response Identifier>
        Alarm State Change Reason - <insert_state_change_reason>
        Alarm Start Time - <Example: 1 January 2025, 3:30 PM UTC>
    Please join the Bridge below so we can start the steps outlined in your Runbook:
        Conference Number: <insert_conference_number>
        Conference URL: <insert_bridge_URL>
    ```
    3. Set the Case to Pending Customer Action.
    4. REMOVE *One Time Only Contacts* from the case after sending above Impact Communication. (If *One Time Only Contacts* is available.)
    5. Follow **Engagement Escalation** plan as mentioned above.
    6. If the customer does not respond within 30 minutes, disengage and continue to monitor until the alarm recovers.

- **No Impact Communication plan**

This plan is initiated when an alarm recovers before Incident Detection and Response have completed initial **Triage**.

    1. Before sending the no impact notification, verify, then remove and/or add customer contacts from the Support Case CC based on the contacts listed in the **Engagement plans - Initial engagement** Engagement plan.


    ["DO NOT add *One Time Only Contacts*."] (Applicable if *One Time Only Contacts* is available.)
    2. Send a no engagement notification to the customer based on the below template:


    *No Impact Template*



    ```
    AWS Incident Detection and Response received an alarm that has recovered for your workload.
        Alarm Identifier - <insert_CloudWatch_Alarm_ARN_or_APM_Response_Identifier>
        Alarm State Change Reason - <insert_state_change_reason>
        Alarm Start Time - <Example: 1 January 2025, 3:30 PM UTC>
        Alarm End Time - <Example: 1 January 2025, 3:35 PM UTC>
    This may indicate a brief customer impact that is currently not ongoing.
    If there is an ongoing impact to your workload, please let us know and we will engage to assist.
    ```
    3. Put the case in to **Pending Customer Action**.
    4. If the customer does not respond within 30 minutes, resolve the case.

**Application architecture overview**

This section provides an overview of the application/workload architecture for Incident Management Engineer and Operations Engineer awareness.

- **AWS Accounts and Regions with key services** - list of AWS accounts with Regions supporting this application. Assists Engineers in assessing underlying infrastructure supporting the application.

  - 123456789012

    - US-EAST-1 - brief desc as appropriate

      - Amazon EC2 - brief desc as appropriate
      - DynamoDB - brief desc as appropriate
      - etc.

    - US-WEST-1 - brief desc as appropriate

      - etc.

  - another-account

    - etc.
