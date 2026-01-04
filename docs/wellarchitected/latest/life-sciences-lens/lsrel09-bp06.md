# LSREL09-BP06 Automate validation testing for

changes

Develop automated functional and regulatory validation test suites
that run after system changes to verify critical functionality, data
integrity, and regulatory controls. Include tests for audit trails,
access control, and business functionality. These tests should also
reassess resiliency factors like recovery time objectives (RTO) and
recovery point objectives (RPO) to verify that changes do not
degrade reliability targets. Test results should be retained as
evidence in the validation package.

**Desired outcome:** Automated
validation verifies that changes do not compromise functionality,
data integrity, or resiliency, and provides evidence of continued
adherence.

**Common anti-patterns:**

- Relying only on manual testing.
- Skipping regression validation for minor changes.
- Not verifying resiliency requirements after updates.

**Benefits of establishing this best
practice:** Reduces downtime risk, improves
reproducibility, and increases regulator confidence by demonstrating
that every change is validated and reliable.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Validation test suites should be version-controlled and updated as
systems evolve. Automating them improves consistency and reduces
the burden on QA teams. These tests must be integrated into the
deployment pipeline so that every change produces verifiable
evidence of continued system validation. Results should be
reviewed, approved, and archived as part of the change control
record.

### Implementation steps

1. Integrate automated validation tests into AWS CodePipeline
   so they run after deployments.
2. Execute functional tests with containerized workloads on
   Amazon ECS/EKS or serverless tests with AWS Lambda.
3. Capture logs and results in Amazon CloudWatch Logs and
   archive them to Amazon S3 for long-term retention.
4. Use AWS Audit Manager to generate audit evidence linking
   test execution to change approvals.
