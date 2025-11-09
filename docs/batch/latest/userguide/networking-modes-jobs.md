# Networking modes for AWS Batch jobs

The following table describes the networking modes and typical usage for AWS Batch job types. See
the links in the "Job type" column for more details regarding considerations and behaviors.

| Job Type                                                                                     | Supported Network Mode(s) | Typical Usage                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [ECS-EC2 simple job](jobs.md "jobs.md")                                                      | `host`                    | Used for the highest scalable embarrassingly parallel batch workloads that<br>only require egress to vpc defined in Compute Environment.                                       |
| [ECS-EC2 multi-node parallel job](multi-node-parallel-jobs.md "multi-node-parallel-jobs.md") | `awsvpc`                  | Used for tightly-coupled, multi-host (node) distributed workloads modeled<br>as a single job with coordinated communications between task nodes.                               |
| [ECS-Fargate simple job](when-to-use-fargate.md "when-to-use-fargate.md")                    | `awsvpc`                  | True serverless for embarrassingly parallel batch workloads. Typically lowest TCO<br>and highest container isolation job model.                                                |
| [EKS-EC2 simple job](eks-jobs.md "eks-jobs.md")                                              | host and pod              | Used for highly scalable embarrassingly parallel batch workloads that only require<br>egress to vpc defined in Compute Environment. Default is host networking.                |
| [EKS-EC2 multi-node parallel job](mnp-eks-jobs.md "mnp-eks-jobs.md")                         | host and pod              | Used for tightly-coupled, multi-host (node) distributed workloads modeled as<br>a single job with coordinated communications between pod nodes. Default is host<br>networking. |
