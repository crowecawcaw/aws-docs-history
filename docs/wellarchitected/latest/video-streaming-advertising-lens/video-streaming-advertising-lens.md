# Video Streaming Advertising Lens - AWS Well-Architected Framework

Publication date: **April 3, 2025** ([Document revisions](document-revisions.md "document-revisions.md"))

This paper describes the Video Streaming Advertising (VSA) Lens for the
AWS Well-Architected Framework. The lens explores how to review and
improve your cloud-based architectures and better understand the
impact of design decisions. We present general design principles and
specific best practices aligned to the six pillars of the
Well-Architected Framework. 

## Introduction

The AWS Well-Architected Framework helps cloud architects build
secure, high-performing, resilient, and efficient infrastructure for
their applications and workloads. The AWS Well-Architected Framework
is based on six pillars. The pillars are operational excellence,
security, reliability, performance efficiency, cost optimization and
sustainability. AWS Well-Architected provides a consistent approach for
customers and AWS Partners to evaluate architectures, remediate
risks, and implement designs that deliver business value.

In this lens, we focus on how to design, architect, and deploy your
advertising workloads in the AWS Cloud. We define components,
explore common workload scenarios, and outline design principles
that help you apply the AWS Well-Architected Framework. We recommend
that you begin designing your architecture by considering the best
practices and questions from the AWS Well-Architected Framework
whitepaper.

Operational challenges with the advertising workloads are:

- High traffic volumes with tens of millions of transactions per
  second.
- Low latency application and data retrieval responses with
  single-digit millisecond response time SLA.
- Rapid changes in traffic volumes and associated fluctuations in
  compute and network infrastructure.
- Data transfer is a significant part of overall operational costs
  and a focus area.
- Very low revenue (and profit margin) per transaction drives the
  focus on cost. Cost efficiency is the dominant design principle.
- End-to-end network latency impacts time available for response
  processing. Roundtrip latency of under 300 milliseconds is
  required to meet industry trading service-level objectives (SLOs).
- The use of 3rd party ISVs (independent software vendors) requires
  responses under two milliseconds to meet end-to-end processing
  SLAs.
- Rapid traffic changes require stateless and flexible
  infrastructure to facilitate automated up and down scaling of
  platform.
- Flexible supply and demand reduces redundancy requirements.

This lens specifies best practices that address the unique characteristics of building and operating advertising workloads in the cloud. They are based on our experience with industry developers and operations teams. It provides guidance on how to design and operate your environment addressing the operational challenges.

This document is intended for those in technology roles, such as chief technology officers (CTOs), Technical directors, architects, developers, and operations team members. After reading this document, you will understand AWS best practices and recommended strategies to use when designing and operating architectures for advertising workloads.

## Custom lens availability

Custom lenses extend the best practice guidance provided by AWS Well-Architected Tool. AWS WA Tool allows you to create your own
[custom
lenses](../userguide/lenses-custom.md "../userguide/lenses-custom.md") or to use lenses created by others that have been
shared with you.

To determine if a custom lens is available for the lens described
in this whitepaper, reach out to your Account Team or Support.
