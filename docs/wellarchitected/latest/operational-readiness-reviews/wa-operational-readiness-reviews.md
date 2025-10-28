# Operational Readiness Reviews (ORR)

Publication date: **June 30, 2022** ([Document history](document-revisions.md "document-revisions.md"))

Amazon Web Services (AWS) created the Operational Readiness Review (ORR) to distill the learnings
from AWS operational incidents into curated questions with best practice guidance. This
document is intended to help you understand how the AWS ORR program was built and guide you in
creating your own ORR program as part of the AWS Well-Architected Framework. Creating an ORR
program can help supplement Well-Architected reviews by including lessons learned that are
specific to your business, culture, tools, and governance rules.

## Introduction

At AWS, we strive to build and operate highly resilient services, keeping in mind that
[everything fails all the time](https://www.allthingsdistributed.com/2016/03/10-lessons-from-10-years-of-aws.html "https://www.allthingsdistributed.com/2016/03/10-lessons-from-10-years-of-aws.html"). When failures happen, we use a closed-loop mechanism
called [Correction of
Errors](https://aws.amazon.com/blogs/mt/why-you-should-develop-a-correction-of-error-coe/ "https://aws.amazon.com/blogs/mt/why-you-should-develop-a-correction-of-error-coe/") (COE) to perform a post-incident analysis of any event of significance, even
if customers don’t see an impact. The focus of a COE is preventing the reoccurrence of that
event in the workload where it happened by generating action items specific to that workload
and event.

However, we also want to stop preventable, known risks that we’ve identified in the COE
process from occurring in other workloads. We, like so many of our customers, can’t afford to
slow the pace of innovation; developer speed and agility is critical to our business. And
given AWS’s decentralized operational culture, we needed to create a scalable, self-service
mechanism to share and enforce the best practices learned from our COE analysis without
slowing builders down.

To do that, we created the Operational Readiness Review (ORR). The ORR program distills
the learnings from AWS operational incidents into curated questions with best practices
guidance. This enables builders to create highly available, resilient systems without sacrificing
agility and speed. ORR questions uncover risks and educate service teams on the implementation of best
practices to prevent the reoccurrence of incidents through removing common causes of impact.
We generate different checklist templates from these questions based on the workload being
reviewed and the outcome we want to achieve. Teams perform self-assessments on operational
risks to achieve operational excellence by reviewing the appropriate ORR checklist throughout
the complete lifecycle of their service, from inception to post-release operations. ORRs helps
us achieve _shorter_, _fewer_, and
_smaller_ incidents. It uses a data-driven approach for reducing risk and
improving the availability and resilience of our systems.

The focus of this paper is to help you understand how to build an ORR program and develop
your own checklist questions to support both the [Operational
Excellence](../operational-excellence-pillar/operational-readiness.md "../operational-excellence-pillar/operational-readiness.md") and [Reliability](../reliability-pillar/resiliency-and-the-components-of-reliability.md "../reliability-pillar/resiliency-and-the-components-of-reliability.md") pillars
of the [AWS Well-Architected
Framework](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected"). The core value proposition of the ORR is using the data from your own
post-incident analysis to generate best practices. Creating an ORR program can help supplement
Well-Architected reviews by including lessons learned that are specific to your business,
culture, tools, and governance rules. ORR is a complementary process to Well-Architected,
using a data-driven approach to ensure a consistent review of operational readiness, with a
specific focus on eliminating known, common causes of impact in your workloads.

## Are you Well-Architected?

The [AWS Well-Architected
Framework](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/") helps you understand the pros and cons of the decisions you make when
building systems in the cloud. The six pillars of the Framework allow you to learn
architectural best practices for designing and operating reliable, secure, efficient,
cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/ "https://aws.amazon.com/well-architected-tool/"), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected "https://console.aws.amazon.com/wellarchitected"), you can review your
workloads against these best practices by answering a set of questions for each pillar.
