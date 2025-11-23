# Security in Elastic Load Balancing

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a
data center and network architecture that are built to meet the requirements of the most
security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility
model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes this as security of the cloud and security in the cloud:

- **Security of the cloud** – AWS is responsible for
  protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also
  provides you with services that you can use securely. Third-party auditors regularly test
  and verify the effectiveness of our security as part of the [AWS compliance programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To learn about the compliance programs that
  apply to ELB, see [AWS services in scope by compliance program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** – Your responsibility is
  determined by the AWS service that you use. You are also responsible for other factors
  including the sensitivity of your data, your company's requirements, and applicable laws and
  regulations.
  This documentation helps you understand how to apply the shared responsibility model when
  using ELB. It shows you how to configure ELB to meet your security and compliance objectives.
  You also learn how to use other AWS services that help you to monitor and secure your ELB
  resources.

With a [Gateway Load Balancer](../gateway.md "../gateway.md"),
you are responsible for choosing and qualifying software from appliance vendors. You must trust
the appliance software to inspect or modify traffic from the load balancer, which operates at
the layer 3 of the Open Systems Interconnection (OSI) model, the network layer. The appliance
vendors listed as [ELB Partners](https://aws.amazon.com/elasticloadbalancing/partners/ "https://aws.amazon.com/elasticloadbalancing/partners/")
have integrated and qualified their appliance software with AWS. You can place a higher degree
of trust in the appliance software from vendors in this list. However, AWS does not guarantee
the security or reliability of software from these vendors.

###### Contents

- [Data protection](data-protection.md "data-protection.md")
- [Identity and
  access management](load-balancer-authentication-access-control.md "load-balancer-authentication-access-control.md")
- [Compliance validation](compliance-validation.md "compliance-validation.md")
- [Resilience](disaster-recovery-resiliency.md "disaster-recovery-resiliency.md")
- [Infrastructure security](infrastructure-security.md "infrastructure-security.md")
- [AWS PrivateLink](load-balancer-vpc-endpoints.md "load-balancer-vpc-endpoints.md")
