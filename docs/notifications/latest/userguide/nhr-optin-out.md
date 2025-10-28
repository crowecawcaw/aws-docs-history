# Enabling or disabling opt-in Regions in AWS User Notifications

Although most AWS Regions are active by default for your AWS account, certain
Regions are activated only when you manually select them. This document refers to those
Regions as _opt-in Regions_. In contrast, Regions that
are active by default, as soon as your AWS account is created, are referred to as
_commercial Regions_, or simply, _Regions_.

If you choose to select an opt-in Region as your notification hub, enable it first
by following the steps in [Enabling a
Region](../../../general/latest/gr/rande-manage.md#rande-manage-enable "../../../general/latest/gr/rande-manage.md#rande-manage-enable"). Enabling or disabling an opt-in Region may impact your notifications experience. For a list of supported opt-in Regions, see [Opt-in
Regions](supported-regions.md#opt-in-Regions "supported-regions.md#opt-in-Regions").

## Disabling a notification hub Region

You must have a notification hub configured to create notification configurations. If you
disable an opt-in Region that contains your only notification hub, you can't create new notification
configurations. You also can't access previous notifications until you enable the opt-in Region or
create a new notification hub.

### Choosing a notification hub Region that isn't enabled

You must enable an opt-in Region to use a notification hub you create in that opt-in Region. If you
don't enable the opt-in Region, your notification hub remains inactive. You can't create
notification configurations or view notifications until you enable that opt-in Region on your
account or select a new notification hub.
