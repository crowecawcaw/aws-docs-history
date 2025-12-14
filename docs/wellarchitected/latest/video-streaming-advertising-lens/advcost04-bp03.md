# ADVCOST04-BP03 Store profiles in a single Region and

replicate asynchronously

Generally, users will only be in one Region at a time and therefore will only be
updating in one Region. As a result, schedule replication a few times a day with AWS Step Functions
and AWS Lambda to meet the resiliency requirements for data while minimizing high latency and
data transfer costs.

## Implementation guidance

1. Develop a Lambda replication function.
2. Configure your Step Functions workflow.
3. Set up a Amazon CloudWatch event rule for scheduling.
4. Implement error handling.
5. Configure monitoring.
6. Test your replication workflow.

## Key AWS services

- AWS Step Functions
- AWS Lambda
