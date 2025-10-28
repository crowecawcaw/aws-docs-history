# Using the AWS CLI to set up Neptune ML on a DB cluster

In addition to the AWS CloudFormation quick-start template and the AWS Management Console, you can also set
up Neptune ML using the AWS CLI.

## Create a DB cluster parameter

group for your new Neptune ML cluster

The following AWS CLI commands create a new DB cluster parameter group and set it up
to work with Neptune ML:

###### To create and configure a DB cluster parameter group for Neptune ML

1. Create a new DB cluster parameter group:

```
aws neptune create-db-cluster-parameter-group \
  --db-cluster-parameter-group-name `(name of the new DB cluster parameter group)` \
  --db-parameter-group-family neptune1
  --description "`(description of your machine learning project)`" \
  --region `(AWS region, such as us-east-1)`
```

2. Create a `neptune_ml_iam_role` DB cluster parameter set to
   the ARN of the `SageMakerExcecutionIAMRole` for your DB cluster to use
   while calling SageMaker AI for creating jobs and getting prediction from hosted ML models:

```
aws neptune modify-db-cluster-parameter-group \
  --db-cluster-parameter-group-name `(name of the new DB cluster parameter group)` \
  --parameters "ParameterName=neptune_ml_iam_role, \
                ParameterValue=`ARN of the SageMakerExcecutionIAMRole`, \
                Description=NeptuneMLRole, \
                ApplyMethod=pending-reboot" \
  --region `(AWS region, such as us-east-1)`
```

Setting this parameter allows Neptune to access SageMaker AI without you having to pass in
the role with every call.

For information about how to create the `SageMakerExcecutionIAMRole`, see
[Create a custom NeptuneSageMakerIAMRole role](machine-learning-manual-setup.md#ml-manual-setup-sm-role "machine-learning-manual-setup.md#ml-manual-setup-sm-role"). 3. Finally, use `describe-db-cluster-parameters` to check that all the
parameters in the new DB cluster parameter group are set as you want them to be:

```
aws neptune describe-db-cluster-parameters \
  --db-cluster-parameter-group-name `(name of the new DB cluster parameter group)` \
  --region `(AWS region, such as us-east-1)`
```

## Attach the new DB cluster parameter group to the DB cluster you will use with Neptune ML

Now you can attach the new DB cluster parameter group that you just created to an existing
DB cluster by using the following command:

```
aws neptune modify-db-cluster \
  --db-cluster-identifier `(the name of your existing DB cluster)` \
  --apply-immediately
  --db-cluster-parameter-group-name `(name of your new DB cluster parameter group)` \
  --region `(AWS region, such as us-east-1)`
```

To make all the parameters effective, you can then reboot the DB cluster:

```
aws neptune reboot-db-instance
  --db-instance-identifier (name of the primary instance of your DB cluster) \
  --profile `(name of your AWS profile to use)` \
  --region `(AWS region, such as us-east-1)`
```

Or, if you're creating a new DB cluster to use with Neptune ML, you can use the
following command to create the cluster with the new parameter group attached, and then create
a new primary (writer) instance:

```
cluster-name=`(the name of the new DB cluster)`
aws neptune create-db-cluster
  --db-cluster-identifier ${cluster-name}
  --engine graphdb \
  --engine-version 1.0.4.1 \
  --db-cluster-parameter-group-name `(name of your new DB cluster parameter group)` \
  --db-subnet-group-name `(name of the subnet to use)` \
  --region `(AWS region, such as us-east-1)`

aws neptune create-db-instance
  --db-cluster-identifier ${cluster-name}
  --db-instance-identifier ${cluster-name}-i \
  --db-instance-class `(the instance class to use, such as db.r5.xlarge)`
  --engine graphdb \
  --region `(AWS region, such as us-east-1)`
```

## Attach the

`NeptuneSageMakerIAMRole` to your DB cluster so that it can access SageMaker AI and Amazon S3 resources

Finally, follow the instructions in [Create a custom NeptuneSageMakerIAMRole role](machine-learning-manual-setup.md#ml-manual-setup-sm-role "machine-learning-manual-setup.md#ml-manual-setup-sm-role") to create an IAM role that will allow
your DB cluster to communicate with SageMaker AI and Amazon S3. Then, use the following command
to attach the `NeptuneSageMakerIAMRole` role you created to your DB cluster:

```
aws neptune add-role-to-db-cluster
  --db-cluster-identifier ${cluster-name}
  --role-arn arn:aws:iam::`(the ARN number of the role's ARN)`:role/NeptuneMLRole \
  --region `(AWS region, such as us-east-1)`
```

## Create two endpoints for SageMaker AI in your Neptune VPC

Neptune ML needs two SageMaker AI endpoints in your Neptune DB cluster's VPC:

- `com.amazonaws.`(AWS region, like us-east-1)`.sagemaker.runtime`
- `com.amazonaws.`(AWS region, like us-east-1)`.sagemaker.api`

If you haven't used the quick-start AWS CloudFormation template, which creates these automatically
for you, you can use the following AWS CLI commands to create them:

This one creates the `sagemaker.runtime` endpoint:

```
aws ec2 create-vpc-endpoint
  --vpc-id `(the ID of your Neptune DB cluster's VPC)`
  --vpc-endpoint-type Interface
  --service-name com.amazonaws.`(AWS region, like us-east-1)`.sagemaker.runtime
  --subnet-ids `(the subnet ID or IDs that you want to use)`
  --security-group-ids `(the security group for the endpoint network interface, or omit to use the default)`
  --private-dns-enabled
```

And this one creates the `sagemaker.api` endpoint:

```
aws ec2 create-vpc-endpoint
  --vpc-id `(the ID of your Neptune DB cluster's VPC)`
  --vpc-endpoint-type Interface
  --service-name com.amazonaws.`(AWS region, like us-east-1)`.sagemaker.api
  --subnet-ids `(the subnet ID or IDs that you want to use)`
  --security-group-ids `(the security group for the endpoint network interface, or omit to use the default)`
  --private-dns-enabled
```

You can also use the [VPC console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/")
to create these endpoints. See [Secure prediction calls in Amazon SageMaker with AWS PrivateLink](https://aws.amazon.com/blogs/machine-learning/secure-prediction-calls-in-amazon-sagemaker-with-aws-privatelink/ "https://aws.amazon.com/blogs/machine-learning/secure-prediction-calls-in-amazon-sagemaker-with-aws-privatelink/") and [Securing all Amazon SageMaker API calls with AWS PrivateLink](https://aws.amazon.com/blogs/machine-learning/securing-all-amazon-sagemaker-api-calls-with-aws-privatelink/ "https://aws.amazon.com/blogs/machine-learning/securing-all-amazon-sagemaker-api-calls-with-aws-privatelink/").

## Create a SageMaker AI inference endpoint parameter in your DB cluster parameter group

To avoid having to specify the SageMaker AI inference endpoint of the model that you're using in
every query you make to it, create a DB cluster parameter named
`neptune_ml_endpoint` in the DB cluster parameter group for Neptune ML. Set the
parameter to the `id` of the instance endpoint in question.

You can use the following AWS CLI command to do that:

```
aws neptune modify-db-cluster-parameter-group \
  --db-cluster-parameter-group-name neptune-ml-demo \
  --parameters "ParameterName=neptune_ml_endpoint, \
                ParameterValue=`(the name of the SageMaker AI inference endpoint you want to query)`, \
                Description=NeptuneMLEndpoint, \
                ApplyMethod=pending-reboot" \
  --region `(AWS region, such as us-east-1)`
```
