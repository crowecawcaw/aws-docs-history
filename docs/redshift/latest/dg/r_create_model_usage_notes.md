Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Usage notes

When using CREATE MODEL, consider the following:

- The CREATE MODEL statement operates in an asynchronous mode and returns upon
  the export of training data to Amazon S3. The remaining steps of training in Amazon SageMaker AI
  occur in the background. While training is in progress, the corresponding
  inference function is visible but can't be run. You can query [STV_ML_MODEL_INFO](r_STV_ML_MODEL_INFO.md "r_STV_ML_MODEL_INFO.md") to see the
  state of training.
- The training can run for up to 90 minutes in the background, by default in the
  Auto model and can be extended. To cancel the training, simply run the [DROP MODEL](r_DROP_MODEL.md "r_DROP_MODEL.md") command.
- The Amazon Redshift cluster that you use to create the model and the Amazon S3 bucket that
  is used to stage the training data and model artifacts must be in the same AWS
  Region.
- During the model training, Amazon Redshift and SageMaker AI store intermediate artifacts in
  the Amazon S3 bucket that you provide. By default, Amazon Redshift performs garbage collection
  at the end of the CREATE MODEL operation. Amazon Redshift removes those objects from
  Amazon S3. To retain those artifacts on Amazon S3, set the S3_GARBAGE COLLECT OFF
  option.
- You must use at least 500 rows in the training data provided in the FROM
  clause.
- You can only specify up to 256 feature (input) columns in the FROM { table_name
  | ( select_query ) } clause when using the CREATE MODEL statement.
- For AUTO ON, the column types that you can use as the training set are
  SMALLINT, INTEGER, BIGINT, DECIMAL, REAL, DOUBLE, BOOLEAN, CHAR, VARCHAR, DATE,
  TIME, TIMETZ, TIMESTAMP, and TIMESTAMPTZ. For AUTO OFF, the column types that you
  can use as the training set are SMALLINT, INTEGER, BIGINT, DECIMAL, REAL, DOUBLE,
  and BOOLEAN.
- You can't use DECIMAL, DATE, TIME, TIMETZ, TIMESTAMP, TIMESTAMPTZ,
  GEOMETRY, GEOGRAPHY, HLLSKETCH, SUPER, or VARBYTE as the target column
  type.
- To improve model accuracy, do one of the following:
  - Add as many relevant columns in the CREATE MODEL command as possible when
    you specify the training data in the FROM clause.
  - Use a larger value for MAX_RUNTIME and MAX_CELLS. Larger values for this
    parameter increase the cost of training a model.

- The CREATE MODEL statement execution returns as soon as the training data is
  computed and exported to the Amazon S3 bucket. After that point, you can check the
  status of the training using the SHOW MODEL command. When a model being trained in
  the background fails, you can check the error using SHOW MODEL. You can't
  retry a failed model. Use DROP MODEL to remove a failed model and recreate a new
  model. For more information about SHOW MODEL, see [SHOW MODEL](r_SHOW_MODEL.md "r_SHOW_MODEL.md").
- Local BYOM supports the same kind of models that Amazon Redshift ML supports for
  non-BYOM cases. Amazon Redshift supports plain XGBoost (using XGBoost version 1.0 or
  later), KMEANS models without preprocessors, and XGBOOST/MLP/Linear Learner models
  trained by trained by Amazon SageMaker AI Autopilot. It supports the latter with
  preprocessors that Autopilot has specified that are also supported by Amazon SageMaker AI
  Neo.
- If your Amazon Redshift cluster has enhanced routing enabled for your virtual private
  cloud (VPC), make sure to create an Amazon S3 VPC endpoint and an SageMaker AI VPC endpoint for
  the VPC that your cluster is in. Doing this enables the traffic to run through
  your VPC between these services during CREATE MODEL. For more information, see
  [SageMaker AI Clarify Job Amazon VPC Subnets and Security Groups](../../../sagemaker/latest/dg/clarify-vpc.md#clarify-vpc-job "../../../sagemaker/latest/dg/clarify-vpc.md#clarify-vpc-job").
