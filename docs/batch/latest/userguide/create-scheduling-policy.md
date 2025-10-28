# Tutorial: Create a scheduling policy

Before you can create a job queue with a scheduling policy, you must create a scheduling policy. When you create
a fair-share scheduling policy, you associate one or more share identifiers or share identifier prefixes with weights
for the queue and optionally assign a decay period and compute reservation to the policy.

###### To create a scheduling policy

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/").
2. From the navigation bar, select the Region to use.
3. In the navigation pane, choose **Scheduling policies**, **Create**.
4. For **Name**, enter a unique name for your scheduling policy. Up to 128 letters (uppercase
   and lowercase), numbers, hyphens, and underscores are allowed.
5. (Optional) For **Share decay seconds**, enter an integer value for the fair-share scheduling policy's
   share decay time. A longer share decay time will use considerably more compute resource usage over a longer time when
   scheduling jobs. This can allow jobs using a share identifier to temporarily use more compute resources than
   the weight for that share identifier would allow if that share identifier had not recently been using
   compute resources.
6. (Optional) For **Compute reservation**, enter an integer value for the fair-share scheduling policy's
   compute reservation. The compute reservation will hold some vCPUs in reserve to be used for share identifiers
   that are not currently active.

The reserved ratio is
`(*computeReservation*/100)^*ActiveFairShares*` where
_ActiveFairShares_ is the number of active share identifiers.

For example, a `computeReservation` value of 50 indicates that AWS Batch should reserve 50% of the
maximum available VCPU if there is only one share identifier, 25% if there are two share identifiers, and
12.5% if there are three share identifiers. A `computeReservation` value of 25 indicates that
AWS Batch should reserve 25% of the maximum available VCPU if there is only one share identifier, 6.25% if there
are two share identifiers, and 1.56% if there are three share identifiers. 7. In the **Share attributes** section, you can specify the share identifier and weight for
each share identifier to associate with the fair-share scheduling policy.

    1. Choose **Add share identifier**.
    2. For **Share identifier**, specify the share identifier. If the string ends with '\*',
     this becomes a share identifier prefix used to match share identifiers for jobs. All of the share
     identifiers and share identifier prefixes in a scheduling policy must be unique and cannot overlap. For
     example, you can't have share identifiers prefix 'UserA\*' and share identifier 'UserA1' in the same fair-share
     scheduling policy.
    3. For **Weight factor**, specify the relative weight for the share identifier. The
     default value is 1.0. A lower value has a higher priority for compute resources. If a share identifier
     prefix is used, jobs with share identifiers that start with the prefix will share the weight factor. This
     effectively increases the weight factor for those jobs, lowering their individual priority but maintaining the
     same weight factor for the share identifier prefix.

8. (Optional) In the **Tags** section, you can specify the key and value for each tag to
   associate with the scheduling policy. For more information, see [Tag your AWS Batch resources](using-tags.md "using-tags.md").
9. Choose **Submit** to finish and create your scheduling policy.
