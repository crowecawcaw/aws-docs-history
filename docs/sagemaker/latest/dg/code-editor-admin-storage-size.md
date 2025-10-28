# Change the default storage size

You can change the default storage settings of your users. You can also change the
default storage settings based on your organizational requirements and the needs of your
users.

To change the storage size of your users, do the following:

1. Update the Amazon EBS storage settings in the domain.
2. Create a user profile and specify the storage settings within it.
   Use the following AWS Command Line Interface (AWS CLI) command to update the domain.

```
aws --region $REGION sagemaker update-domain \
--domain-id $DOMAIN_ID \
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
storage settings.

```
aws --region $REGION sagemaker create-user-profile \
--domain-id $DOMAIN_ID \
--user-profile-name $USER_PROFILE_NAME \
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
profile.

```
aws --region $REGION sagemaker update-user-profile \
--domain-id $DOMAIN_ID \
--user-profile-name $USER_PROFILE_NAME \
--user-settings '{
    "SpaceStorageSettings": {
        "DefaultEbsStorageSettings":{
            "DefaultEbsVolumeSizeInGb":25,
            "MaximumEbsVolumeSizeInGb":200
        }
    }
}'
```
