# Foundations

| CONTAINER_BUILD_REL_01: How do you limit the amount of CPU and<br>memory a container consumes? |
| ---------------------------------------------------------------------------------------------- |
|                                                                                                |

**Use RAM and CPU limits**

By default, a running container will use the full RAM and CPU
of the host system. This can lead to performance bottlenecks
on the host and put your workload in a degraded state.

Setting RAM and CPU limits on your running container will
improve the availability of the host system and the workload.
In Amazon ECS, update the CPU and memory parameters in the
task definition to limit the CPU and RAM a container will
consume.

```

          {
  "containerDefinitions": [
      {
        "command": ["/bin/sh -c 'echo HELLO WORLD! >> /usr/share/nginx/html/index.html'"],
        "entrypoint": ["sh", "-c"],
        "image": "nginx:1.20.1-alpine",
        "name": "hello-world",
        "portMapping": [
            {
              "containerPort": 80,
              "hostPort": 80,
              "protocol": "tcp"
            }
        ]
      }
  ],
  "CPU": "256",
  "memory": "512",
  "executionRoleArn": "arn:aws:iam::012345678910:role/ecsTaskExecutionRole",
  "family": "fargate-task-definition",
  "networkMode": "awsvpc",
  "runtimePlatform": {"operatingSystemFamily": "LINUX" },
  "requiresCompatibilities": [ "FARGATE" ]
  }

```

If you are going to run your container workload on Amazon EKS,
update the CPU and memory values in the resources section of
your YAML file. The requests and limits keys are used to
define how much memory and CPU a specific container will
consume when running.

```

         ---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
  labels:
    app: web
spec:
  replicas: 1
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: app
        ports:
        - containerPort: 80
        image: nginx:1.20.1-alpine
        resources:
          requests:
            memory: "64Mi"
            CPU: "250m"
          limits:
            memory: "128Mi"
            CPU: "500m"

```
