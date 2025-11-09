# Managing App Runner automatic scaling

AWS App Runner automatically scales compute resources, specifically instances, up or down for your App Runner application. Automatic scaling provides adequate
request handling when traffic is heavy, and reduces your cost when traffic slows down.

###### Auto scaling configuration

You can configure a few parameters to adjust auto scaling behavior for your service. App Runner maintains auto scaling settings in a sharable resource
that's called _AutoScalingConfiguration_. You can create and maintain stand-alone auto scaling configurations, before you assign them
to services. After they've been associated to a service, you can continue to maintain the configurations. You can also choose to create a new auto scaling
configuration while you're in the process of creating a new service or configuring an existing one. Once the new auto scaling configuration is created,
you can associate it to the service and continue on with the process of creating or configuring your service.

###### Naming and revisions

An auto scaling configuration has a _name_ and a numeric _revision_. Multiple revisions of a configuration have
the same name and different revision numbers. You can use different configuration names for different auto scaling scenarios, such as _high availability_ or _low cost_. For each name, you can add multiple revisions to fine-tune
the settings for a specific scenario. You can have up to 10 unique auto scaling configuration names and up to 5
revisions for each configuration. If you reach the limit and need to create more, you can delete one and then create another one. App Runner will not allow you
to delete a configuration that's set as the default or in use by an active service. For more information about quotas, see [App Runner resource quotas](architecture.md#architecture.quotas "architecture.md#architecture.quotas").

###### Setting a default configuration

When you create or update an App Runner service, you can provide an auto scaling configuration resource.
Providing an auto scaling configuration is optional. If you don't provide one, App Runner provides a default auto scaling
configuration with recommended values. The auto scaling configuration feature provides you the option to set your own default auto scaling configuration
instead of using the default that App Runner provides. Once you specify another auto scaling configuration as a default, that configuration is automatically
assigned as the default to the new services you create in the future. The new default designation doesn't affect the associations that were previously set
for existing services.

###### Configuring services with auto scaling

You can share a single auto scaling configuration across multiple App Runner services to ensure the services have the same auto scaling behavior. For more
information about configuring auto scaling configurations with the App Runner console or the App Runner API, see the sections that follow in this topic.
For more general information about shareable resources, see [Configuring service settings using sharable resources](manage-configure-resources.md "manage-configure-resources.md").

###### Configurable settings

You can configure the following auto scaling settings:

- _Max concurrency_ – The maximum number of concurrent _requests_ that an instance
  processes. When the number of concurrent requests exceeds this quota, App Runner scales up the service.
- _Max size_ – The maximum number of _instances_ that your service can scale up to. This is
  the highest number of instances that can concurrently handle your service's traffic.
- _Min size_ – The minimum number of _instances_ that App Runner can provision for your service.
  The service always has at least this number of provisioned instances. Some of these instances actively handle traffic. The remainder of them are part of
  the cost-effective compute capacity reserve, which is ready to be quickly activated. You pay for the memory usage of all the provisioned instances. You
  pay for the CPU usage of only the active subset.

###### Note

