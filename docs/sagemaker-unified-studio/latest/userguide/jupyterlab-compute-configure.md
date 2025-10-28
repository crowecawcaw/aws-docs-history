# Compute-specific

configuration

Amazon SageMaker Unified Studio provides a set of Jupyter magic commands. Magic commands, or magics,
enhance the functionality of the IPython environment. For more information about the
magics that Amazon SageMaker Unified Studio provides, run %help in a notebook.

Compute-specific configurations can be configured by %%configure Jupyter magic. The
%%configure magic takes a json-formatted dictionary. To use %%configure magic, please
specify the compute name in the argument -n. Include —f will restart the session to
forcefully apply the new configuration, otherwise this configuration will apply only when
next session starts.

## Configure an EMR Spark

session

When working with EMR on EC2 or EMR Serverless, %%configure command can be used to
configure the Spark session creation parameters. Using conf settings, you can configure
any Spark configuration that's mentioned in the configuration documentation for Apache
Spark.

```

%%configure -n `compute_name` -f
{
    "conf": {
        "spark.sql.shuffle.partitions": "36"
     }
}

```

## Configure a Glue interactive

session

Use the `--` prefix for run arguments specified for Glue.

```

%%configure -n project.spark.compatibility -f
{
   "––enable-auto-scaling": "true"
   "--enable-glue-datacatalog": "false"
}

```

For more information on job parameters, see Job parameters.

You can update Spark configuration via %%configure when working with Glue with
--conf in configure magic. You can configure any Spark configuration that's mentioned in
the configuration documentation for Apache Spark.

```

%%configure -n project.spark.compatibility -f
{
    "--conf": "spark.sql.shuffle.partitions=36"
}

```
