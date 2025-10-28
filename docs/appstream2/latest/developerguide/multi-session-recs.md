# Multi-Session Recommendations

When deciding the maximum number of user sessions on an instance in a multi-session
environment, you should consider several factors to ensure optimal performance and
streaming experience. The following are recommendations for you to determine the optimum
number of user sessions on an instance:

- _Evaluate resource requirements_: Understand the resource
  requirements of the applications being used within the sessions. Consider
  factors such as CPU, memory, disk I/O, and network bandwidth. This evaluation
  will help determine the amount of resources each user session typically
  requires.
- _Consider instance specifications_: Take into account the
  specifications of the instance, including the number of CPUs, available memory,
  and GPU specifications. Instances with higher specifications can handle a larger
  number of user sessions. For more information on different instance types
  supported by AppStream 2.0 and pricing, see [Amazon AppStream 2.0
  pricing](https://aws.amazon.com/appstream2/pricing/ "https://aws.amazon.com/appstream2/pricing/").
- _Performance testing_: Conduct performance testing on the
  applications and workload expected to run within the user sessions. Measure
  resource utilization, response times, and overall system performance. Use this
  data to assess the impact of concurrent user sessions on performance, and
  determine the optimal session-to-instance ratio. You can run these assessments
  across different instance types offered by AppStream 2.0 to find the optimal instance
  type or size for your end users. For more information on different instance
  types offered by AppStream 2.0, see [AppStream 2.0 Instance Families](instance-types.md "instance-types.md").
- _Monitor resource utilization_: Continuously monitor the
  resource utilization of the instance during normal usage. Observe CPU, memory,
  and disk utilization. Ensure that the resource utilization remains within
  acceptable limits to avoid performance degradation. For a multi-session
  environment, you can view these metrics on AppStream 2.0 and the CloudWatch console. For more
  information, see [Monitoring Amazon AppStream 2.0 Resources](monitoring.md "monitoring.md").
- _Consider user behavior patterns_: Analyze user behavior
  patterns to understand peak usage periods and potential concurrent usage. Some
  users might have intermittent or sporadic usage patterns, while others might
  have consistent usage throughout the day. Account for these patterns when
  determining the maximum number of user sessions to avoid resource contention
  during peak periods.

AppStream 2.0 enables you to configure a maximum of 50 user sessions per instance,
regardless of the instance type or size that you choose. However, this is just
an upper limit, and not a recommended limit. The following is an example table
to help you determine the maximum number of user sessions on an instance in a
multi-session fleet. The recommended maximum number of users listed in the table
is based on general guidelines and assumptions. Testing with the real-life
workload is crucial, since actual performance can vary, depending on the
workload's individual characteristics, the application's resource requirements,
and user behavior.

| Recommendations based on workload types                                           | End User Category    | Workload Type                                                                             | Example Users                                                                                                                          | Use Cases                                                                                             | Recommended Configuration(s) |
| --------------------------------------------------------------------------------- | -------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------- |
| End users who conduct a single task and use minimal applications                  | Light                | Task workers, Front desk users                                                            | Data entry applications, Text editing, Bastion host                                                                                    | 4 users per vCPU on Stream.standard.xlarge/2xlarge or Stream.compute.xlarge+ or Stream.memory.xlarge+ |
| End users who conduct a single task and use minimal applications                  | Light to Medium      | Task workers, Front desk users, Contact center employees                                  | Data entry applications, Text editing, Bastion host, Chat, Email, Messaging apps                                                       | 2 users per vCPU on Stream.standard.xlarge/2xlarge or Stream.compute.xlarge+ or Stream.memory.xlarge+ |
| End users who create complex spreadsheets, presentations, and large documents     | Medium               | Task workers, Contact center employees, Business analysts                                 | Data entry applications, Chat, Email, Messaging apps, Productivity apps                                                                | 2 users per vCPU on Stream.memory.xlarge+ or Stream.compute.xlarge+                                   |
| End users with high performance workloads                                         | Medium to Heavy      | Knowledge workers, Software developers, Business intelligence analysts                    | Software Scripting                                                                                                                     | 1 user per vCPU on Stream.memory.xlarge+ or Stream.compute.xlarge+                                    |
| End users with high performance workloads                                         | Heavy                | Knowledge workers, Software developers, Data scientists                                   | Screen sharing, Data analytics, Audio conferencing                                                                                     | 1 user per 2 vCPUs on Stream.memory.xlarge+ or Stream.compute.xlarge+                                 |
| End users with workloads that require graphics and heavy compute/memory resources | Heavy to Accelerated | Graphics/Architecture designers, CAD/CAM users                                            | Audio conferencing, Graphics-intensive applications, such as remote graphics workstations                                              | 1 user per 2 vCPUs Graphics.g4dn.\*                                                                   |
| End users with workloads that require graphics and heavy compute/memory resources | Accelerated          | Video editors, Gamers and game developers, Data miners, GIS data engineers, AI scientists | Audio conferencing, Video transcoding and 3D rendering, Photo-realistic design, Graphics workstations, ML model training, ML inference | 1 user per 2 vCPUs Graphics.G5.\*                                                                     |
