# Get project details

An Amazon SageMaker Unified Studio project contains essential configuration details that you may need to access
for various development, deployment, and administrative tasks. The following section provides
information on how to navigate to your **Project details** page, which
includes key information and metadata. The **Project details** page
includes:

- Project ID
- Project role ARN
- Amazon S3 location
- Domain unit name
- Domain ID

###### To navigate to your **Project details** page

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in using your IAM Identity Center (SSO)
   or AWS credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
2. If not open already, navigate to the Amazon SageMaker Unified Studio home page by choosing the icon located
   at the top left corner of the page.
3. Under **Your projects**, choose your project.
4. If not open already, choose the **Project details** tab.

## View the SageMaker AI domain details associated

with your project

A SageMaker AI domain is created for your Amazon SageMaker Unified Studio Project. You may need to update your
SageMaker AI domain to update your Amazon SageMaker Unified Studio Project. Use the following instructions to get the
associated SageMaker AI domain details.

###### Note

The domain ID in [Get project details](view-project-details.md "view-project-details.md") is _not_ the same as your
SageMaker AI domain ID.

###### To get your SageMaker AI domain details

1. Navigate to your **Project details** tab. For more information, see
   [Get project details](view-project-details.md "view-project-details.md").
2. Copy your **Project ID**.
3. Navigate to the [Amazon Amazon SageMaker AI
   console](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker").
4. Expand the **Admin configurations** section.
5. Under **Admin configurations**, choose
   **Domains**.
6. From the list of domains, find the domain name that contains the **Project
   ID** you copied above. You can use the search function on that page.
7. Choose the hyperlink of your domain to view your **Domain
   details**.
