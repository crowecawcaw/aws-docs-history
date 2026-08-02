# Multi-Region: recovery

The **Multi-Region: recovery** test introduces failures into
dependencies in one Region to validate that your service can recover and serve clients from a
recovery Region within your recovery objectives. This test applies to both active/active and
active/passive architectures. For example, you can initiate your recovery procedure and confirm
your service recovers within your defined Recovery Time Objective (RTO) in the recovery Region.

###### What makes this test unique

- Validates recovery to another Region against your recovery objectives, not just
  in-Region resilience.
- You choose which dependencies to impair in the primary Region, so you can practice
  detection and recovery.
- The test integrates with ARC Region switch so you can track plan execution details in
  the test report.

###### How to pass this test

- This is a recovery test. The RTO countdown starts when test actions begin. The test
  passes if all success alarms return to `OK` state within your Multi-Region
  RTO and remain there until the test actions end. Your service must have a resilience policy
  with a Multi-Region RTO defined.

###### Things to think about

- Choose dependencies in the impaired Region that are significant enough to trigger your
  recovery procedure. Pick hard dependencies or DNS endpoints that, if blocked, would
  meaningfully impair that Region.
- The test injects faults in the impaired Region – you perform the recovery action
  yourself (for example, triggering failover/ARC Region switch plan). The test watches whether your
  recovery Region comes healthy within your RTO by evaluating alarm state.
- Choose success alarms in the recovery Region that validate it's serving traffic –
  or use global/application-level alarms that reflect overall customer experience.
- Consider setting duration longer than your RTO to validate recovery is sustained.
- Ensure your dependencies are actively used during the test (traffic is flowing to them)
  – this validates the block is having an effect. Consider adding alarms or metrics that
  track dependency usage (for example, request count or connection errors) to verify that the
  dependency is being exercised during the test.
- Dependencies must be resolvable DNS endpoints.
- Blocking dependencies that trigger health check failures may cause compute (for example,
  Amazon ECS tasks) to be replaced. The packet loss action does not re-apply to replacement tasks
  and may report as failed.

###### Key test parameters

- **Impaired Region** – The Region where faults are
  injected.
- **Recovery Region** – The Region where you expect
  your service to recover to.
- **Duration** – The length of time the test actions
  run. It takes a few additional minutes afterward to collect final results before the test
  ends. Defaults to your Multi-Region RTO from your service policy plus 30 minutes when you
  first create the test.
- **Dependencies to block** – Choose dependencies that,
  if blocked, would significantly impair your service and help validate failover to another
  Region. By default, the discovered hard dependency with the highest query volume is
  pre-selected. If no dependencies have been classified as hard, none are selected. You can
  adjust or manually add dependencies by DNS domain name. Additional dependencies added here
  are only used for this test and will not be saved to the service's dependency discovery.
  These defaults apply in the console; when using the API, you provide the dependencies
  explicitly.
- **Region Switch plan** (optional) – Attaching an ARC
  Region Switch plan lets the next generation of Resilience Hub include the actual failover timeline in your test
  results and report. If you use manual failover or a custom automation, leave this empty.

###### Actions

This test runs the following AWS FIS actions to drop traffic to the dependencies that you
select. Actions inject 100% packet loss on Amazon EC2 instances, Amazon ECS tasks (Amazon EC2 and Fargate), and
Amazon EKS pods (Amazon EC2). If your service has no resources matching an action's target type, that
action is skipped.

###### Note

The actions used to block dependencies require additional setup: SSM Agent installed on
Amazon EC2 instances, an SSM Agent container in your Amazon ECS task definition, or a Kubernetes
service account for Amazon EKS pods.

| Action                             | Description                                                           |
| ---------------------------------- | --------------------------------------------------------------------- |
| `aws:ssm:send-command`             | Drops traffic from Amazon EC2 instances to the selected dependencies. |
| `aws:ecs:task-network-packet-loss` | Drops traffic from Amazon ECS tasks to the selected dependencies.     |
| `aws:eks:pod-network-packet-loss`  | Drops traffic from Amazon EKS pods to the selected dependencies.      |

To see this test's parameters and their default values, use
`get-test-template`.
