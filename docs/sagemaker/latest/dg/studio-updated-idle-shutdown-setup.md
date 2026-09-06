

# Set up idle shutdown
<a name="studio-updated-idle-shutdown-setup"></a>

 The following sections show how to set up idle shutdown from either the console or using the AWS CLI. Idle shutdown can be set at either the domain or user profile level. 

## Prerequisites
<a name="studio-updated-idle-shutdown-setup-prereq"></a>

 To use idle shutdown with your application, you must complete the following prerequisites. 
+ Ensure that your application is using the SageMaker Distribution (SMD) version 2.0. You can select this version during application creation or update the image version of the application after creation. For more information, see [Update the SageMaker Distribution Image](studio-updated-jl-update-distribution-image.md) . 
+ For applications built with custom images, idle shutdown is supported if your custom image is created with SageMaker Distribution (SMD) version 2.0 or later as the base image. If the custom image is created with a different base image, then you must install the [jupyter-activity-monitor-extension >= 0.3.1](https://anaconda.org/conda-forge/jupyter-activity-monitor-extension) extension on the image and attach the image to your Amazon SageMaker AI domain for JupyterLab applications. For more information about custom images, see [Bring your own image (BYOI)](studio-updated-byoi.md).

## From the Console
<a name="studio-updated-idle-shutdown-setup-console"></a>

 The following sections show how to enable idle shutdown from the console. 

### Add when creating a new domain
<a name="studio-updated-idle-shutdown-setup-console-new-domain"></a>

1. Create a domain by following the steps in [Use custom setup for Amazon SageMaker AI](onboard-custom.md) 

1.  When configuring the application settings in the domain, navigate to either the Code Editor or JupyterLab section.  

1.  Select **Enable idle shutdown**. 

1.  Enter a default idle shutdown time in minutes. This values defaults to `10,080` if no value is entered. 

1.  (Optional) Select **Allow users to set custom idle shutdown time** to allow users to modify the idle shutdown time. 
   +  Enter a maximum value that users can set the default idle shutdown time to. You must enter a maximum value. The minimum value is set by Amazon SageMaker AI and must be `60`. 

### Add to an existing domain
<a name="studio-updated-idle-shutdown-setup-console-existing-domain"></a>

**Note**  
If idle shutdown is set when applications are running, they must be restarted for idle shutdown settings to take effect. 

1.  Navigate to the domain. 

1.  Choose the **App Configurations** tab. 

1.  From the **App Configurations** tab, navigate to either the Code Editor or JupyterLab section. 

1.  Select **Edit**. 

1.  Select **Enable idle shutdown**. 

1.  Enter a default idle shutdown time in minutes. This values defaults to `10,080` if no value is entered. 

1.  (Optional) Select **Allow users to set custom idle shutdown time** to allow users to modify the idle shutdown time. 
   +  Enter a maximum value that users can set the default idle shutdown time to. You must enter a maximum value. The minimum value is set by Amazon SageMaker AI and must be `60`. 

1.  Select **Submit**. 

### Add when creating a new user profile
<a name="studio-updated-idle-shutdown-setup-console-new-userprofile"></a>

1. Add a user profile by following the steps at [Add user profiles](domain-user-profile-add.md) 

1.  When configuring the application settings for the user profile, navigate to either the Code Editor or JupyterLab section. 

1.  Select **Enable idle shutdown**. 

1.  Enter a default idle shutdown time in minutes. This values defaults to `10,080` if no value is entered. 

1.  (Optional) Select **Allow users to set custom idle shutdown time** to allow users to modify the idle shutdown time. 
   +  Enter a maximum value that users can set the default idle shutdown time to. You must enter a maximum value. The minimum value is set by Amazon SageMaker AI and must be `60`. 

1.  Select “Save Changes”. 

### Add to an existing user profile
<a name="studio-updated-idle-shutdown-setup-console-existing-userprofile"></a>

 Note: If idle shutdown is set when applications are running, they must be restarted for idle shutdown settings to take effect. 

1.  Navigate to the user profile. 

1.  Choose the **App Configurations** tab. 

1.  From the ****App Configurations**** tab, navigate to either the Code Editor or JupyterLab section.  

1.  Select **Edit**. 

1.  Idle shutdown settings will show domain settings by default if configured for the domain. 

1.  Select **Enable idle shutdown**. 

1.  Enter a default idle shutdown time in minutes. This values defaults to `10,080` if no value is entered. 

1.  (Optional) Select **Allow users to set custom idle shutdown time** to allow users to modify the idle shutdown time. 
   +  Enter a maximum value that users can set the default idle shutdown time to. You must enter a maximum value. The minimum value is set by Amazon SageMaker AI and must be `60`. 

1.  Select **Save Changes**. 

## From the AWS CLI
<a name="studio-updated-idle-shutdown-setup-cli"></a>

 The following sections show how to enable idle shutdown using the AWS CLI. 

**Note**  
To enforce a specific timeout value from the AWS CLI, you must set `IdleTimeoutInMinutes`, `MaxIdleTimeoutInMinutes`, and `MinIdleTimeoutInMinutes` to the same value.

### Domain
<a name="studio-updated-idle-shutdown-setup-cli-domain"></a>

 The following command shows how to enable idle shutdown when updating an existing domain. To add idle shutdown for a new domain, use the `create-domain` command instead. 

**Note**  
If idle shutdown is set when applications are running, they must be restarted for idle shutdown settings to take effect. 

```
aws sagemaker update-domain --region {{region}} --domain-id {{domain-id}} \
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
<a name="studio-updated-idle-shutdown-setup-cli-userprofile"></a>

 The following command shows how to enable idle shutdown when updating an existing user profile. To add idle shutdown for a new user profile, use the `create-user-profile` command instead. 

**Note**  
If idle shutdown is set when applications are running, they must be restarted for idle shutdown settings to take effect. 

```
aws sagemaker update-user-profile --region {{region}} --domain-id {{domain-id}} \
--user-profile-name {{user-profile-name}} --user-settings file://user-settings.json

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