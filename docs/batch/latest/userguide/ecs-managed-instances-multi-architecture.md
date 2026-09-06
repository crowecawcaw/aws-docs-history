# Running mixed-architecture jobs (X86\_64 and ARM64)

A single Amazon ECS Managed Instances compute environment and job queue can run both
`X86_64` and `ARM64` (AWS Graviton processor-based) jobs. Each job runs
on capacity that matches the CPU architecture declared in its job definition. Set the
architecture with `runtimePlatform.cpuArchitecture` in the job definition. You do
not configure architecture on the compute environment.

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

Then set up the compute environment in one of the following ways:

- Omit `instanceRequirements` to make all instance types eligible.
- Specify `allowedInstanceTypes` that cover every architecture your jobs
  use.

Do not specify instance types

Omit the `instanceRequirements` field from
`managedInstancesProvider.instanceLaunchTemplate` (the setting that restricts
which instance types the compute environment can use). All instance types are
eligible, and Amazon ECS selects capacity that matches each job's
`runtimePlatform.cpuArchitecture`. An `X86_64` job launches on an
x86 instance, and an `ARM64` job launches on an AWS Graviton instance from the same
compute environment.

Specify instance types that cover the required architectures

If you set `instanceRequirements.allowedInstanceTypes`, include instance
types for every architecture your jobs declare. Amazon ECS infers the architecture from the
instance types you allow. The allowed instance types must satisfy each job's
`runtimePlatform.cpuArchitecture`. For example, to run both architectures,
include:

- x86 families, such as `m5` and `c5`
- AWS Graviton families, such as `m7g` and `c7g`

###### Job fails if no matching instance type is available

If the allowed instance types do not include any type that matches a job's declared
architecture, the job fails with the following reason:

`ResourceInitializationError: No available instance types were able to satisfy the
 task and placement constraints.`

For example, if `allowedInstanceTypes` lists only x86 families and you submit
an `ARM64` job, the job fails with this error. To resolve this issue, add an AWS
Graviton instance family to `allowedInstanceTypes`. Or, remove
`instanceRequirements` to allow all instance types.
