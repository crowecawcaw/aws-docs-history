

# Open TensorBoard using the `get_app_url` function as an `ModelTrainer` class method
<a name="debugger-htb-access-tb-get-app-url-estimator-method"></a>

If you are in the process of running a training job using the `ModelTrainer` class of the SageMaker Python SDK and have an active object of the `ModelTrainer` class, you can also access the [`get_app_url` function as a class method](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html) of the `ModelTrainer` class. Open the TensorBoard application or retrieve an unsigned URL by running the `get_app_url` method as follows. The `get_app_url` class method pulls the training job name from the ModelTrainer and opens the TensorBoard application with the specified job.

**Note**  
This functionality is available in the SageMaker Python SDK v2.184.0 and later. To use this functionality, make sure that you upgrade the SDK by running `pip install sagemaker --upgrade`.

**Topics**
+ [Option 1: For SageMaker Studio Classic](#debugger-htb-access-tb-get-app-url-estimator-method-studio)
+ [Option 2: For non-Studio Classic environments](#debugger-htb-access-tb-get-app-url-estimator-method-non-studio)

## Option 1: For SageMaker Studio Classic
<a name="debugger-htb-access-tb-get-app-url-estimator-method-studio"></a>

**To open the TensorBoard application** 

The following code automatically opens the TensorBoard application from the unsigned URL that the `get_app_url()` method returns in the your environment's default web browser.

```
model_trainer.get_app_url(
    app_type=SupportedInteractiveAppTypes.TENSORBOARD # Required.
)
```

**To retrieve an unsigned URL and open the TensorBoard application manually**

The following code prints an unsigned URL that you can copy to a web browser and open the TensorBoard application.

```
print(
    model_trainer.get_app_url(
        app_type=SupportedInteractiveAppTypes.TENSORBOARD, # Required.
        open_in_default_web_browser=False, # Optional. Set to False to print the URL to terminal.
    )
)
```

Note that if you run the preceding two code samples outside the SageMaker AI Studio Classic environment, the function will return a URL to the TensorBoard landing page in the SageMaker AI console, because these do not have sign-in information to your domain and user profile. For creating a presigned URL, see Option 2 in the following section.

## Option 2: For non-Studio Classic environments
<a name="debugger-htb-access-tb-get-app-url-estimator-method-non-studio"></a>

If you use non-Studio Classic environments, such as SageMaker Notebook instance and Amazon EC2, and want to generate a presigned URL to open the TensorBoard application, use the `get_app_url` method with your domain and user profile information as follows.

Note that this option requires the domain user to have the `sagemaker:CreatePresignedDomainUrl` permission. Without the permission, the domain user will receive an exception error.

**Important**  
Do not share any presigned URLs. The `get_app_url` function creates presigned URLs, which automatically authenticates with your domain and user profile and gives access to any applications and files associated with your domain.

```
print(
    model_trainer.get_app_url(
        app_type=SupportedInteractiveAppTypes.TENSORBOARD, # Required
        create_presigned_domain_url={{True}},           # Reguired to be set to True for creating a presigned URL.
        domain_id="{{your-domain-id}}",                 # Required if creating a presigned URL (create_presigned_domain_url=True).
        user_profile_name="{{your-user-profile-name}}", # Required if creating a presigned URL (create_presigned_domain_url=True).
        open_in_default_web_browser=False,            # Optional. Set to False to print the URL to terminal.
        optional_create_presigned_url_kwargs={}       # Optional. Add any additional args for Boto3 create_presigned_domain_url
    )
)
```