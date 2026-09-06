

# Resource: Restrict to job definition prefix on job submission
<a name="iam-example-restrict-job-submission"></a>

Use the following policy to submit jobs to any job queue with any job definition name that starts with {{JobDefA}}.

**Important**  
When scoping resource-level access for job submission, you must provide both job queue and job definition resource types.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "batch:SubmitJob"
            ],
            "Resource": [
                "arn:aws:batch:{{us-east-2}}:{{111122223333}}:job-definition/JobDefA_*",
                "arn:aws:batch:{{us-east-2}}:{{111122223333}}:job-queue/*"
            ]
        }
    ]
}
```

------

## Accounting for job definition revisions
<a name="iam-example-job-definition-revisions"></a>

**Important**  
A policy that references only the job definition name without a revision number or wildcard (for example, `job-definition/my-job-def`) does not match `SubmitJob` requests, because the request ARN includes the revision (for example, `job-definition/my-job-def:1`). Use a wildcard to match all revisions.

The following examples show how to use wildcards and revision numbers in resource ARNs for the `SubmitJob` action.

**Example: Allow a specific job definition revision**

The following policy allows job submissions using only revision 1 of the specified job definition.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "batch:SubmitJob",
      "Resource": [
        "arn:aws:batch:us-east-1:111122223333:job-definition/my-job-def:1",
        "arn:aws:batch:us-east-1:111122223333:job-queue/*"
      ]
    }
  ]
}
```

**Example: Allow all revisions of a job definition**

The following policy allows job submissions using any revision of the specified job definition. The `:*` pattern matches any revision number.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "batch:SubmitJob",
      "Resource": [
        "arn:aws:batch:us-east-1:111122223333:job-definition/my-job-def:*",
        "arn:aws:batch:us-east-1:111122223333:job-queue/*"
      ]
    }
  ]
}
```