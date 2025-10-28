# Reducing the Scope of Impact with Cell-Based Architecture

Publication date: **September 20, 2023** ([Document history](document-revisions.md "document-revisions.md"))

Today, modern organizations face an increasing number of challenges related to resiliency,
be they scalability or availability, especially when customer expectations shift to an
_always on, always available_ mentality. More and more, we have remote teams
and complex distributed systems, along with the growing need for frequent launches and an
acceleration of teams, processes, and systems moving from a centralized model to a distributed
model. All of this means that an organization and its systems need to be more resilient than
ever.

With the increasing use of cloud computing, sharing resources efficiently has become
easier. The development of multi-tenant applications is increasing exponentially, but although
the use of the cloud is more understood and customers are aware that they are in a multi-tenant
environment, what they still want is the experience of a single-tenant environment.

This guidance aims to demonstrate how to increase the resilience of critical applications,
bringing the same fault isolation concepts that AWS applies in its Availability Zones and
Regions to the level of your workload architecture. It expands one of the best practices from
the [AWS Well-Architected
Framework](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/"), [Use
bulkhead architectures to limit scope of impact](../reliability-pillar/rel_fault_isolation_use_bulkhead.md "../reliability-pillar/rel_fault_isolation_use_bulkhead.md"), to help you reduce the effect of
failures to a limited number of components.

## Introduction

Resilience is the ability for workloads—a collection of resources and code that delivers
business value, such as a customer-facing application or backend process—to respond and
quickly recover from failures.

At AWS, we strive to build, operate, and deliver extremely resilient services, and
build recovery mechanisms and mitigations, while keeping in mind that [everything fails all the time](https://www.allthingsdistributed.com/2016/03/10-lessons-from-10-years-of-aws.html "https://www.allthingsdistributed.com/2016/03/10-lessons-from-10-years-of-aws.html"). AWS provides different [isolation boundaries](../../../whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.md "../../../whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.md"), such as Availability Zones (AZs), AWS Regions, control
planes, and data planes. These are not the only mechanisms we use. For more than a decade, our
service teams have used cell-based architecture to build more resilient and scalable services.

Our service teams have a track record of developing services on a
global scale with high availability and one of the things that
contributes to this high availability and resiliency is the
[use
of cell-based architecture](https://www.youtube.com/watch?v=6IknqRZMFic "https://www.youtube.com/watch?v=6IknqRZMFic").

Every organization is at a different point in their resilience journey—some are just
beginning, while others might be more advanced and may require extreme levels of resilience in
their applications. For these types of applications, this guidance can help you increase the
resiliency of your applications and increase the trust of your services with your customers.
Cell-based architecture can give your workload more fault isolation, predictability, and
testability. These are fundamental properties for workloads that need extreme levels of
resilience.

## Are you Well-Architected?

The
[AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/") helps you understand the pros
and cons of the decisions you make when building systems in the
cloud. The six pillars of the Framework allow you to learn
architectural best practices for designing and operating reliable,
secure, efficient, cost-effective, and sustainable systems. Using
the
[AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/ "https://aws.amazon.com/well-architected-tool/"), available at no charge in the
[AWS Management Console](https://console.aws.amazon.com/wellarchitected "https://console.aws.amazon.com/wellarchitected"), you can review your workloads against
these best practices by answering a set of questions for each
pillar.
