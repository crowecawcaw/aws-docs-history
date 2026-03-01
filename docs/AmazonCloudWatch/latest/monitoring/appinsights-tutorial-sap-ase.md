# Tutorial: Set up monitoring for SAP ASE

This tutorial demonstrates how to configure CloudWatch Application Insights to set up monitoring for your SAP
ASE databases. You can use CloudWatch Application Insights automatic dashboards to visualize problem details,
accelerate troubleshooting, and facilitate mean time to resolution (MTTR) for your SAP
ASE databases.

###### Application Insights for SAP ASE topics

- [Supported environments](#appinsights-tutorial-sap-ase-supported-environments "#appinsights-tutorial-sap-ase-supported-environments")
- [Supported operating systems](#appinsights-tutorial-sap-ase-supported-os "#appinsights-tutorial-sap-ase-supported-os")
- [Features](#appinsights-tutorial-sap-ase-features "#appinsights-tutorial-sap-ase-features")
- [Prerequisites](#appinsights-tutorial-sap-ase-prerequisites "#appinsights-tutorial-sap-ase-prerequisites")
- [Set up
  monitoring](#appinsights-tutorial-sap-ase-set-up "#appinsights-tutorial-sap-ase-set-up")
- [Manage
  monitoring](#appinsights-tutorial-sap-ase-manage "#appinsights-tutorial-sap-ase-manage")
- [Configure the alarm threshold](#appinsights-tutorial-sap-hana-configure-alarm-threshold "#appinsights-tutorial-sap-hana-configure-alarm-threshold")
- [View and troubleshoot SAP ASE problems detected by Application Insights](#appinsights-tutorial-sap-ase-troubleshooting-problems "#appinsights-tutorial-sap-ase-troubleshooting-problems")
- [Troubleshooting Application Insights](#appinsights-tutorial-sap-ase-troubleshooting-health-dashboard "#appinsights-tutorial-sap-ase-troubleshooting-health-dashboard")

## Supported environments

CloudWatch Application Insights supports the deployment of AWS resources for the following systems and
patterns. You provide and install SAP ASE database software and supported SAP
application software.

- **One or more SAP ASE databases on a single Amazon EC2 instance** – SAP ASE in a single-node, scale-up
  architecture.
- **Cross-AZ SAP ASE database high availability
  setup** – SAP ASE with high availability configured
  across two Availability Zones using SUSE/RHEL clustering.

###### Note

CloudWatch Application Insights supports only single SAP system ID (SID) ASE HA environments. If multiple ASE HA SIDs are
attached, monitoring will be set up for only the first detected SID.

## Supported operating systems

CloudWatch Application Insights for SAP ASE supports x86-64 architecture on the following operating
systems:

- SuSE Linux 12 SP4
- SuSE Linux 12 SP5
- SuSE Linux 15
- SuSE Linux 15 SP1
- SuSE Linux 15 SP2
- SuSE Linux 15 SP3
- SuSE Linux 15 SP4
- SuSE Linux 15 SP1 For SAP
- SuSE Linux 15 SP2 For SAP
- SuSE Linux 15 SP3 For SAP
- SuSE Linux 15 SP4 For SAP
- SuSE Linux 12 SP4 For SAP
- SuSE Linux 12 SP5 For SAP
- RedHat Linux 7.6
- RedHat Linux 7.7
- RedHat Linux 7.9
- RedHat Linux 8.1
- RedHat Linux 8.4
- RedHat Linux 8.6

## Features

CloudWatch Application Insights for SAP ASE provides the following features:

- Automatic SAP ASE workload detection
- Automatic SAP ASE alarm creation based on static threshold
- Automatic SAP ASE alarm creation based on outlier detection
- Automatic SAP ASE log pattern recognition
- Health dashboard for SAP ASE
- Problem dashboard for SAP ASE

## Prerequisites

You must perform the following prerequisites to configure an SAP ASE database
with CloudWatch Application Insights:

- **SAP ASE configuration parameters** – The following configuration parameters must be enabled on your ASE DB: `"enable monitoring"`,
  `"sql text pipe max messages"`, `"sql text pipe active"`. This allows CloudWatch Application Insights to provide full monitoring capabilities for your DB. If these settings aren't enabled on your ASE database, Application Insights
  will automatically enable them to collect the necessary metrics to allow monitoring.
- **SAP ASE database user** – The
  database user provided during Application Insights onboarding must have permission to
  access the following:
  - System tables in the master database and user (tenant) databases
  - Monitoring tables

- **SAPHostCtrl** – Install and set up SAPHostCtrl on your Amazon EC2 instance.
- **Amazon CloudWatch agent** – Make sure that you are not running a preexisting CloudWatch agent on your Amazon EC2 instance.
  If you have CloudWatch agent installed, make sure to remove the configuration of the resources you are using in CloudWatch Application Insights from the existing CloudWatch agent configuration file to avoid a merge conflict. For more information, see
  [Manually create or edit the CloudWatch agent configuration file](CloudWatch-Agent-Configuration-File-Details.md "CloudWatch-Agent-Configuration-File-Details.md").
- **AWS Systems Manager enablement** – Install SSM
  Agent on your instances, and enable the instances enabled for SSM. For
  information about how to install the SSM agent, see [Working with SSM Agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md") in the _AWS Systems Manager User
  Guide_.
- **Amazon EC2 instance roles** – You must
  attach the following Amazon EC2 instance roles to configure your database.
  - You must attach the `AmazonSSMManagedInstanceCore` role
    to enable Systems Manager. For more information, see [AWS Systems Manager identity-based policy examples](../../../systems-manager/latest/userguide/auth-and-access-control-iam-identity-based-access-control.md "../../../systems-manager/latest/userguide/auth-and-access-control-iam-identity-based-access-control.md").
  - You must attach the `CloudWatchAgentServerPolicy` to
    enable instance metrics and logs to be emitted through CloudWatch. For
    more information, see [Create IAM roles and users for use with Amazon CloudWatch agent](create-iam-roles-for-cloudwatch-agent.md "create-iam-roles-for-cloudwatch-agent.md").
  - You must attach the following IAM inline policy to the Amazon EC2
    instance role to read the password stored in AWS Secrets Manager. For more
    information about inline policies, see [Inline policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") in the _AWS Identity and Access Management User
    Guide_.

  JSON

  ```
  `{
   "Version":"2012-10-17",
   "Statement": [
   {
   "Sid": "VisualEditor0",
   "Effect": "Allow",
   "Action": [
   "secretsmanager:GetSecretValue"
   ],
   "Resource": "arn:aws:secretsmanager:*:*:secret:ApplicationInsights-*"
   }
   ]
  }`

  ```

- **AWS Resource Groups** – You must
  create a resource group that includes all of the associated AWS resources
  used by your application stack to onboard your applications to CloudWatch Application Insights. This
  includes Amazon EC2 instances and Amazon EBS volumes running your SAP ASE database.
  If there are multiple databases per account, we recommend that you create
  one resource group that includes the AWS resources for each SAP ASE
  database system.
- **IAM permissions** – For non-admin
  users:
  - You must create an AWS Identity and Access Management (IAM) policy that allows
    Application Insights to create a service-linked role, and attach it to your
    user identity. For steps to attach the policy, see [IAM policy for CloudWatch Application Insights](appinsights-iam.md "appinsights-iam.md").
  - The user must have permission to create a secret in AWS Secrets Manager to
    store the database user credentials. For more information, see
    [Example: Permission to create secrets](../../../secretsmanager/latest/userguide/auth-and-access_examples.md#auth-and-access_examples_create "../../../secretsmanager/latest/userguide/auth-and-access_examples.md#auth-and-access_examples_create").

  JSON

  ```
  `{
   "Version":"2012-10-17",
   "Statement": [
   {
   "Effect": "Allow",
   "Action": [
   "secretsmanager:CreateSecret"
   ],
   "Resource": "arn:aws:secretsmanager:*:*:secret:ApplicationInsights-*"
   }
   ]
  }`

  ```

- **Service-linked role** – Application Insights
  uses AWS Identity and Access Management (IAM) service-linked roles. A service-linked role is
  created for you when you create your first Application Insights application in the
  Application Insights console. For more information, see [Using service-linked roles for CloudWatch Application Insights](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md").

## Set up monitoring on your SAP ASE database

Use the following steps to set up monitoring for your SAP ASE database

1. Open the [CloudWatch
   console](https://console.aws.amazon.com/cloudwatch "https://console.aws.amazon.com/cloudwatch").
2. From the left navigation pane, under **Insights**, choose
   **Application Insights**.
3. The **Application Insights** page displays the list of
   applications that are monitored with Application Insights, and the monitoring status
   for each application. In the upper right-hand corner, choose **Add
   an application**.
4. On the **Specify application details** page, from the
   dropdown list under **Resource group**, select the AWS
   resource group that contains your SAP ASE database resources. If you
   haven't created a resource group for your application, you can create one by
   choosing **Create new resource group** under the
   **Resource group** dropdown. For more information about
   creating resource groups, see the [_AWS Resource Groups
   User Guide._](../../../ARG/latest/userguide/resource-groups.md "../../../ARG/latest/userguide/resource-groups.md")
5. Under **Monitor CloudWatch Events**, select the check box to
   integrate Application Insights monitoring with CloudWatch Events to get insights from Amazon EBS,
   Amazon EC2, AWS CodeDeploy, Amazon ECS, AWS Health APIs and notifications, Amazon RDS, Amazon S3,
   and AWS Step Functions.
6. Under **Integrate with AWS Systems Manager OpsCenter**, select the
   check box next to **Generate AWS Systems Manager OpsCenter OpsItems for
   remedial actions** to view and get notifications when problems
   are detected for the selected applications. To track the operations that are
   performed to resolve operational work items, called OpsItems, that are
   related to your AWS resources, provide an SNS topic ARN.
7. You can optionally enter tags to help you identify and organize your
   resources. CloudWatch Application Insights supports both tag-based and CloudFormation stack-based resource groups,
   with the exception of Application Auto Scaling groups. For more
   information, see [Tag Editor](../../../ARG/latest/userguide/tag-editor.md "../../../ARG/latest/userguide/tag-editor.md") in the
   _AWS Resource Groups and Tags User Guide_.
8. Choose **Next** to continue to set up monitoring.
9. On the **Review detected components** page, the monitored
   components and their workloads automatically detected by CloudWatch Application Insights are
   listed.

###### Note

Components that contain a detected SAP ASE High Availability workload support only one workload on a component. Components that contain a
detected SAP ASE single node workload support multiple workloads, but you can't add or remove workloads. All automatically detected workloads will be monitored. 10. Choose **Next**. 11. On the **Specify component details** page, enter the
username and password of your SAP ASE databases. 12. Review your application monitoring configuration, and choose
**Submit**. 13. The application details page opens, where you can view the
**Application summary**, the list of
**Monitored components and workloads**, and **Unmonitored
components and workloads**. If you select the radio button next to a
component or workload, you can also view the **Configuration history**,
**Log patterns**, and any **Tags**
that you have created. When you submit your configuration, your account
deploys all of the metrics and alarms for your SAP ASE system, which can
take up to 2 hours.

## Manage monitoring of your SAP ASE database

You can manage user credentials, metrics, and log paths for your SAP ASE database
by performing the following steps:

1. Open the [CloudWatch
   console](https://console.aws.amazon.com/cloudwatch "https://console.aws.amazon.com/cloudwatch").
2. From the left navigation pane, under **Insights**, choose
   **Application Insights**.
3. The **Application Insights** page displays the list of
   applications that are monitored with Application Insights, and the monitoring status
   for each application.
4. Under **Monitored components**, select the radio button
   next to the component name. Then, choose **Manage
   monitoring**.
5. Under **EC2 instance group logs**, you can update the
   existing log path, log pattern set, and log group name. In addition, you can
   add up to three additional **Application logs**.
6. Under **Metrics**, you can choose the SAP ASE metrics
   according to your requirements. SAP ASE metric names are prefixed with
   `asedb`. You can add up to 60 metrics per component.
7. Under **ASE configuration**, enter the username and password
   for the SAP ASE database. This is the username and password that
   Amazon CloudWatch agent uses to connect to the SAP ASE database.
8. Under **Custom alarms**, you can add additional alarms to
   be monitored by CloudWatch Application Insights.
9. Review your application monitoring configuration and choose
   **Submit**. When you submit your configuration, your
   account updates all of the metrics and alarms for your SAP HANA system,
   which can take up to 2 hours.

## Configure the alarm threshold

CloudWatch Application Insights automatically creates a Amazon CloudWatch metric for the alarm to watch, along with
the threshold for that metric. The alarm changes to the `ALARM` state
when the metric surpasses the threshold for a specified number of evaluation
periods. Note that these settings are not retained by Application Insights.

To edit an alarm for a single metric, perform the following steps:

1. Open the [CloudWatch
   console](https://console.aws.amazon.com/cloudwatch "https://console.aws.amazon.com/cloudwatch").
2. In the left navigation pane, choose
   **Alarms**>**All alarms**.
3. Select the radio button next to the alarm that was automatically created
   by CloudWatch Application Insights. Then choose **Actions**, and select
   **Edit** from the dropdown menu.
4. Edit the following parameters under **Metric**.
   1. Under **Statistic**, choose one of the statistics
      or predefined percentiles, or specify a custom percentile. For
      example, `p95.45`.
   2. Under **Period**, choose the evaluations period
      for the alarm. When you evaluate the alarm, each period is
      aggregated into one data point.

5. Edit the following parameters under
   **Conditions**.
   1. Choose whether the metric must be greater than, less than, or
      equal to the threshold.
   2. Specify the threshold value.

6. Under **Additional configuration** edit the following
   parameters.
   1. Under **Datapoints to alarm**, specify the number
      of data points, or evaluation periods, that must be in the
      `ALARM` state to initiate the alarm. When the two
      values match, an alarm is created that enters `ALARM`
      state if the designated number of consecutive periods are exceeded.
      To create an `m` out of `n` alarm, specify a
      lower value for the first data point than for the second. For more
      information about evaluating alarms, see [Evaluating an alarm](CloudWatch_Alarms.md#alarm-evaluation "CloudWatch_Alarms.md#alarm-evaluation").
   2. Under **Missing data treatment**, choose the
      behavior of the alarm when some data points are missing. For more
      information about missing data treatment, see [Configuring how CloudWatch alarms treat missing
      data](CloudWatch_Alarms.md#alarms-and-missing-data "CloudWatch_Alarms.md#alarms-and-missing-data").
   3. If the alarm uses a percentile as the monitored statistic, a
      **Percentiles with low samples** box appears.
      Choose whether to evaluate or ignore cases with low sample rates. If
      you choose **ignore (maintain alarm state)**, the
      current alarm state is always maintained when the sample size is too
      low. For more information about percentiles with low samples, see
      [Percentile-based alarms and low data samples](percentiles-with-low-samples.md "percentiles-with-low-samples.md").

7. Choose **Next**.
8. Under **Notification**, select an SNS topic to notify
   when the alarm is in `ALARM` state, `OK` state, or
   `INSUFFICIENT_DATA` state.
9. Choose **Update alarm**.

## View and troubleshoot SAP ASE problems detected by Application Insights

This section helps you resolve common troubleshooting problems that occur when you configure monitoring for SAP ASE on Application Insights.

###### SAP ASE Backup Server errors

You can identify the error message by checking the dynamically created dashboard. The dashboard shows the error message reported in the
SAP ASE Backup Server. For more details about SAP ASE Backup Server logs, see [SAP Documentation
Backup Server Error Logging](https://help.sap.com/docs/SAP_ASE/aa939a27edb34f019f71cc47b9c0fd9a/a7aeb8b1bc2b10149ccf99b95687a64c.html "https://help.sap.com/docs/SAP_ASE/aa939a27edb34f019f71cc47b9c0fd9a/a7aeb8b1bc2b10149ccf99b95687a64c.html").

###### SAP ASE long running transactions

Identify the long running transaction and confirm whether it can be stopped or if the running time is intentional. For more details, see [2180410 —
How to display transaction log records for long running transactions? — SAP ASE](https://userapps.support.sap.com/sap/support/knowledge/en/2180410 "https://userapps.support.sap.com/sap/support/knowledge/en/2180410").

###### SAP ASE User connections

Review whether your SAP ASE database is sized accordingly for the workload you intend to run on the database. For more details, see [Configuring
User Connections](https://help.sap.com/docs/help/061ec8a5739842df9e505d8944fae8e2/9ea258fceaaa496eb80e17d3d5694ff6.html "https://help.sap.com/docs/help/061ec8a5739842df9e505d8944fae8e2/9ea258fceaaa496eb80e17d3d5694ff6.html") in the SAP documentation.

###### SAP ASE disk space

You can identify the database layer that is causing the problem by checking the
dynamically created dashboard. The dashboard shows the related metrics and log file
snippets. It is important to understand the cause of the disk growth and when
applicable, increase the physical disk size, the allocated disk space, or both. For
more details, see [SAP Documentation disk resize](https://help.sap.com/docs/SAP_ASE/e0d4539d39c34f52ae9ef822c2060077/ab22db00bc2b1014ad3ce047bbf117d7.html "https://help.sap.com/docs/SAP_ASE/e0d4539d39c34f52ae9ef822c2060077/ab22db00bc2b1014ad3ce047bbf117d7.html") in the SAP documentation.

## Troubleshooting Application Insights for SAP ASE

This section provides steps to help you resolve common errors returned by the
Application Insights dashboard.

| Error                                                        | Error returned                                                                                                                                                                                                                                    | Root cause                                                      | Resolution                                                                          |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Unable to add more than 60 monitor metrics.                  | `Component cannot have more than 60 monitored metric`                                                                                                                                                                                             | The current metric limit is 60 monitored metrics per component. | Remove unnecessary metrics to adhere to the limit.                                  |
| No SAP metrics or alarms appear after the onboarding process | The `run` command on the<br>`AWS-ConfigureAWSPackage` failed in AWS Systems Manager. The<br>output shows the error: `CT-LIBRARY error:``ct_connect(): protocol specific layer:<br>external error: The attempt to connect to the server<br>failed` | The username and password might be incorrect.                   | Verify that the username and password are valid, then rerun the onboarding process. |
