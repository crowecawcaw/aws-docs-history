# Wireless Connectivity

For wireless connectivity there are many design choices that
need to be made. For nearly all cases, the most power
efficient applications are those that minimize the amount of
time that the radio or network interface is on. For example,
an LTE-M module's active transmission mode has thousands of
times higher power consumption than its Power Save Mode (PSM).
Typically, the transmission phase utilizes the most power and
can be particularly penalizing to battery powered devices. 

There are a few best practices applicable to Low Power Wide
Area (LPWA) use cases:

- Reduce the amount of time the radio is on
- Use the appropriate technology for the use case. Using the
  wrong technology type can lead to data retransmission and
  reduced power efficiency
- Reduce the amount of data transmitted
- Use LTE network session resumption mechanisms as much as
  possible to reduce lengthy handshakes
- Use advanced error handling techniques and advanced
  buffering techniques to properly manage degraded network
  conditions
- Optimize application and network settings to improve the
  chances of successful communication
- Monitor your device fleet via network information to
  continuously optimize device applications

Given below are details on specific wireless technologies,
along with guidance from the above list that is specific to
each technology.
