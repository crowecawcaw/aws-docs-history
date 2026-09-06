

# Preparing security
<a name="preparing-security"></a>

This section discusses the main security requirements for AWS IoT Device Management Software Package Catalog.

## Resource-based authentication
<a name="resource-based-authorization"></a>

Software Package Catalog uses resource-based authorization to provide added security when updating software on your fleet. This means that you must create an AWS Identity and Access Management (IAM) policy that grants rights to perform `create`, `read`, `update`, `delete`, and `list` actions for software packages and package versions, and reference the specific software packages and package versions that you want to deploy in the `Resources` section. You also need these rights so that you can update the [ reserved named shadow](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#reserved-named-shadow). You reference the software packages and package versions by including an Amazon Resource Name (ARN) for each entity.

**Note**  
If you intend the policy to grant rights for package version API calls (such as [CreatePackageVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_CreatePackageVersion.html), [UpdatePackageVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdatePackageVersion.html), [DeletePackageVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_DeletePackageVersion.html)), then you need to include *both* the software package and the package version ARNs in the policy. If you intend the policy to grant rights for software package API calls (such as [CreatePackage](https://docs.aws.amazon.com/iot/latest/apireference/API_CreatePackage.html), [UpdatePackage](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdatePackage.html), and [DeletePackage](https://docs.aws.amazon.com/iot/latest/apireference/API_DeletePackage.html)) then you must include only the software package ARN in the policy.

Structure the software package and package version ARNs as follows:
+ Software package: `arn:aws:iot:{{<region>}}:{{<accountID>}}:package/{{<packageName>}}/{{package}}` 
+ Package version: `arn:aws:iot:{{<region>}}:{{<accountID>}}:package/{{<packageName>}}/version/{{<versionName>}}` 

**Note**  
There are other related rights that you might include in this policy. For example, you might include an ARN for the `job`, `thinggroup`, and `jobtemplate`. For more information and a complete listing of the policy options, see [Securing users and devices with AWS IoT Jobs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs-security.html).

For example, if you have a software package and package version that’s named as follows:
+ AWS IoT thing: `myThing`
+ Package name: `samplePackage`
+ Version `1.0.0`

The policy might look like the following example:

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iot:createPackage",
                "iot:createPackageVersion",
                "iot:updatePackage",
                "iot:updatePackageVersion"
            ],
            "Resource": [
               "arn:aws:iot:us-east-1:111122223333:package/samplePackage",
               "arn:aws:iot:us-east-1:111122223333:package/samplePackage/version/1.0.0"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "iot:GetThingShadow",
                "iot:UpdateThingShadow"
            ],
            "Resource": "arn:aws:iot:us-east-1:111122223333:thing/myThing/$package"
        }
    ]
}
```

## AWS IoT Job rights to deploy package versions
<a name="job-rights-deploy-versions"></a>

For security purposes it’s important for you to grant rights to deploy packages and package versions, and name the specific packages and package versions they’re allowed to deploy. To do this, you create an IAM role and policy that grants permission to deploy jobs with package versions. The policy must specify the destination package versions as a resource.

**IAM policy**

The IAM policy grants the right to create a job that includes the package and version that are named in the `Resource` section.

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iot:CreateJob",
                "iot:CreateJobTemplate"
            ],
            "Resource":[
                "arn:aws:iot:*:{{111122223333}}:job/{{<jobId>}}",
                "arn:aws:iot:*:{{111122223333}}:thing/{{<thingName>}}/$package",
                "arn:aws:iot:*:{{111122223333}}:thinggroup/{{<thingGroupName>}}",
                "arn:aws:iot:*:{{111122223333}}:jobtemplate/{{<jobTemplateName>}}",
                "arn:aws:iot:*:{{111122223333}}:package/{{<packageName>}}/version/{{<versionName>}}"
            ]
        }
    ]
}
```

**Note**  
If you want to deploy a job that uninstalls a software package and package version, you must authorize an ARN where the package version is `$null`, such as in the following:

```
arn:aws:iot:{{<regionCode>}}:{{111122223333}}:package/{{<packageName>}}/version/$null
```

## AWS IoT Job rights to update the reserved named shadow
<a name="job-rights-update-reserved-named-shadow"></a>

To allow jobs to update the thing’s reserved name shadow when the job successfully completes, you must create an IAM role and policy. There are two ways you can do this in the AWS IoT console. The first is when you create a software package in the console. If you see an **Enable dependencies for package management** dialog box, you can choose to use an existing role or create a new role. Or, in the AWS IoT console, choose **Settings**, choose **Manage indexing**, and then **Manage indexing for device packages and versions**. 

