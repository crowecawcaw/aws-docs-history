# Creating a repository creation

template in Amazon ECR

You can create a repository creation template to define the settings to use for
repositories created by Amazon ECR on your behalf during pull through cache or replication
actions. Once the repository creation template is created, all new repositories created
will have the settings applied. This doesn't have any effect on any previously created
repositories.

When setting up a repository with templates, you have the option to specify KMS keys
and resource tags. If you intend to use KMS keys, resource tags, or a combination of
both in one or more templates, you need to:

- [Create a custom policy for
  repository creation templates](repository-creation-templates-custom.md "repository-creation-templates-custom.md").
- [Create an IAM role for
  repository creation templates](repository-creation-templates-create-iam.md "repository-creation-templates-create-iam.md").
  Once configured, you can attach the custom role to specific templates in your
  registry.

## IAM permissions for creating

repository creation templates

The following permissions are needed for an IAM principal to manage repository
creation templates. These permission must be granted using an identity-based IAM
policy.

- `ecr:CreateRepositoryCreationTemplate` – Grants
  permission to create a repository creation template.
- `ecr:UpdateRepositoryCreationTemplate` – Grants
  permission to update a repository creation template.
- `ecr:DescribeRepositoryCreationTemplates` – Grants
  permission to list repository creation templates in a registry.
- `ecr:DeleteRepositoryCreationTemplate` – Grants
  permission to delete a repository creation template.
- `ecr:CreateRepository` – Grants permission to create an
  Amazon ECR repository.
- `ecr:PutLifecyclePolicy` – Grants permission to create a
  lifecycle policy and apply it to a repository. This permission is only
  required if the repository creation template includes a lifecycle
  policy.
- `ecr:SetRepositoryPolicy` – Grants permission to create
  a permissions policy for a repository. This permission is only required if
  the repository creation template includes a repository policy.
- `iam:PassRole` – Grants permission to allow an
  entity to pass a role to a service or application. This permission is
  necessary for services and applications that need to assume a role to
  perform actions on your behalf.

## Create a repository

creation template

Once you've completed the necessary prerequisites for your templates, you can
proceed to create the repository creation templates.

AWS Management Console

###### To create a repository creation template (AWS Management Console)

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/ "https://console.aws.amazon.com/ecr/").
2. From the navigation bar, choose the Region to create the
   repository creation template in.
3. In the navigation pane, choose **Private
   registry**, **Repository creation
   templates**.
4. On the **Repository creation templates**
   page, choose **Create template**.
5. On the **Step 1: Define template** page, for
   **Template details**, choose **A
   specific prefix** to apply the template to a
   specific repository namespace prefix or choose **Any
   prefix in your ECR registry** to apply the template
   to all repositories that don't match any other template in the
   Region.
   1. If you choose **A specific prefix**,
      for **Prefix** specify the repository
      namespace prefix to apply the template to. There is
      always an assumed `/` applied to the end of
      the prefix. For example, a prefix of `prod`
      would apply to all repositories beginning with
      `prod/`. Similarly, a prefix of
      `prod/team` would apply to all
      repositories beginning with `prod/team/`.
   2. If you choose **Any prefix in your ECR
      registry**, the **Prefix**
      will be set to `ROOT`.

6. For **Applied for**, specify which Amazon ECR
   workflows this template will apply to. The options are
   `PULL_THROUGH_CACHE` and
   `REPLICATION`.
7. For **Template description**, specify an
   optional description for the template and then choose
   **Next**.
8. On the **Step 2: Add repository creation
   configuration** page, specify the repository
   setting configuration to apply to repositories created using the
   template.
   1. For **Image tag mutability**, choose
      the tag mutability setting to use. For more information,
      see [Preventing image tags from being overwritten in
      Amazon ECR](image-tag-mutability.md "image-tag-mutability.md").
      - **Mutable** – Choose
        this option if you want image tags to be
        overwritten. Recommended for repositories using
        pull through cache actions to ensure Amazon ECR can
        update cached images. Additionally, to disable tag
        updates for a few mutable tags, enter tag names or
        use wildcards (\*) to match multiple similar tags
        in the **Mutable tag exclusion**
        text box.
      - **Immutable** – Choose
        this option if you want to prevent image tags from
        being overwritten, and it applies to all tags and
        exclusions in the repository when pushing an image
        with existing tag. Amazon ECR returns an
        `ImageTagAlreadyExistsException` if you
        attempt to push an image with an existing tag.
        Additionally, to enable tag updates for a few
        immutable tags, enter tag names or use wildcards
        (\*) to match multiple similar tags in the
        **Immutable tag exclusion** text
        box.

   2. For **Encryption configuration**,
      choose the encryption setting to use. For more
      information, see [Encryption at rest](encryption-at-rest.md "encryption-at-rest.md").

   When **AES-256** is selected, Amazon ECR
   uses server-side encryption with Amazon Simple Storage Service-managed
   encryption keys which encrypts your data at rest using
   an industry standard AES-256 encryption algorithm. This
   is offered at no additional cost.

   When **AWS KMS** is selected, Amazon ECR
   uses server-side encryption with keys stored in
   AWS Key Management Service (AWS KMS). When you use AWS KMS to encrypt your
   data, you can either use the default AWS managed key,
   which is managed by Amazon ECR, or specify your own AWS KMS
   key, which is referred to as a _customer
   managed key_.

   ###### Note

   The encryption settings for a repository can't be
   changed once the repository is created. 3. For **Repository permissions**,
   specify the repository permissions policy to apply to
   repositories created using this template. You can
   optionally use the drop down to select one of the JSON
   samples for the most common use cases. For more
   information, see [Private repository policies in Amazon ECR](repository-policies.md "repository-policies.md"). 4. For **Repository lifecycle policy**,
   specify the repository lifecycle policy to apply to
   repositories created using this template. You can
   optionally use the drop down to select one of the JSON
   samples for the most common use cases. For more
   information, see [Automate the cleanup of images by using lifecycle
   policies in Amazon ECR](LifecyclePolicies.md "LifecyclePolicies.md"). 5. For **Repository AWS tags**,
   specify the metadata, in the form of key-value pairs, to
   associate with the repositories created using this
   template and then choose **Next**. For
   more information, see [Tagging a private repository in Amazon ECR](ecr-using-tags.md "ecr-using-tags.md"). 6. For **Repository creation role**,
   select a custom IAM role from the drop-down menu to be
   used for repository creation templates when using
   repository tags or KMS in the template (see [Create an IAM role for
   repository creation templates](repository-creation-templates-create-iam.md "repository-creation-templates-create-iam.md") for details).Then choose
   **Next**.

