# AOSPERF05-BP02 Enable a dedicated coordinator node for

OpenSearch Service domain

Improve resource utilization and resilience by enabling a dedicated
coordinator node, reducing private IP address reservations

**Level of risk exposed if this best practice
is not established**: High

**Desired outcome**: You use a
dedicated coordinator node for an OpenSearch Service domain to improve
resource utilization, enhance resilience, and reduce private IP
address reservations.

**Benefits of establishing this best
practice:**

- **Improve resource utilization**:
  Enabling a dedicated coordinator node in your OpenSearch Service domain can improve resource utilization by relieving
  data nodes from coordination responsibilities, allowing them to
  focus on core tasks like search, data storage, and indexing.
- **Enhance domain resiliency**:
  With a dedicated coordinator node, you can also enhance the
  resiliency of your OpenSearch Service domain by reducing the risk of
  resource (memory and CPU) strain on data nodes that are hosting
  OpenSearch Dashboards.
- **Reduce private IP addresses
  reservation**: Provisioning a dedicated coordinator
  node can help reduce the reservation of private IP addresses
  required for virtual private cloud (VPC) domains, making it
  easier to manage your domain's resources.

## Implementation guidance

The following are general guidelines that apply to many use cases.
Each workload is unique, with unique characteristics, so no
generic recommendation is exactly right for every use case.

- General-purpose instances are enough for most of the use
  cases.
- Keep the instance family the same for a dedicated coordinating
  node and data node.
- It is recommended to provision 5% to 10% of your domain's
  total data nodes as dedicated coordinator nodes. For example,
  if your domain has 90 R6g.large data nodes, you can plan for
  coordinator nodes to make up anywhere between 5 and 9 of the
  R6g.large instance type.
- As a starting point, the instance size of your dedicated
  coordinator nodes should be the same as your domain's data
  nodes. However, in certain cases, it may be advisable to use a
  smaller instance type with a higher count to ensure
  availability. For example, if you have R6g.8xlarge as the
  instance size for a data node, you can try 3 instances of
  R6g.2xlarge size instead of one R6g.8xlarge size to achieve
  better availability.
- Source domains typically do not perform coordination tasks. If
  you are using cross region search, it is recommended you
  provision a dedicated coordinator node on the destination
  domains.

### Implementation steps

- Log in to the
  [AWS Management Console](https://console.aws.amazon.com "https://console.aws.amazon.com").
- Navigate to the Amazon OpenSearch Service console.
- Create a new domain or modify an existing domain:
  - For a new domain, choose **Create domain**. For an existing domain, select the domain name and choose **Actions**, then **Edit cluster configuration**..

- Enable dedicated coordinator nodes:
  - In the Cluster configuration section, under Dedicated
    coordinator nodes, toggle on the option to enable
    dedicated coordinator nodes.

- Choose coordinator node instance type and count. Follow the
  recommendations mentioned in the implementation guidance for
  this best practice.
- After configuring the settings, review your setup and choose
  **Create** (for a new domain) or **Save changes** (for an
  existing domain).
