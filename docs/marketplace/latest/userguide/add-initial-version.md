# Step 3: Add initial product version

This page guides you through adding the initial version of your product. Your product may
have multiple versions throughout its lifecycle, and each version is identified by a unique
SageMaker AI ARN.

1. Under **Amazon Resource Names (ARNs)**:
   1. Enter the model or algorithm Amazon SageMaker AI ARN.
      - Example model package ARN:
        `arn:aws:sagemaker:`<region>`:`<account-id>`:model-package/`<model-package-name>``

      To find your model package ARN, see [My marketplace model packages](https://console.aws.amazon.com/sagemaker/home#/model-packages/my-resources "https://console.aws.amazon.com/sagemaker/home#/model-packages/my-resources").
      - Example algorithm ARN:
        `arn:aws:sagemaker:`<region>`:`<account-id>`:algorithm/`<algorithm-name>``

      To find your algorithm resource ARN, see [My algorithms](https://console.aws.amazon.com/sagemaker/home#/algorithms/my-resources "https://console.aws.amazon.com/sagemaker/home#/algorithms/my-resources").

   2. Enter the IAM access role ARN.

   Example IAM ARN:
   `arn:aws:iam::`<account-id>`:role/`<role-name>``

2. Under **Version information**, enter a **Version name**
   and **Release notes.**.
3. Under **Model input details**, enter a summary of the model inputs
   and provide sample input data for real-time and batch job inputs. Optionally, you can provide any input limitations.
4. (Optional) Under **Input parameters**, provide detailed information about each input parameter supported by your product.
   You can provide the parameter name, a description, constraints, and specify if the parameter is required or optional.
   You can provide up to 24 input parameters.
5. (Optional) Under **Custom attributes**, provide any custom invocation parameters supported by your product.
   For each attribute, you can provide a name, description, constraints, and specify if the attribute is required or optional.
6. Under **Model output details**, enter a summary of the model outputs
   and provide sample output data for real-time and batch job outputs. Optionally, you can provide any output limitations.
7. (Optional) Under **Output parameters**, provide detailed information about each output parameter supported by your product.
   You can provide the parameter name, a description, constraints, and specify if the parameter is required or optional.
   You can provide up to 24 output parameters.
8. Under **Usage instructions**, provide clear instructions for using your model
   effectively such as best practices, how to handle common edge cases, or performance optimization suggestions.
9. Under **Git repository and notebook links**, provide links to example notebooks and
   Git repository. Sample notebooks should include how to invoke your model. Your Git repository should include
   notebooks, data files, and other developer tools.
10. Under **Recommended instance types**, select the recommended instance types for your product.

For _model packages_, you'll select recommended instance types for both batch transform and real-time inference.

For _algorithm packages_, you'll select the recommended instance type for training jobs.

###### Note

The instance types available to select are limited to those supported by your model or algorithm package.
These supported instance types were determined when you initially created your resources in Amazon SageMaker AI. This ensures
that your product is only associated with hardware configurations that can effectively run your machine learning solution. 11. Choose **Next** to move to the next step in the
wizard.
