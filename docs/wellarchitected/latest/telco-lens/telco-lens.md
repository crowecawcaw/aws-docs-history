# Telco Lens - AWS Well-Architected

Publication date: **December 30, 2025** ([Document revisions](document-revisions.md "document-revisions.md"))

This paper describes the Telco Lens for the AWS Well-Architected
Framework. The lens explores how to review and improve your cloud-based architecture for
telecommunications workloads and better understand the impact of design decisions. We present
general design principles and specific best practices aligned to the six pillars of the
Well-Architected Framework.

## Telco-specific challenges

The Telco Lens addresses unique operational challenges in
telecommunications workloads:

- High traffic volumes with millions of transactions per second
- Low latency application and data retrieval responses with stringent service level
  agreements (SLAs)
- Rapid changes in traffic volumes and infrastructure scaling requirements
- Significant data transfer costs as a proportion of overall operational costs
- Need for cost efficiency and optimization due to low profit margins per transaction
- Strict end-to-end network latency requirements to meet industry service level
  objectives (SLOs)

## Industry context

The telecommunications industry encompasses wireless and wireline service providers,
independent software vendors (ISVs), and network equipment providers (NEPs) that deliver
essential communication and connectivity services globally. This sector comprises companies
transmitting data, voice, audio, and video worldwide.

## Purpose of this lens

The Telco Lens provides:

1. Best practices for designing and operating telecommunications workloads in AWS
2. Guidance on building resiliency and sustainability into your AWS environment
3. Recommendations for performance, data privacy, and security
4. Strategies to assist communication service providers (CSPs) meet industry-specific
   requirements
5. Controls to expedite adoption of new services into your environment

## Target audience

This document serves technology roles such as CTOs, architects, developers, and
operations teams working on telco workloads. It will assist you to understand AWS best
practices and strategies for designing and operating telco architectures aligned with the
Well-Architected Framework.

## Lens availability

Custom lenses extend the best practice guidance provided by AWS Well-Architected Tool. AWS WA Tool allows you
to create your own [custom lenses](../userguide/lenses-custom.md "../userguide/lenses-custom.md"), or to use
lenses created by others that have been shared with you.

To begin reviewing your telco workload, download and import the [Telco Lens](https://github.com/aws-samples/sample-well-architected-custom-lens/blob/main/telco-lens/telco-lens.json "https://github.com/aws-samples/sample-well-architected-custom-lens/blob/main/telco-lens/telco-lens.json") into AWS Well-Architected Tool from the public [AWS
Well-Architected custom lens GitHub repository](https://github.com/aws-samples/sample-well-architected-custom-lens "https://github.com/aws-samples/sample-well-architected-custom-lens").
