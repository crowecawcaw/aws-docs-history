# Sports Betting Architecture on AWS

Publication date: **November 16, 2023 ([Diagram history](#diagram-history "#diagram-history"))**

This reference architecture describes how sports betting application can be
deployed to address different regulatory requirements. And how AWS Local Zones and AWS Outposts
and hybrid scenarios can help you address those challenges.

## Deployment of All Components on AWS Diagram

This reference architecture describes how to set up betting applications in AWS when regulations require that only a copy of the data be stored within the regulated jurisdiction.

![Reference architecture diagram showing how to set up betting applications in AWS when regulations require that only a copy of the data be stored within the regulated jurisdiction.](images/1-deployment-of-all-components-on-aws.png)

1. The bet entry point uses [**Amazon CloudFront**](https://aws.amazon.com/cloudfront "https://aws.amazon.com/cloudfront").
   [**AWS WAF**](https://aws.amazon.com/waf "https://aws.amazon.com/waf") protects against DDoS attacks, bots, and account takeover.
2. Platform components use containerized deployments, leveraging
   [**Amazon Elastic Kubernetes Service**](https://aws.amazon.com/eks "https://aws.amazon.com/eks") (Amazon EKS) within an AWS Region.
3. Use [**Amazon Managed Streaming for Apache Kafka**](https://aws.amazon.com/msk "https://aws.amazon.com/msk") (Amazon MSK)
   to build real-time streaming data pipelines between services, applications, and data layers.
4. A NAT gateway provides a static IP address for the allowlist on the external provider side. The
   feeds push method uses
   [**Amazon API Gateway**](https://aws.amazon.com/api-gateway "https://aws.amazon.com/api-gateway") with WebSocket
   capability, if required.
5. External service providers with clearance to operate within a geo zone handle external compliance operations and payments.
6. The data platform and message bus stream logs, application data, and user activity data to the analytics
   layer through federation mechanisms, [**AWS Lake Formation**](https://aws.amazon.com/lake-formation "https://aws.amazon.com/lake-formation")
   or [**Amazon Aurora**](https://aws.amazon.com/rds/aurora "https://aws.amazon.com/rds/aurora") zero-ETL.
   **Amazon MSK** uses mirroring for replication.
7. The database layer stores platform data and historical transactions.
   [**Amazon Relational Database Service**](https://aws.amazon.com/rds "https://aws.amazon.com/rds") (Amazon RDS) provides
   resiliency, redundancy, and quick failover.
8. The compute layer uses analytics results through an internal API.
9. The odds engine stores data in [**Amazon DynamoDB**](https://aws.amazon.com/dynamodb "https://aws.amazon.com/dynamodb").
   **CloudFront** serves the feed data to the customers through WebSocket.
10. Native database tools replicate data from the database layer to an external data center for
    compliance. [**AWS Site-to-Site VPN**](https://aws.amazon.com/vpn/site-to-site-vpn "https://aws.amazon.com/vpn/site-to-site-vpn") secures the connection.

## Deployment of Player-Related Components Outside of AWS Diagram

This reference architecture describes deployment of betting applications
to AWS when regulations require that the sportsbook, wallets, and player
account management(PAM) be deployed within the regulated jurisdiction with
no AWS Region available.

![Reference architecture diagram showing how to deploy betting applications to AWS when regulations require that the sportsbook, wallets, and player account management(PAM) be deployed within the regulated jurisdiction with no AWS Region available.](images/2-deployment-of-player-related-components-outside-of-aws.png)

1. The bet entry point uses [**Amazon CloudFront**](https://aws.amazon.com/cloudfront "https://aws.amazon.com/cloudfront").
   [**AWS WAF**](https://aws.amazon.com/waf "https://aws.amazon.com/waf") protects against DDoS attacks, bots, and account takeover.
2. Platform components use containerized deployments, leveraging
   [**Amazon Elastic Kubernetes Service**](https://aws.amazon.com/eks "https://aws.amazon.com/eks") (Amazon EKS) within
   an AWS Region.
3. Use [**Amazon Managed Streaming for Apache Kafka**](https://aws.amazon.com/msk "https://aws.amazon.com/msk") (Amazon MSK) to
   build real-time streaming data pipelines between services, applications, and data layers.
4. A NAT gateway provides a static IP address for the allowlist on the external provider side.
   The feeds push method uses [**Amazon API Gateway**](https://aws.amazon.com/api-gateway "https://aws.amazon.com/api-gateway").
5. External service providers with clearance to operate within a geo zone handle wallet operations and payments.
6. The data latform and message bus stream logs, application data, and user activity
   data to the analytics layer through federation or mirroring.
7. The database layer stores platform data and historical transactions.
   [**Amazon Relational Database Service**](https://aws.amazon.com/rds "https://aws.amazon.com/rds") (Amazon RDS)
   provides resiliency, redundancy, and quick failover.
8. The compute layer uses analytics results through an internal API.
9. The odds engine stores data in an [**Amazon DynamoDB**](https://aws.amazon.com/dynamodb "https://aws.amazon.com/dynamodb") database. The feed information is accessed
   through third-party feed pull or push models. Afterward, **CloudFront** serves the feed data to the customers through WebSocket.
10. If regulations allow, bets are placed in **AWS Local Zones** where AWS Regions are not present.
11. If regulations do not allow the cloud, the bets are placed on-premises
    using [**AWS Outposts**](https://aws.amazon.com/outposts "https://aws.amazon.com/outposts").

## Deployment of All Core Components Outside of AWS Diagram

This reference architecture describes deployment of betting applications to AWS where regulations require that sportsbook, wallets, player account management (PAM), and odds engines
run within a jurisdiction containing no AWS Region.

![Reference architecture diagram showing how to deploy betting applications to AWS where regulations require that sportsbook, wallets, player account management (PAM), and odds engines run within a jurisdiction containing no AWS Region.](images/3-deployment-of-all-core-components-outside-of-aws.png)

1. The bet entry point uses [**Amazon CloudFront**](https://aws.amazon.com/cloudfront "https://aws.amazon.com/cloudfront").
   [**AWS WAF**](https://aws.amazon.com/waf "https://aws.amazon.com/waf") protects against DDoS attacks, bots, and account takeover.
2. Platform components use containerized deployments, leveraging [**Amazon Elastic Kubernetes Service**](https://aws.amazon.com/eks "https://aws.amazon.com/eks") (Amazon EKS) within an AWS Region.
3. Use [**Amazon Managed Streaming for Apache Kafka**](https://aws.amazon.com/msk "https://aws.amazon.com/msk") (Amazon MSK) to build
   real-time streaming data pipelines between services, applications, and data layers.
4. A NAT gateway provides a static IP address for the allowlist on the external provider side.
5. External service providers with clearance to operate within a geo zone handle external compliance operations operations and payments.
6. The data platform and message bus stream logs, application data, and user activity data
   to the analytics layer through federation or mirroring.
7. The database layer stores platform data and historical transactions.
   [**Amazon Relational Database Service**](https://aws.amazon.com/rds "https://aws.amazon.com/rds") (Amazon RDS)
   provides resiliency, redundancy, and quick failover.
8. The compute layer uses analytics results through an internal API.
9. WebSocket provides live feed information. The feed information is accessed by
   third-party feed pull or push models and combined. Odds are calculated within regulated zones.
10. If regulations allow, bets are placed in **AWS Local Zones** where AWS Regions are not present.
11. If regulations do not allow the cloud, the bets are placed on-premises using [**AWS Outposts**](https://aws.amazon.com/outposts "https://aws.amazon.com/outposts").

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/sports-betting-architecture.md "samples/sports-betting-architecture.md") which contains an editable PowerPoint.

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

- Sergey Viktorovich Kurson, Principal Solutions Architect, Amazon Web Services
- Serhii Avramchuk, Senior Account Manager, Amazon Web Services

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date              |
| ------------------- | ----------------------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------- |
| Initial publication | Reference architecture diagram first published. | November 15, 2023 | ###### Note To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using. |
