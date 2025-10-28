# EUCSUS04-BP01

Implement a scaling methodology in AppStream 2.0

Scaling policies improve resource utilization and cost
management for application streaming workloads.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Either fleet type (On-Demand or Always-On) requires a
methodology to verify that the appropriate number of instances
are available when users initiate a connection. 

A combination of step scaling, scheduled scaling, or target
tracking scaling is recommended to match each fleet usage. To
avoid extra consumption of instances, monitor your fleet usage
and modify your scaling policies accordingly. The following
resources describe in further detail the differences between
the types of scaling and how to configure them to align with
the pattern of usage for the applications being delivered.
Keep in mind that the fleet type choice is only available
during the fleet creation process. 

- [AppStream 2.0 Fleet Types](../../../appstream2/latest/developerguide/fleet-type.md "../../../appstream2/latest/developerguide/fleet-type.md")
- [Fleet Auto Scaling for Amazon AppStream 2.0](../../../appstream2/latest/developerguide/autoscaling.md "../../../appstream2/latest/developerguide/autoscaling.md")
- [Scaling Your Desktop Application Streams with Amazon AppStream 2.0](https://aws.amazon.com/blogs/compute/scaling-your-desktop-application-streams-with-amazon-appstream-2-0/ "https://aws.amazon.com/blogs/compute/scaling-your-desktop-application-streams-with-amazon-appstream-2-0/")
- [Scale your Amazon AppStream 2.0 fleets](https://aws.amazon.com/blogs/desktop-and-application-streaming/scale-your-amazon-appstream-2-0-fleets/ "https://aws.amazon.com/blogs/desktop-and-application-streaming/scale-your-amazon-appstream-2-0-fleets/")
- [Monitoring Amazon AppStream 2.0 Resources](../../../appstream2/latest/developerguide/monitoring.md "../../../appstream2/latest/developerguide/monitoring.md")
