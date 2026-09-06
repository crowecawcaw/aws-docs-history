

# AWS managed security requirement packs
<a name="security-requirement-managed-packs"></a>

An AWS managed security requirement pack is a collection of security requirements that AWS creates and maintains, based on industry standards and best practices. You enable a managed pack to evaluate your applications against its requirements during design reviews and code reviews, without writing requirements yourself.

The security requirements in a managed pack are read-only. You cannot change them. You can use an AWS-managed requirement as a template to create a custom requirement, and then edit the copy to fit your organization. For more information, see [Manage security requirements](security-requirements.md).

 AWS updates managed packs over time. When AWS adds or revises a requirement in a managed pack, the change applies to every account that has the pack enabled.

**Note**  
The compliance framework packs are designed to help identify security requirements that may be relevant for compliance with certain frameworks. They do not assess your compliance or guarantee that you will pass an audit.

## AWS managed pack: ASA Base Pack
<a name="security-requirement-managed-packs-base"></a>

A baseline set of security requirements that apply to most workloads. This pack covers common application security concerns such as authentication and authorization, data protection, logging, and input validation. Enable this pack to establish a security baseline for your design and code reviews.

## AWS managed pack: AWS Well-Architected Pack
<a name="security-requirement-managed-packs-well-architected"></a>

Security requirements derived from the security pillar of the AWS Well-Architected Framework. This pack evaluates your application against AWS guidance for protecting data, managing identities and permissions, and detecting and responding to security events. For more information about the framework, see [Security Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).

## AWS managed pack: NIST CSF Pack
<a name="security-requirement-managed-packs-nist-csf"></a>

Security requirements derived from the NIST Cybersecurity Framework (CSF). This pack evaluates your application against control areas drawn from the framework, such as identity and access management, data security, and protective technology. Enable this pack to align your design and code reviews with NIST CSF.

## AWS managed pack: PCI DSS Pack
<a name="security-requirement-managed-packs-pci-dss"></a>

Security requirements derived from the Payment Card Industry Data Security Standard (PCI DSS). This pack evaluates your application against control areas relevant to handling cardholder data, such as access control, encryption of data in transit and at rest, and logging. Enable this pack to align your design and code reviews with PCI DSS.