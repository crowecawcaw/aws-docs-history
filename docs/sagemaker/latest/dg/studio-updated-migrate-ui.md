# Migrate the UI from Studio Classic to

Studio

The first phase for migrating an existing domain involves migrating the UI from
Amazon SageMaker Studio Classic to Amazon SageMaker Studio. This phase does not include the migration of data. Users
can continue working with their data the same way as they were before migration. For
information about migrating data, see [(Optional) Migrate data from
Studio Classic to Studio](studio-updated-migrate-data.md "studio-updated-migrate-data.md").

Phase 1 consists of the following steps:

1. Update application creation permissions for new applications available in
   Studio.
2. Update the VPC configuration for the domain.
3. Upgrade the domain to use the Studio UI.

## Prerequisites

Before running these steps, complete the prerequisites in [Complete prerequisites to migrate the
Studio experience](studio-updated-migrate-prereq.md "studio-updated-migrate-prereq.md").

## Step 1: Update application creation

permissions

Before migrating the domain, update the domain's execution role to grant users
permissions to create applications.

1. Create an AWS Identity and Access Management policy with one of the following contents by following the
   steps in [Creating IAM
   policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md"):
   - Use the following policy to grant permissions for all application
     types and spaces.

   ###### Note

   If the domain uses the `SageMakerFullAccess` policy,
   you do not need to perform this action.
   `SageMakerFullAccess` grants permissions to create
   all applications.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Sid": "SMStudioUserProfileAppPermissionsCreateAndDelete",
    "Effect": "Allow",
    "Action": [
    "sagemaker:CreateApp",
    "sagemaker:DeleteApp"
    ],
    "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:app/*",
    "Condition": {
    "Null": {
    "sagemaker:OwnerUserProfileArn": "true"
    }
    }
    },
    {
    "Sid": "SMStudioCreatePresignedDomainUrlForUserProfile",
    "Effect": "Allow",
    "Action": [
    "sagemaker:CreatePresignedDomainUrl"
    ],
    "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:user-profile/${sagemaker:DomainId}/${sagemaker:UserProfileName}"
    },
    {
    "Sid": "SMStudioAppPermissionsListAndDescribe",
    "Effect": "Allow",
    "Action": [
    "sagemaker:ListApps",
    "sagemaker:ListDomains",
    "sagemaker:ListUserProfiles",
    "sagemaker:ListSpaces",
    "sagemaker:DescribeApp",
    "sagemaker:DescribeDomain",
    "sagemaker:DescribeUserProfile",
    "sagemaker:DescribeSpace"
    ],
    "Resource": "*"
    },
    {
    "Sid": "SMStudioAppPermissionsTagOnCreate",
    "Effect": "Allow",
    "Action": [
    "sagemaker:AddTags"
    ],
    "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:*/*",
    "Condition": {
    "Null": {
    "sagemaker:TaggingAction": "false"
    }
    }
    },
    {
    "Sid": "SMStudioRestrictSharedSpacesWithoutOwners",
    "Effect": "Allow",
    "Action": [
    "sagemaker:CreateSpace",
    "sagemaker:UpdateSpace",
    "sagemaker:DeleteSpace"
    ],
    "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:space/${sagemaker:DomainId}/*",
    "Condition": {
    "Null": {
    "sagemaker:OwnerUserProfileArn": "true"
    }
    }
    },
    {
    "Sid": "SMStudioRestrictSpacesToOwnerUserProfile",
    "Effect": "Allow",
    "Action": [
    "sagemaker:CreateSpace",
    "sagemaker:UpdateSpace",
    "sagemaker:DeleteSpace"
    ],
    "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:space/${sagemaker:DomainId}/*",
    "Condition": {
    "ArnLike": {
    "sagemaker:OwnerUserProfileArn": "arn:aws:sagemaker:us-east-1:`111122223333`:user-profile/${sagemaker:DomainId}/${sagemaker:UserProfileName}"
    },
    "StringEquals": {
    "sagemaker:SpaceSharingType": [
    "Private",
    "Shared"
    ]
    }
    }
    },
    {
    "Sid": "SMStudioRestrictCreatePrivateSpaceAppsToOwnerUserProfile",
    "Effect": "Allow",
    "Action": [
    "sagemaker:CreateApp",
    "sagemaker:DeleteApp"
    ],
    "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:app/${sagemaker:DomainId}/*",
    "Condition": {
    "ArnLike": {
    "sagemaker:OwnerUserProfileArn": "arn:aws:sagemaker:us-east-1:`111122223333`:user-profile/${sagemaker:DomainId}/${sagemaker:UserProfileName}"
    },
    "StringEquals": {
    "sagemaker:SpaceSharingType": [
    "Private"
    ]
    }
    }
    },
    {
    "Sid": "AllowAppActionsForSharedSpaces",
    "Effect": "Allow",
    "Action": [
    "sagemaker:CreateApp",
    "sagemaker:DeleteApp"
    ],
    "Resource": "arn:aws:sagemaker:*:*:app/${sagemaker:DomainId}/*/*/*",
    "Condition": {
    "StringEquals": {
    "sagemaker:SpaceSharingType": [
    "Shared"
    ]
    }
    }
    }
    ]
   }`

   ```

   - Because Studio shows an expanded set of applications, users may
     have access to applications that weren't displayed before.
     Administrators can limit access to these default applications by
     creating an AWS Identity and Access Management (IAM) policy that grants denies permissions for
     some applications to specific users.

   ###### Note

   Application type can be either `jupyterlab` or
   `codeeditor`.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Sid": "DenySageMakerCreateAppForSpecificAppTypes",
    "Effect": "Deny",
    "Action": "sagemaker:CreateApp",
    "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:app/`domain-id`/*/`app-type`/*"
    }
    ]
   }`

   ```

