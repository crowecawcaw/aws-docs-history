# Requirements for alarm

notifications in AWS IoT SiteWise

AWS IoT Events uses an AWS Lambda function in your AWS account to send alarm notifications.
You must create this Lambda function in the same AWS Region as your alarms to enable
alarm notifications. This Lambda function uses [Amazon Simple Notification Service (Amazon SNS)](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md") to send text notifications
and [Amazon Simple Email Service
(Amazon SES)](../../../ses/latest/dg/Welcome.md "../../../ses/latest/dg/Welcome.md") to send email notifications. When you create the AWS IoT Events alarm, you
configure the protocols and settings that the alarm uses to send notifications.

###### Note

End of support notice: On May 20, 2026, AWS
will end support for AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events resources. For more information, see [AWS IoT Events end of support](../../../iotevents/latest/developerguide/iotevents-end-of-support.md "../../../iotevents/latest/developerguide/iotevents-end-of-support.md").

AWS IoT Events provides an AWS CloudFormation stack template that you can use to create this Lambda
function in your account. For more information, see [Alarm notification
Lambda function](../../../iotevents/latest/developerguide/lambda-support.md "../../../iotevents/latest/developerguide/lambda-support.md") in the _AWS IoT Events Developer Guide_.
