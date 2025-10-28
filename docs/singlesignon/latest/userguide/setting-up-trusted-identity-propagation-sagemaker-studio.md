# Setting up trusted identity

propagation with SageMaker Studio

The following procedure walks you through setting up SageMaker Studio for trusted identity
propagation and user background sessions.

## Prerequisites

Before you can get started with this tutorial, you'll need to complete the following tasks:

1. [Enable IAM Identity Center](enable-identity-center.md "enable-identity-center.md"). An
   organization instance is required. For more
   information, see [Prerequisites and
   considerations](trustedidentitypropagation-overall-prerequisites.md "trustedidentitypropagation-overall-prerequisites.md").
2. [Provision the users and groups from
   your source of identities into IAM Identity Center](tutorials.md "tutorials.md").
3. [Confirm that user background sessions are enabled](user-background-sessions.md "user-background-sessions.md") in the IAM Identity Center console. By default, user background sessions are enabled and the session duration is set to 7 days. You can change this duration.

To set up trusted identity propagation from SageMaker Studio, the SageMaker Studio
administrator must perform the following steps.

## Step 1: Enable trusted identity propagation in a new or existing SageMaker Studio domain

SageMaker Studio uses domains to organize user profiles, applications, and their associated resources. To enable trusted identity propagation, you must create a SageMaker Studio domain or modify an existing domain as described in the following procedure.

