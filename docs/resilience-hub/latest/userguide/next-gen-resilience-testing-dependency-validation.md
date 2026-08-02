# Dependency validation

The **Dependency validation** test blocks dependencies
within the Region to see how your service behaves when they are unavailable. It can help
you validate that your service remains healthy when soft dependencies are impaired, and
surface dependencies you may not have known were hard. You can also include known hard
dependencies to understand their impact.

###### What makes this test unique

- Focuses on in-Region dependency failures.
- You choose which dependencies to target.
- If you have enabled dependency discovery in the next generation of Resilience Hub, you can pick from discovered
  dependencies. If not, you can enter DNS endpoints manually.

###### How to pass this test

- This is a sustained test. The test passes if all success alarms remain in
  `OK` state until the test actions end. Use this to validate soft dependencies
  are truly soft – if your alarms breach, the dependency may actually be hard.

###### Things to think about

- Start with a single soft dependency and build up – validate one at a time before
  blocking many.
- If you include a hard dependency, expect your alarms to breach and the test to fail
  – hard dependencies cause significant impact when blocked. This is useful to confirm
  that a dependency is truly hard.
- Choose success alarms that measure overall service health, not the health of the
  dependency itself.
- Ensure your dependencies are actively used during the test (traffic is flowing to them)
  – this validates the block is having an effect. Consider adding alarms or metrics that
  track dependency usage (for example, request count or connection errors) to verify that the
  dependency is being exercised during the test.
- Dependencies must be resolvable DNS endpoints – if the DNS doesn't resolve, the
  action will fail.
- Blocking dependencies that trigger health check failures may cause compute (for example,
  Amazon ECS tasks) to be replaced. The packet loss action does not re-apply to replacement tasks
  and may report as failed.

###### Key test parameters

- **Duration** – The length of time the test actions
  run. It takes a few additional minutes afterward to collect final results before the test
  ends. Default is 30 minutes when you first create the test.
- **Dependencies to block** – By default, the discovered
  soft dependency with the highest query volume is pre-selected. If no dependencies have been
  classified as soft, none are selected. You can adjust to target individual dependencies or
  specific groups, or manually add dependencies by DNS domain name. Additional dependencies
  added here are only used for this test and will not be saved to the service's dependency
  discovery. These defaults apply in the console; when using the API, you provide the
  dependencies explicitly.

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
