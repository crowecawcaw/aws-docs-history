AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Blu Age FAQ

## General

1. **What is the main purpose of AWS Blu Age Refactoring
   capability?**

The refactoring capability refactors legacy monolithic code into java using
contemporary distributed applications using modern languages and frameworks,
following an automated refactoring pattern. This pattern involves automatically
analyzing legacy code, understanding its functionality, and converting it into
equivalent modern code while preserving business logic. The process includes
modernizing not just the code, but also the entire application stack,
dependencies, and infrastructure using automated tools and processes. The
solution aims to speed up modernization while maintaining functional equivalence
and performance. This includes transforming both application code and associated
databases and data stores, while implementing cloud best practices and design
patterns. 2. **Which mainframe applications are supported by
AWS Blu Age?**

AWS Blu Age currently supports the modernization of IBM z/OS mainframe applications
written in COBOL, PL/I, JCL (Job Control Language) and relying on CICS (Customer
Information Control System) transaction manager, BMS (Basic Mapping Support)
screens, IMS MFS Screens, DB2 databases, IMS databases, Flat files, GDG
(Generation data groups) and VSAM (Virtual Storage Access Method) data files. 3. **What mainframe languages can AWS Blu Age
modernize?**

AWS Blu Age transforms COBOL and PL/I code to Java, JCLs to Groovy, screens (BMS or
MFS) to HTML (with Sass) and JavaScript (Angular applications – React is not
supported for now), enabling the modernization of legacy mainframe applications
to cloud-native architectures. These technologies are chosen for their
widespread adoption, robust ecosystem, and cloud-native capabilities. Angular
provides a modern, responsive user interface layer that replaces legacy
green-screen interfaces. It enables the creation of dynamic, user-friendly web
applications that can be accessed across different devices and platforms. Its
component-based architecture supports maintainable and scalable front-end
development. The transformation results in distributed applications that follow
modern architectural patterns and best practices. 4. **How does AWS Blu Age balance legacy constraints with cloud
benefits?**

AWS Blu Age achieves balance by preserving critical business logic and functionality
while introducing cloud-native capabilities. It ensures that modernized
applications maintain necessary legacy business logic while taking advantage of
cloud scalability, agility, and modern operational practices. This approach
helps organizations maintain business continuity while gaining the benefits of
cloud infrastructure. 5. **What role does service-oriented architecture play in the
modernized application?**

Service-oriented architecture plays a fundamental role in breaking down
monolithic applications into more manageable modular components. AWS Blu Age creates
service-oriented and object-oriented applications that facilitate better
maintainability and scalability. This architectural approach enables
organizations to achieve greater business efficiency and prepare for potential
future microservices adoption. 6. **What aspects of the application stack are included in
the refactoring process?**

The refactoring process includes the complete software stack: application
code, dependencies, databases, and infrastructure (e.g. options for caching,
messaging support, etc). It covers the transformation of legacy programming
languages, database systems, data files, and associated infrastructure
components. This comprehensive approach ensures all aspects of the application
are modernized cohesively, resulting in a fully transformed modern application
stack. 7. **Does the AWS Blu Age modernization process eliminate the need
for any testing or quality assurance checks on the modernized Java
application?**

No, the AWS Blu Age modernization process doesn't eliminate the need for any testing
or quality assurance checks on the modernized Java application. 8. **What does AWS Blu Age JAC stand for?**

JAC stands for JICS Administration Console 9. **How can I access the AWS Blu Age tooling?**

