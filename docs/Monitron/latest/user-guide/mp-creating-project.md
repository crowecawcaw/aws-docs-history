Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Creating a project

Although an AWS account can have multiple Amazon Monitron projects,
typically you have one per account. The project name must be unique in your AWS account and AWS Region.

###### To create a project

1. Open the Amazon Monitron console at [https://console.aws.amazon.com/monitron](https://console.aws.amazon.com/monitron/ "https://console.aws.amazon.com/monitron/").
2. Choose **Create Project**.
3. Under **Project Details**, for **Project
   name**, enter a name that:
   - Is unique in the current account
   - Consists of uppercase and lowercase letters, numbers, punctuation
     marks, and spaces
   - Is between 1 and 60 characters

4. By default, Amazon Monitron uses an AWS owned key to encrypt your project
   through the AWS Key Management Service (AWS KMS). If you want to use a different AWS KMS key, choose
   **Custom encryption settings (advanced)** under
   **Data encryption** and do one of the following:
   - If you already have a AWS KMS key that you want to use, under
     **Choose an AWS AWS KMS key**, choose
     the key or enter the key's Amazon Resource Name (ARN).
   - If you want to create a key, choose **Create an AWS AWS KMS key**. This takes you to the AWS KMS
     console so you can set up a custom key.

5. (Optional) To add a tag to the project, enter a key-value pair under
   **Tags** and then choose **Add tag**. To
   remove this tag before creating the project, choose **Remove
   tag**.
6. Choose **Next** to create the project.
