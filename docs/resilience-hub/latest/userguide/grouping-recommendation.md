# AWS Resilience Hub resource grouping

recommendations

This section explains how to generate and review resource grouping recommendations
in AWS Resilience Hub.

###### Note

You can grant the necessary IAM permissions that are required to work with
AWS Resilience Hub by using `AWSResilienceHubAsssessmentExecutionPolicy` AWS
managed policy. For more information about AWS managed policy, see [AWSResilienceHubAsssessmentExecutionPolicy](security-iam-awsmanpol.md#security_iam_aws-assessment-policy "security-iam-awsmanpol.md#security_iam_aws-assessment-policy").

###### To view resource grouping recommendations

1. In the navigation pane, choose **Applications**.
2. Choose **Add application** page, choose the application
   name for which you want to review resource grouping recommendations.
3. Choose the **Application structure** tab.
4. If AWS Resilience Hub displays an information alert, choose **Review
   recommendations** to view all the resource grouping
   recommendations. Else complete the following steps to manually generate
   resource grouping recommendations:
   1. Choose **Resources**.
   2. Choose **Get grouping recommendations** from
      **Actions** menu.

   AWS Resilience Hub scans your resources to check how they can be grouped in
   the best possible way into relevant AppComponents to improve the
   accuracy of the assessments. If AWS Resilience Hub learns that your resources
   can be grouped together, it displays an information alert for the
   same. 3. If the information alert is displayed, choose **Review
   recommendations** to view all the resource grouping
   recommendations.You can identify the AppComponents in the **Review resource
   grouping recommendations** section using the following:
   - **AppComponent name** – Name
     of the AppComponent in which the resources will be grouped.
   - **Confidence level** –
     Indicates the confidence level of AWS Resilience Hub in the grouping
     recommendation.
   - **Resource count** – Indicates
     the number of resources that will be grouped in the
     AppComponent.
   - **AppComponent type** –
     Indicates the type of AppComponent.

###### To view resources that will be grouped in AppComponents

1. Complete the steps in **[To view resource grouping recommendations](#view-resource-grouping "#view-resource-grouping")** procedure
   and then return to this procedure.
2. In **Review resource grouping recommendations** section,
   select the check box (adjacent to the **AppComponent name**)
   to view all the resources that will be grouped together within the selected
   AppComponent. If you select multiple check boxes, AWS Resilience Hub displays a
   dynamically generated **recommendations selected** section
   that groups the selected AppComponents under their respective AppComponent
   type. Choose the number below each AppComponent type to view all the
   resources that will be grouped together within the selected
   AppComponent.

You can identify the resources that will be grouped in the selected
AppComponent in the **Resources** section using the
following:

    * **Logical ID** – Indicates the logical ID
     of the resource. A logical ID is a name used to identify resources
     in your AWS CloudFormation stack, Terraform state file, myApplications application, or AWS Resource Groups.
    * **Physical ID** – The actual assigned
     identifier for the resource, such as an Amazon EC2 instance ID or an Amazon S3
     bucket name.
    * **Type** – Indicates the type
     of resource.
    * **Region** – AWS Region in
     which the resource is located.

###### To accept resource grouping recommendations

1. Complete the steps in **[To view resource grouping recommendations](#view-resource-grouping "#view-resource-grouping")** procedure and
   then return to this procedure.
2. In the **Review resource grouping recommendations**
   section, select all the check boxes adjacent to the **AppComponent
   name**. To find a specific AppComponent, enter the AppComponent
   name in the **Find AppComponents** box.

###### Note

By default, AWS Resilience Hub displays all the resource grouping
recommendations. To filter the table with previously rejected resource
grouping recommendations, choose **Previously
rejected** from the dropdown menu adjacent to the
**Find AppComponents** box. 3. Choose **Accept**. 4. Choose **Accept** in the **Accept resource
grouping recommendation** dialog.

AWS Resilience Hub displays an information alert if the resource grouping is
successful. If you have accepted only a subset of resource grouping
recommendations, **Review resource grouping
recommendations** section displays all the resource grouping
recommendations that you have not accepted.

###### To reject resource grouping recommendations

1. Complete the steps in **[To view resource grouping recommendations](#view-resource-grouping "#view-resource-grouping")** procedure and
   then return to this procedure.
2. In **Review resource grouping recommendations** section,
   select all the check boxes adjacent to the **AppComponent
   name**. To find a specific AppComponent, enter the AppComponent
   name in the **Find AppComponents** box.

###### Note

By default, AWS Resilience Hub displays all the resource grouping
recommendations. To filter the table with previously rejected resource
grouping recommendations, select **Previously
rejected** from the dropdown menu adjacent to the
**Find AppComponents** box. 3. Choose **Reject**. 4. Select one of the reasons for rejecting the resource grouping
recommendation and then choose **Reject** in the
**Reject resource grouping recommendation**
dialog.

AWS Resilience Hub displays an information alert confirming the same. If you have
rejected only a subset of resource grouping recommendations,
**Review resource grouping recommendations** section
displays all the resource grouping recommendations that you have not
accepted.
