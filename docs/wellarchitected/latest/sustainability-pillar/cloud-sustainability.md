# Cloud sustainability

The discipline of sustainability addresses the long-term
environmental, economic, and societal impact of your business
activities. The [United
Nations World Commission on Environment and Development](https://www.un.org/en/academic-impact/sustainability "https://www.un.org/en/academic-impact/sustainability")
defines sustainable development as “development that meets
the needs of the present without compromising the ability of future
generations to meet their own needs.” Your business or organization
can have negative environmental impacts like direct or indirect
carbon emissions, unrecyclable waste, and damage to shared resources
like clean water.

When building cloud workloads, the practice of sustainability is
understanding the impacts of the services used, quantifying impacts
through the entire workload lifecycle, and applying design
principles and best practices to reduce these impacts. This document
focuses on environmental impacts, especially energy consumption and
efficiency, since they are important levers for architects to inform
direct action to reduce resource usage.

When focusing on environmental impacts, you should understand how
these impacts are typically accounted for and the follow-on impacts
to your organization’s own emissions accounting. The
[Greenhouse Gas
Protocol](https://ghgprotocol.org/ "https://ghgprotocol.org/") organizes carbon emissions into the following
scopes, along with relevant emission examples within each scope for
a cloud provider such as AWS:

- **Scope 1:** All direct emissions from the activities of an
  organization or under its control. For example, fuel combustion by data center backup
  generators.
- **Scope 2:** Indirect emissions from electricity purchased and
  used to power data centers and other facilities. For example, emissions from commercial
  power generation.
- **Scope 3:** All other indirect emissions from activities of an
  organization from sources it doesn’t control. AWS examples include emissions related to
  data center construction, and the manufacture and transportation of IT hardware deployed in
  data centers.

From an AWS customer perspective, emissions from your workloads
running on AWS are accounted for as indirect emissions, and part of
your Scope 3 emissions. Each workload deployed generates a fraction
of the total AWS emissions from each of the previous scopes. The
actual amount varies per workload and depends on several factors
including the AWS services used, the energy consumed by those
services, the carbon intensity of the electric grids serving the AWS
data centers where they run, and the AWS procurement of renewable
energy.

This document first describes a shared responsibility model for
environmental sustainability, and then provides architectural best
practices so you can minimize the impact of your workloads by
reducing the total resources required for them to run in AWS data
centers.
