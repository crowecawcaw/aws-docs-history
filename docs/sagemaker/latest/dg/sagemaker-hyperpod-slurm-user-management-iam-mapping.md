# Mapping cluster users to IAM principals for access

Creating the POSIX users with any of the options in [Creating users on a Slurm cluster on SageMaker HyperPod](sagemaker-hyperpod-slurm-user-management-create-users.md "sagemaker-hyperpod-slurm-user-management-create-users.md") gives them accounts
and home directories on the cluster nodes. It does not, however, control who can connect to
the cluster or which Linux account they connect as. Users connect to nodes through AWS Systems Manager
(SSM), and by default every session starts as the generic `ssm-user` account
rather than as the individual's own user. To finish setting up the multi-user environment,
map each cluster user to an IAM principal in the following two steps.

1. **Grant permission to connect.** Give each user's
   IAM role or user the `ssm:StartSession` permission so they can open a
   session to the cluster. For a policy example, see [IAM users for scientists](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-cluster-user "sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-cluster-user").
2. **Connect users as their own Linux account.**
   Associate each IAM role or user with the matching Linux user name so that SSM
   connects the person as their own account instead of `ssm-user`. You do
   this by tagging the IAM principal, as guided in **Option
   2** of step 5 under the procedure **To turn on Run As
   support for Linux and macOS managed nodes** in [Turn on
   Run As support for Linux and macOS managed nodes](../../../systems-manager/latest/userguide/session-preferences-run-as.md "../../../systems-manager/latest/userguide/session-preferences-run-as.md") in the _AWS Systems Manager
   User Guide_. See also [Setting up AWS Systems Manager and Run As for cluster user access control](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-ssm "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-ssm").
