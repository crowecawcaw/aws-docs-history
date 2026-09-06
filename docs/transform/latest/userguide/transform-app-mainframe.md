

# Modernization of mainframe applications
<a name="transform-app-mainframe"></a>

AWS Transform is designed to accelerate the modernization of legacy mainframe applications. It orchestrates the analysis of mainframe codebases, generate documentation, extract business logic, decompose monolithic structures, transform legacy code, and manage the overall journey with human inputs (HITL) when needed. The transformation capabilities of AWS Transform for modernizing and migrating mainframe applications empower you to modernize your critical mainframe application faster, while preserving your business-critical logic throughout the transformation process.

**Topics**
+ [Capabilities and key features](#transform-app-mainframe-features)
+ [High-level walkthrough](#transform-app-mainframe-highlevel-walkthrough)
+ [Human in the loop (HITL)](#transform-app-mainframe-hitl)
+ [Supported file types for transformation of mainframe applications](#transform-app-mainframe-supported-files)
+ [Supported Regions and quotas for AWS Transform mainframe](#qt-webapp-mainframe-service-regions)
+ [High-level overview of mainframe modernization journey](transform-app-mainframe-modernization-journey.md)
+ [Transformation of mainframe applications](transform-app-mainframe-workflow.md)
+ [Build and deploy your modernized application post-refactoring](transform-app-mainframe-workflow-build-deploy.md)

## Capabilities and key features
<a name="transform-app-mainframe-features"></a>

AWS Transform provides the following capabilities for mainframe modernization:
+ Supports modernization of z/OS mainframe applications written in COBOL (Common Business-Oriented Language) and PL/I (Programming Language One) with associated JCL (Job Control Language), CICS (Customer Information Control System) transactions, BMS (Basic Mapping Support) screens, Db2 databases, and VSAM (Virtual Storage Access Method) data files.
+ Supports refactoring of Fujitsu GS21 mainframe applications with PSAM (Presentation Service Access Method), Japanese character sets, and NDB (Network Data Base) data files.
+ Performs goal-driven reasoning, analysis, decomposition, planning, documentation generation, and code refactoring.
+ Automatically refactors COBOL-based mainframe workloads into modern, cloud-optimized Java applications. 
+ Orchestrates and integrates seamlessly with underlying tools executing analysis, documentation, decomposition, planning, and code refactoring.
+ Helps you set up cloud environments for modernized mainframe applications by providing ready-to-use Infrastructure as Code (IaC) templates.

## High-level walkthrough
<a name="transform-app-mainframe-highlevel-walkthrough"></a>

Here's a high-level walkthrough of AWS Transform for modernizing and migrating mainframe applications.

1. Start a chat with AWS Transform, and enter an objective.

1. Based on your objective, AWS Transform proposes a modernization plan––breaking down the high-level goal into intermediate steps.

1. Depending on the goal you provided, AWS Transform can:
   + Assess and reimagine the codebase
   + Create a custom job based on the objective

Along the way, AWS Transform might request information from you to execute the tasks.

**Note**  
For more information about AWS Transform for mainframe refactor capabilities, see [Create a project](https://bluinsights.aws/docs/transformation-center-create-a-project/) in the AWS Transform for mainframe refactor documentation.

## Human in the loop (HITL)
<a name="transform-app-mainframe-hitl"></a>

Throughout the transformation of mainframe applications, you can monitor the progress and status of the transformation tasks through the AWS Transform web experience.

AWS Transform will gather additional information from you in the following scenarios:
+ When additional information is needed to execute tasks.
+ When approval is required for intermediate artifacts (for example, domains decomposition or wave planning).
+ When issues arise that AWS Transform cannot automatically resolve.

## Supported file types for transformation of mainframe applications
<a name="transform-app-mainframe-supported-files"></a>

The supported file types for z/OS include:
+ COBOL artifacts and related CPY (Copybooks)
+ PL/I source files
+ JCL (Job Control Language) and JCL Procedure (PROC)
+ CICS System Definition (CSD)
+ BMS (Basic Mapping Support)
+ Db2 databases
+ VSAM (Virtual Storage Access Method)
+ IMS TM (Transaction Manager)

The supported file types for Fujitsu GS21 include:
+ PSAM (Presentation Service Access Method)
+ ADL (AIM Definition Language)
+ NDB (Network Data Base)

For more information about Fujitsu GS21 see these topics in the *AWS Transform for mainframe* migration guide:
+ [GS21](https://bluinsights.aws/docs/codebase-dependencies-languages-gs21)
+ [Capture & Replay - GS21 Terminals](https://bluinsights.aws/docs/terminals-gs21)
+ [Mainframe, AS400, Open VMS and GS21 ](https://bluinsights.aws/languages/mainframe-as400-and-open-vms)

## Supported Regions and quotas for AWS Transform mainframe
<a name="qt-webapp-mainframe-service-regions"></a>

For a list for supported Regions, see [Supported Regions for AWS Transform](regions.md).

**Note**  
Your data might be processed in a different Region from the Region where you use AWS Transform. For information on cross-region processing, see [Cross-region processing in AWS Transform](cross-region-processing.md).

For the quota limits, see [Quotas for AWS Transform](transform-limits.md).