# Regions for MediaPackage

To reduce latency in your applications, MediaPackage offers a regional endpoint for your
requests. To view the list of AWS Regions where MediaPackage is available, see [MediaPackage
Regions](../../../general/latest/gr/mediapackage.md "../../../general/latest/gr/mediapackage.md").

## AWS opt-in Regions

Although most AWS Regions are active by default for your AWS account, certain
Regions are activated only when you manually select them. This document refers to those
Regions as _opt-in Regions_. In contrast, Regions that
are active by default, as soon as your AWS account is created, are referred to as
_commercial Regions_, or simply, _Regions_.

The term _opt-in_ has a historical basis. Any
AWS Regions introduced after March 20, 2019 are considered to be opt-in Regions.
Opt-in Regions have higher security requirements than commercial Regions, regarding the
sharing of IAM data through accounts that are active in opt-in Regions. All of the
data managed through the IAM service is considered identity data, including users,
groups, roles, policies, identity providers, their associated data (for example, X.509
signing certificates or context-specific credentials), and other account-level settings,
such as password policy and the account alias.

You can activate opt-in Regions automatically during channel setup, by selecting
them. Your channel becomes active in all selected Regions.

If you choose to select an opt-in Region as for your MediaPackage resources, enable it
first by following the steps in [Enabling a
Region](../../../general/latest/gr/rande-manage.md#rande-manage-enable "../../../general/latest/gr/rande-manage.md#rande-manage-enable"), when signed in to the AWS Management Console.

MediaPackage is available in the following AWS opt-in Regions:

- Middle East (UAE) Region, me-central-1
- Asia Pacific (Hyderabad) Region, ap-south-2
- Asia Pacific (Melbourne) Region, ap-southeast-4
