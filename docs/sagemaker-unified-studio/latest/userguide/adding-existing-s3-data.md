# Adding Amazon S3 data

To bring in Amazon S3 data to your project, you must first gain access to the data and then add the data to your project.
You can gain access to the data by using the project role or an access role.

###### Note

If you are using a bucket in a different account than the account that contains the project tooling environment,
you must use an access role to gain access to the data.

## Prerequisite option 1 (recommended): Gain access using an access role

Work with your admin to complete the following steps:

1. Retrieve the project role ARN and the project ID and send them to your admin.
   1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
      using your SSO or AWS credentials.
   2. Navigate to the project that you want to add Amazon S3 data to.
      You can do this by choosing a project from the project selector dropdown at the top of the page.
   3. On the **Project overview** page, copy the project role ARN and the project ID.

2. The admin then must go to the IAM console and create an access role.
   1. Navigate to the IAM console.
   2. On the **Roles** page, choose **Create role**.
   3. Under **Trusted entity type**, choose **Custom trust policy**.
   4. Edit the policy to include the project ID, the project ARN, and the AWS account ID to grant Amazon S3 access permissions.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Principal": {
    "Service": "access-grants.s3.amazonaws.com"
    },
    "Action": [
    "sts:AssumeRole",
    "sts:SetSourceIdentity"
    ],
    "Condition": {
    "StringEquals": {
    "aws:SourceAccount": "`111122223333`"
    }
    }
    },
    {
    "Effect": "Allow",
    "Principal": {
    "AWS": "`project-role-arn`"
    },
    "Action": "sts:AssumeRole",
    "Condition": {
    "StringEquals": {
    "sts:ExternalId": "`project-id`"
    }
    }
    },
    {
    "Effect": "Allow",
    "Principal": {
    "AWS": "`project-role-arn`"
    },
    "Action": [
    "sts:SetSourceIdentity"
    ],
    "Condition": {
    "StringLike": {
    "sts:SourceIdentity": "${aws:PrincipalTag/datazone:userId}"
    }
    }
    },
    {
    "Effect": "Allow",
    "Principal": {
    "AWS": "`project-role-arn`"
    },
    "Action": "sts:TagSession",
    "Condition": {
    "StringEquals": {
    "aws:RequestTag/AmazonDataZoneProject": "`project-id`",
    "aws:RequestTag/AmazonDataZoneDomain": "`domain-id`"
    }
    }
    }
    ]
   }`

   ```

   5. Choose **Next** twice.
   6. Enter a name for the role, then choose **Create role**.
   7. Select the access role from the list on the **Roles** page.
   8. On the **Permissions** tab of the role, choose **Add permissions**, then **Create inline policy**.
   9. Use the JSON editor to create a policy that grants Amazon S3 access permissions.
      The following example shows a policy that grants access to multiple S3 buckets and folders.
      Replace the bucket and folder names with your own values.

   ```

   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "S3AdditionalBucketPermissions",
               "Effect": "Allow",
               "Action": [
                   "s3:ListBucket",
                   "s3:GetBucketLocation"
               ],
               "Resource": [
                   "arn:aws:s3:::`bucket1`",
                   "arn:aws:s3:::`bucket2`",
                   "arn:aws:s3:::`bucket3`"
               ]
           },
           {
               "Sid": "S3AdditionalObjectPermissions",
               "Effect": "Allow",
               "Action": [
                   "s3:GetObject*",
                   "s3:PutObject"
               ],
               "Resource": [
                   "arn:aws:s3:::`bucket1`/*",
                   "arn:aws:s3:::`bucket2`/`folderA`/*",
                   "arn:aws:s3:::`bucket3`/*"
               ]
           },
           {
               "Sid": "S3AGLocationManagement",
               "Effect": "Allow",
               "Action": [
                   "s3:CreateAccessGrantsLocation",
                   "s3:DeleteAccessGrantsLocation",
                   "s3:GetAccessGrantsLocation"
               ],
               "Resource": [
                   "arn:aws:s3:*:*:access-grants/default/*"
               ],
               "Condition": {
                   "ForAnyValue:StringEquals": {
                       "s3:accessGrantsLocationScope": [
                           "s3://`bucket1`/",
                           "s3://`bucket2`/`folderA`/",
                           "s3://`bucket3`/"
                       ]
                   }
               }
           },
           {
               "Sid": "S3AGPermissionManagement",
               "Effect": "Allow",
               "Action": [
                   "s3:CreateAccessGrant",
                   "s3:DeleteAccessGrant"
               ],
               "Resource": [
                   "arn:aws:s3:*:*:access-grants/default/location/*",
                   "arn:aws:s3:*:*:access-grants/default/grant/*"
               ],
               "Condition": {
                   "ForAnyValue:StringLike": {
                       "s3:accessGrantScope": [
                           "s3://`bucket1`/*",
                           "s3://`bucket2`/`folderA`/*",
                           "s3://`bucket3`/*"
                       ]
                   }
               }
           },
           {
               "Sid": "AllowPassRoleOnProjectRoles",
               "Effect": "Allow",
               "Action": [
                   "iam:PassRole"
               ],
               "Resource": "`access-role-arn`",
               "Condition": {
                   "StringEquals": {
                       "iam:PassedToService": [
                           "access-grants.s3.amazonaws.com"
                       ],
                       "aws:ResourceAccount": "${aws:PrincipalAccount}"
                   }
               }
           },
           {
               "Sid": "S3AGTaggingPermission",
               "Effect": "Allow",
               "Action": [
                   "s3:TagResource",
                   "s3:ListTagsForResource"
               ],
               "Resource": [
                   "arn:aws:s3:*:*:access-grants/default/location/*",
                   "arn:aws:s3:*:*:access-grants/default/grant/*"
               ],
               "Condition": {
                   "StringEquals": {
                       "aws:ResourceAccount": "${aws:PrincipalAccount}"
                   }
               }
           }
       ]
   }

   ```

   ###### Note

   Replace `access-role-arn` with the ARN of this access role.
   For a single bucket, you can use `StringEquals` and `StringLike` instead of
   `ForAnyValue:StringEquals` and `ForAnyValue:StringLike` with a single value instead of an array.

   ###### Note

   Amazon SageMaker Unified Studio grants access to subscribed assets using S3 Access Grants.
   To enable granting access to data using S3 Access Grants, an S3 Access Grants instance is required.
   Amazon SageMaker Unified Studio will use an instance if one is already available or will create one.
   S3 Access Grants needs one instance per AWS Region in a single AWS account.
   For more information, see [Working with S3 Access Grants instances](../../../AmazonS3/latest/userguide/access-grants-instance.md "../../../AmazonS3/latest/userguide/access-grants-instance.md") 10. Choose **Next**. 11. Enter a name for the policy, then choose **Create policy**. 12. Optional: if you want to support cross-account data sharing for S3, add the following to your policy:

   ```

   {
       "Sid": "CrossAccountS3AGResourceSharingPermissions",
       "Effect": "Allow",
       "Action": [
           "ram:CreateResourceShare"
       ],
       "Resource": "*",
       "Condition": {
           "StringEqualsIfExists": {
               "ram:RequestedResourceType": [
                   "s3:AccessGrants"
               ]
           },
           "StringEquals": {
               "aws:ResourceAccount": "${aws:PrincipalAccount}"
           }
       }
   },
   {
       "Sid": "CrossAccountS3AGResourceSharingPolicyPermissions",
       "Effect": "Allow",
       "Action": [
           "s3:PutAccessGrantsInstanceResourcePolicy"
       ],
       "Resource": "arn:aws:s3:*:*:access-grants/default",
       "Condition": {
           "StringEquals": {
               "aws:ResourceAccount": "${aws:PrincipalAccount}"
           }
       }
   }

   ```

   13. Choose **Next**.
   14. Enter a name for the policy, then choose **Create policy**.
   15. Optional: If the bucket is in a different account than the the access role,
       ensure cross-account bucket permissions are set by adding a bucket policy that grants
       cross-account permissions to the access role. For example:

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Sid": "S3AdditionalBucketPermissions",
    "Effect": "Allow",
    "Principal": {
    "AWS": "`access-role-arn`"
    },
    "Action": [
    "s3:ListBucket",
    "s3:GetBucketLocation"
    ],
    "Resource": [
    "arn:aws:s3:::`bucketName`"
    ]
    },
    {
    "Sid": "S3AdditionalObjectPermissions",
    "Effect": "Allow",
    "Principal": {
    "AWS": "`access-role-arn`"
    },
    "Action": [
    "s3:GetObject*",
    "s3:PutObject"
    ],
    "Resource": [
    "arn:aws:s3:::`bucketName`/`key`/*"
    ]
    }
    ]
   }`

   ```

   16. Choose **Update policy**.

