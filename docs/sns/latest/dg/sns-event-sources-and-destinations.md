# Amazon SNS event sources and

destinations

Amazon SNS connects AWS services and external systems by routing event-driven notifications.
Amazon SNS receives events from various AWS services, such as data pipeline updates, Amazon EC2
scaling actions, or security alerts, and publishes these events to Amazon SNS topics. These
topics then send notifications to designated destinations.

Amazon SNS supports two main types of destinations: [Application-to-Application (A2A)](sns-system-to-system-messaging.md "sns-system-to-system-messaging.md") and
[Application-to-Person (A2P)](sns-user-notifications.md "sns-user-notifications.md"). In A2A
messaging, Amazon SNS can send events to Lambda to trigger custom business logic, to Amazon SQS for
queuing messages, and to Amazon Data Firehose for streaming data to storage and analytics
services. For A2P messaging, Amazon SNS can send notifications via SMS, email, and push
notifications to mobile devices, ensuring that users or teams receive timely alerts.

By acting as a central hub, Amazon SNS routes notifications to the right places, helping you
automate and manage your AWS infrastructure more effectively. This setup
allows for seamless integration between services and reliable communication with users and
systems.
