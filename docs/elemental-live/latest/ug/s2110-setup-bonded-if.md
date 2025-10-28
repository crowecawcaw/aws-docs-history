# Setup: Remove bonded

interfaces

Read this section if you plan to implement redundant inputs and/or outputs with SMPTE 2110.

SMPTE 2110 inputs and outputs support resiliency, but they do so using SMPTE 2022-7. You
can’t implement input resiliency by bonding the two interfaces on the appliance. This
resiliency implementation has the following impact:

- If you currently have a bonded interface on the appliance (on a Mellanox card or
  on a 25Gb card), you must remove the bond.
- In addition, if you have non-SMPTE 2110 (or non-SMPTE 2022-6) events set up on the
  appliance that use this bonded interface, you must modify the event configuration.
  You might be able to bond other interfaces on other cards in the appliance, and then
  use that bonded interface in those events. If you can’t do that, you must change the
  event configuration to not use a bonded interface.
  If you don't plan to implement redundant SMPTE 2110 inputs or outputs (or SMPTE 2022-6
  inputs), you can retain the bonded interface on the appliance.
