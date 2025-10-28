# Financial Services Industry Lens - AWS Well-Architected Framework

Publication date: **May 15, 2024** ([Document revisions](document-revisions.md "document-revisions.md"))

This document describes the Financial Services Industry Lens for the AWS Well-Architected
Framework. The document describes general design principles, as well as specific best practices
and guidance for the six pillars of the Well-Architected Framework.

## Introduction

The financial services industry includes financial services firms, independent software
vendors (ISVs), market utilities, and infrastructures that supply essential services to
countries around the world. The industry consists of organizations that provide the main
mechanisms for:

- Paying for goods and services
- Financial markets and asset trading
- Serving as intermediates between savers and borrowers (channeling savings into
  investment)
- Insuring against and dispersing risk

The [AWS Well-Architected
Framework](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/") helps you understand the pros and cons of decisions you make while
building systems on AWS. By using the Framework, you learn architectural best practices for
designing and operating reliable, secure, efficient, cost-effective, and sustainable systems
in the cloud. The Framework provides a way for you to consistently measure your architectures
against best practices and identify areas for improvement. We believe that having well
architected systems greatly increases your security, reliability, and the likelihood of
business success.

In this lens, we focus the Well-Architected Framework on how to design, deploy, and
architect financial services industry (FSI) workloads that promote the resiliency, security,
cost savings, and operational performance in line with risk and control objectives that you
define, including those that help you align with the regulatory and compliance requirements of
supervisory authorities.

All customers should begin with the best practices and questions outlined in the [AWS
Well-Architected Framework whitepaper](../framework/welcome.md "../framework/welcome.md"). This document provides additional best
practices that are focused on the technical architectures and workloads that are associated
with financial services institutions.

The Financial Services Industry Lens identifies best practices for security, data privacy,
and resiliency that are intended to address the requirements of financial institutions based
on our experience working with financial institutions worldwide. It provides guidance on
guardrails for technology teams to implement and confidently use AWS to build and deploy
applications. This Lens describes the process of building transparency and auditability into
your AWS environment. It also offers suggestions for controls to help you expedite adoption
of new services into your environment while managing the cost of your IT services.

This document is intended for those in technology leadership roles, such as chief
technology officers (CTOs), architectural leadership, developers, engineers, and operations
team members, as well as individuals in the risk, compliance, and audit functions.

## Lens availability

The Financial Services Industry Lens is available as an AWS-official lens in the [Lens Catalog](../userguide/lens-catalog.md "../userguide/lens-catalog.md") of the [AWS Well-Architected Tool](../userguide/intro.md "../userguide/intro.md").

To get started, follow the steps in [Adding a lens to a workload](../userguide/lenses-add.md "../userguide/lenses-add.md") and select the **Financial Services Industry Lens**.
