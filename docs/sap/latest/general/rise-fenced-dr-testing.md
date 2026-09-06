

# Fenced (Live) DR Testing
<a name="rise-fenced-dr-testing"></a>

Fenced DR Testing is a disaster recovery testing capability for RISE with SAP customers using Long Distance Disaster Recovery (LDDR). It uses network isolation to create a segregated testing environment. Production and DR systems operate simultaneously, eliminating the need for planned downtime during DR validation. Isolation spans multiple layers: network routing, DNS resolution, and application connectivity. These layers prevent cross-contamination between environments.

**Note**  
We recommend using multiple AWS Regions for disaster recovery. For more information about AWS disaster recovery strategies, see the [AWS Well-Architected Framework – Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).

**Note**  
Fenced DR Testing is available in all AWS Regions if you subscribe to RISE with SAP Long Distance Disaster Recovery (LDDR).

## Benefits of fenced DR Testing
<a name="_benefits_of_fenced_dr_testing"></a>

### Zero Production Impact
<a name="_zero_production_impact"></a>
+ Test DR failover without production downtime
+ Eliminates the multi-hour outage window typically required for DR testing
+ Business operations continue uninterrupted during testing

### Complete Network Isolation
<a name="_complete_network_isolation"></a>
+ Production and DR environments operate in isolated network segments using routing controls
+ Maintains strict separation of DNS namespaces and IP address ranges

### End-to-End Integration Testing
<a name="_end_to_end_integration_testing"></a>
+ Test complete disaster recovery scenarios including on-premises system integration
+ Validate network connectivity paths, data replication mechanisms, and application failover procedures
+ Verify recovery time objectives (RTO) and recovery point objectives (RPO) under realistic conditions
+ Conduct full application stack testing including SAP application servers, databases, and supporting infrastructure

### Operational Readiness
<a name="_operational_readiness"></a>
+ Prepare operations teams to execute disaster recovery procedures
+ Identify and resolve issues before an actual disaster occurs
+ Document and refine recovery procedures based on test results
+ Establish baseline performance metrics for recovery operations

## Architecture Overview
<a name="_architecture_overview"></a>

Fenced DR Testing creates a parallel network environment that mirrors your production topology while maintaining isolation. The architecture includes:
+  **Network Segmentation**: Dedicated subnets and routing tables for the DR test environment
+  **DNS Isolation**: Separate DNS resolution to prevent production traffic from reaching test systems
+  **Traffic Control**: Network access control lists (ACLs) and security groups ensuring traffic separation
+  **Monitoring Integration**: Observability of both production and test environments during validation

## LDDR Fenced Testing
<a name="_lddr_fenced_testing"></a>

With Long Distance Disaster Recovery (LDDR) Fenced Testing, you can validate your DR environment without disrupting production. During a fenced test, SAP isolates the DR system in the standby AWS Region from production. Your primary system continues to run normally in the primary Region. Local high-availability replication across Availability Zones remains active. During the test, SAP pauses replication to the standby Region. During this window, cross-region protection is unavailable, and a regional failure might result in data loss. After testing is complete, replication resumes automatically and the DR system re-synchronizes with production.

There are two scenarios for LDDR DR testing:

### LDDR Internal Fencing
<a name="_lddr_internal_fencing"></a>

Production and DR sites remain accessible to you with complete network isolation between sites.

The following diagram shows the network topology for LDDR Internal Fencing.

![Long Distance DR internal fencing with isolated production and DR network segments.](http://docs.aws.amazon.com/sap/latest/general/images/rise-fenceddr-lddr-scenario1-internal-fencing.png)


You must configure network separation on-premises to isolate the DR landscape, to prevent accidental access to production during DR testing. This scenario allows you to perform end-to-end DR testing, for example third-party interfaces and authentication (SSO, LDAP, Kerberos).

### LDDR Complete Fencing
<a name="_lddr_complete_fencing"></a>

The DR site is completely isolated. You provide specific IP addresses for the testing team to access the fenced environment.

The following diagram shows the network topology for LDDR Complete Fencing.

![Long Distance DR complete fencing with the DR site isolated from production.](http://docs.aws.amazon.com/sap/latest/general/images/rise-fenceddr-lddr-scenario2-complete-fencing.png)


The DR site is completely isolated from both the production SAP RISE systems and external networks. You must provide specific IP addresses or ranges for testing team access to the isolated DR systems. Testing IPs have access to both primary and DR sites, so you must carefully verify which environment you are working in during tests. No data replication occurs between sites during DR testing, preventing production users from accidentally accessing the DR environment.

We recommend that you coordinate with SAP on DR test procedures, because you might have existing DR Standard Operating Procedures (SOPs) that can be adapted. As part of the DR test preparation, create a Responsible, Accountable, Consulted, and Informed (RACI) matrix for all parties involved, that is, you, your vendors, and SAP.