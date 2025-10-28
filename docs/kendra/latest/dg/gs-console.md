# Getting started with the Amazon Kendra console

The following procedures show how to create and test an Amazon Kendra index by using
the AWS console. In the procedures you create an index and a data source for an
index. Finally, you test your index by making a search request.

###### Step 1: To create an index (console)

1. Sign in to the AWS Management Console and open the Amazon Kendra
   console at [https://console.aws.amazon.com/kendra/](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. Select **Create index** in the **Indexes**
   section.
3. In the **Specify index details** page, give your index a name and a
   description.
4. In **IAM role**, choose **Create a new
   role** and then give the role a name. The IAM role will have the
   prefix "AmazonKendra-".
5. Leave all of the other fields at their defaults. Choose
   **Next**.
6. In the **Configure user access control** page, choose
   **Next**.
7. In the **Provisioning details** page, choose **Developer
   edition**.
8. Choose **Create** to create your index.
9. Wait for your index to be created. Amazon Kendra provisions the hardware for your
   index. This operation can take some time.

###### Step 2: To add a data source to an index (console)

1. View the available [data sources](data-source.md "data-source.md") to connect Amazon Kendra to and index your documents.
2. In the navigation pane, select **Data sources** and then select
   **Add data source** for your chosen data source.
3. Follow the steps to configure the data source.

###### Step 3: To search an index (console)

1. In the navigation pane, choose the option to search your index.
2. Enter a search term that's appropriate for your index. The **top
   results** and **top document** results are shown.