9. On the **Step 3: Review and create** page,
   review the settings you specified for the repository creation
   template. Choose the **Edit** option to make
   changes. Choose **Create** once you're
   done.

AWS CLI
The [create-repository-creation-template](../../../cli/latest/reference/ecr/create-repository-creation-template.md "../../../cli/latest/reference/ecr/create-repository-creation-template.md") AWS CLI command is used
to create a repository creation template for your private
registry.

###### To create a repository creation template (AWS CLI)

1. Use the AWS CLI to generate a skeleton for the [create-repository-creation-template](../../../cli/latest/reference/ecr/create-repository-creation-template.md "../../../cli/latest/reference/ecr/create-repository-creation-template.md") command.

```
`aws ecr create-repository-creation-template \
 --generate-cli-skeleton`
```

The output of the command displays the full syntax of the
repository creation template.

```
{
"appliedFor":[""], // string array, but valid are PULL_THROUGH_CACHE and REPLICATION
"prefix": "string",
    "description": "string",
    "imageTagMutability": "MUTABLE"|"IMMUTABLE"|"IMMUTABLE_WITH_EXCLUSION"|"MUTABLE_WITH_EXCLUSION",
    "imageTagMutabilityExclusionFilters": [
        "filterType": "WILDCARD",
        "filter": "string"
    ],
    "repositoryPolicy": "string",
    "lifecyclePolicy": "string"
"encryptionConfiguration": {
"encryptionType": "AES256"|"KMS",
        "kmsKey": "string"
    },
    "resourceTags": [
        {
"Key": "string",
            "Value": "string"
        }
    ],
    "customRoleArn": "string", // must be a valid IAM Role ARN
}
```

2. Create a file named
   `repository-creation-template.json` with the
   output of the previous step. This template sets a KMS encryption
   key for any repository created under `prod/*` with a
   repository policy that enables pushing and pulling images to
   future repositories, sets a lifecycle policy that will expire
   images older than two weeks and sets a custom role that will let
   ECR access the KMS key and assign the resource tag
   `examplekey` to future repositories.

```
{
"prefix": "prod",
    "description": "For repositories cached from my PTC rule and in my replication configuration that start with 'prod/'",
    "appliedFor": ["PULL_THROUGH_CACHE","REPLICATION"],
    "encryptionConfiguration": {
"encryptionType": "KMS",
        "kmsKey": "arn:aws:kms:us-west-2:111122223333:key/a1b2c3d4-5678-90ab-cdef-example11111"
    },
    "resourceTags": [
        {
"Key": "examplekey",
            "Value": "examplevalue"
        }
    ],
    "imageTagMutability": "IMMUTABLE_WITH_EXCLUSION",
    "imageTagMutabilityExclusionFilters": [
      {
      "filterType": "WILDCARD",
      "filter": "latest"
      },
      {
      "filterType": "WILDCARD",
      "filter": "beta*"
      }
    ]
    "repositoryPolicy": "{\"Version\":\"2012-10-17\",		 	 	 \"Statement\":[{\"Sid\":\"AllowPushPullIAMRole\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::111122223333:user\/IAMusername\"},\"Action\":[\"ecr:BatchGetImage\",\"ecr:BatchCheckLayerAvailability\",\"ecr:CompleteLayerUpload\",\"ecr:GetDownloadUrlForLayer\",\"ecr:InitiateLayerUpload\",\"ecr:PutImage\",\"ecr:UploadLayerPart\"]}]}",
    "lifecyclePolicy": "{\"rules\":[{\"rulePriority\":1,\"description\":\"Expire images older than 14 days\",\"selection\":{\"tagStatus\":\"any\",\"countType\":\"sinceImagePushed\",\"countUnit\":\"days\",\"countNumber\":14},\"action\":{\"type\":\"expire\"}}]}",
    "customRoleArn": "arn:aws:iam::111122223333:role/myRole"
}
```

3. Use the following command to create a repository creation
   template. Ensure that you specify the name of the configuration
   file created in the previous step in place of the
   `repository-creation-template.json` in the
   following example.

```
`aws ecr create-repository-creation-template \
 --cli-input-json file://`repository-creation-template.json``
```
