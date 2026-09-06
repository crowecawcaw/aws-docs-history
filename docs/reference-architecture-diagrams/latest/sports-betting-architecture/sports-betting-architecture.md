

# Sports Betting Architecture on AWS
<a name="sports-betting-architecture"></a>

Publication date: **November 16, 2023 ([Diagram history](#diagram-history))**

This reference architecture describes how sports betting application can be deployed to address different regulatory requirements. And how AWS Local Zones and AWS Outposts and hybrid scenarios can help you address those challenges.

## Deployment of All Components on AWS Diagram
<a name="1-deployment-of-all-components-on-aws"></a>

 This reference architecture describes how to set up betting applications in AWS when regulations require that only a copy of the data be stored within the regulated jurisdiction. 

![Reference architecture diagram showing how to set up betting applications in AWS when regulations require that only a copy of the data be stored within the regulated jurisdiction.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/sports-betting-architecture/images/1-deployment-of-all-components-on-aws.png)


1.  The bet entry point uses [**Amazon CloudFront**](https://aws.amazon.com/cloudfront). [**AWS WAF**](https://aws.amazon.com/waf) protects against DDoS attacks, bots, and account takeover. 

1.  Platform components use containerized deployments, leveraging [**Amazon Elastic Kubernetes Service**](https://aws.amazon.com/eks) (Amazon EKS) within an AWS Region. 

1.  Use [**Amazon Managed Streaming for Apache Kafka**](https://aws.amazon.com/msk) (Amazon MSK) to build real-time streaming data pipelines between services, applications, and data layers. 

1.  A NAT gateway provides a static IP address for the allowlist on the external provider side. The feeds push method uses [**Amazon API Gateway**](https://aws.amazon.com/api-gateway) with WebSocket capability, if required. 

1.  External service providers with clearance to operate within a geo zone handle external compliance operations and payments.  

1.  The data platform and message bus stream logs, application data, and user activity data to the analytics layer through federation mechanisms, [**AWS Lake Formation**](https://aws.amazon.com/lake-formation) or [**Amazon Aurora**](https://aws.amazon.com/rds/aurora) zero-ETL. **Amazon MSK** uses mirroring for replication. 

1.  The database layer stores platform data and historical transactions. [**Amazon Relational Database Service**](https://aws.amazon.com/rds) (Amazon RDS) provides resiliency, redundancy, and quick failover. 

1.  The compute layer uses analytics results through an internal API. 

1.  The odds engine stores data in [**Amazon DynamoDB**](https://aws.amazon.com/dynamodb). **CloudFront** serves the feed data to the customers through WebSocket. 

1.  Native database tools replicate data from the database layer to an external data center for compliance. [**AWS Site-to-Site VPN**](https://aws.amazon.com/vpn/site-to-site-vpn) secures the connection. 

## Deployment of Player-Related Components Outside of AWS Diagram
<a name="2-deployment-of-player-related-components-outside-of-aws"></a>

 This reference architecture describes deployment of betting applications to AWS when regulations require that the sportsbook, wallets, and player account management(PAM) be deployed within the regulated jurisdiction with no AWS Region available. 

![Reference architecture diagram showing how to deploy betting applications to AWS when regulations require that the sportsbook, wallets, and player account management(PAM) be deployed within the regulated jurisdiction with no AWS Region available.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/sports-betting-architecture/images/2-deployment-of-player-related-components-outside-of-aws.png)


1.  The bet entry point uses [**Amazon CloudFront**](https://aws.amazon.com/cloudfront). [**AWS WAF**](https://aws.amazon.com/waf) protects against DDoS attacks, bots, and account takeover. 

1.  Platform components use containerized deployments, leveraging [**Amazon Elastic Kubernetes Service**](https://aws.amazon.com/eks) (Amazon EKS) within an AWS Region. 

1.  Use [**Amazon Managed Streaming for Apache Kafka**](https://aws.amazon.com/msk) (Amazon MSK) to build real-time streaming data pipelines between services, applications, and data layers. 

1.  A NAT gateway provides a static IP address for the allowlist on the external provider side. The feeds push method uses [**Amazon API Gateway**](https://aws.amazon.com/api-gateway). 

1.  External service providers with clearance to operate within a geo zone handle wallet operations and payments.  

1.  The data latform and message bus stream logs, application data, and user activity data to the analytics layer through federation or mirroring. 

1.  The database layer stores platform data and historical transactions. [**Amazon Relational Database Service**](https://aws.amazon.com/rds) (Amazon RDS) provides resiliency, redundancy, and quick failover. 

1.  The compute layer uses analytics results through an internal API. 

1.  The odds engine stores data in an [**Amazon DynamoDB**](https://aws.amazon.com/dynamodb) database. The feed information is accessed through third-party feed pull or push models. Afterward, **CloudFront** serves the feed data to the customers through WebSocket. 

1.  If regulations allow, bets are placed in **AWS Local Zones** where AWS Regions are not present. 

1.  If regulations do not allow the cloud, the bets are placed on-premises using [**AWS Outposts**](https://aws.amazon.com/outposts). 

## Deployment of All Core Components Outside of AWS Diagram
<a name="3-deployment-of-all-core-components-outside-of-aws"></a>

 This reference architecture describes deployment of betting applications to AWS where regulations require that sportsbook, wallets, player account management (PAM), and odds engines run within a jurisdiction containing no AWS Region. 

![Reference architecture diagram showing how to deploy betting applications to AWS where regulations require that sportsbook, wallets, player account management (PAM), and odds engines run within a jurisdiction containing no AWS Region.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/sports-betting-architecture/images/3-deployment-of-all-core-components-outside-of-aws.png)


1.  The bet entry point uses [**Amazon CloudFront**](https://aws.amazon.com/cloudfront). [**AWS WAF**](https://aws.amazon.com/waf) protects against DDoS attacks, bots, and account takeover. 

1.  Platform components use containerized deployments, leveraging [**Amazon Elastic Kubernetes Service**](https://aws.amazon.com/eks) (Amazon EKS) within an AWS Region. 

1.  Use [**Amazon Managed Streaming for Apache Kafka**](https://aws.amazon.com/msk) (Amazon MSK) to build real-time streaming data pipelines between services, applications, and data layers. 

1.  A NAT gateway provides a static IP address for the allowlist on the external provider side. 

1.  External service providers with clearance to operate within a geo zone handle external compliance operations operations and payments.  

1.  The data platform and message bus stream logs, application data, and user activity data to the analytics layer through federation or mirroring. 

1.  The database layer stores platform data and historical transactions. [**Amazon Relational Database Service**](https://aws.amazon.com/rds) (Amazon RDS) provides resiliency, redundancy, and quick failover. 

1.  The compute layer uses analytics results through an internal API. 

1.  WebSocket provides live feed information. The feed information is accessed by third-party feed pull or push models and combined. Odds are calculated within regulated zones. 

1.  If regulations allow, bets are placed in **AWS Local Zones** where AWS Regions are not present. 

1.  If regulations do not allow the cloud, the bets are placed on-premises using [**AWS Outposts**](https://aws.amazon.com/outposts). 

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Contributors
<a name="contributors"></a>

 Contributors to this reference architecture diagram include: 
+  Sergey Viktorovich Kurson, Principal Solutions Architect, Amazon Web Services 
+  Serhii Avramchuk, Senior Account Manager, Amazon Web Services 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | November 15, 2023 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.