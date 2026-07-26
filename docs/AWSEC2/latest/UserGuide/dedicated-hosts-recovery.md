# Amazon EC2 Dedicated Host recovery

Dedicated Host auto recovery restarts your instances on to a new replacement host when certain
problematic conditions are detected on your Dedicated Host. Host recovery reduces the need for
manual intervention and lowers the operational burden if there is an unexpected Dedicated Host
failure concerning system power or network connectivity events. Other Dedicated Host issues will
require manual intervention to recover from.

###### Contents

- [How host recovery works](dedicated-hosts-recovery-basics.md "dedicated-hosts-recovery-basics.md")
- [Supported instance types](#dedicated-hosts-recovery-instances "#dedicated-hosts-recovery-instances")
- [Pricing](#dedicated-hosts-recovery-pricing "#dedicated-hosts-recovery-pricing")
- [Manage host recovery](dedicated-hosts-recovery-enable.md "dedicated-hosts-recovery-enable.md")
- [View host recovery setting](dedicated-hosts-recovery-view.md "dedicated-hosts-recovery-view.md")
- [Manually recovery unsupported instances](dedicated-hosts-recovery-unsupported.md "dedicated-hosts-recovery-unsupported.md")

## Supported instance types

Host recovery is supported for the following instance families:

- **General purpose:** A1 | M3 | M4 | M5 | M5n | M5zn | M6a | M6g | M6i | T3 | Mac1 | Mac2 | Mac2-m1ultra | Mac2-m2 | Mac2-m2pro | M6in | M7a | M7g | M7i | M8a | M8g | M8gb | M8gn | M8i | M8in | M8ib | M9g | Mac-m4 | Mac-m4pro | Mac-m4max | Mac-m3ultra
- **Compute optimized:** C3 | C4 | C5 | C5n | C6a | C6g | C6i | C6gn | C6in | C7a | C7g | C7gn | C7i | C8a | C8g | C8gb | C8gn | C8i | C8in | C8ib | C9g
- **Memory optimized:** R3 | R4 | R5 | R5b | R5n | R6g | R6i | U-6tb1 | U-9tb1 | U-12tb1 | U-18tb1 | U-24tb1 | X1 | X1e | X2iezn | R6a | R6in | R7a | R7g | R7i | R7iz | R8a | R8g | R8gb | R8gn | R8i | R8in | R8ib | X8g | X8i | U7i-6tb | U7i-8tb | U7i-12tb | U7in-16tb | U7in-24tb | U7in-32tb
- **Accelerated computing:** Inf1 | G3 | G5g | P3

To recover instances that are not supported, see [Manually recover instances that are not supported by Amazon EC2 Dedicated Host recovery](dedicated-hosts-recovery-unsupported.md "dedicated-hosts-recovery-unsupported.md").

###### Note

Dedicated Host auto recovery of supported metal instance types
will take longer to detect and recover from than non-metal instance
types.

## Pricing

There are no additional charges for using host recovery, but the usual Dedicated Host
charges apply. For more information, see [Amazon EC2 Dedicated Hosts
Pricing](https://aws.amazon.com/ec2/dedicated-hosts/pricing/ "https://aws.amazon.com/ec2/dedicated-hosts/pricing/").

As soon as host recovery is initiated, you are no longer billed for the impaired
Dedicated Host. Billing for the replacement Dedicated Host begins only after it enters the
`available` state.

If the impaired Dedicated Host was billed using the On-Demand rate, the replacement Dedicated Host is
also billed using the On-Demand rate. If the impaired Dedicated Host had an active Dedicated Host Reservation, it
is transferred to the replacement Dedicated Host.
