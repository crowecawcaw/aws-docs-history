AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Overview

The following are the high-level steps for using AWS Microservice Extractor for .NET to modernize your
monolithic application by extracting it into smaller services.

1. **Onboard and analyze the application** —
   Onboard the application to Microservice Extractor by providing access to the application
   source code and binaries. The backend service logic of the application is
   analyzed by Microservice Extractor to understand the application and node structure, and
   the dependencies between nodes. Nodes represent classes in the source code of
   the application. The results of this analysis can help you to understand how to
   better group functionalities into separate services. If you have runtime
   profiling data that represents production data, you can optionally use it with
   the analysis to collect actionable runtime metrics. If Porting Assistant for .NET is installed on
   your machine, you can optionally include .NET Core 5 and 6 compatibility data in
   the visualization side panel.
2. **Assist with identifying grouped classes to extract as
   independent services** — Microservice Extractor creates a graphical
   representation of the application that shows the nodes, node types,
   dependencies, and groupings based on dependency coupling. If you have uploaded
   runtime profiling data during application onboarding, for example, transactional
   call volume, then it will be displayed. This graphical representation assists
   you with extracting groupings of nodes as isolated services.
3. **Automated grouping recommendations** —
   You can get grouping recommendations from Microservice Extractor instead of manually
   creating groupings. Microservice Extractor uses machine learning-driven analysis of your
   source code to generate grouping recommendations.
4. **Refactor source code and extract grouped
   nodes** — After the parts of the application that you want
   to extract are grouped and selected, refactor source code by isolating business
   domains and removing dependencies between them. Then, extract the groups as
   separate code solutions. After extracting the groups as separate solutions, you
   can manually edit and build the code solutions, and deploy them as independent
   services in containers.
