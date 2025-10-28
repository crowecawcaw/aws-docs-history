# Infrastructure deployment components

What are all the different components that will need configuring to support your application?

- Region: What AWS Region or Regions are needed?
- High Availability (HA): What Availability Zones will be used?
- Virtual Private Cloud (VPC): What is the CIDR block for the VPC?
- What server instances are needed?
  - Authenticated Reverse Proxy (ARP): OS, AMI, instance type, subnet ID, security group, ingress
    port?
  - Application Deployment Tool server: OS, AMI, instance type, subnet ID, security group, ingress
    port (Chef, Puppet) or egress port (Ansible, Saltstack) port?
  - Amazon RDS with MySQL: DB version, Usage Type, instance class, subnet ID, security group, DB instance ID, storage size, Multi-AZ, Auth type, encryption?
  - Storage: Is your app stateless? Do you require S3 buckets? Do you require persistent storage? Do you require data at rest encryption on your EBS volumes?
    Do you require DB encryption?
  - External (to the Managed Services VPC) server endpoints: SMTP? LDAP?
  - Network requirements: Network filtering (based on security groups?)? Web traffic inspection
    (inbound?outbound?)?

- Tagging: What tags should be used to group resources into logical collections? For example,
  all resources for an application stack. Select tags for your use case; for
  example, `backup=true` to enable backups. Additionally, you must use
  the tag `name=value` in order for any EC2 instances you create to
  display a name in the console.
- Security groups:
  - What security groups are needed?
  - Security group ingress rules?
  - Security group egress rules?
