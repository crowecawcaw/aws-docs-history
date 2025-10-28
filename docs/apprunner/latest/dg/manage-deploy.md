# Deploying a new application version to App Runner

When you [create a service](manage-create.md "manage-create.md") in AWS App Runner, you configure an application source—a container image or a source
repository. App Runner provisions resources to run your service and deploys your application to them.

This topic describes ways to redeploy your application source to your App Runner service when a new version becomes available. This can be a new image version
in the image repository or a new commit in the code repository. App Runner provides two methods to deploy to a service: _automatic_ and
_manual_.

## Deployment methods

App Runner provides the following methods for you to control how application deployments are initiated.

**Automatic deployment**

Use automatic deployment when you want continuous integration and deployment (CI/CD) behavior for your service. App Runner monitors your image or code
repository for changes.

Image repository – Whenever you push a new image version to your image repository, or a new commit to your
code repository, App Runner automatically deploys it to your service without further action on your side.

Code repository – Whenever you push a new commit to your code repository that makes changes in the [source directory](service-source-code.md#service-source-code.source-directory "service-source-code.md#service-source-code.source-directory"), App Runner deploys your entire repository. Because _only changes in the source directory_ trigger an automatic deployment, it’s important to understand how the source directory location
affects the scope of an automated deployment.

- _Top-level directory (repository root)_ – This is the default value that’s set for the source directory when you
  create a service. If your source directory is set to this value, this means the entire repository is inside the source directory. So _all commits_ that you push to the source repository will trigger a deployment in this case.
- _Any directory path that’s not the repository root (non-default)_ – Because _only changes
  that are pushed within the source directory_ will trigger an automatic deployment, any changes pushed to your repository that are
  _not_ in the source directory will not trigger an automatic deployment. Therefore, you must use a manual
  deployment to deploy changes that you push outside of the source directory.

###### Note

App Runner doesn't support automatic deployment for Amazon ECR Public images, and for images in an Amazon ECR repository that belongs to a different AWS account than the
one that your service is in.

**Manual deployment**

Use manual deployment when you want to explicitly initiate each deployment to your service. You initiate a deployment if the repository that you
configured for your service has a new version that you want to deploy. For more information, see [Manual deployment](#manage-deploy.manual "#manage-deploy.manual").

###### Note

When you run a manual deployment, App Runner deploys source from the full repository.

You can configure the deployment method for your service in the following ways:

- _Console_ – For a new service you're creating or for an existing service, in the **Deployment settings**
  section of the **Source and deployment** configuration page, choose **Manual** or
  **Automatic**.

![App Runner deployment method configuration](images/manage-deploy.methods.config.png)

- _API or AWS CLI_ – In a call to either the [CreateService](../api/API_CreateService.md "../api/API_CreateService.md") or [UpdateService](../api/API_UpdateService.md "../api/API_UpdateService.md") action, set the `AutoDeploymentsEnabled` member of the [SourceConfiguration](../api/API_SourceConfiguration.md "../api/API_SourceConfiguration.md") parameter to `False` for manual deployment or
  `True` for automatic deployment.

###### Comparing automatic and manual deployments

Both automatic and manual deployments yield the same result: both methods deploy the full repository.

The difference between the two methods is the triggering mechanism:

- Manual deployments are triggered by a deploy from the console, a call to the AWS CLI, or a call to the App Runner API. The [Manual deployment](#manage-deploy.manual "#manage-deploy.manual") section that follows provides the procedures for these.
- Automatic deployments are triggered by a change within the contents of the [source
  directory](service-source-code.md#service-source-code.source-directory "service-source-code.md#service-source-code.source-directory").

## Manual deployment

With manual deployment, you need to explicitly initiate each deployment to your service. When you have a new version of your application image or code
ready to deploy, you can refer to the following sections to learn how to perform a deployment using the console and the API.

###### Note

When you run a manual deployment, App Runner deploys source from the full repository.

Deploy a version of your application using one of the following methods:

App Runner console

###### To deploy using the App Runner console

1. Open the [App Runner console](https://console.aws.amazon.com/apprunner "https://console.aws.amazon.com/apprunner"), and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Services**, and then choose your App Runner service.

The console displays the service dashboard with a **Service overview**.

![App Runner service dashboard page showing Activity list](images/console-dashboard.png) 3. Choose **Deploy**.

Result: Deployment of the new version starts. On the service dashboard page, the service **Status** changes to
**Operation in progress**. 4. Wait for the deployment to end. On the service dashboard page, the service **Status** should change back to
**Running**. 5. To verify that the deployment is successful, on the service dashboard page, choose the **Default domain** value—it's
the URL to your service's website. Inspect or interact with your web application and verify your version change.

###### Note

To augment the security of your App Runner applications, the _\*.awsapprunner.com_ domain is registered in the [Public Suffix List (PSL)](https://publicsuffix.org/ "https://publicsuffix.org/"). For further security, we recommend that you use cookies with a `__Host-`
prefix if you ever need to set sensitive cookies in the default domain name for your App Runner applications.
This practice will help to defend your domain against cross-site request
forgery attempts (CSRF). For more information see the [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes") page in the Mozilla Developer Network.

App Runner API or AWS CLI
To deploy using the App Runner API or AWS CLI, call the [StartDeployment](../api/API_StartDeployment.md "../api/API_StartDeployment.md") API action. The only
parameter to pass is your service ARN. You already configured your application source location when you created the service, and App Runner can find the
new version. Your deployment starts if the call returns a successful response.
