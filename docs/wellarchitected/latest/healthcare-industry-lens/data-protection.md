# Data protection

| HCL_SEC6. How do you determine and<br>enforce data residency requirements? |
| -------------------------------------------------------------------------- |
|                                                                            |

**Determine applicable
regulatory frameworks and controls as it pertains to data
locality**

Many healthcare organizations fall under data locality
requirements or regulations on where data may be physically
located.  Begin by reviewing these requirements within any
applicable regulatory frameworks. To determine applicable
regulatory frameworks, start with local regulations and
frameworks for the country where your sensitive healthcare
data is generated, hosted, and processed. Engage with legal
counsel who can help you define the scope of the local
regulations, as well as any additional regulation frameworks
that may apply to you.

**Enforce data locality
requirements by implementing controls**

Once the determination of requirements has been made and
documented, technical controls can be put in place to enforce
them.

The AWS Cloud spans many Availability Zones and geographic
Regions around the world. Each AWS Region is fully isolated,
and comprised of multiple Availability Zones. You can choose
to use one or many AWS Regions in your environment. AWS stores
and processes your content in the AWS Regions you select,
using the services you select. AWS will not move your content
without your consent, except as legally required. This allows
you to establish environments in a location or locations of
their choice. For example, AWS customers in Germany can choose
to deploy their AWS services exclusively in one AWS Region,
such as the Europe (Frankfurt) Region, and store their content
onshore in Germany.

