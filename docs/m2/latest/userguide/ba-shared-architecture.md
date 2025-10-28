AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Blu Age Runtime high level architecture

As a part of the AWS Blu Age solution for modernizing legacy programs to Java, the AWS Blu Age Runtime provides a unified, REST-based entry point for modernized applications, and a framework of execution for such applications, through libraries providing legacy constructs and a standardization of programs code organization.

Such modernized applications are the result of the AWS Blu Age Automated Refactor process for modernizing mainframe and midrange programs (referred to in the following document as "legacy") to a web based architecture.

The AWS Blu Age Runtime goals are reproduction of legacy programs behavior (isofunctionality), performances (with respect to programs execution time and resources consumption), and ease of maintenance of modernized programs by Java developers, though the use of familiar environments and idioms such as tomcat, Spring, getters/setters, fluent APIs.

###### Topics

- [AWS Blu Age runtime components](#ba-shared-architecture-components "#ba-shared-architecture-components")
- [Execution environments](#ba-shared-architecture-environments "#ba-shared-architecture-environments")
- [Statelessness and session handling](#ba-shared-architecture-stateless "#ba-shared-architecture-stateless")
- [High availability and statelessness](#ba-shared-architecture-stateless-ha "#ba-shared-architecture-stateless-ha")

## AWS Blu Age runtime components

The AWS Blu Age Runtime environment is composed of two kinds of components:

- A set of java libraries (jar files) often referenced as "the shared folder", and providing legacy constructs and statements.
- A set of web applications (war files) containing Spring-based web applications providing a common set of frameworks and services to modernized programs.

The following sections detail the role of both of these components.

### AWS Blu Age libraries

The AWS Blu Age libraries are a set of jar files stored in a `shared/` subfolder added to the standard tomcat classpath, so as to make them available to all modernized Java programs.
Their goal is to provide features that are neither natively nor easily available in the Java programming environment, but typical of legacy development environments.
Those features are exposed in a way that is as familiar as possible to Java developers (getters/setters, class-based, fluent APIs).
An important example is the **Data Simplifier** library, which provides legacy memory layout and manipulation constructs (encountered in COBOL, PL1 or RPG languages) to Java programs.
Those jars are a core dependency of the modernized Java code generated from legacy programs.
For more information about the Data Simplifier, see [What are data simplifiers in AWS Blu Age](ba-shared-data.md "ba-shared-data.md").

### Web application

Web Application Archives (WARs) are a standard way of deploying code and applications to the tomcat application server.
The ones provided as part of the AWS Blu Age runtime aim at providing a set of execution frameworks reproducing legacy environments and transaction monitors (JCL batches, CICS, IMS...), and associated required services.

The most important one is `gapwalk-application` (often shortened as "Gapwalk"), which provides a unified set of REST-based entry points to trigger and control transactions, programs and batches execution.
For more information, see [AWS Blu Age Runtime APIs](ba-runtime-endpoints.md "ba-runtime-endpoints.md").

This web application allocates Java execution threads and resources to run modernized programs in the context for which they were designed.
Examples of such reproduced environments are detailed in the following section.

Other web applications add to the execution environment (more precisely, to the "Programs Registry" described below) programs emulating the ones available to, and callable from, the legacy programs.
Two important categories of such are:

- Emulation of OS-provided programs: JCL-driven batches especially expect to be able to call a variety of file and database manipulating programs as part of their
  standard environment.
  Examples include `SORT`/`DFSORT` or `IDCAMS`.
  For this purpose, Java programs are provided that reproduce such behavior, and are callable using the same conventions as the legacy ones.
- "Drivers", which are specialized programs provided by the execution framework or middleware as entry points.
  An example is `CBLTDLI`, which COBOL programs executing in the IMS environment depend on to access IMS-related services (IMS DB, user dialog through MFS, etc.).

### Programs registry

To participate in and take advantage of those constructs, frameworks and services, Java programs modernized from legacy ones adhere to a specific structure
documented in [AWS Blu Age structure of a modernized application](ba-shared-structure.md "ba-shared-structure.md").
At startup, the AWS Blu Age Runtime will collect all such programs in a common "Programs Registry" so that they can be invoked (and call each other) afterwards.
The Program Registry provides loose coupling and possibilities of decomposition (since programs calling each other do not have to be modernized simultaneously).

## Execution environments

Frequently encountered legacy environments and choreographies are available:

- JCL-driven batches, once modernized to Java programs and Groovy scripts, can be started in a synchronous (blocking) or asynchronous (detached) way.
  In the latter case, their execution can be monitored through REST endpoints.
- A AWS Blu Age subsystem provides an execution environment similar to CICS through:
  - an entry point used to start a CICS transaction and run associated programs while respecting CICS "run levels" choreography,
  - an external storage for Resource Definitions,
  - an homogeneous set of Java fluent APIs reproducing `EXEC CICS` statements,
  - a set of pluggable classes reproducing CICS services, such as Temporary Storage Queues, Temporary Data Queues or files access (multiple implementations are usually available, such as Amazon Managed Service for Apache Flink,
    Amazon Simple Queue Service, or RabbitMQ for TD Queues),
  - for user-facing applications, the BMS screen description format is modernized to an Angular web application, and the corresponding "pseudo-conversational" dialog is supported.

- Similarly, another subsystem provides IMS message-based choreography, and supports modernization of UI screens in the MFS format.
- In addition, a third subsystem allows execution of programs in an iSeries-like environment, including modernization of DSPF (Display File)-specified screens.

All of those environments build upon common OS-level services such as:

- the emulation of legacy memory allocation and layout (**Data Simplifier**),
- Java thread-based reproduction of the COBOL "run units" execution and parameters passing mechanism (`CALL` statement),
- emulation of flat, concatenated, VSAM (through the **Blusam** set of libraries),
  and GDG Data Set organizations,
- access to data stores, such as RDBMS (`EXEC SQL` statements).

## Statelessness and session handling

An important feature of the AWS Blu Age Runtime is to enable High Availability (HA) and horizontal scalability scenarios when executing modernized programs.

The cornerstone for this is statelessness, an important example of which is HTTP session handling.

### Session handling

Tomcat being web-based, an important mechanism for this is HTTP session handling (as provided by tomcat and Spring) and stateless design.
As such statelessness design is based on the following:

- users connect though HTTPS,
- application servers are deployed behind a Load balancer,
- when a user first connects to the application it will be authenticated and the application server will create an identifier (typically within a cookie)
- this identifier will be used as a key to save and retrieve the user context to/from an external cache (data store).

Cookie management is done automatically by the AWS Blu Age framework and the underlying tomcat server, this is transparent to the user.
The user internet browser will manage this automatically.

The Gapwalk web application may store the session state (the context) in various data stores:

- Amazon ElastiCache (Redis OSS)
- Redis cluster
- in memory map (only for development and standalone environments, not suitable for HA).

## High availability and statelessness

More generally, a design tenet of the AWS Blu Age framework is statelessness: most non-transient states required to reproduce legacy programs behavior are not stored inside the application servers, but shared through an external, common "single source of truth".

Examples of such states are CICS's Temporary Storage Queues or Resource Definitions, and typical external storages for those are Redis-compatible servers or relational databases.

This design, combined with load balancing and shared sessions, leads to most of user-facing dialog (OLTP, "Online Transactional Processing") to be distributable between multiple "nodes" (here, tomcat instances).

Indeed a user may execute a transaction on any server and not care if the next transaction call is performed on a different server.
Then when a new server is spawned (because of auto scaling, or to replace a non healthy server), we can guarantee that any reachable and healthy server can run the transaction as expected with the proper results (expected returned value, expected data change in database, etc.).
