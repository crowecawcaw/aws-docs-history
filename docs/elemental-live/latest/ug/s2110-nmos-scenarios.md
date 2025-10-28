# Choose the resiliency scenario

You can configure the receiver groups and inputs in an Elemental Live event or Conductor Live profile
to support three scenarios. Note that all of the scenarios include NMOS patching,
because you must always set up inputs for patching.

- [Scenario A](input-2110.md "input-2110.md"): NMOS patching only. With this
  setup, the NMOS controller can send requests to Elemental Live that patch SDP files with
  new content. Elemental Live switches to processing the new content.
- [Scenario B](s2110-nmos-scenario-patching-plus-failover.md "s2110-nmos-scenario-patching-plus-failover.md"):
  NMOS patching with hot backup. This scenario combines the patching from scenario A
  with support for Elemental Live hot backup. Hot backup lets Elemental Live automatically fail over
  from a failed input to another input.
- [Scenario C](s2110-nmos-scenario-patching-nw-failover.md "s2110-nmos-scenario-patching-nw-failover.md"):
  NMOS patching with hot backup and network redundancy. This scenario combines
  scenario A with hot backup and the network redundancy that is set up between the
  upstream system (the content source) and Elemental Live.
