

# Unified Operations Getting started: Onboard critical alarms to rapid incident management
<a name="uops-gs-onboard-alarms"></a>

To help quickly notify you of critical incidents, complete the following steps to onboard your alarms to AWS Incident Detection and Response

1. Define and configure your critical alarms for rapid incident management. For detailed information, see [Define and configure alarms in Incident Detection and Response](https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-alarms.html) in the *Incident Detection and Response User Guide*.

   1. For steps to set up alarms using Amazon CloudWatch, see [Define and configure alarms in Incident Detection and Response](https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-alarms.html) in the *Incident Detection and Response User Guide*. For AWS recommendations on critical alarm types for various AWS services, see [Incident Detection and Response (IDR)](https://repost.aws/selections/KP6FA7iQgVSVeSNq1jAcjwxg/incident-detection-and-response-idr). Contact your AWS Unified Operations team if you want AWS to automate the creation of critical AWS alarms for your tagged AWS resources.

   1. To redirect or ingest critical alarms from 3rd party APM tools with [direct Amazon EventBridge integration](https://aws.amazon.com/eventbridge/integrations/), such as DataDog, NewRelic, and so on, see [Ingest alarms from APMs that have direct integration with Amazon EventBridge](https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-ingest_alarms_from_apm_to_eventbridge.html) in the *AWS Incident Detection and Response User Guide*. You must deploy a set of AWS resources (AWS Lambda and Amazon EventBridge event bus rules) to transform and redirect your alarm (event) to AWS Incident Detection and Response. Your AWS Unified Operations team can help provide the CloudFormation template to install these resources.

   1. Redirect or ingest critical alarms from your custom monitoring tool through a 3rd party APM tool that doesn’t have direct integration with Amazon EventBridge. For more information, see [Use webhooks to ingest alarms from APMs without direct integration with Amazon EventBridge](https://docs.aws.amazon.com/IDR/latest/userguide/idr-ingesting-alarms-using-webhooks.html) in the *AWS Incident Detection and Response User Guide*. You must deploy a set of AWS resources (API Gateway AWS Lambda functions, and Amazon EventBridge event bus rules) to transform and redirect your alarm (event) to AWS Incident Detection and Response. Your AWS Unified Operations team can help provide the CloudFormation template to install these resources.

1. Provide workload architecture details, point of contact information and runbook information on mitigation actions for critical alarms. To do this, complete the following steps:

   1. Download and complete the [AWS Incident Detection and Response Workload onboarding questionnaire](https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-questionnaire.html) for each critical workload or application and the [Alarm ingestion questionnaire](https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-questionnaire.html) related to each unique workload. 

     The information in these questionnaires helps the AWS team develop an incident remediation runbook. This runbook enables appropriate actions to be taken to quickly troubleshoot and remediate critical alarms before they cause business downtime. For examples and sample information, see [Workload onboarding and alarm ingestion questionnaires in AWS Incident Detection and Response](https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-questionnaire.html). 

1. Provide access to onboard your critical alarms to AWS Incident Detection and Response

   1. Deploy the `AWSServiceRoleForHealth_EventProcessor` service-linked role (SLR) in your AWS account running the critical workload to be monitored by the AWS incident management team. For more information, see [Provision access for alert ingestion to AWS Incident Detection and Response](https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-access-prov.html). 
**Note**  
To assist your with onboarding of large AWS accounts, AWS can provide you with a AWS Command Line Interface script to fast track the provisioning of this SLR.

   1. (Optional) If your alarms are in Amazon CloudWatch, make sure that the AWS Identity and Access Management user or role that's used for alarm testing (before go-live) has the `cloudwatch:SetAlarmState` IAM permission in your AWS account that's running the critical workload. This is needed for alarm testing (gameday) post onboarding. For more information, see [Test onboarded workloads in AWS Incident Detection and Response](https://docs.aws.amazon.com/IDR/latest/userguide/idr-workloads-testing.html).

1. Create a AWS Support case to subscribe a workload for rapid incident management. Note that your AWS account is automatically enabled for inbound rapid incident management, which means you can raise a case to the Unified Operations Incident Detection and Response queue through the Support Center Console, the AWS Command Line Interface, or the AWS SDK for quick action. For AWS to proactively monitor and create incidents with an outbound AWS Support case, create an AWS Support case for your critical workload. To do this, complete the following steps:

   1. Sign in to the [AWS Support Center Console](https://console.aws.amazon.com/support), select **Create case**, and then select **Technical support**.

   1. For **Service** select **Incident Detection and Response**.

   1. For **Category** select **Onboard new workload**.

   1. For **Severity** select **General guidance**.

   1. Attached the Workload and Alarm questionnaires that you completed in the previous step.