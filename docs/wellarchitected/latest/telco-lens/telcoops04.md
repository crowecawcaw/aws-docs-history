# IP verification

| TELCOOPS04: How do you represent IP addresses to the internet and verify the<br>quality of the address representation? |
| ---------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                        |

Telco's own large CIDR blocks of IP addresses and wish to have them represented with
their ownership even when advertised by AWS. The IP address CIDR block are assigned to telco
resources in the cloud and should be propagated through AWS to the Internet where both the
CIDR block and the ASN associated with the prefixes are represented as owned by the telco.
This improves the reputation of the address prefix propagated across the Internet for telco
subscribers and gives CSPs responsibility and accountability of the address space.

###### Best practices

- [TELCOOPS04-BP01 Implement the Bring Your Own IP (BYOIP)
  address processes and associate the prefixes with the IPAM solution](telcoops04-bp01.md "telcoops04-bp01.md")
