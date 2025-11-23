# Tutorial: Automate managing your own environment endpoints on Amazon MWAA

If you use [AWS Organizations](../../../index.md "../../../index.md") to manage multiple AWS accounts that share resources, Amazon MWAA lets you create and manage your own Amazon VPC endpoints.
This means you can use stricter security policies that allow access only to the resources required by your environment.

When you create an environment in a shared Amazon VPC, the account that owns the main Amazon VPC (_owner_) shares the two private subnets
required by Amazon MWAA with other accounts (_participants_) that belong to the same organization. Participant accounts that share those subnets
can then view, create, modify, and delete environments in the shared VPC.

When you create an environment in a shared, or otherwise policy-restricted, Amazon VPC, Amazon MWAA will first create the service VPC resources,
then enter a [`PENDING`](../API/API_Environment.md#mwaa-Type-Environment-Status "../API/API_Environment.md#mwaa-Type-Environment-Status") state for up to 72 hours.

When the environment status changes from `CREATING` to `PENDING`, Amazon MWAA sends an Amazon EventBridge notification of the change in state.
This lets the owner account create the required endpoints on behalf of participants based on endpoint service information from the Amazon MWAA console or API, or programmatically
In the following, we create new Amazon VPC endpoints using an Lambda function and an EventBridge rule that listens to Amazon MWAA state change notifications.

Here, we create the new endpoints in the same Amazon VPC as the environment. To set up a shared Amazon VPC, create the EventBridge rule and Lambda function would in the owner account,
and the Amazon MWAA environment in the participant account.

###### Topics

- [Prerequisites](#tutorials-customer-managed-endpoints-prerequisites "#tutorials-customer-managed-endpoints-prerequisites")
- [Create the Amazon VPC](#tutorials-customer-managed-endpoints-create-vpc "#tutorials-customer-managed-endpoints-create-vpc")
- [Create the Lambda function](#tutorials-customer-managed-endpoints-create-lambda-function "#tutorials-customer-managed-endpoints-create-lambda-function")
- [Create the EventBridge rule](#tutorials-customer-managed-endpoints-create-eb-rule "#tutorials-customer-managed-endpoints-create-eb-rule")
- [Create the Amazon MWAA environment](#tutorials-customer-managed-endpoints-create-mwaa "#tutorials-customer-managed-endpoints-create-mwaa")

## Prerequisites

To complete the steps in this tutorial, you will need the following:

- ...

## Create the Amazon VPC

Use the following CloudFormation template and AWS CLI command to create a new Amazon VPC. The template sets up the Amazon VPC resources and
modifies the endpoint policy to restrict access to a specific queue.

1. Download the CloudFormation [template](samples/cfn-vpc-private-network.md "samples/cfn-vpc-private-network.md"), then unzip the `.yml` file.
2. In a new command prompt window, navigate to the folder where you saved the template, then use
   [`create-stack`](../../../cli/latest/reference/cloudformation/create-stack.md "../../../cli/latest/reference/cloudformation/create-stack.md")
   to create the stack. The `--template-body` flag specifies the path to the template.

```
`aws cloudformation create-stack --stack-name `stack-name` --template-body file://cfn-vpc-private-network.yml`
```

In the next section, you'll create the Lambda function.

## Create the Lambda function

Use the following Python code and IAM JSON policy to create a new Lambda function and execution role. This function creates Amazon VPC endpoints for a private Apache Airflow webserver
and an Amazon SQS queue. Amazon MWAA uses Amazon SQS to queue tasks with Celery among multiple workers when scaling your environment.

1. Download the Python [function code](samples/mwaa-lambda-shared-vpc.md "samples/mwaa-lambda-shared-vpc.md").
2. Download the IAM [permission policy](samples/lambda-mwaa-shared-vpce-policy.md "samples/lambda-mwaa-shared-vpce-policy.md"), then unzip the file.
3. Open a command prompt, then navigate to the folder where you saved the JSON permission policy. Use
   the IAM [`create-role`](../../../index.md "../../../index.md") command
   to create the new role.

```
`aws iam create-role --role-name `function-role` \
 --assume-role-policy-document file://lambda-mwaa-vpce-policy.json`
```

Note the role ARN from the AWS CLI response. In the next step, we specify this new role as the function's execution role using its ARN. 4. Navigate to the folder where you saved the function code, then use
the[`create-function`](../../../index.md "../../../index.md") command
to create a new function.

```
`aws lambda create-function --function-name `mwaa-vpce-lambda` \
--zip-file file://mwaa-lambda-shared-vpc.zip --runtime python3.8 --role arn:aws:iam::123456789012:role/`function-role` --handler lambda_handler`
```

Note the function ARN from the AWS CLI response. In the next step we specify the ARN to configure the function as a target for a new EventBridge rule.

In the next section, you create the EventBridge rule that invokes this function when the environment enters a `PENDING` state.

## Create the EventBridge rule

Do the following to create a new rule that listens for Amazon MWAA notifications and targets
your new Lambda function.

1. Use the EventBridge `put-rule` command to create a new EventBridge rule.

```
`aws events put-rule --name "`mwaa-lambda-rule`" \
--event-pattern "{\"source\":[\"aws.airflow\"],\"detail-type\":[\"MWAA Environment Status Change\"]}"`
```

The event pattern listens for notifications that Amazon MWAA sends whenever an environment status changes.

```
{
					"source": ["aws.airflow"],
					**"detail-type": ["MWAA Environment Status Change"]**
					}
```

2. Use the `put-targets` command to add the Lambda function as a target for the new rule.

```
`aws events put-targets --rule "`mwaa-lambda-rule`" \
--targets "Id"="`1`","Arn"="arn:aws:lambda:`us-east-1`:`123456789012`:function:`mwaa-vpce-lambda`"`
```

You're ready to create a new Amazon MWAA environment with customer-managed Amazon VPC endpoints.

## Create the Amazon MWAA environment

Use the Amazon MWAA console to create a new environment with customer-managed Amazon VPC endpoints.

1. Open the [Amazon MWAA](https://console.aws.amazon.com/mwaa/home/ "https://console.aws.amazon.com/mwaa/home/") console, and choose **Create an environment**.
2. For **Name** enter a unique name.
3. For **Airflow version** choose the latest version.
4. Choose an **Amazon S3 bucket** and a **DAGs folder**, such as `dags/` to use with the environment, then choose **Next**.
5. On the **Configure advanced settings** page, do the following:
   1. For **Virtual Private Cloud**, choose the Amazon VPC you created in the [previous step](#tutorials-customer-managed-endpoints-create-vpc "#tutorials-customer-managed-endpoints-create-vpc").
   2. For **webserver access**, choose **Public network (internet accessible)**.
   3. For **Security groups**, choose the security group you created with CloudFormation. Because the security groups for the
      AWS PrivateLink endpoints from the earlier step are self-referencing, you must choose the same security group for your environment.
   4. For **Endpoint management**, choose **Customer managed endpoints**.

6. Keep the remaining default settings, then choose **Next**.
7. Review your selections, then choose **Create environment**.

###### Tip

For more information about setting up a new environment, refer to [Getting started with Amazon MWAA](get-started.md "get-started.md").

When the environment is `PENDING`, Amazon MWAA sends a notification that matches the event pattern you set for your rule. The
rule invokes your Lambda function. The function parses the notification event and gets the required endpoint information for the webserver and the Amazon SQS queue.
It then creates the endpoints in your Amazon VPC.

When the endpoints are available, Amazon MWAA resumes creating your environment. When ready, the environment status changes to `AVAILABLE` and you can access the
Apache Airflow webserver using the Amazon MWAA console.
