# AOSOPS03-BP02 Configure notification services to receive

monitoring alerts

Connect monitoring alerts to your messaging infrastructure to stay
informed about domain changes and potential issues.

**Level of risk exposed if this best practice
is not established:** High

**Desired outcome**: Alert
notifications from monitoring systems are integrated with messaging
infrastructure, enabling timely response to issues.

**Benefits of establishing this best
practice:**

- Improved ability to stay on top of changes and potential issues
- Enhanced visibility into domain performance, security, and
  compliance

## Implementation guidance

Amazon SNS provides a built-in integration with Amazon CloudWatch
to receive notifications when an alarm breaches a threshold. You
can receive notifications for events through multiple channels,
including email,
[Amazon Q Developer in chat applications](../../../chatbot/latest/adminguide/what-is.md "../../../chatbot/latest/adminguide/what-is.md") chat notifications, or
[AWS Management Console Mobile Application push notifications](../../../consolemobileapp/latest/userguide/managing-notifications.md "../../../consolemobileapp/latest/userguide/managing-notifications.md").

To set up essential Amazon CloudWatch alarms for your OpenSearch Service domain, follow [AOSOPS03-BP01](aosops03-bp01.md "aosops03-bp01.md") and
[Notifying
users on alarm changes](../../../AmazonCloudWatch/latest/monitoring/Notify_Users_Alarm_Changes.md "../../../AmazonCloudWatch/latest/monitoring/Notify_Users_Alarm_Changes.md").

## Resources

- [Notifying
  users on alarm changes](../../../AmazonCloudWatch/latest/monitoring/Notify_Users_Alarm_Changes.md "../../../AmazonCloudWatch/latest/monitoring/Notify_Users_Alarm_Changes.md")
