

# Setting up cross-account sharing for SageMaker training plans

Amazon SageMaker AI integrates with AWS Resource Access Manager (AWS RAM) so that you can share a training plan that you own with other AWS accounts in your organization in AWS Organizations. Workloads in those accounts can then run on the plan's reserved capacity. With AWS RAM, you share resources that you own by creating a *resource share*. In a resource share, you specify the resources to share and the consumers with whom to share them. For training plans, consumers can be AWS accounts in your organization, organizational units (OUs), or your entire organization.

For more information about AWS RAM, see the *[AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/)*.

This topic explains how to share training plans that you own, and how to use training plans that are shared with you.

**Topics**
+ [Prerequisites for sharing a training plan](#training-plan-resource-sharing-ram-prereqs)
+ [Sharing a training plan](#training-plan-resource-sharing-share)
+ [Accepting resource share invitations](#training-plan-resource-sharing-responses)
+ [Unsharing a training plan](#training-plan-resource-sharing-unshare)
+ [Identifying a shared training plan](#training-plan-resource-sharing-identify)
+ [Permissions for using a shared training plan](#training-plan-resource-sharing-perms)
+ [Billing for a shared training plan](#training-plan-resource-sharing-billing)

## Prerequisites for sharing a training plan
<a name="training-plan-resource-sharing-ram-prereqs"></a>

Before you share a training plan, make sure that you meet the following prerequisites:
+ You own the training plan in your AWS account. You can't share a training plan that has been shared with you.
+ If you want to share with your organization or an OU, sharing with AWS Organizations is turned on. For more information about turning on sharing, see [ Enable Sharing with AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs) in the *AWS RAM User Guide*.

## Sharing a training plan
<a name="training-plan-resource-sharing-share"></a>

To share a training plan, you add it to a resource share. In the resource share, you also choose the consumers and the managed permission that defines what they can do with the plan.

You can share a training plan that you own using the AWS RAM console or the AWS CLI. Training plans are shared in the AWS Region where you created them, so set the console or the `--region` option to that AWS Region.

------
#### [ AWS RAM console ]

**To share a training plan that you own**

1. Sign in to the AWS Management Console and open the AWS RAM console at [https://console.aws.amazon.com/ram/home](https://console.aws.amazon.com/ram/home).

1. Choose **Create a resource share**, and then enter a name for the resource share.

1. In the **Resources** section, for **Resource type** choose **SageMaker Training Plans**, and then select the training plans that you want to share.

1. (Optional) Add tags, and then choose **Next**.

1. Keep the default managed permission, `AWSRAMDefaultPermissionTrainingPlan`, and then choose **Next**.

1. Specify the AWS accounts, OUs, or organization with which you want to share your training plans, and then choose **Next**.

1. Review your resource share configuration, and then choose **Create resource share**. It might take a few minutes to finish creating the resource share.

------
#### [ AWS CLI ]

Use the [create-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html) command. The following AWS CLI command shares a training plan with one AWS account in your organization. Replace the example values with your own:

```sh
aws ram create-resource-share \
  --name {{my-training-plan-share}} \
  --resource-arns {{arn:aws:sagemaker:us-west-2:111122223333:training-plan/my-training-plan}} \
  --principals {{444455556666}} \
  --region {{us-west-2}}
```

------

For more information, see [Creating a Resource Share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-create) in the *AWS RAM User Guide*.

## Accepting resource share invitations
<a name="training-plan-resource-sharing-responses"></a>

Depending on how the owner shares a training plan, each consumer AWS account might receive an invitation to join the resource share. A consumer that receives an invitation must accept it before it can use the training plan.

For more information on accepting a resource share invitation through AWS RAM, see [Using shared AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-shared.html) in the *AWS Resource Access Manager User Guide*.

## Unsharing a training plan
<a name="training-plan-resource-sharing-unshare"></a>

As the owner, you can stop sharing a training plan at any time by removing it from the resource share. Stopping sharing doesn't cancel the workloads that consumers are already running on the plan.

After you stop sharing a training plan, the following applies to each consumer that you removed access from:
+ The consumer can't use the plan for new workloads.
+ Workloads that are already running on the plan keep running until they finish, until the plan ends, or until the consumer stops them.
+ The consumer can't add capacity to a workload that is already running on the plan. A request that would increase the number of instances the workload uses is denied.
+ The consumer can still reduce the number of instances that a running workload uses, or stop the workload, which returns the capacity to you.

------
#### [ AWS RAM console ]

Remove the training plan from the resource share. For more information, see [Update a resource share in AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-update.html) in the *AWS RAM User Guide*.

------
#### [ AWS CLI ]

Use the [disassociate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/disassociate-resource-share.html) command. The following AWS CLI command removes a training plan from a resource share. Replace the example values with your own:

```sh
aws ram disassociate-resource-share \
  --resource-share-arn {{arn:aws:ram:us-west-2:111122223333:resource-share/my-training-plan-share}} \
  --resource-arns {{arn:aws:sagemaker:us-west-2:111122223333:training-plan/my-training-plan}} \
  --region {{us-west-2}}
```

------

## Identifying a shared training plan
<a name="training-plan-resource-sharing-identify"></a>

Consumers can identify training plans that are shared with them, and the AWS account that owns each plan, using the SageMaker AI console, the AWS RAM console, or the AWS CLI.

------
#### [ SageMaker AI console ]

Choose **Training Plans** in the left pane of the SageMaker AI console. The list shows the training plans that you own and the training plans that are shared with you. The account ID in a training plan's ARN is the account ID of the training plan owner.

------
#### [ AWS RAM console ]

See [Viewing resources shared with you](https://docs.aws.amazon.com/ram/latest/userguide/working-with-shared-view-sr.html) in the *AWS RAM User Guide*. The page lists each shared resource with the AWS account that owns it.

------
#### [ AWS CLI ]

Use the [list-training-plans](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/list-training-plans.html) command. The command returns the training plans that you own and the training plans that are shared with you. The account ID in `TrainingPlanArn` is the account ID of the training plan owner.

To describe or use a shared training plan, specify its full ARN. A training plan name on its own refers to a plan in your own account. The following command describes a shared training plan:

```sh
aws sagemaker describe-training-plan \
  --training-plan-name {{arn:aws:sagemaker:us-west-2:111122223333:training-plan/my-training-plan}}
```

------

## Permissions for using a shared training plan
<a name="training-plan-resource-sharing-perms"></a>

Principals in the consumer account need IAM permission for each action that they call, on the shared training plan's ARN. A policy that allows the action on all resources (`"*"`) already does this. A policy that limits the action to resources in the consumer account doesn't, so add the training plan's ARN to it. The following example policy allows a principal in the consumer account to create training jobs that use a shared training plan:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sagemaker:CreateTrainingJob",
      "Resource": [
        "arn:aws:sagemaker:us-west-2:444455556666:training-job/*",
        "arn:aws:sagemaker:us-west-2:111122223333:training-plan/my-training-plan"
      ]
    }
  ]
}
```

For SageMaker Studio apps, the space's execution role also needs `sagemaker:DescribeTrainingPlan` on the training plan's ARN.

Principals don't need permissions on the owner's `reserved-capacity` ARNs. For more information about the other permissions that training plan users need, see [IAM for SageMaker training plans](training-plan-iam-permissions.md).

## Billing for a shared training plan
<a name="training-plan-resource-sharing-billing"></a>

The owner pays for a plan's reserved capacity when the plan is purchased, and sharing the plan doesn't change that. Consumers are never charged for the capacity in a training plan that is shared with them, and aren't charged separately for the compute time that their workloads use on that capacity.

Standard charges for storage and other resources still apply to each account.