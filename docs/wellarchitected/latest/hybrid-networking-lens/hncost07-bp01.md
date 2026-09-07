

# HNCOST07-BP01 Use dedicated connection for high-volume predictable traffic
<a name="hncost07-bp01"></a>

 Deploy dedicated connection for production workloads requiring consistent, high-bandwidth connectivity between on-premises and cloud environments. Dedicated connection offers lower per-GB costs compared to IPSec VPN and avoids internet variability. 

 **Desired outcome:** Predictable, reduced data transfer costs for mission-critical workloads. 

 **Level of risk exposed if this best practice is not established:** Medium 

 **Benefits of establishing this best practice:** 
+  cost savings versus VPN for high-volume traffic 
+  Improved performance and reliability 

## Implementation guidance
<a name="implementation-guidance-58"></a>
+  Start with low bandwidth dedicated connections and scale up with high bandwidth connections or multiple connections with LAG 

## Resources
<a name="resources-48"></a>
+  [AWS Direct Connect Pricing](https://aws.amazon.com/directconnect/pricing/) 