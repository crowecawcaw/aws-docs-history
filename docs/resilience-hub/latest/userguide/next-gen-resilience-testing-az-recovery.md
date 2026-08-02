# Availability Zone: recovery

The **Availability Zone: recovery** test injects the symptoms
of a power interruption in a single Availability Zone, affecting compute, networking, storage,
and database resources within that AZ. It can help you validate that your service detects the
impaired AZ, continues operating in the healthy AZs, and returns to a healthy state within your
defined RTO. In addition, this test can help you surface single-AZ dependencies you may not be
aware of.

###### What makes this test unique

- Targets a single Availability Zone that you choose, focusing on zonal, in-Region
  resilience.
- This is a recovery test – your service must recover within your RTO.

###### How to pass this test

- This is a recovery test. The RTO countdown starts when test actions begin. The test
  passes if all success alarms return to `OK` state within your RTO and remain
  there until the test actions end.

###### Things to think about

- Choose success alarms that measure regional service health (for example, regional error
  rate, latency) – avoid per-AZ alarms since the impaired AZ is expected to be
  unhealthy.
- Most meaningful for multi-AZ architectures where traffic can shift to healthy AZs. Can
  also be run against single-AZ services.
- If you have AWS Application Recovery Controller (ARC) zonal autoshift enabled on your
  resources, the test exercises that shift automatically. If autoshift is not configured, the
  action is skipped.

###### Key test parameters

- **Availability Zone** – Choose the AZ to impair.
  Select an AZ where your service has resources deployed.
- **Duration** – The length of time the test actions
  run. It takes a few additional minutes afterward to collect final results before the test
  ends. Defaults to your RTO from your service policy plus 30 minutes when you first create the
  test. Set it longer than your RTO to validate that recovery is sustained.

###### Actions

This test runs the following AWS FIS actions to impair the Availability Zone that you select.
If your service has no resources matching an action's target type, that action is skipped. For
details about each action, see the [AWS FIS actions reference](../../../fis/latest/userguide/fis-actions-reference.md "../../../fis/latest/userguide/fis-actions-reference.md").

| Action                                                | Description                                                                                                                      |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `aws:ec2:stop-instances`                              | Stops instances in the impaired AZ for the duration.                                                                             |
| `aws:ec2:api-insufficient-instance-capacity-error`    | Blocks new instance launches in the impaired AZ.                                                                                 |
| `aws:ec2:asg-insufficient-instance-capacity-error`    | Prevents Auto Scaling from provisioning capacity in the AZ.                                                                      |
| `aws:network:disrupt-connectivity`                    | Blocks traffic entering and leaving the subnet, and blocks access to Amazon S3 Express One<br>Zone directory buckets if present. |
| `aws:rds:failover-db-cluster`                         | Fails over the cluster if the writer is in the impaired AZ.                                                                      |
| `aws:elasticache:replicationgroup-interrupt-az-power` | Terminates cache nodes in the impaired AZ without replacement for the duration.                                                  |
| `aws:arc:start-zonal-autoshift`                       | Shifts traffic to healthy AZs.                                                                                                   |

To see this test's parameters and their default values, use
`get-test-template`.
