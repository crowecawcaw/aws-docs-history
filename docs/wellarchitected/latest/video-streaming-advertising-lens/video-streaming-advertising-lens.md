

# Video Streaming Advertising Lens - AWS Well-Architected Framework
<a name="video-streaming-advertising-lens"></a>

 Last update **November 10, 2026** ([Release notes](release-notes.md)) 

 The AWS Well-Architected Framework helps cloud architects build secure, high-performing, resilient, and efficient infrastructure for their applications and workloads. It is based on six pillars: operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability. The framework provides a consistent approach for customers and AWS Partners to evaluate architectures, remediate risks, and implement designs that deliver business value. 

 In this lens, we focus on how to design, architect, and deploy your advertising workloads in the AWS Cloud. We define components, explore common workload scenarios, and outline design principles that help you apply the AWS Well-Architected Framework to the unique challenges of programmatic advertising: millisecond latency budgets, petabyte-scale data volumes, privacy regulation compliance, and the operational demands of continual ad-supported streaming. 

## Introduction
<a name="introduction"></a>

 This lens is intended for architects, engineers, and technical decision-makers who design and operate advertising technology workloads on AWS. It covers the full spectrum of modern advertising workloads: real-time bidding infrastructure, data pipelines, privacy-enhanced collaboration, FAST channel playout, server-guided ad insertion, agentic AI for advertising automation, and converged linear/digital operations. 

### Who can use this guidance
<a name="who-can-use-this-guidance"></a>

 This document is intended for those in technology roles such as chief technology officers (CTOs), technical directors, architects, developers, and operations team members who build and run: 
+  Supply-side platforms (SSPs), ad exchanges, and demand-side platforms (DSPs) 
+  Programmatic advertising infrastructure handling real-time bidding 
+  Publisher systems delivering FAST channels, SGAI, and innovative ad formats 
+  Data and measurement systems for advertising analytics and attribution 
+  Privacy-enhanced collaboration systems for cross-party audience analysis 
+  Converged linear TV and digital advertising operations 

### What this guidance helps customers achieve
<a name="what-this-guidance-helps-customers-achieve"></a>

 Advertising platforms face a set of operational challenges that distinguish them from general cloud workloads: 
+  **High traffic volumes** with tens of millions of transactions per second and single-digit millisecond latency requirements. 
+  **Low revenue and profit margin per transaction** driving focus on cost efficiency, where even small optimizations compound significantly at scale. 
+  **Rapid changes in traffic volumes** requiring automated scaling that can absorb 10x spikes during live events without manual intervention. 
+  **Data transfer as a significant cost driver**, where cross-AZ and cross-region data movement that seems negligible per transaction becomes the largest cost category at RTB scale. 
+  **Large data volumes** (100 petabytes, up to 1 trillion events per week) requiring purpose-built data pipeline architectures. 
+  **Evolving privacy regulations** (GDPR, CCPA, COPPA, and IAB TCF v2.3) that span multiple jurisdictions and apply differently to different data types. 
+  **Third-party signal loss** from the deprecation of cookies and device identifiers, requiring privacy-preserving alternatives for targeting and measurement. 
+  **AI/ML complexity** for fraud detection, contextual targeting, bid price prediction, and the emerging wave of agentic AI advertising workflows. 
+  **Linear/digital convergence** where publishers must operate incompatible linear TV and digital advertising stacks simultaneously for a decade or more. 

 After reading this document, you will understand AWS best practices and recommended strategies to use when designing and operating architectures for advertising workloads. You can evaluate your existing architectures against these best practices, identify gaps, and prioritize improvements. 

### Lens availability
<a name="custom-lens-availability"></a>

 Custom lenses extend the best practice guidance provided by AWS Well-Architected Tool. AWS WA Tool allows you to create your own [custom lenses](https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-custom.html), or to use lenses created by others that have been shared with you. 

To begin reviewing your video streaming advertising workload, download and import the [Video Streaming Advertising Lens](https://github.com/aws-samples/sample-well-architected-custom-lens/blob/main/video-streaming-advertising-lens/video-streaming-advertising-lens.json) into AWS Well-Architected Tool from the public [AWS Well-Architected custom lens GitHub repository](https://github.com/aws-samples/sample-well-architected-custom-lens).