# Machine Learning Lens - AWS Well-Architected

Framework

Publication date: **November 19, 2025** ([Document revisions](document-revisions.md "document-revisions.md"))

Machine learning (ML) has evolved from research and development to the mainstream, driven
by the exponential growth of data sources, generative AI and scalable cloud-based compute
resources. AWS customers use AI/ML for a wide variety of applications, ranging from foundation
model development and fine-tuning to sophisticated computer vision implementations. Common use
cases include call center operations, personalized recommendations, fraud detection, social
media content moderation, audio and video content analysis, product design services, and
identity verification. These applications use both custom-built models and pre-trained solutions
to address specific business needs. AI/ML adoption has become common across nearly every
industry, including healthcare and life sciences, automotive, industrial and manufacturing,
financial services, media and entertainment, and telecommunications.

Machine learning harnesses algorithms to discover patterns in data, delivering considerable
value to customers while requiring responsible implementation. AWS is committed to developing
fair and accurate AI and ML services and providing you with the tools and guidance needed to
[build AI and ML
applications responsibly](https://aws.amazon.com/machine-learning/responsible-machine-learning/ "https://aws.amazon.com/machine-learning/responsible-machine-learning/").

This whitepaper provides you with a set of best practices. You can apply this guidance and
architectural principles when designing your ML workloads and after your workloads have entered
production as part of continuous improvement. Although the guidance is cloud- and
technology-agnostic, the paper also includes guidance and resources to assist you to implement
these best practices on AWS.

## Introduction

The AWS Well-Architected Framework assists you to understand the benefits and risks of
decisions made while building workloads on AWS. Through the Framework, you learn operational
and architectural best practices for designing and operating cloud workloads. It provides a
consistent method to measure your operations and architectures against best practices and
identify improvement opportunities.

Your ML models depend on high-quality input data to generate accurate results. As data
evolves over time, continuous monitoring is essential to detect, correct, and mitigate
accuracy and performance issues, often requiring model retraining with refined datasets.

While application workloads rely on deterministic, step-by-step instructions to solve
problems, ML workloads enable algorithms to learn from data through iterative and continuous
cycles. The ML Lens complements and builds upon the Well-Architected Framework to address the
fundamental differences between traditional application workloads and machine learning
workloads.

This paper is intended for those in a technology role, such as chief technology officers
(CTOs), architects, developers, data scientists, and ML engineers. After reading this paper,
you will understand the best practices and strategies to use when you design and operate ML
workloads on AWS.

## Distinction from the Generative AI

Lens

The Machine Learning Lens addresses the broad spectrum of ML workloads, including
traditional supervised and unsupervised learning, predictive analytics, classification,
regression, and clustering tasks. Common ML use cases covered by this lens include computer
vision for object detection and image classification, fraud detection and risk scoring,
recommendation engines, predictive maintenance, demand forecasting, customer churn prediction,
anomaly detection, and medical diagnosis systems. In contrast, the Generative AI Lens focuses
on foundation models and generative AI applications that create content, such as text
generation, image synthesis, and conversational AI systems.

While both lenses share common ML principles, the Generative AI Lens emphasizes prompt
engineering, foundation model selection, retrieval-augmented generation (RAG) architectures,
and the specific governance challenges of generative AI systems. The Machine Learning Lens
provides comprehensive guidance for the full ML lifecycle across ML paradigms, making it the
foundational lens for ML workloads.

## Lens availability

Custom lenses extend the best practice guidance provided by AWS Well-Architected Tool. AWS WA Tool allows you to create your own
[custom
lenses](../userguide/lenses-custom.md "../userguide/lenses-custom.md"), or to use lenses created by others that have been
shared with you.

To begin reviewing your machine learning workload, download and import the [Machine Learning Lens](https://github.com/aws-samples/sample-well-architected-custom-lens/blob/main/machine-learning-lens/machine-learning-lens.json "https://github.com/aws-samples/sample-well-architected-custom-lens/blob/main/machine-learning-lens/machine-learning-lens.json") into AWS Well-Architected Tool from the public [AWS Well-Architected custom lens GitHub repository](https://github.com/aws-samples/sample-well-architected-custom-lens "https://github.com/aws-samples/sample-well-architected-custom-lens").
