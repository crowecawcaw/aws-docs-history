# Editing AWS Resilience Hub application resources

To receive accurate and helpful resiliency assessments, ensure that your application
description is updated and matches your actual AWS application and resources. Assessment
reports, validation, and recommendations are based on the listed resources. If you add or
remove resources from an AWS application, you should reflect those changes in
AWS Resilience Hub.

AWS Resilience Hub provides transparency about your application sources. You can identify and edit
the resources and the application sources in your application.

###### Note

Editing the resources modifies only the AWS Resilience Hub reference of your application. No
changes are made to your actual resources.

You can add resources that are missing, modify existing resources, or remove resources
that you don’t need. Resources are grouped into logical Application Components
(AppComponents). You can edit the AppComponents to better reflect the structure of your
application.

Add to or update your application resources by editing a draft version of your application
and publishing the changes to a new (release) version. AWS Resilience Hub uses the release version
(which includes the updated resources) of your application for running resiliency
assessments.

###### To assess the resiliency of your application

1. In the navigation pane, choose **Applications**.
2. On the **Applications** page, choose the application name that
   you want to edit.
3. From **Actions** menu, choose **Assess
   resiliency**.
4. In the **Run resiliency assessment** dialog, enter a unique name
   for the report or use the generated name in the **Report name**
   box.
5. Choose **Run**.
6. After you are notified that the assessment report has been generated, choose the
   **Assessments** tab and your assessment to view the
   report.
7. Choose the **Review** tab to view your application's assessment
   report.

###### To enable scheduled assessment

1. In the navigation pane, choose **Applications**.
2. On the **Applications** page, select the application for which
   you want to enable scheduled assessment.
3. Turn on **Automatically assess daily**.

###### To disable scheduled assessment

1. In the navigation pane, choose **Applications**.
2. On the **Applications** page, select the application for which
   you want to enable scheduled assessment.
3. Turn off **Automatically assess daily**.

###### Note

Disabling scheduled assessment will disable drift notification. 4. Choose **Turn off**.

###### To enable drift notification for your application

1. In the navigation pane, choose **Applications**.
2. On the **Applications** page, select the application for which
   you want to enable drift notification or edit the drift notification
   settings.
3. You can edit drift notification by choosing one of the following options:
   - From **Actions**, choose **Enable drift
     notification**.
   - Choose **Enable notification** in **Application
     drifts** section.

4. Complete the steps in [Setup scheduled assessments and drift
   notification](scheduled-assessment.md "scheduled-assessment.md"), and then return to this
   procedure.
5. Choose **Enable**.

Enabling drift notification will also enable scheduled assessment.

###### To edit drift notification for your application

###### Note

This procedure is applicable if you have enabled scheduled assessment
(**Automatically assess daily** is turned on) and drift
notification.

1. In the navigation pane, choose **Applications**.
2. On the **Applications** page, select the application for which
   you want to enable drift notification or edit the drift notification
   settings.
3. You can edit drift notification by choosing one of the following options:
   - From **Actions**, choose **Edit drift
     notification**.
   - Choose **Edit notification** in **Application
     drifts** section.

4. Complete the steps in [Setup scheduled assessments and drift
   notification](scheduled-assessment.md "scheduled-assessment.md"), and then return to this
   procedure.
5. Choose **Save**.

###### To update the security permissions of your application

1. In the navigation pane, choose **Applications**.
2. On the **Applications** page, select the application for which
   you want to update the security permissions.
3. From **Actions**, choose **Update
   permissions**.
4. To update the security permissions, complete the steps in [Setup permissions](setup-permissions.md "setup-permissions.md"), and then return
   to this procedure.
5. Choose **Save and update**.

###### To attach a resiliency policy to your application

1. In the navigation pane, choose **Applications**.
2. On the **Applications** page, choose the application name that
   you want to edit.
3. From **Actions** menu, choose **Attach resiliency
   policy**.
4. In the **Attach policy** dialog, select a resiliency policy from
   **Select a resiliency policy** dropdown list.
5. Choose **Attach**.

###### To edit input sources, resources, and AppComponents of your application

1. In the navigation pane, choose **Applications**.
2. On the **Applications** page, choose the application name that
   you want to edit.
