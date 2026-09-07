

# Internet of Things (IoT) Lens
<a name="iot-lens"></a>

 This whitepaper describes the AWS IoT Lens for the AWS Well-Architected Framework, which you can use to review and improve your cloud-based architectures and better understand the business impact of your design decisions. This document describes general design principles, as well as specific best practices and guidance for five of the six pillars of the Well-Architected Framework. 

Publication date: **July 2, 2025** ([Document revisions](document-revisions.md))

## Introduction
<a name="introduction"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/well-architected) helps you understand the pros and cons of the decisions you make when building systems on AWS. Using the Framework allows you to learn architectural best practices for designing and operating reliable, secure, efficient, and cost-effective systems in the cloud. The Framework provides a way for you to consistently measure your architectures against best practices and identify areas for improvement. We believe that having well-architected systems greatly increases the likelihood of business success. 

 

 In this Lens, we focus on how to design, deploy, and architect your Internet of Things (IoT) workloads at the edge and in the AWS Cloud. The guidance provided includes both IoT and industrial IoT (IIoT) workloads and the document calls out specific guidance for segments such as consumer, commercial and industrial when relevant. To implement a well-architected IoT application, follow the well-architected principles, starting from the procurement of connected physical assets (things), operating the asset to the eventual decommissioning of those same assets in a secure, reliable, scalable, sustainable and automated fashion. In addition to AWS Cloud best practices, this document also articulates the impact, considerations, and recommendations for connecting physical assets to the internet. 

 

 This document only covers IoT specific workload details from the Well-Architected Framework. We recommend that you read the [AWS Well-Architected Framework whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) and consider the best practices and questions for other lenses. 

 This document is intended for those in technology roles, such as chief technology officers (CTOs), architects, developers, embedded engineers, security and operations team members. After reading this document, you will understand AWS best practices and strategies for IoT and IIoT applications. 

## Lens availability
<a name="lens-availability"></a>

 The IoT Lens is available as an AWS-official lens in the [Lens Catalog](https://docs.aws.amazon.com/wellarchitected/latest/userguide/lens-catalog.html) of the [AWS Well-Architected Tool](https://docs.aws.amazon.com/wellarchitected/latest/userguide/intro.html). 

 To get started, follow the steps in [Adding a lens to a workload](https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-add.html) and select the **IoT Lens**. 