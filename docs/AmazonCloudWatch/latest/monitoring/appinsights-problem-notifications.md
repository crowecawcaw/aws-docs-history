# Receive notifications for detected problems

You can use Amazon SNS notifications, Systems Manager OpsCenter, or CloudWatch Events to receive notifications about problems that are detected in your applications. 
 


###### CloudWatch Application Insights Amazon SNS notifications for detected problems


You can configure Amazon SNS notifications using the AWS Management Console or the AWS CLI. To set up notifications using the AWS Management Console, you must have the necessary Amazon SNS permissions as shown in
 the following example. 



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sns:ListTopics",
 "sns:Subscribe",
 "sns:CreateTopic"
 ], 
 "Resource": [
 "*" 
 ]
 }
 ] 
}`

```




After you set up Amazon SNS notifications, you receive email notifications when a problem is created or resolved. You also receive 
 notifications when a new observation is added to an existing problem.

The following example shows the content of an email notification.


```

    You are receiving this email because Problem "p-1234567" has been CREATED by Amazon CloudWatch Application Insights
    
    Problem Details: 
    Problem URL: https://`//console.aws.amazon.com/cloudwatch/home?region=us-east-1#settings:AppInsightsSettings/problemDetails?problemId=p-1234567`
    Problem Summary: Title of the problem
    Severity: HIGH
    Insights: Something specific is broken
    Status : RESOLVED
    AffectedResource: arn:aws:ec2:us-east-1:`555555555555`:host/testResource
    Region: us-east-1
    RecurringCount: 0
    StartTime: 2019-03-23T10:42:57.777Z
    LastUpdatedTime: 2019-03-23T21:49:37.777Z
    LastRecurrenceTime: 
    StopTime: 2019-03-23T21:49:37.777Z
    
    Recent Issues
    - TelemetryArn:alarm1
      StartTime: 2024-08-15T22:12:46.007Z
      StopTime:
    - TelemetryArn:log-group1
      StartTime: 2024-08-15T22:12:46.007Z
      StopTime: 2024-08-15T22:12:46.007Z

```

###### How to receive problem notifications using Systems Manager


**Actions through AWS Systems Manager.** CloudWatch Application Insights provides
 built-in integration with Systems Manager OpsCenter. If you choose to use this
 integration for your application, an OpsItem is created on the OpsCenter console
 for every problem detected with the application. From the OpsCenter console, you
 can view summarized information about the problem detected by CloudWatch Application Insights and pick a
 Systems Manager Automation runbook to take remedial actions or further identify
 Windows processes that are causing resource issues in your application. 


###### How to receive problem notifications using CloudWatch Events


From the CloudWatch console, select **Rules** under
 **Events** in the left navigation pane. From
 the **Rules** page, select **Create rule**. Choose **Amazon CloudWatch Application Insights**
 from the **Service Name** dropdown list and choose
 the **Event Type**. Then, choose **Add target** and select the target and parameters, for
 example, an **SNS topic** or **Lambda function**.
