

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# AMS responsibility matrix (RACI)
<a name="raci-table"></a>

**Note**  
In order to fulfill its obligations in a timely manner, AWS Managed Services (AMS) may require inputs from you for deciding an appropriate course of action. AMS will contact the designated customer contact for all such clarifications and inputs. AMS will expect a response to such queries within 24 business hours. In case there is no reply within 24 business hours, AMS may choose an action on your behalf.

The AMS responsible, accountable, consulted, and informed, or RACI, matrix assigns primary responsibility either to the customer or AMS for a variety of activities.

AMS manages your AWS infrastructure. The following table provides an overview of the responsibilities of customer and AMS for activities in the lifecycle of an application running within an AMS managed environment.

AMS is not responsible for any of the following activities for Customer Managed accounts or the infrastructure running within them; therefore this RACI is not applicable.
+ **R** stands for responsible party that does the work to achieve the task.
+ **C** stands for consulted; a party whose opinions are sought, typically as subject matter experts; and with whom there is bilateral communication.
+ **I** stands for informed; a party which is informed on progress, often only on completion of the task or deliverable.
+ **Self-service Provisioning** refers to resources that are provisioned by the customer with self-service through the AWS API or Console, including Developer Mode and Self-Service Provisioned Services.
**Note**  
Some sections contain 'R' for both AMS and Customers. This is because, in the AWS Shared Responsibility model, both AMS and the customers take joint ownership to respond to infrastructure and application issues.

  To provide self-service provisioning capabilities, AMS has created elevated IAM roles with permission boundaries to limit unintended changes from direct AWS service access. Roles do not prevent all changes and you are responsible to adhere to your internal controls, compliance, and to validate that all AWS services being used meet the required certifications. We call this the Self-Service Provisioning mode. For details on AWS compliance requirements, see [AWS Compliance](https://aws.amazon.com/compliance/).

  For resources that you provision through self-service, AMS provides incident management, detective controls and guardrails, reporting, designated resources (Cloud Service Delivery Manager and Cloud Architect), Security & access, and technical support through service requests. Additionally, where applicable, you assume responsibility for continuity management, patch management, infrastructure monitoring, and change management for resources provisioned or configured outside of the AMS change management system.


<table>
<thead>
  <tr><th><b>Activity</b></th><th><b>Customer</b></th><th><b>AWS Managed Services (AMS)</b></th></tr>
</thead>
<tbody>
  <tr><td colspan="3"><b>Application lifecycle</b></td></tr>
  <tr><td>Application development</td><td>R</td><td>I</td></tr>
  <tr><td>Application infrastructure requirements analysis and design</td><td>R</td><td>C</td></tr>
  <tr><td>Design and optimization for non-standard AMS stacks</td><td>R</td><td>C</td></tr>
  <tr><td>Design and optimization of AMS standard stack</td><td>I</td><td>R</td></tr>
  <tr><td>Application deployment</td><td>R</td><td>C</td></tr>
  <tr><td>AWS Infrastructure deployment</td><td>C</td><td>R</td></tr>
  <tr><td>Application monitoring</td><td>R</td><td>I</td></tr>
  <tr><td>Application testing/optimization</td><td>R</td><td>I</td></tr>
  <tr><td>AWS infrastructure optimization guidance</td><td>I</td><td>R</td></tr>
  <tr><td>AWS infrastructure monitoring</td><td>I</td><td>R</td></tr>
  <tr><td>Troubleshoot and resolve application issues</td><td>R</td><td>C</td></tr>
  <tr><td>Troubleshoot and resolve AWS network issues</td><td>C</td><td>R</td></tr>
  <tr><td rowspan="2">Troubleshoot and resolve operating system and infrastructure issues<br /><i>Self-Service Provisioning</i></td><td>C</td><td>R</td></tr>
  <tr><td><i>R</i></td><td><i>C</i></td></tr>
  <tr><td colspan="3"><b>Application and ITSM Integration</b></td></tr>
  <tr><td>Application integration with AWS Service Offerings</td><td>R</td><td>C</td></tr>
  <tr><td>ITSM integration with the AWS Managed Services Interface</td><td>R</td><td>C</td></tr>
  <tr><td colspan="3"><b>Networking</b></td></tr>
  <tr><td>Managed Environment VPC and VPC set-up and configuration</td><td>C</td><td>R</td></tr>
  <tr><td>Allocate private address space for VPCs (e.g. /16)</td><td>R</td><td>C</td></tr>
  <tr><td>Configure &amp; Operate non-AWS Managed Services, Customer managed Firewalls/Proxy/Bastions/HOSTs</td><td>R</td><td>C</td></tr>
  <tr><td>Configure &amp; Operate AWS Security Groups/NAT/Customer Bastions/NACL inside the Managed Environment</td><td>I</td><td>R</td></tr>
  <tr><td>Networking (e.g. DirectConnect) configuration and implementation within customer network</td><td>R</td><td>C</td></tr>
  <tr><td>Networking configuration and implementation within the Managed Environment</td><td>C</td><td>R</td></tr>
  <tr><td colspan="3"><b>Managed environment configuration</b></td></tr>
  <tr><td>Define default Auto Scaling settings for baseline Stack templates</td><td>I</td><td>R</td></tr>
  <tr><td>Recommend RI optimization</td><td>C</td><td>R</td></tr>
  <tr><td>Purchase RI and PIOP capacity</td><td>R</td><td>C</td></tr>
  <tr><td>Remove capacity when capacity is over provisioned (when supported by customer application)</td><td>C</td><td>R</td></tr>
  <tr><td>Create/update AWS customer specific information for AWS Managed Services</td><td>C</td><td>R</td></tr>
  <tr><td rowspan="2">S3 configuration<br /><i>Self-service provisioning</i></td><td>C</td><td>R</td></tr>
  <tr><td>R</td><td>C</td></tr>
  <tr><td>Glacier configuration</td><td>C</td><td>R</td></tr>
  <tr><td>Define archival policy</td><td>R</td><td>C</td></tr>
  <tr><td>Archival policy configuration</td><td>C</td><td>R</td></tr>
  <tr><td>Selecting customer maintenance window</td><td>R</td><td>I</td></tr>
  <tr><td colspan="3"><b>AWS RDS Management</b></td></tr>
  <tr><td>Monitor source/replica/RO replication health</td><td>I</td><td>R</td></tr>
  <tr><td>Identify RCA of source failover</td><td>I</td><td>R</td></tr>
  <tr><td rowspan="2">Automated snapshot (backup) configuration<br />Self-service provisioning</td><td>C</td><td>R</td></tr>
  <tr><td>R</td><td>C</td></tr>
  <tr><td rowspan="2">Coordinate and schedule DB engine patch management<br />Self-service provisioning</td><td>C</td><td>R</td></tr>
  <tr><td>R</td><td>C</td></tr>
  <tr><td rowspan="2">Recommend DB storage and PIOP capacity<br /><i>Self-service provisioning</i></td><td>C</td><td>R</td></tr>
  <tr><td>R</td><td>C</td></tr>
  <tr><td rowspan="2">Recommend instance sizing for running databases<br /><i>Self-service provisioning</i></td><td>C</td><td>R</td></tr>
  <tr><td>R</td><td>C</td></tr>
  <tr><td rowspan="2">Recommend RI optimization for Managed Environment<br /><i>Self-service provisioning</i></td><td>C</td><td>R</td></tr>
  <tr><td>R</td><td>C</td></tr>
  <tr><td rowspan="2">RDS performance monitoring (CloudWatch)<br /><i>Self-service provisioning</i></td><td>C</td><td>R</td></tr>
  <tr><td>R</td><td>C</td></tr>
  <tr><td rowspan="2">RDS event subscription configuration (SNS)<br /><i>Self-service provisioning</i></td><td>C</td><td>R</td></tr>
  <tr><td>R</td><td>C</td></tr>
  <tr><td rowspan="2">RDS security group configuration<br /><i>Self-service provisioning</i></td><td>C</td><td>R</td></tr>
  <tr><td>R</td><td>C</td></tr>
  <tr><td>RDS engine parameter/option configuration</td><td>R</td><td>C</td></tr>
  <tr><td>DB table design</td><td>R</td><td>I</td></tr>
  <tr><td>DB indexing</td><td>R</td><td>I</td></tr>
  <tr><td>DB log analysis</td><td>R</td><td>I</td></tr>
  <tr><td colspan="3"><b>AMS Change Management</b></td></tr>
  <tr><td>Creating customer RFCs (e.g. access to resources creating/updating/deleting managed stacks, deploying/updating applications, changes to configuration of AWS Service Offerings)</td><td>R</td><td>I</td></tr>
  <tr><td>Approving Customer RFCs</td><td>I</td><td>R</td></tr>
  <tr><td>Creating AWS Managed Services RFCs (e.g. access to resources, creating resources on customer’s behalf, applying updates to OS as part of Patch Management)</td><td>I</td><td>R</td></tr>
  <tr><td>Approving non-automated RFCs</td><td>R</td><td>I</td></tr>
  <tr><td>Submitting request for new Change Types</td><td>R </td><td>C</td></tr>
  <tr><td>Creating new Change Types</td><td>I</td><td>R</td></tr>
  <tr><td> Maintenance of application change calendar </td><td> R </td><td> C </td></tr>
  <tr><td> Notice of upcoming Maintenance Window </td><td> I </td><td> R </td></tr>
  <tr><td colspan="3"><b>AWS Service Catalog</b></td></tr>
  <tr><td> Create portfolios and products </td><td> R </td><td> I </td></tr>
  <tr><td> Distribute products to end users </td><td> R </td><td> I </td></tr>
  <tr><td> Create tags and tag option library </td><td> R </td><td> C </td></tr>
  <tr><td> Sharing portfolios and products with end users </td><td> R </td><td> I </td></tr>
  <tr><td> Revise / update portfolios and products </td><td> R </td><td> I </td></tr>
  <tr><td> Create and assign constraints to portfolios and products </td><td> R </td><td> C </td></tr>
  <tr><td> Associate Service Actions to products </td><td> R </td><td> C </td></tr>
  <tr><td> Update provisioned resources with new version of product </td><td> R </td><td> I </td></tr>
  <tr><td colspan="3"><b>Provisioning</b></td></tr>
  <tr><td>Customer specific additions to AWS Managed Services baseline AMI </td><td> R</td><td> C </td></tr>
  <tr><td> Configure additional approved Change Types used to provision Stack templates </td><td> C </td><td> R </td></tr>
  <tr><td rowspan="2">Launch managed Stacks and associated AWS resources submitted through AMS change management process or AWS Service Catalog.<br /><i>Self-service provisioning</i></td><td>I</td><td>R</td></tr>
  <tr><td>R</td><td>I</td></tr>
  <tr><td> Install/Update custom and 3rd party applications on Instances provisioned through AMS change management process or AWS Service Catalog. </td><td> R </td><td> I </td></tr>
  <tr><td colspan="3"><b>Provisioning - Stack Architecture</b></td></tr>
  <tr><td rowspan="2">Providing OS licenses (including usage fees for the applicable AWS services – e.g. EC2 and RDS)<br /><i>Self-Service Provisioning</i></td><td>I</td><td>R</td></tr>
  <tr><td><i>R</i></td><td><i>I</i></td></tr>
  <tr><td rowspan="2">Define baseline infrastructure templates (Stacks) for application deployment through AMS change management system.<br /><i>Self-Service Provisioning</i></td><td>I</td><td>R</td></tr>
  <tr><td><i>R</i></td><td><i>I</i></td></tr>
  <tr><td> Creating baseline approved AMIs8</td><td> I</td><td>R</td></tr>
  <tr><td> Evaluate customer application inventory and determine fit with available infrastructure templates (Stacks) </td><td>R</td><td>C</td></tr>
  <tr><td> Define unique Stacks that are in addition to the baseline template offerings </td><td> R </td><td> C </td></tr>
  <tr><td colspan="3"><b>Logging, Monitoring and Event Management</b></td></tr>
  <tr><td> Recording AWS infrastructure change logs </td><td>I</td><td>R</td></tr>
  <tr><td> Recording all application change logs </td><td>R</td><td>C</td></tr>
  <tr><td rowspan="2">Installation and configuration of agents and scripts for patching, security, monitoring, etc. of AWS infrastructure provisioned through the AMS change management process.<br /><i>Self-Service Provisioning</i></td><td>I</td><td>R</td></tr>
  <tr><td><i>R</i></td><td><i>C</i></td></tr>
  <tr><td> Define customer specific monitoring and incident requirements</td><td>R</td><td>C</td></tr>
  <tr><td> Configuring alerts for Managed Environment </td><td>I</td><td>R</td></tr>
  <tr><td rowspan="2">Monitoring all AMS configured alerts<br /><i>Self-Service Provisioning</i></td><td>I</td><td>R</td></tr>
  <tr><td><i>R</i></td><td><i>C</i></td></tr>
  <tr><td rowspan="2">Investigating infrastructure Alerts for Incident notification<br /><i>Self-Service Provisioning</i></td><td>I</td><td>R</td></tr>
  <tr><td><i>R</i></td><td><i>C</i></td></tr>
  <tr><td>Investigating application alarms</td><td>R</td><td>C</td></tr>
  <tr><td colspan="3"><b>Incident Management</b></td></tr>
  <tr><td rowspan="2">Proactively notify Incidents on AWS infrastructure based on monitoring<br /><i>Self-Service Provisioning</i></td><td>I</td><td>R</td></tr>
  <tr><td><i>R</i></td><td><i>C</i></td></tr>
  <tr><td>Handle application performance issues and outages</td><td>R</td><td>I</td></tr>
  <tr><td>Categorize Incident priority </td><td>I</td><td>R</td></tr>
  <tr><td>Provide Incident response </td><td>I</td><td>R</td></tr>
  <tr><td>Provide Incident resolution / infrastructure restore SLAs do not apply to instance-based resources provisioned outside AMS change management, including those provisioned using self-service provisioning and developer mode. </td><td>C</td><td>R</td></tr>
  <tr><td colspan="3"><b>Problem Management</b></td></tr>
  <tr><td> Identify Problems in Managed Environment </td><td>C</td><td>R</td></tr>
  <tr><td> Perform RCA for Problems in Managed Environment </td><td>C</td><td>R</td></tr>
  <tr><td>Remediation of Problems in Managed Environment</td><td>C</td><td>R</td></tr>
  <tr><td>Identify and remediate application problems</td><td>R</td><td>I</td></tr>
  <tr><td colspan="3"><b>Security Management</b></td></tr>
  <tr><td rowspan="2">Customer infrastructure security and/or establishing baseline for security compliance process as determined and agreed to during customer onboarding.<br /><i>Self-Service Provisioning</i></td><td>C</td><td>R</td></tr>
  <tr><td><i>R</i></td><td><i>C</i></td></tr>
  <tr><td>Maintaining valid licenses for Managed EPS</td><td>R</td><td>C</td></tr>
  <tr><td rowspan="2">Configure Managed EPS<br /><i>Self-Service Provisioning</i></td><td>I</td><td>R</td></tr>
  <tr><td><i>R</i></td><td><i>C</i></td></tr>
  <tr><td rowspan="2">Update Managed EPS<br /><i>Self-Service Provisioning</i></td><td>I</td><td>R</td></tr>
  <tr><td><i>R</i></td><td><i>C</i></td></tr>
  <tr><td rowspan="2">Monitoring malware on instances provisioned through the AMS CM process.<br /><i>Self-Service Provisioning</i></td><td>I</td><td>R</td></tr>
  <tr><td><i>R</i></td><td><i>C</i></td></tr>
  <tr><td rowspan="2">Maintaining and updating virus signatures.<br /><i>Self-Service Provisioning</i></td><td>I</td><td>R</td></tr>
  <tr><td><i>R</i></td><td><i>C</i></td></tr>
  <tr><td rowspan="2">Remediating instances infected with malware.<br /><i>Self-Service Provisioning</i></td><td>C</td><td>R</td></tr>
  <tr><td><i>R</i></td><td><i>C</i></td></tr>
  <tr><td>Security event management</td><td>C</td><td>R</td></tr>
  <tr><td colspan="3"><b>Security - Access Management</b></td></tr>
  <tr><td>Manage the lifecycle of users, and their permissions for local directory services, which are used to access AWS Managed Services</td><td>R</td><td>I</td></tr>
  <tr><td>Operate federated authentication system(s) for customer access to AWS console/APIs</td><td>R</td><td>C</td></tr>
  <tr><td>Accept and maintain Active Directory (AD) trust from AWS Managed Services AD to customer managed AD</td><td>R</td><td>C</td></tr>
  <tr><td>During onboarding, create cross-account IAM Admin roles within each managed account</td><td>R</td><td>C</td></tr>
  <tr><td>Secure the AWS root credential for each account</td><td>I</td><td>R</td></tr>
  <tr><td>Define IAM resources for Managed Environment</td><td>C</td><td>R</td></tr>
  <tr><td>Manage privileged credentials for OS access for AMS engineers</td><td>I</td><td>R</td></tr>
  <tr><td>Manage privileged credentials for OS access provided to customer by AMS</td><td>R</td><td>I</td></tr>
  <tr><td colspan="3"><b>Security Incident Response - Prepare</b></td></tr>
  <tr><td colspan="3"><b>Communications</b></td></tr>
  <tr><td>Provide customer security contact details for AMS to use during security events notifications and security escalations</td><td>R</td><td>I</td></tr>
  <tr><td>Store and manage the supplied customer security contact details to use during security events and security escalations</td><td>CI</td><td>R</td></tr>
  <tr><td colspan="3"><b>Training</b></td></tr>
  <tr><td>Provide customer with documentation to support AMS during incident response process</td><td>I</td><td>R</td></tr>
  <tr><td>Practice shared responsibility during incident response processes through security gamedays</td><td>RI</td><td>RC</td></tr>
  <tr><td colspan="3"><b>Resource management</b></td></tr>
  <tr><td>Configure supported security management AWS services for alerting, alerts correlation, noise reduction and additional rules</td><td>I</td><td>R</td></tr>
  <tr><td>Maintain asset (AWS resources) inventory, and know the asset value and criticality of assets. This information is helpful during incident containment strategy</td><td>R</td><td>CI</td></tr>
  <tr><td>Employ AWS tags to identify resources and workloads</td><td>R</td><td>CI</td></tr>
  <tr><td>Define and configure log retention and archival</td><td>CI</td><td>R</td></tr>
  <tr><td>Secure baselining of AWS account, configurations, policies and access management</td><td>CI</td><td>RC</td></tr>
  <tr><td colspan="3"><b>Security Incident Response - Detect</b></td></tr>
  <tr><td colspan="3"><b>Logging, indicators and monitoring</b></td></tr>
  <tr><td>Configure logging and monitoring to enable event management for instance and accounts</td><td>CI</td><td>R</td></tr>
  <tr><td>Monitor supported AWS services for security alerts</td><td>I</td><td>R</td></tr>
  <tr><td>Deploy and manage endpoint security tools</td><td>CI</td><td>R</td></tr>
  <tr><td>Monitor for malware on instances using AMS supported endpoint security tool</td><td>I</td><td>R</td></tr>
  <tr><td>Notify customer of detected events through outbound messaging</td><td>I</td><td>R</td></tr>
  <tr><td>Route notification and any subsequent updates to the decision makers for specific accounts and workloads to improve incident response time</td><td>R</td><td>CI</td></tr>
  <tr><td>Define, deploy, and maintain AMS standard detection services (for example, Amazon GuardDuty and AWS Config)</td><td>CI</td><td>R</td></tr>
  <tr><td>Record AWS infrastructure change logs</td><td>I</td><td>RC</td></tr>
  <tr><td>Enable and configure logging, monitoring to enable event management for the application</td><td>R</td><td>C</td></tr>
  <tr><td>Implement and maintain an allow-list, deny-list, and custom detections on supported AWS security services (for example, Amazon GuardDuty)</td><td>RCI</td><td>R</td></tr>
  <tr><td colspan="3"><b>Security event reporting</b></td></tr>
  <tr><td>Notify AMS of a suspicious activity or an active security investigation</td><td>R</td><td>CI</td></tr>
  <tr><td>Notify detected security events and incidents to the customer</td><td>I</td><td>R</td></tr>
  <tr><td>Notify planned event that might trigger Security Incident Response process</td><td>R</td><td>CI</td></tr>
  <tr><td colspan="3"><b>Security Incident Response - Analyze</b></td></tr>
  <tr><td colspan="3"><b>Investigation and analysis</b></td></tr>
  <tr><td>Perform initial response for supported security alert generated by a supported detection source</td><td>I</td><td>RC</td></tr>
  <tr><td>Assess false/true positives using the available data</td><td>RI</td><td>RC</td></tr>
  <tr><td>Generate a snapshot of affected instances to be shared with the customer if needed</td><td>I</td><td>R</td></tr>
  <tr><td>Perform forensics tasks such as chain of custody, file system analysis, memory forensics, and binary analysis</td><td>R</td><td>CI</td></tr>
  <tr><td>Collect application logs to aid investigation</td><td>R</td><td>I</td></tr>
  <tr><td>Collect data and logs to aid investigation on security alerts</td><td>RCI</td><td>RC</td></tr>
  <tr><td>Engage SMEs within AWS services on security investigations</td><td>CI</td><td>R</td></tr>
  <tr><td>Engage third-party vendors during investigation (for example, for EPS anti-malware investigation and engaging with TrendMicro support team)</td><td>RCI</td><td>I</td></tr>
  <tr><td>Share investigation logs from supported AWS services to customers during an investigation</td><td>I</td><td>R</td></tr>
  <tr><td colspan="3"><b>Communication</b></td></tr>
  <tr><td>Send alert and notifications from AMS detection sources for managed resources</td><td>I</td><td>R</td></tr>
  <tr><td>Manage alert and notifications for application security events</td><td>R</td><td>I</td></tr>
  <tr><td>Engage customer security point of contact during a security incident investigation</td><td>R</td><td>I</td></tr>
  <tr><td colspan="3"><b>Security Incident Response - Contain</b></td></tr>
  <tr><td colspan="3"><b>Containment strategy and execution</b></td></tr>
  <tr><td>Decide on the execution of the agreed containment strategy and agree with the consequences that might affect the availability of services during the containment window</td><td>R</td><td>CI</td></tr>
  <tr><td>Make a backup of affected systems for further analysis</td><td>CI</td><td>R</td></tr>
  <tr><td>Contain applications and workloads (through application specific configuration or response activity)</td><td>R</td><td>CI</td></tr>
  <tr><td>Define the containment strategy based on the security incident and the affected resource</td><td>CI</td><td>R</td></tr>
  <tr><td>Enable encryption and secure storage of point in time backups of affected systems</td><td>CI</td><td>R</td></tr>
  <tr><td>Execute supported containment actions for AWS resources including EC2 instances, network, and IAM</td><td>CI</td><td>R</td></tr>
  <tr><td colspan="3"><b>Security Incident Response - Eradicate</b></td></tr>
  <tr><td colspan="3"><b>Eradication strategy and execution</b></td></tr>
  <tr><td>Define eradication options based on the security incident and the affected resource on customer application workloads</td><td>R</td><td>CI</td></tr>
  <tr><td>Decide on the agreed eradication strategy, timing of eradication execution, and the consequences</td><td>R</td><td>CI</td></tr>
  <tr><td>Define eradication steps based on the security incident and the affected resource on AMS managed workloads</td><td>CI</td><td>R</td></tr>
  <tr><td>Eradicate and harden AWS resources including EC2 instances, network, and IAM eradication</td><td>CI</td><td>R</td></tr>
  <tr><td>Eradicate and harden applications and workloads (through application specific configuration or response activity)</td><td>R</td><td>I</td></tr>
  <tr><td colspan="3"><b>Security Incident Response - Recover</b></td></tr>
  <tr><td colspan="3"><b>Recovery preparation and execution</b></td></tr>
  <tr><td>Configure backup plans and targets as requested by the customer</td><td>R</td><td>I</td></tr>
  <tr><td>Review backup plans to restore AMS managed workloads</td><td>CI</td><td>R</td></tr>
  <tr><td>Perform backup restoration activities for resources of supported AWS services</td><td>I</td><td>R</td></tr>
  <tr><td>Backup customer application, APP configuration, and deployment settings, and review backup plans to restore customer applications and workloads post-incident</td><td>R</td><td>I</td></tr>
  <tr><td>Restore applications and customer workloads (through application specific restoration steps)</td><td>R</td><td>I</td></tr>
  <tr><td colspan="3"><b>Security Incident Response – Post Incident Report</b></td></tr>
  <tr><td colspan="3"><b>Post incident reporting</b></td></tr>
  <tr><td>Share appropriate lessons learned and action items with customer post incident as required</td><td>I</td><td>R</td></tr>
  <tr><td colspan="3"><b>Patch Management9</b></td></tr>
  <tr><td rowspan="2">Monitor for applicable updates to supported OS and software preinstalled with supported OS for EC2 instances.<br /><i>Self-Service Provisioning</i></td><td>I</td><td>R</td></tr>
  <tr><td><i>R</i></td><td><i>C</i></td></tr>
  <tr><td>Notify customer of upcoming updates (<i>applies to AMS Standard Patch only</i>)</td><td>I</td><td>R</td></tr>
  <tr><td>Exclude certain updates and/or certain Stacks from patching activities</td><td>R</td><td>I</td></tr>
  <tr><td>Define default and custom maintenance windows schedules and other parameters (e.g. maintenance window duration) to apply patches (<i>applies to AMS Patch</i><br /><i>Orchestrator only</i>)</td><td>R</td><td>I</td></tr>
  <tr><td>Define custom Patch Baselines to filter and exclude specific patches (<i>applies to AMS Patch Orchestrator only</i>)</td><td>R</td><td>I</td></tr>
  <tr><td>Tag instances to associate them with custom maintenance windows and Patch Baselines (<i>applies to AMS Patch Orchestrator only</i>)</td><td>R</td><td>I</td></tr>
  <tr><td>Track the patch status of resources and highlight systems that aren’t current in the monthly business review.</td><td>C</td><td>R</td></tr>
  <tr><td rowspan="2">Patch the Windows operating system, and Microsoft packages installed on the operating system which are governed by Windows Update<br /><i>Self-Service Provisioning</i></td><td>I</td><td>R</td></tr>
  <tr><td><i>R</i></td><td>-</td></tr>
  <tr><td rowspan="2">Patch installed applications, software, or application dependencies not managed by Windows Update <i>Self-service provisioning</i></td><td>R</td><td>I</td></tr>
  <tr><td><i>R</i></td><td>-</td></tr>
  <tr><td rowspan="2">Patch the Linux operating system and any package that is enabled for management by the operating system's native package manager (for example Yum, Apt, Zypper)<br /><i>Self-service provisioning</i></td><td>I</td><td>R</td></tr>
  <tr><td><i>R</i></td><td>-</td></tr>
  <tr><td rowspan="2">Patch installed applications, software, or application dependencies not managed by the Linux operating system's native package manager<br /><i>Self-service provisioning</i></td><td>R</td><td>I</td></tr>
  <tr><td><i>R</i></td><td>-</td></tr>
  <tr><td colspan="3"><b>Continuity Management</b></td></tr>
  <tr><td>Specify backup schedules</td><td>R</td><td>I</td></tr>
  <tr><td rowspan="2">Execute backups per schedule.<br /><i>Self-Service Provisioning</i></td><td>I</td><td>R</td></tr>
  <tr><td><i>R</i></td><td><i>C</i></td></tr>
  <tr><td>Validate backups</td><td>R</td><td>I</td></tr>
  <tr><td>Request backup restoration activities</td><td>R</td><td>I</td></tr>
  <tr><td rowspan="2">Execute backup restoration activities.<br /><i>Self-Service Provisioning</i></td><td>I</td><td>R</td></tr>
  <tr><td><i>R</i></td><td><i>C</i></td></tr>
  <tr><td rowspan="2">Restore affected Stacks and VPCs.<br /><i>Self-Service Provisioning</i></td><td>I</td><td>R</td></tr>
  <tr><td><i>R</i></td><td><i>C</i></td></tr>
  <tr><td>Restore affected custom/3rd party application</td><td>R</td><td>C</td></tr>
  <tr><td colspan="3"><b>Reporting</b></td></tr>
  <tr><td rowspan="2">Prepare and deliver monthly service report<br /><i>AMS on AWS Outposts</i></td><td>I</td><td>R</td></tr>
  <tr><td>R</td><td>I</td></tr>
  <tr><td rowspan="2">Configure and retrieve API audit history on demand (CloudTrail).<br /><i>Self-service provisioning</i></td><td>I</td><td>R</td></tr>
  <tr><td>R</td><td>I</td></tr>
  <tr><td> Provide access to incident history through AWS Managed Services Interface</td><td>I</td><td>R</td></tr>
  <tr><td rowspan="2">Provide access to change history through AWS Managed Services Interface.<br /><i>Self-service provisioning</i></td><td>I</td><td>R</td></tr>
  <tr><td>N/A</td><td>N/A</td></tr>
  <tr><td colspan="3"><b>Service Request Management</b></td></tr>
  <tr><td>Request information using service requests</td><td>R</td><td>I</td></tr>
  <tr><td> Reply to service requests</td><td>I</td><td>R</td></tr>
</tbody>
</table>


8AMS provides AMIs for Amazon EC2 only

9AMS is responsible for End of Life OSes only when the customer signs an extended support agreement with OS vendor