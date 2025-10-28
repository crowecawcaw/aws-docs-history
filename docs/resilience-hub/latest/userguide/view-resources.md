# Viewing resources of AWS Resilience Hub application

###### To view resources of your application

1. In the navigation pane, choose **Applications**.
2. On the **Applications** page, select the application for
   which you want to update the security permissions.
3. From **Actions**, choose **View
   resources**.

In **Resources** tab, you can identify resources in the
**Resources** table by the following:

    * **Logical ID** – A logical ID is a name used
     to identify resources in your AWS CloudFormation stack, Terraform state file,
     myApplications application, or AWS Resource Groups.


    ###### Note



    	+ Terraform lets you use the same name for different
    	 resource types. Therefore, you see "*- resource type*" at the end of the logical
    	 ID for resources that share the same name.
    	+ To view the instances of all the application resources,
    	 choose the plus (**+**) sign before the
    	 **Logical ID**. To view all the
    	 instances of an application resource, choose the plus
    	 (**+**) sign before the Logical ID of
    	 each resource.


    	For more information about the supported resources, see
    	 [AWS Resilience Hub supported resources](supported-resources.md "supported-resources.md").
    * **Status** – This indicates whether the
     AWS Resilience Hub will assess your resource for resiliency.
    * **Resource type** – The resource type
     identifies the component resource for your application. For example,
     `AWS::EC2::Instance` declares an Amazon EC2
     instance.
     For more information about grouping AppComponent resources, see [Grouping resources in an Application
     Component](AppComponent.md "AppComponent.md").
    * **Source name** – The name of the input
     source. Choose a source name to view its details in the respective
     application. For manually added input sources, the link will not be
     available. For example, if you choose the source name that is imported
     from an AWS CloudFormation stack, you will be redirected to the stack details
     page on the AWS CloudFormation.
    * **Source type** – The type of the input
     source.
    * **AppComponent type** – The type of input
     source. Input sources include AWS CloudFormation stacks, myApplications
     applications, AWS Resource Groups, Terraform state files, and manually added
     resources.


    ###### Note

    To edit your Amazon EKS clusters, complete the steps in **To edit the input sources of your AWS Resilience Hub
     application** procedure.
    * **Physical ID** – The actual assigned
     identifier for that resource, such as an Amazon EC2 instance ID or an S3
     bucket name.
    * **Included** – This indicates whether
     AWS Resilience Hub includes these resources in the application.
    * **AppComponents** – The AWS Resilience Hub component
     that was assigned to this resource when its application structure was
     discovered.
    * **Name** – Name of the application
     resource.
    * **Account** – The AWS account that owns the
     physical resource.

4. Choose **Save and update**.
