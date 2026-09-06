

# Receiving AWS Elemental MediaTailor channel assembly alerts
<a name="channel-assembly-alerts"></a>

MediaTailor creates alerts for issues or potential issues that occur with your channel assembly resources. The alert describes the issue, when the issue occurred, and the affected resources.

You can view the alerts in the AWS Management Console, the AWS Command Line Interface (AWS CLI), AWS SDKs, or programmatically using the MediaTailor [ListAlerts](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ListAlerts.html) API.

**Important**  
Alerts are only available for channel assembly resources created on or after July 14th, 2021.


**Channel Assembly Alerts**  


- **VOD Source**
  - **Alert Code:** NOT\_PROCESSED / **Alert Message:** MediaTailor hasn't processed the package configuration {{configurationPath}}. / **Notes:** 
  - **Alert Code:** UNREACHABLE / **Alert Message:** We can't reach the URL {{url}}. / **Notes:** 
  - **Alert Code:** UNAUTHORIZED / **Alert Message:** {{url}} didn't authorize the request. / **Notes:** 
  - **Alert Code:** TIMEOUT / **Alert Message:** The connection to {{url}} timed out. / **Notes:** 
  - **Alert Code:** UNPARSABLE\_MANIFEST / **Alert Message:** MediaTailor encountered an issue while parsing the manifest from {{url}}. / **Notes:** 
  - **Alert Code:** VARIANT\_DURATION\_MISMATCH / **Alert Message:** MediaTailor encountered variants with mismatched total durations while parsing the manifest from {{url}}. This might cause stalling during playback. / **Notes:** Your manifest has varying durations across variants/representations. This might result in missing or incorrect captions, and MediaTailor being unable to insert ads.
  - **Alert Code:** SEGMENT\_DURATION\_TOO\_LONG / **Alert Message:** MediaTailor encountered a segment with a duration greater than thirty seconds while parsing the manifest from {{url}}. This might cause stalling during playback, missing or incorrect captions, and the inability to insert advertisements. / **Notes:** Your manifest contains a segment that is greater than 30 seconds.
  - **Alert Code:** TARGET\_DURATION\_MISMATCH / **Alert Message:** MediaTailor encountered a mismatch of EXT-X-TARGETDURATION values across HLS manifests while parsing the manifest from {{url}}. This might cause stalling during playback. / **Notes:** The target duration doesn't match across all manifests in the source..

- **Source Location**
  - **Alert Code:** NOT\_PROCESSED
  - **Alert Message:** MediaTailor hasn't processed the resource {{resourceName}}.
  - **Notes:** 

- **Program**
  - **Alert Code:** VOD\_SOURCE\_ALERT / **Alert Message:** The VOD source {{vodSourceName}} in this program has the following alert: {{vodSourceAlertCode}}: {{vodSourceAlertMessage}} / **Notes:** 
  - **Alert Code:** SOURCE\_LOCATION\_ALERT / **Alert Message:** The source location {{sourceLocationName}} contained in this program has the following alert: {{sourceLocationAlertCode}}: {{sourceLocationAlertMessage}} / **Notes:** 
  - **Alert Code:** CODEC\_MISMATCH / **Alert Message:** MediaTailor encountered mismatched codec in {{channelName}} schedule. The mismatch is in {{sourceGroupName}} between {{programName1}}'s manifest {{manifestUrl}} and {{programName2}}'s manifest {{manifestUrl}}. / **Notes:** 
  - **Alert Code:** RESOLUTION\_MISMATCH / **Alert Message:** MediaTailor encountered mismatched resolution in {{channelName}} schedule. The mismatch is in {{sourceGroupName}} between {{programName1}}'s manifest {{manifestUrl}} and {{programName2}}'s manifest {{manifestUrl}}. / **Notes:** 
  - **Alert Code:** BANDWIDTH\_MISMATCH / **Alert Message:** MediaTailor encountered mismatched bandwidth in {{channelName}} schedule. The mismatch is in {{sourceGroupName}} between {{programName1}}'s manifest {{manifestUrl}} and {{programName2}}'s manifest {{manifestUrl}}. / **Notes:** 
  - **Alert Code:** FRAMERATE\_MISMATCH / **Alert Message:** MediaTailor encountered mismatched framerate in {{channelName}} schedule. The mismatch is in {{sourceGroupName}} between {{programName1}}'s manifest {{manifestUrl}} and {{programName2}}'s manifest {{manifestUrl}}. / **Notes:** 
  - **Alert Code:** TARGET\_DURATION\_MISMATCH / **Alert Message:** MediaTailor encountered mismatched EXT-X-TARGETDURATION values across HLS manifests in {{channelName}} schedule. The mismatch is in {{sourceGroupName}} between {{programName1}}'s manifest {{manifestUrl}} and {{programName2}}'s manifest {{manifestUrl}}. / **Notes:** 
  - **Alert Code:** SEGMENT\_DURATION\_MISMATCH / **Alert Message:** MediaTailor encountered mismatched segment duration values across manifests in {{channelName}} schedule. The mismatch is in {{sourceGroupName}} between {{programName1}}'s manifest {{manifestUrl}} and {{programName2}}'s manifest {{manifestUrl}}. / **Notes:** 
  - **Alert Code:** NO\_COMMON\_SEGMENT\_BOUNDARY\_FOR\_AD\_SLATE / **Alert Message:** MediaTailor was not able to insert ad slate at offset {{offsetMillis}} for program {{programName}}. There is no common segment boundary at the ad slate's start time. / **Notes:** 
  - **Alert Code:** NOT\_PROCESSED / **Alert Message:** MediaTailor hasn't processed the resource {{resourceName}}. / **Notes:** 
  - **Alert Code:** TOO\_MANY\_ALERTS / **Alert Message:** MediaTailor has found too many alerts and will not provide any more alerts for {{programName}}. Clear existing alerts to continue receiving alerts for {{programName}}. / **Notes:** 

