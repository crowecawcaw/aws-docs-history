# Submit work to an Amazon EMR cluster

This section describes the methods that you can use to submit work to an Amazon EMR cluster. To
submit work, you can add steps, or you can interactively submit Hadoop jobs to the
primary node.

Consider the following rules of step behavior when you submit steps to a cluster:

- A step ID can contain up to 256 characters.
- You can have up to 256 PENDING and RUNNING steps in a cluster.
- Even if you have 256 active steps running on a cluster, you can interactively
  submit jobs to the primary node. You can submit an unlimited number of steps
  over the lifetime of a long-running cluster, but only 256 steps can be RUNNING or
  PENDING at any given time.
- With Amazon EMR versions 4.8.0 and later, except version 5.0.0, you can cancel pending
  steps. For more information, see [Cancel steps when you submit work to an Amazon EMR cluster](emr-cancel-steps.md "emr-cancel-steps.md").
- With Amazon EMR versions 5.28.0 and later, you can cancel both pending and running
  steps. You can also choose to run multiple steps in parallel to improve cluster
  utilization and save cost. For more information, see [Considerations for running multiple steps in
  parallel when you submit work to Amazon EMR](emr-concurrent-steps.md "emr-concurrent-steps.md").

###### Note

For the best performance, we recommend that you store custom bootstrap actions, scripts, and other files that you want to use with Amazon EMR in an Amazon S3 bucket that is in the same AWS Region as your cluster.

###### Topics

- [Adding steps to a cluster with the Amazon EMR
  Management Console](emr-add-steps-console.md "emr-add-steps-console.md")
- [Adding steps to an Amazon EMR cluster with the AWS CLI](add-step-cli.md "add-step-cli.md")
- [Considerations for running multiple steps in
  parallel when you submit work to Amazon EMR](emr-concurrent-steps.md "emr-concurrent-steps.md")
- [Viewing steps after submitting work to an Amazon EMR cluster](emr-view-steps.md "emr-view-steps.md")
- [Cancel steps when you submit work to an Amazon EMR cluster](emr-cancel-steps.md "emr-cancel-steps.md")
