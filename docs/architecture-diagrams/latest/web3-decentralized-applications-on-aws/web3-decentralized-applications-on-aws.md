# Web3 Decentralized Applications on AWS

Publication date: **August 3, 2023 ([Diagram history](#diagram-history "#diagram-history"))**

Use this architecture as a reference for developing static hosted web applications that communicate with a blockchain network through an Amazon Managed Blockchain node.

## Web3 Decentralized Applications on AWS Diagram

![Reference architecture diagram showing how to develop static hosted web applications that communicate with a blockchain network through an Amazon Managed Blockchain node.](images/web-decentralized-applications-on-aws.png)

1. The browser makes a requests to the **Amazon CloudFront**
   domain, routed to the closest distribution for the Decentralized Application (DApp).
2. The DApp is cached at the edge in **CloudFront**. The
   DApp files are distributed to the edge by a **CloudFront**
   distribution that makes a request to an **Amazon Simple Storage Service**
   (Amazon S3) bucket, where the DApp files are statically hosted.

The **Amazon S3** bucket is secured by blocking all traffic except
for a configured origin Access Identity of the CloudFront Distribution. Refer to
[Restricting
access to an Amazon S3 origin](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md"). 3. The DApp makes requests to the **Amazon API Gateway** from the browser. 4. All requests to the **API Gateway** are sent to the **AWS Lambda**
DApp Backend. It reads the path and method requests and binds them into a Web3.js request
with a sigv4 signed Http Request Provider. 5. **Amazon Managed Blockchain** Ethereum Node
receives and processes Web3 requests. 6. Ethereum requests and transactions are propagated to and received
from the decentralized Ethereum Blockchain Mainnet.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/web3-decentralized-applications-on-aws.md "samples/web3-decentralized-applications-on-aws.md") which contains an editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Contributors

Contributors to this reference architecture diagram include:

- Aaron Sempf, Principal Partner Solutions Architect, Amazon Web Services
- Gonzalo Ron, Senior Partner Sales Solutions Architect, Amazon Web Services

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date           |
| ------------------- | ----------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------- |
| Initial publication | Reference architecture diagram first published. | August 3, 2023 | ###### Note To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using. |
