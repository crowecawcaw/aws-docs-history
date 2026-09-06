

# Runtime coverage and troubleshooting for Amazon EC2 instance
<a name="gdu-assess-coverage-ec2"></a>

For an Amazon EC2 resource, the runtime coverage is evaluated at the instance level. Your Amazon EC2 instances can run multiple types of applications and workloads amongst others in your AWS environment. This feature also supports Amazon ECS managed Amazon EC2 instances and if you have Amazon ECS clusters running on an Amazon EC2 instance, the coverage issues at the instance level will show up under Amazon EC2 runtime coverage. 

**Topics**
+ [Reviewing coverage statistics](#review-coverage-statistics-ec2-runtime-monitoring)
+ [Coverage status change with EventBridge notifications](#ec2-runtime-monitoring-coverage-status-change)
+ [Troubleshooting Amazon EC2 runtime coverage issues](#ec2-runtime-monitoring-coverage-issues-troubleshoot)

## Reviewing coverage statistics
<a name="review-coverage-statistics-ec2-runtime-monitoring"></a>

The coverage statistics for the Amazon EC2 instances associated with your own accounts or your member accounts is the percentage of the healthy EC2 instances over all EC2 instances in the selected AWS Region. The following equation represents this as:

*(Healthy instances/All instances)\*100*

If you have also deployed the GuardDuty security agent for your Amazon ECS clusters, then any instance level coverage issue associated with Amazon ECS clusters running on an Amazon EC2 instance will appear as an Amazon EC2 instance runtime coverage issue. 

Choose one of the access methods to review the coverage statistics for your accounts.

------
#### [ Console ]
+ Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).
+ In the navigation pane, choose **Runtime Monitoring**.
+ Choose the **Runtime coverage** tab.
+ Under the **EC2 instance runtime coverage** tab, you can view the coverage statistics aggregated by the coverage status of each Amazon EC2 instance that is available in the **Instances list** table. 
  + You can filter the **Instance list** table by the following columns:
    + **Account ID**
    + **Agent management type**
    + **Agent version**
    + **Coverage status**
    + **Instance ID**
    + **Cluster ARN**
+ If any of your EC2 instances have the **Coverage status** as **Unhealthy**, the **Issue** column includes additional information about the reason for the **Unhealthy** status.

------
#### [ API/CLI ]
+ Run the [ListCoverage](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListCoverage.html) API with your own valid detector ID, current Region, and service endpoint. You can filter and sort the instance list using this API.
  + You can change the example `filter-criteria` with one of the following options for `CriterionKey`:
    + `ACCOUNT_ID`
    + `RESOURCE_TYPE`
    + `COVERAGE_STATUS`
    + `AGENT_VERSION`
    + `MANAGEMENT_TYPE`
    + `INSTANCE_ID`
    + `CLUSTER_ARN`
  + When the `filter-criteria` includes `RESOURCE_TYPE` as **EC2**, Runtime Monitoring doesn't support the use of **ISSUE** as the `AttributeName`. If you use it, the API response will result in `InvalidInputException`.

    You can change the example `AttributeName` in `sort-criteria` with the following options:
    + `ACCOUNT_ID`
    + `COVERAGE_STATUS`
    + `INSTANCE_ID`
    + `UPDATED_AT`
  + You can change the {{max-results}} (up to 50).
  + To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

  ```
  aws guardduty --region {{us-east-1}} list-coverage --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --sort-criteria '{"AttributeName": "{{EKS_CLUSTER_NAME}}", "OrderBy": "{{DESC}}"}' --filter-criteria '{"FilterCriterion":[{"CriterionKey":"{{ACCOUNT_ID}}", "FilterCondition":{"EqualsValue":"111122223333"}}] }'  --max-results {{5}}
  ```
+ Run the [GetCoverageStatistics](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetCoverageStatistics.html) API to retrieve coverage aggregated statistics based on the `statisticsType`.
  + You can change the example `statisticsType` to one of the following options:
    + `COUNT_BY_COVERAGE_STATUS` – Represents coverage statistics for EKS clusters aggregated by coverage status.
    + `COUNT_BY_RESOURCE_TYPE` – Coverage statistics aggregated based on the type of AWS resource in the list.
    + You can change the example `filter-criteria` in the command. You can use the following options for `CriterionKey`:
      + `ACCOUNT_ID`
      + `RESOURCE_TYPE`
      + `COVERAGE_STATUS`
      + `AGENT_VERSION`
      + `MANAGEMENT_TYPE`
      + `INSTANCE_ID`
      + `CLUSTER_ARN`
  + To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

  ```
  aws guardduty --region {{us-east-1}} get-coverage-statistics --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --statistics-type {{COUNT_BY_COVERAGE_STATUS}} --filter-criteria '{"FilterCriterion":[{"CriterionKey":"{{ACCOUNT_ID}}", "FilterCondition":{"EqualsValue":"123456789012"}}] }'
  ```

------

If the coverage status of your EC2 instance is **Unhealthy**, see [Troubleshooting Amazon EC2 runtime coverage issues](#ec2-runtime-monitoring-coverage-issues-troubleshoot).

## Coverage status change with EventBridge notifications
<a name="ec2-runtime-monitoring-coverage-status-change"></a>

The coverage status of your Amazon EC2 instance might appear as **Unhealthy**. To know when the coverage status changes, we recommend you to monitor the coverage status periodically, and troubleshoot if the status becomes **Unhealthy**. Alternatively, you can create an Amazon EventBridge rule to receive a notification when the coverage status changes from either **Unhealthy** to **Healthy** or otherwise. By default, GuardDuty publishes this in the [EventBridge bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html) for your account.

### Sample notification schema
<a name="ec2-gdu-coverage-status-eventbridge-schema"></a>

In an EventBridge rule, you can use the pre-defined sample events and event patterns to receive coverage status notification. For more information about creating an EventBridge rule, see [Create rule](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html#eb-gs-create-rule) in the *Amazon EventBridge User Guide*. 

Additionally, you can create a custom event pattern by using the following example notification schema. Make sure to replace the values for your account. To get notified when the coverage status of your Amazon EC2 instance changes from `Healthy` to `Unhealthy`, the `detail-type` should be {{GuardDuty Runtime Protection Unhealthy}}. To get notified when the coverage status changes from `Unhealthy` to `Healthy`, replace the value of `detail-type` with {{GuardDuty Runtime Protection Healthy}}.

```
{
  "version": "0",
  "id": "event ID",
  "detail-type": "GuardDuty Runtime Protection Unhealthy",
  "source": "aws.guardduty",
  "account": "AWS account ID",
  "time": "event timestamp (string)",
  "region": "AWS Region",
  "resources": [
       ],
  "detail": {
    "schemaVersion": "1.0",
    "resourceAccountId": "string",
    "currentStatus": "string",
    "previousStatus": "string",
    "resourceDetails": {
        "resourceType": "EC2",
        "ec2InstanceDetails": {
          "instanceId":"",
          "instanceType":"",
          "clusterArn": "",
          "agentDetails": {
            "version":""
          },
          "managementType":""
        }
    },
    "issue": "string",
    "lastUpdatedAt": "timestamp"
  }
}
```

## Troubleshooting Amazon EC2 runtime coverage issues
<a name="ec2-runtime-monitoring-coverage-issues-troubleshoot"></a>

If the coverage status of your Amazon EC2 instance is **Unhealthy**, you can view the reason under the **Issue** column.

If your EC2 instance is associated with an EKS cluster and the security agent for EKS was installed either manually or through automated agent configuration, then to troubleshoot the coverage issue, see [Runtime coverage and troubleshooting for Amazon EKS clusters](eks-runtime-monitoring-coverage.md).

The following table lists the issue types and the corresponding troubleshooting steps.



- ** No Agent Reporting **
  - **Issue message:** Waiting for SSM notification / **Troubleshooting steps:** Receiving the SSM notification may take a few minutes. <br />Make sure that the Amazon EC2 instance is SSM managed. For more information, see the steps under *Method 1 - By using AWS Systems Manager* in [Installing the security agent manually](installing-gdu-security-agent-ec2-manually.md). 
  - **Issue message:** (Empty on purpose) / **Troubleshooting steps:** If you are managing the GuardDuty security agent manually, make sure that you followed the steps under [Managing security agent manually for Amazon EC2 resource](managing-gdu-agent-ec2-manually.md).
  - **Troubleshooting steps:** If you've enabled automated agent configuration:+  Your EC2 instance is SSM managed. <br />+  View the status of your security agent periodically. For more information, see [Validating GuardDuty security agent installation status](installing-gdu-security-agent-ec2-manually.md#validate-ec2-gdu-agent-installation-healthy). 
  - **Troubleshooting steps:** Validate that the VPC endpoint for your Amazon EC2 instance is correctly configured. For more information, see [Validating VPC endpoint configuration](validate-vpc-endpoint-config-runtime-monitoring.md).
  - **Troubleshooting steps:** If your organization has a service control policy (SCP), validate that permissions boundary is not restricting the `guardduty:SendSecurityTelemetry` permission. For more information, see [Validating your organization service control policy in a multi-account environment](prereq-runtime-monitoring-ec2-support.md#validate-organization-scp-ec2).
  - **Issue message:** Agent disconnected / **Troubleshooting steps:**  +  View the status of your security agent. For more information, see [Validating GuardDuty security agent installation status](installing-gdu-security-agent-ec2-manually.md#validate-ec2-gdu-agent-installation-healthy). <br />+  View the security agent logs to identify the potential root cause. The logs provide detailed errors that you can use to troubleshoot the issue yourself. The log files are available under `/var/log/amzn-guardduty-agent/`. <br />Do `sudo journalctl -u amazon-guardduty-agent`.  

- ** Agent Not Provisioned **
  - **Issue message:** Instances with exclusion tags are excluded from Runtime Monitoring. / **Troubleshooting steps:** GuardDuty doesn't receive runtime events from Amazon EC2 instances that are launched with the exclusion tag `GuardDutyManaged`:`false`.<br />To receive runtime events from this Amazon EC2 instance, remove the exclusion tag.
  - **Issue message:** Kernel version is lower than the supported version. / **Troubleshooting steps:** For information about supported kernel versions across OS distributions, see [Validate architectural requirements](prereq-runtime-monitoring-ec2-support.md#validating-architecture-req-ec2) for Amazon EC2 instances.
  - **Issue message:** Kernel version is higher than the supported version. / **Troubleshooting steps:** For information about supported kernel versions across OS distributions, see [Validate architectural requirements](prereq-runtime-monitoring-ec2-support.md#validating-architecture-req-ec2) for Amazon EC2 instances.
  - **Issue message:** Unable to retrieve instance identity document. / **Troubleshooting steps:** Follow these steps:1.  Confirm that your resource is an Amazon EC2 instance, and not a hybrid non-EC2 instance. <br />2.  Confirm that the Instance Metadata Service (IMDS) is enabled. To do this, see [Configure Instance Metadata Service options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html) in the *Amazon EC2 User Guide*. <br />3.  Verify that the instance identity document exists. To do this, see [Retrieve the instance identity document](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/retrieve-iid.html) in the *Amazon EC2 User Guide*. <br />4.  If the instance identity document still doesn't exists, then restart the instance. The instance identity document is generated when the instance is stopped and started, restarted, or launched.  

- ** SSM Association Creation Failed **
  - **Issue message:** GuardDuty SSM association already exists in your account / **Troubleshooting steps:**  1.  Delete the existing association manually. For more information, see [Deleting associations](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state-manager-delete-association.html) in the *AWS Systems Manager User Guide*. <br />2.  After you delete the association, disable and then re-enable the GuardDuty automated agent configuration for Amazon EC2.  
  - **Issue message:** Your account has too many SSM associations / **Troubleshooting steps:** Choose **one** of the following two options:+  Delete any unused SSM associations. For more information, see [Deleting associations](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state-manager-delete-association.html) in the *AWS Systems Manager User Guide*. <br />+  Check if your account is eligible for a quota increase. For more information, see [Systems Manager Service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *AWS General Reference*. 

- ** SSM Association Updation Failed **
  - **Issue message:** GuardDuty SSM association does not exist in your account
  - **Troubleshooting steps:** GuardDuty SSM association is not present in your account. Disable and then re-enable Runtime Monitoring.

- ** SSM Association Deletion Failed **
  - **Issue message:** GuardDuty SSM association does not exist in your account
  - **Troubleshooting steps:** The SSM association is not present in your account. If the SSM association was deleted intentionally, then no action is needed.

- ** SSM Instance Association Execution Failed **
  - **Issue message:** Architectural requirements or other prerequisites are not met.
  - **Troubleshooting steps:** For information about verified operating system distributions, see [Prerequisites for Amazon EC2 instance support](prereq-runtime-monitoring-ec2-support.md).<br />If you still experience this issue, the following steps will help you identify and potentially resolve the issue:1.  Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/). <br />2.  In the navigation pane, under **Node management**, select **State Manager**. <br />3.  Filter by **Document Name** property and enter **AmazonGuardDuty-ConfigureRuntimeMonitoringSsmPlugin**. <br />4.  Select the corresponding association ID and view its **Execution history**. <br />5.  Using the execution history, view the failures, identify the potential root cause, and try to resolve it. 

- ** VPC Endpoint Creation Failed **
  - **Issue message:** VPC endpoint creation not supported for shared VPC {{vpcId}} / **Troubleshooting steps:** Runtime Monitoring supports the use of a shared VPC within an organization. For more information, see [Using shared VPC with Runtime Monitoring](runtime-monitoring-shared-vpc.md).
  - **Issue message:** **Only when using shared VPC with automated agent configuration**<br />Owner account ID {{111122223333}} for shared VPC {{vpcId}} doesn't have either Runtime Monitoring, automated agent configuration, or both, enabled / **Troubleshooting steps:** The shared VPC owner account must enable Runtime Monitoring and automated agent configuration for at least one resource type (Amazon EKS or Amazon ECS (AWS Fargate)). For more information, see [Prerequisites specific to GuardDuty Runtime Monitoring](runtime-monitoring-shared-vpc.md#shared-vpc-runtime-monitoring-prereq-gd-setup).
  - **Issue message:** Enabling private DNS requires both `enableDnsSupport` and `enableDnsHostnames` VPC attributes set to `true` for {{vpcId}} (Service: Ec2, Status Code:400, Request ID: {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}). / **Troubleshooting steps:** Ensure that the following VPC attributes are set to `true` – `enableDnsSupport` and `enableDnsHostnames`. For more information, see [DNS attributes in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support).<br />If you're using Amazon VPC Console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/) to create the Amazon VPC, then select both **Enable DNS hostnames** and **Enable DNS resolution**. For more information, see [VPC configuration options](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html#create-vpc-options).<br />After updating the VPC attributes, you must accelerate a retry of the VPC endpoint creation by making one of these changes:+  You can add or modify the `GuardDutyManaged` tag for your Amazon EC2 instance (recommended). For example, you can add `GuardDutyManaged`:`true` to include the instance for Runtime Monitoring. <br />+  You can change the Amazon EC2 instance state (stop or restart). 

- **Shared VPC Endpoint Deletion Failed**
  - **Issue message:** Shared VPC endpoint deletion not allowed for account ID {{111122223333}}, shared VPC {{vpcId}}, owner account ID {{555555555555}}.
  - **Troubleshooting steps:** +  Disabling the Runtime Monitoring status of the shared VPC participant account doesn't impact the shared VPC endpoint policy and the security group that exists in the owner account.  <br />To delete the shared VPC endpoint and security group, you must disable Runtime Monitoring or automated agent configuration status in the shared VPC owner account. <br />+  The shared VPC participant account can't delete the shared VPC endpoint and security group hosted in the shared VPC owner account. 

- ** Agent not reporting **
  - **Issue message:** (Empty on purpose)
  - **Troubleshooting steps:** The issue type has reached end of support. If you continue experiencing this issue and not already done so, enable GuardDuty automated agent for Amazon EC2.<br />If the issue still persists, consider disabling Runtime Monitoring for a few minutes and then enable it again.

