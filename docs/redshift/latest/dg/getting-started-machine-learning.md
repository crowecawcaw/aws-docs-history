Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Getting started with Amazon Redshift ML

Amazon Redshift ML makes it easy for SQL users to create, train, and deploy machine learning
models using familiar SQL commands. With Amazon Redshift ML, you can use your data in your
Redshift cluster to train models with Amazon SageMaker AI. Later, the models are localized and
predictions can be made within an Amazon Redshift database. Amazon Redshift ML currently supports the machine
learning algorithms: XGBoost (AUTO ON and OFF) and multilayer perceptron (AUTO ON), K-Means (AUTO OFF), and Linear Learner.

###### Topics

- [Cluster and configure setup for Amazon Redshift ML
  administration](#admin-setup "#admin-setup")
- [Using model explainability with Amazon Redshift ML](#clarify "#clarify")
- [Amazon Redshift ML probability metrics](#probability_metrics "#probability_metrics")

## Cluster and configure setup for Amazon Redshift ML

administration

Before you work with Amazon Redshift ML, complete the cluster setup and configure
permissions for using Amazon Redshift ML.

### Cluster setup for using Amazon Redshift ML

Before you work with Amazon Redshift ML, complete the following prerequisites.

As an Amazon Redshift administrator, do the following one-time setup for using Amazon Redshift provisioned clusters.
For using Amazon Redshift ML with Amazon Redshift Serverless, see
[Getting started with
Amazon Redshift Serverless](../gsg/new-user-serverless.md "../gsg/new-user-serverless.md").

To perform one-time cluster setup for Amazon Redshift ML

1. Create a Redshift cluster using the AWS Management Console or the AWS Command Line Interface (AWS CLI).
   Make sure to attach the AWS Identity and Access Management (IAM) policy while creating the cluster.
   For more information about permissions required to use Amazon Redshift ML with
   Amazon SageMaker AI, see
   [Permissions required to use Amazon Redshift machine learning (ML)](../mgmt/redshift-iam-access-control-identity-based.md#iam-permission-ml? "../mgmt/redshift-iam-access-control-identity-based.md#iam-permission-ml?")
2. Create the IAM role required for using Amazon Redshift ML in one of
   the following ways:
   - To use SageMaker AI with Amazon Redshift ML, create an IAM role with
     `AmazonS3FullAccess` and
     `AmazonSageMakerFullAccess` policies. If you plan
     to also create Forecast models, attach the `AmazonForecastFullAccess`
     policy to your role as well.
   - To use Amazon Bedrock with Amazon Redshift ML, create an IAM role with
     `AmazonS3FullAccess` and
     `AmazonBedrockFullAccess` policies.
   - We recommend that you create an IAM role through the Amazon Redshift console
     that has the `AmazonRedshiftAllCommandsFullAccess` policy with
     permissions to run SQL commands, such as CREATE MODEL. Amazon Redshift uses a
     seamless API-based mechanism to programmatically create IAM roles in
     your AWS account on your behalf. Amazon Redshift automatically attaches
     existing AWS managed policies to the IAM role. This approach means
     that you can stay within the Amazon Redshift console and don't have to switch
     to the IAM console for role creation. For more information, see [Creating an IAM role as default for Amazon Redshift](../mgmt/default-iam-role.md "../mgmt/default-iam-role.md").

   When an IAM role is created as the default for your cluster, include
   `redshift` as part of the resource name or use a
   Redshift-specific tag to tag those resources.

   To use Amazon Bedrock foundation models, add the following section:

   ```
   // Required section if you use Bedrock models.
   {
      "Effect": "Allow",
      "Action": "bedrock:InvokeModel",
      "Resource": [
          "arn:aws:bedrock:`<region>`::foundation-model/*"
      ]
   }


   ```

   - If you want to create an IAM role with a more restrictive policy,
     you can use the policy following. You can also modify this policy to meet
     your needs.

   The Amazon S3 bucket `redshift-downloads/redshift-ml/` is the
   location where the sample data used for other steps and examples is
   stored. You can remove it if you don't need to load data from Amazon S3.
   Or, replace it with other Amazon S3 buckets that you use to load data into
   Amazon Redshift.

   The `your-account-id`,
   `your-role`, and
   `amzn-s3-demo-bucket` values are
   the ones that you specify as part of your CREATE MODEL command.

   (Optional) Use the AWS KMS keys section of the sample policy if you
   specify an AWS KMS key while using Amazon Redshift ML. The
   `your-kms-key` value is the
   key that you use as part of your CREATE MODEL command.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "cloudwatch:PutMetricData",
    "ecr:BatchCheckLayerAvailability",
    "ecr:BatchGetImage",
    "ecr:GetAuthorizationToken",
    "ecr:GetDownloadUrlForLayer",
    "logs:CreateLogGroup",
    "logs:CreateLogStream",
    "logs:DescribeLogStreams",
    "logs:PutLogEvents",
    "sagemaker:*Job*",
    "sagemaker:AddTags",
    "sagemaker:CreateModel",
    "sagemaker:CreateEndpoint",
    "sagemaker:CreateEndpointConfig",
    "sagemaker:DeleteEndpoint",
    "sagemaker:DeleteEndpointConfig",
    "sagemaker:DeleteModel"
    ],
    "Resource": "*"
    },
    {
    "Effect": "Allow",
    "Action": [
    "iam:PassRole",
    "s3:AbortMultipartUpload",
    "s3:GetObject",
    "s3:DeleteObject",
    "s3:PutObject"
    ],
    "Resource": [
    "arn:aws:iam::`111122223333`:role/`<your-role>`",
    "arn:aws:s3:::amzn-s3-demo-bucket/*",
    "arn:aws:s3:::redshift-downloads/*"
    ]
    },
    {
    "Effect": "Allow",
    "Action": [
    "s3:GetBucketLocation",
    "s3:ListBucket"
    ],
    "Resource": [
    "arn:aws:s3:::amzn-s3-demo-bucket",
    "arn:aws:s3:::redshift-downloads"
    ]
    },
    {
    "Effect": "Allow",
    "Action": [
    "kms:CreateGrant",
    "kms:Decrypt",
    "kms:DescribeKey",
    "kms:Encrypt",
    "kms:GenerateDataKey*"
    ],
    "Resource": [
    "arn:aws:kms:`us-east-1`:`111122223333`:key/`<your-kms-key>`"
    ]
    }
    ]
   }`

   ```

