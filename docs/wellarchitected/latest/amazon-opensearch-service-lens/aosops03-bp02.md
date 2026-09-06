

# AOSOPS03-BP02 Configure notification services to receive monitoring alerts
<a name="aosops03-bp02"></a>

 Connect monitoring alerts to your messaging infrastructure to stay informed about domain changes and potential issues. 

 **Level of risk exposed if this best practice is not established:** High 

 **Desired outcome**: Alert notifications from monitoring systems are integrated with messaging infrastructure, enabling timely response to issues. 

 **Benefits of establishing this best practice:** 
+  Improved ability to stay on top of changes and potential issues 
+  Enhanced visibility into domain performance, security, and compliance 

## Implementation guidance
<a name="implementation-guidance-6"></a>

 Amazon SNS provides a built-in integration with Amazon CloudWatch to receive notifications when an alarm breaches a threshold. You can receive notifications for events through multiple channels, including email, [Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) chat notifications, or [AWS Management Console Mobile Application push notifications](https://docs.aws.amazon.com/consolemobileapp/latest/userguide/managing-notifications.html). 

 To set up essential Amazon CloudWatch alarms for your OpenSearch Service domain, follow [AOSOPS03-BP01](aosops03-bp01.md) and [Notifying users on alarm changes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Notify_Users_Alarm_Changes.html). 

## Resources
<a name="resources-6"></a>
+  [Notifying users on alarm changes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Notify_Users_Alarm_Changes.html) 