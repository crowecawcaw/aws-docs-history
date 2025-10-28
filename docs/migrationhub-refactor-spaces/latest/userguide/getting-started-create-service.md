AWS Migration Hub Refactor Spaces will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub Refactor Spaces, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Step 4: Create a service

Services provide the application’s business capabilities. Your existing application is
represented by one or more services. Each service has an endpoint (either an HTTP/HTTPS URL or an
AWS Lambda function).

After your environment is created, you view information about the environment on the
environment details page (the page with the environment's name as the heading). The environment
details page shows a summary of your environment and lists the applications in your
environment.

The following procedure describes how to create a service starting from the environment
details page. You can also create a service by choosing **Create service** under
**Quick actions** in the Refactor Spaces navigation pane.

###### To create a service from the environment details page

1. From the list of applications, choose the name of the application that you want to add the
   service to.
2. On the application details page (the page with the application's name as the heading),
   under **Services**, choose **Create service**.
3. Enter the name for the new service.
4. (Optional) Enter a description for the service.
5. Select one of the service endpoint types, **VPC** or
   **Lambda**.
   - Select **VPC** if the service is a URL endpoint in a VPC.
     1. Select a VPC to be added to the environment network bridge.
     2. Enter the service URL endpoint.

     If you are creating a service in an environment without a network bridge and the URL
     is private, you must configure [VPC to VPC connectivity](../../../whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.md "../../../whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.md") between your service VPC and the Refactor Spaces application
     proxy VPC.

     VPC endpoint URLs can contain publicly resolvable DNS names (http://www.example.com)
     or an IP address. Private DNS names are not supported in service URLs, but you can use
     private IP addresses that are in the service’s VPC. 3. (Optional) Enter a health check endpoint URL.

   - Select **Lambda** if the service is a Lambda function.
     1. Choose a Lambda function from your account.
     2. (Optional) You can choose a Lambda function alias for the selected Lambda function, if
        one is available.

6. (Optional) Under **Route traffic to this service**, if you want to set
   this service as the application's default route, select the corresponding check box.

When you create a service, you can optionally route application traffic to it at the same
time. If the application the service is being created in does not have any routes, you can make
the service the application’s default route so that all traffic is routed to the service. If
the application has existing routes, then you can add a route with a path to point to the
service.