3. To allow Amazon Redshift and SageMaker AI to assume the role to interact with other
   services, add the following trust policy to the IAM role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "redshift.amazonaws.com",
 "sagemaker.amazonaws.com",
 "forecast.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

4. (Optional) Create an Amazon S3 bucket and an AWS KMS key. These are for Amazon Redshift to
   use to store the training data sent to Amazon SageMaker AI and receive the trained model
   from Amazon SageMaker AI.
5. (Optional) Create different combinations of IAM roles and Amazon S3 buckets for
   controlling access to different user groups.
6. When you turn on enhanced VPC routing, traffic between Redshift ML and your
   S3 bucket goes through your private VPC. For more information about VPC
   routing, see [Enhanced VPC routing in
   Amazon Redshift](../mgmt/enhanced-vpc-routing.md "../mgmt/enhanced-vpc-routing.md").

For more information about permissions required to specify a private VPC for
your hyperparameter tuning job, see [Permissions required to use Amazon Redshift ML with Amazon SageMaker AI](../mgmt/redshift-iam-access-control-identity-based.md "../mgmt/redshift-iam-access-control-identity-based.md").

###### Note

Inference calls made to remote SageMaker AI models do not go through your VPC.

For information on how to use the CREATE MODEL statement to start creating models
for different use cases, see [CREATE MODEL](r_CREATE_MODEL.md "r_CREATE_MODEL.md").

