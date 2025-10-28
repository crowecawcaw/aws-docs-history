# Create a private model hub

Use the following steps to create a private hub to manage access control for
pretrained JumpStart foundation models for your organization. You must intstall
the SageMaker Python SDK and configure the necessary IAM permissions before creating a
model hub.

###### Create a private hub

1. Install the SageMaker Python SDK and import the necessary Python packages.

```
# Install the SageMaker Python SDK
!pip3 install sagemaker --force-reinstall --quiet

# Import the necessary Python packages
import boto3
from sagemaker import Session
from sagemaker.jumpstart.hub.hub import Hub
```

2. Initialize a SageMaker AI Session.

```
sm_client = boto3.client(`'sagemaker'`)
session = Session(sagemaker_client=sm_client)
session.get_caller_identity_arn()
```

3. Configure the details of your private hub such as the internal hub name,
   UI display name, and UI hub description.

###### Note

If you do not specify an Amazon S3 bucket name when creating your hub, the SageMaker
hub service creates a new bucket on your behalf. The new bucket has the
following naming structure:
`sagemaker-hubs-`REGION`-`ACCOUNT_ID``.

```
HUB_NAME=`"Example-Hub"`
HUB_DISPLAY_NAME=`"Example Hub UI Name"`
HUB_DESCRIPTION=`"A description of the example private curated hub."`
REGION=`"us-west-2"`
```

4. Check that your **Admin** IAM role has the necessary
   Amazon S3 permissions to create a private hub. If your role does not have the
   necessary permissions, navigate to the **Roles** page in
   the IAM console. Choose the **Admin** role and then
   choose **Add permissions** in the **Permissions
   policies** pane to create an inline policy with the following
   permissions using the JSON editor:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:ListBucket",
 "s3:GetObject",
 "s3:GetObjectTagging"
 ],
 "Resource": [
 "arn:aws:s3:::jumpstart-cache-prod-`REGION`",
 "arn:aws:s3:::jumpstart-cache-prod-`REGION`/*"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

5. Create a private model hub using your configurations from **Step
   3** using `hub.create()`.

```
hub = Hub(hub_name=`HUB_NAME`, sagemaker_session=session)

try:
# Create the private hub
  hub.create(
      description=`HUB_DESCRIPTION`,
      display_name=`HUB_DISPLAY_NAME`
  )
  print(f`"Successfully created Hub with name {HUB_NAME} in {REGION}"`)
# Check that no other hubs with this internal name exist
except Exception as e:
  if "ResourceInUse" in str(e):
    print(f`"A hub with the name {HUB_NAME} already exists in your account."`)
  else:
    raise e
```

6. Verify the configuration of your new private hub with the following `describe` command:

```
hub.describe()
```
