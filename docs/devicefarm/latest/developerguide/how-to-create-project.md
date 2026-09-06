

# Creating a project in AWS Device Farm
<a name="how-to-create-project"></a>

You can create a project by using the AWS Device Farm console, AWS CLI, or AWS Device Farm API.

## Prerequisites
<a name="how-to-create-project-prerequisites"></a>
+ Complete the steps in [Setting up](setting-up.md).

## Create a project (console)
<a name="how-to-create-project-console"></a>

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Projects**.

1. Choose **New project**.

1. Enter a name for your project. Optionally, you may supply one or more of the parameters below, then choose **Submit**.

   Optional configuration parameters:  
**Virtual Private Cloud (VPC) settings**  
Select a VPC, subnets, and security group to be applied to the device under test and its paired test host. This feature is only supported with private devices. See [VPC-ENI in AWS Device Farm](vpc-eni.md) for more information.  
**Execution Role ARN**  
An IAM role to be assumed by the test runner in custom test environments. For more information, see [Access AWS resources using an IAM Execution Role](custom-test-environments-iam-roles.md).  
**Environment Variables**  
One or more variables to be inserted into the environment of the test execution runner process. Variable names beginning with "DEVICEFARM\_" are reserved for service use. We recommend against storing sensitive values in these environment variables, and instead suggest using an IAM execution role to fetch such values from AWS Secrets Manager during your test.

## Create a project (AWS CLI)
<a name="how-to-create-project-cli"></a>
+ Run **create-project**, specifying the project name.

  Example:

  ```
  aws devicefarm create-project --name {{MyProjectName}}
  ```

  The AWS CLI response includes the Amazon Resource Name (ARN) of the project.

  ```
  {
      "project": {
          "name": "MyProjectName",
          "arn": "arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE",
          "created": 1535675814.414
      }
  }
  ```

  For more information, see [**create-project**](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/create-project.html) and [AWS CLI reference](cli-ref.md).

## Create a project (API)
<a name="how-to-create-project-api"></a>
+ Call the [`CreateProject`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateProject.html) API.

For information about using the Device Farm API, see [Automating Device Farm](api-ref.md).