1.  Open the SageMaker AI console, navigate to **Domains**, and do either of the following.
    - **Create a new SageMaker Studio domain by using [Setup for organizations](../../../sagemaker/latest/dg/onboard-custom.md#onboard-custom-instructions "../../../sagemaker/latest/dg/onboard-custom.md#onboard-custom-instructions").**

    Choose **Set up for
    organizations**, and then do the following:

        + Choose **AWS Identity Center** as the authentication method.
        + Select the **Enable trusted identity propagation for all users on this domain** check box.

    - **Modify an existing SageMaker Studio domain.**
      - Select an existing domain that uses IAM Identity Center for authentication.

      ###### Important

      Trusted identity propagation is only supported in SageMaker Studio domains that use IAM Identity Center for
      authentication. If the domain uses IAM for
      authentication, you can't change the authentication
      method, and therefore you can't enable trusted identity propagation.
      - [Edit domain
        settings](../../../sagemaker/latest/dg/domain-edit.md "../../../sagemaker/latest/dg/domain-edit.md"). Edit the
        **Authentication and
        permissions** settings to enable trusted
        identity propagation.

2.  Proceed to [Step 2: Configure the default domain execution role](#setting-up-trusted-identity-propagation-sagemaker-studio-domain-execution-role "#setting-up-trusted-identity-propagation-sagemaker-studio-domain-execution-role"). This role is required for users of a SageMaker Studio domain to access other AWS services such as Amazon S3.

## Step 2: Configure the default domain execution role and role trust

policy

A _domain execution role_ is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a SageMaker Studio domain assumes on behalf of all users in the domain. The permissions that you assign to this role determine what actions SageMaker Studio can perform.

1. To create or select a domain execution role, do either of the following:
   - **Create or select a role by using [Setup for organizations](../../../sagemaker/latest/dg/onboard-custom.md#onboard-custom-instructions "../../../sagemaker/latest/dg/onboard-custom.md#onboard-custom-instructions").**
     - Open the SageMaker AI console and follow the console guidance in **Step 2: Configure roles and ML activities** to create a new domain execution role or select an existing role.
     - Complete the rest of the setup steps to create your SageMaker Studio domain.

   - **Create an execution role manually.**
     - Open the IAM console and [create the execution role yourself](../../../sagemaker/latest/dg/sagemaker-roles.md#sagemaker-roles-create-execution-role "../../../sagemaker/latest/dg/sagemaker-roles.md#sagemaker-roles-create-execution-role").

2. [Update the trust
   policy](../../../IAM/latest/UserGuide/id_roles_update-role-trust-policy.md "../../../IAM/latest/UserGuide/id_roles_update-role-trust-policy.md") that is attached to the domain execution role
   so that it includes the following two actions: [`sts:AssumeRole`](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") and [`sts:SetContext`](../../../IAM/latest/UserGuide/reference_policies_iam-condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_iam-condition-keys.md"). For information about how to find the execution role for your SageMaker Studio domain, see [Get domain execution role](../../../sagemaker/latest/dg/sagemaker-roles.md#sagemaker-roles-get-execution-role-domain "../../../sagemaker/latest/dg/sagemaker-roles.md#sagemaker-roles-get-execution-role-domain").

A _trust policy_ specifies the identity that can assume a role. This policy is
required to allow the SageMaker Studio service to assume the domain
execution role. Add these two actions so that they appear as follows in
your policy.

```
{

    "Version": "2012-10-17",


    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "sagemaker.amazonaws.com"
                ]
            },
            "Action": [
                "sts:AssumeRole",
                "sts:SetContext"
            ]
        }
    ]
}
```

## Step 3: Verify required Amazon S3 Access Grant permissions for the domain execution role

To use Amazon S3 Access Grants, you must have a permissions policy attached (either as an inline policy or a customer managed policy) to your SageMaker Studio domain execution role that contains the following permissions.

```
{

    "Version": "2012-10-17",

    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetDataAccess",
                "s3:GetAccessGrantsInstanceForPrefix"
                ],
            "Resource": "arn:aws:s3:us-east-2:111122223333:access-grants/default"
        }
    ]
}

```

If you don't have a policy that contains these permissions, follow the
instructions in [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the
_AWS Identity and Access Management User Guide_.

## Step 4: Assign groups and users to the domain

Assign groups and users to the SageMaker Studio domain by following the steps in [Add groups and users](../../../sagemaker/latest/dg/domain-groups-add.md "../../../sagemaker/latest/dg/domain-groups-add.md").

## Step 5: Set up Amazon S3 Access Grants

To set up Amazon S3 Access Grants, follow the steps in [Configuring Amazon S3 Access Grants for trusted identity propagation through IAM Identity Center](tip-tutorial-s3.md#tip-tutorial-s3-configure "tip-tutorial-s3.md#tip-tutorial-s3-configure"). Use the step-by-step instructions to complete the following tasks:

1. Create an Amazon S3 Access Grants instance.
2. Register a location in that instance.
3. Create grants to allow specific IAM Identity Center users or groups to access designated Amazon S3 locations or subsets (for example, specific prefixes) within those locations.

## Step 6: Submit a SageMaker training job and view user background session details

In SageMaker Studio, launch a new Jupyter notebook and submit a training job. While the job is running, complete the following steps to view the session information and to verify that the user background session context is active.

1. Open the IAM Identity Center console.
2. Choose **Users**.
3. On the **Users** page, choose the username of the user whose sessions you want to manage. This takes you to a page with the user's information.
4. On the user's page, choose the **Active sessions** tab. The number in parentheses next to **Active sessions** indicates the number of active sessions for this user.
5. To search for sessions by the Amazon Resource Name (ARN) of the job that is using the session, in the **Session type** list, choose **User background sessions**, and then enter the job ARN in the search box.

Following is an example of how a training job that is using a user background session appears in the A**ctive sessions** tab for a user.

![](images/sagemaker-studio-training-job-displayed-in-identity-center-console-active-sessions.png)

## Step 7: View the CloudTrail logs to verify trusted identity propagation in CloudTrail

When trusted identity propagation is enabled, actions appear in CloudTrail event logs under the `onBehalfOf` element. The `userId` reflects the ID of the IAM Identity Center user who initiated the training job. The following CloudTrail event captures the process of trusted identity propagation.

```

                            "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:SageMaker",
    "arn": "arn:aws:sts::111122223333:assumed-role/SageMaker-ExecutionRole-20250728T125817/SageMaker",
    "accountId": "111122223333",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
        "sessionIssuer": {
            "type": "Role",
            "principalId": "AROA123456789EXAMPLE",
            "arn": "arn:aws:iam::111122223333:role/service-role/SageMaker-ExecutionRole-20250728T125817",
            "accountId": "111122223333",
            "userName": "SageMaker-ExecutionRole-20250728T125817"
        },
        "attributes": {
            "creationDate": "2025-07-29T17:17:10Z",
            "mfaAuthenticated": "false"
        }
    },
    "onBehalfOf": {
        "userId": "2801d3e0-f0e1-707f-54e8-f558b19f0a10",
        "identityStoreArn": "arn:aws:identitystore::777788889999:identitystore/d-1234567890"
    }
},


```

## Runtime considerations

If an administrator sets **MaxRuntimeInSeconds** for long-running training or processing jobs that is lower than the user background session duration, SageMaker Studio runs the job for the minimum of either **MaxRuntimeInSeconds** or the user background session duration.

For more information about **MaxRuntimeInSeconds**, see the guidance for the `CreateTrainingJob` [StoppingCondition](../../../sagemaker/latest/APIReference/API_CreateTrainingJob.md#sagemaker-CreateTrainingJob-request-StoppingCondition "../../../sagemaker/latest/APIReference/API_CreateTrainingJob.md#sagemaker-CreateTrainingJob-request-StoppingCondition") parameter in the _Amazon SageMaker API Reference_.
