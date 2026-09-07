

# MIDASEC01-BP06 Establish a communication protocol between IT and OT systems
<a name="midasec01-bp06"></a>

 Define secure communication and data exchange methods between IT and OT environments. Use edge services to control and monitor flows across the boundary and verify that only authorized systems interact. 

 **Desired outcome:** Reduced risk of unintended system access and data leakage between IT and OT, while enabling secure data-driven operations. 

 **Benefits of establishing this best practice:** Promotes security-by-design, improves clarity in responsibility demarcation, and supports long-term scalability and digital transformation. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance-9"></a>

 Establish secure communication patterns between IT and OT networks by defining allowed protocols, data flows, and security controls. 

 Implement edge processing capabilities to manage data exchange, using protocol gateways for format translation and security enforcement. 

 Monitor all cross-boundary communications and implement automated alerts for unauthorized access attempts. This can be achieved using AWS IoT Greengrass and AWS IoT SiteWise for edge management, but the key is maintaining clear security boundaries while enabling necessary operational data flows. 

### Implementation steps
<a name="implementation-steps-10"></a>
+  Use AWS IoT Greengrass to manage and secure data ingestion at the edge. 
+  Define and monitor edge-to-cloud traffic patterns. 
+  Use VPC endpoints and private connectivity where needed for isolation. 
+  Document IT and OT interfaces, protocols, and access policies. 

## Resources
<a name="resources-10"></a>

 **Related documents:** 
+  [ What is AWS IoT Greengrass? ](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-aws-iot-greengrass.html) 
+  [ What is AWS IoT SiteWise? ](https://docs.aws.amazon.com/iotsitewise/latest/userguide/what-is-sitewise.html) 