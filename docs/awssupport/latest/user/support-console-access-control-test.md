# Testing Support Center Console API calls

To validate that API calls to the console work, open the [AWS Support Center Console](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support"). If the calls aren't successful, then you see a banner
outlining the errors.

You can use AWS CloudTrail to debug the API calls made to the Support Center Console. The CloudTrail event for
the API call shows if you have missing IAM policies. You can also investigate IP address
forwarding issues by comparing your browser's IP addresses to the client IP address in the CloudTrail
event.

To view CloudTrail events for calls to the Support Center Console, complete the following steps:

1. Sign in to the AWS Management Console and open the CloudTrail console at
   [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the navigation pane, choose **Event history**. You see a filtered list
   of events with the most recent events showing first. The default filter for events is
   **Read only**, set to **false**. To clear the filter, choose
   **X** at the right of the filter.
3. Choose the event source **support-console.amazonaws.com**. On the event details page, you
   can view details about the event, see any referenced resources, and view the event
   record.
