

# Deploying a sample Amazon ECS application using the AWS Copilot CLI
<a name="copilot-deploy"></a>

**AWS Copilot CLI End-of-Support Notice**  
AWS Copilot CLI will reach end-of-support on **June 12, 2026**. After this date, the tool will no longer receive updates, security patches, or technical support.  
No new features or enhancements after June 12, 2026
No security updates or bug fixes
No technical support
Existing deployments will continue to function, but without ongoing maintenance
**Need Help?** Contact AWS Support or visit our [blogpost](https://aws.amazon.com/blogs/containers/announcing-the-end-of-support-for-the-aws-copilot-cli/) for detailed migration guidance.

After installing the AWS Copilot CLI, you can follow these steps to deploy a sample app, verify the deployment, and clean up resources.

## Prerequisites
<a name="copilot-cli-prerequisites"></a>

Before you begin, make sure that you meet the following prerequisites:
+ Install and configure the AWS CLI. For more information, see [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
+ Run `aws configure` to set up a default profile that the AWS Copilot CLI will use to manage your application and services.
+ Install and run Docker. For more information, see [Get started with Docker](https://www.docker.com/get-started).

## Deploy a sample Amazon ECS application using a single command
<a name="copilot-deploy-one"></a>

1. Deploy a sample web application that is cloned from a GitHub repository using the following command. For more information about AWS Copilot `init` and its flags, see the [AWS Copilot documentation](https://aws.github.io/copilot-cli/docs/commands/init/).

   ```
   git clone https://github.com/aws-samples/aws-copilot-sample-service.git demo-app && \ 
   cd demo-app &&                               \
   copilot init --app {{demo}}                      \
     --name {{api}}                                 \
     --type {{'Load Balanced Web Service'}}         \
     --dockerfile {{'./Dockerfile'}}                \
     --port {{80}}                                  \
     --tag  {{latest}}                              \
     --deploy
   ```

1. After the deployment is complete, the AWS Copilot CLI will return a URL that you can use to verify the deployment. You can also use the following commands to verify the app's status.
   + List all of your AWS Copilot applications.

     ```
     copilot app ls
     ```
   + Show information about the environments and services in your application.

     ```
     copilot app show
     ```
   + Show information about your environments.

     ```
     copilot env ls
     ```
   + Show information about the service, including endpoints, capacity and related resources.

     ```
     copilot svc show
     ```
   + List of all the services in an application.

     ```
     copilot svc ls
     ```
   + Show logs of a deployed service.

     ```
     copilot svc logs
     ```
   + Show service status.

     ```
     copilot svc status
     ```

1. When you're finished with this demo, run the following command to clean up associated resources and avoid incurring charges for unused resources.

   ```
   copilot app delete
   ```