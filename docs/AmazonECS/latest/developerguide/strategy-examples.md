

# Example Amazon ECS task placement strategies
<a name="strategy-examples"></a>

You can specify task placement strategies with the following actions: [CreateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html), [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html), and [RunTask](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html).

**Topics**
+ [Distribute tasks evenly across Availability Zones](#even-az)
+ [Distribute tasks evenly across all instances](#even-instance)
+ [Bin pack tasks based on memory](#binpack)
+ [Place tasks randomly](#random)
+ [Distribute tasks evenly across Availability Zones and then distributes tasks evenly across the instances within each Availability Zone](#az-instance)
+ [Distribute tasks evenly across Availability Zones and then bin pack tasks based on memory within each Availability Zone](#az-memory)
+ [Distribute tasks evenly across instances and then bin pack tasks based on memory](#instance-memory)

## Distribute tasks evenly across Availability Zones
<a name="even-az"></a>

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
<a name="even-instance"></a>

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
<a name="binpack"></a>

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
<a name="random"></a>

The following strategy places tasks randomly.

```
"placementStrategy": [
    {
        "type": "random"
    }
]
```

## Distribute tasks evenly across Availability Zones and then distributes tasks evenly across the instances within each Availability Zone
<a name="az-instance"></a>

The following strategy distributes tasks evenly across Availability Zones and then distributes tasks evenly across the instances within each Availability Zone.

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
<a name="az-memory"></a>

The following strategy distributes tasks evenly across Availability Zones and then bin packs tasks based on memory within each Availability Zone.

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
<a name="instance-memory"></a>

The following strategy distributes tasks evenly across evenly across all instances and then bin packs tasks based on memory within each instance. 

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