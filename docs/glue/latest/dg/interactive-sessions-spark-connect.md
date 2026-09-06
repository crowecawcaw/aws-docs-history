

# Using Spark Connect with AWS Glue interactive sessions
<a name="interactive-sessions-spark-connect"></a>

 [Apache Spark Connect](https://spark.apache.org/spark-connect/) introduces a decoupled client-server architecture that separates your application from the Spark driver process. With Spark Connect, AWS Glue interactive sessions benefit from a lightweight client that starts faster, uses fewer local resources, and provides native compatibility with the PySpark DataFrame and SQL APIs. You can use AWS Glue interactive sessions from your preferred notebook tooling or IDE. 

 Spark Connect is supported natively in AWS Glue version 5.1 and above. You can connect to a AWS Glue interactive session directly from an environment that supports the PySpark `remote()` API. 

## Comparing session types: Livy and Spark Connect
<a name="is-spark-connect-comparison"></a>

 AWS Glue interactive sessions support two session types. The following table compares Livy-based sessions and Spark Connect sessions. 


| Feature | Livy | Spark Connect | 
| --- | --- | --- | 
| Protocol | REST | gRPC (to send logical execution plans) \+ Apache Arrow (to stream results) | 
| Connection method | Statement APIs (`RunStatement`, `CancelStatement`, `GetStatement`, `ListStatements`) | Direct connection through endpoint URL using PySpark `remote()` API | 
| Client requirement | `aws-glue-sessions` package for kernels or AWS SDK | PySpark with Spark Connect support | 
| IDE support | Through Jupyter with SparkMagic kernel | Notebooks on SageMaker Unified Studio or IDEs with Python interpreters like VS Code, PyCharm, and others | 

## When to use Spark Connect
<a name="is-spark-connect-use-cases"></a>

 Use Spark Connect sessions when you need direct, programmatic access to a AWS Glue interactive session from your development environment. The following are common use cases: 
+ **Notebooks in SageMaker Unified Studio** – Connect to AWS Glue interactive sessions directly from your notebook environment for interactive data exploration.
+ **IDEs such as VS Code or PyCharm** – Use PySpark from your preferred IDE to develop and test Spark applications against a remote AWS Glue cluster.
+ **Python scripts and applications** – Access AWS Glue interactive sessions programmatically from a Python application that uses the PySpark `remote()` API.

## Region availability
<a name="is-spark-connect-regions"></a>

AWS Glue interactive sessions with Spark Connect is available in the following AWS Regions:
+ Asia Pacific (Mumbai)
+ Asia Pacific (Seoul)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)
+ Asia Pacific (Tokyo)
+ Canada (Central)
+ Europe (Frankfurt)
+ Europe (Ireland)
+ Europe (London)
+ Europe (Paris)
+ Europe (Stockholm)
+ South America (São Paulo)
+ US East (Ohio)
+ US East (N. Virginia)
+ US West (Oregon)

## Considerations and limitations
<a name="is-spark-connect-limitations"></a>

 Consider the following when you use Spark Connect with AWS Glue interactive sessions: 
+ Spark Connect is available for AWS Glue interactive sessions running AWS Glue version 5.1 and later.
+ Statement APIs (`RunStatement`, `CancelStatement`, `GetStatement`, and `ListStatements`) are not supported for Spark Connect sessions. You interact with the session directly through the PySpark client.
+ You can't change the session type after you create a session. To switch between Livy and Spark Connect, you must create a new session.
+ Spark Connect is not supported on AWS Glue Studio. For interactive development using AWS Glue, you can use Notebooks in SageMaker Unified Studio or your preferred IDEs with Python interpreters.
+ Fine-grained access control through Lake Formation is not supported for Spark Connect sessions.