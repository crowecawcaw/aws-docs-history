# Software and architecture patterns

| HCL_SUS3. Does your organization<br>monitor workload activity and remove or refactor components<br>that are no longer necessary? |
| -------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                  |

**Analyze demand on workloads
to identify components that can be removed or refactored. Then,
engage component owners and stakeholders to redesign clinical
workflows, and decrease workload infrastructure**

Some healthcare delivery systems and large independent software
vendors (ISV) have sprawling IT footprints with numerous siloed
systems. Identifying and
[removing
or refactoring components](../sustainability-pillar/remove-or-refactor-workload-components-with-low-or-no-use.md "../sustainability-pillar/remove-or-refactor-workload-components-with-low-or-no-use.md") with little or no use can
simplify workflows, decrease cost, and improve sustainability.
Cloud archives can minimize the cost of retaining data from
retired components.

| HCL_SUS4. How do you optimize the<br>impact of and applications and the equipment that run<br>them? |
| --------------------------------------------------------------------------------------------------- |
|                                                                                                     |

**Evaluate the overall impact
of applications, devices, and equipment**

As documented in the
[Sustainability
pillar of the AWS Well-Architected Framework](../sustainability-pillar/sustainability-pillar.md "../sustainability-pillar/sustainability-pillar.md"), it is
recommended to
[optimize
impact on customer devices and equipment](../sustainability-pillar/optimize-impact-on-customer-devices-and-equipment.md "../sustainability-pillar/optimize-impact-on-customer-devices-and-equipment.md").  For example,
as new features are released for a healthcare application, build
those features as backward compatible, minimizing the need for
new hardware.  Additionally, evaluate the potential impact of
new or upgraded hardware requirements to minimize the overall
impact when architecting new workloads or features.
