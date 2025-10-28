# Understanding serverless data processing

Processing data in serverless applications largely falls within the following three patterns:

- **Asynchronous processing**– big data processing, image/video manipulation, web hooks
- **Synchronous processing** – web apps, web services, microservices, web hooks
- **Streaming** – processing inbound data streams, from apps, IoT devices
  The following topics provide a broad overview of each serverless processing pattern and explain the most common services you can use for each type.
  Use these topics to gain a conceptual understanding of serverless data processing on AWS.

###### Topics

- [Asynchronous processing](#usecases_data-processing "#usecases_data-processing")
- [Synchronous processing](#usecases_interactive-synchronous "#usecases_interactive-synchronous")
- [Streaming](#usecases_streaming "#usecases_streaming")
- [Stateless data](#usecases_stateless "#usecases_stateless")

## Asynchronous processing

Serverless development allows your applications to ingest, process and analyze high volumes of data quickly and efficiently.

As the volume of data coming from increasingly diverse sources grows, you might find you
need to move quickly to process this data to ensure that your application's business logic can meet your needs.
To process data at scale, organizations need to elastically provision resources to manage the information they receive
from various microservices, mobile devices, operational data stores, and other sources.

Learn how to build a scalable serverless data processing solution. Use Amazon Simple Storage Service to trigger data processing or load machine learning (ML) models so
that Lambda can perform ML inference in real time.

- **File processing** – Suppose you have a photo
  sharing application. People use your application to upload photos, and the application
  stores these user photos in an Amazon S3 bucket. Then, your application creates a thumbnail
  version of each user's photos and displays them on the user's profile page. In this
  scenario, you may choose to create a Lambda function that creates a thumbnail
  automatically. Amazon S3 is one of the supported AWS event sources that can publish
  _object-created events_ and invoke your Lambda function. Your Lambda
  function code can read the photo object from the Amazon S3 bucket, create a thumbnail version,
  and then save it in another Amazon S3 bucket.
- **Image identification** – Given the same photo sharing application, suppose now that you want to
  provide automatic categorization of images for your users. In this scenario, Amazon Rekognition
  will queue each images for processing. After analysis, faces are detected and your application can implement
  similarity scores to group photos by family members, for example. Objects, scenes, activities, landmarks, and
  dominant colors are detected and labels are applied to improve categorization and search.

To implement asynchronous processing in similar scenarios, you can use the following AWS services together.

- **AWS Lambda** — For compute processing tasks.
- **AWS Step Functions** — For managing and orchestrating
  microservice workflows.
- **Amazon Simple Notification Service** — For message delivery from publishers to
  subscribers, plus _fan out_ which is when a message published to a
  topic is replicated and pushed to multiple endpoints for parallel asynchronous
  processing.
- **Amazon Simple Queue Service** — For creating secure, durable, and
  scalable queues for asynchronous processing.
- **Amazon DynamoDB** and **Amazon S3** — For storing and retrieving data and files

## Synchronous processing

Microservice architecture breaks applications into loosely coupled services. Each microservice is independent,
making it easy to scale up a single service or function without needing to scale the entire application.
Individual services are loosely coupled, letting independent teams focus on a single business process,
without the need for them to understand the entire application.

Microservices also let you choose which individual components suit your business needs,
giving you the flexibility to change your selection without rewriting your entire workflow. Different teams can use
the programming languages and frameworks of their choice to work with their microservice,
and this microservice can still communicate with any other in the application
through application programming interfaces (APIs).

Examples:

- **Websites** — Suppose you are creating a website and you want to host the
  back-end logic on Lambda. You can invoke your Lambda function over `HTTP` using Amazon API Gateway as the `HTTP` endpoint.
  Now, your web client can invoke the API, and then API Gateway can route the request to Lambda. You can also implement route authentication
  and authorization by integrating Amazon Cognito with API Gateway
- **Mobile applications** — Suppose you have a custom mobile application that produces events.
  You can create a Lambda function to process events published by your custom application. For example, you can configure a Lambda
  function to process the clicks within your custom mobile application.

To implement synchronous processing in similar scenarios, you can use the following AWS services together.

- **AWS Lambda** — For compute processing tasks.
- **Amazon API Gateway** — For connecting and scaling inbound
  requests.
- **AWS Step Functions** — For managing and orchestrating
  microservice workflows.
- **Amazon DynamoDB** & **S3** — For storing and retrieving data and files.
- **Amazon Cognito** for authentication and authorization of
  users.

## Streaming

Streaming data lets you to gather analytical insights from your application and process them in real-time.
Streaming typically presents a unique set of design and architectural challenges.

Lambda and Amazon Kinesis can process real-time streaming data for application activity tracking, transaction order processing,
click-stream analysis, data cleansing, log filtering, indexing, social media analysis,
Internet of Things (IoT) device data telemetry, and metering.

- **Data and analytics** — Suppose you are building an analytics application and
  storing raw data in a DynamoDB table. When you write, update, or delete items in a table, DynamoDB streams can publish item
  update events to a stream associated with the table. In this case, the event data provides the item key,
  event name (such as insert, update, and delete), and other relevant details. You can write a Lambda function to
  generate custom metrics by aggregating raw data.
- **Monitoring metrics** — Amazon Prime Video monitors metrics from devices worldwide to
  ensure quality-of-service. The team chose Amazon Kinesis Data Streams to deliver video stream metadata and to collect metrics.
  Data is sent to Amazon OpenSearch Service for application monitoring and forensic analysis.
  The services aggregate, analyze, and visualize data to provide real-time insights that help the team
  find and fix streaming issues as they happen. For more information on this specific use-case, see
  [Using AWS to Deliver Streaming Experience to More Than 18 Million Football Fans](https://aws.amazon.com/solutions/case-studies/amazon-prime-video/?did=cr_card&trk=cr_card "https://aws.amazon.com/solutions/case-studies/amazon-prime-video/?did=cr_card&trk=cr_card")

To implement serverless streaming in similar scenarios, you can use the following AWS services together.

- **AWS Lambda** — For compute processing tasks.
- **Amazon Kinesis** — For collecting, processing, and analyzing
  real-time and streaming data.
- **Amazon DynamoDB** & **Amazon S3** — For storing and retrieving data and files.

## Stateless data

When building Lambda functions, you should assume that the environment exists only for a single invocation. The function should initialize any required state when
it is first started – for example, fetching a shopping cart from a DynamoDB table. It should commit any permanent data changes before exiting to a durable store such as
Amazon S3, DynamoDB, or Amazon SQS. It should not rely on any existing data structures or temporary files, or any internal state that would be managed by multiple invocations
(such as counters or other calculated, aggregate values).

Lambda provides an initializer before the handler where you can initialize database connections, libraries, and other resources. Since execution environments are
reused where possible to improve performance, you can amortize the time taken to initialize these resources over multiple invocations. However, you should not store
any variables or data used in the function within this global scope.