2. Attach the policy to the execution role of the domain. For instructions,
   follow the steps in [Adding IAM identity permissions (console)](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console").

## Step 2: Update VPC configuration

If you use your domain in `VPC-Only` mode, ensure your VPC configuration
meets the requirements for using Studio in `VPC-Only` mode. For more
information, see [Connect Amazon SageMaker Studio
in a VPC to External Resources](studio-updated-and-internet-access.md "studio-updated-and-internet-access.md").

## Step 3: Upgrade to the

Studio UI

Before you migrate your existing domain from Studio Classic to Studio, we recommend
creating a test domain using Studio with the same configurations as your existing
domain.

Use this test domain to interact with Studio, test out networking
configurations, and launch applications, before migrating the existing
domain.

1. Get the domain ID of your existing domain.
   1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
   2. From the left navigation pane, expand **Admin
      configurations** and choose
      **Domains**.
   3. Choose the existing domain.
   4. On the **Domain details** page, choose the
      **Domain settings** tab.
   5. Copy the **Domain ID**.

2. Add the domain ID of your existing domain.

```
export REF_DOMAIN_ID="`domain-id`"
export SM_REGION="`region`"
```

3. Use `describe-domain` to get important information about
   the existing domain.

```
export REF_EXECROLE=$(aws sagemaker describe-domain --region=$SM_REGION --domain-id=$REF_DOMAIN_ID | jq -r '.DefaultUserSettings.ExecutionRole')
export REF_VPC=$(aws sagemaker describe-domain --region=$SM_REGION --domain-id=$REF_DOMAIN_ID | jq -r '.VpcId')
export REF_SIDS=$(aws sagemaker describe-domain --region=$SM_REGION --domain-id=$REF_DOMAIN_ID | jq -r '.SubnetIds | join(",")')
export REF_SGS=$(aws sagemaker describe-domain --region=$SM_REGION --domain-id=$REF_DOMAIN_ID | jq -r '.DefaultUserSettings.SecurityGroups | join(",")')
export AUTHMODE=$(aws sagemaker describe-domain --region=$SM_REGION --domain-id=$REF_DOMAIN_ID | jq -r '.AuthMode')
```

4. Validate the parameters.

```
echo "Execution Role: $REF_EXECROLE || VPCID: $REF_VPC || SubnetIDs: $REF_SIDS || Security GroupIDs: $REF_SGS || AuthMode: $AUTHMODE"
```

5. Create a test domain using the configurations from the existing
   domain.

```
IFS=',' read -r -a subnet_ids <<< "$REF_SIDS"
IFS=',' read -r -a security_groups <<< "$REF_SGS"
security_groups_json=$(printf '%s\n' "${security_groups[@]}" | jq -R . | jq -s .)

aws sagemaker create-domain \
--domain-name "TestV2Config" \
--vpc-id $REF_VPC \
--auth-mode $AUTHMODE \
--subnet-ids "${subnet_ids[@]}" \
--app-network-access-type VpcOnly \
--default-user-settings "
{
    \"ExecutionRole\": \"$REF_EXECROLE\",
    \"StudioWebPortal\": \"ENABLED\",
    \"DefaultLandingUri\": \"studio::\",
    \"SecurityGroups\": $security_groups_json
}
"
```

6. After the test domain is `In Service`, use the test
   domain's ID to create a user profile. This user profile is used to
   launch and test applications.

```
aws sagemaker create-user-profile \
--region="$SM_REGION" --domain-id=`test-domain-id` \
--user-profile-name test-network-user
```

#### Test Studio

functionality

Launch the test domain using the `test-network-user` user
profile. We suggest that you thoroughly test the Studio UI and create
applications to test Studio functionality in `VPCOnly` mode.
Test the following workflows:

- Create a new JupyterLab Space, test environment and
  connectivity.
- Create a new Code Editor, based on Code-OSS, Visual Studio Code - Open Source Space, test environment and
  connectivity.
- Launch a new Studio Classic App, test environment and
  connectivity.
- Test Amazon Simple Storage Service connectivity with test read and write
  actions.

If these tests are successful, then upgrade the existing domain. If you
encounter any failures, we recommended fixing your environment and
connectivity issues before updating the existing domain.

#### Clean up test domain

resources

After you have migrated the existing domain, clean up test domain
resources.

1. Add the test domain's ID.

```
export TEST_DOMAIN="`test-domain-id`"
export SM_REGION="`region`"
```

2. List all applications in the domain that are in a running
   state.

```
active_apps_json=$(aws sagemaker list-apps --region=$SM_REGION --domain-id=$TEST_DOMAIN)
echo $active_apps_json
```

3. Parse the JSON list of running applications and delete them. If
   users attempted to create an application that they do not have
   permissions for, there may be spaces that are not captured in the
   following script. You must manually delete these spaces.

```
echo "$active_apps_json" | jq -c '.Apps[]' | while read -r app;
do
    if echo "$app" | jq -e '. | has("SpaceName")' > /dev/null;
    then
        app_type=$(echo "$app" | jq -r '.AppType')
        app_name=$(echo "$app" | jq -r '.AppName')
        domain_id=$(echo "$app" | jq -r '.DomainId')
        space_name=$(echo "$app" | jq -r '.SpaceName')

        echo "Deleting App - AppType: $app_type || AppName: $app_name || DomainId: $domain_id || SpaceName: $space_name"
        aws sagemaker delete-app --region=$SM_REGION --domain-id=$domain_id \
        --app-type $app_type --app-name $app_name --space-name $space_name

        echo "Deleting Space - AppType: $app_type || AppName: $app_name || DomainId: $domain_id || SpaceName: $space_name"
        aws sagemaker delete-space --region=$SM_REGION --domain-id=$domain_id \
        --space-name $space_name
    else

        app_type=$(echo "$app" | jq -r '.AppType')
        app_name=$(echo "$app" | jq -r '.AppName')
        domain_id=$(echo "$app" | jq -r '.DomainId')
        user_profile_name=$(echo "$app" | jq -r '.UserProfileName')

        echo "Deleting Studio Classic - AppType: $app_type || AppName: $app_name || DomainId: $domain_id || UserProfileName: $user_profile_name"
        aws sagemaker delete-app --region=$SM_REGION --domain-id=$domain_id \
        --app-type $app_type --app-name $app_name --user-profile-name $user_profile_name

    fi

done
```

4. Delete the test user profile.

```
aws sagemaker delete-user-profile \
--region=$SM_REGION --domain-id=$TEST_DOMAIN \
--user-profile-name "test-network-user"
```

5. Delete the test domain.

```
aws sagemaker delete-domain \
--region=$SM_REGION --domain-id=$TEST_DOMAIN
```

After you have tested Studio functionality with the configurations in your test
domain, migrate the existing domain. When Studio is the default experience for a
domain, Studio is the default experience for all users in the domain. However, the
user settings takes precedence over the domain settings. Therefore, if a user has their
default experience set to Studio Classic in their user settings, then that user will have
Studio Classic as their default experience.

You can migrate the existing domain by updating it from the SageMaker AI console, the AWS CLI,
or AWS CloudFormation. Choose one of the following tabs to view the relevant instructions.

You can set Studio as the default experience for the existing domain by
using the SageMaker AI console.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. From the left navigation pane expand **Admin
   configurations** and choose **Domains**.
3. Choose the existing domain that you want to enable Studio as the
   default experience for.
4. On the **Domain details** page expand
   **Enable the new Studio**.
5. (Optional) To view the details about the steps involved in enabling
   Studio as your default experience, choose **View
   details**. The page shows the following.
   - In the **SageMaker Studio Overview** section
     you can view the applications that are included or available in
     the Studio web-based interface.
   - In the **Enablement process** section you can
     view descriptions of the workflow tasks to enable
     Studio.

   ###### Note

   You will need to migrate your data manually. For
   instructions about migrating your data, see [(Optional) Migrate data from
   Studio Classic to Studio](studio-updated-migrate-data.md "studio-updated-migrate-data.md").
   - In the **Revert to Studio Classic
     experience** section you can view how to revert
     back to Studio Classic after enabling Studio as your default
     experience.

6. To begin the process to enable Studio as your default experience,
   choose **Enable the new Studio**.
7. In the **Specify and configure role** section, you
   can view the default applications that are automatically included in
   Studio.

To prevent users from running these applications, choose the AWS Identity and Access Management
(IAM) Role that has an IAM policy that denies access. For
information about how to create a policy to limit access, see [Step 1: Update application creation
permissions](#studio-updated-migrate-limit-apps "#studio-updated-migrate-limit-apps"). 8. In the **Choose default S3 bucket to attach CORS
policy** section, you can give Studio access to Amazon S3
buckets. The default Amazon S3 bucket, in this case, is the default Amazon S3
bucket for your Studio Classic. In this step you can do the
following:

    * Verify the domain’s default Amazon S3 bucket to attach the CORS
     policy to. If your domain does not have a default Amazon S3 bucket,
     SageMaker AI creates an Amazon S3 bucket with the correct CORS policy
     attached.
    * You can include 10 additional Amazon S3 buckets to attach the CORS
     policy to.


    If you wish to include more than 10 buckets, you can add them
     manually. For more information about manually attaching the CORS
     policy to your Amazon S3 buckets, see [(Optional) Update your CORS policy
     to access Amazon S3 buckets](#studio-updated-migrate-cors "#studio-updated-migrate-cors").

To proceed, select the check box next to **Do you agree to
overriding any existing CORS policy on the chosen Amazon S3
buckets?**. 9. The **Migrate data** section contains information
about the different data storage volumes for Studio Classic and Studio.
Your data will not be migrated automatically through this process. For
instructions about migrating your data, lifecycle configurations, and
JupyterLab extensions, see [(Optional) Migrate data from
Studio Classic to Studio](studio-updated-migrate-data.md "studio-updated-migrate-data.md"). 10. Once you have completed the tasks on the page and verified your
configuration, choose **Enable the new Studio**.
To set Studio as the default experience for the existing domain using the
AWS CLI, use the [update-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html") call. You must set `ENABLED` as the value
for `StudioWebPortal`, and set `studio::` as the value for
`DefaultLandingUri` as part of the
`default-user-settings` parameter. 

`StudioWebPortal` indicates if the Studio experience is the
default experience and `DefaultLandingUri` indicates the default
experience that the user is directed to when accessing the domain. In this
example, setting these values on a domain level (in
`default-user-settings`) makes Studio the default experience
for users within the domain.

If a user within the domain has their `StudioWebPortal` set to
`DISABLED` and `DefaultLandingUri` set to
`app:JupyterServer:` on a user level (in
`UserSettings`), this takes precedence over the domain settings.
In other words, that user will have Studio Classic as their default experience,
regardless of the domain settings.

The following code example shows how to set Studio as the default
experience for users within the domain:

```
aws sagemaker update-domain \
--domain-id `existing-domain-id` \
--region `AWS Region` \
--default-user-settings '
{
    "StudioWebPortal": "ENABLED",
    "DefaultLandingUri": "studio::"
}
'
```

- To obtain your
  `existing-domain-id`, use the
  following instructions:

###### To get

`existing-domain-id`

    1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
    2. From the left navigation pane, expand **Admin
     configurations** and choose
     **Domains**.
    3. Choose the existing domain.
    4. On the **Domain details** page, choose the
     **Domain settings** tab.
    5. Copy the **Domain ID**.

- To ensure you are using the correct AWS Region for your domain,
  use the following instructions:

###### To get

`AWS Region`

    1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
    2. From the left navigation pane, expand **Admin
     configurations** and choose
     **Domains**.
    3. Choose the existing domain.
    4. On the **Domain details** page, verify that
     this is the existing domain.
    5. Expand the AWS Region dropdown list from the top right of
     the SageMaker AI console, and use the corresponding AWS Region ID to
     the right of your AWS Region name. For example,
     `us-west-1`.

After you migrate your default experience to Studio, you can give
Studio access to Amazon S3 buckets. For example, you can include access to your
Studio Classic default Amazon S3 bucket and additional Amazon S3 buckets. To do so, you must
manually attach a [Cross-Origin
Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS "https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS") (CORS) configuration to the Amazon S3 buckets. For more
information about how to manually attach the CORS policy to your Amazon S3 buckets,
see [(Optional) Update your CORS policy
to access Amazon S3 buckets](#studio-updated-migrate-cors "#studio-updated-migrate-cors").

Similarly, you can set Studio as the default experience when you create a
domain from the AWS CLI using the [create-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-domain.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-domain.html") call. 

You can set the default experience when creating a domain using the AWS CloudFormation.
For an CloudFormation migration template, see [SageMaker Studio Administrator IaC Templates](https://github.com/aws-samples/sagemaker-studio-admin-iac-templates/tree/main?tab=readme-ov-file#phase-1-migration "https://github.com/aws-samples/sagemaker-studio-admin-iac-templates/tree/main?tab=readme-ov-file#phase-1-migration"). For more information
about creating a domain using CloudFormation, see [Creating Amazon SageMaker AI domain using CloudFormation](https://github.com/aws-samples/cloudformation-studio-domain?tab=readme-ov-file#creating-sagemaker-studio-domains-using-cloudformation "https://github.com/aws-samples/cloudformation-studio-domain?tab=readme-ov-file#creating-sagemaker-studio-domains-using-cloudformation").

For information about the domain resource supported by AWS CloudFormation, see [AWS::SageMaker AI::Domain](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.md#cfn-sagemaker-domain-defaultusersettings "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.md#cfn-sagemaker-domain-defaultusersettings").

After you migrate your default experience to Studio, you can give
Studio access to Amazon S3 buckets. For example, you can include access to your
Studio Classic default Amazon S3 bucket and additional Amazon S3 buckets. To do so, you must
manually attach a [Cross-Origin
Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS "https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS") (CORS) configuration to the Amazon S3 buckets. For
information about how to manually attach the CORS policy to your Amazon S3 buckets,
see [(Optional) Update your CORS policy
to access Amazon S3 buckets](#studio-updated-migrate-cors "#studio-updated-migrate-cors").

In Studio Classic, users can create, list, and upload files to Amazon Simple Storage Service (Amazon S3)
buckets. To support the same experience in Studio, administrators must
attach a [Cross-Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS "https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS") (CORS) configuration to the Amazon S3
buckets. This is required because Studio makes Amazon S3 calls from the internet
browser. The browser invokes CORS on behalf of users. As a result, all of the
requests to Amazon S3 buckets fail unless the CORS policy is attached to the Amazon S3
buckets.

You may need to manually attach the CORS policy to Amazon S3 buckets for the
following reasons.

- If there is already an existing Amazon S3 default bucket that doesn’t have
  the correct CORS policy attached when you migrate the existing domain's
  default experience to Studio.
- If you are using the AWS CLI to migrate the existing domain's default
  experience to Studio. For information about using the AWS CLI to
  migrate, see [Set Studio
  as the default experience for the existing domain using the AWS CLI](#studio-updated-migrate-set-studio-updated-cli "#studio-updated-migrate-set-studio-updated-cli").
- If you want to attach the CORS policy to additional Amazon S3
  buckets.

###### Note

If you plan to use the SageMaker AI console to enable Studio as your default
experience, the Amazon S3 buckets that you attach the CORS policy to will have
their existing CORS policies overridden during the migration. For this
reason, you can ignore the following manual instructions.

However, if you have already used the SageMaker AI console to migrate and want to
include more Amazon S3 buckets to attach the CORS policy to, then continue with
the following manual instructions.

The following procedure shows how to manually add a CORS configuration to an
Amazon S3 bucket.

###### To add a CORS configuration to an Amazon S3 bucket

1. Verify that there is an Amazon S3 bucket in the same AWS Region as the
   existing domain with the following name. For instructions, see [Viewing
   the properties for an Amazon S3 bucket](../../../AmazonS3/latest/userguide/view-bucket-properties.md "../../../AmazonS3/latest/userguide/view-bucket-properties.md").

```
sagemaker-`region`-`account-id`
```

2. Add a CORS configuration with the following content to the default
   Amazon S3 bucket. For instructions, see [Configuring cross-origin resource sharing (CORS)](../../../AmazonS3/latest/userguide/enabling-cors-examples.md "../../../AmazonS3/latest/userguide/enabling-cors-examples.md").

```
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "POST",
            "PUT",
            "GET",
            "HEAD",
            "DELETE"
        ],
        "AllowedOrigins": [
            "https://*.sagemaker.aws"
        ],
        "ExposeHeaders": [
            "ETag",
            "x-amz-delete-marker",
            "x-amz-id-2",
            "x-amz-request-id",
            "x-amz-server-side-encryption",
            "x-amz-version-id"
        ]
    }
]
```

Amazon SageMaker Data Wrangler exists as its own feature in the Studio Classic experience. When you
enable Studio as your default experience, use the [Amazon SageMaker Canvas](canvas.md "canvas.md")
application to access Data Wrangler functionality. SageMaker Canvas is an application in which you
can train and deploy machine learning models without writing any code, and
Canvas provides data preparation features powered by Data Wrangler.

The new Studio experience doesn’t support the classic Data Wrangler UI, and you
must create a Canvas application if you want to continue using Data Wrangler.
However, you must have the necessary permissions to create and use Canvas
applications.

Complete the following steps to attach the necessary permissions policies to
your SageMaker AI domain's or user’s AWS IAM role.

###### To grant permissions for Data Wrangler functionality inside Canvas

1. Attach the AWS managed policy [AmazonSageMakerFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess") to your user’s IAM role. For a
   procedure that shows you how to attach IAM policies to a role, see
   [Adding IAM identity permissions (console)](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console") in the
   _AWS IAM User Guide._

If this permissions policy is too permissive for your use case, you
can create scoped-down policies that include at least the following
permissions:

```
{
    "Sid": "AllowStudioActions",
    "Effect": "Allow",
    "Action": [
        "sagemaker:CreatePresignedDomainUrl",
        "sagemaker:DescribeDomain",
        "sagemaker:ListDomains",
        "sagemaker:DescribeUserProfile",
        "sagemaker:ListUserProfiles",
        "sagemaker:DescribeSpace",
        "sagemaker:ListSpaces",
        "sagemaker:DescribeApp",
        "sagemaker:ListApps"
    ],
    "Resource": "*"
},
{
    "Sid": "AllowAppActionsForUserProfile",
    "Effect": "Allow",
    "Action": [
        "sagemaker:CreateApp",
        "sagemaker:DeleteApp"
    ],
    "Resource": "arn:aws:sagemaker:`region`:`account-id`:app/`domain-id`/`user-profile-name`/canvas/*",
    "Condition": {
        "Null": {
            "sagemaker:OwnerUserProfileArn": "true"
        }
    }
}
```

2. Attach the AWS managed policy [AmazonSageMakerCanvasDataPrepFullAccess](../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasDataPrepFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasDataPrepFullAccess.md") to your user’s
   IAM role.
   After attaching the necessary permissions, you can create a Canvas
   application and log in. For more information, see [Getting started with using Amazon SageMaker Canvas](canvas-getting-started.md "canvas-getting-started.md").

When you’ve logged into Canvas, you can directly access Data Wrangler and begin
creating data flows. For more information, see [Data preparation](canvas-data-prep.md "canvas-data-prep.md") in the Canvas documentation.

[Amazon SageMaker Autopilot](../../AWSIronmanApiDoc/integ/npepin-studio-migration-autopilot-to-canvas/latest/dg/autopilot-automate-model-development.md "../../AWSIronmanApiDoc/integ/npepin-studio-migration-autopilot-to-canvas/latest/dg/autopilot-automate-model-development.md") exists as its own feature in the Studio Classic experience. When
you migrate to using the updated Studio experience, use the [Amazon SageMaker Canvas](canvas.md "canvas.md")
application to continue using the same automated machine learning (AutoML)
capabilities via a user interface (UI). SageMaker Canvas is an application in which you can
train and deploy machine learning models without writing any code, and
Canvas provides a UI to run your AutoML tasks.

The new Studio experience doesn’t support the classic Autopilot UI. You must
create a Canvas application if you want to continue using Autopilot's AutoML
features via a UI.

However, you must have the necessary permissions to create and use Canvas
applications.

- If you are accessing SageMaker Canvas from Studio, add those permissions to
  the execution role of your SageMaker AI domain or user profile.
- If you are accessing SageMaker Canvas from the Console, add those permissions to
  your user’s AWS IAM role.
- If you are accessing SageMaker Canvas via a [presigned URL](setting-up-canvas-sso.md#canvas-optional-access "setting-up-canvas-sso.md#canvas-optional-access"), add those permissions to the IAM role that
  you're using for Okta SSO access.
  To enable AutoML capabilities in Canvas, add the following policies to
  your execution role or IAM user role.

- AWS managed policy: [`CanvasFullAccess`.](security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasFullAccess "security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasFullAccess")
- Inline policy:

```
{
    "Sid": "AllowAppActionsForUserProfile",
    "Effect": "Allow",
    "Action": [
        "sagemaker:CreateApp",
        "sagemaker:DeleteApp"
    ],
    "Resource": "arn:aws:sagemaker:`region`:`account-id`:app/`domain-id`/`user-profile-name`/canvas/*",
    "Condition": {
        "Null": {
            "sagemaker:OwnerUserProfileArn": "true"
        }
    }
}
```

###### To attach IAM policies to an execution role

1.  ###### Find the execution role attached to your SageMaker AI user profile
    1. In the SageMaker AI console [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/"),
       navigate to **Domains**, then choose your SageMaker AI
       domain.
    2. The execution role ARN is listed under _Execution role_ on the **User
       Details** page of your user profile. Make note of
       the execution role name in the ARN.
    3. In the IAM console [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"), choose
       **Roles**.
    4. Search for your role by name in the search field.
    5. Select the role.

2.  Add policies to the role

        1. In the IAM console [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"), choose
         **Roles**.
        2. Search for your role by name in the search field.
        3. Select the role.
        4. In the **Permissions** tab, navigate to the
         dropdown menu **Add permissions**.
        5. * For managed policies: Select **Attach
        	 policies**, search for the name of the
        	 manage policy you want to attach.


        	Select the policy then choose **Add
        	 permissions**.
        	* For inline policies: Select **Create inline
        	 policy**, paste your policy in the JSON
        	 tab, choose next, name your policy, and choose
        	 **Create**.

    For a procedure that shows you how to attach IAM policies to a role, see
    [Adding IAM identity permissions (console)](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console") in the _AWS IAM User Guide._

After attaching the necessary permissions, you can create a Canvas
application and log in. For more information, see [Getting started with using Amazon SageMaker Canvas](canvas-getting-started.md "canvas-getting-started.md").

## Set Studio Classic as the default

experience

Administrators can revert to Studio Classic as the default experience for an existing
domain. This can be done through the AWS CLI.

###### Note

When Studio Classic is set as the default experience on a domain level, Studio Classic
is the default experience for all users in the domain. However, settings on a
user level takes precedence over the domain level settings. So if a user has
their default experience set to Studio, then that user will have Studio as
their default experience.

To revert to Studio Classic as the default experience for the existing domain using
the AWS CLI, use the [update-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html") call. As part of the `default-user-settings`
field, you must set:

- `StudioWebPortal` value to `DISABLED`.
- `DefaultLandingUri` value to `app:JupyterServer:`

`StudioWebPortal` indicates if the Studio experience is the default
experience and `DefaultLandingUri` indicates the default experience that the
user is directed to when accessing the domain. In this example, setting these values
on a domain level (in `default-user-settings`) makes Studio Classic the
default experience for users within the domain.

If a user within the domain has their `StudioWebPortal` set to
`ENABLED` and `DefaultLandingUri` set to `studio::`
on a user level (in `UserSettings`), this takes precedence over the
domain level settings. In other words, that user will have Studio as their
default experience, regardless of the domain level settings.

The following code example shows how to set Studio Classic as the default experience for
users within the domain:

```
aws sagemaker update-domain \
--domain-id `existing-domain-id` \
--region `AWS Region` \
--default-user-settings '
{
    "StudioWebPortal": "DISABLED",
    "DefaultLandingUri": "app:JupyterServer:"
}
'
```

Use the following instructions to obtain your
`existing-domain-id`.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. From the left navigation pane, expand **Admin
   configurations** and choose **Domains**.
3. Choose the existing domain.
4. On the **Domain details** page, choose the **Domain
   settings** tab.
5. Copy the **Domain ID**.

To obtain your `AWS Region`, use the following
instructions to ensure you are using the correct AWS Region for your
domain.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. From the left navigation pane, expand **Admin
   configurations** and choose **Domains**.
3. Choose the existing domain.
4. On the **Domain details** page, verify that this is the
   existing domain.
5. Expand the AWS Region dropdown list from the top right of the SageMaker AI console,
   and use the corresponding AWS Region ID to the right of your AWS Region
   name. For example, `us-west-1`.
