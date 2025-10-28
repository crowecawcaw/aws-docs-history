# Amazon EventBridge and AWS Organizations

AWS Organizations can work with Amazon EventBridge, formerly Amazon CloudWatch Events, to raise events when administrator-specified actions
occur in an organization. For example, because of the sensitivity of such actions, most
administrators would want to be warned every time someone creates a new account in the
organization or when an administrator of a member account attempts to leave the
organization. You can configure EventBridge rules that look for these actions and then send
the generated events to administrator-defined targets. Targets can be an Amazon SNS topic
that emails or text messages its subscribers. You could also create an AWS Lambda
function that logs the details of the action for your later review.

For a tutorial that shows how to enable EventBridge to monitor key activity in your
organization, see [Tutorial: Monitor important changes to your
organization with Amazon EventBridge](orgs_tutorials_cwe.md "orgs_tutorials_cwe.md").

###### Important

Currently, AWS Organizations is hosted in only the US East (N. Virginia) Region (even though
it is available globally). To perform the steps in this tutorial, you must configure
the AWS Management Console to use that region.

To learn more about EventBridge, including how to configure and enable it, see the _[Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md")_.
