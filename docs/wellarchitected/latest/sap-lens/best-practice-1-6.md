# Best Practice 1.6 – Implement

dependency monitoring

Configure your workload to provide information about the status (for example,
reachability or response time) of resources it depends on. Examples of external
dependencies can include interfaces (for example, through SAP PI/PO), external data
stores, DNS, on premises components, Active Directory controllers and network devices. Use
this information to determine when a response is required. Consider third party monitoring
tools that can provide cross-technology metrics to monitor the health of end-to-end
dependencies.

**Suggestion 1.6.1 - Implement health tracking for your key SAP
interfaces and cross system business processes**

Identify and monitor your key interfaces which your SAP workload is dependent on.
Monitor the health of these interfaces endpoints, errors, queue length and success rates.
Use in-built mechanisms in SAP or third-party integration tools to set up alerts on
interface failure or delay and feed these into your monitoring tools. Consider all
interface pathways:

- Between different AWS hosted SAP systems (direct via RFC or web
  service/HTTPS)
- Between AWS hosted SAP systems and on-premises systems (HTTPS/SFTP - through SAP
  PI or third-party integration platform)
- Between AWS hosted SAP systems and SAP Business Technology Platform (via SAP
  Cloud Connector)
- Between AWS hosted SAP systems and external party systems (typically via HTTPS
  over the internet/VPN)
  Consider Solution Manager Business Process Monitoring for cross-system dependency
  monitoring throughout your SAP and non-SAP landscape.

- SAP Documentation: [SAP Business Process and Interface Monitoring](https://help.sap.com/viewer/c458e6a97c6746f2afb2a3d1bf0a630b/LATEST/en-US/2ffcb651ade3147fe10000000a44176d.html "https://help.sap.com/viewer/c458e6a97c6746f2afb2a3d1bf0a630b/LATEST/en-US/2ffcb651ade3147fe10000000a44176d.html")
- AWS Marketplace: [Products and Tools for SAP Monitoring](https://aws.amazon.com/marketplace/search/results?page=1&searchTerms=SAP&category=45c68cc2-ccd6-426b-94bd-92a791004dc2 "https://aws.amazon.com/marketplace/search/results?page=1&searchTerms=SAP&category=45c68cc2-ccd6-426b-94bd-92a791004dc2")

**Suggestion 1.6.2 - Implement health tracking for your enterprise
services which SAP is dependent on**

An SAP workload is typically dependent on several foundational enterprise services to
be healthy for business users. Consider these foundation services in your monitoring
approach and tools. Example foundational services include Direct Connect for on-premises
system connectivity, Active Directory for authentication/SSO, Network Time Protocol (NTP)
for time synchronization, antivirus services and connectivity to an operating system patch
repository (for example, Microsoft Windows Update or SUSE patching).

- AWS Documentation: [Collect metrics and logs from Amazon EC2 instances and on-premises servers with the
  CloudWatch Agent](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md")
- AWS Documentation: [Enhanced monitoring capabilities for AWS Direct Connect](../../../directconnect/latest/UserGuide/monitoring-cloudwatch.md "../../../directconnect/latest/UserGuide/monitoring-cloudwatch.md")
