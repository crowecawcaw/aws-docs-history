Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Perform an interactive analysis of streaming data

You use a serverless notebook powered by Apache Zeppelin to interact with your streaming data.
Your notebook can have multiple notes, and each note can have one or more paragraphs where you can write your code.

The following example SQL query shows how to retrieve data from a data source:

```
%flink.ssql(type=update)
select * from stock;
```

For more examples of Flink Streaming SQL queries, see [Examples and tutorials for Studio notebooks in Managed Service for Apache Flink](how-zeppelin-examples.md "how-zeppelin-examples.md") following, and
[Queries](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/table/sql/queries/overview/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/table/sql/queries/overview/")
in the Apache Flink documentation.

You can use Flink SQL queries in the Studio notebook to query streaming data. You may also use Python (Table API)
and Scala (Table and Datastream APIs) to write programs to query your streaming data interactively.
You can view the results of your queries or programs, update them in seconds, and re-run them to view updated results.

## Flink interpreters

You specify which language Managed Service for Apache Flink uses to run your application by using an _interpreter_. You can
use the following interpreters with Managed Service for Apache Flink:

| Name            | Class                     | Description                                                                                                                           |
| --------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| %flink          | FlinkInterpreter          | Creates ExecutionEnvironment/StreamExecutionEnvironment/BatchTableEnvironment/StreamTableEnvironment and provides a Scala environment |
| %flink.pyflink  | PyFlinkInterpreter        | Provides a python environment                                                                                                         |
| %flink.ipyflink | IPyFlinkInterpreter       | Provides an ipython environment                                                                                                       |
| %flink.ssql     | FlinkStreamSqlInterpreter | Provides a stream sql environment                                                                                                     |
| %flink.bsql     | FlinkBatchSqlInterpreter  | Provides a batch sql environment                                                                                                      |

For more information about Flink interpreters, see
[Flink interpreter for Apache Zeppelin](https://zeppelin.apache.org/docs/0.9.0/interpreter/flink.html "https://zeppelin.apache.org/docs/0.9.0/interpreter/flink.html").

If you are using `%flink.pyflink` or `%flink.ipyflink` as your interpreters, you will need to use the `ZeppelinContext` to visualize the results within the notebook.

For more PyFlink specific examples, see [Query your data streams interactively using Managed Service for Apache Flink Studio and Python](https://aws.amazon.com/blogs/big-data/query-your-data-streams-interactively-using-kinesis-data-analytics-studio-and-python/ "https://aws.amazon.com/blogs/big-data/query-your-data-streams-interactively-using-kinesis-data-analytics-studio-and-python/").

## Apache Flink table environment variables

Apache Zeppelin provides access to table environment resources using environment variables.

You access Scala
table environment resources with the following variables:

| Variable | Resource                                   |
| -------- | ------------------------------------------ |
| `senv`   | `StreamExecutionEnvironment`               |
| `stenv`  | `StreamTableEnvironment for blink planner` |

You access Python
table environment resources with the following variables:

| Variable | Resource                                   |
| -------- | ------------------------------------------ |
| `s_env`  | `StreamExecutionEnvironment`               |
| `st_env` | `StreamTableEnvironment for blink planner` |

For more information about using table environments, see [Concepts and Common API](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/table/common/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/table/common/") in the Apache Flink documentation.
