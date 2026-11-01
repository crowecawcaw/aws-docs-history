

# Monitoring License Manager with Amazon EventBridge
<a name="monitoring-eventbridge"></a>

When a license or grant changes state, AWS License Manager (License Manager) sends an event to Amazon EventBridge. EventBridge lets you act on system events, such as resource changes, and automate your AWS services. You write rules that specify which events interest you. Each rule also defines the actions to take when an event matches the rule. For example, you can start workflows, send notifications, or keep an audit trail of license and grant changes. You don't need to poll the License Manager API.

To learn where a rule can send events, see [Event bus targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html) in the *Amazon EventBridge User Guide*.

License Manager sends events to the default event bus in the home AWS Region of the license or grant. For the full list of License Manager events, see [AWS License Manager events](https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-license-manager.html) in the *AWS Events Reference*.