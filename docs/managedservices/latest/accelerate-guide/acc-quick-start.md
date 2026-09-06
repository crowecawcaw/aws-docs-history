

# (Optional) Quick Start template in Accelerate
<a name="acc-quick-start"></a>

The Quick Start template automates the deployment and configuration of AMS Resource Tagger in Accelerate-enabled AWS accounts. This template saves time and effort compared to manual setup. Use this template as-is to define monitoring, patching, and backup basics in one account. Or, use it as a StackSet to apply settings across Organizations Units to standardise settings for multiple accounts.

You can also use it as a starting point to build your own custom AMS Resource Tagger profile and use snippets from the documentation to create more complex definitions for tagging.

## Quick Start template functionality
<a name="quick-start-features"></a>

The Quick Start template completes the following tasks:
+ Creates and deploys a configuration version for AMS Resource Tagger.
+ Applies tags to Amazon EC2 instances that enable AMS management and creation of monitoring resources.
+ (Optional) Applies tags to managed EC2 instances that enable them to be patched on a desired schedule, and creates a Patching Maintenance Window to facilitate the patching.
**Warning**  
 By default, instances are rebooted and stopped instances are started automatically for patch installation.
+ (Optional) Applies tags to managed EC2 instances that enable them to be backed up as defined in the [default AMS Backup Plan](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-backup-select-plan.html#acc-backup-plan-default).
+ (Optional) Applies tags to managed Amazon Relational Database Service (Amazon RDS) resources that enable them to be backed up according to the [Enhanced backup plan](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-backup-select-plan.html#acc-backup-plan-enhanced). A backup plan also enables Point in time recovery (PITR) for Amazon RDS. If Amazon RDS automated backup isn't enabled, then the database restarts close to the time of the next backup window.

![Illustration of the Quick Start template functions.](http://docs.aws.amazon.com/managedservices/latest/accelerate-guide/images/acc-quick-start-template.png)


## Quick Start template overrides and exclusions
<a name="quick-start-overrides-exclusions"></a>

After you use this template to create a Quick Start stack, use the following steps to exclude specific instances from Management/Monitoring, Patching, or Backup:
+ **Management and Monitoring:** To exclude an EC2 instance from being managed and monitored by AMS, add this tag to the instance: `ExcludeFromAMSQuickStartMonitoring=true`.
+ **Patching:** EC2 instances that are members of an Auto Scaling group, Amazon Elastic Container Service, or Amazon Elastic Kubernetes Service cluster are excluded from Patching by this Quick Start template.

  To disable the creation of a Patching Window and patch-related tagging of EC2 instances, set the CloudFormation stack parameter to `EnablePatching=false`.

  To exclude an EC2 instance from being targeted by the Quick Start patching window when `EnablePatching=true`, add this tag to the instance: `ExcludeFromAMSQuickStartPatching=true`.
+ **Backup:** EC2 instances that are members of an Auto Scaling groups, ECS, or EKS cluster are excluded from Backup by this Quick Start template.

  To exclude an EC2 instance from being targeted by the default AMS Backup Plan, when `EnableBackup=true`, add this tag to that instance: `ExcludeFromAMSQuickStartBackup=true`.

**Tip**  
You can tag EC2 instances in bulk. Use [Tag Editor](https://docs.aws.amazon.com/tag-editor/latest/userguide/find-resources-to-tag.html) to bulk-select and tag resources in one step in the AWS Management Console.

## Quick Start template parameters
<a name="quick-start-parameters"></a>

This Quick Start template configures Resource Tagger to add the tag `ams:rt:ams-managed=true` to all EC2 instances in the account, excluding instances that you add the `ExcludeFromAMSQuickStartMonitoring=true` tag to. Use the following parameters to control the optional parts of this stack according to your requirements:






- **EnableBackup**
  - **Value:** 'true' (default) / **Effect:** All AMS-managed EC2 instances (`ams:rt:ams-managed=true`) are tagged with `ams:rt:backup-orchestrator=true` for backup daily at 4AM UTC as per the default [AMS Backup Plan](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-backup-select-plan.html#acc-backup-plan-default).<br />For all RDS instances and clusters, the template applies the `ams:rt:backup-orchestrator-enhanced=true` ["continuous backup"](https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery.html#point-in-time-recovery-rds) with [maximum retention(31 days)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.BackupRetention.html) as per the [Enhanced backup plan](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-backup-select-plan.html#acc-backup-plan-enhanced).<br />If this changes your PITR retention period, the database might be restarted in some cases, for example if there are other pending configuration updates.
  - **Value:** 'false' / **Effect:** No instances are targeted for backup by this quick start template.

- **EnablePatching**
  - **Value:** 'false' (default) / **Effect:** No instances are targeted for patching by this Quick Start template.
  - **Value:**  'true' / **Effect:** All AMS-managed instances (`ams:rt:ams-managed=true`) are tagged with `ams:rt:Patch Group=AMSQuickStartPatchWindow` and a basic [SSM Maintenance Window](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html) resource is created to facilitate patching according to the schedule defined in `CronExpression`.<br />To apply the `ams:rt:Patch Group` tag to the EC2 instance, you must [ turn off access to tags in the instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html#turn-off-access-to-tags-in-IMDS) for that instance.

- **CronExpression**
  - **Value:** -
  - **Effect:** The default value of cron(0 30 19 ? \* SAT\#2 \*) sets the 2nd Saturday of the month at 7:30PM according to the Timezone parameter. Use [cron syntax](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html#eb-cron-expressions).

- **Timezone**
  - **Value:** -
  - **Effect:** Target instances are patched according to CronExpression. Use [IANA format](https://docs.aws.amazon.com/athena/latest/ug/athena-supported-time-zones.html).



## Download the Quick Start template
<a name="quick-start-download"></a>

Download the [AMSQuickStart.zip file](samples/AMSQuickStart.zip).

Or, run the following command in [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html) to deploy the `AMSQuickStart.yaml`:

------
#### [ AWS Command Line Interface ]

```
curl -s "https://docs.aws.amazon.com/en_us/managedservices/latest/accelerate-guide/samples/AMSQuickStart.zip" -o "AMSQuickStart.zip"
unzip -q -o AMSQuickStart.zip
for region in {{region1}} {{region2}} ;
do
aws cloudformation create-stack \
    --region $region \
    --stack-name "AMSQuickStart" \
    --template-body file://AMSQuickStart.yaml \
    --parameters \
        ParameterKey=EnableBackup,ParameterValue="{{true}}" \
        ParameterKey=EnablePatching,ParameterValue="{{false}}" \
        ParameterKey=Timezone,ParameterValue="{{US/Eastern}}" \
        ParameterKey=CronExpression,ParameterValue="{{cron(0 30 19 ? * SAT#2 *)}}" \
;
done
```

------
#### [ AWS Tools for PowerShell ]

```
Invoke-WebRequest -Uri 'https://docs.aws.amazon.com/en_us/managedservices/latest/accelerate-guide/samples/AMSQuickStart.zip' -OutFile 'AMSQuickStart.zip'
Expand-Archive -Path 'AMSQuickStart.zip' -DestinationPath . -Force
@('{{region1}}', '{{region2}}') | `
ForEach-Object { `
New-CFNStack `
    -Region $_ `
    -StackName 'AMSQuickStart' `
    -TemplateBody (Get-Content 'AMSQuickStart.yaml' -Raw) `
    -Parameter @(
        @{ParameterKey = "EnableBackup"; ParameterValue = "{{true}}"},
        @{ParameterKey = "EnablePatching"; ParameterValue = "{{false}}"},
        @{ParameterKey = "Timezone"; ParameterValue = "{{US/Eastern}}"},
        @{ParameterKey = "CronExpression"; ParameterValue = "{{cron(0 30 19 ? * SAT#2 *)}}"}
    )
}
```

------

For a description of each parameter, see the preceding section, [Quick Start template parameters](#quick-start-parameters).