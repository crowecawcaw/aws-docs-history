# Create a Model Package

Resource

To create a model package resource that you can use to create deployable models in
Amazon SageMaker AI and publish on AWS Marketplace specify the following information:

- The Docker container that contains the inference code, or the algorithm
  resource that was used to train the model.
- The location of the model artifacts. Model artifacts can either be
  packaged in the same Docker container as the inference code or stored in
  Amazon S3.
- The instance types that your model package supports for both real-time
  inference and batch transform jobs.
- Validation profiles, which are batch transform jobs that SageMaker AI runs to test
  your model package's inference code.

Before listing model packages on AWS Marketplace, you must validate them. This
ensures that buyers and sellers can be confident that products work in
Amazon SageMaker AI. You can list products on AWS Marketplace only if validation
succeeds.

The validation procedure uses your validation profile and sample data to
run the following validations tasks:

    1. Create a model in your account using the model package's inference
     image and the optional model artifacts that are stored in
     Amazon S3.


    ###### Note

    A model package is specific to the region in which you create
     it. The S3 bucket where the model artifacts are stored must be
     in the same region where your created the model package.
    2. Create a transform job in your account using the model to verify
     that your inference image works with SageMaker AI.
    3. Create a validation profile.

###### Note

In your validation profile, provide only data that you want to expose
publicly.

Validation can take up to a few hours. To see the status of the jobs in
your account, in the SageMaker AI console, see the **Transform
jobs** pages. If validation fails, you can access the scan and
validation reports from the SageMaker AI console. After fixing issues, recreate the
algorithm. When the status of the algorithm is `COMPLETED`, find
it in the SageMaker AI console and start the listing process

###### Note

To publish your model package on AWS Marketplace, at least one validation
profile is required.
You can create an model package either by using the SageMaker AI console or by using the
SageMaker API.

###### Topics

- [Create a Model Package
  Resource (Console)](#sagemaker-mkt-create-model-pkg-console "#sagemaker-mkt-create-model-pkg-console")
- [Create a Model Package
  Resource (API)](#sagemaker-mkt-create-model-pkg-api "#sagemaker-mkt-create-model-pkg-api")

## Create a Model Package

Resource (Console)

###### To create a model package in the SageMaker AI console:

1.  Open the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2.  From the left menu, choose **Inference**.
3.  Choose **Marketplace model packages**, then choose
    **Create marketplace model package**.
4.  On the **Inference specifications** page, provide the
    following information:
    1. For **Model package name**, type a name for
       your model package. The model package name must be unique in
       your account and in the AWS region. The name must have 1 to 64
       characters. Valid characters are a-z, A-Z, 0-9, and -
       (hyphen).
    2. Type a description for your model package. This description
       appears in the SageMaker AI console and in the AWS Marketplace.
    3. For **Inference specification options**,
       choose **Provide the location of the inference image and
       model artifacts** to create a model package by
       using an inference container and model artifacts. Choose
       **Provide the algorithm used for training and its
       model artifacts** to create a model package from an
       algorithm resource that you created or subscribe to from
       AWS Marketplace.
    4. If you chose **Provide the location of the inference
       image and model artifacts** for **Inference
       specification options**, provide the following
       information for **Container definition** and
       **Supported resources**:
       1. For **Location of inference image**,
          type the path to the image that contains your inference
          code. The image must be stored as a Docker container in
          Amazon ECR.
       2. For **Location of model data
          artifacts**, type the location in S3 where
          your model artifacts are stored.
       3. For **Container DNS host name** ,
          type the name of the DNS host to use for your
          container.
       4. For **Supported instance types for real-time
          inference**, choose the instance types that
          your model package supports for real-time inference from
          SageMaker AI hosted endpoints.
       5. For **Supported instance types for batch
          transform jobs**, choose the instance types
          that your model package supports for batch transform
          jobs.
       6. **Supported content types**, type the
          content types that your model package expects for
          inference requests.
       7. For **Supported response MIME
          types**, type the MIME types that your model
          package uses to provide inferences.

    5. If you chose **Provide the algorithm used for training
       and its model artifacts** for **Inference
       specification options**, provide the following
       information:
       1. For **Algorithm ARN**, type the
          Amazon Resource Name (ARN) of the algorithm resource to
          use to create the model package.
       2. For **Location of model data
          artifacts**, type the location in S3 where
          your model artifacts are stored.

    6. Choose **Next**.

5.  On the **Validation and scanning** page, provide the
    following information:
    1. For **Publish this model package on AWS Marketplace**,
       choose **Yes** to publish the model package on
       AWS Marketplace.
    2. For **Validate this resource**, choose
       **Yes** if you want SageMaker AI to run batch transform jobs
       that you specify to test the inference code of your model package.

    ###### Note

    To publish your model package on AWS Marketplace, your model package
    must be validated. 3. For **IAM role**, choose an IAM role that
    has the required permissions to run batch transform jobs in
    SageMaker AI, or choose **Create a new role** to allow
    SageMaker AI to create a role that has the
    `AmazonSageMakerFullAccess` managed policy
    attached. For information, see [How to use SageMaker AI execution roles](sagemaker-roles.md "sagemaker-roles.md"). 4. For **Validation profile**, specify the
    following:

        * A name for the validation profile.
        * A **Transform job definition**. This
         is a JSON block that describes a batch transform job.
         This is in the same format as the [`TransformJobDefinition`](../APIReference/API_TransformJobDefinition.md "../APIReference/API_TransformJobDefinition.md") input
         parameter of the [`CreateAlgorithm`](../APIReference/API_CreateAlgorithm.md "../APIReference/API_CreateAlgorithm.md") API.

6.  Choose **Create marketplace model package**.

## Create a Model Package

Resource (API)

To create a model package by using the SageMaker API, call the [`CreateModelPackage`](../APIReference/API_CreateModelPackage.md "../APIReference/API_CreateModelPackage.md")
API.
