# Logical expressions for AWS IoT FleetWise

campaigns

AWS IoT FleetWise uses a logical expression to recognize what data to collect as part of a
campaign. For more information about expressions, see [Expressions](../../../iotevents/latest/developerguide/iotevents-expressions.md "../../../iotevents/latest/developerguide/iotevents-expressions.md") in the _AWS IoT Events Developer Guide_.

The expression variable should be constructed to comply with the rules for the
type of data being collected. For telemetry system data, the expression variable
should be the signal's fully qualified name. For vision system data, the expression combines the
signal's fully qualified name with the path leading from the signal's data type to
one of its properties.

For example, if the signal catalog contains the following nodes:

```
{
    myVehicle.ADAS.Camera:
    type: sensor
    datatype: Vehicle.ADAS.CameraStruct
    description: "A camera sensor"

    myVehicle.ADAS.CameraStruct:
    type: struct
    description: "An obstacle detection camera output struct"
}
```

If the nodes follow the ROS 2 definition:

```
{
    Vehicle.ADAS.CameraStruct.msg:
    boolean obstaclesExists
    uint8[] image
    Obstacle[30] obstacles
}
{
    Vehicle.ADAS.Obstacle.msg:
    float32: probability
    uint8 o_type
    float32: distance
}
```

The following are all possible event expression variables:

```
{
...
    $variable.`myVehicle.ADAS.Camera.obstaclesExists`
    $variable.`myVehicle.ADAS.Camera.Obstacle[0].probability`
    $variable.`myVehicle.ADAS.Camera.Obstacle[1].probability`
...
    $variable.`myVehicle.ADAS.Camera.Obstacle[29].probability`
    $variable.`myVehicle.ADAS.Camera.Obstacle[0].o_type`
    $variable.`myVehicle.ADAS.Camera.Obstacle[1].o_type`
...
    $variable.`myVehicle.ADAS.Camera.Obstacle[29].o_type`
    $variable.`myVehicle.ADAS.Camera.Obstacle[0].distance`
    $variable.`myVehicle.ADAS.Camera.Obstacle[1].distance`
...
    $variable.`myVehicle.ADAS.Camera.Obstacle[29].distance`
}
```