3. Choose the **Application structure** tab.
4. Choose the plus sign **+** before **Version**,
   and then select the application version with **Draft**
   status.
5. To edit input sources, resources, and AppComponents of your application, complete
   the steps in the following procedures.

###### To edit the input sources of your application

1. To edit the input sources of your application, choose the **Input
   sources** tab.

The **Input sources** section lists all the input sources of your
application resources. You can identify the input sources by the following:

    * **Source name** – The name of the input source.
     Choose a source name to view its details in the respective application. For
     manually added input sources, the link will not be available. For example,
     if you choose the source name that is imported from an AWS CloudFormation stack, you
     will be redirected to the stack details page on the AWS CloudFormation
     console.
    * **Source ARN** – The Amazon Resource Name (ARN) of
     the input source. Choose an ARN to view its details in the respective
     application. For manually added input sources, the link will not be
     available. For example, if you choose an ARN that is imported from an
     AWS CloudFormation stack, you will be redirected to the stack details page on the
     AWS CloudFormation console.
    * **Source Type** – The type of input source. Input
     sources include Amazon EKS clusters, AWS CloudFormation stacks, myApplications
     applications, AWS Resource Groups, Terraform state files, and manually added
     resources.
    * **Associated resources** – The number of resources
     that are associated with the input source. Choose a number to view all the
     associated resources of an input source in the
     **Resources** tab.

2. To add input sources to your application, from the **Input
   sources** section, choose **Add input sources**. For
   more information about adding input sources, see [Add resource collections](discover-structure.md "discover-structure.md").
3. To edit input sources, select the input sources and choose one the following
   options from **Actions**:
   - **Reimport input sources (up to 5)** – Reimports
     up to five selected input sources.
   - **Delete input sources** – Deletes the selected
     input sources.

   To publish an application, it must contain a minimum of one input source.
   If you delete all the input sources, **Publish new
   version** will be disabled.

###### To edit the resources of your application

1. To edit the resources of your application, choose the
   **Resources** tab.

###### Note

To see the list of unassessed resources, choose **View unassessed
resources**.

The **Resources** section lists resources from the application
that you chose to use as a template for your application description. To enhance
your search experience, AWS Resilience Hub has grouped resources based on multiple search
criteria. These search criteria include AppComponent types,
**Unsupported** resources, and **Excluded**
resources. To filter the resources based on a search criteria in the
**Resources** table, choose the number below each of the search
criteria.

You can identify the resources by the following:

    * **Logical ID** – A logical ID is a name used to
     identify resources in your AWS CloudFormation stack, Terraform state file, manually
     added application, myApplications application, or AWS Resource Groups.


    ###### Note



    	+ Terraform lets you use the same name for different resource
    	 types. Therefore, you see "*- resource
    	 type*" at the end of the logical ID for resources
    	 that share the same name.
    	+ To view the instances of all the application resources, choose
    	 the plus (**+**) sign before the
    	 **Logical ID**. To view all the instances
    	 of an application resource, choose the plus
    	 (**+**) sign before the Logical ID of each
    	 resource.


    	For more information about the supported resources, see [AWS Resilience Hub supported resources](supported-resources.md "supported-resources.md").
    * **Resource type** – The resource type identifies
     the component resource for your application. For example,
     `AWS::EC2::Instance` declares an Amazon EC2
     instance.
     For more information about grouping AppComponent resources, see [Grouping resources in an Application
     Component](AppComponent.md "AppComponent.md").
    * **Source name** – The name of the input source.
     Choose a source name to view its details in the respective application. For
     manually added input sources, the link will not be available. For example,
     if you choose the source name that is imported from an AWS CloudFormation stack, you
     will be redirected to the stack details page on the AWS CloudFormation.
    * **Source Type** – The type of input source. Input
     sources include AWS CloudFormation stacks, myApplications applications, AWS Resource Groups,
     Terraform state files, and manually added resources.


    ###### Note

    To edit your Amazon EKS clusters, complete the steps in **To edit the input sources of your AWS Resilience Hub
     application** procedure.
    * **Source stack** – The AWS CloudFormation stack that
     contains the resource. This column depends on the type of application
     structure that you selected.
    * **Physical ID** – The actual assigned identifier
     for that resource, such as an Amazon EC2 instance ID or an S3 bucket name.
    * **Included** – This indicates whether AWS Resilience Hub
     includes these resources in the application.
    * **Assessable** – This indicates whether the
     AWS Resilience Hub will assess your resource for resiliency.
    * **AppComponents** – The AWS Resilience Hub component that
     was assigned to this resource when its application structure was
     discovered.
    * **Name** – Name of the application
     resource.
    * **Account** – The AWS account that owns the
     physical resource.

