# Manage Linux subscriptions in License Manager

With AWS License Manager, you can view and manage commercial Linux subscriptions that your Amazon EC2
instances use. You can track utilization of your Linux subscriptions for the AWS Regions
and accounts in AWS Organizations that you've defined in your settings. License Manager gives you a comprehensive
view of your running instances that use Linux subscriptions. It also indicates when an instance
has more than one subscription defined.

The data that License Manager discovers is aggregated and displayed in the License Manager console and
in the Amazon CloudWatch dashboard. You can also access your subscription data through the
AWS CLI and the License Manager Linux subscription API or associated SDKs.

Linux license subscriptions can come from the following sources:

###### Subscription-included AMIs

- Red Hat Enterprise Linux (RHEL)
- RHEL Bring Your Own Subscription model (BYOS) with the Red Hat Cloud Access Program
- SUSE Linux Enterprise Server
- Ubuntu Pro subscription-included AMI

###### Third-party subscription providers

- RHEL subscription from Red Hat Subscription Manager (RHSM)
  Linux subscription discovery uses the eventual consistency model. A consistency model determines the
  manner and timing in which data is loaded and presented in your Linux subscriptions view. With
  this model, License Manager ensures that your Linux subscription data is updated periodically from
  your resources. In the event that some data is not ingested during these intervals, the
  information is delivered at the next metric emission. This behavior can delay resources,
  such as newly launched EC2 commercial Linux instances, from displaying in the Linux
  subscriptions dashboard.

###### Note

It can take up to 36 hours for the initial resource discovery to complete, and up to 12
hours for newly launched instances to be discovered and reported. Once your resources are
discovered, Amazon CloudWatch metrics are emitted hourly for Linux subscriptions data.

If your accounts are in AWS Organizations, you can register a member account as the delegated
administrator. For more information, see [Delegated administrator settings in License Manager](delegated-administrator.md "delegated-administrator.md").

###### Duplicate subscriptions detected

When License Manager detects two Linux subscriptions on the same EC2 instance, it sets the
duplicate subscription alert. You can view and filter Linux subscription data from the
**Instances** page in the License Manager console.

**Red Hat Enterprise Linux 7 Extended Lifecycle Support (RHEL 7 ELS)
instances:** When you launch an instance from a subscription-included AMI for
RHEL 7 ELS, you should still register your instance with Red Hat and consume an entitlement.
In this case, License Manager reports a duplicate subscription, but that's the expected behavior.

**Other Red Hat Linux instances:** We recommend that
you search the subscription inventory in the [Red Hat
Hybrid Cloud Console](https://console.redhat.com/ "https://console.redhat.com/") to find out which subscriptions your instance consumes.

###### Additional topics

- [Configure Linux subscription
  discovery in License Manager](linux-subscriptions-manage-discovery.md "linux-subscriptions-manage-discovery.md")
- [View discovered instance data in
  License Manager](linux-subscriptions-instances-view.md "linux-subscriptions-instances-view.md")
- [Billing information for Linux
  subscriptions in License Manager](linux-subscriptions-billing-information.md "linux-subscriptions-billing-information.md")
- [Manage Amazon CloudWatch alarms for Linux
  subscriptions in License Manager](linux-subscriptions-usage-alarms.md "linux-subscriptions-usage-alarms.md")
