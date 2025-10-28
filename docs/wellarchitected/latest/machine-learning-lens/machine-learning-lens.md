# Machine Learning Lens

Publication date: **July 5th, 2023** ([Document history](document-history.md "document-history.md"))

In recent years, machine learning (ML) has moved from research and
development to the mainstream, driven by the increasing number of
data sources and scalable cloud-based compute resources. AWS’
customers currently use AI/ML for a wide variety of applications
such as call center operations, personalized recommendations,
identifying fraudulent activities, social media content
moderation, audio and video content analysis, product design
services, and identity verification. Industries using AI/ML
include healthcare and life sciences, industrial and
manufacturing, financial services, media and entertainment, and
telecom.

Machine learning, through its use of algorithms to find patterns
in data, can bring considerable power to its customers and thus
recommends responsibility in its use. AWS is committed to
developing fair and accurate AI and ML services and providing you
with the tools and guidance needed to build AI and ML applications
responsibly. For more information on this important
topic, refer to
[AWS'
Responsible AI](https://aws.amazon.com/machine-learning/responsible-machine-learning/ "https://aws.amazon.com/machine-learning/responsible-machine-learning/").

This whitepaper provides you with a set of proven best practices.
You can apply this guidance and architectural principles when
designing your ML workloads, and after your workloads have entered
production as part of continuous improvement. Although the
guidance is cloud- and technology-agnostic, the paper also
includes guidance and resources to help you implement these best
practices on AWS.

## Introduction

The
[AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/") helps you understand the benefits
and risks of decisions you make while building workloads on AWS.
By using the Framework, you learn operational and architectural
best practices for designing and operating workloads in the cloud.
It provides a way to consistently measure your operations and
architectures against best practices and identify areas for
improvement.

Your ML models depend on the quality of input data to generate
accurate results. As data changes with time, monitoring is
required to continually detect, correct, and mitigate issues with
accuracy and performance. This monitoring step might require you
to retrain your model over time using the latest refined data.

While application workloads rely on step-by-step instructions to
solve a problem, ML workloads enable algorithms to learn from data
through an iterative and continuous cycle. The ML Lens complements
and builds upon the Well-Architected Framework to address this
difference between these two types of workloads.

This paper is intended for those in a technology role, such as
chief technology officers (CTOs), architects, developers, data
scientists, and ML engineers. After reading this paper, you will
understand the best practices and strategies to use when you
design and operate ML workloads on AWS.

## Lens availability

The Machine Learning Lens is available as an AWS-official lens in the [Lens Catalog](../userguide/lens-catalog.md "../userguide/lens-catalog.md") of the [AWS Well-Architected Tool](../userguide/intro.md "../userguide/intro.md").

To get started, follow the steps in [Adding a lens to a workload](../userguide/lenses-add.md "../userguide/lenses-add.md") and select the **Machine Learning Lens**.
