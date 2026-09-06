

# Building AWS Glue jobs with interactive sessions
<a name="interactive-sessions-chapter"></a>

 Data engineers can author AWS Glue jobs faster and more easily than before using interactive sessions in AWS Glue. 

## Overview of AWS Glue interactive sessions
<a name="interactive-sessions-overview"></a>

 With AWS Glue interactive sessions, you can rapidly build, test, and run data preparation and analytics applications. Interactive sessions provides a programmatic and visual interface for building and testing extract, transform, and load (ETL) scripts for data preparation. Interactive sessions run Apache Spark analytics applications and provide on-demand access to a remote Spark runtime environment. AWS Glue transparently manages serverless Spark for these interactive sessions. 

 Interactive sessions are flexible, so you build and test your applications from the environment of your choice. You can create and work with interactive sessions through the AWS Command Line Interface and the API. You can use Jupyter-compatible notebooks to visually author and test your notebook scripts. Interactive sessions provide an open-source Jupyter kernel that integrates almost anywhere that Jupyter does, including integrating with IDEs such as PyCharm, IntelliJ, and VS Code. This enables you to author code in your local environment and run it seamlessly on the interactive sessions backend. 

 Using the interactive sessions API, customers can programmatically run applications that use Apache Spark analytics without having to manage Spark infrastructure. You can run one or more Spark statements within a single interactive session. 

 Interactive sessions support two session types: Livy and Spark Connect. Livy sessions use REST-based Statement APIs, while Spark Connect sessions provide a direct gRPC connection to the Spark cluster using the PySpark `remote()` API. Spark Connect is available in AWS Glue version 5.1 and later. 

 Interactive sessions therefore provide a faster, cheaper, more-flexible way to build and run data preparation and analytics applications. To learn how to use interactive sessions, see the documentation in this section. [ Magics supported by AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/interactive-sessions-magics.html#interactive-sessions-magics2) 

### Limitations
<a name="interactive-sessions-limitations"></a>
+ Job bookmarks are not supported in interactive sessions.
+  Creating notebook jobs using the AWS Command Line Interface is not supported. 
+  AWS Glue Studio notebooks do not support Scala. 