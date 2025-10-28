# Open TensorBoard using the

`sagemaker.interactive_apps.tensorboard` module

The `sagemaker.interactive_apps.tensorboard` module provides a function
called `get_app_url` that generates unsigned or presigned URLs to open
the TensorBoard application in any environment in SageMaker AI or Amazon EC2. This is to provide
a unified experience for both Studio Classic and non-Studio Classic users. For the Studio
environment, you can open TensorBoard by running the `get_app_url()`
function as it is, or you can also specify a job name to start tracking as the
TensorBoard application opens. For non-Studio Classic environments, you can open TensorBoard
by providing your domain and user profile information to the utility function.
With this functionality, regardless of where or how you run training code and launch
training jobs, you can directly access TensorBoard by running the
`get_app_url` function in your Jupyter notebook or terminal.

###### Note

This functionality is available in the SageMaker Python SDK v2.184.0 and later. To
use this functionality, make sure that you upgrade the SDK by running `pip
 install sagemaker --upgrade`.

###### Topics

- [Option 1: For SageMaker AI
  Studio Classic](#debugger-htb-access-tb-url-unsigned "#debugger-htb-access-tb-url-unsigned")
- [Option 2: For non-Studio Classic
  environments](#debugger-htb-access-tb-url-presigned "#debugger-htb-access-tb-url-presigned")

## Option 1: For SageMaker AI

Studio Classic

If you are using SageMaker Studio Classic, you can directly open the TensorBoard
application or retrieve an unsigned URL by running the `get_app_url`
function as follows. As you are already within the Studio Classic environment and
signed in as a domain user, `get_app_url()` generates unsigned
URL because it is not necessary to authenticate again.

**To open the TensorBoard application**

The following code automatically opens the TensorBoard application from the
unsigned URL that the `get_app_url()` function returns in the your
environment's default web browser.

```
from sagemaker.interactive_apps import tensorboard

region = "`us-west-2`"
app = tensorboard.TensorBoardApp(region)

app.get_app_url(
    training_job_name="`your-training_job_name`" # Optional. Specify the job name to track a specific training job
)
```

**To retrieve an unsigned URL and open the TensorBoard
application manually**

The following code prints an unsigned URL that you can copy to a web browser
and open the TensorBoard application.

```
from sagemaker.interactive_apps import tensorboard

region = "`us-west-2`"
app = tensorboard.TensorBoardApp(region)
print("Navigate to the following URL:")
print(
    app.get_app_url(
        training_job_name="`your-training_job_name`", # Optional. Specify the name of the job to track.
        open_in_default_web_browser=`False`           # Set to False to print the URL to terminal.
    )
)
```

Note that if you run the preceding two code samples outside the SageMaker AI
Studio Classic environment, the function will return a URL to the TensorBoard
landing page in the SageMaker AI console, because these do not have sign-in information
to your domain and user profile. For creating a presigned URL, see Option 2
in the following section.

## Option 2: For non-Studio Classic

environments

If you use non-Studio Classic environments, such as SageMaker Notebook instance or
Amazon EC2, and want to open TensorBoard directly from the environment you are in,
you need to generate a URL presigned with your domain and user profile
information. A _presigned_ URL is a URL that's signed in to
Amazon SageMaker Studio Classic while the URL is being created with your domain and user
profile, and therefore granted access to all of the domain applications and
files associated with your domain. To open TensorBoard through a presigned
URL, use the `get_app_url` function with your domain and user
profile name as follows.

Note that this option requires the domain user to have the
`sagemaker:CreatePresignedDomainUrl` permission. Without the
permission, the domain user will receive an exception error.

###### Important

Do not share any presigned URLs. The `get_app_url` function
creates presigned URLs, which automatically authenticates with your
domain and user profile and gives access to any applications and files
associated with your domain.

```
print(
    app.get_app_url(
        training_job_name="`your-training_job_name`", # Optional. Specify the name of the job to track.
        create_presigned_domain_url=`True`,           # Reguired to be set to True for creating a presigned URL.
        domain_id="`your-domain-id`",                 # Required if creating a presigned URL (create_presigned_domain_url=True).
        user_profile_name="`your-user-profile-name`", # Required if creating a presigned URL (create_presigned_domain_url=True).
        open_in_default_web_browser=`False`,          # Optional. Set to False to print the URL to terminal.
        optional_create_presigned_url_kwargs={}     # Optional. Add any additional args for Boto3 create_presigned_domain_url
    )
)
```

###### Tip

The `get_app_url` function runs the [`SageMaker.Client.create_presigned_domain_url`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/create_presigned_domain_url.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/create_presigned_domain_url.html") API
in the AWS SDK for Python (Boto3) in the backend. As the Boto3
`create_presigned_domain_url` API creates presigned domain URLs
that expire in 300 seconds by default, presigned TensorBoard application URLs
also expire in 300 seconds. If you want to extend the expiration time, pass the
`ExpiresInSeconds` argument to the
`optional_create_presigned_url_kwargs` argument of the
`get_app_url` function as follows.

```
optional_create_presigned_url_kwargs={"ExpiresInSeconds": `1500`}
```

###### Note

If any of your input passed to the arguments of `get_app_url` is
invalid, the function outputs a URL to the TensorBoard landing page instead of
opening the TensorBoard application. The output message would be similar to the
following.

```
Navigate to the following URL:
https://us-west-2.console.aws.amazon.com/sagemaker/home?region=us-west-2#/tensor-board-landing
```
