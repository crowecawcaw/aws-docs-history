# Test and deploy after transformation

Deploy your transformed applications to the landing zone and validate the connectivity between your applications and the transformed database, and optionally set up CI/CD pipelines. Sample CI/CD pipeline configurations are generated as reference to help you implement your deployment automation. This final phase validates the complete modernization.

## Configure resources

You need to configure resources used in deployment such as IAM roles, instance profiles
and S3 bucket. AWS Transform does not have permissions to create S3 buckets or to make changes in
your IAM. This action is needed to be performed by a user who has permissions to create new
roles. Usually it is account administrator.

To simplify the process, we provide a setup script that automatically:

- Executes the necessary CloudFormation templates
- Creates the ECS Service-Linked Role
- Sets up all required IAM resources

###### Important

Run the provided setup script as is - do not modify any resource names in the templates or script as this may impact the deployment process.

For Linux:

```
./setup.sh --region <YOUR-Region>
```

For Windows:

```
./setup.ps1 -Region <YOUR-Region>
```

## Check security groups in your VPC

AWS Transform deploys the applications to the same subnet and same security group as Aurora PostgreSQL instance.

In order for the application to connect to the Aurora instance, make sure that this security group has outbound rules allowing connection to the same security group and inbound rules allowing connection from the same security group.

## Select and configure applications

The AWS Transform UI shows a list of applications that can be deployed. Select application and
click **Configure and Commit** to open a configuration window
where you can specify:

- Target infrastructure for the applications: select ECS or one of the EC2 instances
- Application or instance parameters

After you complete and close the configuration window, AWS Transform:

- Generates deployment artifacts based on your configuration
- Commits these artifacts to your repository, including:
  - Deployment scripts
  - CloudFormation templates
  - Sample CI/CD pipeline configurations (which you can use as reference for setting up your deployment automation)

Once the commit is complete, the application status changes to _Configured and
committed_. You can then select the applications and use the **Deploy** button in the top right to initiate deployment.

## ECS deployment

All applications with target ECS are deployed into a new ECS cluster that is created in your account. Each application is deployed in its own dedicated container - multiple applications per container are not supported. You configure container parameters for each application individually, such as required CPU and Memory.

## EC2 deployment

You can select one of proposed EC2 instances and can configure the its parameters such as instance type. Multiple applications can be deployed to the same EC2 instance:

- To deploy multiple applications to a single instance, select the same target EC2 instance for each of these applications during configuration.
- All applications that have the same instance selected as a target are deployed to that instance and assigned different random ports.
- Note that if you edit instance parameters for one application, and then edit another application targeting the same instance, the changes affect all applications deployed to that instance.

## Deployment success

Upon successful deployment, your applications are running on Aurora PostgreSQL with reduced licensing costs, improved performance, and cloud-native scalability. The job stays open unless explicitly stopped. This allows the option for a possible re-deployment with updated deployment parameters.
