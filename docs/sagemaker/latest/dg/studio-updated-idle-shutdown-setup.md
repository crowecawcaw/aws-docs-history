# Set up idle shutdown

The following sections show how to set up idle shutdown from either the console or using the
AWS CLI. Idle shutdown can be set at either the domain or user profile level.

## Prerequisites

To use idle shutdown with your application, you must complete the following prerequisites.

- Ensure that your application is using the SageMaker Distribution (SMD) version
  2.0. You can select this version during application creation or update the image version
  of the application after creation. For more information, see [Update the SageMaker
  Distribution Image](studio-updated-jl-update-distribution-image.md "studio-updated-jl-update-distribution-image.md") .
- For applications built with custom images, idle shutdown is supported if your custom image
  is created with SageMaker Distribution (SMD) version 2.0 or later as the base image. If the
  custom image is created with a different base image, then you must install the [jupyter-activity-monitor-extension >= 0.3.1](https://anaconda.org/conda-forge/jupyter-activity-monitor-extension "https://anaconda.org/conda-forge/jupyter-activity-monitor-extension") extension on the image and attach
  the image to your Amazon SageMaker AI domain for JupyterLab applications. For more information about
  custom images, see [Bring your own image (BYOI)](studio-updated-byoi.md "studio-updated-byoi.md").

## From the Console

The following sections show how to enable idle shutdown from the console.

### Add when creating a new domain

1. Create a domain by following the steps in [Use custom setup for Amazon SageMaker AI](onboard-custom.md "onboard-custom.md")
2. When configuring the application settings in the domain, navigate to either the Code Editor or
   JupyterLab section.
3. Select **Enable idle shutdown**.
4. Enter a default idle shutdown time in minutes. This values defaults to `10,080` if no value
   is entered.
5. (Optional) Select **Allow users to set custom idle shutdown time** to allow users to modify the
   idle shutdown time.
   - Enter a maximum value that users can set the default idle shutdown time to. You must
     enter a maximum value. The minimum value is set by Amazon SageMaker AI and must be
     `60`.

### Add to an existing domain

###### Note

If idle shutdown is set when applications are running, they must be restarted for idle
shutdown settings to take effect.

1. Navigate to the domain.
2. Choose the **App Configurations** tab.
3. From the **App Configurations** tab, navigate to either the Code Editor or
   JupyterLab section.
4. Select **Edit**.
5. Select **Enable idle shutdown**.
6. Enter a default idle shutdown time in minutes. This values defaults to
   `10,080` if no value is entered.
7. (Optional) Select **Allow users to set custom idle shutdown time** to
   allow users to modify the idle shutdown time.
   - Enter a maximum value that users can set the default idle shutdown time to. You must
     enter a maximum value. The minimum value is set by Amazon SageMaker AI and must be
     `60`.

8. Select **Submit**.

### Add when creating a new user profile

1. Add a user
   profile by following the steps at [Add user profiles](domain-user-profile-add.md "domain-user-profile-add.md")
2. When configuring the application settings for the user profile, navigate to either the
   Code Editor or JupyterLab section.
3. Select **Enable idle shutdown**.
4. Enter a default idle shutdown time in minutes. This values defaults to
   `10,080` if no value is entered.
5. (Optional) Select **Allow users to set custom idle shutdown time** to
   allow users to modify the idle shutdown time.
   - Enter a maximum value that users can set the default idle shutdown time to. You must
     enter a maximum value. The minimum value is set by Amazon SageMaker AI and must be
     `60`.

6. Select “Save Changes”.

### Add to an existing user profile

Note: If idle shutdown is set when applications are running, they must be restarted for idle
shutdown settings to take effect.

1. Navigate to the user profile.
2. Choose the **App Configurations** tab.
3. From the \***\*App Configurations\*\*** tab, navigate to
   either the Code Editor or JupyterLab section.
4. Select **Edit**.
5. Idle shutdown settings will show domain settings by default if configured for the domain.
6. Select **Enable idle shutdown**.
7. Enter a default idle shutdown time in minutes. This values defaults to
   `10,080` if no value is entered.
8. (Optional) Select **Allow users to set custom idle shutdown time** to
   allow users to modify the idle shutdown time.
   - Enter a maximum value that users can set the default idle shutdown time to. You must
     enter a maximum value. The minimum value is set by Amazon SageMaker AI and must be
     `60`.

9. Select **Save Changes**.

## From the AWS CLI

The following sections show how to enable idle shutdown using the AWS CLI.

###### Note

To enforce a specific timeout value from the AWS CLI, you must set
`IdleTimeoutInMinutes`, `MaxIdleTimeoutInMinutes`, and
`MinIdleTimeoutInMinutes` to the same value.

### Domain

The following command shows how to enable idle shutdown when updating an existing domain. To add
idle shutdown for a new domain, use the `create-domain` command instead.

###### Note

If idle shutdown is set when applications are running, they must be restarted for idle
shutdown settings to take effect.

```
aws sagemaker update-domain --region `region` --domain-id `domain-id` \
--default-user-settings file://default-user-settings.json

## default-user-settings.json example for enforcing the default timeout
{
    "JupyterLabAppSettings": {
        "AppLifecycleManagement": {
            "IdleSettings": {
                "LifecycleManagement": "ENABLED",
                "IdleTimeoutInMinutes": 120,
                "MaxIdleTimeoutInMinutes": 120,
                "MinIdleTimeoutInMinutes": 120
        }
    }
}

## default-user-settings.json example for letting users customize the default timeout, between 2-5 hours
{
    "JupyterLabAppSettings": {
        "AppLifecycleManagement": {
            "IdleSettings": {
                "LifecycleManagement": "ENABLED",
                "IdleTimeoutInMinutes": 120,
                "MinIdleTimeoutInMinutes": 120,
                "MaxIdleTimeoutInMinutes": 300
        }
    }
}
```

### User profile

The following command shows how to enable idle shutdown when updating an existing user profile. To
add idle shutdown for a new user profile, use the `create-user-profile` command
instead.

###### Note

If idle shutdown is set when applications are running, they must be restarted for idle
shutdown settings to take effect.

```
aws sagemaker update-user-profile --region `region` --domain-id `domain-id` \
--user-profile-name `user-profile-name` --user-settings file://user-settings.json

## user-settings.json example for enforcing the default timeout
{
    "JupyterLabAppSettings": {
        "AppLifecycleManagement": {
            "IdleSettings": {
                "LifecycleManagement": "ENABLED",
                "IdleTimeoutInMinutes": 120,
                "MaxIdleTimeoutInMinutes": 120,
                "MinIdleTimeoutInMinutes": 120
        }
    }
}

## user-settings.json example for letting users customize the default timeout, between 2-5 hours
{
    "JupyterLabAppSettings": {
        "AppLifecycleManagement": {
            "IdleSettings": {
                "LifecycleManagement": "ENABLED",
                "IdleTimeoutInMinutes": 120,
                "MinIdleTimeoutInMinutes": 120,
                "MaxIdleTimeoutInMinutes": 300
        }
    }
}
```
