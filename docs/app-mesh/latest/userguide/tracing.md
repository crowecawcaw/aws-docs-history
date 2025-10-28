# Tracing

###### Important

End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect "https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect").

###### Important

To fully implement tracing, you'll need to update your application.

To see all the available data from your chosen service, you'll have to instrument
your application using the applicable libraries.

## Monitor App Mesh with AWS X-Ray

###### Important

End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect "https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect").

AWS X-Ray is a service that provides tools that let you view, filter, and gain insights
into data collected from the requests your application serves. These insights help you
identify issues and opportunities to optimize your app. You can see detailed information
about requests and responses, and downstream calls your application makes to other AWS
services.

X-Ray integrates with App Mesh to manage your Envoy microservices. Trace data from Envoy is
sent to the X-Ray daemon running in your container.

Implement X-Ray in your application code using the [SDK](../../../xray/index.md "../../../xray/index.md") guide specific
to your language.

### Enable X-Ray tracing through App Mesh

- ###### Depending on the type of service:
  - **ECS -** In the Envoy proxy container
    definition, set the `ENABLE_ENVOY_XRAY_TRACING` environment
    variable to `1` and the `XRAY_DAEMON_PORT`
    environment variable to `2000`.
  - **EKS -** In the App Mesh Controller
    configuration, include `--set tracing.enabled=true` and
    `--set tracing.provider=x-ray`.

- In your X-Ray container, expose port `2000` and run as user
  `1337`.

### X-Ray examples

An Envoy container definition for Amazon ECS

```

      {
        "name": "envoy",
        "image": "840364872350.dkr.ecr.us-west-2.amazonaws.com/aws-appmesh-envoy:v1.15.1.0-prod",
        "essential": true,
        "environment": [
          {
            "name": "APPMESH_VIRTUAL_NODE_NAME",
            "value": "mesh/myMesh/virtualNode/myNode"
          },
          {
            **"name": "ENABLE\_ENVOY\_XRAY\_TRACING",
 "value": "1"**
           }
        ],
        "healthCheck": {
          "command": [
            "CMD-SHELL",
            "curl -s http://localhost:9901/server_info | cut -d' ' -f3 | grep -q live"
            ],
           "startPeriod": 10,
           "interval": 5,
           "timeout": 2,
           "retries": 3
      }

```

Updating the App Mesh controller for Amazon EKS

```

helm upgrade -i appmesh-controller eks/appmesh-controller \
--namespace appmesh-system \
--set region=${AWS_REGION} \
--set serviceAccount.create=false \
--set serviceAccount.name=appmesh-controller \
**--set tracing.enabled=true** \
**--set tracing.provider=x-ray**

```

### Walkthroughs for using the X-Ray

- [Monitor with AWS X-Ray](https://github.com/aws/aws-app-mesh-examples/tree/main/examples/apps/colorapp#monitor-with-aws-x-ray "https://github.com/aws/aws-app-mesh-examples/tree/main/examples/apps/colorapp#monitor-with-aws-x-ray")
- [App Mesh with Amazon EKS - Observability: X-Ray](https://github.com/aws/aws-app-mesh-examples/blob/main/walkthroughs/eks/o11y-xray.md "https://github.com/aws/aws-app-mesh-examples/blob/main/walkthroughs/eks/o11y-xray.md")
- [Distributed tracing with
  X-Ray](https://www.appmeshworkshop.com/x-ray/ "https://www.appmeshworkshop.com/x-ray/") in the AWS App Mesh [Workshop](https://www.appmeshworkshop.com/introduction/ "https://www.appmeshworkshop.com/introduction/")

### To learn more about AWS X-Ray

- [AWS X-Ray
  documentation](../../../xray/index.md "../../../xray/index.md")

### Troubleshooting AWS X-Ray with App Mesh

- [Unable to see AWS X-Ray traces for my applications.](troubleshoot-observability.md "troubleshoot-observability.md")

## Jaeger for App Mesh with Amazon EKS

Jaeger is an open source, end to end distributed tracing system. It can be used to profile
networks and for monitoring. Jaeger can also help you troubleshoot complex cloud native
applications.

To implement Jaeger into your application code, you can find the guide specific to your
language in the Jaeger documentation [tracing
libraries](https://www.jaegertracing.io/docs/1.21/client-libraries/ "https://www.jaegertracing.io/docs/1.21/client-libraries/").

### Installing Jaeger using Helm

1. Add the EKS repository to Helm:

```
helm repo add eks https://aws.github.io/eks-charts
```

2. Install App Mesh Jaeger

```

helm upgrade -i appmesh-jaeger eks/appmesh-jaeger \
--namespace appmesh-system

```

### Jaeger Example

The following is an example of creating a `PersistentVolumeClaim` for
Jaeger persistent storage.

```

helm upgrade -i appmesh-controller eks/appmesh-controller \
--namespace appmesh-system \
--set tracing.enabled=true \
--set tracing.provider=jaeger \
--set tracing.address=appmesh-jaeger.appmesh-system \
--set tracing.port=9411

```

### Walkthrough for using the Jaeger

- [App Mesh with EKS—Observability: Jaeger](https://github.com/aws/aws-app-mesh-examples/blob/main/walkthroughs/eks/o11y-jaeger.md "https://github.com/aws/aws-app-mesh-examples/blob/main/walkthroughs/eks/o11y-jaeger.md")

### To learn more about Jaeger

- [Jaeger Documentation](https://www.jaegertracing.io/ "https://www.jaegertracing.io/")

## Datadog for tracing

Datadog can be used for tracing as well as metrics. For more information and
installation instructions, find the guide specific to your application language in
the [Datadog
documentation](https://docs.datadoghq.com/tracing/setup_overview/ "https://docs.datadoghq.com/tracing/setup_overview/").