- **Channel**
  - **Alert Code:** PROGRAM\_ALERT
  - **Alert Message:** The program {{programName}} contained in this channel has the following alert: {{programAlertCode}}: {{programAlertMessage}}
  - **Notes:** 



## Troubleshooting manifest-related alerts
<a name="channel-assembly-troubleshooting-manifest-alerts"></a>

When you encounter manifest-related alerts such as `UNPARSABLE_MANIFEST`, `VARIANT_DURATION_MISMATCH`, or `TARGET_DURATION_MISMATCH`, check the following:

1. **Verify source requirements**: Ensure your content meets the requirements outlined in [Integrating a content source for MediaTailor ad insertion](integrating-origin.md).

1. **Check manifest logs**: For detailed manifest error analysis and event types, see [AWS Elemental MediaTailor manifest logs description and event types](log-types.md).

1. **Check error codes**: For detailed error analysis, see [Troubleshooting MediaTailor](troubleshooting.md).

1. **Review manifest format**: Verify that your manifest follows the correct format specifications for your streaming protocol (HLS or DASH).

## Viewing alerts
<a name="channel-assembly-viewing-alerts-procedure"></a>

You can view alerts for any MediaTailor channel assembly resource. When you view the alerts for channels and programs, MediaTailor includes all of the related resources contained within the channel or program. For example, when you view the alerts for a specific program, you also see alerts for the source location and VOD sources that the program contains.

To view alerts, perform the following procedure.

------
#### [ Console ]

**To view alerts in the console**

1. Open the MediaTailor console at [https://console.aws.amazon.com/mediatailor/](https://console.aws.amazon.com/mediatailor/).

1. Choose the resource that you want to view alerts for.

1. Select the **Alerts** tab to view the alerts.

------
#### [ AWS Command Line Interface (AWS CLI) ]

To list alerts for a channel assembly resource, you need the resource's [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html). You can use the `describe-{{resource_type}}` command in the AWS Command Line Interface (AWS CLI) to get the resource's ARN. For example, run the [describe-channel](https://docs.aws.amazon.com/cli/latest/reference/mediatailor/describe-channel.html) command to get a specific channel's ARN:

```
aws mediatailor describe-channel --channel-name {{MyChannelName}}
```

Then use the [aws mediatailor list-alerts](https://docs.aws.amazon.com/cli/latest/reference/mediatailor/list-alerts.html) command to list the alerts associated with the resource:

```
aws mediatailor list-alerts --resource-arn arn:aws:mediatailor:{{region}}:{{aws-account-id}}:{{resource-type}}/{{resource-name}}
```

------
#### [ API ]

To list alerts for a channel assembly resource, you need the resource's [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html). You can use the `Describe{{Resource}}` operation in the MediaTailor API to get the resource's ARN. For example, use the [DescribeChannel](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DescribeChannel.html) operation to get a specific channel's ARN.

Then use the [ListAlerts](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ListAlerts.html) API to list the alerts for the resource.

------

## Handling alerts
<a name="channel-assembly-handling-alerts"></a>

When an alert occurs, view the alerts in the AWS Management Console, or use the AWS Command Line Interface (AWS CLI), AWS SDKs, or the MediaTailor Alerts API to determine the possible sources of the issue.

After you resolve the issue, MediaTailor clears the alert.