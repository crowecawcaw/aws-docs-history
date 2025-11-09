# Foundations

Foundational requirements are those whose scope extends beyond a
single workload or project. Before architecting any system,
foundational requirements that influence reliability should be in
place. For example, you must have sufficient network bandwidth
to your data center.

With AWS, most of these foundational requirements are already
incorporated or can be addressed as needed. The cloud is designed
to be nearly limitless, so it’s the responsibility of AWS to
satisfy the requirement for sufficient networking and compute
capacity, permitting you to change resource size and allocations
on demand.

The following questions focus on these considerations for reliability. (For a list of
reliability questions and best practices, see the [Appendix](a-reliability.md "a-reliability.md").).

| REL 1:  How do you manage Service Quotas and constraints?                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| For cloud-based workload architectures, there are Service Quotas (which are<br>also referred to as service limits). These quotas exist to prevent accidentally<br>provisioning more resources than you need and to limit request rates on API<br>operations so as to protect services from abuse. There are also resource<br>constraints, for example, the rate that you can push bits down a fiber-optic<br>cable, or the amount of storage on a physical disk. |

| REL 2:  How do you plan your network topology?                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Workloads often exist in multiple environments. These include multiple cloud<br>environments (both publicly accessible and private) and possibly your existing<br>data center infrastructure. Plans must include network considerations such as<br>intra<br>• and inter-system connectivity, public IP address management, private IP<br>address management, and domain name resolution. |
