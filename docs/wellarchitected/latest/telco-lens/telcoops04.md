

# IP address representation and management
<a name="telcoops04"></a>


|  TELCOOPS04: How do you represent IP addresses to the internet and verify the quality of the address representation?  | 
| --- | 
| [TELCOOPS04-BP01 Manage User Equipment (UE) IP address pools using cloud-based IPAM integrated with 5G core network functions](telcoops04-bp01.md) | 

 Operators own large CIDR blocks of public IP addresses and need those blocks to be represented under their own ownership even when the traffic is advertised from the cloud. When operator prefixes and their associated autonomous system number (ASN) are represented as operator-owned, the address space keeps its reputation across the internet and the operator retains accountability for it. Separately, subscriber traffic uses internal user equipment (UE) address pools that the mobile core manages and that must coexist with cloud infrastructure addressing. 

 This capability covers how the operator's address space is represented and managed in the cloud across both of these domains: public prefix representation and reputation, and the internal UE pool addressing that has to route correctly without colliding with VPC ranges. 