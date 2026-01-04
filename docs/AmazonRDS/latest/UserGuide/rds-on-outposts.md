# Supported DB instance classes for Amazon RDS on AWS Outposts

Amazon RDS on AWS Outposts supports the following DB instance classes:

- General purpose DB instance classes
  - db.m7i.48xlarge
  - db.m7i.24xlarge
  - db.m7i.16xlarge
  - db.m7i.12xlarge
  - db.m7i.8xlarge
  - db.m7i.4xlarge
  - db.m7i.2xlarge
  - db.m7i.xlarge
  - db.m7i.large
  - db.m5.24xlarge
  - db.m5.16xlarge
  - db.m5.12xlarge
  - db.m5.8xlarge
  - db.m5.4xlarge
  - db.m5.2xlarge
  - db.m5.xlarge
  - db.m5.large

- Memory optimized DB instance classes

      + db.r7i.48xlarge
      + db.r7i.24xlarge
      + db.r7i.16xlarge
      + db.r7i.12xlarge
      + db.r7i.8xlarge
      + db.r7i.4xlarge
      + db.r7i.2xlarge
      + db.r7i.xlarge
      + db.r7i.large
      + db.r5.24xlarge
      + db.r5.16xlarge
      + db.r5.12xlarge
      + db.r5.8xlarge
      + db.r5.4xlarge
      + db.r5.2xlarge
      + db.r5.xlarge
      + db.r5.large

  Depending on how you've configured your Outpost, you might not have all of these classes available. For example, if you
  haven't purchased the db.r5 classes for your Outpost, you can't use them with RDS on Outposts.

Only general purpose SSD storage is supported for RDS on Outposts DB instances. For more
information about DB instance classes, see [DB instance classes](Concepts.md "Concepts.md").

Amazon RDS manages maintenance and recovery for your DB instances and requires active capacity on the Outpost to do so.
We recommend that you configure N+1 EC2 instances for each DB instance class in your production environments.
RDS on Outposts can use the extra capacity of these EC2 instances for maintenance and repair operations.
For example, if your production environments have 3 db.m5.large and 5 db.r5.xlarge DB instance classes, then
we recommend that they have at least 4 m5.large EC2 instances and 6 r5.xlarge EC2 instances.
For more information, see [Resilience in AWS Outposts](../../../outposts/latest/userguide/disaster-recovery-resiliency.md "../../../outposts/latest/userguide/disaster-recovery-resiliency.md") in the
_AWS Outposts User Guide_.
