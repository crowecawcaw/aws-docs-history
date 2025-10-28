End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Managing alarm notifications in AWS IoT Events

AWS IoT Events integrates with Lambda, offering custom event processing capabilities. This
section explores how to use Lambda functions within your AWS IoT Events detector models, allowing
you to execute complex logic, interact with external services, and implement
sophisticated event handling.

AWS IoT Events uses a Lambda function to manage alarm notifications. You can use the Lambda
function provided by AWS IoT Events or create a new one.

###### Topics

- [Creating a Lambda function in AWS IoT Events](alarms-create-lambda.md "alarms-create-lambda.md")
- [Using the Lambda function provided by
  AWS IoT Events](use-alarm-notifications.md "use-alarm-notifications.md")
- [Manage IAM Identity Center access of alarm
  recipients in AWS IoT Events](sso-authorization-recipients.md "sso-authorization-recipients.md")