### Managing permissions and ownership

Just as with other database objects, such as tables or functions, Amazon Redshift binds
creating and using ML models to access control mechanisms. There are separate
permissions for creating a model that runs prediction functions.

The following examples use two user groups, `retention_analyst_grp`
(model creator) and `marketing_analyst_grp` (model user) to illustrate how
Amazon Redshift manages access control. The retention analyst creates machine learning
models that the other set of users can use through acquired permissions.

A superuser can GRANT USER or GROUP permission to create machine learning models
using the following statement.

```
GRANT CREATE MODEL TO GROUP retention_analyst_grp;
```

Users or groups with this permission can create a model in any schema in the
cluster if a user has the usual CREATE permission on the SCHEMA. The machine learning
model is part of the schema hierarchy in a similar way to tables, views, procedures,
and user-defined functions.

Assuming a schema `demo_ml` already exists, grant the two user groups
the permission on the schema as follows.

```
GRANT CREATE, USAGE ON SCHEMA demo_ml TO GROUP retention_analyst_grp;
```

```
GRANT USAGE ON SCHEMA demo_ml TO GROUP marketing_analyst_grp;
```

To let other users use your machine learning inference function, grant the EXECUTE
permission. The following example uses the EXECUTE permission to grant the
marketing_analyst_grp GROUP the permission to use the model.

```
GRANT EXECUTE ON MODEL demo_ml.customer_churn_auto_model TO GROUP marketing_analyst_grp;
```

Use the REVOKE statement with CREATE MODEL and EXECUTE to revoke those permissions
from users or groups. For more information on permission control commands, see [GRANT](r_GRANT.md "r_GRANT.md") and [REVOKE](r_REVOKE.md "r_REVOKE.md").

## Using model explainability with Amazon Redshift ML

With model explainability in Amazon Redshift ML, you use feature importance values to help
understand how each attribute in your training data contributes to the predicted result.

Model explainability helps improve your machine learning (ML) models by
explaining the predictions that your models make.
Model explainability helps explain how these models
make predictions using a feature attribution approach.

Amazon Redshift ML incorporates model explainability to provide model explanation
functionality to Amazon Redshift ML users. For more information about
model explainability, see [What Is Fairness and Model
Explainability for Machine Learning Predictions?](../../../sagemaker/latest/dg/clarify-fairness-and-explainability.md "../../../sagemaker/latest/dg/clarify-fairness-and-explainability.md") in the
_Amazon SageMaker AI Developer Guide_.

Model explainability also monitors the inferences that models make in production for
feature attribution drift. It also provides tools to help you generate
model governance reports that you can use to inform risk and compliance teams, and
external regulators.

When you specify the AUTO ON or AUTO OFF option when using the CREATE MODEL
statement, after the model training job finishes, SageMaker AI creates the explanation output.
You can use the EXPLAIN_MODEL function to query the explainability report in a JSON
format. For more information, see [Machine learning functions](ml-function.md "ml-function.md").

## Amazon Redshift ML probability metrics

In supervised learning problems, class labels are outcomes of predictions that use the input data. For example,
if you're using a model to predict whether a customer would resubscribe to a streaming service, possible labels
are likely and unlikely. Redshift ML provides the capability of probability metrics, which assign a probability to
each label to indicate its likelihood. This helps you make more informed decisions based on the predicted outcomes.
In Amazon Redshift ML, probability metrics are available when creating AUTO ON models with a problem type of either
binary classification or multiclass classification. If you omit the AUTO ON parameter, Redshift ML assumes that the
model should have AUTO ON.

### Create the model

When creating a model, Amazon Redshift automatically detects the model type and problem type. If it is a classification problem,
Redshift automatically creates a second inference function that you can use to output probabilities relative to each
label. This second inference function's name is your specified inference function name followed by the string `_probabilities`.
For example, if you name your inference function as `customer_churn_predict`, then the second inference function's name
is `customer_churn_predict_probabilities`. You can then query this function to get the probabilities of each label.

