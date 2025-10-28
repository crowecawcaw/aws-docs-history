# Evaluating data quality with AWS Glue Studio

AWS Glue Data Quality evaluates and monitors the quality of your data based on
rules that you define. This makes it easy to identify the data that needs action. In
AWS Glue Studio, you can add data quality nodes to your visual job to create data
quality rules on tables in your Data Catalog.
You
can
then monitor and evaluate changes to your
datasets as they
evolve over time. For an
overview of how to work with AWS Glue Data Quality in AWS Glue Studio, see
the following
video.

The
following are the high-level steps for how you work with AWS Glue Data Quality:

1. **Create
   data quality rules** – Build a set of data quality rules using the DQDL
   builder by choosing built-in rulesets that you configure.
2. **Configure a data quality job** – Define actions based on the
   data quality results and output options.
3. **Save and run
   a
   data quality
   job**
   – Create and run a job. Saving the job will save the
   rulesets
   that
   you created for the job.
4. **Monitor and review the data quality results** – Review the data
   quality results after the job run is complete. Optionally, schedule the job for a future
   date.

## Benefits

Data analysts, data engineers, and data scientists can use the
Evaluate Data
Quality node in AWS Glue Studio to analyze, configure, monitor, and improve the quality
of data from the visual job editor. The benefits of using the data quality node
include the
following:

- **You can detect data quality issues** - You can
  check for issues by creating rules that check characteristics of your datasets.
- **It's easy to get started** - You can start with
  pre-built rules and actions.
- **Tight integration** - You can use data quality
  nodes in AWS Glue Studio because AWS Glue Data Quality runs on top of
  the AWS Glue Data Catalog.
