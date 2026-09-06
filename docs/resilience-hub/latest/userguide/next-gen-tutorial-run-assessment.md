

# Step 3: Run your first failure mode assessment
<a name="next-gen-tutorial-run-assessment"></a>

With a service created and a policy applied, you can now run a failure mode assessment. During the assessment, the next generation of Resilience Hub automatically discovers your resources and builds a topology before analyzing failure modes.

**Console:**

1. Navigate to your service.

1. Choose **Failure mode guidance** and add any assertions about your service. For more information, see [Failure mode guidance](next-gen-failure-mode-guidance.md).

1. Choose **Run failure mode assessment**.

1. Wait for the assessment to complete. This typically takes 5–15 minutes.

**AWS CLI:**

```
aws resiliencehubv2 start-failure-mode-assessment \
  --service-arn "arn:aws:resiliencehub:us-east-1:123456789012:service/api-service:def456"
```

To check the status of the assessment:

```
aws resiliencehubv2 list-failure-mode-assessments \
  --service-arn "arn:aws:resiliencehub:us-east-1:123456789012:service/api-service:def456"
```

**What happens during the assessment**

While the assessment runs, the next generation of Resilience Hub performs the following steps in the background:

1. the next generation of Resilience Hub assumes your invoker role.

1. It reads resources from your configured input sources (AWS CloudFormation, tags, Terraform, Amazon EKS).

1. It identifies parent-child relationships (for example, Auto Scaling group to EC2 instances).

1. Resilience Hub builds a topology of your service.

1. It builds a topology showing data flow and containment.

1. A multi-agent AI system analyzes the architecture for failure modes against your resilience policy and AWS Well-Architected best practices.

Once topology generation is complete, you can view the results in the console:
+ **Graph view** – Visual map of resources and connections.
+ **Table view** – List of all discovered resources with metadata.
+ **JSON export** – Download the full topology for external analysis.