AWS Blu Age tooling is accessible through the AWS Console via AWS Mainframe Modernization (M2)
Refactor, with feature access based on your accreditation level. Start with the
Transformation Center to assess automatic Java refactoring of your source code.
For detailed guidance, refer to the [AWS
Blu Insights](https://bluinsights.aws/ "https://bluinsights.aws/") documentation. After modernization, you can deploy
applications using runtime. For more information, see [AWS Mainframe Modernization
documentation](ba-runtime-options.md "ba-runtime-options.md"). 10. **How to size (workload and timeline) a
project?**

See [AWS Blu
Insights Estimates](https://bluinsights.aws/docs/business-estimate/ "https://bluinsights.aws/docs/business-estimate/") for more information on this or work with your
Account Manager. 11. **Are there specific requirements to maintain Java AWS Blu Age
migrated solutions?**

No, there are no specific requirements to maintain Java AWS Blu Age migrated
solutions. 12. **What are the technical specifications and
compatibility of AWS Blu Age generated code?**

AWS Blu Age generated code is designed with specific technical characteristics and
broad compatibility. While it doesn't support JPA, it uses direct SQL execution
with externalized queries. The code relies on runtime-specific libraries for
functional equivalence, web services generation, and MQ implementations. The
generated code can be imported into any Java IDE for development, testing,
building, and deployment, though required libraries must be imported
accordingly. While Maven is integrated by default with AWS Mainframe Modernization service for
build processes, alternative tools like Gradle can be used by modifying the
packaging format after transformation. The platform offers flexibility in terms
of development tools and source control, with training available for development
teams managing the code. For more information, see [AWS Blu Age Runtime high level architecture](ba-shared-architecture.md "ba-shared-architecture.md").

## AWS Blu Age Runtime

1. **Where can I find information about
   AWS Blu Age Runtime?**

Refer the [Set up AWS Blu Age Runtime](ba-runtime-setup.md "ba-runtime-setup.md") documentation runtime
that details set-up process onboarding, retrieving artifacts, deployment, etc. 2. **Are the AWS Blu Age JAR dependencies uploaded to the client's
Maven Repository for local development?**

Libraries can be imported into EC2 using an AMI which can be used
for configuring Development, Test & Production environment. Training
& enablement will be given to the team to maintain/enhance the generated
application code. For more information, see [AWS Blu Age Runtime high level architecture](ba-shared-architecture.md "ba-shared-architecture.md"). 3. **What does the term “Gapwalk” refer to in the distributed
AWS Blu Age Runtime jars?**

For information on Gapwalk, see [AWS Blu Age Runtime artifacts](ba-runtime-artifacts.md "ba-runtime-artifacts.md") . 4. **How to request access to the AWS Blu Age Runtime
?**

The Runtime is accessible through the [Blu Age Toolbox](https://bluinsights.aws/docs/bluage-toolbox-introduction "https://bluinsights.aws/docs/bluage-toolbox-introduction") on Blu Insights. 5. **What are the supported Runtimes for AWS Blu Age refactored
applications?**

AWS Blu Age offers a single Runtime to cater to different stages of your modernization journey and operational needs see [AWSBlu Age Runtime](ba-runtime-options.md "ba-runtime-options.md"). 6. **When is the AWS Blu Age Runtime
used?**

An AWS Blu Age Runtime is necessary to support the execution of
AWS Blu Age refactored applications. A runtime is necessary during
AWS Blu Age-based refactoring projects for testing the refactored
applications. Once refactoring project is over, a runtime is also
needed for maintaining, testing, and running AWS Blu Age refactored
applications in production. 7. **How does AWS distribute new releases for AWS Blu Age Runtime?**

The AWS Blu Age Runtime releases are accessible through the [Blu Age Toolbox](https://bluinsights.aws/docs/bluage-toolbox-introduction "https://bluinsights.aws/docs/bluage-toolbox-introduction"). See the [AWSBlu Age release notes](ba-release-notes.md "ba-release-notes.md"). 8. **How often are new major and minor versions
of AWS Blu Age runtime released?**

For more information,
see [AWS Mainframe Modernization components lifecycle](lifecycle-m2.md "lifecycle-m2.md"). 9. **How does AWS provide support for
AWS Blu Age Runtime?**

Support is provided through AWS Support, where issues are addressed
by raising a ticket, and the standard SLA applies. For more information, see [AWS Mainframe Modernization components lifecycle](lifecycle-m2.md "lifecycle-m2.md"). 10. **What does the AWS Mainframe Modernization AWS Blu Age Runtime entail?**

The AWS Blu Age Runtime includes toolbox libraries for accelerating modernization,
facilitating cloud integrations, and improving code quality and maintainability.
It also enables more modernization automation by facilitating transitions
between legacy architectures and cloud architectures. The runtime provides
support for handling legacy verbs and data structures memory representations
using java idioms. It allows building modernized applications based on
object-oriented programming techniques and able to reproduce legacy control
flows. It modernizes legacy VSAM data sets or IMS hierarchical databases support
using a relational database such as Amazon Aurora. It provides java replacements for
legacy system utilities (IDCAMS, IEBGENER, DFSORT,etc), and legacy transaction
management systems (CICS, IMS). It facilitates cloud integrations with caching
in Amazon ElastiCache and support for AWS messaging solutions (SQS, Kinesis). 11. **Does AWS Blu Age Runtime support non-x86
computer architectures?**

Currently, AWS Blu Age Runtime only support x86-based computer architectures
and compute. AWS Blu Age Runtime doesn't support ARM-based and Graviton-based
compute. 12. **How can customers stay informed about AWS Blu Age Runtime versions,
including notifications of new
releases and access to version history and release
notes?**

New versions of AWS Blu Age Runtime are uploaded to our [official release page](ba-release-notes.md "ba-release-notes.md"). We recommend checking this page regularly,
ideally every 3 months, for the latest versions and updates. Regarding access to
version history and release notes, availability depends on the end-of-life (EOL)
date for each major version. For detailed information on EOL dates, version
upgrade planning, and access to historical information, see
[AWS Blu Age lifecycle](ba-lifecycle.md "ba-lifecycle.md"). 13. **What are the main components of AWS Blu Age Runtime high-level
architecture?**

The AWS Blu Age Runtime architecture comprises two main component types. First are Java
libraries (jar files) stored in a shared folder (accessible to the application
server classloader) that provide legacy constructs and statements support.
Second are web applications (war files) containing Spring-based applications
that provide frameworks and services to modernized programs. The runtime also
includes: a Programs Registry that collects all programs for invocation and
cross-program calls and a Scripts Registry that collects all modernized jobs
scripts. These components work together to provide a unified REST-based entry
point and execution framework for modernized applications. The Runtime and the
modernized application are deployed together in an application server (e.g.
Tomcat). 14. **How to configure the shared folder holding AWS Blu Age Runtime
artifacts?**

The AWS Blu Age Runtime artifacts (jars) must be gathered in a shared folder, accessible to
the application server classloader. For a tomcat server, the configuration is
made by modifying the regular configuration file named catalina.properties. For
instance, if you created the shared folder as a folder named “shared”, in the
tomcat folder, you will need to modify the common.loader entry in the
catalina.properties to make the shared folder accessible to the tomcat
classloader, as such:

```
common.loader="${catalina.base}/lib","${catalina.base}/lib/*.jar","${catalina.home}/lib","${catalina.home}/lib/*.jar","${catalina.home}/shared","${catalina.home}/shared/*.jar"
```

15. **How does AWS Blu Age Runtime handle statelessness and session
    management?**

AWS Blu Age Runtime implements statelessness and session management through multiple
mechanisms. For HTTP sessions, it uses cookie-based identification with external
cache storage for user context. Sessions can be stored in various datastores
including Amazon ElastiCache, Redis cluster, or in-memory maps. The statelessness design
ensures that most non-transient states are stored externally in a common 'single
source of truth', enabling high availability and horizontal scaling. This
approach, combined with load balancing and shared sessions, allows distribution
of user-facing dialog across multiple nodes. 16. **What role do web applications play in the AWS Blu Age Runtime
environment?**

[Web applications in AWS Blu Age Runtime](ba-shared-architecture.md#ba-shared-architecture-components "ba-shared-architecture.md#ba-shared-architecture-components") serve multiple key functions. They
provide execution frameworks that reproduce legacy environments and transaction
monitors (like JCL batches, CICS, IMS). They offer REST-based entry points
through the `gapwalk-application.war` for triggering and controlling transactions,
programs, and batches. Additionally, they provide emulation of OS-provided
programs and specialized 'driver' programs that legacy applications depend on
for accessing services like IMS DB or user dialogs through MFS. 17. **How are programs registered and managed in AWS Blu Age Runtime?**

Programs in AWS Blu Age Runtime are registered through a [ProgramRegistry system](ba-shared-structure.md#ba-shared-structure-run-call "ba-shared-structure.md#ba-shared-structure-run-call") that populates during server startup. Each
program implements the [Program](ba-shared-structure.md#ba-shared-structure-write "ba-shared-structure.md#ba-shared-structure-write") interface and is marked as a Spring component. Programs are
registered using their identifiers, with multiple entries possible if a program
has several identifiers. The registration process is automatic and logged in
Tomcat logs. The [ProgramRegistry](ba-shared-structure.md#ba-shared-structure-run-call "ba-shared-structure.md#ba-shared-structure-run-call") enables other programs and scripts to locate and
call registered programs, maintaining the modularity and interconnectivity of
the modernized system. 18. **How is configuration managed in AWS Blu Age Runtime
applications?**

Configuration in AWS Blu Age Runtime is managed through YAML files using Spring Boot
framework capabilities. Two main configuration files are used:
application-main.yml for framework configuration and `application-profile.yml` for
client-specific options. The system follows Spring's precedence logic, allowing
configuration overrides through various means. Additional configuration can be
provided through JNDI for databases and command-line parameters, offering
flexibility in configuration management. Loggers configuration is done using
logback xml configuration files. 19. **What role do secrets managers play in the AWS Blu Age Runtime
configuration?**

Secrets managers in AWS Blu Age Runtime secure sensitive configuration data like database
credentials and Redis cache passwords. They allow storage of critical data in
AWS secrets and reference them in YAML configuration files. The system
supports different types of secrets, including database secrets that
automatically populate all relevant fields and single-password secrets for
password-protected resources. This approach enhances security by keeping
sensitive data separate from application configuration. 20. **How can developers write their own programs compatible
with AWS Blu Age Runtime?**

Developers can create AWS Blu Age Runtime-compatible programs by implementing the Program
interface and [following specific patterns](ba-shared-structure.md "ba-shared-structure.md"). The program must be declared as a
Spring component, implement required methods, and be properly registered in the
ProgramRegistry. Developers need to create companion context and configuration
classes, handle program identifiers, and ensure proper integration with the
Spring framework. The implementation should follow AWS Blu Age Runtime conventions for program
structure and execution. 21. **How does AWS Blu Age Runtime handle program execution
errors?**

AWS Blu Age Runtime handles program execution errors through multiple mechanisms. For batch
jobs, it captures execution status, exit codes, and detailed error information
in the job execution details. Error handling includes specific exit codes (-1
for technical errors, -2 for service program failures) and detailed logging in
Tomcat logs. The system can be configured to rollback transactions on runtime
exceptions and provides options for error notification and recovery. Error
details are accessible through REST endpoints for monitoring and
troubleshooting. 22. **What AWS Blu Age Runtime monitoring capabilities are available for
batch jobs?**

AWS Blu Age Runtime provides monitoring capabilities for batch jobs through various [endpoints](ba-endpoints-gapwalk.md#ba-endpoints-gapwalk-batch "ba-endpoints-gapwalk.md#ba-endpoints-gapwalk-batch"). It tracks job execution status, start/end times,
execution mode, and detailed results. The system offers [endpoints](ba-endpoints-gapwalk.md#ba-endpoints-gapwalk-batch "ba-endpoints-gapwalk.md#ba-endpoints-gapwalk-batch") for listing triggered scripts, retrieving job execution
details, and monitoring currently running jobs. Metrics’ endpoints provide JVM
statistics, session counts, and detailed batch execution metrics. The platform
also supports pagination and time-based filtering of monitoring data. 23. **How are AWS Blu Age Runtime job execution statuses tracked and
managed?**

Job execution statuses are tracked through a comprehensive status system that
includes states like DONE, TRIGGERED, RUNNING, KILLED, and FAILED. Each job
execution receives a unique identifier for tracking and maintains detailed
execution information including start time, end time, caller information, and
execution results. The system provides [REST endpoints](ba-endpoints-gapwalk.md#ba-endpoints-gapwalk-batch "ba-endpoints-gapwalk.md#ba-endpoints-gapwalk-batch") for querying job status, managing running jobs, and
retrieving execution history. Status information persists in server memory and
can be purged based on age for resource management. 24. **How does AWS Blu Age Runtime handle external system
interactions?**

The runtime handles external system interactions through various mechanisms,
including REST endpoints for service integration, support for message queues
(SQS, RabbitMQ, IBM MQ), and database connectivity options. It provides
emulation of legacy system interactions through specialized components, supports
SSL/TLS for secure communications, and includes features for handling external
file systems. The system also supports integration with external authentication
providers and can be configured to interact with various third-party
services. 25. **How is authentication handled in AWS Blu Age Runtime?**

AWS Blu Age Runtime supports multiple authentication methods, with OAuth2 being the primary
mechanism. It can integrate with identity providers like Amazon Cognito or
Keycloak. Authentication configuration is managed through the main configuration
file named application-main.yml, where security settings, identity providers,
and authentication methods can be defined. The system supports features like XSS
protection, CORS, CSRF, and can be configured for both global security and
specific endpoint security. For development, a local authentication system with
default super admin credentials is also available. 26. **How does AWS Blu Age Runtime ensure high
availability?**

AWS Blu Age Runtime ensures high availability through several mechanisms. It implements
statelessness by storing non-transient states in external shared storage,
enabling multiple application instances to work together. The system supports
load balancing and shared sessions, allowing requests to be distributed across
multiple nodes. For data storage, it can utilize highly available databases and
caching systems. The architecture supports automatic fail-over and can be
deployed across multiple availability zones for increased reliability. 27. **What component is used to reproduce CICS distributed
transactions with AWS Blu Age applications?**

The AWS Blu Age Runtime provides a dedicated endpoint to allow existing JICS transactions to
be invoked as part of a global transaction (XA support). The underlying two
phases commit support relies on the Atomikos software component. 28. **What is the AWS Blu Age name of the classes that are used to
define specific program behavior?**

Each program is bound to a dedicated Configuration class which allows to
specify the program specific behaviors. For more information on naming and
location conventions, see [AWS Blu Age structure of
modernized application](ba-shared-structure.md "ba-shared-structure.md") 29. **Which encoding has the following character sequence
order: space, lowercase characters, uppercase characters,
numerals?**

Charsets belonging to the EBCDIC variants family (such as CP1047, CP297,
etc). 30. **What are the pricing dimensions for AWS Blu Age Runtime?**

AWS Mainframe Modernization-core-hours (See [AWS Mainframe Modernization
pricing](https://aws.amazon.com/fr/mainframe-modernization/pricing/ "https://aws.amazon.com/fr/mainframe-modernization/pricing/")). 31. **What is the mechanism used to pass raw data through HTTP
to the program endpoints?**

Base64 encoded strings. 32. **How does a user launch a batch job
run?**

Using an HTTP call to one of the dedicated batch endpoint (see [batch endpoints documentation page](ba-endpoints-gapwalk.md#ba-endpoints-gapwalk-batch "ba-endpoints-gapwalk.md#ba-endpoints-gapwalk-batch")). 33. **Which AWS Blu Age Runtime endpoint is the main entry point from the
main web front-end application?**

```
/transaction
```

34. **What does AWS Blu Age JICS stand for?**

The AWS Blu Age JICS is the runtime component used to support the modernization of
CICS resources. The resources definitions are stored in a dedicated data store.
To administer them, use either the REST API or the JICS application console. For
information, see [Manage JICS application
console in AWS Blu Age](ba-endpoints-jac.md "ba-endpoints-jac.md"). 35. **What AWS Blu Age Runtime caching mechanisms are
available?**

AWS Blu Age Runtime supports multiple caching mechanisms, including Redis and EhCache. Redis
is recommended for production environments, providing shared persistent caching
across multiple nodes. EhCache is available for standalone deployments with
embedded volatile local caching. The system supports caching for various
components, including Blusam data, session information, JICS resources, and
temporary storage queues. Cache configuration can be customized for different
use cases and performance requirements. 36. **How do we estimate the price of an AWS Mainframe Modernization AWS Blu Age Runtime
deployment?**

AWS provides estimates to customers based on their requirements and target
architecture. 37. **What is the AWS Mainframe Modernization AWS Blu Age Runtime price?**

AWS Mainframe Modernization offers two pricing models for AWS Blu Age: a Managed Runtime option that
includes the runtime, compute resources, internal storage, and automation, and a
Non-managed Runtime option that covers the AWS Blu Age runtime itself only. For
AWS deployments, both use a pay-as-you-go pricing structure. For the most
up-to-date and detailed pricing information, it's recommended to consult the
official [AWS Mainframe Modernization Pricing](https://aws.amazon.com/mainframe-modernization/pricing/ "https://aws.amazon.com/mainframe-modernization/pricing/") page. 38. **What if we need to deploy an AWS Blu Age refactored
application on an infrastructure not listed in the supported
runtime?**

If you need to deploy an AWS Blu Age refactored application on an
infrastructure not listed in the supported runtime, several options are
available. First, check if your infrastructure is compatible with existing
deployment options like Amazon EKS Anywhere or other container orchestration
platforms. If so, you may be able to use the AWS Blu Age Runtime.
For non-compatible infrastructures, we recommend consulting with an AWS
mainframe specialist to explore custom solutions or potential adaptations. You
can also submit a Product Feature Request (PFR) for expanded infrastructure
support. Contact your AWS representative to discuss your specific needs and
the best approach for your environment. 39. **How is the AWS Blu Age Runtime licensed? Is it open
source?**

AWS Blu Age Runtime is not open source. It's AWS IP distributed as a
cloud-native service. There are two deployment options:

    1. [AWS Blu Age Managed](ba-runtime-options.md#ba-runtime-options-managed "ba-runtime-options.md#ba-runtime-options-managed"), the runtime is deployed into a dedicated
     AWS managed service, taking advantage of an all-preconfigured and
     ready for deployment environment without setup nor
     Administration.
    2. [AWS Blu Age Non Managed](ba-runtime-options.md#ba-runtime-options-non-managed "ba-runtime-options.md#ba-runtime-options-non-managed"), which can be deployed into your own
     bespoke AWS architecture based on Amazon EC2 or Amazon ECS/AWS Fargate, that
     you have to provision and setup by yourself. Both options incur runtime
     fees, which are included in the project estimates provided to you. As
     this is a managed service with Support access, you don't need the source
     code. For more details on pricing, see [AWS Mainframe Modernization Pricing page](https://aws.amazon.com/ar/mainframe-modernization/pricing/ "https://aws.amazon.com/ar/mainframe-modernization/pricing/").

40. **How are changes and upgrades to AWS Blu Age frameworks
    and libraries managed ?**

AWS Blu Age frameworks and libraries are updated through regular code
generation and deployment processes. These updates are managed as part of the
AWS Mainframe Modernization lifecycle, which includes version upgrades and
support from the AWS Blu Age team or certified partners. For detailed
information on versioning, upgrade processes, and support timelines, please
refer to the [AWS Mainframe Modernization lifecycle documentation](lifecycle-m2.md "lifecycle-m2.md"). 41. **What are the supported version of tools (Tomcat, Postgres, MQ, etc.) and dependencies (Spring, Angular, etc.) the AWS Blu Age Runtime uses ?**

See details in [Release Notes](ba-release-notes.md "ba-release-notes.md"). 42. **What does 'Standalone' mean in the context of BAC and JAC ?**

Standalone refers to a special packaging and deployment mode for BAC (Blusam Administration Console) and JAC (JICS Administration Console) that allows these web applications to run independently in their own Tomcat server, separate from your modernized application. The BAC and JAC standalone versions are available into `aws-bluage-webapps-x.y.z.zip`. BAC and JAC non-standalone versions are available into `gapwalk-x.y.z.zip` under `webapps-consoles` folder. See [AWS Blu Age Runtime artifacts](ba-runtime-artifacts.md "ba-runtime-artifacts.md").

## Data

1. **Which database options are available for the modernized
   applications, regarding the modernization of the legacy
   database?**

The modernized applications can use several modern database options including:
PostgreSQL, Amazon Aurora, RDS for PostgreSQL, Oracle database, MS-SQL, and IBM Db2.
These options provide flexibility in choosing the most appropriate database
system based on specific requirements, while leveraging the benefits of modern
database management systems and cloud-native features. 2. **What is the transformation coverage of IBM Db2 for z/OS
to Postgres DDL?**

Full transformation (including database constraints). 3. **Does AWS Blu Age support Group Data Generation
(GDG)?**

Yes, using GDG in batches is supported, with the support of relative and
absolute generations and automatic clean-up strategies. 4. **Does AWS Blu Age support concatenated data
sets?**

Yes, using concatenated data sets in batches is supported. With concatenation
in action, several data sets can be read as a single data set. Please note that
the Blusam data sets cannot be part of a concatenation. 5. **What is the process applied on SQL
queries?**

Adjusted during code transformation, depending on the target database. 6. **Which options apply if there are multiple databases for
an application?**

Configure the target database for each query and define all the databases in
the application and in Apache Tomcat. 7. **Can Blusam be disabled?**

Yes, in the main configuration file, and no database is required (for more information, see
[Blusam configuration documentation page](ba-shared-blusam.md#ba-shared-blusam-configuration "ba-shared-blusam.md#ba-shared-blusam-configuration")). 8. **Which AWS Blu Age API is used to replace databases such as IMS
DB?**

The JHDB (Java Hierarchical DataBase) API. 9. **Which AWS Blu Age product can be used to migrate legacy data
and databases to a modern relational database management system
(RDBMS)?**

AWS Blu Age DB modernization Tool ([Data
Migrator](https://bluinsights.aws/docs/data-migrator-introduction "https://bluinsights.aws/docs/data-migrator-introduction")). 10. **What is AWS Blu Age Data Simplifier and what problem does it
solve in modernization?**

[Data Simplifier](ba-shared-data.md "ba-shared-data.md") is a core library in AWS Blu Age that addresses the
challenge of handling legacy memory access patterns in Java. It provides
constructs to support low-level memory access, legacy data types (like zoned,
packed, alphanumeric), and mixed structured/raw memory access that are common in
mainframe applications but not natively available in Java. The library exposes
these features through familiar Java patterns like getters/setters and
class-based APIs, making them accessible to Java developers while maintaining
legacy functionality. 11. **How does AWS Blu Age handles legacy memory layouts and data
structures?**

AWS Blu Age handles legacy memory layouts through the [Record](ba-shared-data.md#ba-shared-data-fqn "ba-shared-data.md#ba-shared-data-fqn") interface, which provides an abstraction of byte arrays with
fixed size. For structured data like COBOL '01 data items', it uses [RecordEntity](ba-shared-data.md#ba-shared-data-fqn "ba-shared-data.md#ba-shared-data-fqn") subclasses that are automatically generated during
modernization. These classes maintain the hierarchical structure of the legacy
data, with each element having a parent-child relationship. The system supports
both raw memory access and structured access patterns, preserving the
flexibility of legacy systems while providing a modern programming
interface. 12. **How does AWS Blu Age deals with VSAM data sets
modernization?**

The [Blusam](ba-shared-blusam.md "ba-shared-blusam.md") component is
providing the support for the modernization of the VSAM data sets, with a
dedicated API, endpoints and an administration web-application (BAC: [Blusam Administration Console](ba-shared-bac-userguide.md "ba-shared-bac-userguide.md")). Blusam relies on a relational
database as backend (PostgreSQL, either using RDS or Aurora).

## Transformation

1. **Were can I found details about the transformation
   process?**

See [AWS Blu Insights](https://bluinsights.aws/ "https://bluinsights.aws/")
documentation. 2. **What are the names of the AWS Blu Age generated
modules?**

Service, entities, web, and tools. 3. **Why was Java/Spring chosen as one of the target
technologies for AWS Blu Age?**

Java/Spring was chosen as a target technology because of its widespread
adoption, large talent pool, and robust enterprise capabilities. The Java
ecosystem offers extensive libraries, frameworks, and tools that support modern
application development. Spring framework provides enterprise-grade features,
cloud-native capabilities, and follows industry best practices, making it ideal
for modernized applications. 4. **What is the name of the parent project that contains the
AWS Blu Age generated modules?**

The name of the parent project is suffixed by “-pom” and can be defined in the
Transformation Center using the Transform property named project. 5. **How does AWS Blu Age manage legacy scheduler modernization, if
provided?**

Legacy scheduler assets are not being modernized by AWS Blu Age. They’re being taken
into account during the assessment phase, to help identify possible missing
artifacts. 6. **What is the requirement for debugging the generated code
with AWS Blu Age?**

Any integrated development environment (IDE) supporting Java, such as Eclipse,
JetBrain, or VisualCode.

## Deployment

1. **Which environments are available to deploy the
   modernized application with AWS Blu Age?**

Windows Server, Linux server, and Docker Linux container. 2. **Can AWS Blu Age refactored applications run on any
infrastructure?**

While AWS Blu Age refactored applications are not designed to run on any
infrastructure, they offer significant flexibility in deployment options. These
applications can be deployed on various compute platforms, including cloud
managed services, serverless compute, and on-premises infrastructure. 3. **Which MQ configuration does AWS Blu Age
support?**

SQS, IBM WebSphere MQ. 4. **Into which application servers can a user deploy Java
business application logic with AWS Mainframe Modernization
runtime?**

Apache Tomcat, version greater or equal to 10.1. 5. **How does the refactored application integrate with other
AWS services like Amazon Aurora?**

The modernized application integrates with AWS services by supporting
transformation to cloud-native database solutions like Amazon Aurora and RDS for
PostgreSQL. AWS Blu Age ensures integration between modernized applications and
AWS services, enabling organizations to use cloud capabilities. This
integration extends to both data storage and application services within the
AWS ecosystem. Beyond database storage, AWS Blu Age Runtime integrates with various
AWS services including Amazon ElastiCache for Redis caching, AWS Secrets Manager for
configuration management, and AWS Mainframe Modernization for deployment. It supports Amazon EC2, Amazon EKS,
ECS managed by Fargate for container deployment. The system can utilize
AWS Identity and Access Management for authentication, Amazon Simple Storage Service for storage, and supports integration
with other AWS services through configuration and service connectors. 6. **How does the refactored application ensure scalability
requirements are met?**

The solution ensures scalability by transforming applications into
cloud-native architectures that can use the AWS elastic infrastructure. It
implements modern design patterns and best practices that enable horizontal and
vertical scaling. The service-oriented approach allows for independent scaling
of components. The modernized applications can take advantage of cloud services'
inherent scalability features. 7. **What happens after the source code refactoring is
completed?**

After source code refactoring, two main steps occur. First, the refactored
application is built. Second, the application is deployed. The deployment is done in your AWS account ([AWS Mainframe Modernization AWSBlu Age Runtime](ba-runtime-setup.md "ba-runtime-setup.md")) where
customers manage their own infrastructure and deploy on various platforms, including Amazon EC2, ECS on EC2 or on Fargate, EKS on EC2. 8. **How can I deploy and run an application modernized with
AWS Blu Age on a custom Amazon Linux AMI?**

This can be achieved by deploying the application using AWS Blu Age Runtime
on Amazon EC2. The process involves creating a Java/Spring
application with a dependency on the AWS Blu Age Runtime library and deploying
it on a custom Amazon Linux AMI. For detailed instructions on this approach,
see [Set up AWS Blu Age Runtime on Amazon EC2](ba-runtime-deploy-ec2.md "ba-runtime-deploy-ec2.md"). 9. **Is there an Amazon Machine Image (AMI) available? Is
there a Docker image available?**

    * **AMI**: No, due to customers' needs to
     customize and set up their environment as they prefer, there is no AMI
     available. Customers can retrieve the AWS Blu Age artifacts and set up
     their instance according to their requirements.
    * **Docker Image**: No, there is no
     available docker image, out of the box, but the [Set up
     AWS Blu Age Runtime on container](ba-runtime-deploy-container.md "ba-runtime-deploy-container.md") page explains how to build and deploy
     your own docker image based on AWS Blu Age Runtime binaries, to a suitable container
     management system.

10. **Can customer package and run an AWS Blu Age application
    as a Docker container?**

Yes, refer to [Set up AWS Blu Age Runtime on container](ba-runtime-deploy-container.md "ba-runtime-deploy-container.md"). 11. **How does job scheduling work with
batch?**

It is integrated with Control-M /Stone branch or with any other Distributed
scheduler.

## Security

1. **How does the application protect against SQL injection attacks?**

The application implements SQL best practices throughout. All database queries use prepared statements, which effectively prevent SQL injection attacks by separating SQL code from user supplied data. This ensures that user input is always treated as data rather than executable code. 2. **What measures are in place to prevent OS command injection vulnerabilities?**

AWS security teams conduct regular security reviews of AWS Blu Age Runtime. If the teams detect any anomalies such as code that could potentially allow OS command injection, AWS immediately works to resolve. This continuous monitoring ensures that the runtime remains secure against command injection threats. 3. **Is the application vulnerable to directory traversal attacks?**

No. This vulnerability does not apply to the front-end Angular application. For the back-end, the application uses only one endpoint with a limited interface contract that never contains "path" or "directory" information. This design eliminates the risk of directory traversal attacks. 4. **How does the application protect against XSS attacks?**

The application follows Angular security best practices as described in the official [Angular security documentation](https://angular.dev/best-practices/security "https://angular.dev/best-practices/security"). The application's nature is inherently limited in terms of UI since it corresponds to the legacy mainframe application. The application handles no URLs, dynamic scripts, or HTML generated by the back-end. This limited attack surface significantly reduces XSS risks. 5. **What protection is implemented against CSRF attacks?**

The application utilizes Spring's native [CSRF support](https://docs.spring.io/spring-security/reference/servlet/exploits/csrf.html "https://docs.spring.io/spring-security/reference/servlet/exploits/csrf.html"), which provides robust protection against cross-site request forgery attacks out of the box. 6. **Can user input lead to HTTP header injection?**

No. User inputs are strictly limited in length to match the legacy mainframe application format. When the back-end receives a request, it immediately formats the input according to predefined formats, which would truncate any injected content. Additionally, the application never constructs HTTP headers based on user inputs in the single endpoint used by the application, making HTTP header injection impossible. 7. **How is the application protected against clickjacking attacks?**

The application performs most actions using keystrokes rather than mouse clicks, making it inherently resistant to clickjacking attacks. This design choice significantly reduces the attack surface for this type of vulnerability. 8. **Can buffer overflow attacks occur in the application?**

No. User inputs are strictly limited in length to correspond with the legacy mainframe application format. When the back-end receives a request, it immediately formats the input according to the corresponding formats, preventing buffer overflow conditions from occurring. 9. **How are access control and authorization managed?**

Access control determines globally whether users have rights to access the unique back-end endpoint. Once authenticated, the application code and data handle authorization controls. This ensures proper separation of concerns and secure access management. 10. **What measures prevent session hijacking?**

The combined use of Spring and Angular native capabilities for session management and XSS prevention, along with adherence to framework best practices, prevents session hijacking. The application can further enhance protection by:

    * **Using HTTPS**: Ensures all communication is encrypted.
    * **Implementing Token-Based Authentication**: The application can activate this when needed.
    * **Monitoring User Sessions**: The application can activate session monitoring and anomaly detection to identify suspicious activity.

These layered security measures provide comprehensive protection against session hijacking attempts.