AWS also provides mechanisms for customers to allow or deny
access to specific Regions.  When using AWS Organizations,
implement service control policies (SCP) to limit access to
specific AWS services or resources. SCPs can be used with
[AWS Control Tower data residency controls](https://aws.amazon.com/about-aws/whats-new/2021/11/aws-control-tower-controls-data-residency-requirements/ "https://aws.amazon.com/about-aws/whats-new/2021/11/aws-control-tower-controls-data-residency-requirements/") to create
additional guardrails to enforce data locality requirements.
Continuing the example above, you can implement a service
control policy that allows only access to the Europe
(Frankfurt) Region and denies access to all others.  A sample
service control policy, or SCP, can be found
[here](../../../organizations/latest/userguide/orgs_manage_policies_scps_examples_general.md "../../../organizations/latest/userguide/orgs_manage_policies_scps_examples_general.md").
Additionally, if you are using AWS Control Tower, implement
the [Region
deny guardrail](../../../controltower/latest/userguide/region-deny.md "../../../controltower/latest/userguide/region-deny.md") to deny access to specific Regions.

| HCL_SEC7. How are you protecting<br>health data at rest and in transit? |
| ----------------------------------------------------------------------- |
|                                                                         |

**Encrypt sensitive health
data at rest and in transit at all times**

Protect all sensitive data stored and transmitted within a
cloud environment with AWS encryption services. The AWS
Business Associate Addendum (BAA), applicable to customers who
align with the Health Insurance Portability and Accountability
Act (HIPAA), requires the encryption of protected health
information (PHI) as defined by HIPAA at rest and in transit.
Encryption at rest and in transit may be required by other
applicable frameworks.

As documented in the
[data
encryption](../../../whitepapers/latest/introduction-aws-security/data-encryption.md "../../../whitepapers/latest/introduction-aws-security/data-encryption.md") section of the
[Introduction
to AWS Security](../../../whitepapers/latest/introduction-aws-security/welcome.md "../../../whitepapers/latest/introduction-aws-security/welcome.md") whitepaper and the
[Encrypting
Data-at-Rest and -in-Transit](../../../whitepapers/latest/logical-separation/encrypting-data-at-rest-and--in-transit.md "../../../whitepapers/latest/logical-separation/encrypting-data-at-rest-and--in-transit.md") section of the
[Logical
Separation on AWS](../../../whitepapers/latest/logical-separation/welcome.md "../../../whitepapers/latest/logical-separation/welcome.md") whitepaper, AWS allows you to add a
layer of security to your data at rest in the cloud, providing
scalable and efficient encryption features. These include:

- Data at rest encryption capabilities available in most AWS
  services, such as Amazon Elastic Block Store (Amazon EBS),
  Amazon S3, Amazon RDS, Amazon Redshift, Amazon ElastiCache, AWS Lambda, and Amazon SageMaker AI
- Flexible key management options, including AWS Key Management Service (AWS KMS), that allow you to choose
  whether to have AWS manage the encryption keys or enable
  you to keep complete control over your own keys
- Dedicated, hardware-based cryptographic key storage using
  AWS CloudHSM, allowing you to help satisfy your compliance
  requirements
- Encrypted message queues for the transmission of sensitive
  data using server-side encryption (SSE) for Amazon Simple Queue Service (Amazon SQS)

In addition, AWS provides APIs for you to integrate encryption
and data protection with any of the services you develop or
deploy in an AWS environment.

**Implement encryption
controls as part of the infrastructure
architecture**

Use infrastructure as code to declare encryption as a
configuration when creating an environment template. Use
alerts and automated remediation, where possible, with AWS Config that can detect when a resource is not configured to
use encryption. Where automated remediation is not available,
verify that alerts are generated and sent to the appropriate
parties.

Amazon EBS, block-storage for use with Amazon EC2 Auto Scaling, uses AWS KMS keys to encrypt storage
volumes and snapshots. Encryption operations occur on the
servers that host Amazon EC2 instances, ensuring the security of data
at rest and data in transit between an instance and attached
Amazon EBS volumes. Consider configuring your AWS accounts for Amazon EBS
[encryption
by default](../../../AWSEC2/latest/UserGuide/EBSEncryption.md "../../../AWSEC2/latest/UserGuide/EBSEncryption.md"), enforcing that any created Amazon EBS volumes are
encrypted automatically.

Amazon RDS uses configuration policies that can enforce
encrypted connections to a hosted database. The Amazon RDS
documentation contains information on
[using
SSL/TLS to encrypt a connection to the database](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md"),
including options for enforcing the connection through either
parameter groups (Amazon RDS for Postgres, Aurora for Postgres, Amazon RDS
for MariaDB, or Amazon RDS for Microsoft SQL Server) or option groups
(Amazon RDS for Oracle).

Amazon S3 buckets that may contain health data should be configured
to require secure connections with the use of a bucket policy,
and require encryption of data at rest. Below is an example of
a bucket policy that explicitly denies access when a secure
transport connection is not used:

JSON

```


```

Encryption in transit between systems must be identified and
enforced where possible. AWS services provide HTTPS endpoints
using TLS for communication, providing encryption in transit
when communicating with the AWS APIs. Insecure protocols, such
as HTTP, can be blocked in a VPC through the use of security
groups. HTTP requests can also be
[automatically
redirected to HTTPS](../../../AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.md "../../../AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.md") in Amazon CloudFront or on an
[Application Load Balancer](../../../elasticloadbalancing/latest/application/load-balancer-listeners.md "../../../elasticloadbalancing/latest/application/load-balancer-listeners.md").

When hosting applications on Amazon EC2 instances, use open standard
transport encryption mechanisms such as Transport Layer
Security (TLS) to encrypt data during transit between
instances and endpoints. Certain Amazon EC2 instance types can
offload encrypting traffic between instances to the underlying
Nitro System hardware, using Authenticated Encryption with
Associated Data (AEAD) algorithms with 256-bit encryption. For more detail and a list of supported instance
types, see [encryption
in transit](../../../AWSEC2/latest/UserGuide/data-protection.md "../../../AWSEC2/latest/UserGuide/data-protection.md").

Microservice architectures should also consider controls to
enforce encryption of data between services when hosting and
processing health data. AWS App Mesh, a service mesh that
makes it easy to monitor and control service, features
Transport Layer Security (TLS) encrypts communication between
the Envoy proxies deployed on compute resources that are
represented in App Mesh. When the proxy is deployed with an
application, your application code is not responsible for
negotiating a TLS session. The proxy negotiates TLS on your
application's behalf. For more detail, see
[Transport
Layer Security (TLS)](../../../app-mesh/latest/userguide/tls.md "../../../app-mesh/latest/userguide/tls.md").

| HCL_SEC8. How do you isolate<br>sensitive data? |
| ----------------------------------------------- |
|                                                 |

**Isolate health data from
non-health data**

Organizations working with health data should take steps to
isolate and segment health data from non-health data. In
conjunction with the recommendations around data discovery and
classification, it is important to separate health data so the
organization can implement the necessary technical and
administrative controls.

Isolation can be accomplished through a variety of methods
depending on the cloud environment. AWS recommends beginning
with using multiple AWS accounts and designating specific
accounts as containing health data. AWS accounts provide a
level of segmentation that allows strict controls to be put in
place for workloads that host and process health data.
[AWS Organizations](../../../organizations.md "../../../organizations.md"), an account management service that
enables you to consolidate multiple AWS accounts into an
organization that you create and centrally manage, provides
management capabilities that allow you to group like accounts
into organizational units (OUs) and apply policies at the OU
level. This verifies that all accounts within that OU are
using a standardized set of policies and controls, which can
help organizations align to their specific compliance needs.

Furthermore, as outlined in the
[Organizing
Your AWS Environment Using Multiple Accounts
whitepaper](../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md "../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md"), when you limit sensitive data stores to an
account that is built to manage it, you can more easily
constrain the number of people and processes that can access
and manage the data. This approach simplifies the process of
achieving least privilege access. Limiting access at the
coarse-grained level of an account helps contain exposure to
highly sensitive data.

**Limit access to health
data**

It is also important to limit access to health data within an
account. Use resource isolation, such as designated Amazon S3
buckets, to separate health data from non-health data.
Resource isolation can also be used to isolate tenants and
tenant-specific data. Resource isolation and tenant isolation
reinforce the benefits to account isolation, limiting access
to sensitive data to only the people and systems that require
it, without unnecessarily blocking access to less sensitive
data. Refer to the Security pillar section of the
[Well-Architected
Framework SaaS Lens](../saas-lens/saas-lens.md "../saas-lens/saas-lens.md") for additional recommendations on
tenant isolation.

Tagging allows limiting access to specific resources through
the use of
[conditional
statements](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in IAM policies. By adding a specific
resource tag to an IAM policy, such as `data type: health`,
organizations can allow or deny access to resources with that
tag. This approach adds an additional layer of authorization
to resources that host and process health data.
