# Connect Studio

JupyterLab notebooks to Amazon S3 Access Grants with Training and Processing jobs

Use the following information to grant Amazon S3 Access Grants to access data in Amazon SageMaker
Training and Processing jobs.

When a user with trusted identity propagation enabled launches a SageMaker Training or
Processing job that needs to access Amazon S3 data:

- SageMaker AI calls Amazon S3 Access Grants to get temporary credentials based on the user's
  identity
- If successful, these temporary credentials access the Amazon S3 data
- If unsuccessful, SageMaker AI falls back to using the IAM role credentials

###### Note

To enforce that all of the permission are granted through Amazon S3 Access Grants, you
will need to remove related Amazon S3 access permission your execution role and attach them
to your corresponding [Amazon S3 Access Grant](../../../singlesignon/latest/userguide/tip-tutorial-s3.md#tip-tutorial-s3-create-grant "../../../singlesignon/latest/userguide/tip-tutorial-s3.md#tip-tutorial-s3-create-grant").

###### Topics

- [Considerations](#s3-access-grants-jobs-considerations "#s3-access-grants-jobs-considerations")
- [Set up Amazon S3 Access Grants with Training
  and Processing jobs](#s3-access-grants-jobs-setup "#s3-access-grants-jobs-setup")

## Considerations

Amazon S3 Access Grants cannot be used with [Pipe mode](augmented-manifest-stream.md "augmented-manifest-stream.md") for both
SageMaker Training and Processing for Amazon S3 input.

When trusted identity propagation is enabled, you cannot launch a SageMaker Training Job
with the following feature

- Remote Debug
- Debugger
- Profiler

When trusted identity propagation is enabled, you cannot launch a Processing job with the
following feature

- DatasetDefinition

## Set up Amazon S3 Access Grants with Training

and Processing jobs

After Amazon S3 Access Grants is set up, [add the following
permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") to your domain or user [execution role](sagemaker-roles.md#sagemaker-roles-get-execution-role "sagemaker-roles.md#sagemaker-roles-get-execution-role").

- `us-east-1` is your
  AWS Region
- `111122223333` is your
  AWS account ID
- `S3-ACCESS-GRANT-ROLE` is your Amazon S3 Access
  Grant role

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowDataAccessAPI",
            "Effect": "Allow",
            "Action": [
                "s3:GetDataAccess",
                "s3:GetAccessGrantsInstanceForPrefix"
            ],
            "Resource": [
                "arn:aws:s3:`us-east-1`:`111122223333`:access-grants/default"
            ]
        },
        {
            "Sid": "RequiredForIdentificationPropagation",
            "Effect": "Allow",
            "Action": "sts:SetContext",
            "Resource": "arn:aws:iam::`111122223333`:role/`S3-ACCESS-GRANT-ROLE`"
        }
    ]
}
```
