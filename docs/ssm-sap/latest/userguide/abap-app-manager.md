# Register SAP ABAP application with AWS Systems Manager for SAP

###### Important

You must register the SAP HANA database you want to connect to the SAP ABAP application before registering the SAP ABAP application.

Follow along these steps to register either a single node or a multi node (distributed or high availability) SAP ABAP as a Systems Manager for SAP application.

1. Go to https://console.aws.amazon.com/systems-manager/ > **Application Tools** > **Application Manager**.
2. Select **Create Application** > **Enterprise Workload**.
3. For Application type, select **SAP ABAP**.
4. In **Application details**, enter a name for the application you want to register with Application Manager.
5. Provide the following details of your workload.
   1. **Instance ID** – This is the Amazon EC2 instance ID where your workload is currently running. Choose **Browse instances**, and select the instance ID for your primary SAP ABAP workload.
   2. **SAP System Identifier (SID)** – This is the SAP System Identifier (`sapsid`) of your SAP ABAP instance.
   3. **SAP HANA database Amazon Resource Name (ARN)** – This is the Amazon Resource Name (ARN) of the SAP HANA database you want to connect to your SAP ABAP application.
      - Select **Browse databases** to choose the database.
      - Select **Register a new application** to register an SAP HANA database to connect to the SAP ABAP application. You can refresh the database list on successful completion of the SAP HANA application.

6. (_Optional_). In **Connected Web Dispatcher components** you can provide the following details of up to 5 of your SAP Web Dispatcher resources that your application is using. SAP Web Dispatcher resources are only discoverable by Systems Manager for SAP after you input these details:
   1. **SAP System Identifier (SID)** is the SAP System Identifier (`sapsid`) of your SAP Web Dispatcher resource.
   2. **Instance ID** is the Amazon EC2 instance ID on which your SAP Web Dispatcher is currently running. Select **Browse instances** to find the instance ID.

7. (_Optional_). In **Application tags**, you can add 100 tags associated to resources.
8. Select **Create**.

**Application tabs**

On registration completion, you can see your application in the list of applications. You can see the following tabs for each application.

Overview
For more information, see [Viewing overview information about an application](../../../systems-manager/latest/userguide/application-manager-working-viewing-overview.md "../../../systems-manager/latest/userguide/application-manager-working-viewing-overview.md").

Resources
You can find the **Topology** of a Systems Manager for SAP application in the **Resources** tab. It provides the details of your application components. The child components are embedded under parent components. Select each component to view its details.

For more information, see [Viewing application resources](../../../systems-manager/latest/userguide/application-manager-working-viewing-resources.md "../../../systems-manager/latest/userguide/application-manager-working-viewing-resources.md").

Instances
For more information, see [Working with your application instances](../../../systems-manager/latest/userguide/application-manager-working-instances.md "../../../systems-manager/latest/userguide/application-manager-working-instances.md").

Compliance
For more information, see [Viewing compliance information](../../../systems-manager/latest/userguide/application-manager-working-viewing-resource-compliance.md "../../../systems-manager/latest/userguide/application-manager-working-viewing-resource-compliance.md").

Monitoring

###### Note

You must on-board your Systems Manager for SAP application with Amazon CloudWatch Application Insights to view monitoring details in this tab.

Use the following steps to on-board your registered SAP HANA application with Application Insights.

1. Open https://console.aws.amazon.com/systems-manager/.
2. Go to **Application Manager**.
3. From the list of applications, find and select your SAP application. This opens your application details window.
4. Go to the **Monitoring** tab > **Application Insights** > **Add an application**.
5. You are now redirected to Amazon CloudWatch Application Insights console.
6. Follow the instructions described in [Set up your SAP HANA database for monitoring](../../../AmazonCloudWatch/latest/monitoring/appinsights-tutorial-sap-hana.md#appinsights-tutorial-sap-hana-set-up "../../../AmazonCloudWatch/latest/monitoring/appinsights-tutorial-sap-hana.md#appinsights-tutorial-sap-hana-set-up").

Under **Select an application or resource group**, make sure to select the SAP HANA application registered with Systems Manager for SAP.

###### Note

You can create only one CloudWatch Application Insights application on a single-node SAP ABAP application. You can onboard either the SAP ABAP application or the connected SAP HANA application. 7. Once you have completed onboarding your registered SAP HANA application with Amazon CloudWatch Application Insights, you can view monitoring details in the **Monitoring** tab.

For more information, see [Viewing monitoring information](../../../systems-manager/latest/userguide/application-manager-working-viewing-monitors.md "../../../systems-manager/latest/userguide/application-manager-working-viewing-monitors.md").

OpsItems
For more information, see [Viewing OpsItems for an application](../../../systems-manager/latest/userguide/application-manager-working-viewing-OpsItems.md "../../../systems-manager/latest/userguide/application-manager-working-viewing-OpsItems.md").

Logs
For more information, see [Viewing log groups and log data](../../../systems-manager/latest/userguide/application-manager-viewing-logs.md "../../../systems-manager/latest/userguide/application-manager-viewing-logs.md").

Runbooks
For more information, see [Working with runbooks in Application Manager](../../../systems-manager/latest/userguide/application-manager-working-runbooks.md "../../../systems-manager/latest/userguide/application-manager-working-runbooks.md").

Cost
You must enable AWS Cost Explorer Service to view details in the Cost tab. For more information, see [Enabling Cost Explorer](../../../cost-management/latest/userguide/ce-enable.md "../../../cost-management/latest/userguide/ce-enable.md").

The cost of the single-node SAP ABAP application is an aggregate of the cost of SAP ABAP and SAP HANA applications on the same EC2 instance.
