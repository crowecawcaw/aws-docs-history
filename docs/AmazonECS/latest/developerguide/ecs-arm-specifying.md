# Specifying the ARM architecture in an Amazon ECS task definition

To use the ARM architecture, specify `ARM64` for the
`cpuArchitecture` task definition parameter.

In the following example, the ARM architecture is specified in a task definition. It's
in JSON format.

```
{
    **"runtimePlatform": {
 "operatingSystemFamily": "LINUX",
 "cpuArchitecture": "ARM64"
 },**
...
}
```

In the following example, a task definition for the ARM architecture displays "hello
world."

```
{
 "family": "arm64-testapp",
 "networkMode": "awsvpc",
 "containerDefinitions": [
    {
        "name": "arm-container",
        "image": "public.ecr.aws/docker/library/busybox:latest",
        "cpu": 100,
        "memory": 100,
        "essential": true,
        "command": [ "echo hello world" ],
        "entryPoint": [ "sh", "-c" ]
    }
 ],
 "requiresCompatibilities": [ "EC2" ],
 "cpu": "256",
 "memory": "512",
 "runtimePlatform": {
        "operatingSystemFamily": "LINUX",
        "cpuArchitecture": "ARM64"
  },
 "executionRoleArn": "arn:aws:iam::123456789012:role/ecsTaskExecutionRole"
}
```
