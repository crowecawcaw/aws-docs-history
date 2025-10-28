# Edit in the Cloud on AWS

Publication date: **June 12, 2022 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture helps you build a virtual, video editing environment on AWS to
collaborate with your editors and creative professionals. This architecture can also be [deployed on AWS](../../../solutions/latest/edit-in-the-cloud-on-aws/welcome.md "../../../solutions/latest/edit-in-the-cloud-on-aws/welcome.md") using an AWS CloudFormation template that launches, configures, and runs the AWS services
required to deploy this solution using AWS best practices for security and
availability.

## Edit in the Cloud on AWS

![Reference architecture diagram showing how you can use AWS services to help you build a virtual, video editing environment on AWS to collaborate with your editors and creative professionals.](images/edit-in-cloud-on-aws.png)

1. An **Amazon Elastic Compute Cloud** (Amazon EC2) instance for Windows Server 2019
   with Teradici Cloud Access Software or NICE DCV and NVIDIA T4 GPU drivers for running your
   Non-Linear Editor (NLE) software of choice. During deployment, the solution gives you the
   option to install either Teradici’s Cloud Access Software, or NICE DCV. Users can then
   access the cloud workstation using either Teradici’s PC-over-IP (PCoIP) client or the NICE
   DCV client, accordingly.
2. **AWS Directory Service** for user authentication.
3. **Amazon FSx for Windows File Server** to access digital assets via the
   **Amazon EC2** instance through your editor of choice. **FSx for Windows File Server** will auto-mount the network share upon startup of
   the Windows **Amazon EC2** instance. **FSx for Windows File Server** will be used for storing your media assets to be used by your
   non-linear editor (NLE).

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/edit-in-cloud-on-aws.md "samples/edit-in-cloud-on-aws.md") which contains an
editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS
feed.

| Change                         | Description                                     | Date           |
| ------------------------------ | ----------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------- |
| Reference architecture updated | Updated for technical accuracy                  | July 12, 2022  |
| Reference architecture updated | Updated for technical accuracy                  | March 12, 2022 |
| Initial publication            | Reference architecture diagram first published. | May 19, 2021   | ###### Note To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using. |
