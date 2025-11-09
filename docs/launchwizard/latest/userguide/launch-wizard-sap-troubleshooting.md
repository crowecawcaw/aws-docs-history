# Troubleshoot AWS Launch Wizard for SAP

Each application in your account in the same AWS Region can be uniquely identified by
the application name specified at the time of a deployment. The application name can be used
to view the details related to the application launch.

###### Contents

- [Launch Wizard provisioning events](#launch-wizard-sap-provisioning "#launch-wizard-sap-provisioning")
- [CloudWatch Logs](#launch-wizard-sap-logs "#launch-wizard-sap-logs")
- [AWS CloudFormation stack](#launch-wizard-sap-cloudformation "#launch-wizard-sap-cloudformation")
- [Pre- and post-deployment
  configuration scripts](#launch-wizard-sap-troubleshooting-scripts "#launch-wizard-sap-troubleshooting-scripts")
- [Application launch quotas](#launch-wizard-sap-quotas "#launch-wizard-sap-quotas")
- [Instance level logs](#launch-wizard-sap-instance-level-logs "#launch-wizard-sap-instance-level-logs")
- [SAP application software deployment
  logs](#launch-wizard-sap-application-logs "#launch-wizard-sap-application-logs")
- [Errors](#launch-wizard-sap-errors "#launch-wizard-sap-errors")
- [AWS Systems Manager for SAP](#launch-wizard-sap-troubleshoot-ssm "#launch-wizard-sap-troubleshoot-ssm")
- [Support](#launch-wizard-sap-support "#launch-wizard-sap-support")

## Launch Wizard provisioning events

Launch Wizard captures events from SSM Automation and AWS CloudFormation to track the status of an ongoing
application deployment. If an application deployment fails, you can view the deployment
events for this application by selecting **Deployments** from the
navigation pane. A failed event shows a status of **Failed** along with
a failure message.

## CloudWatch Logs

Launch Wizard streams provisioning logs from all of the AWS log sources, such as AWS CloudFormation, SSM,
and CloudWatch Logs. You can access CloudWatch logs for your SAP deployment with the following
steps.

1. Sign in to console.aws.amazon.com and go to AWS Launch Wizard.
2. Under **Deployments** on the left panel, go to
   **SAP** and you can see the list of your SAP
   deployments.
3. Select the failed deployment for which you want to verify the logs.
4. Choose **Actions** > **View/Manage
   resources** > **View CloudWatch application
   logs**.
5. You can now view the detailed logs and log streams that provide additional
   information on the SAP application type that failed during deployment.

## AWS CloudFormation stack

Launch Wizard uses AWS CloudFormation to provision the infrastructure resources of an application. Launch Wizard
launches various stacks in your account for validation and application resource
creation. You can verify the stacks via AWS console or AWS CLI.

Console

1. Sign in to console.aws.amazon.com and go to AWS Launch Wizard.
2. Under **Deployments** on the left panel, go to
   **SAP** and you can see the list of your SAP
   deployments.
3. Select the failed deployment for which you want to verify the
   stacks.
4. Choose **Actions** > **View/Manage
   resources** > **View CloudFormation template** .
5. You can now view all the stacks and their current status. To see
   more details on any stack, select a **Stack
   name**.
6. You are now on the **Stack details** page of your
   selected stack. Choose **Events** from the top menu
   bar to view the cause of the failure.

CLI
AWS CloudFormation stacks can be found in your account using the AWS CloudFormation [describe-stacks](../../../AWSCloudFormation/latest/UserGuide/using-cfn-describing-stacks.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-describing-stacks.md") API. The following are the relevant filters for
the [describe-stacks](../../../AWSCloudFormation/latest/UserGuide/using-cfn-describing-stacks.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-describing-stacks.md") API.

- **Application resources**

`LaunchWizard-`APPLICATION_NAME``.

You can view the status of these AWS CloudFormation stacks. If any of them fail, you
can view the cause of the failure.

## Pre- and post-deployment

configuration scripts

###### Can't find the output of my scripts

- **Cause:** Customizations are key scripts that
  you want to run on the EC2 instances and the logs from script deployments are
  not included with the provisioning logs.
- **Solution:** The logs for scripts that run on
  EC2 instances are included in the CloudWatch log group that Launch Wizard creates in your
  account for the workload. The CloudWatch log group can be identified as
  `LaunchWizard-`APPLICATION_NAME`` .
  You can find the following logs in this log group.
  - `lw-customization/`<instance-id>`/preDeploymentConfiguration`
    — For pre-deployment configuration scripts that run on the
    specified EC2 instance.
  - `lw-customization/`<instance-id>`/postDeploymentConfiguration`
    — For post-deployment configuration scripts that run on the
    specified EC2 instance.

## Application launch quotas

Launch Wizard allows for a maximum of 25 active applications for any given application type. Up
to three applications can be `in progress` at a time. If you want to increase
this limit, contact [Support](https://aws.amazon.com/contact-us "https://aws.amazon.com/contact-us").

## Instance level logs

To check the progress of a deployment, you can log in to an instance as soon its
instance state is listed as **running**. When the deployment is
finished, the log files are moved to `/tmp`.

By default, your provisioned Amazon EC2 instances are retained when a deployment fails. If
you created your Launch Wizard deployment with these default settings, you can navigate to the
following paths for further evaluation.

| Directory                          | Purpose                                                                                                                                                                       |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/root/install`                    | The working directory of Launch Wizard SAP deployment.                                                                                                                        |
| `/root/install/scripts`            | The home directory of Launch Wizard SAP deployment. It contains all the<br>scripts called by Launch Wizard.                                                                   |
| `/root/install/scripts/log`        | All the logs related to the deployment (`install.log`<br>file).                                                                                                               |
| `/tmp/`                            | Based on the SAP components that are deployed on an Amazon EC2 instance,<br>Launch Wizard creates a folder in this directory for SAP software application<br>deployment logs. |
| `/var/log/messages`                | The unhandled exceptions of an Amazon EC2 instance.                                                                                                                           |
| `/var/log/zypper.log`              | All the logs for SLES operating system package installation<br>failures.                                                                                                      |
| `/var/log/yum.log`                 | All the logs for RHEL operating system package installation<br>failures.                                                                                                      |
| `/var/log/pacemaker`               | All the logs for pacemaker cluster.                                                                                                                                           |
| `/var/log/pacemaker/pacemaker.log` |
| `/var/log/cluster/corosync.log`    |

## SAP application software deployment

logs

Depending on which SAP components are deployed on an instance, Launch Wizard creates a folder
in `/tmp` to log all of the SAP software application deployment logs. If a
database component is deployed on an instance, the folder name in the file will be
`NW_ABAP_DB`. If an application server is deployed, the folder name will
be `NW_ABAP_APP`. For single node deployments, there will be multiple
folders, such as `NW_ABAP_DB` and `NW_ABAP_CI`, which represent
the different components deployed on the instance.

## Errors

###### Your requested instance type is not supported in your requested Availability

Zone

- **Cause:** This failure might occur during the
  launch of your instance, or during the validation of the instances that Launch Wizard
  launches in your selected subnets.
- **Solution:** For this scenario, you must choose
  a different Availability Zone and retry the deployment from the initial page of
  the Launch Wizard console.

###### Infrastructure template already exists

- **Cause:** This failure occurs when you choose to
  create a new infrastructure configuration and then navigate back to the first
  step in the wizard to review or adjust any settings. Launch Wizard has already registered
  the configuration template, so choosing **Next** results in the
  error "Template name already exists. Select a new template name."
- **Solution:**

Perform one of the following actions to continue with your
deployment.

    + Change the name of the configuration template and continue.
    + Choose another template and continue.
    + Delete the template causing the error by navigating to the
     **Saved Infrastructure Setting** tab under
     **Deployments – SAP**, and then continue with your
     configuration using the same configuration name.

## AWS Systems Manager for SAP

###### An Internal Error Occurred

- **Cause:** For users using AWS Systems Manager for the
  first time, the CloudFormation resource
  (`AWS::SystemsManagerSAP::Application`) can fail with a message
  `An Internal Error Occurred` due to issues during the
  SLR (service-linked role)
  `AWSSSMForSAPServiceLinkedRolePolicy` creation.
- **Solution:**
  1.  Use the [IAM console](https://console.aws.amazon.com/iam/home "https://console.aws.amazon.com/iam/home") to ensure that
      `AWSSSMForSAPServiceLinkedRolePolicy` is in your
      account.
  2.  Retry the Launch Wizard deployment to complete the registration
      successfully.
  3.  If errors persist, contact [Support](../../../awssupport/latest/user/case-management.md#creating-a-support-case "../../../awssupport/latest/user/case-management.md#creating-a-support-case")

For more information, see [Troubleshooting AWS Systems Manager for
SAP](../../../ssm-sap/latest/userguide/troubleshooting.md "../../../ssm-sap/latest/userguide/troubleshooting.md").

## Support

If your deployment is failing after following the troubleshooting steps listed here,
we recommend you to create a support case with the following information.

```

            [Error description]:<Provide a brief description of the error.>

            [Deployment information]: Provide information about the failed deployment.
            Account number: <AWS account number>
            Deployment name: <Enter deployment name>
            Deployment type: <Single-instance/Multi-instance/High availability>
            SAP HANA version: <Enter SAP HANA database version>
            SAP application: <Enter SAP application name>
            OS type: <Enter operating system>
            OS version: <Enter operating system version>
            Amazon EC2 instance family: <Enter Amazon EC2 instance family>
            Amazon EC2 instance type: <Enter Amazon EC2 instance type>
            If used proxy: <Yes/No>
            AMI type: <BYOI/BYOS/Marketplace>
            Instances retained: <Yes/No>
            FailedStackID (optional):

            [Required logs] Provide the following logs. Based on the scenario and state of deployment, some logs may not be available.
            /root/install/scripts/log/
            /tmp/install.log
            /tmp/inputs.json
            /var/log/cloud-init.log
            /var/log/hdblcm.log (If SAP HANA install is selected)
            /tmp/NW directory (If SAP HANA install is selected)

            If you haven't retained your Amazon EC2 instance, provide the logs extracted from CloudWatch logs.

            [Troubleshooting]
            Provide the details of the troubleshooting steps that you carried out and the results from them.

```

For more information, see [Creating a
support case](../../../awssupport/latest/user/case-management.md#creating-a-support-case "../../../awssupport/latest/user/case-management.md#creating-a-support-case").
