Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Use a Studio notebook with Managed Service for Apache Flink

Studio notebooks for Managed Service for Apache Flink allows you to interactively query data streams in real time, and easily
build and run stream processing applications using standard SQL, Python, and Scala. With a few clicks
in the AWS Management console, you can launch a serverless notebook to
query data streams and get results in seconds.

A notebook is a web-based development environment. With notebooks, you get a simple
interactive development experience combined with the advanced capabilities provided by
Apache Flink. Studio notebooks uses notebooks powered by [Apache Zeppelin](https://zeppelin.apache.org/ "https://zeppelin.apache.org/"), and uses [Apache Flink](https://flink.apache.org/ "https://flink.apache.org/") as the stream processing engine.
Studio notebooks seamlessly combines these technologies to make advanced analytics on data
streams accessible to developers of all skill sets.

Apache Zeppelin provides your Studio notebooks with a complete suite of analytics tools, including the following:

- Data Visualization
- Exporting data to files
- Controlling the output format for easier analysis
  To get started using Managed Service for Apache Flink and Apache Zeppelin, see [Tutorial: Create a Studio notebook in
  Managed Service for Apache Flink](example-notebook.md "example-notebook.md"). For more
  information about Apache Zeppelin, see the [Apache Zeppelin documentation](http://zeppelin.apache.org "http://zeppelin.apache.org").

With a notebook, you model queries using the
Apache Flink
[Table API & SQL](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/table/overview/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/table/overview/")
in SQL, Python, or Scala, or
[DataStream API](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/datastream/overview/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/datastream/overview/")
in Scala. With
a few clicks, you can then
promote the Studio notebook to a continuously-running, non-interactive, Managed Service for Apache Flink stream-processing application
for your production workloads.

###### This topic contains the following sections:

- [Use the correct Studio notebook
  Runtime version](studio-notebook-versions.md "studio-notebook-versions.md")
- [Create a
  Studio notebook](how-zeppelin-creating.md "how-zeppelin-creating.md")
- [Perform an interactive analysis of streaming data](how-zeppelin-interactive.md "how-zeppelin-interactive.md")
- [Deploy as an application with durable state](how-notebook-durable.md "how-notebook-durable.md")
- [IAM permissions](how-zeppelin-iam.md "how-zeppelin-iam.md")
- [Use connectors and dependencies](how-zeppelin-connectors.md "how-zeppelin-connectors.md")
- [User-defined functions](how-zeppelin-udf.md "how-zeppelin-udf.md")
- [Enable checkpointing](how-zeppelin-checkpoint.md "how-zeppelin-checkpoint.md")
- [Upgrade Studio Runtime](upgrading-studio-runtime.md "upgrading-studio-runtime.md")
- [Work with AWS Glue](how-zeppelin-glue.md "how-zeppelin-glue.md")
- [Examples and tutorials for Studio notebooks in Managed Service for Apache Flink](how-zeppelin-examples.md "how-zeppelin-examples.md")
- [Troubleshoot Studio notebooks for Managed Service for Apache Flink](how-zeppelin-troubleshooting.md "how-zeppelin-troubleshooting.md")
- [Create custom IAM policies for Managed Service for Apache Flink
  Studio notebooks](how-zeppelin-appendix-iam.md "how-zeppelin-appendix-iam.md")
