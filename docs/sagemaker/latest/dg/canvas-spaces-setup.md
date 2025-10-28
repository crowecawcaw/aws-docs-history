# Store SageMaker Canvas application data in your own SageMaker AI

space

Your Amazon SageMaker Canvas application data, such as datasets that you import and your model
artifacts, is stored in a _Amazon SageMaker Studio private space_.
The space consists of a storage volume for your application data with 100 GB of storage per
user profile, the type of the space (in this case, a Canvas application), and the image
for your application's container. When you set up Canvas and launch your application for
the first time, SageMaker AI creates a default private space that is assigned to your user profile
and stores your Canvas data. You don't have to do any additional configuration to set up
the space because SageMaker AI automatically creates the space on your behalf. However, if you don't
want to use the default space, you have the option to specify a
space that you created yourself. This can be useful if you want to isolate your data. The
following page shows you how to create and configure your own Studio
space for storing Canvas application data.

###### Note

You can only configure a custom Studio space for new Canvas
applications. You can't modify the space configuration for existing Canvas
applications.

## Before you begin

Your Amazon SageMaker AI domain or user profile must have at least 100 GB of storage in order to
create and use the SageMaker Canvas application.

If you created your domain through the SageMaker AI console, enough storage is provisioned
by default and you don't need to take any additional action. If you created your
domain or user profile with the [CreateDomain](../APIReference/API_CreateDomain.md "../APIReference/API_CreateDomain.md") or
[CreateUserProfile](../APIReference/API_CreateUserProfile.md "../APIReference/API_CreateUserProfile.md") APIs, then make sure that you set the
`MaximumEbsVolumeSizeInGb` value to 100 GB or greater. To set a greater
storage value, you can either create a new domain or user profile, or you can update
an existing domain or user profile using the [UpdateDomain](../APIReference/API_UpdateDomain.md "../APIReference/API_UpdateDomain.md") or
[UpdateUserProfile](../APIReference/API_UpdateUserProfile.md "../APIReference/API_UpdateUserProfile.md") APIs.

## Create a new space

First, create a new Studio space that is configured to
store Canvas application data. This is the space that you specify when creating a new
Canvas application in the next step.

To create a space, you can use the AWS SDK for Python (Boto3) or the
AWS CLI.

SDK for Python (Boto3)
The following example shows you how to use the AWS SDK for Python (Boto3) `create_space`
method to create a space that you can use
for Canvas applications. Make sure to specify these parameters:

- `DomainId`: Specify the ID for your SageMaker AI domain. To find
  your ID, you can go to the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/") and locate your domain
  in the **Domains** section.
- `SpaceName`: Specify a name for the new space.
- `EbsVolumeSizeinGb`: Specify the storage volume size
  for your space (in GB). The minimum value is `5` and the maximum is
  `16384`.
- `SharingType`: Specify this field as
  `Private`. For more information, see
  [Amazon SageMaker Studio spaces](studio-updated-spaces.md "studio-updated-spaces.md").
- `OwnerUserProfileName`: Specify the user profile name.
  To find user profile names associated with a domain, you can go to
  the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/") and locate your domain in the **Domains** section.
  In the domain's settings, you can view the user profiles.
- `AppType`: Specify this field as
  `Canvas`.

```

response = client.create_space(
    DomainId='<your-domain-id>',
    SpaceName='<your-new-space-name>',
    SpaceSettings={
        'AppType': 'Canvas',
        'SpaceStorageSettings': {
            'EbsStorageSettings': {
                'EbsVolumeSizeInGb': <storage-volume-size>
            }
        },
    },
    OwnershipSettings={
        'OwnerUserProfileName': '<your-user-profile>'
    },
    SpaceSharingSettings={
        'SharingType': 'Private'
    }
)

```

AWS CLI
The following example shows you how to use the AWS CLI `create-space`
method to create a space that you can use for Canvas
applications. Make sure to specify these parameters:

- `domain-id`: Specify the ID for your domain. To find
  your ID, you can go to the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/") and locate your domain
  in the **Domains** section.
- `space-name`: Specify a name for the new space.
- `EbsVolumeSizeinGb`: Specify the storage volume size
  for your space (in GB). The minimum value is `5` and the maximum is
  `16384`.
- `SharingType`: Specify this field as
  `Private`. For more information, see
  [Amazon SageMaker Studio spaces](studio-updated-spaces.md "studio-updated-spaces.md").
- `OwnerUserProfileName`: Specify the user profile name.
  To find user profile names associated with a domain, you can go
  to the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/") and locate your domain
  in the **Domains** section. In the domain's
  settings, you can view the user profiles.
- `AppType`: Specify this field as
  `Canvas`.

```

create-space
--domain-id <your-domain-id>
--space-name <your-new-space-name>
--space-settings '{
        "AppType": "Canvas",
        "SpaceStorageSettings": {
            "EbsStorageSettings": {"EbsVolumeSizeInGb": <storage-volume-size>}
        },
     }'
--ownership-settings '{"OwnerUserProfileName": "<your-user-profile>"}'
--space-sharing-settings '{"SharingType": "Private"}'

```

You should now have a space. Keep track of your space's name for the next step.

## Create a new Canvas application

After creating a space, create a new Canvas application that specifies the space as
its storage location.

To create a new Canvas application, you can use the AWS SDK for Python (Boto3) or the AWS CLI.

###### Important

You must use the AWS SDK for Python (Boto3) or the AWS CLI to create your Canvas application.
Specifying a custom space when creating Canvas applications through the SageMaker AI console isn't
supported.

SDK for Python (Boto3)
The following example shows you how to use the AWS SDK for Python (Boto3) `create_app`
method to create a new Canvas application.
Make sure to specify these parameters:

- `DomainId`: Specify the ID for your SageMaker AI domain.
- `SpaceName`: Specify the name of the space that you
  created in the previous step.
- `AppType`: Specify this field as
  `Canvas`.
- `AppName`: Specify `default` as the app
  name.

```

response = client.create_app(
    DomainId='<your-domain-id>',
    SpaceName='<your-space-name>',
    AppType='Canvas',
    AppName='default'
)

```

AWS CLI
The following example shows you how to use the AWS CLI
`create-app` method to create a new Canvas application. Make sure
to specify these parameters:

- `DomainId`: Specify the ID for your SageMaker AI domain.
- `SpaceName`: Specify the name of the space that you
  created in the previous step.
- `AppType`: Specify this field as
  `Canvas`.
- `AppName`: Specify `default` as the app
  name.

```
create-app
--domain-id <your-domain-id>
--space-name <your-space-name>
--app-type Canvas
--app-name default
```

You should now have a new Canvas application that uses a custom Studio space
as the storage location for application data.

###### Important

Any time you delete the Canvas application (or log out)
and have to re-create the application, you must provide your space in the `SpaceName`
field to make sure that Canvas uses your space.

The space is attached to the user profile you specified in the space configuration.
You can delete your Canvas application without deleting the space, and the data stored
in the space remains. The data stored in your space is only deleted if you delete your
user profile, or if you directly delete the space.
