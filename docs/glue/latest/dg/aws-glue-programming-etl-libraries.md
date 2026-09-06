

# Developing and testing AWS Glue job scripts locally
<a name="aws-glue-programming-etl-libraries"></a>

When you develop and test your AWS Glue for Spark job scripts, there are multiple available options:
+ AWS Glue Studio console
  + Visual editor
  + Script editor
  + AWS Glue Studio notebook
+ Interactive sessions
  + Jupyter notebook
+ Docker image
  + Local development
  + Remote development

You can choose any of the above options based on your requirements.

If you prefer no code or less code experience, the AWS Glue Studio visual editor is a good choice.

If you prefer an interactive notebook experience, AWS Glue Studio notebook is a good choice. For more information, see [Using Notebooks with AWS Glue Studio and AWS Glue](https://docs.aws.amazon.com/glue/latest/ug/notebooks-chapter.html). If you want to use your own local environment, interactive sessions is a good choice. For more information, see [Using interactive sessions with AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/interactive-sessions-chapter.html).

If you prefer local/remote development experience, the Docker image is a good choice. This helps you to develop and test AWS Glue for Spark job scripts anywhere you prefer without incurring AWS Glue cost.

If you prefer local development without Docker, installing the AWS Glue ETL library directory locally is a good choice.

## Developing using AWS Glue Studio
<a name="develop-using-studio"></a>

The AWS Glue Studio visual editor is a graphical interface that makes it easy to create, run, and monitor extract, transform, and load (ETL) jobs in AWS Glue. You can visually compose data transformation workflows and seamlessly run them on AWS Glue's Apache Spark-based serverless ETL engine. You can inspect the schema and data results in each step of the job. For more information, see the [AWS Glue Studio User Guide](https://docs.aws.amazon.com/glue/latest/ug/what-is-glue-studio.html).

## Developing using interactive sessions
<a name="develop-using-interactive-sessions"></a>

Interactive sessions allow you to build and test applications from the environment of your choice. For more information, see [Using interactive sessions with AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/interactive-sessions-chapter.html).