## Prerequisite option 2: Gain access using the project role

Work with your admin to complete the following steps:

1. Retrieve the project role ARN and send it to your admin.
   1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
      using your SSO or AWS credentials.
   2. Navigate to the project that you want to add Amazon S3 data to.
      You can do this by choosing a project from the project selector dropdown at the top of the page.
   3. On the **Project overview** page, copy the project role ARN.

2. The admin then must go to the IAM console and update the project role.
   1. Navigate to the IAM console.
   2. On the **Roles** page, search for the project role using the last string in the project role ARN,
      for example: `datazone_usr_role_1a2b3c45de6789_abcd1efghij2kl`.
   3. Select the project role to navigate to the project role details.
   4. Under the **Permissions** tab, choose **Add permissions**,
      then choose **Create inline policy**.
   5. Use the JSON editor to create a policy so that the project has access to Amazon S3 locations,
      using the Amazon S3 resource ARNs. The following example shows a policy that grants access to multiple S3 buckets and folders.
      Replace the bucket and folder names with your own values.

   ```

   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "S3AdditionalBucketPermissions",
               "Effect": "Allow",
               "Action": [
                   "s3:ListBucket",
                   "s3:GetBucketLocation"
               ],
               "Resource": [
                   "arn:aws:s3:::`bucket1`",
                   "arn:aws:s3:::`bucket2`",
                   "arn:aws:s3:::`bucket3`"
               ]
           },
           {
               "Sid": "S3AdditionalObjectPermissions",
               "Effect": "Allow",
               "Action": [
                   "s3:GetObject*",
                   "s3:PutObject"
               ],
               "Resource": [
                   "arn:aws:s3:::`bucket1`/*",
                   "arn:aws:s3:::`bucket2`/`folderA`/*",
                   "arn:aws:s3:::`bucket3`/*"
               ]
           }
       ]
   }

   ```

   6. Choose **Next**
   7. Enter a name for the policy, then choose **Create policy**.

