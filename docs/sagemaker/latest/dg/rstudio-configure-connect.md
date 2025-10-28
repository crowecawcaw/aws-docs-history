# Add an RStudio Connect URL

RStudio Connect is a publishing platform for Shiny applications, R Markdown reports,
dashboards, plots, and more. RStudio Connect makes it easy to surface machine learning and data
science insights by making hosting content simple and scalable. If you have an RStudio Connect
server, then you can set the server as the default place where apps are published. For more
information about RStudio Connect, see [RStudio Connect](https://www.rstudio.com/products/connect/ "https://www.rstudio.com/products/connect/").

When you onboard to RStudio on Amazon SageMaker AI domain, an RStudio Connect server is not created. You
can create an RStudio Connect server on an Amazon EC2 instance to use Connect with Amazon SageMaker AI domain.
For information about how to set up your RStudio Connect server, see [Host RStudio Connect and Package Manager for ML development in RStudio on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/host-rstudio-connect-and-package-manager-for-ml-development-in-rstudio-on-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/host-rstudio-connect-and-package-manager-for-ml-development-in-rstudio-on-amazon-sagemaker/").

**Add an RStudio Connect URL**

If you have an RStudio Connect URL, you can update the default URL so that your
RStudio Users can publish to it.

1. Navigate to the **domains** page.
2. Select the desired domain.
3. Choose **domain Settings**.
4. Under **General Settings**, select **Edit**.
5. From the new page, select **RStudio Settings** on the left side.
6. Under **RStudio Connect URL**, enter the RStudio Connect URL to add.
7. Select **Submit**.

**CLI**

You can set a default RStudio Connect URL when you create your domain. The only way to
update your RStudio Connect URL from the AWS CLI is to delete your domain and create a new one
with the updated RStudio Connect URL.
