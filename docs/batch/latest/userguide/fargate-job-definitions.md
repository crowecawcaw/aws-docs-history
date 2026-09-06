

# Job definitions on Fargate
<a name="fargate-job-definitions"></a>

AWS Batch jobs on AWS Fargate don't support all of the job definition parameters that are available. Some parameters are not supported at all, and others behave differently for Fargate jobs.

The following list describes job definition parameters that are not valid or otherwise restricted in Fargate jobs.

`platformCapabilities`  
Must be specified as `FARGATE`.  

```
"platformCapabilities": [ "FARGATE" ]
```

`type`  
Must be specified as `container`.  

```
"type": "container"
```

Parameters in `containerProperties`    
`executionRoleArn`  
Must be specified for jobs running on Fargate resources. For more information, see [IAM Roles for Tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.  

```
"executionRoleArn": "arn:aws:iam::123456789012:role/ecsTaskExecutionRole"
```  
`fargatePlatformConfiguration`  
(Optional, only for Fargate job definitions). Specifies the Fargate platform version, or `LATEST` for a recent platform version. Possible values for `platformVersion` are `1.3.0`, `1.4.0`, and `LATEST` (default).  

```
"fargatePlatformConfiguration": { "platformVersion": "1.4.0" }
```  
`runtimePlatform`  
(Optional) Specifies the operating system family and CPU architecture for the job. This parameter applies to both Fargate and Amazon ECS Managed Instances job definitions. The valid value for `operatingSystemFamily` is `LINUX` (default). The valid values for `cpuArchitecture` are `X86_64` (default) and `ARM64` (AWS Graviton).  
You select the architecture per job in the job definition, not on the compute environment. A single Fargate compute environment and job queue can run both `X86_64` and `ARM64` jobs. Fargate provisions capacity that matches each job's `cpuArchitecture`. Provide a container image that supports the declared architecture, or use a multi-architecture image manifest to support both. For more information, see [Running mixed-architecture jobs (X86\_64 and ARM64)](fargate-multi-architecture.md).  

```
"runtimePlatform": {
  "operatingSystemFamily": "LINUX",
  "cpuArchitecture": "ARM64"
}
```

`instanceType``ulimits`  
Not applicable for jobs running on Fargate resources.

`memory``vcpus`  
These settings must be specified in `resourceRequirements`

`privileged`  
Either don't specify this parameter, or specify `false`.  

```
"privileged": false
```

`resourceRequirements`  
Both memory and vCPU requirements must be specified using [supported values](job_definition_parameters.md#ContainerProperties-resourceRequirements-Fargate-memory-vcpu). GPU resources aren't supported for jobs that run on Fargate resources.  
If you use GuardDuty Runtime Monitoring, there is a slight memory overhead for the GuardDuty security agent. Therefore the memory limit must include the size of the GuardDuty security agent. For information about the GuardDuty security agent memory limits, see [CPU and memory limits](https://docs.aws.amazon.com/guardduty/latest/ug/prereq-runtime-monitoring-ecs-support.html#ecs-runtime-agent-cpu-memory-limits) in the *GuardDuty User Guide*. For information about the best practices, see [How do I remediate out of memory errors on my Fargate tasks after enabling Runtime Monitoring](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-troubleshooting.html#memory-error) in the *Amazon ECS Developer Guide*.  

```
"resourceRequirements": [
  {"type": "MEMORY", "value": "512"},
  {"type": "VCPU",   "value": "0.25"}
]
```

Parameters in `linuxParameters`    
`devices``maxSwap``sharedMemorySize``swappiness``tmpfs`  
Not applicable for jobs that run on Fargate resources.

Parameters in `logConfiguration`    
`logDriver`  
Only `awslogs` and `splunk` are supported. For more information, see [Use the awslogs log driver](using_awslogs.md).

Members in `networkConfiguration`    
`assignPublicIp`  
If the private subnet doesn't have a NAT gateway attached to send traffic to the Internet, `[assignPublicIp](https://docs.aws.amazon.com/batch/latest/APIReference/API_NetworkConfiguration.html#Batch-Type-NetworkConfiguration-assignPublicIp)` must be "`ENABLED`". For more information, see [AWS Batch IAM execution role](execution-IAM-role.md).