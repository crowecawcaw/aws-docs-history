# Generating Microsoft

estimates with AWS Modernization Calculator

AWS Modernization Calculator for Microsoft workloads provides a pricing estimate for
modernizing your Microsoft workloads using open source and AWS cloud-native services
deployed on AWS.

The calculator creates an estimate total cost of ownership for transforming your Windows
and SQL server applications into a modern architecture. To use the calculator, you don't
need an AWS account.

AWS Modernization Calculator for Microsoft workloads recommends modernized architecture
for application patterns such as multi-tier, batch processing, CI/CD, or containerization.
These recommendations are based on commonly adopted architectures by the AWS customer
community. The calculator offers a reliable way to get modernization cost estimates without
in-depth assessments. Using this information, you can conduct an in-depth assessment with
Migration Hub Strategy Recommendations. For more information, see [What is Migration Hub
Strategy Recommendations?](../../../migrationhub-strategy/latest/userguide/what-is-mhub-strategy.md "../../../migrationhub-strategy/latest/userguide/what-is-mhub-strategy.md")

###### Topics

- [Procedure](#modernization-cal-process "#modernization-cal-process")
- [Architecture category and pattern](#step1-pattern "#step1-pattern")
- [Architecture size](#step2-size "#step2-size")
- [Modernized architecture pattern](#step3-architecture "#step3-architecture")
- [AWS service configuration](#step4-configuration "#step4-configuration")
- [My Estimate](#estimate "#estimate")

## Procedure

###### To generate an estimate with AWS Modernization Calculator for Microsoft Workloads

1. Open the AWS Modernization Calculator for Microsoft Workloads at [https://modernization.calculator.aws/microsoft/workload](https://modernization.calculator.aws/microsoft/workload "https://modernization.calculator.aws/microsoft/workload").
2. In the **New estimate** section, add a description for this estimate.
3. In the **Current application/workload location** section,
   choose the current location of where your application is deployed.
4. Select an **Architecture category** and an **Architecture
   pattern**.

For more information on architecture category and pattern, see
[Architecture category and pattern](#step1-pattern "#step1-pattern"). 5. Choose **Next**. 6. On the **Select an architecture size** page, you can select your architecture
characteristics (optional) and sizing.

For more information, see [Architecture size](#step2-size "#step2-size"). 7. Choose **Next**. 8. On the **Select modernized architecture pattern** page, select a modernized
architecture pattern for your application.

For more information, see [Modernized architecture pattern](#step3-architecture "#step3-architecture"). 9. Choose **Next**. 10. On the **Edit service configuration** page, review the summary of recommendations.

For more information, see [AWS service configuration](#step4-configuration "#step4-configuration"). 11. For an overview of your Microsoft estimate, choose **Save**.

For more information, see [My Estimate](#estimate "#estimate")

## Architecture category and pattern

You can specify the architecture category of your application by choosing from **Architecture
pattern**, **Use case**, or **Custom**. The category selection
provides further options to analyze your application.

- **Architecture pattern** refers to a fundamental schema for
  software systems in an organization. It defines the structural composition of
  the program and the interactions between the elements. In most enterprises, some
  of the commonly found patterns include the following.
  - **Multi-tier** pattern has been a cornerstone
    architecture pattern for decades, and remains a popular pattern for
    user-facing applications. Multi-tier generally consists of a
    presentation tier, data tier, and logic tier. These three tiers can be
    hosted on the same or separate servers. This pattern provides a general
    framework to ensure decoupled and independently scalable application
    components can be separately developed, managed, and maintained.
  - **Batch processing** is the method computers
    periodically use to complete high-volume and repetitive data jobs.
    Certain data processing tasks, such as backups, filtering, and sorting,
    can be compute intensive and inefficient to run on individual data
    transactions. Instead, data systems process such tasks in batches. These
    tasks are processed during off-peak times such as the evening and
    overnight.

- **Use case** includes grouped architecture patterns. This
  grouping represents a collaboration by different teams on performing tasks. Use
  cases are further categorized into the following.
  - **Software development** involves several steps
    including creating, testing, staging, and deploying software. In an
    organization, multiple teams collaborate as a group to create
    software.
  - **Container** provides a standard way to package your
    application's code, configurations, and dependencies into a single
    object. Containers share an operating system that's installed on the
    server and run as resource-isolated processes. This ensures quick,
    reliable, and consistent deployments, regardless of the environment.
    Containers are lightweight and provide a consistent and portable
    software environment for applications to run and scale virtually
    anywhere. Building and deploying microservices, running batch jobs for
    machine learning applications, and moving existing applications into the
    cloud are some of common use cases.

- **Custom** category provides you with the option to build any
  custom architectures by selecting the relevant AWS services from the list.
  This is a suitable option if you're familiar with AWS services and their role
  in your application's architecture pattern.

## Architecture size

This step includes a short questionnaire about the specifics of your application's
architecture. All questions are optional. The calculator provides a sizing
recommendation based on your answers. The default recommendation is
**Small**.

If you choose to answer the questions, the calculator recommends a size. You can
proceed with the recommended size or select any size that meets your business
requirements.

## Modernized architecture pattern

The calculator provides modernized architecture pattern options based on
your inputs in preceding steps. You can download the pattern diagram to learn
more.

If you see more than one option, you can choose the recommended or another pattern. If
you have one recommendation without options, choose the recommended pattern to proceed
to the next step.

## AWS service configuration

This page provides a summary of recommendations. You can see a list of
recommended AWS services. You can add or remove any service, and change the
recommended settings of each service.

- **AWS Region** has a drop-down list that you can select the
  Region where you want to host your modernized application from. The pricing of
  AWS services can differ by Region.
- **Estimated cost** provides the total monthly cost of running
  a modernized application on AWS. The cost isn't intended as an actual price
  quote. It doesn't account for data transfer charges or any additional
  configurations offered by AWS services.
- **AWS services** lists the recommended services for your
  modernized application. You can add or delete any service from this list. You
  can expand each service card to modify size and parameters for that service. You
  can also see the breakdown of cost for each service by expanding _Show
  calculation_, which is located in each service card.
- Select **Save** to see a graphical presentation of estimate
  on **My Estimate** page.

## My Estimate

This page provides the estimate for your modernized application. You can do the
following with this page:

- Clone the same or add new workload to your estimate.
- Increase or decrease the number of applications in a workload.
- Change the recommended AWS services by editing a workload.
- Add the cost of accessing Support to your estimate.
- Export to an excel file or share your estimate by using a unique URL.

_If you retrieve and modify a shared estimate, you must save and share the
modified version. The modifications aren't automatically added to your original
estimate._
