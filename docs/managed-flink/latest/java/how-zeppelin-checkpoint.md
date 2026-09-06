

# Enable checkpointing
<a name="how-zeppelin-checkpoint"></a>

You enable checkpointing by using environment settings. For information about checkpointing, see [Fault Tolerance](https://docs.aws.amazon.com/managed-flink/latest/java/how-fault.html) in the [Managed Service for Apache Flink Developer Guide](https://docs.aws.amazon.com/managed-flink/latest/java/).

## Set the checkpointing interval
<a name="how-zeppelin-checkpoint-interval"></a>

The following Scala code example sets your application's checkpoint interval to one minute:

```
// start a checkpoint every 1 minute
stenv.enableCheckpointing(60000)
```

The following Python code example sets your application's checkpoint interval to one minute:

```
st_env.get_config().get_configuration().set_string(
    "execution.checkpointing.interval", "1min"
)
```

## Set the checkpointing type
<a name="how-zeppelin-checkpoint-type"></a>

The following Scala code example sets your application's checkpoint mode to `EXACTLY_ONCE` (the default):

```
// set mode to exactly-once (this is the default)
stenv.getCheckpointConfig.setCheckpointingMode(CheckpointingMode.EXACTLY_ONCE)
```

The following Python code example sets your application's checkpoint mode to `EXACTLY_ONCE` (the default):

```
st_env.get_config().get_configuration().set_string(
    "execution.checkpointing.mode", "EXACTLY_ONCE"
)
```