

# Web3 Decentralized Applications on AWS
<a name="web3-decentralized-applications-on-aws"></a>

Publication date: **August 3, 2023 ([Diagram history](#diagram-history))**

Use this architecture as a reference for developing static hosted web applications that communicate with a blockchain network through an Amazon Managed Blockchain node.

## Web3 Decentralized Applications on AWS Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing how to develop static hosted web applications that communicate with a blockchain network through an Amazon Managed Blockchain node.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/web3-decentralized-applications-on-aws/images/web-decentralized-applications-on-aws.png)


1. The browser makes a requests to the **Amazon CloudFront** domain, routed to the closest distribution for the Decentralized Application (DApp). 

1. The DApp is cached at the edge in **CloudFront**. The DApp files are distributed to the edge by a **CloudFront** distribution that makes a request to an **Amazon Simple Storage Service** (Amazon S3) bucket, where the DApp files are statically hosted. 

    The **Amazon S3** bucket is secured by blocking all traffic except for a configured origin Access Identity of the CloudFront Distribution. Refer to [Restricting access to an Amazon S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html). 

1. The DApp makes requests to the **Amazon API Gateway** from the browser. 

1. All requests to the **API Gateway** are sent to the **AWS Lambda** DApp Backend. It reads the path and method requests and binds them into a Web3.js request with a sigv4 signed Http Request Provider. 

1. **Amazon Managed Blockchain** Ethereum Node receives and processes Web3 requests. 

1. Ethereum requests and transactions are propagated to and received from the decentralized Ethereum Blockchain Mainnet. 

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Contributors
<a name="contributors"></a>

 Contributors to this reference architecture diagram include: 
+  Aaron Sempf, Principal Partner Solutions Architect, Amazon Web Services 
+  Gonzalo Ron, Senior Partner Sales Solutions Architect, Amazon Web Services 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | August 3, 2023 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.