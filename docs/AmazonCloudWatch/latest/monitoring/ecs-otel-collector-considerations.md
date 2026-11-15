

# Considerations
<a name="ecs-otel-collector-considerations"></a>
+ **Network metrics with `awsvpc` networking** Containers in a task that uses the `awsvpc` network mode share one network interface. Each container's network metrics report the traffic of the whole task, so don't add them up across the containers in a task. Use the task-level network metrics instead.
+ **Launch type filters** For tasks on Amazon ECS Managed Instances, `aws.ecs.launchtype` isn't set. To filter by launch type, use `aws.ecs.task.launch_type`.
+ **Image tags** For images pulled by digest, `container.image.tag` is `latest`.
+ **Cost** Ingested volume is roughly the number of tasks × (28 \+ 26 × containers per task) × collections per month × bytes per data point. The collection interval and the number of resource attributes that you keep have the largest effect. To collect only task-level metrics, add a `filter` processor that keeps metrics whose names start with `ecs.task.`.
+ **Application telemetry** To also receive OTLP data from your application in the same collector, add an `otlp` receiver bound to `127.0.0.1`. Containers in an `awsvpc` task share `localhost`. Don't bind the receiver to `0.0.0.0`, and don't map its ports to the host.