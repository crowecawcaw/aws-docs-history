# Change the default storage

size for your JupyterLab users

You can change the default storage settings for your users. You can also change the
default storage settings based on your organizational requirements and the needs of your
users.

To change the storage size, this section provides commands to do the following:

1. Update the Amazon EBS storage settings in the Amazon SageMaker AI domain (domain).
2. Create a user profile and specify the storage settings within it.
   Use the following AWS Command Line Interface (AWS CLI) commands to change the default storage
   size.

Use the following AWS CLI command to update the domain:

```
aws --region `AWS Region` sagemaker update-domain \
--domain-id `domain-id` \
--default-user-settings '{
    "SpaceStorageSettings": {
        "DefaultEbsStorageSettings":{
            "DefaultEbsVolumeSizeInGb":5,
            "MaximumEbsVolumeSizeInGb":100
        }
    }
}'
```

Use the following AWS CLI command to create the user profile and specify the default
storage settings:

```
aws --region `AWS Region` sagemaker create-user-profile \
--domain-id `domain-id` \
--user-profile-name `user-profile-name` \
--user-settings '{
    "SpaceStorageSettings": {
        "DefaultEbsStorageSettings":{
            "DefaultEbsVolumeSizeInGb":5,
            "MaximumEbsVolumeSizeInGb":100
        }
    }
}'
```

Use the following AWS CLI commands to update the default storage settings in the user
profile:

```
aws --region `AWS Region` sagemaker update-user-profile \
--domain-id `domain-id` \
--user-profile-name `user-profile-name` \
--user-settings '{
    "SpaceStorageSettings": {
        "DefaultEbsStorageSettings":{
            "DefaultEbsVolumeSizeInGb":25,
            "MaximumEbsVolumeSizeInGb":200
        }
    }
}'
```
