After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Working in the notebook environment

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

Choosing **Go to Notebook** or **Analyze in Notebook** will open Jupyter Lab in a new tab in your web browser. You will land in the launcher page of SageMaker studio.

###### To start a notebook with FinSpace kernel

1. In the upper-left corner of SageMaker Studio, choose **Amazon SageMaker Studio** to open Studio Launcher.
2. On the **Launcher** page, choose **Notebooks and compute resources**.
3. For **Select a SageMaker image**, choose the FinSpace PySpark image.
4. Choose **Notebook** to create a notebook in the FinSpace PySpark image.

## FinSpace kernel

The FinSpace PySpark Kernel comes with all the libraries required to access and work with data stored in FinSpace, including the Spark Cluster management API and time series analytics library.
The FinSpace Cluster Management API is used to instantiate and connect the notebook instance to a dedicated Spark Cluster. FinSpace Spark clusters use Kerberos authentication for additional
security. FinSpace provides with complete resource isolation when working with Spark Clusters.

When a FinSpace PySpark Kernel is instantiated for the first time in a new notebook session, you can expect a startup time of about 3 to 5 minutes to allow bootstrapping of all dependencies
on the image supporting the notebook.
