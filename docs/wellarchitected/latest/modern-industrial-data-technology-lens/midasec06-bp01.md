

# MIDASEC06-BP01 Use secure data exchange protocols
<a name="midasec06-bp01"></a>

 Use secure and standardized protocols for sharing industrial data internally and externally, helping protect integrity and confidentiality. 

 **Desired outcome:** Data is transmitted securely across different systems and organizations without unauthorized interception or tampering. 

 **Benefits of establishing this best practice:** Helps prevent data breaches, supports secure collaboration, and aligns with industry data exchange standards. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance-24"></a>

 Use MQTT over TLS, HTTPS, or OPC-UA with encryption and certificate-based authentication. 

### Implementation steps
<a name="implementation-steps-25"></a>
+  Configure IoT and gateway devices to communicate over secure protocols. 
+  Enforce TLS 1.2 or higher for all data-in-transit. 
+  Implement endpoint authentication using certificates or tokens. 
+  Monitor traffic for anomalies using AWS IoT Device Defender. 

## Resources
<a name="resources-25"></a>
+  [AWS IoT Core protocols ](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html) 
+  [ What is AWS IoT Device Defender? ](https://docs.aws.amazon.com/iot-device-defender/latest/ug/what-is.html) 