**Note**  
If you choose to have the AWS IoT Job service update the reserved named shadow when a job successfully completes, the API call is counted toward your **Device Shadow and registry operations** and can incur a cost. For more information, see [AWS IoT Core pricing](https://aws.amazon.com/iot-core/pricing/).

When you use the **Create role** option, the generated role’s name begins with `aws-iot-role-update-shadows` and contains the following policies:

**Setting up a role**

**Permissions**  
The permissions policy grants the rights to query and update the thing shadow. The `$package` parameter in the resource ARN targets the reserved named shadow.    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iot:DescribeEndpoint",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "iot:GetThingShadow",
                "iot:UpdateThingShadow"
            ],
            "Resource": [
            "arn:aws:iot:{{us-east-1}}:{{111122223333}}:thing/{{<thingName>}}/$package"
            ]
        }
    ]
}
```

**Trust relationship**  
In addition to the permissions policy, the role requires a trust relationship with AWS IoT Core so that the entity can assume the role and update the reserved named shadow.    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "iot.amazonaws.com"
        },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

**Setting up a user policy**

**iam:PassRole permission**  
Finally, you must have the permission to pass the role to AWS IoT Core when you call the [ UpdatePackageConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdatePackageConfiguration.html) API operation.    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iam:PassRole",
                "iot:UpdatePackageConfiguration"
            ],
            "Resource": "arn:aws:iam::{{111122223333}}:role/{{<roleName>}}"
        }
    ]
}
```

## AWS IoT Jobs permissions to download from Amazon S3
<a name="job-rights-download-job-document"></a>

The job document is saved in Amazon S3. You refer to this file when you dispatch through AWS IoT Jobs. You must provide AWS IoT Jobs with the rights to download the file (`s3:GetObject`). You must also set up a trust relationship between Amazon S3 and AWS IoT Jobs. For instructions to create these policies, see [ Presigned URLs](https://docs.aws.amazon.com/iot/latest/developerguide/create-manage-jobs.html#create-manage-jobs-presigned-URLs) in [Managing Jobs](https://docs.aws.amazon.com/iot/latest/developerguide/create-manage-jobs.html).

## Permissions to update the software bill of materials for a package version
<a name="job-rights-update-sbom"></a>

To update the software bill of materials for a package version in the `Draft`, `Published`, or `Deprecated` lifecycle states, you need an AWS Identity and Access Management role and policies for locating the new software bill of materials in Amazon S3 and updating the package version in AWS IoT Core.

First, you will place the updated software bill of materials in your versioned Amazon S3 bucket and call the `[UpdatePackageVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdatePackageVersion.html)` API operation with the `sboms` parameter included. Next, your authorized principal will assume the IAM role you created, locate the updated software bill of materials in Amazon S3, and update the package verison in AWS IoT Core for Software Package Catalog.

The following policies are required to perform this update:

**Policies**
+ **Trust policy** Policy establishing a trust relationship with the authorized principal assuming the IAM role so it can locate the updated software bill of materials from your versioned bucket in Amazon S3 and update the package version in AWS IoT Core.
  +   
****  

    ```
    {
        "Version":"2012-10-17",		 	 	 
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "s3.amazonaws.com"
            },
                "Action": "sts:AssumeRole"
            }
        ]
    }
    ```
  +   
****  

    ```
    {
        "Version":"2012-10-17",		 	 	 
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "iot.amazonaws.com"
            },
                "Action": "sts:AssumeRole"
            }
        ]
    }
    ```
+ **Permissions policy**: Policy to access the Amazon S3 versioned bucket where the software bill of materials are stored for a package version and update the package version in AWS IoT Core.
  +   
****  

    ```
    {
        "Version":"2012-10-17",		 	 	 
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:GetObject"
                ],
                "Resource": [
                    "arn:aws:s3:::{{awsexamplebucket1}}"
                ]
            }
        ]
    }
    ```
  +   
****  

    ```
    {
        "Version":"2012-10-17",		 	 	 
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "iot:UpdatePackageVersion"
                ],
                "Resource": [
                    "arn:aws:iot:*:{{111122223333}}:package/{{<packageName>}}/version/{{<versionName>}}"
                ]
            }
        ]
    }
    ```
+ **Pass role permissions**: Policy granting permission to pass the IAM role to Amazon S3 and AWS IoT Core when you call the `[UpdatePackageVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdatePackageVersion.html)` API operation.
  +   
****  

    ```
    {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "iam:PassRole",
            "s3:GetObject"
          ],
          "Resource": [
            "arn:aws:s3:::{{awsexamplebucket1}}"
          ]
        }
      ]
    }
    ```
  +   
****  

    ```
    {
        "Version":"2012-10-17",		 	 	 
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "iam:PassRole",
                    "iot:UpdatePackageVersion"
                ],
                "Resource": "arn:aws:iam::{{111122223333}}:role/{{<roleName>}}"
            }
        ]
    }
    ```

**Note**  
You can't update the software bill of materials on a package version that has transitioned to the `Deleted` lifecycle state.

For more information on creating an IAM role for an AWS service, see [Creating a role to delegate permission to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html).

For more information on creating an Amazon S3 bucket and uploading objects to it, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) and [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html).