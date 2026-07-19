# Running a failure mode assessment at the service level

You can run a failure mode assessment from the console or using the AWS CLI. The
assessment runs asynchronously. Typical completion time is 5 to 15 minutes depending on service
complexity.

**Prerequisites**

- The service's invoker role must be configured and accessible. For more information, see
  [Required IAM permissions and roles](next-gen-iam-permissions.md "next-gen-iam-permissions.md").
- The service must have a valid discovered topology with a data flow relationship between
  at least two resources. For more information, see
  [Minimum topology requirements](next-gen-minimum-topology-requirements.md "next-gen-minimum-topology-requirements.md").
- At least one resilience policy should be applied. Assessments without policies still run
  but produce fewer targeted findings.
  **To start a failure mode assessment (console)**

1. Navigate to your service.
2. Choose **Failure mode guidance** and add any assertions about
   your service. For more information, see
   [Failure mode guidance](next-gen-failure-mode-guidance.md "next-gen-failure-mode-guidance.md").
3. Choose **Run failure mode assessment**.
4. Wait for the assessment to complete (typically 5 to 15 minutes).
   **To start a failure mode assessment (CLI)**

```
aws resiliencehubv2 start-failure-mode-assessment \
  --service-arn "arn:aws:resiliencehub:us-east-1:123456789012:service/checkout:abc123"
```

**To check assessment status**

```
aws resiliencehubv2 list-failure-mode-assessments \
  --service-arn "arn:aws:resiliencehub:..."
```

Status values progress as follows: `PENDING`, then
`IN_PROGRESS`, then `SUCCESS` or
`FAILED`.

During the assessment, Next generation Resilience Hub runs resource discovery in the background:

1. Next generation Resilience Hub assumes your invoker role.
2. Reads resources from your configured input sources (CloudFormation, tags, Terraform, or
   Amazon EKS).
3. Identifies parent-child relationships (for example, Auto Scaling group to Amazon EC2
   instances).
4. Resilience Hub builds a topology of your service.
5. Builds a topology showing data flow and containment.
   Once topology is complete, you can view it in the console:

- **Graph view** – Visual map of resources and
  connections.
- **Table view** – List of all discovered resources with
  metadata.
- **JSON export** – Download the full topology for
  external analysis.
