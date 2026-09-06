# Running mixed-architecture jobs (X86\_64 and ARM64)

A single Fargate compute environment and job queue can run both `X86_64` and
`ARM64` (AWS Graviton processor-based) jobs. Each job runs on Fargate capacity
that matches the CPU architecture declared in its job definition. Set the architecture with
`runtimePlatform.cpuArchitecture` in the job definition. You do not configure
architecture on the compute environment. Fargate provisions matching capacity for each job
automatically, so there's no instance type selection to manage.

To run mixed-architecture jobs, provide a container image that supports both architectures
(a multi-architecture image manifest), and register one job definition per architecture that
sets `runtimePlatform.cpuArchitecture` to `X86_64` or
`ARM64`. You can submit jobs for either job definition to the same job queue.

```
"runtimePlatform": {
  "operatingSystemFamily": "LINUX",
  "cpuArchitecture": "ARM64"
}
```

Amazon ECS Managed Instances offers the same per-job architecture selection with more
compute flexibility. For more information, see [Running mixed-architecture jobs (X86\_64 and ARM64)](ecs-managed-instances-multi-architecture.md "ecs-managed-instances-multi-architecture.md").
