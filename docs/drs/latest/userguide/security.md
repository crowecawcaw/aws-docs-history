# Security in AWS Elastic Disaster Recovery

## Overview

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a
data center and network architecture that is built to meet the requirements of the most
security-sensitive organizations.

Security is a shared responsibility between AWS and you. The
[shared responsibility
model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")

describes this as security of the cloud and security in the cloud:

- **Security of the cloud** – AWS is
  responsible for protecting the infrastructure that runs AWS services in the AWS
  Cloud. AWS also provides you with services that you can use securely.
  Third-party auditors regularly test and verify the effectiveness of our security
  as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/")

. To learn about the
compliance programs that apply to AWS Elastic Disaster Recovery (AWS DRS), see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/")
.

- **Security in the cloud** – Your responsibility is
  determined by the AWS service that you use. You are also responsible for other factors
  including the sensitivity of your data, your company’s requirements, and applicable laws
  and regulations

This documentation helps you understand how to apply the shared responsibility model
when using AWS DRS. It shows you how to configure AWS DRS to meet your security and
compliance objectives. You also learn how to use other AWS services that help you to
monitor and secure your AWS Elastic Disaster Recovery resources.

The customer is responsible for making sure that no misconfigurations are present
during and after the recovery process, including:

1. The replication server should be accessed only from the CIDR range of the source servers.
   Proper security groups rules should be assigned to the replication server after it is
   created.
2. After the recovery, the customer should make sure that on the recovery
   instances only allowed ports are exposed to the public internet.
3. Hardening of OS packages and other software deployed in the recovery instances
   is completely under the customer’s responsibility and we recommend the
   following:
   1. Packages should be up to date and free of known vulnerabilities.
   2. Only necessary OS/application services should be up and running.

4. Activating the Anti-DDOS protection (AWS Shield) in the customer's AWS Account
   to eliminate the risk of denial of service attacks on the replication servers as
   well as the migrated servers.
