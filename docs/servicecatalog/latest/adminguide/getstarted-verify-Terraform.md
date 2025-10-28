# Step 9: Test the end user experience

To verify end users can successfully access the end user console view and launch your
`Simple S3 bucket` product, sign in to AWS as the end user
and perform the tasks below.

###### To verify that the end user can access the end user console

- Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/") to see:
  - **Products** – The products that the user can use.
  - **Provisioned products** – The provisioned
    products that the user has launched.

###### To verify the end user can launch the Terraform product

1. In the **Products** section of the console, choose
   **Simple S3 bucket**.
2. Choose **Launch product** to start the wizard that configures your product.
3. On the **Launch Simple S3 bucket** page, enter
   `Amazon S3 product` for the provisioned product name.
4. On the **Parameters** page, enter the following and choose
   **Next**:
   - **bucket_name** – Provide a unique name for the Amazon S3 bucket. For example,
     `terraform-s3-product`.

5. Choose **Launch product**. The console
   displays the stack details page for the Amazon S3 product launch. The initial status of the
   product is **Under change**. It takes several minutes for AWS Service Catalog to
   launch the product. To see the current status, refresh your browser. After a successful product launch,
   the status is **Available**.

AWS Service Catalog creates a new Amazon S3 bucket named `terraform-s3-product`.
