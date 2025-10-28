AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Application analysis and

extraction

AWS Microservice Extractor for .NET analyzes the source code of a monolithic application and creates a
visualization of the application, which includes nodes, dependencies, call flows, and
relevant metrics. You can use the visualization of the application to make informed
decisions about the structure of the application, and to identify parts of the
application to group together and extract as independent services.

After Microservice Extractor extracts a specified functionality group within the application, you can
manually package and deploy the functionalities as independent services in containers.
You can then integrate the smaller services with your custom workflows.

Extracting monolithic applications into smaller, independent services is an iterative
process. Based on your requirements, you can repeat the process by onboarding the newly
extracted monolithic application into Microservice Extractor. This further assists with identifying and
extracting components as independent services.
