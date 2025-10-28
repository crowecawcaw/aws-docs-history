# Container Build Lens

Publication date: **October 20, 2022** ([Document revisions](document-revisions.md "document-revisions.md"))

This whitepaper describes the Container Build Lens for the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/"). It helps
customers review and improve their cloud-based architectures and better understand the business
impact of their design decisions. The document describes general design principles, as well as
specific best practices and implementation guidance using the six pillars of the
Well-Architected Framework.

This lens whitepaper is intended for those in technology roles,
such as chief technology officers (CTOs), architects, developers,
and operations team members. After reading this paper, you will understand AWS best practices and the strategies to use when designing container images.

## Introduction

The AWS Well-Architected Framework helps you understand the pros and cons of decisions you make while building systems on AWS. Using the framework, you will learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems in the cloud. It provides a way for you to measure your architectures against best practices and identify areas for improvement. We know that having well-architected systems greatly increases the likelihood of business success.

Two of the components that make up the Well-Architected Container Build Lens are the
whitepaper and implementation guidance document. The lens whitepaper provides cloud-agnostic
questions and best practices on how to build and manage containers and container images. In
addition, the paper offers implementation guidance by providing examples for building and
managing containers and container images in the AWS Cloud. 

The Container Build Lens will focus specifically on the container design and build process.
Topics such as best practices for container orchestration architecture design principles and
general best practices in software development are considered out of scope for this lens.
These topics are addressed in other AWS publications. See the **Resources** sections under [Pillars of the Well-Architected Framework](pillars-of-the-well-architected-framework.md "pillars-of-the-well-architected-framework.md") for more information.

For brevity, we have only covered details from the Well-Architected Framework that are
specific to containerized build processes. Consider best practices and questions that have not
been included in this document when designing your architecture. We recommend that you read
the [AWS
Well-Architected Framework whitepaper](../framework/welcome.md "../framework/welcome.md"). This document is intended for those in
technology roles (such as developers, architects, and engineers) who wish to understand the
fundamental architectural concepts when building and managing containerized applications and
container images in AWS Cloud. The lens helps technologists follow a set of established
AWS well-architected best practices.

## Lens availability

The Container Build Lens is available as an AWS-official lens in the [Lens Catalog](../userguide/lens-catalog.md "../userguide/lens-catalog.md") of the [AWS Well-Architected Tool](../userguide/intro.md "../userguide/intro.md").

To get started, follow the steps in [Adding a lens to a workload](../userguide/lenses-add.md "../userguide/lenses-add.md") and select the **Container Build Lens**.