3. Under the **Permissions** tab, choose **Add permissions**, then choose **Create inline policy**.
4. Use the JSON editor to create a policy so that the project has access to an Amazon S3 location, using the Amazon S3 resource ARN that you noted previously.

```

{
    "Sid": "S3AGLocationManagement",
    "Effect": "Allow",
    "Action": [
        "s3:CreateAccessGrantsLocation",
        "s3:DeleteAccessGrantsLocation",
        "s3:GetAccessGrantsLocation"
    ],
    "Resource": [
        "arn:aws:s3:*:*:access-grants/default/*"
    ],
    "Condition": {
        "ForAnyValue:StringEquals": {
            "s3:accessGrantsLocationScope": [
                "s3://`bucket1`/",
                "s3://`bucket2`/`folderA`/",
                "s3://`bucket3`/"
            ]
        }
    }
},
{
    "Sid": "S3AGPermissionManagement",
    "Effect": "Allow",
    "Action": [
        "s3:CreateAccessGrant",
        "s3:DeleteAccessGrant"
    ],
    "Resource": [
        "arn:aws:s3:*:*:access-grants/default/location/*",
        "arn:aws:s3:*:*:access-grants/default/grant/*"
    ],
    "Condition": {
        "ForAnyValue:StringLike": {
            "s3:accessGrantScope": [
                "s3://`bucket1`/*",
                "s3://`bucket2`/`folderA`/*",
                "s3://`bucket3`/*"
            ]
        }
    }
}

```

###### Note

For a single bucket, you can use `StringEquals` and `StringLike` instead of
`ForAnyValue:StringEquals` and `ForAnyValue:StringLike` with a single value instead of an array.

###### Note

Amazon SageMaker Unified Studio grants access to subscribed assets using S3 Access Grants.
To enable granting access to data using S3 Access Grants, an S3 Access Grants instance is required.
Amazon SageMaker Unified Studio will use an instance if one is already available or will create one.
S3 Access Grants needs one instance per AWS Region in a single AWS account.
For more information, see [Working with S3 Access Grants instances](../../../AmazonS3/latest/userguide/access-grants-instance.md "../../../AmazonS3/latest/userguide/access-grants-instance.md") 5. Choose **Next**. 6. Enter a name for the policy, then choose **Create policy**.

## Add the data to your project

When your admin has granted your project access to the Amazon S3 resources,
you can add them to your project.

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the project that you want to add Amazon S3 data to.
3. On the **Data** page, choose the plus icon **+**.
4. Select **Add S3 location**, then choose **Next**.
5. Enter a name for the location path.
6. (Optional) Add a description of the location path.
7. Use the S3 URI and Region provided by your admin.
8. If your admin has granted you access using an access role instead of the project role,
   enter the access role ARN from your admin.
9. Choose **Add S3 location**.

The Amazon S3 data is then accessible within your project in the left navigation on the **Data** page.

## Verify the setup

After creating the connection, verify that the S3 Access Grants location was registered correctly:

1. Navigate to the Amazon S3 console.
2. In the left navigation, choose **Access Grants**.
3. Choose **View Details**, then choose **Locations**.
4. Confirm that the S3 URI is registered against the IAM role you created.

###### Note

If the connection failed to register the Amazon S3 Access Grants location, you must delete the existing connection and create a new one.
