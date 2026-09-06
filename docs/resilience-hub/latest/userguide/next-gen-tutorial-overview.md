

# Tutorial overview and prerequisites
<a name="next-gen-tutorial-overview"></a>

This tutorial walks you through the end-to-end workflow for creating your first system and service, running a failure mode assessment, and reviewing the results. By the end, you will have a working resilience assessment for one of your applications.


| Step | What you will do | Estimated time | 
| --- | --- | --- | 
| 1 | Configure a resilience policy | 3 minutes | 
| 2 | Create your first system and service | 5 minutes | 
| 3 | Run your first failure mode assessment | 5–15 minutes (asynchronous) | 
| 4 | Review findings and recommendations | 10 minutes | 
| 5 | Enable dependency discovery (optional) | 5 minutes | 
| 6 | Run your first resilience test (optional) | 10 minutes | 

**Total time:** approximately 40–50 minutes.

Before you begin this tutorial, ensure the following:
+ You have an AWS account with deployed resources (AWS CloudFormation stack, tagged resources, or Amazon EKS cluster).
+ You have an IAM service role for the next generation of Resilience Hub. You can let the console create one automatically when you create your service, or create one manually beforehand. For more information, see [Required IAM permissions and roles](next-gen-iam-permissions.md).
+ You have IAM permissions to call the next generation of Resilience Hub APIs.