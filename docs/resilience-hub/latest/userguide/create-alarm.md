# Creating alarms from the operational

recommendations

AWS Resilience Hub creates an AWS CloudFormation template that contains details to create the selected
alarms in Amazon CloudWatch. After the template is generated, you can access it through an Amazon S3
URL, download the same and place it in your code pipeline or create a stack through the
AWS CloudFormation console.

To create an alarm based on AWS Resilience Hub recommendations, you must create an AWS CloudFormation
template for the recommended alarms and include them in your code base.

###### To create alarms in operational recommendations

1. In the left navigation menu, choose **Applications**.
2. In **Applications**, choose your application.
3. Choose **Assessments** tab.

In **Resiliency assessments** table, you can identify your
assessments using the following information:

    * **Name** – Name of the assessment you had provided at
     the time of creation.
    * **Status** – Indicates the execution state of the
     assessment.
    * **Compliance status** – Indicates if the assessment
     is compliant with the resiliency policy.
    * **Resiliency drift status** – Indicates if your
     application has drifted or not from the previous successful
     assessment.
    * **App version** – Version of your application.
    * **Invoker** – Indicates the role that invoked the
     assessment.
    * **Start time** – Indicates the start time of the
     assessment.
    * **End time** – Indicates the end time of the
     assessment.
    * **ARN** – The Amazon Resource Name (ARN) of the
     assessment.

4. Select an assessment from the **Resiliency assessments**
   table. If you don't have an assessment, complete the procedure in [Running resiliency assessments in AWS Resilience Hub](run-assessment.md "run-assessment.md") and then return to this step.
5. Choose **Operational recommendations**.
6. If not selected by default, choose **Alarms** tab.

In **Alarms** table, you can identify the recommended alarms
using the following:

    * **Name** – Name of the alarm that you have set
     for your application.
    * **Description** – Describes the objective of
     the alarm.
    * **State** – Indicates the current
     implementation state of the Amazon CloudWatch alarms.


    This column displays one of the following values:




    	+ **Implemented** – Indicates that the
    	 alarms recommended by AWS Resilience Hub are implemented in your
    	 application. Choosing the number below will filter the
    	 **Alarms** table to display all the
    	 recommended alarms that are implemented in your
    	 application.
    	+ **Not implemented** – Indicates that
    	 the alarms recommended by AWS Resilience Hub are included but not
    	 implemented in your application. Choosing the number below will
    	 filter the **Alarms** table to display all the
    	 recommended alarms that are not implemented in your
    	 application.
    	+ **Excluded** – Indicates that the
    	 alarms recommended by AWS Resilience Hub are excluded from your
    	 application. Choosing the number below will filter the
    	 **Alarms** table to display all the
    	 recommended alarms that are excluded from your application. For
    	 more information about including and excluding recommended
    	 alarms, see [Including or excluding operational
    	 recommendations](exclude-recommend.md "exclude-recommend.md").
    	+ **Inactive** – Indicates that the
    	 alarms are deployed to Amazon CloudWatch, but the status is set to
    	 **INSUFFICIENT\_DATA** in Amazon CloudWatch. Choosing
    	 the number below will filter the **Alarms**
    	 table to display all the implemented and inactive alarms.
    * **Configuration** – Indicates if there are any
     pending configuration dependencies that needs to be addressed.
    * **Type** – Indicates the type of alarm.
    * **AppComponent** – Indicates the Application
     Components (AppComponents) that are associated with this alarm.
    * **Reference ID** – Indicates the logical
     identifier of the AWS CloudFormation stack event in AWS CloudFormation.
    * **Recommendation ID** – Indicates the logical
     identifier of the AWS CloudFormation stack resource in AWS CloudFormation.

7. In **Alarms** tab, to filter the alarm recommendations in
   **Alarms** table based on a specific state, select a number
   below the same.
8. Select the recommended alarms that you want to set up for your application,
   and choose **Create CloudFormation template**.
9. In **Create CloudFormation template** dialog, you can use the
   auto-generated name, or you can enter a name for AWS CloudFormation template in the
   **CloudFormation template name** box.
10. Choose **Create**. This can take up to a few minutes to
    create the AWS CloudFormation template.

Complete the following procedure to include the recommendations in your code
base.

###### To include the AWS Resilience Hub recommendations your code base

1. Choose **Templates** tab to view the template you just
   created. You can identify your templates using the following:
   - **Name** – Name of the assessment you had
     provided at the time of creation.
   - **Status** – Indicates the execution state of
     the assessment.
   - **Type** – Indicates the type of operational
     recommendation.
   - **Format** – Indicates the format (JSON/ text)
     in which the template is created.
   - **Start time** – Indicates the start time of
     the assessment.
   - **End time** – Indicates the end time of the
     assessment.
   - **ARN** – The ARN of the template

2. Under **Template details**, choose the link below
   **Templates S3 Path** to open the template object in Amazon S3
   console.
3. In Amazon S3 console, from **Objects** table, choose the Alarms
   folder link.
4. To copy the Amazon S3 path, select the check box in front of the JSON file and
   choose **Copy URL**.
5. Create an AWS CloudFormation stack from AWS CloudFormation console. For more information about
   creating an AWS CloudFormation stack, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md").

While creating the AWS CloudFormation stack, you must provide the Amazon S3 path that you
copied from the previous step.
