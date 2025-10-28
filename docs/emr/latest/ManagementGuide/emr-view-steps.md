# Viewing steps after submitting work to an Amazon EMR cluster

You can see up to 10,000 steps that Amazon EMR completed within the last seven days. You can also
view 1,000 steps that Amazon EMR completed any time. This total includes both user-submitted and system steps.

If you submit new steps once the cluster reaches the 1,000 step record limit, Amazon EMR deletes the inactive
user-submitted steps whose statuses have been COMPLETED, CANCELLED, or FAILED for more than seven days.
If you submit steps beyond the 10,000 step record limit, Amazon EMR deletes the
inactive user-submitted step records regardless of their inactive duration.
Amazon EMR doesn't remove these records from the log files. Amazon EMR removes them
from the AWS console, and they aren't returned when you use the AWS CLI or API
to retrieve cluster information. System step records are never removed.

The step information you can view depends on the mechanism used to retrieve cluster
information. The following table indicates the step information returned by each of the
available options.

| Option         | DescribeJobFlow or --describe --jobflow | ListSteps or list-steps |
| -------------- | --------------------------------------- | ----------------------- |
| SDK            | 256 steps                               | Up to 10,000 steps      |
| Amazon EMR CLI | 256 steps                               | NA                      |
| AWS CLI        | NA                                      | Up to 10,000 steps      |
| API            | 256 steps                               | Up to 10,000 steps      |
