AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Set up Amazon CloudWatch alarms for AWS Blu Age Runtime on container

You can set up CloudWatch to have more visible notifications whenever your deployed applications encounter
exceptions. This helps you to monitor your application log redirected to CloudWatch, and add an alarm to warn you of
possible errors.

## Alarm setup

With CloudWatch logs, you can configure any number of metrics and alarms, depending on your
application and your needs.

Specifically, you can set up proactive alarms for usage alerts directly during your
cluster creation, so that you get notified when errors occur. To highlight errors
in the connection to the AWS Blu Age control system, add a metric concerning the string "Error
C" in the logs. You can then define an alarm that reacts to this metric.
