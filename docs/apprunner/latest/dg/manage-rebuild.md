# Rebuilding a failed App Runner service

If you receive a **Failed to create** error when creating an App Runner service, you can do one of the following.

- Follow the steps in [When the service fails to create](troubleshooting-create-failure.md "troubleshooting-create-failure.md") to identify the cause of the error.
- If you find an error in the source or configuration, make the necessary changes and then rebuild your service.
- If a temporary issue with App Runner caused your service to fail, rebuild your failed service without making any changes to the source or configuration.
  You can rebuild your failed service either through the [App Runner console](#manage-rebuild.console "#manage-rebuild.console") or the
  [App Runner API or AWS CLI](#manage-rebuild.api "#manage-rebuild.api").

## Rebuilding a failed App Runner service using the App Runner console

Rebuild with updates
Creating a service can fail for a variety of reasons. When this happens, it's important to identify and rectify the root cause of the issue
before rebuilding your service. For more information, see [When the service fails to create](troubleshooting-create-failure.md "troubleshooting-create-failure.md").

###### To rebuild a failed service with updates

1. Go to the **Configurations** tab on your service page and choose **Edit**.

The page opens a summary panel that displays a list of all your updates. 2. Make the required changes and review them in the summary panel. 3. Choose **Save and rebuild**.

You can monitor progress on the **Logs** tab of your service page.

Rebuild without updates
If a temporary issue causes your service creation to fail, you can rebuild your service without modifying its source or configuration settings.

###### To rebuild a failed service without updates

- Choose **Rebuild** on the top right corner of your service page.

You can monitor progress on the **Logs** tab of your service page.

- If your service fails to create again, follow the troubleshooting instructions in [When the service fails to create](troubleshooting-create-failure.md "troubleshooting-create-failure.md"). Make the necessary changes
  and then rebuild your service.

## Rebuilding failed App Runner service using the App Runner API or AWS CLI

Rebuild with updates
To rebuild a failed service:

1. Follow the instructions in [When the service fails to create](troubleshooting-create-failure.md "troubleshooting-create-failure.md") to find the cause of the error.
2. Make the necessary changes to the branch or the image of the source repository or the configuration that caused the error.
3. Rebuild by calling the [UpdateService](../api/API_UpdateService.md "../api/API_UpdateService.md") API action with the new source code repository
   or source image repository parameters. App Runner retrieves the latest commit from the source code repository.

###### Example Rebuilding with updates

In the following example the source configuration of an image-based service is being updated. The value of the `Port` is changed to
`80`.

Updating the `input.json` file for image-based App Runner service

```
{
  "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa",
  "SourceConfiguration": {
    "ImageRepository": {
      "ImageConfiguration": {
        "Port": `"80"`
      }
    }
  }
}
```

Calling the `UpdateService` API action.

```
`aws apprunner update-service
--cli-input-json file:`//input.json``
```

Rebuild without updates
To rebuild your failed service using the App Runner API or AWS CLI, call the [UpdateService](../api/API_UpdateService.md "../api/API_UpdateService.md") API
action without making any changes to source or configuration of your service. Choose to rebuild without making updates only if your service creation
failed due a temporary issue with App Runner.
