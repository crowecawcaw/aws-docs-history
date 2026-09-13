

# Streaming Media Lens - AWS Well-Architected
<a name="streaming-media-lens"></a>

Last updated: **September 11, 2026** ([Release notes](release-notes.md))

This whitepaper describes the AWS Streaming Media Lens for the AWS Well-Architected Framework, which helps customers apply best practices in the design, delivery, and maintenance of their cloud-based streaming media workloads. The document describes general design principles, as well as specific best practices and guidance for the six pillars of the Well-Architected Framework.

This paper is intended for those in technology roles, such as technology leaders, architects, developers, and operations team members. After reading this paper, you will understand AWS best practices and the strategies to use when designing and operating streaming media workloads in a cloud environment.

The AWS Well-Architected Framework helps cloud architects build secure, high-performing, resilient, and efficient infrastructure for their applications and workloads. Based on six pillars, AWS Well-Architected provides a consistent approach for customers and AWS Partners to evaluate architectures, remediate risks, and implement designs that deliver business value.

In this lens, we focus on how to design and deploy streaming media workloads by defining components, exploring common workload scenarios, and outlining design principles that help you to apply the AWS Well-Architected Framework. We address specific best practices aligned with the pillars of the Well-Architected Framework.

Streaming media workloads transmit audio and video from content publishers to audiences. Streaming media is typically used for one-to-many broadcasts to audiences over HTTP. Readers interested in real-time communications for web conferencing applications should refer to [Real-Time Communication on AWS](https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/welcome.html).

For brevity, we only cover details from the Well-Architected Framework that are specific to streaming media workloads. We recommend that you start by considering best practices and questions from the [AWS Well-Architected Framework whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) when designing your architecture

## Lens availability
<a name="custom-lens-availability"></a>

 Custom lenses extend the best practice guidance provided by AWS Well-Architected Tool. AWS WA Tool allows you to create your own [custom lenses](https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-custom.html), or to use lenses created by others that have been shared with you. 

To begin reviewing your streaming media workload, download and import the [Streaming Media Lens](https://github.com/aws-samples/sample-well-architected-custom-lens/blob/main/streaming-media-lens/streaming-media-lens.json) into AWS Well-Architected Tool from the public [AWS Well-Architected custom lens GitHub repository](https://github.com/aws-samples/sample-well-architected-custom-lens).