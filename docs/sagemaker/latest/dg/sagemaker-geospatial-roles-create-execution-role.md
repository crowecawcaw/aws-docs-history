# Creating an new SageMaker AI

execution role

To work with SageMaker geospatial capabilities, you must set up a user, group, or role, and an
execution role. A user role is an AWS identity with
permissions
policies that determine what the user can and cannot do within AWS.
An execution role is an IAM role that grants the service permission to access your
AWS resources. An execution role consists of permissions and trust policy. The trust
policy specifies which principals have the permission to assume the role.

SageMaker geospatial also requires a different service principal,
`sagemaker-geospatial.amazonaws.com`. If you are an existing SageMaker AI
customer, you must add this additional service principal to your trust policy.

Use the following procedure to create an new execution role with the IAM managed
policy, `AmazonSageMakerGeospatialFullAccess`, attached. If your use case
requires more granular permissions, use other sections of this guide to create an
execution role that meets your business needs.

###### Important

The IAM managed policy, `AmazonSageMakerGeospatialFullAccess`, used
in the following procedure, only grants the execution role permission to perform
certain Amazon S3 actions on buckets or objects with `SageMaker`,
`Sagemaker`, `sagemaker`, or `aws-glue` in the
name. To learn how to update the execution role's policy to grant it access to other
Amazon S3 buckets and objects, see [Add Additional Amazon S3
Permissions to a SageMaker AI Execution Role](sagemaker-roles.md#sagemaker-roles-get-execution-role-s3 "sagemaker-roles.md#sagemaker-roles-get-execution-role-s3").

###### To create a new role

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Select **Roles** and then select **Create
   role**.
3. Select **SageMaker**.
4. Select **Next: Permissions**.
5. The IAM managed policy, `AmazonSageMakerGeospatialFullAccess` is
   automatically attached to this role. To see the permissions included in this
   policy, select the sideways arrow next to the policy name. Select
   **Next: Tags**.
6. (Optional) Add tags and select **Next: Review**.
7. Give the role a name in the text field under **Role name**
   and select **Create role**.
8. In the **Roles** section of the IAM console, select the
   role you just created in step 7. If needed, use the text box to search for the
   role using the role name you entered in step 7.
9. On the role summary page, make note of the ARN.
