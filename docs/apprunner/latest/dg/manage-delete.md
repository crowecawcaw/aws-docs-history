# Deleting an App Runner service

When you want to terminate the web application that's running in your AWS App Runner service, you can delete the service. Deleting a service stops the running
web service, removes the underlying resources, and deletes your associated data.

You might want to delete an App Runner service for one or more of the following reasons:

- _You don't need the web application anymore_ – For example, it's retired, or it's a development version that you're done
  using.
- _You've reached the App Runner service quota_ – You want to create a new service in the same AWS Region and you've reached the
  quota associated with your account. For more information, see [App Runner resource quotas](architecture.md#architecture.quotas "architecture.md#architecture.quotas").
- _Security or privacy considerations_ – You want App Runner to delete the data that it stores for your service.

## Pausing and deleting compared

_Pause_ your App Runner service to _temporarily_ disable it. Only compute resources are terminated, and your stored data
(for example, the container image with your application version) remains intact. Resuming your service is quick—your application is ready to be
deployed to new compute resources. Your App Runner domain remains the same.

_Delete_ your App Runner service to _permanently_ remove it. Your stored data is deleted. If you need to recreate the
service, App Runner needs to fetch your source again, and also to build it if it's a code repository. Your web application gets a new App Runner domain.

## What does App Runner delete?

When you delete your service, App Runner deletes some associated items, and doesn't delete others. The following lists provide the details.

###### Items that App Runner deletes:

- _Container image_ – A copy of the image that you deployed or the image that App Runner built from your source code. It's stored
  in Amazon Elastic Container Registry (Amazon ECR) using internal AWS accounts that are owned by App Runner.
- _Service configuration_ – The configuration settings that are associated with your App Runner service. They're stored in
  Amazon DynamoDB using internal AWS accounts that are owned by App Runner.

###### Items that App Runner doesn't delete:

- _Connection_ – You might have a connection that's associated with your service. An App Runner connection is a separate resource
  that might be shared among several App Runner services. If you don't need the connection anymore, you can explicitly delete it. For more information, see
  [Managing App Runner connections](manage-connections.md "manage-connections.md").
- _Custom domain certificates_ – If you link custom domains to an App Runner service, App Runner internally creates certificates that
  track domain validity. They're stored in AWS Certificate Manager (ACM). App Runner doesn't delete the certificate for seven days after a
  domain is unlinked from your service or after the service is deleted. For more information, see [Managing custom domain names for an App Runner service](manage-custom-domains.md "manage-custom-domains.md").

## Delete your service

Delete your App Runner service using one of the following methods:

App Runner console

###### To delete your service using the App Runner console

1. Open the [App Runner console](https://console.aws.amazon.com/apprunner "https://console.aws.amazon.com/apprunner"), and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Services**, and then choose your App Runner service.

The console displays the service dashboard with a **Service overview**.

![App Runner service dashboard page showing Activity list](/images/apprunner/latest/dg/images/console-dashboard.png) 3. Choose **Actions**, and then choose **Delete**.

The console takes you to the **Services** page. The deleted service displays the **Operation in progress**
status, and then the service disappears from the list. Your service is now deleted.

App Runner API or AWS CLI
To delete your service using the App Runner API or AWS CLI, call the [DeleteService](../api/API_DeleteService.md "../api/API_DeleteService.md") API action.
If the call returns a successful response with a [Service](../api/API_Service.md "../api/API_Service.md") object showing `"Status":
 "OPERATION_IN_PROGRESS"`, App Runner starts deleting your service.
