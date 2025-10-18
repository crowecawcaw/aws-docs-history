# Create a composite alarm

The steps in this section explain how to use the CloudWatch console to create a composite
 alarm. You can also use the API or AWS CLI to create a composite alarm. For more information,
 see [PutCompositeAlarm](../APIReference/API_PutCompositeAlarm.md "../APIReference/API_PutCompositeAlarm.md") or [put-composite-alarm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-composite-alarm.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-composite-alarm.html")


###### To create a composite alarm

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, and then choose
 **All alarms**.
3. From the list of alarms, select the check box next to each of the existing alarms
 that you want to reference in your rule expression, and then choose **Create
 composite alarm**.
4. Under **Specify composite alarm conditions**, specify the rule
 expression for your new composite alarm.


###### Note

Automatically, the alarms that you selected from the list of alarms are listed in
 the **Conditions** box. By default, the `ALARM` function
 has been designated to each of your alarms, and each of your alarms is joined by the
 logical operator `OR`.


You can use the following substeps to modify your rule expression:


	1. You can change the required state for each of your alarms from
	 `ALARM` to `OK` or `INSUFFICIENT_DATA`.
	2. You can change the logical operator in your rule expression from `OR`
	 to `AND` or `NOT`, and you can add parentheses to group your
	 functions.
	3. You can include other alarms in your rule expression or delete alarms from your
	 rule expression.**Example: Rule expression with conditions**



```
(ALARM("CPUUtilizationTooHigh") OR 
ALARM("DiskReadOpsTooHigh")) AND 
OK("NetworkOutTooHigh")
```

In the example rule expression where the composite alarm goes into
 `ALARM` when ALARM ("CPUUtilizationTooHigh" or ALARM("DiskReadOpsTooHigh")
 is in `ALARM` at the same time as OK("NetworkOutTooHigh") is in
 `OK`.
5. When finished, choose **Next**.
6. Under **Configure actions**, you can choose from the
 following:


For ***Notification***




	* **Select an exisiting SNS topic**, **Create a new SNS
	 topic**, or **Use a topic ARN** to define the SNS topic
	 that will receive the notification.
	* **Add notification**, so your alarm can send multiple
	 notifications for the same alarm state or different alarm states.
	* **Remove** to stop your alarm from sending notifications or
	 taking actions.
(Optional) To have the alarm invoke a Lambda function when it changes state, choose
 **Add Lambda action**. Then specify the function name or ARN, and
 optionally choose a specific version of the function.


For ***Systems Manager action***




	* **Add Systems Manager action**, so your alarm can perform an
	 SSM action when it goes into ALARM.
To learn more about Systems Manager actions, see [Configuring CloudWatch to create OpsItems from alarms](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.html") in the *AWS Systems Manager
 User Guide* and [Incident
 creation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-creation.html "https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-creation.html") in the *Incident Manager User Guide*. To create an
 alarm that performs an SSM Incident Manager action, you must have the correct
 permissions. For more information, see [Identity-based policy examples for AWS Systems Manager Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/security_iam_id-based-policy-examples.html "https://docs.aws.amazon.com/incident-manager/latest/userguide/security_iam_id-based-policy-examples.html") in
 the *Incident Manager User Guide*.


To have the alarm start an investigation, choose **Add investigation
 action** and then select your investigation group. For more information about
 CloudWatch investigations, see [CloudWatch investigations](Investigations.md "Investigations.md").
7. When finished, choose **Next**.
8. Under **Add name and description**, enter an alarm name and
 *optional* description for your new composite alarm. The name must
 contain only UTF-8 characters, and can't contain ASCII control characters. The
 description can include markdown formatting, which is displayed only in the alarm
 **Details** tab in the CloudWatch console. The markdown can be useful to
 add links to runbooks or other internal resources.
9. When finished, choose **Next**.
10. Under **Preview and create**, confirm your information, and then
 choose **Create composite alarm**.


###### Note

You can create a cycle of composite alarms, where one composite alarm and another
 composite alarm depend on each other. If you find yourself in this scenario, your
 composite alarms stop being evaluated, and you can't delete your composite alarms
 because they're dependent on each other. The easiest way to break the cycle of
 dependecy between your composite alarms is to change the function
 `AlarmRule` in one of your composite alarms to `False`.
