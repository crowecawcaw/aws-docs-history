# Migration Lens - AWS Well-Architected Framework

Publication date: **January 24, 2024** ([Document revisions](document-revisions.md "document-revisions.md"))

This whitepaper describes the Migration Lens for the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/"). It provides AWS customers with a set of Well-Architected best practices and guidance on the migration of their on-premises or hybrid workloads into a fully cloud-based implementation.

## Introduction

The three phases of an AWS Migration consist of _assess_, _mobilize_, and _migrate and modernize_. The Well-Architected Framework superimposes the six pillars (operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability) to help you reduce your cloud migration and implementation risks.

In doing so, the Migration Lens combines the three phases of migration (assess, mobilize, and migrate and modernize) and the six pillars of the AWS Well-Architected Framework, and serves as a foundational guidance for migration best practices that customers can reference to evaluate the decisions they make on their migration and measure them against AWS best practices.

The AWS Well-Architected Framework helps you understand the pros and cons of decisions you make while building systems on AWS. Using the Framework, you can learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems in the cloud. It provides a way for you to measure your architectures against best practices and identify areas for improvement. We believe that having well-architected systems greatly increases the likelihood of business success.

One of the first decisions to make when you start thinking about migrating workloads to the cloud is to decide your migration strategy. A migration strategy is the approach used to move applications to the cloud, also known as the _7 Rs_: _retire, retain, rehost, relocate, repurchase, replatform,_ and _refactor_. For more details on each R, see [Definitions](definitions.md "definitions.md").

The Migration Lens focuses specifically on rehost, relocate, replatform, and retire migration strategies. The refactor strategy involves modernizing the application during the migration. These topics are addressed in other AWS publications.
For brevity, we have only covered details from the [Well-Architected Framework](../framework/the-pillars-of-the-framework.md "../framework/the-pillars-of-the-framework.md") that are specific to migration. Consider best practices and questions that have not been included in this document when designing your architecture. We recommend that you complete a full Well-Architected Framework Review (WAFR) prior to performing this AWS Migration Lens review.

This lens whitepaper is intended for those in technology roles, such as chief technology officers (CTOs), architects, developers, and operations team members. After reading this paper, you should understand AWS best practices and strategies to use when migrating workloads to the AWS Cloud.

## Lens availability

The Migration Lens is available as an AWS-official lens in the [Lens Catalog](../userguide/lens-catalog.md "../userguide/lens-catalog.md") of the [AWS Well-Architected Tool](../userguide/intro.md "../userguide/intro.md").

To get started, follow the steps in [Adding a lens to a workload](../userguide/lenses-add.md "../userguide/lenses-add.md") and select the **Migration Lens**.
