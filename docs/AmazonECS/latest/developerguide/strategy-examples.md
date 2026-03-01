# Example Amazon ECS task placement strategies

You can specify task placement strategies with the following actions: [CreateService](../APIReference/API_CreateService.md "../APIReference/API_CreateService.md"), [UpdateService](../APIReference/API_UpdateService.md "../APIReference/API_UpdateService.md"), and [RunTask](../APIReference/API_RunTask.md "../APIReference/API_RunTask.md").

###### Examples

- [Distribute tasks evenly across Availability Zones](#even-az "#even-az")
- [Distribute tasks evenly across all instances](#even-instance "#even-instance")
- [Bin pack tasks based on memory](#binpack "#binpack")
- [Place tasks randomly](#random "#random")
- [Distribute tasks evenly across Availability Zones and then distributes tasks evenly across the instances within each Availability Zone](#az-instance "#az-instance")
- [Distribute tasks evenly across Availability Zones and then bin pack tasks based on memory within each Availability Zone](#az-memory "#az-memory")
- [Distribute tasks evenly across instances and then bin pack tasks based on memory](#instance-memory "#instance-memory")

## Distribute tasks evenly across Availability Zones

The following strategy distributes tasks evenly across Availability Zones.

```
"placementStrategy": [
    {
        "field": "attribute:ecs.availability-zone",
        "type": "spread"
    }
]
```

## Distribute tasks evenly across all instances

The following strategy distributes tasks evenly across all instances.

```
"placementStrategy": [
    {
        "field": "instanceId",
        "type": "spread"
    }
]
```

## Bin pack tasks based on memory

The following strategy bin packs tasks based on memory.

```
"placementStrategy": [
    {
        "field": "memory",
        "type": "binpack"
    }
]
```

## Place tasks randomly

The following strategy places tasks randomly.

```
"placementStrategy": [
    {
        "type": "random"
    }
]
```

## Distribute tasks evenly across Availability Zones and then distributes tasks evenly across the instances within each Availability Zone

The following strategy distributes tasks evenly across Availability Zones and then
distributes tasks evenly across the instances within each Availability Zone.

```
"placementStrategy": [
    {
        "field": "attribute:ecs.availability-zone",
        "type": "spread"
    },
    {
        "field": "instanceId",
        "type": "spread"
    }
]
```

## Distribute tasks evenly across Availability Zones and then bin pack tasks based on memory within each Availability Zone

The following strategy distributes tasks evenly across Availability Zones and then
bin packs tasks based on memory within each Availability Zone.

```
"placementStrategy": [
    {
        "field": "attribute:ecs.availability-zone",
        "type": "spread"
    },
    {
        "field": "memory",
        "type": "binpack"
    }
]
```

## Distribute tasks evenly across instances and then bin pack tasks based on memory

The following strategy distributes tasks evenly across evenly across all instances
and then bin packs tasks based on memory within each instance.

```
"placementStrategy": [
    {
        "field": "instanceId",
        "type": "spread"
    },
    {
        "field": "memory",
        "type": "binpack"
    }
]
```
