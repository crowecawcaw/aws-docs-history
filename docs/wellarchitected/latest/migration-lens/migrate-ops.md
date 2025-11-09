# Migrate

The migrate phase is a pivotal stage in any migration process, and
effective strategies are key to success. It's essential to have a
well-defined testing phase strategy that covers thorough testing
of workloads in the AWS cloud environment. Rigorous and
appropriate testing helps identify and rectify issues before they
impact operations. Additionally, it's crucial to review your
application lifecycle management, such as the CI/CD pipeline, and
make necessary adjustments once your workloads are in the AWS Cloud. Aligning your application deployment and management
processes with the cloud environment can enhance efficiency and
maximize the benefits of AWS migration.

| MIG-OPS-08: What is your testing phase strategy? |
| ------------------------------------------------ |
|                                                  |

Every application migration has a testing phase, and you have to
plan how the tests are done, what to test, and what are the test
criteria. Functional testing ensures the seamless integration of
your application with the new environment, requiring the
development of comprehensive unit tests to validate application
workflows. Meanwhile, performance testing evaluates system
response times, identifies bottlenecks, and facilitates
optimization efforts, with cycles of testing and optimization as
needed.

## MIG-OPS-BP-8.1 Ensure you have a testing strategy in place

This BP applies to the following best practice areas: Prepare

With a rehost migration strategy, there is generally no need to perform a full regression functional test, like what you might perform with a major update to an application's code base. Logically, the application architecture and code base are unchanged in AWS, but there have been changes in the infrastructure and it's important to focus the testing on those areas.

When using a rehost migration pattern, your source workloads are cloned into AWS, and when they launch on the Amazon EC2 platform, they may attempt to speak to the services and applications which are still hosted on-premises. This could cause outages to your live systems and corrupt application data, so any testing with cloned workloads must be performed within an isolated network environment, or while the source systems are powered off. Even with source systems powered off, there can still be complications with shared user authentication systems (like Microsoft Active Directory) being updated by test systems.

This need for isolation makes meaningful application testing challenging. Technically, you could provision an isolated network in AWS for testing, but this would also need to permit safe and secure access to a number of shared infrastructure services, perhaps interface with other business critical applications still on-premises, and end users would need to be able to connect to the test application to run the tests. This generally requires significant effort, without really providing the assurance sought, as so much needs to be implemented to protect or replicate the source environment that it becomes questionable if you are actually performing representative testing.

### Implementation guidance

**Suggestion 8.1.1**: Use a risk-based, _points of change_ testing strategy with your applications.

The primary change point is in the network, as the application's servers would be hosted in the AWS Cloud, which may have changed the prevailing network latency and could negatively impact end-user performance or interfaces with other applications. Additionally, there may be new controls implemented in the network, with additional firewall rules or network security groups which could impact connectivity to internal or external users, other applications, or external systems. You should create a series of test cases that perform transactions most likely to be impacted by increased network latency, or new network controls, and this may need to be performed from a variety of different user types (for example, internal browser user, fat-client desktop internal user, external browser user, or cloud-hosted virtual desktop user). Have a minimal set of functional test cases that validate the basic application capabilities (for example, user login, navigation around the application, and access to interfacing systems), and create a baseline set of test results from the applications before migration. Finally create a set of test cases that validate operational integration with the cloud operating strategy and model to verify the operational readiness to run the applications in AWS Cloud.

**Suggestion 8.1.2**: Test potential network latencies before moving workloads to the AWS Cloud.

Understand the network latency variance between the source and target environment. Measure the network latency between your users and your on-premises application servers, then deploy test servers on your target AWS networks and measure network latency between your users and the test workloads. If you have multiple source and target geographies, sites, or campuses and user locations (such as virtual desktop on-premises, fat-client on corporate network, or remote laptop on internet and VPN), document and baseline each scenario, then provide the network latency baselines to the migration planning team. It's a common scenario to migrate some of your workloads while keeping identity and access management systems on-premises (for example, Microsoft Active Directory). In this case, you need to consider the extra latency required to authenticate user and application activity. One best practice to minimize potential impact is to extend and configure your on-premises Active Directory domain into AWS, so that workloads running in AWS can communicate with Microsoft AD services hosted there. To explore the options for Microsoft Active Directory in AWS, see [Active Directory Domain Services on AWS](https://aws.amazon.com/solutions/partners/active-directory-ds/ "https://aws.amazon.com/solutions/partners/active-directory-ds/").

**Suggestion 8.1.3**: Test application performance before and after migration.

If application transaction performance is important, procure up-to-date performance tests results for the applications before migration, and repeat the same performance tests using the same test suite in the AWS Cloud. Attempting to compare test results from different test tools won't give you the assurance you want. Restrict performance testing to only what is needed to validate acceptable performance, with tests that focus on the points of change in the migrated application instance. If performance testing is not within an acceptable range, a rollback decision should be taken immediately to avoid impacting your business. Consider using automated test tools to minimize the time and effort required.

**Suggestion 8.1.4**: Perform a test cutover in AWS Application Migration Service.

The server test cutover is essential for confirming Application Migration Service is able to successfully create a clone of the source server which can boot up on the Amazon EC2 platform. The test cutover should be performed within an isolated subnet in AWS, especially for Active Directory connected Windows workloads, to protect live systems and data hosted on-premises. Application Migration Service provides the ability to specify which AWS subnet to use for test cutovers.

| MIG-OPS-09: Have you reviewed your application lifecycle management (like your CI/CD pipeline) and verified if it needs any adjustment once your workloads are in the AWS Cloud? |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                                                  |

CI/CD pipelines or software development lifecycles (SDLC) can
vary in complexity between applications and businesses. Many
contain deployment steps that interact with the underlying
infrastructure in order to provision and de-provision resources,
while others may just need connectivity to code repositories and
tools. When migrating these applications to AWS, take these
processes into consideration, as it requires multiple stages to
migrate both the running application and the associated
deployment pipelines if present.

## MIG-OPS-BP-9.1 Determine if your current CI/CD pipeline works on AWS

This BP applies to the following best practice areas: Prepare

### Implementation guidance

**Suggestion 9.1.1**:
Assess your existing pipeline tools.

An assessment of each tool in the pipeline is required to
verify that it has capabilities to work with the AWS
services required. This assessment drives the requirement to
either build the migration plan and updates required to
support the new target AWS landing zone, or the selection of
new tools to achieve the desired outcome.

## MIG-OPS-BP-9.2 Provision resources through infrastructure as code (IaC) templates

This BP applies to the following best practice areas: Prepare

### Implementation guidance

**Suggestion 9.2.1**: Consider using AWS CloudFormation.

It is recommended that all resources required for each application are provisioned through IaC templates. These templates could be written in [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") or another IaC tool. This approach keeps configuration with the application code so it can be managed centrally. With the rehost migration pattern, AWS MGN takes care of the source workload migrations, including all application data and configuration present on the source systems. However, the infrastructure components and configuration around the migrated application server on the Amazon EC2 platform still need to be deployed (for example, VPCs, subnets, network security groups, network access control lists, and load balancers).

**Suggestion 9.2.2**: Consider using a configuration management tool.

Maintain an accurate and complete record of all your cloud workloads, their relationships, and configuration changes over time. For more detail, see [Configuration management](../../../whitepapers/latest/aws-caf-operations-perspective/configuration-management.md "../../../whitepapers/latest/aws-caf-operations-perspective/configuration-management.md").
