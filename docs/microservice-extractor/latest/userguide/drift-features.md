AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Primary features

The primary features of AWS Microservice Extractor for .NET are:

###### Application analysis and graphical representation of application classes

Microservice Extractor analyzes your monolithic applications and, based on the analysis, produces a
graphical representation that displays the application classes, optionally configured metrics
for applicable classes, and dependencies between them. The interactive graph groups classes by
functionality to help you make decisions about which parts of the application to extract as
independent services.

###### Automated packaging of grouped functionalities into smaller services

You can designate the parts of an application to extract as separate services by grouping
parts of the application code based on the functionality they implement. Microservice Extractor attempts to
convert the grouped classes into code solutions. Internal application method calls can be
converted to API operations so that the new, smaller services can function independently from
the monolithic application.

###### Porting Assistant for .NET integration

You can determine whether your application dependencies are compatible with .NET Core.
Dependencies that are compatible with .NET Core can be grouped together using the Porting Assistant for .NET
integration with Microservice Extractor. Microservice Extractor detects whether Porting Assistant for .NET is installed on your machine and
gives you the option to include .NET Core compatibility data. When this intergration is enabled,
you can view .NET Core compatible dependencies in the visualization panel for your monolithic
application. You can also perform single-step extract-and-port operations on the extracted
microservice or monolithic application as part of the extraction workflow.

###### Automated refactoring recommendations

You can start refactoring older monolithic applications when you are not familiar with
their original architecture or retrofitted features. The prescriptive guidance provided by
AWS Microservice Extractor for .NET's automated recommendations reduces the time it takes to identify and refactor
microservices from legacy applications.

AWS Microservice Extractor for .NET's automated recommendations and prescriptive guidance allows you to start
refactoring older monolithic applications when you are not familiar with their original
architecture or retroffitted features. The prescriptive guidance and recommendations from
AWS Microservice Extractor for .NET reduces the time it would normally take to refactor microservices from legacy
applications.
