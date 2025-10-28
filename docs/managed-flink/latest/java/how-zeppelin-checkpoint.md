Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Enable checkpointing

You enable checkpointing by using environment settings. For information about checkpointing, see
[Fault Tolerance](how-fault.md "how-fault.md")
in the [Managed Service for Apache Flink Developer Guide](../java.md "../java.md").

## Set the checkpointing interval

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
