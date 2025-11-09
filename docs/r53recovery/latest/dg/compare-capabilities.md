# Compare multi-AZ and multi-Region recovery capabilities in ARC

Zonal shift, zonal autoshift, routing control, and Region switch in Amazon Application Recovery Controller (ARC) can all achieve rapid
recovery and help you to ensure resilience for your AWS applications. These features are
highly available, and help support recovery in scenarios when your application is
experiencing increased latency or reduced availability. These features also help recover
applications quickly by shifting traffic away from isolated impairments, which limits the
impact and time lost from impairments.

Routing control and Region switch are focused on AWS applications that are in multiple
AWS Regions (multi-Region), while zonal shift and zonal autoshift only support shifting traffic
for supported resources with multi-AZ applications.

The information in the following table includes some of the key features of the ARC
resilience capabilities. These descriptions can help you better understand how
a specific option might be the best choice for your application's needs.

| Routing control                                                             | Region switch                                                               | Zonal shift                                                                                                                                                            | Zonal autoshift                                                                                                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Regional**<br>Reroutes traffic from one AWS Region to another (primarily) | **Regional**<br>Reroutes traffic from one AWS Region to another (primarily) | **Zonal**<br>Shifts traffic away from an Availability Zone<br>Traffic goes to other Availability Zones in the Region, not to a specific target                         | **Zonal**<br>Shifts traffic away from an Availability Zone<br>Traffic goes to other Availability Zones in the Region, not to a specific target                  |
| **Requires setup**<br>Requires configuration and setup                      | **Requires setup**<br>Requires configuration and setup                      | **May require setup**<br>Requires opt-in for some supported resources<br>For more information, refer to [Supported resources](arc-zonal-shift.md "arc-zonal-shift.md") | **Requires setup**<br>Must be enabled for a supported resource<br>For more information, refer to [Supported resources](arc-zonal-shift.md "arc-zonal-shift.md") |
| **Customer-initiated**<br>Customer determines when to re-route traffic      | **Customer-initiated**<br>Customer determines when to re-route traffic      | **Customer-initiated**<br>Customer determines when to start a zonal shift                                                                                              | **AWS-initiated**<br>AWS shifts application traffic away from an AZ on your behalf                                                                              |
| **Fee-based**<br>Requires separate charges for routing control              | **Fee-based**<br>Requires separate charges for Region switch plans          | **Included with services (no additional charge)**<br>Creating zonal shifts to move traffic away from AZs is included for supported<br>resources                        | **Included with services (no additional charge)**<br>Starting autoshifts to move traffic away from AZs on your behalf is included for<br>supported resources    |
| **Does not expire**<br>Traffic can be rerouted to a replica indefinitely    | **Does not expire**<br>Application can be shifted to a replica indefinitely | **Temporary**<br>All zonal shifts must be set to expire                                                                                                                | **Temporary**<br>AWS starts and ends autoshifts                                                                                                                 |

To learn more about each of these features, see the following chapters:

- [Zonal shift in ARC](arc-zonal-shift.md "arc-zonal-shift.md")
- [Zonal autoshift in ARC](arc-zonal-shift.md "arc-zonal-shift.md")
- [Routing control in ARC](routing-control.md "routing-control.md")
- [Region switch in ARC](region-switch.md "region-switch.md")
