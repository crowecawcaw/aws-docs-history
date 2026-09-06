

# Resolver endpoint scaling
<a name="best-practices-resolver-endpoint-scaling"></a>

Resolver endpoint security groups use connection tracking to gather information about traffic to and from the endpoints. Each endpoint interface has a maximum number of connections that can be tracked, and a high volume of DNS queries can exceed the connections and cause throttling and query loss. Connection tracking is AWS's default behavior for monitoring the state of traffic flowing through security groups (SGs). Using connection tracking in SGs will reduce the throughput of traffic, however, you can implement untracked connections to reduce overhead and improve performance. For more information see [Untracked connections](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#untracked-connections).

If the connection tracking is enforced either by using restrictive security group rules or queries are routed through Network Load Balancer (see [Automatically tracked connections](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#automatic-tracking)), the overall maximum queries per second per IP address for an endpoint can be as low as 1500.

The following tables list the recommended security group rules for inbound Resolver endpoints.


**Inbound endpoint ingress rules**  

| Protocol type | Port number | Source IP | 
| --- | --- | --- | 
| TCP | 53 | 0.0.0.0/0 | 
| UDP | 53 | 0.0.0.0/0 | 


**Inbound endpoint egress rules**  

| Protocol type | Port number | Destination IP | 
| --- | --- | --- | 
| TCP | All | 0.0.0.0/0 | 
| UDP | All | 0.0.0.0/0 | 

The following tables list the recommended security group rules for outbound Resolver endpoints.


**Outbound endpoint ingress rules**  

| Protocol type | Port number | Source IP | 
| --- | --- | --- | 
| TCP | All | 0.0.0.0/0 | 
| UDP | All | 0.0.0.0/0 | 


**Outbound endpoint egress rules**  

| Protocol type | Port number | Destination IP | 
| --- | --- | --- | 
| TCP | 53 | 0.0.0.0/0 | 
| UDP | 53 | 0.0.0.0/0 | 

**Note**  
**Security group port requirements:**  
**Inbound endpoints** require ingress rules allowing TCP and UDP on port 53 to receive DNS queries from your network. Egress rules can allow all ports since the endpoint might need to respond to queries from various source ports.
**Outbound endpoints** require egress rules allowing TCP and UDP access to the ports you're using for DNS queries on your network. Port 53 is shown in the example above because it's the most common DNS port, but your network might use different ports. Ingress rules can allow all ports to accommodate responses from your DNS servers.

**Inbound Resolver endpoints**

For clients using an inbound resolver endpoint, the capacity of the elastic network interface will be impacted if you have over 40,000 unique IP address and port combinations generating the DNS traffic.