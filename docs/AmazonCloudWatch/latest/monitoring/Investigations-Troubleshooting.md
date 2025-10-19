# Troubleshooting

###### Topics

* [CloudWatch investigations cannot assume
 the necessary IAM roles or permissions. Please verify required roles and
 permissions are correctly configured](#Investigations-Troubleshooting-Permissions "#Investigations-Troubleshooting-Permissions")
* [Unable to identify
 event source. Verify that the resource exists in your application topology and
 the resource type is supported.](#Investigations-Troubleshooting-eventsource "#Investigations-Troubleshooting-eventsource")
* [Analysis complete. Submit
 additional findings to receive updated suggestions](#Investigations-Troubleshooting-complete "#Investigations-Troubleshooting-complete")
* [Source account status
 shows "Pending link to monitoring account"](#Investigations-Troubleshooting-cross-account "#Investigations-Troubleshooting-cross-account")
* [Incident report
 generation issues](#Investigations-Troubleshooting-IncidentReports "#Investigations-Troubleshooting-IncidentReports")

## CloudWatch investigations cannot assume
 the necessary IAM roles or permissions. Please verify required roles and
 permissions are correctly configured


CloudWatch investigations use an IAM role to be able to access information in your topology. This
 IAM role must be configured with adequate permissions. For more information about
 the necessary permissions, see [How to control what data CloudWatch investigations has
 access to during investigations](Investigations-Security.md#Investigations-Security-Data "Investigations-Security.md#Investigations-Security-Data").


## Unable to identify
 event source. Verify that the resource exists in your application topology and
 the resource type is supported.


There are several AWS services and features that we recommend you to enable to
 provide additional valuable information to CloudWatch investigations. These services and features can
 help CloudWatch investigations identify event sources. For more information, see [(Recommended) Best practices to
 enhance investigations](Investigations-RecommendedServices.md "Investigations-RecommendedServices.md").


## Analysis complete. Submit
 additional findings to receive updated suggestions


When you see this message, CloudWatch investigations has finished analyzing your topology and telemetry
 based on the findings that it has found so far. If you think that the root cause
 hasn't been found, you can manually add more telemetry to the investigation, and
 this might cause CloudWatch investigations to scan your system again based on the new information.


To add new telemetry, navigate to that service's console and add the telemetry to
 the investigation. For example, to add a Lambda metric to the investigation, you can
 do the following:



1. Open the Lambda console.
2. In the **Monitor** section, find the metric.
3. Open the vertical ellipsis context menu 
![An example of a CloudWatch overview home page, showing alarms and their current state, and examples of other metrics graph widgets that might appear on the overview home page.](/images/AmazonCloudWatch/latest/monitoring/images/vmore.png)
 for the metric, choose
 **Investigate**, **Add to investigation**
 Then, in the **Investigate** pane, select the name of the
 investigation.

## Source account status
 shows "Pending link to monitoring account"


Check that both your monitoring account and source account are set up
 correctly.



1. Check that the source account ID and the source account role name are
 correct.
2. The monitoring account role needs to have `sts:AssumeRole`
 permission to assume the source account role.
3. The source account role needs to have a trust policy for the monitoring
 account role to assume.
4. The trust policy in the source account role must be properly scoped to
 have the Investigation Group arn in the `sts:ExternalId` context
 key:



```

            "Condition": {
                "StringEquals": {
                    "sts:ExternalId": "investigation-group-arn"
                }
            }

```

## Incident report
 generation issues


This section describes common issues you might encounter when generating incident
 reports and how to resolve them.


### Report generation fails or produces incomplete content


If incident report generation fails, verify the
 following:



* The investigation has at least one accepted hypothesis in the
 **Feed**
* Your user and your investigation group have the necessary permissions, see [User permissions for your CloudWatch investigations group](Investigations-Security.md#Investigations-Security-IAM "Investigations-Security.md#Investigations-Security-IAM") .
