# Cellular

In addition to the broad use cases mentioned above, there are
a number of considerations to take into account to make an
energy efficient choice for cellular connectivity.  For
devices that communicate using LTE modems, select network
operators that support eDRX (Extended Discontinuous Reception)
and PSM (Power Save Mode).  These are two complementary
features that can be used together to optimize power
consumption in LTE devices.

In PSM, LTE devices enter a low-power sleep mode for extended
periods of time, waking up at pre-defined intervals to
reconnect to the network without a full negotiation, greatly
reducing power consumption. With PSM, while the device is
asleep the radio can be considered to be completely off, in
contrast to eDRX, which continues a paging cycle. This means
that if a page or network-initiated downlink request were to
be made, the device in PSM mode would not receive anything.
This can result in an increased disconnected window compared
to eDRX.

eDRX allows the device to more precisely define the interval
between listening periods, which can reduce power consumption
while still maintaining connectivity. This is useful for
devices that need to remain connected to the network for
longer periods of time, such as mobile devices. This increased
paging window means that latency between a request to the
device is increased but the device is nonetheless available.

 PSM is more power efficient than eDRX.  However, there is an
inflection point at which it may make more sense for a device
to use one versus the other. While building an application you
should test your particular hardware for overall power
consumption during a typical window of sleep and active
states. Use both PSM and eDRX at the predefined eDRX paging
windows and then choose the methodology that best optimizes
your device's power usage during its typical usage.  eDRX is
also a more recent technology and might not be supported by
all network providers.
