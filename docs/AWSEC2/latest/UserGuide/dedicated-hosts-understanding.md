# Amazon EC2 Dedicated Host auto-placement and host affinity

Placement control for Dedicated Hosts happens on both the instance level and host
level.

## Auto-placement

Auto-placement is configured at the host level. It allows you to manage
whether instances that you launch are launched onto a specific host, or onto any
available host that has matching configurations.

When auto-placement is **disabled** for a Dedicated Host, it
accepts only host tenancy instance launches that specify its unique host ID. This
is the default setting for new Dedicated Hosts.

When auto-placement is **enabled** for a Dedicated Host, it
accepts any untargeted, host tenancy instance launches that match its instance
type configuration.

When launching an instance, you need to configure its tenancy. Launching an
instance onto a Dedicated Host without providing a specific `HostId` enables it
to launch on any Dedicated Host that has auto-placement _enabled_ and
that matches its instance type.

## Host affinity

Host affinity is configured at the instance level. It establishes a launch
relationship between an instance and a Dedicated Host.

When affinity is set to `Host`, an instance launched onto a
specific host always restarts on the same host if stopped. This applies to both
targeted and untargeted launches.

When affinity is set to `Default`, and you stop and restart the
instance, it can be restarted on any available host. However, it tries to launch
back onto the last Dedicated Host on which it ran (on a best-effort basis).
