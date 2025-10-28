# ADVSUS04-BP01 Use batch processing for data cleansing and enrichment to create customer profiles

Use batch processing for data cleansing and customer profile
enrichment in advertising workloads. Schedule the batch jobs
during periods of lowest carbon consumption to minimize resource
usage and environmental impact.

## Implementation guidance

- For workloads like privacy-enhanced data collaboration that
  involve data cleansing, enrichment, and customer profile
  creation, implement batch processing architectures to
  minimize resource usage.
- Use AWS services like
  [AWS Batch](https://aws.amazon.com/batch/ "https://aws.amazon.com/batch/") and
  [AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/") to queue up and schedule these batch
  jobs during periods when the carbon intensity is lower, such
  as times when more renewable energy is available or when
  demand is lower.
- Consider using
  [AWS Graviton](https://aws.amazon.com/ec2/graviton/ "https://aws.amazon.com/ec2/graviton/")-based instances if supported, for batch
  processing workloads, if as they offer energy-efficient
  compute capabilities.
- Sample data sets when possible, to reduce compute,
  analytics, and data transfer needs.

## Key AWS services

- [AWS Instance Scheduler](https://aws.amazon.com/solutions/implementations/instance-scheduler/ "https://aws.amazon.com/solutions/implementations/instance-scheduler/") (for scheduling batch jobs during
  low-carbon periods)
