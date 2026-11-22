

# Example PromQL queries

Metric names contain periods, so put them in quotation marks inside braces, as in the following examples.

**Task CPU utilization (percent), by service**

```
100 * sum by ("@resource.aws.ecs.service.name") ({"ecs.task.cpu.utilized"})
    / sum by ("@resource.aws.ecs.service.name") ({"ecs.task.cpu.reserved"} > 0)
```

**Task memory utilization (percent), by service**

```
100 * sum by ("@resource.aws.ecs.service.name") ({"ecs.task.memory.utilized"})
    / sum by ("@resource.aws.ecs.service.name") ({"ecs.task.memory.reserved"} > 0)
```

**Running tasks, by service**

```
count by ("@resource.aws.ecs.service.name") (
  count by ("@resource.aws.ecs.service.name", "@resource.aws.ecs.task.id") ({"ecs.task.memory.utilized"}))
```

**Containers closest to their memory limit**

```
topk(10, 100 * max by ("@resource.container.name", "@resource.aws.ecs.task.id") ({"container.memory.usage"})
            / max by ("@resource.container.name", "@resource.aws.ecs.task.id") ({"container.memory.usage.limit"} > 0))
```