# Linux Instances

These are the rules to configure for your Linux parent and child domain controllers.

All testing was performed using Amazon Linux. While the dynamic port range for Windows is
49152 to 65535, many Linux kernels use the port range 32768 to 61000. Run the below command to view the IP port range.

`cat /proc/sys/net/ipv4/ip_local_port_range`

## Parent Domain Controller, Linux

| FROM: Parent domain controllers TO: Linux stack and shared services subnets | Source Port   | Destination Port | Protocol                                                                                          |
| --------------------------------------------------------------------------- | ------------- | ---------------- | ------------------------------------------------------------------------------------------------- | ----------- | ---------------- | -------- |
| 389                                                                         | 32768 - 61000 | UDP              |
| 88                                                                          | 32768 - 61000 | TCP              | FROM: Stack subnets, including shared services TO: Linux forest root domain controllers           | Source Port | Destination Port | Protocol |
| ---                                                                         | ---           | ---              |
| 32768 - 61000                                                               | 88            | TCP              |
| 32768 - 61000                                                               | 389           | UDP              | ## Child Domain Controller, Linux FROM: Child domain controllers TO: Linux AWS domain controllers | Source Port | Destination Port | Protocol |
| ---                                                                         | ---           | ---              |
| 49152 - 65535                                                               | 53            | TCP              |
| 49152 - 65535                                                               | 88            | TCP              |
| 389                                                                         | 49152 - 65535 | UDP              |
| 49152 - 65535                                                               | 389           | UDP              | FROM: Child domain controllers TO: Linux stack and shared services subnets                        | Source Port | Destination Port | Protocol |
| ---                                                                         | ---           | ---              |
| 88                                                                          | 32768 - 61000 | TCP              |
| 389                                                                         | 32768 - 61000 | UDP              | FROM: Stack subnets, including shared services TO: Linux child domain controller                  | Source Port | Destination Port | Protocol |
| ---                                                                         | ---           | ---              |
| 32768 - 61000                                                               | 88            | TCP              |
| 32768 - 61000                                                               | 389           | UDP              |
