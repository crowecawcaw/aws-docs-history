# AMS on Outposts

[AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/") is a managed hardware solution that extends
AMS managed landing zones to customer data centers. With AMS support on AWS Outposts, customers seeking the
cloud expertise, cost savings and standardized platform offered by AMS, are no longer limited to hosting
resources inside AWS Regions. With AMS on AWS Outposts, customers with on-premise requirements can now modernize on AWS,
while enjoying the patching, backup, provisioning, incident management, business continuity, and cost optimization services offered by AMS.

Once an AWS Outposts is activated in your AMS Multi-Account Landing Zone or Single-Account Landing Zone account, you can follow existing AMS change
management processes to provision and manage AWS resources. AMS-hosted infrastructure can be managed by
specifying your AWS Outposts-specific subnet. AWS Outposts lifecycles can be managed directly in the AWS Outposts console using the
AWS Outposts self-provision services role.

For information on the role, see [AWS Outposts](outposts.md "outposts.md").

## AWS Outposts installation and operational management

The onboarding to AMS on AWS Outposts process is comprised of:

1. Outposts Planning
2. Order Validation
3. Outposts Onboarding to AMS
4. Lifecycle Management

### AWS Outposts planning

During AWS Outposts planning, you identify AMS on AWS Outposts use cases and engage key
stakeholders, including your AMS account team and AWS Outposts representatives, to align on capacity
strategy.

1. Once use cases requiring AMS on AWS Outposts have been identified, engage your AMS account
   team to discuss capacity planning.
2. Once your AWS Outposts capacity requirements have been determined, your AMS account team
   engages the AWS Outposts service team to discuss AWS Outposts onboarding plan, roles and
   responsibilities. During this time an AWS Outposts single point of contact (SPOC) is assigned
   to you. The AWS Outposts SPOC assists in finalizing AWS Outposts sizing requirements.

### AWS Outposts order validation

During order validation, you create an AWS Outposts site, and order your required capacity directly in
the AWS Outposts console or through your AWS Outposts account representative.

Once you, the AMS account team, the AWS Outposts team are aligned, you can request the AWS Outposts
self-provisioned service role using change type ID ct-3qe6io8t6jtny, to create your site and AWS Outposts
order directly in the AWS Outposts console.

Alternatively, you can work through the AWS Outposts SPOC to create Outpost Sites and orders.
Your AWS Outposts SPOC remains to provide status updates to you and the AMS account team during site and
order validation, and AWS Outposts installation.

### AWS Outposts onboarding to AMS

Once your AWS Outposts unit is activated in your AMS managed VPC, you can request that monitors be
created to track availability, capacity, exceptions and network connectivity for your Outposts
hardware. By following the monitoring deployment steps described next, your AWS Outposts hardware is actively
monitored by AMS.

1. Once your AWS Outposts has been installed and activated, you can request
   AWS Outposts-specific monitoring by submitting the following template with an RFC using the
   Management | Other | Other | Create (ct-1e1xtak34nx76) change type. AMS operations
   ensures that the AWS Outposts subnet is tracked in AMS internal tooling.
   - AWS Outposts ID
   - Subnet CIDR
   - Recommended AWS Outposts alarms:
     - InstanceFamilyCapacityAvailabilityAlert
     - InstanceTypeCapacityAvailabilityAlert
     - EBSVolumeTypeCapacityAvailabilityAlert
     - CapacityExceptionsAlert
     - Direct Connect ConnectionAlert

   - For each of the above alerts, specify the following parameters:
     - Statistic ("Average" is recommended. Other options include sum,
       maximum, minimum, sample count and p90)
     - Period ("5 minutes" is recommended. Other options include 10 and 30 seconds,
       1, 5, and 15 minutes, 1 and 6 hours, and 1 day)
     - Threshold type ("Static" is recommended. "Anomaly" are also options.)
     - Condition ("Whenever call count is greater than", "equal to", "less than" are
       also options.)
     - Condition Value ("25%" is configured by default. Another other positive
       integer is allowable.)
     - Notification topic (AMS operations topics are automatically assigned.
       However any other, or custom, topic can also be added.)

2. Monitoring and operations Support
   - AMS operations monitors AWS Outposts metrics for network disconnection
     or component failures. AMS operations provides first response services for AWS Outposts issues,
     and escalates, if needed, to Premium support or EC2 support.
   - AMS operations is available to address issues related to your
     AWS Outposts unit.

3. When EC2 instance status or system status checks fail, AMS operations follows
   existing processes to bring the instance back online. If the restart fails or AWS Outposts capacity
   is insufficient, then an AMS operations team member notifies you directly to determine
   next steps.

### AWS Outposts life cycle management

Once AWS Outposts has been onboarded to your AMS account, you are notified if any availability,
capacity, or network exceptions, occur. You can decommission AWS Outposts directly through the AWS Outposts
console or the AWS Outposts SPOC.

You can manage AWS Outposts directly in the AWS Outposts console using the AWS Outposts self-service
provisioning service role or developer mode. You can also request AWS Outposts through your CSDM, or
AWS Outposts single point of contact, (SPOC).

High-availability on AWS Outposts can be achieved by deploying two or more AWS Outposts. Configuring two or
more AWS Outposts enables the multi-availability zone option for your Amazon Relational Database Service instances.

## Provisioning AMS managed resources on AWS Outposts

Provisioning AWS resources hosted on AWS Outposts (for example, Amazon EC2, Amazon EMR, Amazon EKS, Amazon ECS, Amazon EBS, and Amazon S3) in AMS
accounts (Single-Account Landing Zone, Multi-Account Landing Zone, and Accelerate accounts) are subject to the same
AMS support levels as resources in AWS Regions. You can use AMS change management, self-service provisioning
services, or developer mode to create and modify the resources created on AWS Outposts.

Currently, all instance types (M5/M5d, C5/C5d, R5/R5d, I3en, G4dn), Amazon Elastic Block Store, Amazon Elastic Container Service,
Amazon Elastic Kubernetes Service, Amazon EMR, Amazon Relational Database Service DBs, Application Load Balancers, and App Mesh Envoy proxy are available directly on AWS Outposts.
These resources are eligible for the same AMS operations support as resources in existing regions.

## Limitations of AMS on AWS Outposts

- Operational support for AWS Outposts-hosted resources is dependent on consistent network
  connectivity. AWS Outposts network disconnection prevents AMS operations from being able to
  troubleshoot any incidents or problems that occur on the disconnected AWS Outposts unit. For AMS on AWS Outposts
  service level contingencies, see the updated
  [AWS Service Level Agreements (SLAs)](https://aws.amazon.com/legal/service-level-agreements/ "https://aws.amazon.com/legal/service-level-agreements/").
- Amazon Relational Database Service:
  - The create RDS change type (ct-2z60dyvto9g6c), by default, enables multi-AZ and requires
    a DB subnet group. DB subnet groups require two subnets in two separate Availability Zones (AZ).
    If you have only one AWS Outposts, creating a DB subnet group is an issue since AWS Outposts are only assigned
    to a single AZ. To circumvent this limitation, follow these instructions:
    1. Request a DB subnet group through an RFC with a Management | Other | Other CT,
       and specify the subnet on the AWS Outposts.
    2. Create a custom CFN template to deploy RDS on AWS Outposts, and specify the subnet group
       created in the previous step. To learn more about doing this, see
       [Custom resources](../../../AWSCloudFormation/latest/UserGuide/template-custom-resources.md "../../../AWSCloudFormation/latest/UserGuide/template-custom-resources.md").
    3. Request that AMS deploy the CFN template containing the target RDS instance
       through the AMS CFN ingest CT (ct-36cn2avfrrj9v).
    4. Note that currently, RDS for AWS Outposts does not provide metrics and logs due to a limitation
       of RDS Service.

  - Workload ingest (WIGs): Linux WIGs only works if the pre-WIGs EC2 instance is on a non-AWS Outposts subnet.
    The reason is because Linux WIGs creates a WIGs node in the subnet of the first EC2 instance using
    m4.large, by default. As AWS Outposts doesn't have that instance type, WIGs is not able to
    launch its worker node. The workaround for this is to create the initial EC2 instance in a
    non-AWS Outposts subnet, then the target instance can be created on AWS Outposts. Moreover, currently,
    only Nitro-based EC2 instance types including C5, C5d, M5, M5d, R5, R5d, G4, and I3en are
    supported on AWS Outposts.
  - Amazon Elastic Block Store (EBS): Create EBS Volume CT (ct-16xg8qguovg2w) does not work, as volumes get created
    in AWS instead of AWS Outposts as we do not provide the AWS Outposts Amazon resource number (ARN) as an input parameter to the
    CT.
  - Network connectivity: Network connectivity is your responsibility per the AWS Outposts team.
  - Brownfield and account takeover: AWS Outposts activated in non-AMS accounts cannot be
    transitioned into AMS, due to the nature of AWS Outposts billing and enterprise support requirements.

## AMS on AWS Outposts compliance

AMS on AWS Outposts compliance attestation
AWS Outposts control plane has been attested to HIPAA eligible, PCI and ISO compliance.
However, AMS on AWS Outposts control plane has not been attested for AWS Outposts. For this reason,
customers are encouraged to pursue compliance attestation AMS on AWS Outposts
environment.

For controlling resource creation on the Outpost unit, customers are encouraged to
segregate developer access to the Outpost, to prevent excess developer access in
standard AMS managed accounts.

AMS Managed Workloads requiring FedRAMP compliance
Foremost, AMS management accounts must first be assessed for regulatory compliance,
since control plane data would flow out of the AWS Outposts to AMS management accounts.

If FedRAMP certification is required and the AMS account structure is compliant, then it
is recommended that you either utilize a datacenter vendor that already has the required
certification and owns all of the service link appliance (or already encrypts egress data).

Finally, additional data protection can be put in place by working with your account team to
deploy an SCP that restricts data to the AWS Outposts and prevents the creation of any in-region
resources in the account hosting the Outpost.

Impact on existing compliance for AMS accounts
An account utilizing AWS Outposts does not need to be retested for compliance as
long as no regulated data is being consumed and the account is logically separated. AMS management
accounts can manage non-regulated and regulated accounts as long as cross account
authentication/authorization and ingress/ egress data flows are segregated between VPCs.
Therefore, even though both the non-compliant Outpost account and existing compliant application
accounts are in the same organization (including shared services, networking, logging, master,
security AMS services), the compliance application account still retains compliance since data
is logically separated.

## AMS on AWS Outposts FAQs

Which use cases qualify for AMS support on AWS Outposts?
AMS on AWS Outposts can be leveraged by enterprises needing a proven cloud operating
model have workloads requiring low latency (e.g., factory robot management and mainframe migration),
edge computing (e.g., remote workstations and edge data streamlining), and large data transfer
loads.

Why should I use this feature?
AMS provides monitoring of AWS Outposts hardware and first response to any AWS Outposts
hardware issue. Moreover, the following support features for all managed resources hosted on
AWS Outposts:

- Logging, Monitoring, Guardrails, and Event Management
- Continuity Management
- Security and Access Management
- Patch Management
- Change Management
- Automated and Self-Service Provisioning Management
- Incident and Problem Management
- Reporting (Reporting for AWS Outposts hardware will not be initially supported
  with AMS on AWS Outposts)
- Service Request Management
- Developer Mode
- Enterprise Support

How do I use this feature?
**AWS Outposts planning**: During AWS Outposts planning, you have
identified AMS on AWS Outposts use cases and will engage key stakeholders, including the AMS account
team and AWS Outposts representatives, to align on capacity strategy.

**Order validation**: During order validation, you create an
AWS Outposts site, and order your required capacity directly in the AWS Outposts console, or through your AWS Outposts account representative.

**AWS Outposts onboarding to AMS**: Once your AWS Outposts unit is activated
in your AMS managed VPC, you can request that your AWS Outposts be onboarded to your AMS account by submitting a request for
change (RFC) using the template in the AMS User Guide
([AWS Outposts](outposts.md "outposts.md")). AMS operations then creates a subnet
and monitors for your Outpost using the inputs provided on the RFC.

**Lifecycle management**: Once AWS Outposts has been onboarded to
your AMS account, you are notified of any availability, capacity, or network exceptions. You can decommission AWS Outposts
directly through the AWS Outposts console or your AWS Outposts single point of contact (SPOC).

What are the limitations of AMS on AWS Outposts?
Data residency (e.g., country-specific data localization laws, etc.) use cases have not yet been validated for AMS on AWS Outposts.

AWS Outposts activated in non-AMS accounts cannot be transitioned into AMS, due to the nature
of AWS Outposts billing and Enterprise Support requirements.

AWS Outposts control plane has been attested to HIPAA eligible, PCI and ISO compliance.
However, AMS on AWS Outposts control plane has not been attested for AWS Outposts. For this
reason, customers are encouraged to pursue compliance attestation AMS on AWS Outposts
environment.

Can I opt out of this feature?
Provisioning AWS Outposts into your AMS environment is optional. Once deployed into
your AMS account, AWS Outposts can be deprovisioned via the AWS Outposts console at any time,
if no longer needed.

How will AMS on AWS Outposts be billed?
AMS uplift on AWS Outposts charges will be applied at the Group B tier.

How will the AMS Service Level Agreement change to accommodate AWS Outposts?
Incident management will be contingent on AWS Outposts availability. AWS Outposts
availability is subject to customer network availability, which is the responsibility of the customer.
AWS Outposts availability is also subject to AWS Outposts hardware uptime, which is dependent on
AWS Outposts Service Level Agreements.

See also [AWS Outposts FAQs](https://aws.amazon.com/outposts/faqs/ "https://aws.amazon.com/outposts/faqs/").
