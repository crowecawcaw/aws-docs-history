End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Manage IAM Identity Center access of alarm

recipients in AWS IoT Events

AWS IoT Events uses AWS IAM Identity Center to manage the SSO access of alarms recipients. Implementing
IAM Identity Center for AWS IoT Events notification recipients can enhance security and user experience. To
enable the alarm to send notifications to the recipients, you must enable IAM Identity Center and
add recipients to your IAM Identity Center store. For more information, see [Add Users](../../../singlesignon/latest/userguide/addusers.md "../../../singlesignon/latest/userguide/addusers.md") in
_AWS IAM Identity Center User Guide_.

###### Important

- You must choose the same AWS Region for AWS IoT Events, AWS Lambda, and
  IAM Identity Center.
- AWS Organizations only supports one IAM Identity Center Region at a time. If you
  want to make IAM Identity Center available in a different Region, you must first
  delete your current IAM Identity Center configuration. For more information, see
  [IAM Identity Center Region
  Data](../../../singlesignon/latest/userguide/regions.md#region-data "../../../singlesignon/latest/userguide/regions.md#region-data") in _AWS IAM Identity Center User Guide_.
