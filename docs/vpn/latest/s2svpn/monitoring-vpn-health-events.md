# AWS Health and AWS Site-to-Site VPN events

AWS Site-to-Site VPN automatically sends notifications to the [AWS Health Dashboard](../../../health/latest/ug/aws-health-dashboard-status.md "../../../health/latest/ug/aws-health-dashboard-status.md"). This dashboard
requires no setup, and is ready to use for authenticated AWS users. You can configure
multiple actions in response to event notifications through the AWS Health Dashboard.

The AWS Health Dashboard provides the following types of notifications for your VPN
connections:

- [Tunnel endpoint replacement notifications](#tunnel-replacement-notifications "#tunnel-replacement-notifications")
- [Single tunnel VPN
  notifications](#single-tunnel-notifications "#single-tunnel-notifications")

## Tunnel endpoint replacement notifications

You receive a **Tunnel endpoint replacement
notification** in the AWS Health Dashboard when one or both of the VPN tunnel
endpoints in your VPN connection is replaced. A tunnel endpoint is replaced when AWS
performs tunnel updates, or when you modify your VPN connection. For more
information, see [AWS Site-to-Site VPN tunnel endpoint replacements](endpoint-replacements.md "endpoint-replacements.md").

When a tunnel endpoint replacement is complete, AWS sends the **Tunnel endpoint replacement notification** through a AWS Health Dashboard
event.

## Single tunnel VPN

notifications

A Site-to-Site VPN connection consists of two tunnels for redundancy. We strongly recommend
that you configure both tunnels for high availability. If your VPN connection has
one tunnel up but the other is down for more than one hour in a day, you receive a
_monthly_
**VPN single tunnel notification** through an AWS Health Dashboard
event. This event will be updated daily with any new VPN connections detected as
single tunnel, with notifications sent weekly. A new event will be created each
month, which will clear any VPN connections no longer detected as single
tunnel.
