# Tutorial: Set up monitoring for SAP

HANA

This tutorial demonstrates how to configure CloudWatch Application Insights to set up monitoring for your SAP
HANA databases. You can use CloudWatch Application Insights automatic dashboards to visualize problem details,
accelerate troubleshooting, and facilitate mean time to resolution (MTTR) for your SAP
HANA databases.

###### Application Insights for SAP HANA topics

- [Supported
  environments](#appinsights-tutorial-sap-hana-supported-environments "#appinsights-tutorial-sap-hana-supported-environments")
- [Supported operating
  systems](#appinsights-tutorial-sap-hana-supported-os "#appinsights-tutorial-sap-hana-supported-os")
- [Features](#appinsights-tutorial-sap-hana-features "#appinsights-tutorial-sap-hana-features")
- [Prerequisites](#appinsights-tutorial-sap-hana-prerequisites "#appinsights-tutorial-sap-hana-prerequisites")
- [Set up
  monitoring](#appinsights-tutorial-sap-hana-set-up "#appinsights-tutorial-sap-hana-set-up")
- [Manage
  monitoring](#appinsights-tutorial-sap-hana-manage "#appinsights-tutorial-sap-hana-manage")
- [Troubleshooting problems detected](#appinsights-tutorial-sap-hana-troubleshooting "#appinsights-tutorial-sap-hana-troubleshooting")
- [Detecting outliers](#appinsights-tutorial-sap-hana-troubleshooting-anomaly-detection "#appinsights-tutorial-sap-hana-troubleshooting-anomaly-detection")
- [Troubleshooting Application Insights](#appinsights-tutorial-sap-hana-troubleshooting-health-dashboard "#appinsights-tutorial-sap-hana-troubleshooting-health-dashboard")

## Supported

environments

CloudWatch Application Insights supports the deployment of AWS resources for the following systems and
patterns. You provide and install SAP HANA database software and supported SAP
application software.

- **SAP HANA database on a single Amazon EC2
  instance** — SAP HANA in a single-node, scale-up
  architecture, with up to 24TB of memory.
- **SAP HANA database on multiple Amazon EC2
  instances** — SAP HANA in a multi-node, scale-out
  architecture.
- **Cross-AZ SAP HANA database high availability
  setup** — SAP HANA with high availability configured
  across two Availability Zones using SUSE/RHEL clustering.

###### Note

CloudWatch Application Insights supports only single SID HANA environments. If multiple HANA SIDs are
attached, monitoring will be set up for only the first detected SID.

## Supported operating

systems

CloudWatch Application Insights for SAP HANA supports x86-64 architecture on the following operating
systems:

- SuSE Linux 12 SP4 For SAP
- SuSE Linux 12 SP5 For SAP
- SuSE Linux 15
- SuSE Linux 15 SP1
- SuSE Linux 15 SP2
- SuSE Linux 15 For SAP
- SuSE Linux 15 SP1 For SAP
- SuSE Linux 15 SP2 For SAP
- SuSE Linux 15 SP3 For SAP
- SuSE Linux 15 SP4 For SAP
- SuSE Linux 15 SP5 For SAP
- RedHat Linux 8.6 For SAP With High Availability and Update Services
- RedHat Linux 8.5 For SAP With High Availability and Update Services
- RedHat Linux 8.4 For SAP With High Availability and Update Services
- RedHat Linux 8.3 For SAP With High Availability and Update Services
- RedHat Linux 8.2 For SAP With High Availability and Update Services
- RedHat Linux 8.1 For SAP With High Availability and Update Services
- RedHat Linux 7.9 For SAP With High Availability and Update Services

## Features

CloudWatch Application Insights for SAP HANA provides the following features:

- Automatic SAP HANA workload detection
- Automatic SAP HANA alarm creation based on static threshold
- Automatic SAP HANA alarm creation based on outlier detection
- Automatic SAP HANA log pattern recognition
- Health dashboard for SAP HANA
- Problem dashboard for SAP HANA

## Prerequisites

You must perform the following prerequisites to configure an SAP HANA database
with CloudWatch Application Insights:

- **SAP HANA** – Install a running and
  reachable SAP HANA database 2.0 SPS05 on an Amazon EC2 instance.
- **SAP HANA database user** – A
  database user with monitoring roles must be created in the SYSTEM database
  and all tenants.

###### Example

The following SQL commands create a user with monitoring roles.

```
su - `<sid>`adm
hdbsql -u SYSTEM -p `<SYSTEMDB password>` -d SYSTEMDB
CREATE USER CW_HANADB_EXPORTER_USER PASSWORD `<Monitoring user password>` NO FORCE_FIRST_PASSWORD_CHANGE;
CREATE ROLE CW_HANADB_EXPORTER_ROLE;
GRANT MONITORING TO CW_HANADB_EXPORTER_ROLE;
GRANT CW_HANADB_EXPORTER_ROLE TO CW_HANADB_EXPORTER_USER;
```

- **Python 3.8** – Install Python 3.8 or
  later versions on your operating system. Use the latest release of Python. If
  Python3 is not detected on your operating system, Python 3.6 will be installed.

For more information, see the [installation example](#install "#install").

###### Note

Manual installation of Python 3.8 or higher is required for SuSE Linux 15 SP4, RedHat Linux 8.6, and later operating systems.

- **Pip3** – Install the installer
  program, pip3, on your operating system. If pip3 is not detected on your
  operating system, it will be installed.
- **hdbclient** – CloudWatch Application Insights uses the python driver to connect to the SAP HANA database. If the client is not installed under python3, ensure that you have hdbclient tar file version `2.10 or later` under
  `/hana/shared/SID/hdbclient/`.
- **Amazon CloudWatch agent** – Make sure that you are not running a preexisting CloudWatch agent on your Amazon EC2 instance.
  If you have CloudWatch agent installed, make sure to remove the configuration of the resources you are using in CloudWatch Application Insights from the existing CloudWatch agent configuration file to avoid a merge conflict. For more information, see
  [Manually create or edit the
  CloudWatch agent configuration file](CloudWatch-Agent-Configuration-File-Details.md "CloudWatch-Agent-Configuration-File-Details.md").
- **AWS Systems Manager enablement** – Install
  SSM Agent on your instances, and the instances must be enabled for SSM.
  For information about how to install the SSM Agent, see [Working with SSM
  Agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md") in the _AWS Systems Manager User Guide_.
- **Amazon EC2 instance roles** – You must
  attach the following Amazon EC2 instance roles to configure your database.
  - You must attach the `AmazonSSMManagedInstanceCore` role
    to enable Systems Manager. For more information, see [AWS Systems Manager identity-based policy examples](../../../systems-manager/latest/userguide/auth-and-access-control-iam-identity-based-access-control.md "../../../systems-manager/latest/userguide/auth-and-access-control-iam-identity-based-access-control.md").
  - You must attach the `CloudWatchAgentServerPolicy` to
    enable instance metrics and logs to be emitted through CloudWatch. For
    more information, see [Create IAM roles and users for use with CloudWatch
    agent](create-iam-roles-for-cloudwatch-agent.md "create-iam-roles-for-cloudwatch-agent.md").
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

- **AWS resource groups** – You must
  create a resource group that includes all of the associated AWS resources
  used by your application stack to onboard your applications to CloudWatch Application Insights. This
  includes Amazon EC2 instances and Amazon EBS volumes running your SAP HANA database.
  If there are multiple databases per account, we recommend that you create
  one resource group that includes the AWS resources for each SAP HANA
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
  Application Insights console. For more information, see [Using service-linked roles for
  CloudWatch Application Insights](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md").

## Set up your SAP HANA database

for monitoring

Use the following steps to set up monitoring for your SAP HANA database

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
   resource group that contains your SAP HANA database resources. If you
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
   resources. CloudWatch Application Insights supports both tag-based and AWS CloudFormation stack-based resource groups,
   with the exception of Application Auto Scaling groups. For more
   information, see [Tag Editor](../../../ARG/latest/userguide/tag-editor.md "../../../ARG/latest/userguide/tag-editor.md") in the
   _AWS Resource Groups and Tags User Guide_.
8. Choose **Next** to continue to set up monitoring.
9. On the **Review detected components** page, the monitored
   components and their workloads automatically detected by CloudWatch Application Insights are
   listed.
   1. To add workloads to a component that contains a detected SAP HANA
      single node workload, select the component, then choose **Edit
      component**.

   ###### Note

   Components that contain a detected SAP HANA multi node or HANA High Availability workload support only one workload on a component.

   ![The review components for monitoring page of the CloudWatch Application Insights console: select component to edit.](images/appinsights-multiapp-hana-review.png) 2. To add a new workload, choose **Add new workload**.

   ![The edit component section of the CloudWatch Application Insights console: choose lower left button to add workload.](images/appinsights-multiapp-hana-edit.png) 3. When you are finished editing workloads, choose **Save changes**.

10. Choose **Next**.
11. On the **Specify component details** page, enter the username and password.
12. Review your application monitoring configuration, and choose
    **Submit**.
13. The application details page opens, where you can view the
    **Application summary**, the list of
    **Monitored components and workloads**, and **Unmonitored
    components and workloads**. If you select the radio button next to a
    component or workload, you can also view the **Configuration history**,
    **Log patterns**, and any **Tags**
    that you have created. When you submit your configuration, your account
    deploys all of the metrics and alarms for your SAP HANA system, which can
    take up to 2 hours.

## Manage monitoring of your SAP

HANA database

You can manage user credentials, metrics, and log paths for your SAP HANA database
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
6. Under **Metrics**, you can choose the SAP HANA metrics
   according to your requirements. SAP HANA metric names are prefixed with
   `hanadb`. You can add up to 40 metrics per component.
7. Under **HANA configuration**, enter the password and user
   name for the SAP HANA database. This is the username and password that
   Amazon CloudWatch agent uses to connect to the SAP HANA database.
8. Under **Custom alarms**, you can add additional alarms to
   be monitored by CloudWatch Application Insights.
9. Review your application monitoring configuration and choose
   **Submit**. When you submit your configuration, your
   account updates all of the metrics and alarms for your SAP HANA system,
   which can take up to 2 hours.

## View and

troubleshoot SAP HANA problems detected by CloudWatch Application Insights

The following sections provide steps to help you resolve common troubleshooting
scenarios that occur when you configure monitoring for SAP HANA on
Application Insights.

###### Troubleshooting topics

- [SAP HANA
  database reaches memory allocation limit](#appinsights-tutorial-sap-hana-troubleshooting-memory "#appinsights-tutorial-sap-hana-troubleshooting-memory")
- [Disk
  full event](#appinsights-tutorial-sap-hana-troubleshooting-disk-full "#appinsights-tutorial-sap-hana-troubleshooting-disk-full")
- [SAP HANA backup stopped running](#appinsights-tutorial-sap-hana-troubleshooting-backup-stopped "#appinsights-tutorial-sap-hana-troubleshooting-backup-stopped")

### SAP HANA

database reaches memory allocation limit

###### Description

Your SAP application that is backed by an SAP HANA database malfunctions
because of high memory pressure, leading to application performance
degradation.

###### Resolution

You can identify the application layer that is causing the problem by
checking the dynamically created dashboard, which shows the related metrics
and log file snippets. In the following example, the problem may be because
of a large data load in the SAP HANA system.

![Memory allocation exceeded.](images/appinsights-memory-allocation-1.png)

The used memory allocation exceeds the threshold of 80 percent of the total
memory allocation limit.

![Log group showing out of memory.](images/appinsights-memory-allocation-2.png)

The log group shows the scheme `BNR-DATA` and table
`IMDBMASTER_30003` ran out of memory. In addition, the log group
shows the exact time of the issue, current global location limit, shared memory,
code size, and OOM reservation allocation size.

![Log group text.](images/appinsights-memory-allocation-3.png)

### Disk

full event

###### Description

Your SAP application that is backed by an SAP HANA database stops
responding, which leads to an inability to access the database.

###### Resolution

You can identify the database layer that is causing the problem by
checking the dynamically created dashboard, which shows the related metrics
and log file snippets. In the following example, the problem may be that the
administrator failed to enable automatic log backup, which caused the
sap/hana/log directory to fill up.

![Log group showing out of memory.](images/appinsights-disk-full-1.png)

The log group widget in the problem dashboard shows the `DISKFULL`
event.

![Log group showing out of memory.](images/appinsights-disk-full-2.png)

### SAP HANA backup stopped running

###### Description

Your SAP application that is backed by an SAP HANA database has stopped
working.

###### Resolution

You can identify the database layer that is causing the problem by
checking the dynamically created dashboard, which shows the related metrics
and log file snippets.

The log group widget in the problem dashboard shows the `ACCESS
 DENIED` event. This includes additional information, such as the S3
bucket, the S3 bucket folder, and the S3 bucket Region.

![Log group showing out of memory.](images/appinsights-backup-stopped-2.png)

## Detecting outliers for SAP HANA

For specific SAP HANA metrics, such as the number of thread count, CloudWatch applies
statistical and machine learning algorithms to define the threshold. These
algorithms continuously analyze the metrics of the SAP HANA database, determine
normal baselines, and surface anomalies with minimal user intervention. The
algorithms generate an outlier detection model, which generates a range of expected
values that represent normal metric behavior.

Detecting outliers algorithms account for the seasonality and trend changes of
metrics. The seasonality changes can be hourly, daily, or weekly, as shown in the
following examples of the SAP HANA CPU usage.

![Log group showing out of memory.](images/appinsights-anomaly-detection.png)

After you create a model, CloudWatch outlier detection continuously evaluates the model
and makes adjustments to it to ensure that is it as accurate as possible. This
includes retraining the model to adjust if the metric values evolve over time or
experience sudden changes. It also includes predictors to improve the models for
metrics that are seasonal, spiky, or sparse.

## Troubleshooting Application Insights for SAP HANA

This section provides steps to help you resolve common errors returned by the
Application Insights dashboard.

### Unable to add more than 60

monitored metrics

The output shows the following error.

```
Component cannot have more than 60 monitored metrics
```

**Root cause** – The current metric limit is 60 monitored metrics per component.

**Resolution** – To stay under the limit, remove metrics that are not necessary.

### No SAP metrics appear after the onboarding process

Use the following information to find out why SAP metrics don't appear on the dashboard after the onboarding process. The first step is to troubleshoot why the SAP metrics don't appear using the AWS Management Console or Exporter logs from an Amazon EC2 instance. Next, review the error output to find a resolution.

#### Troubleshoot why SAP metrics don't appear after onboarding

You can use the AWS Management Console or exporter logs from an Amazon EC2 instance for troubleshooting.

AWS Management Console

###### Troubleshoot no SAP metrics appear after onboarding using the console

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the left navigation pane, choose **State Manager**.
3. Under **Associations**, check the
   status of the document
   `AWSEC2-ApplicationInsightsCloudwatchAgentInstallAndConfigure`.
   If the status is `Failed`, under **Execution id**, select the failed id and view the output.
4. Under **Associations**, check the status of the document `AWS-ConfigureAWSPackage`. If the status is `Failed`, under **Execution id**, select the failed id and view the output.

Exporter logs from Amazon EC2 instance

###### Troubleshoot no SAP metrics appear after onboarding using

exporter logs

1. Connect to the Amazon EC2 instance where your SAP HANA database is running.
2. Find the correct naming convention for
   `WORKLOAD_SHORT_NAME` using the following
   command. You will use this short name in the following two
   steps.

```
sudo systemctl | grep exporter
```

###### Note

Application Insights adds a suffix, `WORKLOAD_SHORT_NAME` to the service name depending on the workload that is running. The short names for SAP HANA single node, multiple nodes, and high availability deployments are
`HANA_SN`, `HANA_MN`, and `HANA_HA`. 3. To check for errors in the exporter manager service logs, run the following command replacing `WORKLOAD_SHORT_NAME` with the short name you found in [Step 2](#step-find-short-name "#step-find-short-name").

```
sudo journalctl -e --unit=prometheus-hanadb_exporter_manager_`WORKLOAD_SHORT_NAME`.service
```

4. If the exporter manager service logs do not show an error, check for errors in the exporter service logs by running the following command.

```
sudo journalctl -e --unit=prometheus-hanadb_exporter_`WORKLOAD_SHORT_NAME`.service
```

#### Resolving the common root causes for SAP metrics not appearing after onboarding

The following examples describe how to resolve the common root causes of
SAP metrics not appearing after onboarding.

- The output shows the following error.

```
Reading json config file path: /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.d/default ...
Reading json config file path: /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.d/ssm_AmazonCloudWatch-ApplicationInsights-SSMParameterForTESTCWEC2INSTANCEi0d88867f1f3e36285.tmp ...
2023/11/30 22:25:17 Failed to merge multiple json config files.
2023/11/30 22:25:17 Failed to merge multiple json config files.
2023/11/30 22:25:17 Under path : /metrics/append_dimensions | Error : Different values are specified for append_dimensions
2023/11/30 22:25:17 Under path : /metrics/metrics_collected/disk | Error : Different values are specified for disk
2023/11/30 22:25:17 Under path : /metrics/metrics_collected/mem | Error : Different values are specified for mem
2023/11/30 22:25:17 Configuration validation first phase failed. Agent version: 1.0. Verify the JSON input is only using features supported by this version.
```

**Resolution** – Application Insights is trying to configure the same metrics that are pre-configured as part of the existing CloudWatch agent configuration file. Remove the existing files under
`/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.d/` or remove the metrics that are causing the conflict from the existing CloudWatch agent configuration file.

- The output shows the following error.

```
Unable to find a host with system database, for more info rerun using -v
```

**Resolution** – The username, password, or database port may be incorrect. Verify that the username, password, and port are valid, then re-run the onboarding process.

- The output shows the following error.

```
This hdbcli installer is not compatible with your Python interpreter
```

**Resolution** – Upgrade pip3 and wheel as shown in the following example for Python 3.6.

```
python3.6 -m pip install --upgrade pip setuptools wheel
```

- The output shows the following error.

```
Unable to install hdbcli using pip3. Please try to install it
```

**Resolution** – Ensure that you have followed the `hdbclient` prerequisites or install `hdbclient` manually under pip3.

- The output shows the following error.

```
Package 'boto3' requires a different Python: 3.6.15 not in '>= 3.7'
```

**Resolution** – Python 3.8 or higher is required for this operating system version. Check the Python 3.8 prerequisites and install it.

- The output shows one of the following installation errors.

```
Can not execute `setup.py` since setuptools is not available in the build environment
```

or

```
[SSL: CERTIFICATE_VERIFY_FAILED]
```

**Resolution** – Install Python using SUSE Linux commands as shown in the following example. The following example installs the latest version of [Python 3.8](https://www.python.org/downloads/ "https://www.python.org/downloads/").

```
wget https://www.python.org/ftp/python/3.8.<LATEST_RELEASE>/Python-3.8.<LATEST_RELEASE>.tgz
tar xf Python-3.*
cd Python-3.*/
sudo zypper install make gcc-c++ gcc automake autoconf libtool
sudo zypper install zlib-devel
sudo zypper install libopenssl-devel libffi-devel
./configure --with-ensurepip=install
sudo make
sudo make install
sudo su
python3.8 -m pip install --upgrade pip setuptools wheel

```
