# Controlling access and labeling jobs using tags

You can label and control access to your S3 Batch Operations jobs by adding
_tags_. Tags can be used to identify who is responsible for a
Batch Operations job. The presence of job tags can grant or limit a user's ability to cancel a
job, activate a job in the confirmation state, or change a job's priority level. You can
create jobs with tags attached to them, and you can add tags to jobs after they're created.
Each tag is a key-value pair that can be included when you create the job or updated
later.

###### Warning

Make sure that your job tags don't contain any confidential information or personal
data.

Consider the following tagging example: Suppose that you want your Finance department
to create a Batch Operations job. You could write an AWS Identity and Access Management (IAM) policy that allows a
user to invoke `CreateJob`, provided that the job is created with the
`Department` tag assigned the value `Finance`. Furthermore,
you could attach that policy to all users who are members of the Finance
department.

Continuing with this example, you could write a policy that allows a user to update
the priority of any job that has the desired tags, or cancel any job that has those
tags. For more information, see [Controlling permissions for Batch Operations using job
tags](batch-ops-job-tags-examples.md "batch-ops-job-tags-examples.md").

You can add tags to new S3 Batch Operations jobs when you create them, or you can add them
to existing jobs.

Note the following tag restrictions:

- You can associate up to 50 tags with a job as long as they have unique tag keys.
- A tag key can be up to 128 Unicode characters in length, and tag values can be up to 256 Unicode characters
  in length.
- The key and values are case sensitive.
  For more information about tag restrictions, see [User-Defined Tag Restrictions](../../../awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.md "../../../awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.md") in the _AWS Billing and Cost Management User
  Guide_.

## API operations related to S3 Batch Operations job tagging

Amazon S3 supports the following API operations that are specific to S3 Batch Operations job
tagging:

- [GetJobTagging](../API/API_control_GetJobTagging.md "../API/API_control_GetJobTagging.md")
  – Returns the tag set associated with a Batch Operations job.
- [PutJobTagging](../API/API_control_PutJobTagging.md "../API/API_control_PutJobTagging.md")
  – Replaces the tag set associated with a job. There are two distinct
  scenarios for S3 Batch Operations job tag management using this API action:
  - Job has no tags – You can add a set of tags to a job (the job has no prior
    tags).
  - Job has a set of existing tags – To modify the existing tag set, you can either replace
    the existing tag set entirely, or make changes within the existing tag
    set by retrieving the existing tag set using [GetJobTagging](../API/API_control_GetJobTagging.md "../API/API_control_GetJobTagging.md"), modify that tag set, and
    use this API action to replace the tag set with the one you have
    modified.

  ###### Note

  If you send this request with an empty tag set, S3 Batch Operations deletes the existing tag set on
  the object. If you use this method, you are charged for a Tier 1
  Request (`PUT`). For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing "https://aws.amazon.com/s3/pricing").

  To delete existing tags for your Batch Operations job, the
  `DeleteJobTagging` action is preferred because it
  achieves the same result without incurring charges.

- [DeleteJobTagging](../API/API_control_DeleteJobTagging.md "../API/API_control_DeleteJobTagging.md") – Deletes the tag set
  associated with a Batch Operations job.
