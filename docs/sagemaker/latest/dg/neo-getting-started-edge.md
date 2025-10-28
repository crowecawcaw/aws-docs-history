# Set up Neo on Edge Devices

This guide to getting started with Amazon SageMaker Neo shows you how to compile a model, set up
your device, and make inferences on your device. Most of the code examples use Boto3. We
provide commands using AWS CLI where applicable, as well as instructions on how to satisfy
prerequisites for Neo.

###### Note

You can run the following code snippets on your local machine, within a SageMaker notebook,
within Amazon SageMaker Studio, or (depending on your edge device) on your edge device. The
setup is similar; however, there are two main exceptions if you run this guide within a
SageMaker notebook instance or SageMaker Studio session:

- You do not need to install Boto3.
- You do not need to add the `‘AmazonSageMakerFullAccess’` IAM
  policy
  This guide assumes you are running the following instructions on your edge device.
