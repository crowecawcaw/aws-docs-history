# Setting up a SMPTE 2110 input using NMOS

Follow this procedure if you have a SMPTE 2110 source and your organization uses NMOS
IS-04 and IS-05.

###### Note

This section assumes that you have read [Working with SMPTE 2110](SMPTE-ST-2110.md "SMPTE-ST-2110.md") and are
familiar with how SMPTE 2110 works and with its prerequisites.

You must enable NMOS on the appliance, as a one-time action. Then the setup of a SMPTE
2110 source is a two-step process. First, you create a 2110 receiver group to replicate the
SMPTE 2110 receivers in Elemental Live. Then in the event, you create an input that uses the 2110
receiver group. In this way, a SMPTE 2110 source is similar to an SDI source, which is
represented in Elemental Live by an SDI device that is used by an SDI input.

###### Topics

- [Enable NMOS](s2110-nmos-configure.md "s2110-nmos-configure.md")
- [Obtain information from the NMOS
  operator](s2110-nmos-obtain-info.md "s2110-nmos-obtain-info.md")
- [Determine the SDPs to create](s2110-nmos-design-sdps.md "s2110-nmos-design-sdps.md")
- [Create the receiver group](s2110-nmos-create-receiver-group.md "s2110-nmos-create-receiver-group.md")
- [Create a receiver group input](s2110-nmos-create-input.md "s2110-nmos-create-input.md")
- [Choose the resiliency scenario](s2110-nmos-scenarios.md "s2110-nmos-scenarios.md")
- [Resiliency scenario A: Supporting NMOS
  patching](s2110-nmos-scenario-patching.md "s2110-nmos-scenario-patching.md")
- [Resiliency scenario B:
  Supporting NMOS patching and failover](s2110-nmos-scenario-patching-plus-failover.md "s2110-nmos-scenario-patching-plus-failover.md")
- [Resiliency scenario C:
  Supporting NMOS patching and network failover](s2110-nmos-scenario-patching-nw-failover.md "s2110-nmos-scenario-patching-nw-failover.md")
