# LSOPS06-BP01 Validate data quality during

ingestion

Define data quality measurements and implement checks during
ingestion.

**Desired outcome:** Data is clean
and ready for analysis upon ingestion.

**Benefits of establishing this best
practice:**

- More trusted results.
- Faster output to conclusions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Build data quality checks into data ingestion pipelines.

Plan to isolate erroneous data and have a way to review it as
needed.

### Implementation steps

1. Identify expected patterns in received data.
2. Build data quality checks in AWS Glue Data Quality.
3. Incorporate checks in data pipelines.
4. Build processes to catch and isolate erroneous data. Alert
   personnel to investigate data errors

## Resources

**Related examples:**

- [Measure
  performance of AWS Glue Data Quality for ETL pipelines](https://aws.amazon.com/blogs/big-data/measure-performance-of-aws-glue-data-quality-for-etl-pipelines/ "https://aws.amazon.com/blogs/big-data/measure-performance-of-aws-glue-data-quality-for-etl-pipelines/")

**Related tools:**

- [AWS Glue](https://aws.amazon.com/glue/ "https://aws.amazon.com/glue/")
- [AWS Glue Data Quality](https://aws.amazon.com/glue/features/data-quality/ "https://aws.amazon.com/glue/features/data-quality/")
