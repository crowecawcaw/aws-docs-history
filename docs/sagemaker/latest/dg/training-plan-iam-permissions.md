# IAM for SageMaker training plans

SageMaker training plans requires specific permissions for two distinct roles::

1. **Plan creator role**: Users assigned the _Plan Creator_ role need permissions to search training plan
   offerings, create new training plans, list and describe training plans.
2. **Plan user role**: Users with the _Plan User_ role require permissions to use training plans in SageMaker training jobs
   or when creating and updating SageMaker HyperPod clusters.
   Before using SageMaker training plans, update permissions based on your access method:

- For AWS Management Console or SageMaker SDKs users: Update the permissions of the IAM role configured
  for the console user or API user.
- For AWS CLI users: Ensure your AWS CLI profile is correctly configured with the appropriate
  credentials and permissions.
- For Studio application users such as JupyterLab, set permissions on the execution
  role associated with the space used by the application.
  You can set these permissions using either a managed policy or individual more granular
  permissions.

For information about how to update the permissions policy for a role, see [Update
permissions for a role](../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md "../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md"). For information about how to find and update an execution
role, see [Get your execution role](sagemaker-roles.md#sagemaker-roles-get-execution-role "sagemaker-roles.md#sagemaker-roles-get-execution-role").

###### Note

Administrators should carefully consider which users need the ability to create training
plans and assign permissions accordingly.

## Managed policies

- For plan creators: [`AmazonSageMakerTrainingPlanCreateAccess`](../../../aws-managed-policy/latest/reference/AmazonSageMakerTrainingPlanCreateAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerTrainingPlanCreateAccess.md") provides access to
  create and manage training plans.
- For plan users: [`AmazonSageMakerFullAccess`](../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md") includes the permissions to use
  training plans.

###### Note

- The `AmazonSageMakerFullAccess` managed policy is designed as an
  ease-of-use policy primarily for experimentation purposes. While it provides broad
  access to SageMaker AI features, including the use of training plans, it's important to
  note:
  - This policy is not recommended for production environments due to its broad
    permissions.
  - It does not include permissions for creating training plans, as
    `CreateTrainingPlan` is considered an administrative action requiring
    upfront payment.
  - For production use cases, we strongly recommend creating custom policies that
    adhere to the principle of least privilege, granting only the specific permissions
    required for each role.

## Individual permissions

The following list details the granular permissions that should be set in the IAM policy
statements of a role, based on the specific actions a user needs to perform with
SageMaker training plans:

### Training plans list of permissions

- `SearchTrainingPlanOfferings`: This permission allows users to search for
  available training plan offerings.

```
{
  "Sid": "SearchTrainingPlanOfferingsPermissions",
  "Effect": "Allow",
  "Action": [
    "sagemaker:SearchTrainingPlanOfferings"
  ],
  "Resource": "*"
}
```

- `CreateTrainingPlan`: This permission allows users to create new training
  plans.

###### Note

You must also include permissions for `CreateReservedCapacity` and
`AddTags`, and specify both `training-plan` and
`reserved-capacity` resource types.

```
{
  "Sid": "CreateTrainingPlanPermissions",
  "Effect": "Allow",
  "Action": [
    "sagemaker:CreateTrainingPlan",
    "sagemaker:CreateReservedCapacity",
    "sagemaker:AddTags"
  ],
  "Resource": [
    "arn:aws:sagemaker:*:*:training-plan/*",
    "arn:aws:sagemaker:*:*:reserved-capacity/*"
  ]
}
```

- `DescribeTrainingPlan` : This permission allows users to view details of
  existing training plans.

```
{
  "Sid": "DescribeTrainingPlanPermissions",
  "Effect": "Allow",
  "Action": [
    "sagemaker:DescribeTrainingPlan"
  ],
  "Resource": [
    "arn:aws:sagemaker:::training-plan/*"
  ]
}
```

- `ListTrainingPlans`: This permission allows users to list all training
  plans in their AWS account.

```
{
  "Sid": "ListTrainingPlansPermissions",
  "Effect": "Allow",
  "Action": [
    "sagemaker:ListTrainingPlans"
  ],
  "Resource": "*"
}
```

### Individual permissions per type of

user

This section provides a detailed breakdown of the individual permissions required for
each role, as mentioned in the [IAM for SageMaker training plans](training-plan-iam-permissions.md "training-plan-iam-permissions.md") section.

For plan creators, the following permissions are necessary:

- `sagemaker:SearchTrainingPlanOfferings`
- `sagemaker:CreateTrainingPlan`
- `sagemaker:CreateReservedCapacity`
- `sagemaker:AddTags`
- `sagemaker:DescribeTrainingPlan`
- `sagemaker:ListTrainingPlans`

Plan users require these permissions:

- `sagemaker:CreateTrainingJob` (for SageMaker Training Job)
- `sagemaker:CreateCluster` and `sagemaker:UpdateCluster` (for
  SageMaker HyperPod)
- Access to the `training-plan` and `reserved-capacity`
  resources; When configuring IAM policies for SageMaker training plans, include permissions for
  both `training-plan` and `reserved-capacity` resources. These
  resources are required for both SageMaker training jobs and SageMaker HyperPod clusters. This
  allows your IAM roles to interact with SageMaker training plans resources and manage Reserved
  Capacity.
  - For SageMaker training jobs, ensure your policy includes the
    `"arn:aws:sagemaker:::training-plan/"` and
    `"arn:aws:sagemaker:::reserved-capacity/"` resource ARNs.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sagemaker:CreateTrainingJob"
        ...// other existing known required actions
      ],
      "Resource": [
        "arn:aws:sagemaker:::training-job/",
        "arn:aws:sagemaker:::training-plan/",
        "arn:aws:sagemaker:::reserved-capacity/*"
      ]
    }
  ]
}
```

Similarly, for SageMaker HyperPod configurations, include these same ARNs in addition to the
cluster-specific resources.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sagemaker:CreateCluster",
        "sagemaker:UpdateCluster",
        ...// other existing known required actions
      ],
      "Resource": [
        "arn:aws:sagemaker:::cluster/",
        "arn:aws:sagemaker:::training-plan/",
        "arn:aws:sagemaker:::reserved-capacity/*"
      ]
    }
  ]
}
```
