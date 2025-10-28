After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Delivery Model for Persisting Application Output to an

External Destination

Amazon Kinesis Data Analytics uses an "at least once" delivery model for application output to the configured
destinations. When an application is running, Kinesis Data Analytics takes internal checkpoints. These
checkpoints are points in time when output records have been delivered to the destinations
without data loss. The service uses the checkpoints as needed to ensure that your
application output is delivered at least once to the configured destinations.

In a normal situation, your application processes incoming data continuously. Kinesis Data Analytics writes
the output to the configured destinations, such as a Kinesis data stream or a Firehose delivery
stream. However, your application can be interrupted occasionally, for example:

- You choose to stop your application and restart it later.
- You delete the IAM role that Kinesis Data Analytics needs to write your application output to the
  configured destination. Without the IAM role, Kinesis Data Analytics doesn't have any permissions
  to write to the external destination on your behalf.
- A network outage or other internal service failure causes your application to
  stop running momentarily.
  When your application restarts, Kinesis Data Analytics ensures that it continues to process and write
  output from a point before or equal to when the failure occurred. This helps ensure that it
  doesn't miss delivering any application output to the configured destinations.

Suppose that you configured multiple destinations from the same in-application stream.
After the application recovers from failure, Kinesis Data Analytics resumes persisting output to the
configured destinations from the last record that was delivered to the slowest destination.

This might result in the same output record delivered more than once to other destinations.
In this case, you must handle potential duplications in the destination externally.
