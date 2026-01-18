# Resource: Restrict job submission by resource tags on job definition and job queue

Use the following policy to submit jobs only when both the job queue has the tag `Environment=dev` and the job definition has the tag `Project=calc`. This policy demonstrates how to use resource tags to control access to AWS Batch resources during job submission.

###### Important

When submitting jobs with policies that evaluate job definition resource tags, you must submit jobs using the job definition revision format (`job-definition:revision`). If you submit jobs without specifying a revision, job definition tags will not be evaluated, potentially bypassing your intended access controls. The `*:*` pattern in the resource ARN enforces that submissions must include a revision, ensuring tag policies are always effectively applied.

This policy uses two separate statements because it applies different tag conditions to different resource types. When scoping resource-level access for job submission, you must provide both job queue and job definition resource types.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "batch:SubmitJob",
      "Resource": "arn:aws:batch:*:*:job-queue/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Environment": "dev"
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": "batch:SubmitJob",
      "Resource": "arn:aws:batch:*:*:job-definition/*:*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Project": "calc"
        }
      }
    }
  ]
}
```
