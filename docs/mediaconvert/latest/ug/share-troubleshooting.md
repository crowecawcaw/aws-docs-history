# Troubleshooting share requests

If you encounter issues when you create share requests, check the following:

**400 Bad Request**

Verify that your job ID and support case ID are correctly
formatted.

**403 Forbidden**

Make sure that your IAM user or role has the
`mediaconvert:CreateResourceShare` permission and can
access the specified job.

**404 Not Found**

Verify that the job exists and that the support case ID is
valid.

**409 Conflict**

A share request for this job is already in progress. Wait for it to complete before you submit a new request.

**429 Too Many Requests**

You've exceeded the rate limit of 0.1 requests per second. Wait before you retry your request.

If sharing fails after the request is accepted, check the
`lastShareDetails` field in the job response for specific error
information.
