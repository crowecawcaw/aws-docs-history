# Managing Amazon OpenSearch Ingestion pipeline costs

You can start and stop ingestion pipelines in Amazon OpenSearch Ingestion to control data flow based
on your needs. Stopping a pipeline halts data processing while preserving configurations, so
you can restart it without reconfiguring it. This can help optimize costs, manage resource
usage, or troubleshoot issues. When you stop a pipeline, OpenSearch Ingestion doesn't process
incoming data, but previously ingested data remains available in OpenSearch.

Starting and stopping simplifies the setup and teardown processes for pipelines that you use
for development, testing, or similar activities that don't require continuous availability.
While your pipeline is stopped, you aren't charged for any Ingestion OCU hours. You can
still update stopped pipelines, and they receive automatic minor version updates and
security patches. Restarting a pipeline resumes processing from new incoming data.

###### Note

If your pipeline has excess capacity but needs to remain operational, consider
adjusting its maximum capacity limits rather than stopping and restarting it. This can
help manage costs while ensuring that the pipeline continues processing data
efficiently. For more details, see [Scaling pipelines in Amazon OpenSearch Ingestion](ingestion-scaling.md "ingestion-scaling.md").

The following topics explain how to start and stop pipelines using the AWS Management Console, AWS CLI, and
OpenSearch Ingestion API.

###### Topics

- [Stopping an Amazon OpenSearch Ingestion pipeline](pipeline--stop.md "pipeline--stop.md")
- [Starting an Amazon OpenSearch Ingestion pipeline](pipeline--start.md "pipeline--start.md")
