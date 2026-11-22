

# TELCOPERF03-BP03 Implement network timing synchronization using dedicated timing infrastructure alongside cloud compute

 RAN and transport functions require nanosecond-level frequency and phase synchronization from IEEE 1588 Precision Time Protocol (PTP) or Synchronous Ethernet (SyncE), delivered by dedicated timing infrastructure such as GNSS receivers and PTP grandmasters. Cloud compute consumes this timing; it doesn't provide it. This best practice plans the timing infrastructure as a separate layer that feeds the compute environment. **Desired outcome:** 
+  RAN timing uses dedicated GNSS receivers and PTP grandmasters at cell sites or aggregation points, distributing timing through IEEE 1588 telecom profiles. 
+  Cloud compute running Distributed Unit (DU) software receives timing from the site's PTP infrastructure through its network interfaces, not from a cloud time service. 
+  Timing accuracy is monitored, with alarms that trigger before degradation reaches levels that affect radio performance. 

 **Common anti-patterns:** 
+  Expecting Outposts or EC2 instances to act as PTP grandmasters or distribute telecom-grade IEEE 1588 timing to radio equipment. 
+  Confusing an application-level time service with telecom-grade timing distribution for radio frequency and phase synchronization. 
+  Not planning dedicated timing infrastructure as part of site design, then finding at deployment that the compute environment can't provide the timing the RAN requires. 
+  Monitoring timing only at the grandmaster and not at the DU, so drift at the consuming function goes unseen. 

 **Benefits of establishing this best practice:** 
+  Timing accuracy meets 3GPP and ITU-T requirements for the deployed radio technology. 
+  The boundary between operator-owned timing infrastructure and cloud compute is well defined, with documented interfaces. 
+  Holdover behavior for GNSS outages is specified and tested, with monitoring that detects degradation before it affects subscribers. 
+  Radio synchronization is correct because timing comes from a compliant telecom source rather than an application clock. 

 **Level of risk exposed if this best practice is not established:** High \#\# Implementation guidance Timing in a telco network is a physical-layer concern that exists independently of the compute environment, and the single most important thing to internalize is that the cloud doesn't provide it. A 5G gNB needs phase synchronization accurate to around 1.5 microseconds or tighter, and that timing originates from GNSS satellites, is received by a site antenna and receiver, and is distributed through a chain of PTP grandmasters and boundary clocks to the radio units and DU compute. When the DU runs on an Outpost, the Outpost supplies compute, storage, and networking, and the DU receives PTP timing through a network interface from the site's timing infrastructure exactly as it would on any other server. 

 The confusion this best practice guards against is between application-grade and radio-grade timing. Cloud time services, including the PTP hardware clock available on some instances, provide microsecond-accurate wall-clock time suitable for event ordering, log correlation, and control-plane timestamping. That isn't the same as the nanosecond-accurate, telecom-profile-compliant timing that radio synchronization demands, and treating one as a substitute for the other produces a deployment that appears timed but fails radio compliance. The two serve different domains and should be kept distinct: the radio timing domain fed by dedicated infrastructure, and the operational timing domain fed by the cloud time service. 

 The practical consequence for site design is a separate workstream. The timing infrastructure (GNSS antenna, PTP grandmaster, boundary clocks, cabling) must be planned, procured, and installed independently of the compute, and the two connect at the DU's PTP client port. Monitoring must sit at the DU, not only at the grandmaster, so drift at the point of consumption is caught, and holdover behavior for GNSS loss must be specified and tested. \#\#\# Implementation steps 
+  Define timing requirements per radio technology: document the phase accuracy, frequency accuracy, and holdover requirements for your deployed radio technology, referencing the relevant ITU-T and 3GPP specifications. 
+  Design the site timing architecture independently: plan GNSS antenna placement, PTP grandmaster location, boundary-clock topology, and cabling as a dedicated infrastructure layer that connects to the DU compute at a defined interface. 
+  Configure DU compute as a timing consumer: configure the DU's PTP client to synchronize from the site grandmaster through the appropriate network interface, and don't use the cloud PTP clock for radio synchronization. 
+  Use the cloud time service for non-radio timing: configure control-plane applications, logging, and orchestration to use the Amazon Time Sync Service for operational timestamps, separate from the radio timing domain. 
+  Monitor accuracy and holdover: monitor PTP time error and frequency offset at the DU with alarms below the compliance limit, and alert on loss of GNSS lock to signal entry into holdover. \#\# Resources **Key AWS services:** 
+  [AWS Outposts](https://aws.amazon.com/outposts/) 
+  [Amazon EC2](https://aws.amazon.com/ec2/) 
+  [Amazon Time Sync Service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-time.html) 