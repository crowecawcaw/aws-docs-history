# Using Jobs in SageMaker Unified Studio

Jobs in SageMaker Unified Studio provide a comprehensive platform for creating, managing, and executing data processing workloads
across your organization. As a core component of SageMaker Unified Studio, jobs enable you to unify your data engineering,
machine learning, and analytics workflows in a single environment.

Whether you're migrating existing AWS Glue jobs or building new data processing pipelines, jobs provide
the flexibility to work with your preferred authoring tools while maintaining enterprise-grade monitoring, governance,
and scalability. This chapter covers everything you need to know about using jobs effectively in SageMaker Unified Studio.

SageMaker data processing job encapsulates a Python script that connects to your source data, processes it, and then writes it out to your data target.
Typically, a job runs extract, transform, and load (ETL) scripts. SageMaker jobs can be started based on a schedule or event, or on demand.
You can monitor job runs to understand runtime metrics such as completion status, duration, and resources consumed.

When processing your data, SageMaker can write output files in several data formats, including JSON, CSV, ORC (Optimized Row Columnar),
Apache Parquet, and Apache Avro. For some data formats, common compression formats can be written to optimize storage and performance.

## Benefits of using jobs

- **Simple** - Jobs are easy to learn, understand, create, run, and monitor.
- **Flexible** - Jobs support a wide variety of workloads, capabilities, and compute engines.
- **Scalable** - Jobs support your biggest processing workloads.

## Limitations

- Jobs support AWS Glue ETL compute resource on AWS Glue 4.0 and 5.0

## Best Practices

- **Use appropriate authoring methods** - Choose IDE for familiar development tools, Visual ETL for ease of use, and Notebooks for interactive development.
- **Optimize compute resources** - Right-size your job configurations based on data volume and processing requirements.
- **Implement version control** - Use Git integration to track changes and collaborate effectively.
- **Monitor performance** - Regularly review job run metrics to identify optimization opportunities.
- **Test thoroughly** - Use debugging tools to test jobs before production deployment.
- **Organize with Workflows** - Group related jobs into Workflows for better orchestration and dependency management.

## Next Steps

After setting up jobs in SageMaker Unified Studio, consider these next steps:

- Create Workflows to orchestrate multiple jobs and define dependencies.
- Set up monitoring and alerting for critical job runs.
- Explore advanced features like data lineage tracking and cost optimization.
- Integrate jobs with your existing CI/CD pipelines for automated deployment.
