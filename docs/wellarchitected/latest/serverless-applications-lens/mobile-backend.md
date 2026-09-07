

# Mobile backend
<a name="mobile-backend"></a>

Users increasingly expect their mobile applications to have a fast, consistent, and feature-rich user experience. At the same time, mobile user patterns are dynamic with unpredictable peak usage and often have a global footprint. 

The growing demand from mobile users means that applications need a rich set of mobile services that work together seamlessly without sacrificing control and flexibility of the backend infrastructure. Certain capabilities across mobile applications, are expected by default:
+  Ability to query, mutate, and subscribe to database changes. 
+  Offline persistence of data and bandwidth optimizations when connected. 
+  Search, filtering, and discovery of data in applications. 
+  Analytics of user behavior. 
+  Targeted messaging through multiple channels (Push Notifications, SMS, Email). 
+  Rich content such as images and videos. 
+  Data synchronization across multiple devices and multiple users. 
+  Fine-grained authorization controls for viewing and manipulating data. 

 Building a serverless mobile backend on AWS enables you to provide these capabilities while automatically managing scalability, elasticity, and availability in an efficient and cost effective way. 

## Characteristics
<a name="characteristics-2"></a>
+  You want to control application data behavior from the client and explicitly select what data you want from the API. 
+  You want your business logic to be decoupled from your mobile application as much as possible. 
+  You are looking to provide business functionalities as an API to optimize development across multiple platforms. 
+  You are seeking to use managed services to reduce undifferentiated heavy lifting of maintaining mobile backend infrastructure while providing high levels of scalability and availability. 
+  You want to optimize your mobile backend costs based upon actual user demand instead of paying for idle resources. 

## Reference architecture
<a name="mobile-backend-ref-arch"></a>

![Reference architecture diagram for a mobile backend](http://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/images/reference-architecture-for-mobile-backend.png)


 

1.  **Amazon Cognito** is used for user management and as an identity provider for your mobile application. Additionally, it allows mobile users to leverage existing social identities such as Facebook, Twitter, Google\+, and Amazon to sign in. 

1.  **Mobile users** interact with the mobile application backend by performing GraphQL operations against AWS AppSync and AWS service APIs (for example, Amazon S3 and Amazon Cognito). 

1.  **Amazon S3** stores mobile application static assets including certain mobile user data such as profile images. Its contents are securely served via CloudFront. 

1. ** AWS AppSync** hosts GraphQL HTTP requests and responses to mobile users. In this scenario, data from AWS AppSync is in real-time when devices are connected, and data is available offline as well. Data sources for this scenario are Amazon DynamoDB, Amazon OpenSearch Service, or AWS Lambda functions. 

1.  **Amazon OpenSearch Service** acts as a main search engine for your mobile application as well as analytics. 

1.  **Amazon DynamoDB** provides persistent storage for your mobile application, including mechanisms to expire unwanted data from inactive mobile users through a **Time to Live (TTL)** feature. 

1.  An **AWS Lambda** function handles interaction with other third-party services, or calling other AWS services for custom flows, which can be part of the GraphQL response to clients. 

1.  **Amazon DynamoDB Streams** captures item-level changes and enables a Lambda function to update additional data sources. 

1.  An **AWS Lambda** function manages streaming data between DynamoDB and OpenSearch Service, allowing customers to combine data sources logical GraphQL types and operations. 

1.  **Amazon Pinpoint** captures analytics from clients, including user sessions and custom metrics for application insights. 

1.  **Amazon Pinpoint** delivers messages to all users or devices, or a targeted subset based on analytics that have been gathered. Messages can be customized and sent using push notifications, email, or SMS channels. 

## Configuration notes
<a name="configuration-notes-2"></a>
+  [Performance test](https://github.com/alexcasalboni/aws-lambda-power-tuning) your Lambda functions with different memory and timeout settings to ensure that you’re using the most appropriate resources for the job. 
+  Follow [best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices.html) when creating your DynamoDB tables and consider having AWS AppSync automatically provision them from a GraphQL schema, which will use a well-distributed hash key and create indexes for your operations. Make certain to calculate your read and write capacity, and table partitioning to ensure reasonable response times. 
+  Use the AWS AppSync [server-side data caching](https://docs.aws.amazon.com/appsync/latest/devguide/enabling-caching.html) to optimize your application experience, as all subsequent query requests to your API will be returned from the cache, which means data sources won’t be contacted directly unless the TTL expires. 
+  Follow [best practices](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html) when managing Amazon OpenSearch Service domains. Additionally, Amazon OpenSearch Service provides an extensive [guide](https://www.elastic.co/guide/en/elasticsearch/guide/current/scale.html) on designing concerning sharding and access patterns that also apply here. 
+  Use the fine-grained access controls of AWS AppSync, configured in resolvers, to filter GraphQL requests down to the per-user or group level if necessary. This can be applied to AWS Identity and Access Management (IAM) or Amazon Cognito user pools authorization with AWS AppSync. 
+  Use AWS Amplify and Amplify CLI to compose and integrate your application with multiple AWS services. Amplify Console also takes care of deploying and managing stacks. 

 For low-latency requirements where near-to-none business logic is required, Amazon Cognito Federated Identity can provide scoped credentials so that your mobile application can talk directly to an AWS service, for example, when uploading a user’s profile picture, retrieve metadata files from Amazon S3 scoped to a user.