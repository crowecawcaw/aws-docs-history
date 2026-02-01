# AWS Ground Station Site Capabilities

To simplify your experience, AWS Ground Station determines a common set of capabilities for an antenna
type and then deploys multiple antenna to a ground station location. Part of the onboarding
steps ensures your satellite is compatible with the antenna types at a specific location.
When you reserve a contact, you indirectly determine the antenna type used. This ensures
your experience at a particular ground station location remains the same over time
regardless of which antennas are being used. The specific performance of your contact will
vary due to a wide variety of environmental concerns such as weather at the site.

Currently, all sites support the following capabilities:

###### Note

Each row in the following table indicates an independent communication path, unless
otherwise indicated. Duplicate rows exist to reflect our multi-channel capabilities that
allow multiple communication paths to be used concurrently.

| Capability Type               | Frequency Range    | Bandwidth Range | Polarization | Common Name                             | Notes                                                                                                                                                                                                                                                                                                                        |
| ----------------------------- | ------------------ | --------------- | ------------ | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| antenna-downlink              | 7750<br>• 8500 MHz | 50<br>• 400 MHz | RHCP         | X-band wideband downlink                | This capability requires the use of the [AWS Ground Station Agent](../gs-agent-ug.md "../gs-agent-ug.md").<br>This capability is not supported in Alaska 1 or Punta Arenas 1.<br>The aggregate bandwidth must not exceed 400MHz per polarization at each location.<br>All utilized frequency ranges must be non-overlapping. |
| antenna-downlink              | 7750<br>• 8500 MHz | 50<br>• 400 MHz | RHCP         |
| antenna-downlink              | 7750<br>• 8500 MHz | 50<br>• 400 MHz | RHCP         |
| antenna-downlink              | 7750<br>• 8500 MHz | 50<br>• 400 MHz | RHCP         |
| antenna-downlink              | 7750<br>• 8500 MHz | 50<br>• 400 MHz | RHCP         |
| antenna-downlink              | 7750<br>• 8500 MHz | 50<br>• 400 MHz | LHCP         |
| antenna-downlink              | 7750<br>• 8500 MHz | 50<br>• 400 MHz | LHCP         |
| antenna-downlink              | 7750<br>• 8500 MHz | 50<br>• 400 MHz | LHCP         |
| antenna-downlink              | 7750<br>• 8500 MHz | 50<br>• 400 MHz | LHCP         |
| antenna-downlink              | 7750<br>• 8500 MHz | 50<br>• 400 MHz | LHCP         |
| antenna-downlink              | 2200<br>• 2290 MHz | Up to 40 MHz    | RHCP         | S-band downlink                         | Only one polarization can be used at a time                                                                                                                                                                                                                                                                                  |
| antenna-downlink              | 2200<br>• 2290 MHz | Up to 40 MHz    | LHCP         |
| antenna-downlink              | 7750<br>• 8500 MHz | Up to 40 MHz    | RHCP         | X-band narrowband downlink              | Only one polarization can be used at a time                                                                                                                                                                                                                                                                                  |
| antenna-downlink              | 7750<br>• 8500 MHz | Up to 40 MHz    | LHCP         |
| antenna-uplink                | 2025<br>• 2110 MHz | Up to 40 MHz    | RHCP         | S-band uplink                           | Only one polarization can be used at a time<br>EIRP 20-50 dBW                                                                                                                                                                                                                                                                |
| antenna-uplink                | 2025<br>• 2110 MHz | Up to 40 MHz    | LHCP         |
| antenna-uplink-echo           | 2025<br>• 2110 MHz | 2 MHz           | RHCP         | Uplink echo                             | Matches antenna-uplink restrictions                                                                                                                                                                                                                                                                                          |
| antenna-uplink-echo           | 2025<br>• 2110 MHz | 2 MHz           | LHCP         |
| antenna-downlink-demod-decode | 7750<br>• 8500 MHz | Up to 500 MHz   | RHCP         | X-band demodulated and decoded downlink |                                                                                                                                                                                                                                                                                                                              |
| antenna-downlink-demod-decode | 7750<br>• 8500 MHz | Up to 500 MHz   | LHCP         |                                         |
| tracking                      | N/A                | N/A             | N/A          | N/A                                     | Support for auto-tracking and program tracking                                                                                                                                                                                                                                                                               |

\* RHCP = right-handed circular polarization, and LHCP = left-handed circular polarization. For more information on polarization, see [Circular polarization](https://en.wikipedia.org/wiki/Circular_polarization "https://en.wikipedia.org/wiki/Circular_polarization").
