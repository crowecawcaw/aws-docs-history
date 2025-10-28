AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Concepts

The following concepts and definitions can help you to understand the AWS Microservice Extractor for .NET
tool.

###### Nodes

Nodes represent the classes in the source code of the monolithic application.

###### Groups

Closely related functions are organized as groups of nodes in the graphical representation
of a monolithic application. Application nodes are displayed with their dependencies to help you
understand the functional architecture of your application. This visualization of the
application nodes and dependencies can help you to group them together by functionality.

###### Visualization

The Microservice Extractor visualization uses source code analysis and runtime metrics to produce a
graphical representation of a monolithic application. The graph shows dependencies between
application nodes, call counts, and static references between code artifacts. You can use the
graph and call counts to understand the dependencies between nodes, and to identify heavily
called ones. You can run the assessment tool from the standalone Microservice Extractor application.

###### Canvas

Independent views for arranging nodes and creating groups.

###### Extraction

Extraction is the process of separating out logically grouped parts of a monolithic
application into smaller, independent services. These parts are referred to as islands in the
visualization of an application. You can perform an extraction using Microservice Extractor after an
application has been assessed.
