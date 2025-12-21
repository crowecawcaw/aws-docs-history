# Zonal shift in ARC

Amazon Application Recovery Controller (ARC) _zonal shift_ allows you to shift traffic for a
supported resource away from an impaired Availability Zone (AZ) in an AWS Region to
healthy AZs in the same Region. Shifting your resource's traffic away from an impaired AZ
reduces the duration and severity of impact caused by power outages, or hardware or software
issues in an AZ, and helps to mitigate issues and quickly recover your application. You
might choose to shift traffic, for example, because a bad deployment is causing latency
issues, or because the Availability Zone is impaired.

You must opt-in resources in order to use zonal shift. For more information, refer to [Supported resources](arc-zonal-shift.md "arc-zonal-shift.md").

Before you start a zonal shift, you must prescale your application and ensure that you
have sufficient capacity to shift traffic away from an Availability Zone. After prescaling,
you can choose the Availability Zone to shift away from and the resource to shift traffic
away for, and then start the zonal shift. You can cancel the shift at any time to have
traffic begin returning to the original Availability Zone. For more information, see [Best practices for zonal shifts in ARC](route53-arc-best-practices.md "route53-arc-best-practices.md")

All zonal shifts are temporary mitigations. You set an initial expiration when you start a
zonal shift, from one minute up to three days (72 hours), which you can extend, if you need
to continue the traffic shift.

In specific scenarios, zonal shift does not shift traffic away from the AZ. For more
information, see [Supported resources](arc-zonal-shift.md "arc-zonal-shift.md").
