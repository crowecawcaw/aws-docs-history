# Comparing Amazon EBS volume types gp2

and gp3

Here is a comparison of cost between gp2 and gp3 volumes in the US East (N. Virginia)
Region. For the most up to date information, see the [Amazon EBS General Purpose Volumes](https://aws.amazon.com/ebs/general-purpose/ "https://aws.amazon.com/ebs/general-purpose/") product page and
the [Amazon EBS Pricing Page](https://aws.amazon.com/ebs/pricing/ "https://aws.amazon.com/ebs/pricing/").

| Volume type                     | gp3                                                                                                                                                | gp2                                                                                                                       |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Volume size**                 | 1 GiB – 16 TiB                                                                                                                                     | 1 GiB – 16 TiB                                                                                                            |
| **Default/Baseline IOPS**       | 3000                                                                                                                                               | 3 IOPS/GiB (minimum 100 IOPS) to a maximum of 16,000 IOPS. Volumes<br>smaller than 1 TiB can also burst up to 3,000 IOPS. |
| **Max IOPS/volume**             | 16,000                                                                                                                                             | 16,000                                                                                                                    |
| **Default/Baseline throughput** | 125 MiB/s                                                                                                                                          | Throughput limit is between 128 MiB/s and 250 MiB/s, depending on the<br>volume size.                                     |
| **Max throughput/volume**       | 1,000 MiB/s                                                                                                                                        | 250 MiB/s                                                                                                                 |
| **Price**                       | $0.08/GiB-month 3,000 IOPS free and $0.005/provisioned IOPS-month<br>over 3,000; 125 MiB/s free and $0.04/provisioned MiB/s-month over<br>125MiB/s | $0.10/GiB-month                                                                                                           |
