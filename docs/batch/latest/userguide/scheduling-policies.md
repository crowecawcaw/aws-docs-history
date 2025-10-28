# Use fair-share scheduling policies to assign share identifiers

You can use scheduling policies to configure how compute resources in a job queue are
allocated between users or workloads. Using fair-share scheduling policies, you can assign different
share identifiers to workloads or users. AWS Batch assigns each share identifier a percentage
of the total resources that are available during a period of time.

The fair-share percentage is calculated using the `shareDecaySeconds` and
`shareDistribution` values. You can add time to the fair-share analysis by assigning a
share decay time to the policy. Adding time gives more weight to time and less to the defined
weight. You can hold compute resources in reserve for share identifiers that aren't active by
specifying a compute reservation. For more information, see [SchedulingPolicyDetail](../APIReference/API_SchedulingPolicyDetail.md "../APIReference/API_SchedulingPolicyDetail.md").
