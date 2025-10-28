# Viewing alarms

You can view all the active alarms that you have set up to monitor the resiliency of
your applications. AWS Resilience Hub uses AWS CloudFormation template to store alarm details that is in-turn
used for creating the alarms in Amazon CloudWatch. You can access the AWS CloudFormation template using Amazon S3
URL, and can download and place it into your code pipeline or create a stack through the
AWS CloudFormation console.

To view alarms from the dashboard, choose **Dashboard** from the left
navigation menu. In **Implemented alarms** table, you can identify the
implemented alarms using the following information:

- **Application impacted** – Name of the applications
  that have implemented this alarm.
- **Active alarms** – Indicates the number of active
  alarms triggered from the applications.
- **FIS in progress** – Indicates the AWS FIS experiment
  that is currently running for your application.

###### To view the alarms implemented in your application

1. In the left navigation menu, choose **Applications**.
2. Select an application from the **Applications** table.
3. In the application summary page, the **Implemented alarms**
   table displays all the recommended alarms that are implemented in your
   application.

To find a specific alarm in the **Implemented alarms** table,
in the **Find alarms by text, property, or value** box, select
one of the following fields, choose an operation, and then type a value.

    * **Alarm name** – Name of the alarm that you
     have set for your application.
    * **Description** – Describes the objective of
     the alarm.
    * **State** – Indicates the current
     implementation state of the Amazon CloudWatch alarm.


    This column displays one of the following values:




    	+ **Implemented** – Indicates that the
    	 alarms recommended by AWS Resilience Hub are implemented in your
    	 application. Choose the number below to view all the recommended
    	 and implemented alarms in **Operational
    	 recommendations** tab.
    	+ **Not implemented** – Indicates that
    	 the alarms recommended by AWS Resilience Hub are included but not
    	 implemented in your application. Choose the number below to view
    	 all the recommended and non-implemented alarms in
    	 **Operational recommendations** tab.
    	+ **Excluded** – Indicates that the
    	 alarms recommended by AWS Resilience Hub are excluded from your
    	 application. Choose the number below to view all the recommended
    	 and excluded alarms in **Operational
    	 recommendations** tab. For more information about
    	 including and excluding recommended alarms, see [Including or excluding operational
    	 recommendations](exclude-recommend.md "exclude-recommend.md").
    	+ **Inactive** – Indicates that the
    	 alarms are deployed to Amazon CloudWatch, but the status is set to
    	 **INSUFFICIENT\_DATA** in Amazon CloudWatch. Choose
    	 the number below to view all the implemented and inactive alarms
    	 in **Operational recommendations** tab.
    * **Source template** – Provides the Amazon
     Resource Name (ARN) of the AWS CloudFormation stack that contains the alarm
     details.
    * **Resource** – Displays the resources that
     this alarm is attached to and was implemented for.
    * **Metric** – Displays the Amazon CloudWatch metric
     assigned for the alarm. For more information about Amazon CloudWatch metrics, see
     [Amazon CloudWatch Metrics](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Metric "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Metric").
    * **Last change** – Displays the date and time
     an alarm was last modified.

###### To view the recommended alarms from assessments

1. In the left navigation menu, choose **Applications**.
2. Select an application from the **Applications** table.

To find an application, enter the application name in the **Find
applications** box. 3. Choose **Assessments** tab.

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
   table.
5. Choose **Operational recommendations** tab.
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




    	+ **Implemented**  – Indicates that the
    	 alarm is implemented in your application. Choosing the number
    	 below will filter the **Alarms** table to
    	 display all the recommended alarms that are implemented in your
    	 application.
    	+ **Not implemented** – Indicates that
    	 the alarm is not implemented or included in your application.
    	 Choosing the number below will filter the
    	 **Alarms** table to display all the
    	 recommended alarms that are not implemented in your
    	 application.
    	+ **Excluded** – Indicates that the
    	 alarm is excluded from the application. Choosing the number
    	 below will filter the **Alarms** table to
    	 display all the recommended alarms that are excluded from your
    	 application. For more information about including and excluding
    	 recommended alarms, see [Including or excluding operational
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
