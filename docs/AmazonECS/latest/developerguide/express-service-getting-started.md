# Create your first Express Mode service using the AWS CLI

This tutorial shows you how to create an Express Mode service application using the AWS AWS CLI. You'll deploy a simple web application that demonstrates the core capabilities of Express Mode service.

## Prerequisites

Before you begin, ensure you have:

- An AWS account with appropriate permissions
- The AWS AWS CLI installed and configured
- A container image stored in Amazon ECR or a private registry

## Step 1: Create IAM Roles

An Express Mode service requires two IAM roles. The Task Execution Role allows Amazon ECS to pull container images and write logs on your behalf.
Create a task execution role and infrastructure role with the following policies:

```
#Create the roles with ECS trust policies
aws iam create-role --role-name ecsTaskExecutionRole \
    --assume-role-policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "ecs-tasks.amazonaws.com"
                },
                "Action": "sts:AssumeRole",
            }
        ]
    }'

aws iam create-role --role-name ecsInfrastructureRoleForExpressServices \
    --assume-role-policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AllowAccessInfrastructureForECSExpressServices",
                "Effect": "Allow",
                "Principal": {
                    "Service": "ecs.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }'
```

```
#Attach the AWS managed policies
aws iam attach-role-policy --role-name ecsTaskExecutionRole \
    --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy
aws iam attach-role-policy --role-name ecsInfrastructureRoleForExpressServices \
    --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSInfrastructureRoleforExpressGatewayServices
```

For more information, see [Amazon ECS task execution IAM role](task_execution_IAM_role.md "task_execution_IAM_role.md").

## Step 2: Create your first Express Mode service application

Create an Express Mode service application with the minimum required parameters:

```
aws ecs create-express-gateway-service \
    --image "public.ecr.aws/nginx/nginx:latest" \
    --execution-role-arn arn:aws:iam::123456789012:role/ecsTaskExecutionRole \
    --infrastructure-role-arn arn:aws:iam::123456789012:role/ecsInfrastructureRoleForExpressServices \
    --monitor-resources

```

This command creates an Express Mode service application with:

- A unique service name generated from the image name
- 1 vCPU and 2 GB memory
- Port 80 for HTTPS traffic
- Auto scaling based on CPU utilization
- An internet-facing Application Load Balancer in the default VPC and public subnets
- A URL unique to this service in the format `servicename.ecs.region.on.aws`

The command continuously monitors resources as they are being provisioned and returns status. Once the service deployment is complete, the
Application URL is ready to receive traffic. When you interrupt the monitoring, the information about the created service is returned, including the service ARN and URL:

```
{
    "service": {
        "cluster": "arn:aws:ecs:region:123456789012:cluster/default",
        "serviceName": "nginx-1234",
        "serviceArn": "arn:aws:ecs:region:123456789012:service/default/nginx-1234",
        "infrastructureRoleArn": "arn:aws:iam::123456789012:role/ecsInfrastructureRoleForExpressServices",
        "status": {
            "statusCode": "ACTIVE"
        },
        "createdAt": "UNIXTIMESTAMP"
    }
}

```

## Step 3: Create an Express Mode service application with custom settings

You can customize your Express Mode service application by specifying additional parameters:

```
aws ecs create-express-gateway-service \
    --execution-role-arn arn:aws:iam::123456789012:role/ecsTaskExecutionRole \
    --infrastructure-role-arn arn:aws:iam::123456789012:role/ecsInfrastructureRoleForExpressServices \
    --primary-container \
        ‘{“image”=“123456789012.dkr.ecr.region.amazonaws.com/my-app:latest", \
        “containerPort”=8080, \
        “environment”=[{“name”=“ENV”,”value”=“production”},{“name”=“DEBUG”,”value”=“false”}]}’ \
    --service-name "my-web-app" \
    --cpu 2 \
    --memory 4 \
    --health-check-path "/health" \
    --scaling-target ‘{“minTaskCount”=3,”maxTaskCount”=100}’
    --monitor-resources

```

This creates an application with:

- A custom name "my-web-app"
- 2 vCPU and 4 GB memory
- Port 8080 for application traffic
- Custom health check endpoint
- Environment variables
- Minimum 3 tasks, maximum 100 tasks for auto scaling

## Step 4: Monitor your deployment

The `--monitor-resources` flag works on any Create, Update or Delete call to your Express Mode services. But in addition, you can monitor
the resources in a service at any time, separate from a mutating action. Deployment time can vary depending on the resources that need to be provisioned.
Once the status changes to `ACTIVE`, your application is ready to receive traffic.

```
aws ecs monitor-express-gateway-service --service-arn arn:aws:ecs:region:123456789012:service/app-23d97h88

```

You can also find current configuration and status of your Express Mode service application:

```
aws ecs describe-express-gateway-service --service-arn arn:aws:ecs:region:123456789012:service/app-23d97h88

```

## Step 5: Access your application

Access the Express Mode service application using the provided URL when it becomes active. The URL format is:

```
https://<service-name>.ecs.<region>.on.aws/
```

For example:

```
https://app-23d97h88.ecs.us-west-2.on.aws/
```

Your application is now running with:

- Automatic SSL/TLS termination
- Load balancing across multiple Availability Zones
- Auto scaling based on CPU utilization
- CloudWatch logging and monitoring
- 5XX Rollback Alarms and Canary Deployments for future updates
