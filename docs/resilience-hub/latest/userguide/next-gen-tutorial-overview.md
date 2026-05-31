# Tutorial overview and prerequisites

This tutorial walks you through the end-to-end workflow for creating your first system and
service, running a failure mode assessment, and reviewing the results. By the end, you will have
a working resilience assessment for one of your applications.

| Step | What you will do                       | Estimated time              |
| ---- | -------------------------------------- | --------------------------- |
| 1    | Configure a resilience policy          | 3 minutes                   |
| 2    | Create your first system and service   | 5 minutes                   |
| 3    | Run your first failure mode assessment | 5–15 minutes (asynchronous) |
| 4    | Review findings and recommendations    | 10 minutes                  |

**Total time:** approximately 30–40 minutes.

Before you begin this tutorial, ensure the following:

- You have an AWS account with deployed resources (AWS CloudFormation stack, tagged resources, or
  Amazon EKS cluster).
- You have created the invoker role (`AWSResilienceHubAssessmentRole`).
  For more information, see
  [Setting up Next generation Resilience Hub](next-gen-setting-up.md "next-gen-setting-up.md").
- You have IAM permissions to call the next generation of Resilience Hub APIs.
