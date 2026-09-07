

# ADVCOST04-BP03 Store profiles in a single Region and replicate asynchronously
<a name="advcost04-bp03"></a>

 Generally, users will only be in one Region at a time and therefore will only be updating in one Region. As a result, schedule replication a few times a day with AWS Step Functions and AWS Lambda to meet the resiliency requirements for data while minimizing high latency and data transfer costs. 

## Implementation guidance
<a name="implementation-guidance-advcost04-bp03"></a>

1.  Develop a Lambda replication function. 

1.  Configure your Step Functions workflow. 

1.  Set up a Amazon CloudWatch event rule for scheduling. 

1.  Implement error handling. 

1.  Configure monitoring. 

1.  Test your replication workflow. 

## Key AWS services
<a name="key-aws-services-50"></a>
+  AWS Step Functions 
+  AWS Lambda 