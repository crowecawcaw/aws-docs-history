# Edit or delete a canary

You can edit or delete an existing canary.

**Edit canary**

When you edit a canary, even if you don't change its schedule,
 the schedule is reset corresponding to when you edit the canary. For example, if you have a canary that
 runs every hour, and you edit that canary, the canary will run immediately after the edit is completed and
 then every hour after that.

###### To edit or update a canary

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Application Signals**, 
 **Synthetics Canaries**.
3. Select the button next to the canary name, and choose **Actions**, 
 **Edit**.
4. (Optional) If this canary performs visual monitoring of screenshots and you want to set the next run
 of the canary as the baseline, select **Set next run as new baseline**.
5. (Optional) If this canary performs visual monitoring of screenshots and you want to remove a screenshot from 
 visual monitoring or you want to designate parts of the 
 screenshot to be ignored during visual comparisons, under **Visual Monitoring**
 choose **Edit Baseline**.


The screenshot appears, and you can do one of the following:




	* To remove the screenshot from being used for visual monitoring, select 
	 **Remove screenshot from visual test baseline**.
	* To designate parts of the screenshot to be ignored during visual comparisons, 
	 click and drag to draw areas
	 of the screen to ignore. Once you have done this for all the areas that you want to ignore
	 during comparisons, choose **Save**.
6. Under **Script editor**, **Runtime version**, select a synthetics runtime version to execute the canary. For information on synthetics runtime versions, see [Synthetics runtime versions](CloudWatch_Synthetics_Canaries_Library.md "CloudWatch_Synthetics_Canaries_Library.md") .


Under **Browser configuration**, you can enable the browser to test the canary. You must select at least one browser.
7. Make any other changes to the canary that you'd like, and choose **Save**.
**Delete canary**

When you delete a canary, you can choose whether to also delete other resources used and created by the canary.
 If the canary’s `ProvisionedResourceCleanup` field is set to `AUTOMATIC` or 
 `DeleteLambda` is specified as `true` when you
 delete the canary, 
 CloudWatch Synthetics will automatically delete the Lambda functions and layers that are used by the canary.

When you delete a canary, you should also delete the following:


* Lambda functions and layers used by this canary. Their prefix is
 `cwsyn-*MyCanaryName*`.
* CloudWatch alarms created for this canary. These alarms have a name that starts with
 `Synthetics-Alarm-*MyCanaryName*`. For more 
 information about deleting alarms, see [Edit or delete a CloudWatch alarm](Manage-CloudWatch-Alarm.md#Edit-CloudWatch-Alarm "Manage-CloudWatch-Alarm.md#Edit-CloudWatch-Alarm").
* Amazon S3 objects and buckets, such as the canary's results location and artifact
 location.
* IAM roles created for the canary. These have the name
 `role/service-role/CloudWatchSyntheticsRole-*MyCanaryName*`.
* Log groups in CloudWatch Logs created for the canary. These logs groups have the following
 names: `/aws/lambda/cwsyn-*MyCanaryName*-`randomId``.
Before you delete a canary, you might want to view the canary details and make note of
 this information. That way, you can delete the correct resources after you delete the
 canary.

###### To delete a canary

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Application Signals**, 
 **Synthetics Canaries**.
3. If the canary is currently in the `RUNNING` state, you must stop it. Only canaries
 in the `STOPPED`, `READY(NOT_STARTED)`, or `ERROR` states can be deleted.


To stop the canary, select the button next to the canary name, and choose **Actions**, 
 **Stop**.
4. Select the button next to the canary name, and choose **Actions**, 
 **Delete**.
5. Choose whether to also delete the other resources created for and used by the canary. 
 Lambda functions and layers will be deleted alongside the canary, but you can additionally choose to delete the canary's IAM role and IAM policy.


Enter `Delete` into the box and choose **Delete**.
6. Delete the other resources used by and created for the canary, as listed earlier in this
 section.
