

# MIDASEC01-BP03 Secure machine-to-machine and human-to-machine access
<a name="midasec01-bp03"></a>

 Help protect communication between devices and systems in industrial settings by securing machine-to-machine (M2M) and human-to-machine (H2M) access using authentication, authorization, and encryption methods tailored to industrial protocols and devices. 

 **Desired outcome:** Avoid unauthorized access to industrial devices and trace actions across automation systems. 

 **Benefits of establishing this best practice:** Reduces the scope of impact, improves system integrity, and provides operational visibility for audit and compliance. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance-6"></a>

 Use X.509 certificates for M2M identity, IoT policies for access control, and managed bastion solutions like AWS Systems Manager Session Manager for H2M. 

### Implementation steps
<a name="implementation-steps-7"></a>
+  Provision devices with unique X.509 certificates using AWS IoT Core. 
+  Define and enforce AWS IoT policies for device communication. 
+  Use AWS Systems Manager Session Manager for secure remote access to edge and OT assets. 
+  Monitor access using AWS CloudTrail and AWS IoT Device Defender. 

## Resources
<a name="resources-7"></a>

 **Related documents:** 

 [Iot Security Best Practices](https://docs.aws.amazon.com/iot/latest/developerguide/iot-security-best-practices.html) 

 [Session Manager Userguide](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) 