# Set up, configure, and manage your application for monitoring from the CloudWatch console

This section provides steps to set up, configure, and manage your application
for monitoring from the CloudWatch console.

###### Console procedures

- [Add and configure an application](#appinsights-add-configure "#appinsights-add-configure")
- [Enable Application Insights for Amazon ECS and Amazon EKS resource monitoring](#appinsights-container-insights "#appinsights-container-insights")
- [Disable monitoring for an application component](#appinsights-disable-monitoring "#appinsights-disable-monitoring")
- [Delete an application](#appinsights-delete-app "#appinsights-delete-app")

## Add and configure an application

###### Add and configure an application from the CloudWatch console

To get started with CloudWatch Application Insights from the CloudWatch console, perform the following
steps.

1. **Start.** Open the [CloudWatch console
   landing page](http://console.aws.amazon.com/cloudwatch "http://console.aws.amazon.com/cloudwatch"). From the left navigation pane, under
   **Insights**, choose **Application
   Insights**. The page that opens shows the list of
   applications that are monitored with CloudWatch Application Insights, along with their
   monitoring status.
2. **Add an application.** To set up
   monitoring for your application, choose **Add an
   application**. When you choose **Add an
   application**, you are prompted to **Choose
   Application Type**.
   - **Resource group-based
     application**. When you select this option, you
     can choose which resource groups in this account to monitor. To use multiple applications on a component,
     you must use resource group-based monitoring.
   - **Account-based
     application**. When you select this option, you can
     monitor all of the resources in this account. If you want to
     monitor all of the resources in an account, we recommend
     this option over the resource group-based option because the
     application onboarding process is faster.

###### Note

You can't combine resource group-based monitoring with
account-based monitoring using Application Insights. In order to change
the application type, you must delete all of the applications
that are being monitored, and **Choose Application
Type**.

When you add your first application for monitoring, CloudWatch Application Insights creates a
service-linked role in your account, which gives Application Insights
permissions to call other AWS services on your behalf. For more
information about the service-linked role created in your account by
Application Insights, see [Using service-linked roles for CloudWatch Application Insights](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md"). 3. Resource-based application monitoring

    1. **Select an application or
     resource group.** On the
     **Specify application details**
     page, select the AWS resource group that contains
     your application resources from the dropdown list.
     These resources include front-end servers, load
     balancers, auto scaling groups, and database
     servers.


    If you have not created a resource group for
     your application, you can create one by choosing
     **Create new resource group**.
     For more information about creating resource
     groups, see the [*AWS Resource Groups User
     Guide*](../../../ARG/latest/userguide/welcome.md "../../../ARG/latest/userguide/welcome.md").
    2. **Notifications for problem insights.** To view and get notified when problems are detected for selected applications, choose Amazon SNS notifications or Systems Manager OpsCenter Opsitems.




    	1. **Set up Amazon SNS notification (Recommended).** Choose **Select existing topic** or **Create new topic**.
    	2. **Integrate with AWS
    	 Systems Manager OpsCenter.** Under **Advanced Settings**,
    	 select the **Generate Systems Manager OpsCenter OpsItems for remedial actions** check box. To track the operations that are taken to
    	 resolve operational work items (OpsItems) that are related to your AWS resources, provide the Amazon SNS topic ARN.
    3. **Monitor CloudWatch
     Events**. Select the check box to
     integrate Application Insights monitoring with CloudWatch Events
     to get insights from Amazon EBS, Amazon EC2,
     AWS CodeDeploy, Amazon ECS,
     AWS Health APIs And Notifications, Amazon RDS, Amazon S3, and
     AWS Step Functions.
    4. **Tags —
     optional**. CloudWatch Application Insights supports both tag-based
     and CloudFormation-based resource groups (with the
     exception of Auto Scaling groups). For more
     information, see [Working with Tag Editor](../../../ARG/latest/userguide/tag-editor.md "../../../ARG/latest/userguide/tag-editor.md").
    5. Choose **Next**.


    An [ARN](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") is generated for the application in
     the following format.



    ```
    arn:`partition`:applicationinsights:`region`:`account-id`:application/resource-group/`resource-group-name`
    ```

    Example



    ```
    arn:aws:applicationinsights:us-east-1:123456789012:application/resource-group/my-resource-group
    ```
    6. On the **Review detected components** page, under **Review components for monitoring**, the table lists the detected components
     and their associated detected workloads.


    ###### Note

    For components that support multiple
     customized workloads, you can monitor up to five
     workloads for each component. These workloads will
     be monitored separately from the component.



    ![The detected components section of the CloudWatch Application Insights console: overview of detected components and associated workloads.](images/appinsights-multiapp-review-component.png)

    Under **Associated
     workloads**, there are several possible
     messages that appear if a workload is not
     listed.




    	* **Couldn't detect
    	 workloads** – An issue occurred
    	 when trying to detect workloads. Make sure that
    	 you have completed the [Prerequisites to configure an application for monitoring](appinsights-prereqs.md "appinsights-prereqs.md"). If you need to add
    	 workloads, choose **Edit
    	 component**.
    	* **No workloads detected** – We didn't detect any workloads. You may need to add workloads. To do so, choose **Edit component**.
    	* **Not applicable** – The component doesn't support customized workloads and will be monitored with default metrics, alarms, and logs.
    	 You can't add workloads to these components.
    7. To edit a component, select a component, and then choose **Edit component**. A
     side panel opens with workloads detected on the component. In this panel, you can edit the component details and add new workloads.



    ![The review detected components section of the CloudWatch Application Insights console: associated workloads can be edited.](images/appinsights-multiapp-edit-component.png)



    	* To edit the workload type or name, use the dropdown list.



    	![The Edit component section of the CloudWatch Application Insights console: dropdown list of workload type.](images/appinsights-multiapp-edit-name-type.png)
    	* To add a workload to the component, choose **Add new workload**.



    	![The edit component section of the CloudWatch Application Insights console: lower left button to add a new workload.](images/appinsights-multiapp-add-workload.png)



    		+ If **Add new workload** doesn't appear, this component doesn't support multiple workloads.
    		+ If the **Associated workloads** heading doesn't appear, this component doesn't support customized workloads.
    	* To remove a workload, choose
    	 **Remove** next to the workload
    	 that you want to remove from monitoring.



    	![The edit component section of the CloudWatch Application Insights console: remove a workload.](images/appinsights-multiapp-remove-workload.png)
    	* To disable monitoring for the entire component, clear the **Monitoring** check box.



    	![The edit component section of the CloudWatch Application Insights check box to disable monitoring.](images/appinsights-multiapp-disable-monitoring.png)
    	* When you are done editing the component, choose **Save changes** in the lower right corner. Any changes to workloads for a component are visible on the
    	 **Review components for monitoring** table under **Associated workloads**.
    8. On the **Review detected components** page, choose **Next**.
    9. The **Specify component details** page includes all components with customizable associated workloads from the previous step.


    ###### Note

    If a component header has an
     *optional* tag, additional
     details for the workloads in that component are
     optional.


    If a component doesn't appear on this page, the component doesn't have any additional details that can be specified in this step.
    10. Choose **Next**.
    11. On the **Review and submit** page, review all monitored component and workload details.
    12. Choose **Submit**.

Account-based application monitoring

    1. **Application
     name**. Enter a name for your
     account-based application.
    2. **Automated monitoring of
     new resources**. By default, Application Insights
     uses recommended settings to configure monitoring
     for resource components that are added to your
     account after you onboard the application. You can
     exclude monitoring for resources added after
     onboarding your application by clearing the check
     box.
    3. **Monitor CloudWatch
     Events**. Select the check box to
     integrate Application Insights monitoring with CloudWatch Events
     to get insights from Amazon EBS, Amazon EC2,
     AWS CodeDeploy, Amazon ECS,
     AWS Health APIs And Notifications, Amazon RDS, Amazon S3, and
     AWS Step Functions.
    4. **Integrate with AWS
     Systems Manager OpsCenter.** To view and
     get notified when problems are detected for
     selected applications, select the
     **Generate Systems Manager OpsCenter
     OpsItems for remedial actions** check
     box. To track the operations that are taken to
     resolve operational work items (OpsItems) that are
     related to your AWS resources, provide the SNS
     topic ARN.
    5. **Tags —
     optional**. CloudWatch Application Insights supports both tag-based
     and CloudFormation-based resource groups (with the
     exception of Auto Scaling groups). For more
     information, see [Working with Tag Editor](../../../ARG/latest/userguide/tag-editor.md "../../../ARG/latest/userguide/tag-editor.md").
    6. **Discovered
     resources**. All of the resources
     discovered in your account are added to this list.
     If Application Insights is unable to discover all of the
     resources in your account, an error message
     appears at the top of the page. This message
     includes a link to the [documentation for how to add the required
     permissions](appinsights-account-based-onboarding-permissions.md "appinsights-account-based-onboarding-permissions.md").
    7. Choose **Next**.


    An [ARN](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") is generated for the application in
     the following format.



    ```
    arn:`partition`:applicationinsights:`region`:`account-id`:application/TBD/`application-name`
    ```

    Example



    ```
    arn:aws:applicationinsights:us-east-1:123456789012:application/TBD/my-application
    ```

4. After you submit your application monitoring configuration, you
   will be taken to the details page for the application, where you can
   view the **Application summary**, the list of
   **Monitored components** and
   **Unmonitored components**, and, by selecting
   the tabs next to **Components**, the
   **Configuration history**, **Log
   patterns**, and any **Tags** that you
   have applied.

To view insights for the application, choose **View
Insights**.

You can update your selections for CloudWatch Events monitoring and
integration with AWS Systems Manager OpsCenter by choosing
**Edit**.

Under **Components**, you can select the
**Actions** menu to Create, Modify, or Ungroup
an instance group.

You can manage monitoring for components, including application
tier, log groups, event logs, metrics, and custom alarms, by
selecting the bullet next to a component and choosing
**Manage monitoring**.

## Enable Application Insights for Amazon ECS and Amazon EKS resource monitoring

You can enable Application Insights to monitor containerized applications and
microservices from the Container Insights console. Application Insights supports
monitoring for the following resources:

- Amazon ECS clusters
- Amazon ECS services
- Amazon ECS tasks
- Amazon EKS clusters

When Application Insights is enabled, it provides recommended metrics and logs,
detects potential problems, generates CloudWatch Events, and creates automatic
dashboards for your containerized applications and microservices.

You can enable Application Insights for containerized resources from the Container
Insights or Application Insights consoles.

###### Enable Application Insights from the Container Insights console

From the Container Insights console, on the Container Insights
**Performance monitoring** dashboard, choose
**Auto-configure Application Insights**. When Application Insights is
enabled, it displays details about detected problems.

###### Enable Application Insights from the Application Insights console

When ECS clusters appear in the component list, Application Insights
automatically enables additional container monitoring with Container
Insights.

For EKS clusters, you can enable additional monitoring with Container
Insights to provide diagnostics information, such as container restart
failures, to help you isolate and resolve problems. Additional steps are
required to set up Container Insights for EKS. For information, see [Setting up Container Insights on Amazon EKS and Kubernetes](deploy-container-insights-EKS.md "deploy-container-insights-EKS.md") for steps to set up
Container Insights on EKS.

Additional monitoring for EKS with Container Insights is supported on
Linux instances with EKS.

For more information about Container Insights support for ECS and EKS
clusters, see [Container Insights](ContainerInsights.md "ContainerInsights.md").

## Disable monitoring for an application component

To disable monitoring for an application component, from the application
details page, select the component for which you want to disable monitoring.
Choose **Actions**, and then **Remove from
monitoring**.

## Delete an application

To delete an application, from the CloudWatch dashboard, on the left navigation
pane, choose **Application Insights** under
**Insights**. Select the application that you want to
delete. Under **Actions**, choose **Delete
application**. This deletes monitoring and deletes all of the
saved monitors for application components. The application resources are not
deleted.
