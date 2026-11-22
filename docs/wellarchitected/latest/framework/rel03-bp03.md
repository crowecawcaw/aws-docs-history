

# REL03-BP03 Provide service contracts per API

 A service contract is a documented, machine-readable agreement between an API producer and its consumers. It defines the operations, data types, and fields that both sides rely on, so each can change its implementation without breaking the other. With a versioning strategy, consumers keep using the current API and migrate on their own schedule. Producers deploy whenever they are ready, and teams pick the technology stack that suits them. 

 **Desired outcome:** 
+  Your services operate independently while sharing an integrated runtime dependency through a common contract. 
+  Your producer and consumer changes do not interrupt the overall system as long as both sides honor the contract. 
+  Your components release functionality, upgrade dependencies, or fail over to a disaster recovery (DR) site with little or no impact on each other. 
+  Your services scale independently to absorb demand without requiring other services to scale with them. 

 **Common anti-patterns:** 
+  Teams create APIs without strongly typed schemas, so bindings cannot be generated and payloads cannot be validated programmatically. 
+  Teams adopt no versioning strategy, which forces consumers to update and release whenever a contract changes, or fail. 
+  Error messages expose details of the underlying implementation instead of describing integration failures in the domain language. 
+  Teams do not use contracts to build test cases or mock implementations, which prevents independent testing of components. 

 **Benefits of establishing this best practice:** 
+  Distributed systems whose components communicate over contracts are more reliable. 
+  Developers catch mismatches early through type checking that verifies requests and responses against the contract. 
+  Each API has a clear, self-documenting interface. 
+  Interoperability improves across different systems and programming languages. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A service contract names the operations an API exposes and defines the data objects and fields for each request and response. With strong typing, tools generate client bindings and validate payloads automatically. Without a typed schema, integration errors occur only at runtime, often in production, and each consumer discovers them separately. 

 Contracts change over time. Extending a contract is the lighter option: you add optional fields or supply default values for new required fields, so existing consumers keep working. Extension suits JSON-based protocols such as REST and GraphQL. When a change is not backward compatible, you version the API instead. Proxy versioning places a facade in front of the service that maps requests and responses between versions, so the team maintains a single codebase. XML-based protocols such as SOAP need testing with consumers before you rely on extension, because consumer tolerance for added fields varies. 

 Because both sides agree on the interface, a consumer and a producer can release, upgrade, or fail over to a DR site independently, as long as neither breaks the contract. [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) fronts REST APIs, integrates with AWS and other web services, and supports the OpenAPI specification and versioning. [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html) exposes a GraphQL endpoint defined by a schema that serves as the contract for queries, mutations, and subscriptions. [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) uses event schemas for asynchronous integrations and generates code bindings from them. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define the contract first:** Before implementation, express the API's capabilities and define strongly typed data objects and fields for its input and output. A contract-first approach lets producers and consumers develop and test against the same agreement in parallel. 

1.  **Manage REST contracts with Amazon API Gateway:** [Import an OpenAPI definition](https://docs.aws.amazon.com/apigateway/latest/developerguide/import-edge-optimized-api.html) to create an API, and integrate it with infrastructure as code tools such as the [AWS Serverless Application Model](https://aws.amazon.com/serverless/sam/) and the [AWS Cloud Development Kit (AWS CDK) (AWS CDK)](https://aws.amazon.com/cdk/). [Export an API definition](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-export-api.html) to give consumers and testing tools an integration specification. 

1.  **Define GraphQL contracts with AWS AppSync:** [Define a GraphQL schema](https://docs.aws.amazon.com/appsync/latest/devguide/designing-your-schema.html) to generate the contract interface and simplify access to complex REST models, multiple database tables, or legacy services. [AWS Amplify](https://aws.amazon.com/amplify/) projects integrated with AppSync generate strongly typed client query files and a GraphQL client library for [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) tables. 

1.  **Define event contracts with Amazon EventBridge:** For asynchronous integrations, use event schemas from the schema registry or define your own with the OpenAPI specification. From a registered schema, generate client bindings so your code integrates with events in a type-safe way. See [Amazon EventBridge code bindings](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema-code-bindings.html). 

1.  **Extend contracts before you version them:** When you add capability, prefer extension by adding optional fields or default values for required fields, which keeps existing consumers working. JSON-based protocols such as REST and GraphQL suit extension well. Test XML-based protocols such as SOAP with consumers first to confirm that extension is feasible. 

1.  **Version with a proxy facade when extension is not enough:** For breaking changes, use proxy versioning so the underlying service keeps a single codebase. With API Gateway, use [request and response mappings](https://docs.aws.amazon.com/apigateway/latest/developerguide/request-response-data-mappings.html#transforming-request-response-body) to supply defaults for new fields or strip removed fields between versions. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL03-BP01 Choose how to segment your workload](rel03-bp01.md) 
+  [REL03-BP02 Build services focused on specific business domains and functionality](rel03-bp02.md) 
+  [REL04-BP02 Implement loosely coupled dependencies](rel04-bp02.md) 
+  [REL05-BP03 Control and limit retry calls](rel05-bp03.md) 
+  [REL05-BP05 Set client timeouts](rel05-bp05.md) 

 **Related documents:** 
+  [What is an API? - Application Programming Interfaces Explained](https://aws.amazon.com/what-is/api/) 
+  [Implementing Microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/microservices-on-aws.html) 
+  [Microservice Trade-Offs](https://martinfowler.com/articles/microservice-trade-offs.html) 
+  [Microservices](https://www.martinfowler.com/articles/microservices.html) 
+  [OpenAPI extensions for API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html) 
+  [GitHub - OAI/OpenAPI-Specification: The OpenAPI Specification Repository](https://github.com/OAI/OpenAPI-Specification) 
+  [Schemas and Types \| GraphQL](https://graphql.org/learn/schema/) 

 **Related videos:** 
+  [AWS re:Invent 2023 - I didn't know Amazon API Gateway did that (SVS323)](https://www.youtube.com/watch?v=SlWJCTrMLOA) 

 **Related examples:** 
+  [Develop REST APIs using OpenAPI in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api.html) 
+  [Amazon API Gateway to Amazon DynamoDB CRUD aplication using OpenAPI](https://serverlessland.com/patterns/apigw-ddb-openapi-crud) 
+  [Implement path-based API versioning by using custom domains in Amazon API Gateway](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-path-based-api-versioning-by-using-custom-domains.html) 
+  [Building a client application using Amplify client](https://docs.aws.amazon.com/appsync/latest/devguide/building-a-client-app.html#aws-appsync-building-a-client-app) 

 **Related workshops:** 
+  [Modern application integration patterns in a serverless age: API Gateway service integration](https://catalog.us-east-1.prod.workshops.aws/workshops/be7e1ee7-b91f-493d-93b0-8f7c5b002479/en-US/labs/asynchronous-request-response-poll/api-gateway-service-integration) 

 **Related services:** 
+  [Amazon API Gateway](https://aws.amazon.com/api-gateway/) 
+  [AWS AppSync](https://aws.amazon.com/appsync/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [Microservices on AWS](https://aws.amazon.com/microservices/) 