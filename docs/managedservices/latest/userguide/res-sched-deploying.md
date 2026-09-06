

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Deploying AMS Resource Scheduler
<a name="res-sched-deploying"></a>

To deploy AMS Resource Scheduler, use the automated change type (CT) : Deployment \| AMS Resource Scheduler \| Solution \| Deploy (ct-0ywnhc8e5k9z5) to raise an RFC that then deploys the solution in your account. Once the RFC is executed, a CloudFormation stack containing AMS Resource Scheduler resources with default configuration, is automatically provisioned into your account. For more on Resource Scheduler change types, see [AMS Resource Scheduler](https://docs.aws.amazon.com/managedservices/latest/ctref/deployment-ams-resource-scheduler-section.html).

**Note**  
To find out if AMS Resource Scheduler is already deployed in your account, check the AWS Lambda console for that account and look for the **AMSResourceScheduler ** function.

After the AMS Resource Scheduler is provisioned in your account, we recommend you review the default configuration and, if required, customize configurations such as tag key, timezone, scheduled services, and so forth, based on your preferences. For details on the recommended customizations, see [Customizing AMS Resource Scheduler](res-sched-customize.md), next.

To make the custom configurations, or just confirm the Resource Scheduler configuration, 