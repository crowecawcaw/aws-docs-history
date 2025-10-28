# Best practices for Amazon Location Service

This topic provides best practices to help you use Amazon Location Service. While these best practices can
help you take full advantage of the Amazon Location Service, they do not represent a complete solution. You
should follow only the recommendations that are applicable for your environment.

###### Topics

- [Security](#security-best-practice "#security-best-practice")

## Security

To help manage or even avoid security risks, consider the following best practices:

- Use identity federation and IAM roles to manage, control, or limit access to your
  Amazon Location resources. For more information, see [IAM Best Practices](../../../IAM/latest/UserGuide/IAMBestPractices.md "../../../IAM/latest/UserGuide/IAMBestPractices.md")
  in the _IAM User Guide_.
- Follow the Principle of Least Privilege to grant only the minimum required access to
  your Amazon Location Service resources.
- For Amazon Location Service resources used in web applications, restrict access using an
  `aws:referer` IAM condition, limiting use by sites other than
  those included in the allow-list.
- Use monitoring and logging tools to track resource access and usage. For more
  information, see [Logging and Monitoring in
  Amazon Location Service](security-logging-and-monitoring.md "security-logging-and-monitoring.md") and [Logging Data Events for Trails](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md") in the AWS CloudTrail User Guide.
- Use secure connections, such as those that begin with `https://` to add
  security and protect users against attacks while data is being transmitted between the
  server and browser.

### Detective security best practices for

Amazon Location Service

The following best practices for Amazon Location Service can help detect security incidents:

**Implement AWS monitoring tools**

Monitoring is critical to incident response and maintains the reliability and
security of Amazon Location Service resources and your solutions. You can implement monitoring
tools from the several tools and services available through AWS to monitor your
resources and your other AWS services.

For example, Amazon CloudWatch allows you to monitor metrics for Amazon Location Service and enables
you to setup alarms to notify you if a metric meets certain conditions you've set
and has reached a threshold you've defined. When you create an alarm, you can set
CloudWatch to sent a notification to alert using Amazon Simple Notification Service. For more information, see
[Logging and Monitoring in
Amazon Location Service](security-logging-and-monitoring.md "security-logging-and-monitoring.md").

**Enable AWS logging tools**

Logging provides a record of actions taken by a user, role or an AWS service in
Amazon Location Service. You can implement logging tools such as AWS CloudTrail to collect data on
actions to detect unusual API activity.

When you create a trail, you can configure CloudTrail to log events. Events are
records of resource operations performed on or within a resource such as the
request made to Amazon Location, the IP address from which the request was made, who
made the request, when the request was made, along with additional data. For more
information, see [Logging Data Events for Trails](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md") in the AWS CloudTrail User Guide.

### Preventive security best practices for

Amazon Location Service

The following best practices for Amazon Location Service can help prevent security incidents:

**Use secure connections**

Always use encrypted connections, such as those that begin with
`https://` to keep sensitive information secure in transit.

**Implement least privilege access to
resources**

When you create custom policies to Amazon Location resources, grant only the
permissions required to perform a task. It's recommended to start with a minimum
set of permissions and grant additional permissions as needed. Implementing least
privilege access is essential to reducing the risk and impact that could result
from errors or malicious attacks. For more information, see [Use AWS Identity and Access Management to authenticate](security-iam.md "security-iam.md").

**Use globally-unique IDs as device IDs**

Use the following conventions for device IDs.

- Device IDs must be unique.
- Device IDs should not be secret, because they can be used as foreign keys
  to other systems.
- Device IDs should not contain personally-identifiable information (PII),
  such as phone device IDs or email addresses.
- Device IDs should not be predictable. Opaque identifiers like UUIDs are
  recommended.

**Do not include PII in device position properties**

When sending device updates (for example, using [DevicePositionUpdate](../APIReference/API_DevicePositionUpdate.md "../APIReference/API_DevicePositionUpdate.md")), do not include personally-identifiable
information (PII) such as phone number or email address in the
`PositionProperties`.