The vCPU resource count determines the number of instances that App Runner can provide to your service. This is an adjustable quota value for the
_Fargate On-Demand_ vCPU resource count that resides in the AWS Fargate service. To view the vCPU quota settings for your account or
to request a quota increase, use the Service Quotas console in the AWS Management Console. For more information, see [AWS Fargate service quotas](../../../AmazonECS/latest/developerguide/service-quotas.md#service-quotas-fargate "../../../AmazonECS/latest/developerguide/service-quotas.md#service-quotas-fargate") in the
_Amazon Elastic Container Service Developer Guide_.

## Manage auto scaling for a service

Manage auto scaling for your App Runner services using one of the following methods:

App Runner console
When you [create a service](manage-create.md "manage-create.md") using the App Runner console or [update a service
configuration](manage-configure.md "manage-configure.md"), you can specify an auto scaling configuration.

###### Note

When you change the auto scaling configuration or revision that's associated to a service, your service is re-deployed.

The **Auto scaling** configuration page offers several options to configure auto scaling for your service.

- To assign an existing configuration and revision – Choose a value from the **Existing
  configurations** drop-down. The latest revision version will default in the adjacent drop-down. If a different revision exists that
  you would prefer to select, do so from the revision drop-down. The configuration values for the revision version display.
- To create and assign a new auto scaling configuration – Select **Create new ASC** from
  the **Create** menu. This launches the **Add custom auto scaling configuration** page. Enter a
  **Configuration name** and values for the auto scaling parameters. Then select **Add**. App Runner creates the new
  auto scaling configuration resource for you and returns you to **Auto scaling** section with the new configuration selected and
  displayed.
- To create and assign a new revision – First select the configuration name from the **Existing
  configurations** drop-down. Then select **Create ASC revision** from the **Create** menu. This
  launches the **Add custom auto scaling configuration** page. Enter values for the auto scaling parameters. Then select
  **Add**. App Runner creates a new auto scaling configuration revision for you and returns you to **Auto scaling**
  section with the new revision selected and displayed.

![App Runner console configuration page showing auto scaling options](images/console-autoscaling.png)

App Runner API or AWS CLI
When you call the [CreateService](../api/API_CreateService.md "../api/API_CreateService.md") or [UpdateService](../api/API_UpdateService.md "../api/API_UpdateService.md") App Runner API actions, you can use the `AutoScalingConfigurationArn` parameter to specify an auto scaling
configuration resource for your service.

The next section provides guidance to manage your auto scaling configuration resources.

## Manage auto scaling configurations resources

Manage the App Runner auto scaling configurations and revisions for your account using one of the following methods:

App Runner console

### Manage auto scaling configurations

The **Auto scaling configurations** page lists the auto scaling configurations that you have set up in your account. You
can create and manage your auto scaling configurations on this page and then later assign them to one or more App Runner services.

You can do any of the following from this page:

- Create a new auto scaling configuration.
- Create a new revision for an existing auto scaling configuration.
- Delete an auto scaling configuration.
- Set an auto scaling configuration as the default.

![App Runner Auto scaling configurations page](images/asc-top-level.png)

###### To manage auto scaling configurations in your account

1. Open the [App Runner console](https://console.aws.amazon.com/apprunner "https://console.aws.amazon.com/apprunner"), and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Auto scaling configurations**. The console displays a list of auto scaling
   configurations in your account.

You can now do any of the following.

    * **To create a new auto scaling configuration**, follow these steps.


    	1. On the **Auto scaling configurations** page, select **Create**.


    	The **Create auto scaling configuration** page displays.
    	2. Enter values for **Configuration name**, **Concurrency**, **Minimum size**,
    	 and **Maximum size**.
    	3. (Optional) If you'd like to add tags, select **Auto new tag**. Then on the fields that appear enter a
    	 **Name** and a **Value** (optional).
    	4. Select **Create**.
    * **To create a new revision for an existing auto scaling configuration**, follow these steps.


    	1. On the **Auto scaling configurations** page, select the radio button next to the configuration that needs the
    	 new revision. Then select **Create revision** from the **Actions** menu.


    	The **Create revision** page displays.
    	2. On , enter values for **Concurrency**, **Minimum size**, and **Maximum
    	 size**.
    	3. (Optional) If you'd like to add tags, select **Auto new tag**. Then on the fields that appear enter a
    	 **Name** and a **Value** (optional).
    	4. Select **Create**.
    * **To delete an auto scaling configuration**, follow these steps.


    	1. On the **Auto scaling configurations** page, select the radio button next to the configuration that you need to
    	 delete.
    	2. Select **Delete** from the **Actions** menu.
    	3. To proceed with the deletion, select **Delete** on the confirmation dialogue. Otherwise, select
    	 **Cancel**.


    	###### Note

    	App Runner validates that your deletion choice is not set as a default or is currently in use by any active services.
    * **To set an auto scaling configuration as the default**, follow these steps.


    	1. On the **Auto scaling configurations** page, select the radio button next to the configuration that you need to
    	 set as the default.
    	2. Select **Set as default** from the **Actions** menu.
    	3. A dialogue displays informing you that App Runner will use the latest revision as the default configuration for all the new
    	 services you create. Select **Confirm** to proceed. Otherwise select **Cancel**.


    	###### Note



    		+ When you set an auto scaling configuration as default, it automatically gets assigned as the default configuration to the
    		 new services you create in future.
    		+ The new default designation doesn't affect the associations that were previously set for existing services.
    		+ If the designated default auto scaling configuration has revisions, App Runner assigns its latest revision as the
    		 default.

### Manage revisions

The console also has a page for creating and managing your existing auto scaling revisions called **Auto scaling
revisions**. Access this page by selecting the name of a configuration on the **Auto scaling configurations**
page.

You can do any of the following from the **Auto scaling revisions** page:

- Create a new auto scaling revision.
- Set an auto scaling configuration revision as the default.
- Delete a revision.
- Delete the whole auto scaling configuration, including all of the associated revisions.
- View the configuration details for a revision.
- View a list of the services associated to a revision.
- Change the revision for a listed service.

![App Runner Auto scaling configurations page](images/asc-revisions.png)

###### To manage auto scaling revisions in your account

1.  Open the [App Runner console](https://console.aws.amazon.com/apprunner "https://console.aws.amazon.com/apprunner"), and in the **Regions** list, select your AWS Region.
2.  In the navigation pane, choose **Auto scaling configurations**. The console displays a list of auto scaling
    configurations in your account. The prior set of procedures in the [Manage auto scaling configurations](#manage-autoscaling.manage-asc-asc "#manage-autoscaling.manage-asc-asc") section includes a screen image of this page.
3.  Now you can drill down into a specific auto scaling configuration to view and manage all of its revisions. In the **Auto scaling
    configurations** pane, under the **Configuration name** column, choose an auto scaling configurations name.
    Select the actual name, rather than the radio button. This will navigate you to a list of all the revisions for that configuration on the
    **Auto scaling revisions** page.
4.  You can now do any of the following.
    - **To create a new revision for an existing auto scaling configuration**, follow these steps.
      1. On the **Auto scaling revisions** page, select **Create revision**.

      The **Create revision** page displays. 2. Enter values for **Concurrency**, **Minimum size**, and **Maximum
      size**. 3. (Optional) If you'd like to add tags, select **Auto new tag**. Then on the fields that appear enter a
      **Name** and a **Value** (optional). 4. Select **Create**.

    - **To delete the whole auto scaling configuration, including all of the associated revisions**, follow
      these steps.
      1. Select **Delete configuration** on the top right of the page.
      2. To proceed with the deletion, select **Delete** on the confirmation dialogue. Otherwise, select
         **Cancel**.

      ###### Note

      App Runner validates that your deletion choice is not set as a default or is currently in use by any active services.

    - **To set an auto scaling revision as the default**, follow these steps.
      1. Select the radio button next to the revision that you need to set as the default.
      2. Select **Set as default** from the **Actions** menu.

      ###### Note

          + When you set an auto scaling configuration as default, it automatically gets assigned as the default configuration to the
           new services you create in future.
          + The new default designation doesn't affect the associations that were previously set for existing services.

    - **To view the configuration details for a revision**, follow these steps.
      1. Select the radio button next to the revision.

      The configuration details for the revision, including the ARN, displays in the lower split panel. Refer to the screen image
      at the end of this procedure.

    - **To view a list of the services associated to a revision**, follow these steps.
      1. Select the radio button next to the revision.

      The **Services** panel, displays in the lower split panel, beneath the revision configuration details. The
      panel lists all of the services that use this auto scaling configuration revision. Refer to the screen image at the end of this
      procedure.

    - **To change the revision for a listed service**, follow these steps.

          1. Select the radio button next to the revision, if you haven't done so already.


          The **Services** panel, displays in the lower split panel, beneath the revision configuration details. The
           panel lists all of the services that use this auto scaling configuration revision. Refer to the screen image at the end of this
           procedure.
          2. On the **Services** panel, select the radio button next to the service that you want to modify. Then select
           **Change revisions.**
          3. The **Change ASC revision** panel displays. Choose from the available revisions in the drop-down. Only the
           revisions of the auto scaling configuration you chose earlier are available. If you need to change to a different auto scaling
           configuration, follow the procedures under the prior section [Manage auto scaling for a service](#manage-autoscaling.manage "#manage-autoscaling.manage").


          Select **Update** to proceed with the change. Otherwise select **Cancel**.


          ###### Note

          When you change a revision that's associated to a service, your service is re-deployed.

          You must select refresh on this panel to see the updated associations.

          To see the ongoing activity and the status for the service redeployment, use the panel breadcrumbs to navigate to **App Runner**
          **>**
          **Services**, select the service, then view the **Logs** tab from the
           **Service overview** panel.

      ![App Runner Auto scaling revisions page with split panel beneath that displays the services associated the selected revision.](images/asc-revisions-services.png)

App Runner API or AWS CLI
Use the following App Runner API actions to manage your auto scaling configuration resources.

- [CreateAutoScalingConfiguration](../api/API_CreateAutoScalingConfiguration.md "../api/API_CreateAutoScalingConfiguration.md") – Creates a new auto scaling
  configuration or a revision to an existing one.
- [UpdateDefaultAutoScalingConfiguration](../api/API_UpdateDefaultAutoScalingConfiguration.md "../api/API_UpdateDefaultAutoScalingConfiguration.md") –Sets an auto scaling
  configuration to be the default. The existing default auto scaling configuration will be set to non-default automatically.
- [ListAutoScalingConfigurations](../api/API_ListAutoScalingConfigurations.md "../api/API_ListAutoScalingConfigurations.md") – Returns a list of the auto
  scaling configurations that are associated with your AWS account, with summary information.
- [ListServicesForAutoScalingConfiguration](../api/API_ListServicesForAutoScalingConfiguration.md "../api/API_ListServicesForAutoScalingConfiguration.md") – Returns a list
  of the associated App Runner services using an auto scaling configuration.
- [DescribeAutoScalingConfiguration](../api/API_DescribeAutoScalingConfiguration.md "../api/API_DescribeAutoScalingConfiguration.md") – Returns a full
  description of an auto scaling configuration.
- [DeleteAutoScalingConfiguration](../api/API_DeleteAutoScalingConfiguration.md "../api/API_DeleteAutoScalingConfiguration.md") – Deletes an auto scaling
  configuration. You can delete a top level auto scaling configuration, a specific revision of one, or all revisions associated with the top level
  configuration. Use the optional `DeleteAllRevisions` parameter to delete all of the revisions. If you reach the auto scaling
  configuration [resource quota](architecture.md#architecture.quotas "architecture.md#architecture.quotas") for your AWS account, you might need to delete unnecessary auto
  scaling configurations.
