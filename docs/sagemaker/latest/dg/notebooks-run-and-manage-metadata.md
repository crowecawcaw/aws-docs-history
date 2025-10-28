# Get Amazon SageMaker Studio Classic Notebook and App

Metadata

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

You can access notebook metadata and App metadata using the Amazon SageMaker Studio Classic UI.

###### Topics

- [Get Studio Classic Notebook
  Metadata](#notebooks-run-and-manage-metadata-notebook "#notebooks-run-and-manage-metadata-notebook")
- [Get App Metadata](#notebooks-run-and-manage-metadata-app "#notebooks-run-and-manage-metadata-app")

## Get Studio Classic Notebook

Metadata

Jupyter notebooks contain optional metadata that you can access through the Amazon SageMaker Studio Classic
UI.

###### To view the notebook metadata:

1. In the right sidebar, choose the **Property Inspector** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/gears.png)
   ).
2. Open the **Advanced Tools** section.

The metadata should look similar to the following.

```
{
    "instance_type": "ml.t3.medium",
    "kernelspec": {
        "display_name": "Python 3 (Data Science)",
        "language": "python",
        "name": "python3__SAGEMAKER_INTERNAL__arn:aws:sagemaker:us-west-2:<acct-id>:image/datascience-1.0"
    },
    "language_info": {
        "codemirror_mode": {
            "name": "ipython",
            "version": 3
        },
        "file_extension": ".py",
        "mimetype": "text/x-python",
        "name": "python",
        "nbconvert_exporter": "python",
        "pygments_lexer": "ipython3",
        "version": "3.7.10"
    }
}
```

## Get App Metadata

When you create a notebook in Amazon SageMaker Studio Classic, the App metadata is written to a file
named `resource-metadata.json` in the folder
`/opt/ml/metadata/`. You can get the App metadata by opening an Image
terminal from within the notebook. The metadata gives you the following information, which
includes the SageMaker image and instance type the notebook runs in:

- **AppType** – `KernelGateway`
- **DomainId** – Same as the Studio ClassicID
- **UserProfileName** – The profile name of the current
  user
- **ResourceArn** – The Amazon Resource Name (ARN) of the App,
  which includes the instance type
- **ResourceName** – The name of the SageMaker image

Additional metadata might be included for internal use by Studio Classic and is subject to
change.

###### To get the App metadata

1. In the center of the notebook menu, choose the **Launch Terminal**
   icon (
   ![Dollar sign icon representing currency or financial transactions.](images/studio/icons/notebook-launch-terminal.png)
   ). This opens a terminal in the SageMaker image that the notebook runs
   in.
2. Run the following commands to display the contents of the
   `resource-metadata.json` file.

```
`$` cd /opt/ml/metadata/
cat resource-metadata.json
```

The file should look similar to the following.

```
{
    "AppType": "KernelGateway",
    "DomainId": "d-xxxxxxxxxxxx",
    "UserProfileName": "profile-name",
    "ResourceArn": "arn:aws:sagemaker:us-east-2:account-id:app/d-xxxxxxxxxxxx/profile-name/KernelGateway/datascience--1-0-ml-t3-medium",
    "ResourceName": "datascience--1-0-ml",
    "AppImageVersion":""
}
```
