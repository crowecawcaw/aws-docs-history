# EUCCOST05-BP01 Gather usage data and hardware requirements in your existing environment

Before selecting a service for your EUC workload, gather usage
data in your existing EUC environment. Collect data in different
areas, like usage patterns and resource utilization. Usage
patterns portray how intensively your applications are being
used (for example, hours per day and days per week). Resource
utilization details how efficiently your compute resources are
being used by these applications (like CPU, RAM, GPU, disk
space, and disk IO). Both areas help you select the optimal
service for a given application or set of applications. You can
gather this data using OS or third-party tools.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

If you use a desktop virtualization Environment, your VDI
solution may include reporting tools that can provide you with
the required data. Tools like
[Citrix
Director](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/director.html "https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/director.html") or

[VMware
vRealize Operations Manager](https://docs.vmware.com/en/vRealize-Operations/index.html "https://docs.vmware.com/en/vRealize-Operations/index.html") can be used for this.

Alternatively, you may use scripting to wrap application launches and log the usage
of applications using these scripts in a file or database that you can use later to
analyze the data. Your OS may include tools to visualize and log the resource utilization
of your applications.

For example, Windows offers the [Windows Performance Monitor](https://techcommunity.microsoft.com/t5/ask-the-performance-team/windows-performance-monitor-overview/ba-p/375481 "https://techcommunity.microsoft.com/t5/ask-the-performance-team/windows-performance-monitor-overview/ba-p/375481") to capture performance metrics over an elapsed
period of time.

If you do not have any tools available to gather usage patterns, you can conduct a
survey with a representative selection of users to understand their usage of your
applications.
