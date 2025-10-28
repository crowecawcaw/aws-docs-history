# Fraud Protection in AWS End User Messaging SMS

Protect is a set of capabilities that help you to manage SMS message deliveries to all
countries where your customers are located, helping you to combat Artificially Inflated
Traffic (AIT). SMS AIT (or SMS Pumping) occurs when bots target web and mobile applications,
especially workflows that trigger immediate SMS sends like login or sign-up processes.
Protect lets you set rules at the account level, by country, or by use case (such as
transaction alerts vs. authentication). These rules instruct how End User Messaging
evaluates risk and delivers your messages. With SMS Protect, you can set configurations
to:

- Create protect configurations – These are
  containers for your rules, where blocking decisions are made. Create separate
  configurations for different use cases to optimize protection. Set rules at the
  account level or for specific use cases. To apply protect configurations, reference
  them when making API calls by either adding the
  _ProtectConfigurationId_ parameter to
  `SendTextMessage`, `SendMediaMessage`, or
  `SendVoiceMessage` API requests, or by associating it with the SMS
  configuration set you send messages with.
- Set country rules – Within each [protect configuration](protect-configuration.md "protect-configuration.md"), define
  country-specific rules. Choose from:
  - Allow (service default) – Permits all
    messages.
  - Block – Prevents all messages to the
    specified country.
  - Monitor – Allows messages while
    informing you of AIT risk (additional cost applies).
  - Filter – Allows messages but blocks
    those identified by our risk model (additional cost applies).

- Manage phone number exceptions – Use [phone number rule overrides](filter-and-monitor-messages.md "filter-and-monitor-messages.md") to
  create allow exceptions for protect blocked numbers or block specific numbers that
  would otherwise be allowed.
- Implement message feedback – Track customer
  engagement with [message feedback API](message-feedback.md "message-feedback.md"). For
  example, use trackable links to confirm message receipt or monitor usage of one-time
  passwords (OTPs).
- Enable monitoring and alerting – Utilize
  protect [metrics and
  dashboards](filter-and-monitor-messages-monitor.md "filter-and-monitor-messages-monitor.md"), event destinations, and CloudWatch to oversee message AIT risk and
  deliveries.

###### Important

- Messages using “monitor” or “filter” mode incur additional charges for AIT
  risk evaluation. See [pricing for
  details](https://aws.amazon.com/end-user-messaging/pricing/ "https://aws.amazon.com/end-user-messaging/pricing/").
- Protect’s filter and monitor modes use statistical models that generate AIT
  risk predictions based on patterns in data. We are always working to improve
  these models, but as with any such models, the accuracy of their predictions is
  not guaranteed (e.g., there is a chance that legitimate SMS messages may be
  flagged as an AIT risk).
- Filter and monitor modes are designed to help you mitigate the impacts of AIT,
  but do not guarantee complete protection from AIT. We recommend using additional
  safeguards on your web and mobile applications for well- rounded AIT
  protection.

###### Topics

- [Protect configuration](protect-configuration.md "protect-configuration.md")
- [Country rule modes](filter-and-monitor-messages.md "filter-and-monitor-messages.md")
- [View protect
  metrics](filter-and-monitor-messages-monitor.md "filter-and-monitor-messages-monitor.md")
- [Phone number override
  rules](protect-rule-override.md "protect-rule-override.md")
