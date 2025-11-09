# EUCCOST05-BP02 Select the most cost-effective service for your EUC workload

Invest time into planning your EUC deployment. A persistent Amazon WorkSpaces, for example, is
a desktop as a service assigned to a named user. If this named user needs to run a certain
resource-intensive application only occasionally, it is not recommended to over-provision
the hardware resources for this WorkSpace to meet the application requirements, as these
resources will be under-utilized most of the time. Instead, consider deploying this
application to an Amazon WorkSpaces Applications fleet, where you have a more granular choice of instance types
and are charged for the actual usage only per hour or even per second.

The usage patterns and usage data collected help you govern your
application landscape and select the most appropriate service
and bundle and instance for each of your applications.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Amazon WorkSpaces offers a variety of different bundles to
choose from, and each one has a different hardware
configuration (vCPU and RAM), some of which supporting a GPU.
In total, you have the choice between five non-GPU bundles and
four GPU-enabled bundles.

With Amazon WorkSpaces Applications, you have a more granular choice from many non-GPU and GPU-enabled
instance types. Review your application workloads and match them to the most appropriate
service and bundle or instance type to avoid over-provisioning of resources. 

Consider Amazon WorkSpaces Applications with appropriate instance types for workloads that can be
characterized as CPU-intensive or RAM-intensive or requires a GPU and that typically shows
a lower utilization.

In a typical EUC environment, users are often using certain applications permanently
over the course of a day and other applications only occasionally. For a CPU-intensive or
RAM-intensive workload, or for applications requiring a GPU, Amazon WorkSpaces Applications can be the more
cost-effective solution, especially if the application is only used occasionally. If you
have any usage data (usage patterns) on these applications, we recommend you review these
and calculate a cost estimate of the usage on Amazon WorkSpaces Applicationsusing these usage patterns.
This helps you understand if provisioning the application on Amazon WorkSpaces Applications will be more
cost-effective than provisioning it on Amazon WorkSpaces if choosing a more powerful bundle.

Even the combined usage of a less powerful WorkSpaces instance for standard applications
and WorkSpaces Applications for more demanding workloads can come at a lower cost compared to a more
powerful WorkSpaces bundle as the only service. If there isn't enough data to make a decisive
decision, identify a mechanism to capture this data in your existing environment or
perform a proof of concept (PoC) to capture this data.

If your users only need to access web-based applications,
consider using Amazon WorkSpaces Secure Browser. Examples of
web-based applications are Salesforce, SAP-Fiori, Confluence,
or your intranet websites. WorkSpaces Secure Browser
service is a low cost, fully-managed, Linux-based service
designed to provide secure browser access to internal websites
SaaS applications for up to 200 streaming hours. 

If you need a persistent environment with users who require a high degree of
flexibility in customizing their environment and installing their own applications,
Amazon WorkSpaces Personal is your best option. As opposed to Amazon WorkSpaces Personal, Amazon WorkSpaces Applications is
not designed to allow users to install their own software due to the non-persistent nature
of the WorkSpaces Applications fleet.
