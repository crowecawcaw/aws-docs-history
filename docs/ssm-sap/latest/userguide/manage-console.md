

# Manage SAP applications
<a name="manage-console"></a>

From the AWS Console for SAP applications, you can view application details, start and stop applications, and monitor operations.

**Topics**
+ [Application details](#application-details)
+ [Start an application](#start-application)
+ [Stop an application](#stop-application)

## Application details
<a name="application-details"></a>

To view the details of a registered application, open the [AWS Console for SAP applications](https://console.aws.amazon.com/awsforsap/home), choose **Applications**, and then choose the application. The application details page contains the following tabs.

**Example**  
View the topology of your Systems Manager for SAP application, including type and status. The child components are embedded under parent components. Select each component to view its details. Tenant database details can be viewed from components of type HANA.
View the EC2 instances and EBS volumes associated with your Systems Manager for SAP application.
View a summary of AWS Backup recovery points and backup jobs for your Systems Manager for SAP application. To modify backup schedules or manage backups, choose **Go to AWS Backup** to open the AWS Backup console. This tab is only available for SAP HANA applications.
View system and application tags assigned to your Systems Manager for SAP application as key-value pairs. Choose **Manage user tags** to add, modify, or delete tags.
View the results of previous configuration check evaluations by selecting a check, or choose **Run checks** to perform a new evaluation. For more information, see [Run Configuration Checks](configuration-checks-console.md).
View operations performed on your Systems Manager for SAP application. Select an operation ID to view more details and events associated with that operation.
View cost information for your Systems Manager for SAP application. AWS Cost Explorer uses tags to track your application costs. Choose **Activate application tags** to activate the tags associated with your application. Cost Explorer can take up to 24 hours to report costs after activating tags. For more information, see [Using cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html).  
Costs are calculated based on the AWS resources used by your application. Keep this in mind when evaluating single-node setups where SAP HANA and SAP ABAP share the same EC2 instance, or other configurations where applications share resources.

## Start an application
<a name="start-application"></a>

Follow these steps to start a Systems Manager for SAP application.

1. Open the [AWS Console for SAP applications](https://console.aws.amazon.com/awsforsap/home).

1. Choose **Applications**, then choose the application that you want to start.

1. Choose **Actions**, then choose **Start application**.

1. Choose **Start**.

You can monitor the task status using the *operation ID* provided in the flash banner or by choosing the **Operations** tab.

## Stop an application
<a name="stop-application"></a>

Follow these steps to stop a Systems Manager for SAP application.

1. Open the [AWS Console for SAP applications](https://console.aws.amazon.com/awsforsap/home).

1. Choose **Applications**, then choose the application that you want to stop.

1. Choose **Actions**, then choose **Stop application**.

   1. When stopping an SAP HANA application, you can also stop the associated EC2 instance where the SAP HANA application is running.

   1. When stopping an SAP ABAP application, you can also stop the connected SAP HANA application, and/or stop the associated EC2 instance where the SAP ABAP and SAP HANA applications are running.
**Note**  
You can stop the EC2 instance only if you have selected the option to stop the connected SAP HANA application.

1. Choose **Stop**.

You can monitor the task status using the *operation ID* provided in the flash banner or by choosing the **Operations** tab.