```
CREATE MODEL customer_churn_model
FROM customer_activity
    PROBLEM_TYPE BINARY_CLASSIFICATION
TARGET churn
FUNCTION customer_churn_predict
IAM_ROLE {default}
AUTO ON
SETTINGS ( S3_BUCKET 'amzn-s3-demo-bucket'
```

### Get probabilities

Once the probability function is ready, running the command returns a
[SUPER type](r_SUPER_type.md "r_SUPER_type.md") that contains arrays
of the returned probabilities and their associated labels. For example,
the result `"probabilities" : [0.7, 0.3], "labels" : ["False.", "True."]`
means that the False label has a probability of 0.7, and the True label has a probability of 0.3.

```
SELECT customer_churn_predict_probabilities(Account_length, Area_code,
            VMail_message, Day_mins, Day_calls, Day_charge,Eve_mins, Eve_calls,
            Eve_charge, Night_mins, Night_calls, Night_charge,Intl_mins, Intl_calls,
            Intl_charge, Cust_serv_calls)
FROM customer_activity;

customer_churn_predict_probabilities
 --------------------
 {"probabilities" : [0.7, 0.3], "labels" : ["False.", "True."]}
 {"probabilities" : [0.8, 0.2], "labels" : ["False.", "True."]}
 {"probabilities" : [0.75, 0.25], "labels" : ["True.", "False"]}

```

The probabilities and labels arrays are always sorted by their probabilities in descending order.
You can write a query to return just the predicted label with the highest probability by unnesting the
SUPER returned results of the probability function.

```
SELECT prediction.labels[0], prediction.probabilities[0]
            FROM (SELECT customer_churn_predict_probabilities(Account_length, Area_code,
            VMail_message, Day_mins, Day_calls, Day_charge,Eve_mins, Eve_calls,
            Eve_charge, Night_mins, Night_calls, Night_charge,Intl_mins, Intl_calls,
            Intl_charge, Cust_serv_calls) AS prediction
FROM customer_activity);

  labels   | probabilities
-----------+--------------
 "False."  | 0.7
 "False."  | 0.8
 "True."   | 0.75

```

To make the queries simpler, you can store the results of the prediction function in a table.

```
CREATE TABLE churn_auto_predict_probabilities AS
             (SELECT customer_churn_predict_probabilities(Account_length, Area_code,
             VMail_message, Day_mins, Day_calls, Day_charge,Eve_mins, Eve_calls,
             Eve_charge, Night_mins, Night_calls, Night_charge,Intl_mins,
             Intl_calls, Intl_charge, Cust_serv_calls) AS prediction
FROM customer_activity);

```

You can query the table with the results to return only predictions that have a probability higher than 0.7.

```
SELECT prediction.labels[0], prediction.probabilities[0]
FROM churn_auto_predict_probabilities
WHERE prediction.probabilities[0] > 0.7;

  labels   | probabilities
-----------+--------------
 "False."  | 0.8
 "True."   | 0.75

```

Using index notation, you can get the probability of a specific label.
The following example returns probabilities of all the `True.` labels.

```
SELECT label, index, p.prediction.probabilities[index]
FROM churn_auto_predict_probabilities p, p.prediction.labels AS label AT index
WHERE label='True.';

  label  | index | probabilities
---------+-------+---------------
 "True." |     0 | 0.3
 "True." |     0 | 0.2
 "True." |     0 | 0.75

```

The following example returns all rows that have a `True`. label with
a probability greater than 0.7, indicating that the customer is likely to churn.

```
SELECT prediction.labels[0], prediction.probabilities[0]
FROM churn_auto_predict_probabilities
WHERE prediction.probabilities[0] > 0.7 AND prediction.labels[0] = "True.";

labels     | probabilities
-----------+--------------
 "True."   | 0.75

```
