# Request a quota increase

The Service Quotas console provides information about AWS Control Tower quotas. You can use the
Service Quotas console to view the default service quotas or to [request quota increases](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/controltower/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/controltower/quotas") for adjustable quotas.

###### Note

Newly created accounts and organizations might experience a quota below the default of 10 accounts.

###### The following quotas can be viewed through the Service Quotas console

- _Concurrent account operations quota_ : The maximum number
  of concurrent account operations that can be performed at the same time.
  Default: 5, Maximum: 10, adjustable
- _Number of accounts in a single OU_ : The maximum number of
  AWS Control Tower managed accounts that can be present in one OU. If you add accounts
  beyond this limit, the OU registration process in AWS Control Tower cannot be performed.
  To learn more about the number of accounts per OU, review [Limitations based on underlying AWS
  services](region-stackset-limitations.md "region-stackset-limitations.md") in the AWS Control Tower documentation.
  Default: 1000, not adjustable.
- _Concurrent operations for organizational units (OUs)_ :
  The maximum number of concurrent OU-related operations that can be performed at
  the same time. Default: 1, not adjustable.
  For example, you can request a quota increase from five of up to ten concurrent
  account-related operations. Some AWS Control Tower performance characteristics may change after a
  quota increase. For example, it may take longer to update an OU when you have more
  accounts in it. Or, it may take longer to complete an action on an OU with five SCPs
  than with three SCPs.

###### Note

A service quota increase request may require up to two days before it takes
effect. Be sure to request the quota increase from your AWS Control Tower home Region.

As an alternative, you can contact [AWS Support](https://aws.amazon.com//premiumsupport/ "https://aws.amazon.com//premiumsupport/") to request a quota increase for some resources in AWS Control Tower.
Or you can view the video that follows, and learn how to automate certain service quota
increases.

**Video: Automate requests for service quota increases, in
services related to AWS Control Tower**

This video (7:24) describes how to automate service quota increases for related,
integrated AWS services, based on deployments in AWS Control Tower. It also shows how to
automate enrollment of new accounts into AWS Enterprise support for your organization.
For better viewing, select the icon at the lower right corner of the video to enlarge it
to full screen. Captioning is available.

When provisioning new accounts in this environment, you can use lifecycle events to
trigger automated requests for service quota increases in specified AWS Regions.

More information about AWS quotas is available in the [AWS
General Reference](../../../general/latest/gr/aws_service_limits.md#limits_config "../../../general/latest/gr/aws_service_limits.md#limits_config").
