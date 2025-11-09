# Use Amazon EMR cluster scaling to adjust

for changing workloads

You can adjust the number of Amazon EC2 instances available to an Amazon EMR cluster automatically
or manually in response to workloads that have varying demands. To use automatic scaling,
you have two options. You can enable Amazon EMR managed scaling or create a custom automatic
scaling policy. The following table describes the differences between the two
options.

|                               | Amazon EMR managed scaling                                                                                                                                                                    | Custom automatic scaling                                                                                                                                                                  |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scaling policies and rules    | No policy required. Amazon EMR manages the automatic scaling activity by<br>continuously evaluating cluster metrics and making optimized scaling<br>decisions.                                | You need to define and manage the automatic scaling policies and<br>rules, such as the specific conditions that trigger scaling activities,<br>evaluation periods, cooldown periods, etc. |
| Supported Amazon EMR releases | Amazon EMR version 5.30.0 and higher (except Amazon EMR version 6.0.0)                                                                                                                        | Amazon EMR version 4.0.0 and higher                                                                                                                                                       |
| Supported cluster composition | Instance groups or instance fleets                                                                                                                                                            | Instance groups only                                                                                                                                                                      |
| Scaling limits configuration  | Scaling limits are configured for the entire cluster.                                                                                                                                         | Scaling limits can only be configured for each instance group.                                                                                                                            |
| Metrics evaluation frequency  | Every 5 to 10 seconds<br>More frequent evaluation of metrics allows Amazon EMR to make more precise<br>scaling decisions.                                                                     | You can define the evaluation periods only in five-minute<br>increments.                                                                                                                  |
| Supported applications        | Only YARN applications are supported, such as Spark, Hadoop, Hive,<br>Flink. Amazon EMR managed scaling does not support applications that are not<br>based on YARN, such as Presto or HBase. | You can choose which applications are supported when defining the<br>automatic scaling rules.                                                                                             |

## Considerations

- An Amazon EMR cluster always comprises one or three primary nodes. Once you
  initially configure the cluster, you can only scale core and task nodes. You
  can't scale the number of primary nodes for the cluster.
- For instance groups, reconfiguration operations and resize operations occur
  consecutively and not concurrently. If you initiate a reconfiguration while an
  instance group is resizing, the reconfiguration starts once the instance group
  completes the resize in progress. Conversely, if you initiate a resize operation
  while an instance group is busy with reconfiguration, the resizing starts once the reconfiguration is complete.