2. To find a resource that is not listed, enter the resource logical ID in the search
   box.
3. To remove a resource from your application, select the resource, and then choose
   **Exclude resource** from **Actions**.
4. To resolve the resources on your application, choose **Refresh
   resources**.
5. To modify your existing application resources, complete the following
   steps:
   1. Select a resource, and then choose **Update stacks** from
      **Actions**.
   2. In the **Update stacks** page, to update your resources,
      complete the appropriate procedures in [Add resource collections](discover-structure.md "discover-structure.md"), and then return to this
      procedure.
   3. Choose **Save**.

6. To add a resource to your application, from **Actions**, choose
   **Add resource** and complete the following steps:
   1. Select a resource type from the **Resource type**
      dropdown list.
   2. Select an AppComponent from the **AppComponent** dropdown
      list.
   3. Enter the resource logical ID in the **Resource name**
      box.
   4. Enter the physical resource ID, or resource name, or the resource ARN in
      the **Resource identifier** box.
   5. Choose **Add**.

7. To edit the resource name, select a resource, choose **Edit resource
   name** from **Actions**, and then complete the
   following steps:
   1. Enter the resource logical ID in the **Resource name**
      box.
   2. Choose **Save**.

8. To edit the resource identifier, select a resource, choose **Edit resource
   identifier** from **Actions**, and then complete the
   following steps:
   1. Enter the physical resource ID, or resource name, or the resource ARN in
      the **Resource identifier** box.
   2. Choose **Save**.

9. To change the AppComponent, select a resource, choose **Change
   AppComponent** from **Actions**, and complete the
   following steps:
   1. Select an AppComponent from the **AppComponent** dropdown
      list.
   2. Choose **Add**.

10. To delete a resource, select a resource, and then choose **Delete
    resource** from **Actions**.
11. To include a resource, select a resource, and then choose **Include
    resource** from **Actions**.

###### To edit the AppComponents of your application

1. To edit the AppComponents of your application, choose the
   **AppComponents** tab.

###### Note

For more information about grouping AppComponent resources, see [Grouping resources in an Application
Component](AppComponent.md "AppComponent.md").

The **AppComponents** section lists all the logical components
that the resources are grouped into. You can identify the AppComponents by the
following:

    * **AppComponent name** – The name of the AWS Resilience Hub
     component that was assigned to this resource when its application structure
     was discovered.
    * **AppComponent type** – The type of AWS Resilience Hub
     component.
    * **Source name** – The name of the input source.
     Choose a source name to view its details in the respective application. For
     example, if you choose the source name that is imported from an AWS CloudFormation
     stack, you will be redirected to the stack details page on the
     AWS CloudFormation.
    * **Resource count** – The number of resources that
     are associated with the input source. Choose a number to view all the
     associated resources of an input source in the
     **Resources** tab.

2. To create an AppComponent, from **Actions** menu, choose
   **Create new AppComponent** and complete the following
   steps:
   1. Enter a name for the AppComponent in the **AppComponent
      name** box. For reference, we have pre-populated this field
      with a sample name.
   2. Select the type of AppComponent from the **AppComponent
      type** dropdown list.
   3. Choose **Save**.

3. To edit an AppComponent, select an AppComponent, and then choose **Edit
   AppComponent** from **Actions**.
4. To delete an AppComponent, select an AppComponent, and then choose
   **Delete AppComponent** from
   **Actions**.
   After you make changes to your resource list, you will receive an alert indicating that
   changes have been made to the draft version of your application. To run an accurate
   resiliency assessment, you must publish a new version of your application. For more
   information about how to publish a new version, see [Publishing a new AWS Resilience Hub application
   version](applications-publish.md "applications-publish.md").
