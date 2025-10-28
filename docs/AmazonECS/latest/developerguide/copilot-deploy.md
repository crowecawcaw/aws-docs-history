# Deploying a sample Amazon ECS application using the AWS Copilot

CLI

After installing the AWS Copilot CLI, you can follow these steps to deploy a sample app,
verify the deployment, and clean up resources.

## Prerequisites

Before you begin, make sure that you meet the following prerequisites:

- Install and configure the AWS CLI. For more information, see [AWS Command Line
  Interface](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
- Run `aws configure` to set up a default profile that the AWS Copilot
  CLI will use to manage your application and services.
- Install and run Docker. For more information, see [Get started with
  Docker](https://www.docker.com/get-started "https://www.docker.com/get-started").

## Deploy a sample Amazon ECS application using a

single command

1. Deploy a sample web application that is cloned from a GitHub repository
   using the following command. For more information about AWS Copilot
   `init` and its flags, see the [AWS Copilot
   documentation](https://aws.github.io/copilot-cli/docs/commands/init/ "https://aws.github.io/copilot-cli/docs/commands/init/").

```
`git clone https://github.com/aws-samples/aws-copilot-sample-service.git demo-app && \
cd demo-app && \
copilot init --app `demo` \
 --name `api` \
 --type `'Load Balanced Web Service'` \
 --dockerfile `'./Dockerfile'` \
 --port `80` \
 --tag `latest` \
 --deploy`
```

2. After the deployment is complete, the AWS Copilot CLI will return a URL that you
   can use to verify the deployment. You can also use the following commands to
   verify the app's status.
   - List all of your AWS Copilot applications.

   ```
   `copilot app ls`
   ```

   - Show information about the environments and services in your
     application.

   ```
   `copilot app show`
   ```

   - Show information about your environments.

   ```
   `copilot env ls`
   ```

   - Show information about the service, including endpoints, capacity
     and related resources.

   ```
   `copilot svc show`
   ```

   - List of all the services in an application.

   ```
   `copilot svc ls`
   ```

   - Show logs of a deployed service.

   ```
   `copilot svc logs`
   ```

   - Show service status.

   ```
   `copilot svc status`
   ```

3. When you're finished with this demo, run the following command to clean up
   associated resources and avoid incurring charges for unused
   resources.

```
`copilot app delete`
```
