# Streaming Media Lens

Publication date: **September 29, 2021** ([Document history and contributors](document-history.md "document-history.md"))

This whitepaper describes the AWS Streaming Media Lens for the AWS
Well-Architected Framework, which helps customers apply best
practices in the design, delivery, and maintenance of their
cloud-based streaming media workloads. The document describes
general design principles, as well as specific best practices and
guidance for the six pillars of the Well-Architected Framework.

This paper is intended for those in technology roles, such as
technology leaders, architects, developers, and operations team
members. After reading this paper, you will understand AWS best
practices and the strategies to use when designing and operating
streaming media workloads in a cloud environment.

## Introduction

The AWS Well-Architected Framework helps cloud architects build
secure, high-performing, resilient, and efficient infrastructure for
their applications and workloads. Based on six pillars —
operational excellence, security, reliability, performance
efficiency, cost optimization, and sustainability — AWS Well-Architected provides a
consistent approach for customers and AWS Partners to evaluate
architectures, remediate risks, and implement designs that deliver
business value.

In this Lens, we focus on how to design and deploy **streaming
media** workloads by defining components, exploring common workload scenarios, and
outlining design principles that help you to apply the AWS Well-Architected Framework. We
then address specific best practices aligned with the pillars of the Well-Architected
Framework.

Streaming media workloads transmit audio and video from content
publishers to audiences. Streaming media is typically used for
one-to-many broadcasts to audiences over HTTP. Readers interested in
real-time communications for web conferencing applications should
refer to the
[Real-Time
Communication on AWS whitepaper](../../../whitepapers/latest/real-time-communication-on-aws/welcome.md "../../../whitepapers/latest/real-time-communication-on-aws/welcome.md").

For brevity, we only cover details from the
Well-Architected Framework that are specific to streaming media
workloads. We recommend that you start by considering best practices
and questions from the
[AWS Well-Architected Framework whitepaper](../framework/welcome.md "../framework/welcome.md") when designing your
architecture.

## Lens availability

The Streaming Media Lens is available as an AWS-official lens in the [Lens Catalog](../userguide/lens-catalog.md "../userguide/lens-catalog.md") of the [AWS Well-Architected Tool](../userguide/intro.md "../userguide/intro.md").

To get started, follow the steps in [Adding a lens to a workload](../userguide/lenses-add.md "../userguide/lenses-add.md") and select the **Streaming Media Lens**.
