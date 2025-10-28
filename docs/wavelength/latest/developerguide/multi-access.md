# Multi-access AWS Wavelength

TCP, UDP, and ICMP traffic from the device on the carrier network to an Amazon EC2 instance in
the Wavelength Zone is supported. However, when a mobile subscriber connects to an external,
non-cellular network offered by the communications service provider (CSP), such as a WiFi
network, traffic is denied for most partners because traffic is characterized as _internet
facing_.

With the proliferation of high-speed 5G networks, CSPs now offer new connectivity
solutions to residential, small-business, and enterprise customers such as Fixed Wireless Access (FWA).

The following CSP partners that offer AWS Wavelength Zones have expanded the available ingress
traffic flows:

| Communication service provider | Ingress from outside the carrier network | Ingress from 4G/5G-connected device | Ingress from Fixed Wireless Access |
| ------------------------------ | ---------------------------------------- | ----------------------------------- | ---------------------------------- |
| Orange                         | Yes                                      | Yes                                 | Yes                                |
| Verizon                        | No                                       | Yes                                 | Yes                                |
| Vodafone                       | No                                       | Yes                                 | No                                 |
