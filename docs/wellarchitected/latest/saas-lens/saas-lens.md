# SaaS Lens

Publication date: **April 4, 2023** ([Document revisions](document-revisions.md "document-revisions.md"))

This paper describes the SaaS Lens for the
**AWS Well-Architected Framework**,
which enables customers to review and improve their cloud-based
architectures and better understand the business impact of their
design decisions. We address general design principles as well as
specific best practices and guidance in five conceptual areas that
we define as the pillars of the
Well-Architected Framework.

## Introduction

The
[AWS
Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/") helps you understand the pros and
cons of decisions you make while building systems on AWS. By using
the Framework you will learn architectural best practices for
designing and operating reliable, secure, efficient, and
cost-effective systems in the cloud. It provides a way for you to
consistently measure your architectures against best practices and
identify areas for improvement. We believe that having
well-architected systems greatly increases the likelihood of
business success.

In this “Lens” we focus on how to design, deploy, and architect your
multi-tenant software as a service (SaaS) application workloads in the AWS Cloud. For
brevity, we have only covered details from the Well-Architected
Framework that are specific to SaaS workloads. You should still
consider best practices and questions that have not been included in
this document when designing your architecture. We recommend that
you read the
[AWS
Well-Architected Framework whitepaper](../framework/welcome.md "../framework/welcome.md").

This document is intended for those in technology roles, such as
chief technology officers (CTOs), architects, developers, and
operations team members. After reading this document, you will
understand AWS best practices and strategies to use when designing
architectures for SaaS applications.

## Lens availability

The SaaS Lens is available as an AWS-official lens in the [Lens Catalog](../userguide/lens-catalog.md "../userguide/lens-catalog.md") of the [AWS Well-Architected Tool](../userguide/intro.md "../userguide/intro.md").

To get started, follow the steps in [Adding a lens to a workload](../userguide/lenses-add.md "../userguide/lenses-add.md") and select the **SaaS Lens**.
