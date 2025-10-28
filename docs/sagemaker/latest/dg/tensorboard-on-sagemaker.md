# TensorBoard in Amazon SageMaker AI

Amazon SageMaker AI with TensorBoard is a capability of Amazon SageMaker AI that brings the [TensorBoard](https://www.tensorflow.org/tensorboard "https://www.tensorflow.org/tensorboard") visualization tools to
SageMaker AI and integrated with SageMaker Training and domain. It provides options to administer
your AWS account and users belonging to the account through [SageMaker AI domain](sm-domain.md "sm-domain.md"), to give the domain
users access to the TensorBoard data with appropriate permissions to Amazon S3, and
help the domain users perform model debugging tasks using the TensorBoard visualization
plugins. SageMaker AI with TensorBoard is extended with the SageMaker AI Data Manager plugin, with which
domain users can access a number of training jobs in one place within the TensorBoard
application.

###### Note

This feature is for debugging the training of deep learning models using PyTorch or
TensorFlow.

**For data scientists**

Training large models can have scientific problems that require data scientists to debug
and resolve them in order to improve model convergence and stabilize gradient descent
processes.

When you encounter model training issues, such as loss not converging, or vanishing or
exploding weights and gradients, you need to access tensor data to dive deep and analyze the
model parameters, scalars, and any custom metrics. Using SageMaker AI with TensorBoard, you can
visualize model output tensors extracted from training jobs. As you experiment with
different models, multiple training runs, and model hyperparameters, you can select multiple
training jobs in TensorBoard and compare them in one place.

**For administrators**

Through the TensorBoard landing page in the SageMaker AI console or [SageMaker AI domain](sm-domain.md "sm-domain.md"), you can manage
TensorBoard application users if you are an administrator of an AWS account or SageMaker AI
domain. Each domain user can access their own TensorBoard application given the
granted permissions. As a SageMaker AI domain administrator and domain user, you can create
and delete the TensorBoard application given the permission level you have.

###### Note

You cannot share the TensorBoard application for collaboration purposes because SageMaker AI
domain does not allow application sharing among users. Users can share the output
tensors saved in an S3 bucket, if they have access to the bucket.

## Supported frameworks and AWS Regions

The TensorBoard application in SageMaker AI is available for the following machine learning
frameworks and AWS Regions.

###### Frameworks

- PyTorch
- TensorFlow
- Hugging Face Transformers

###### AWS Regions

- US East (N. Virginia) (`us-east-1`)
- US East (Ohio) (`us-east-2`)
- US West (Oregon) (`us-west-2`)
- Europe (Frankfurt) (`eu-central-1`)
- Europe (Ireland) (`eu-west-1`)

###### Note

Amazon SageMaker AI with TensorBoard runs on an `ml.r5.large` instance and incurs
charges after the SageMaker AI free tier or the free trial period of the feature. For more
information, see [Amazon SageMaker AI
Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").

###### Topics

- [Prepare a training job to collect
  TensorBoard output data](debugger-htb-prepare-training-job.md "debugger-htb-prepare-training-job.md")
- [Accessing the TensorBoard application on
  SageMaker AI](debugger-htb-access-tb.md "debugger-htb-access-tb.md")
- [Load and visualize output tensors using
  the TensorBoard application](debugger-htb-access-tb-data.md "debugger-htb-access-tb-data.md")
- [Delete unused TensorBoard applications](debugger-htb-delete-app.md "debugger-htb-delete-app.md")
