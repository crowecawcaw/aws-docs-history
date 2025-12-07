# Creating pipelines

The pipeline configuration wizard guides you through creating your data
pipeline.

1. Under **General settings**, provide the data source details
   including source name and type. You can also specify pipeline tags and the name
   of your pipeline.
2. Under **Destination**, specify the destination details. CloudWatch Logs
   is the default destination.
3. Under **Processor**, add the desired processors and parsers.
   A parser is a required first step for certain data types. You can perform custom
   parsing using processors like Grok or CSV. Processors that are not supported by the
   data type are disabled.
4. Under **Review and create**, review the pipeline
   configuration. If you're satisfied with the configuration, choose
   **Create pipeline** to start deployment and creation of
   pipeline resources. Pipeline creation completion takes up to 5 minutes depending
   on the source type. Upon completion, you'll be taken to the Pipelines tab in the
   Ingestion Console.

###### Important

Pipeline processor configurations are logged in AWS CloudTrail events for
auditing and compliance purposes. To protect sensitive information, do not include
passwords, API keys, or other sensitive information in processor
configurations.
