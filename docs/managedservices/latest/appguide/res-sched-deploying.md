# Deploying AMS Resource Scheduler

To deploy AMS Resource Scheduler, use the automated change type (CT) : Deployment | AMS Resource Scheduler | Solution | Deploy (ct-0ywnhc8e5k9z5)
to raise an RFC that then deploys the solution in your account. Once the RFC is executed, a CloudFormation stack containing
AMS Resource Scheduler resources with default configuration, is automatically provisioned into your account. For more on Resource Scheduler change types, see
[AMS Resource Scheduler](../ctref/deployment-ams-resource-scheduler-section.md "../ctref/deployment-ams-resource-scheduler-section.md").

###### Note

To find out if AMS Resource Scheduler is already deployed in your account, check the AWS Lambda console for that account and look
for the **AMSResourceScheduler** function.

After the AMS Resource Scheduler is provisioned in your account, we recommend you review the default configuration and, if required,
customize configurations such as tag key, timezone, scheduled services, and so forth, based on your preferences. For details on the
recommended customizations, see [Customizing AMS Resource Scheduler](res-sched-customize.md "res-sched-customize.md"), next.

To make the custom configurations, or just confirm the Resource Scheduler configuration,
