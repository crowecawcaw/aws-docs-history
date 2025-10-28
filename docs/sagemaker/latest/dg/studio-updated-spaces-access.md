# Launch spaces

The following sections give information about accessing spaces in a domain. Spaces can
be accessed in one of the following ways:

- from the
  Amazon SageMaker AI console
- from
  Studio
- using the
  AWS CLI

###### To access spaces from the Amazon SageMaker AI console

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Under **Admin configurations**, choose
   **Domains**.
3. From the list of domains, select the domain that contains the
   spaces.
4. On the **Domain details** page, select the
   **Space management** tab. For more information
   about managing spaces, see [Collaboration with shared spaces](domain-space.md "domain-space.md").
5. From the list of spaces for that domain, select the space to
   launch.
6. Choose **Launch Studio** for the space that you want
   to launch.
   Follow these steps to access spaces from Studio for a specific
   application type.

###### To access spaces from Studio

1. Open Studio by following the steps in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. Select the application type with spaces that you want to
   access.
   The following sections show how to access a space from the AWS Command Line Interface (AWS CLI).
   The procedures are for domains that use AWS Identity and Access Management (IAM) or AWS IAM Identity Center
   authentication.

### IAM

authentication

The following procedure outlines generally how to access a space using
IAM authentication from the AWS CLI.

1. Create a presigned domain URL specifying the name of the space
   that you want to access.

```
aws \
    --region `region` \
    sagemaker \
    create-presigned-domain-url \
    --domain-id `domain-id` \
    --user-profile-name `user-profile-name` \
    --space-name `space-name`
```

2. Navigate to the URL.

### Accessing a

space in IAM Identity Center authentication

The following procedure outlines how to access a space using IAM Identity Center
authentication from the AWS CLI.

1. Use the following command to return the URL associated with the
   space.

```
aws \
    --region `region` \
    sagemaker \
    describe-space \
    --domain-id `domain-id` \
    --space-name `space-name`
```

2. Append the respective redirect parameter for the application type
   to the URL to be federated through IAM Identity Center. For more information about
   the redirect parameters, see [describe-space](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-space.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-space.html").
3. Navigate to the URL to be federated through IAM Identity Center.
