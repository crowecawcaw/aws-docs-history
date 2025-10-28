# Building AWS Glue jobs with interactive sessions

Data engineers can author AWS Glue jobs faster
and more easily than before using interactive sessions in AWS Glue.

###### Topics

- [Overview of AWS Glue interactive sessions](#interactive-sessions-overview "#interactive-sessions-overview")
- [Getting started with AWS Glue interactive sessions](interactive-sessions.md "interactive-sessions.md")
- [Configuring AWS Glue interactive sessions for Jupyter and AWS Glue Studio notebooks](interactive-sessions-magics.md "interactive-sessions-magics.md")
- [Converting a script or notebook into an AWS Glue job](interactive-sessions-convert.md "interactive-sessions-convert.md")
- [Working with streaming operations in AWS Glue interactive sessions](interactive-sessions-streaming.md "interactive-sessions-streaming.md")
- [AWS Glue interactive session pricing](interactive-sessions-session-pricing.md "interactive-sessions-session-pricing.md")
- [Developing and testing AWS Glue job scripts locally](aws-glue-programming-etl-libraries.md "aws-glue-programming-etl-libraries.md")
- [Development endpoints](development.md "development.md")

## Overview of AWS Glue interactive sessions

With AWS Glue interactive sessions, you can rapidly build, test, and run data preparation and analytics applications.
Interactive sessions provides a programmatic and visual interface for building and testing extract, transform, and load (ETL) scripts for
data preparation. Interactive sessions run Apache Spark analytics applications and provide on-demand access to a remote Spark runtime environment.
AWS Glue transparently manages serverless Spark for these interactive sessions.

Interactive sessions are flexible, so you build and test your applications from the environment of your choice. You can create and work
with interactive sessions through the AWS Command Line Interface and the API. You can use Jupyter-compatible notebooks to visually author and test your notebook
scripts. Interactive sessions provide an open-source Jupyter kernel that integrates almost anywhere that Jupyter does, including integrating with
IDEs such as PyCharm, IntelliJ, and VS Code. This enables you to author code in your local environment and run it seamlessly on the interactive
sessions backend.

Using the interactive sessions API, customers can programmatically run applications that use Apache Spark analytics without having to manage
Spark infrastructure. You can run one or more Spark statements within a single interactive session.

Interactive sessions therefore provide a faster, cheaper, more-flexible way to build and run data preparation and analytics applications.
To learn how to use interactive sessions, see the documentation in this section.

[Magics supported by AWS Glue](interactive-sessions-magics.md#interactive-sessions-magics2 "interactive-sessions-magics.md#interactive-sessions-magics2")

###

Limitations

- Job bookmarks are not supported in interactive sessions.
- Creating notebook jobs using the AWS Command Line Interface is not supported.
- AWS Glue Studio notebooks do not support Scala.
