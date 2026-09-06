

We are no longer updating the Amazon Machine Learning service or accepting new users for it. This documentation is available for existing users, but we are no longer updating it. For more information, see [ What is Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html).

# Step 1: Prepare Your Data
<a name="step-1-download-edit-and-upload-data"></a>

In machine learning, you typically obtain the data and ensure that it is well formatted before starting the training process. For the purposes of this tutorial, we obtained a sample dataset from the [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/), formatted it to conform to Amazon ML guidelines, and made it available for you to download. Download the dataset from our Amazon Simple Storage Service (Amazon S3) storage location and upload it to your own S3 bucket by following the procedures in this topic.

 For Amazon ML formatting requirements, see [Understanding the Data Format for Amazon ML](understanding-the-data-format-for-amazon-ml.md).

**To download the datasets**

1. Download the file that contains the historical data for customers who have purchased products similar to your bank term deposit by clicking [banking.zip](samples/banking.zip). Unzip the folder and save the banking.csv file to your computer.

1. Download the file that you will use to predict whether potential customers will respond to your offer by clicking [banking-batch.zip](samples/banking-batch.zip). Unzip the folder and save the banking-batch.csv file to your computer.

1.  Open `banking.csv`. You will see rows and columns of data. The *header row* contains the attribute names for each column. An *attribute* is a unique, named property that describes a particular characteristic of each customer; for example, nr\_employed indicates the customer's employment status. Each row represents the collection of observations about a single customer.   
![CSV file showing header row with column names euribor3m, nr_employed, and y above data rows.](http://docs.aws.amazon.com/machine-learning/latest/dg/images/image1.png)

   You want your ML model to answer the question "Will this customer subscribe to my new product?". In the `banking.csv` dataset, the answer to this question is attribute **y**, which contains the values 1 (for yes) or 0 (for no). The attribute that you want Amazon ML to learn how to predict is known as the *target attribute*. 
**Note**  
Attribute **y** is a binary attribute. It can contain only one of two values, in this case 0 or 1. In the original UCI dataset, the **y** attribute is either Yes or No. We have edited the original dataset for you. All values of attribute **y** that mean yes are now 1, and all values that mean no are now 0. If you use your own data, you can use other values for a binary attribute. For more information about valid values, see [Using the AttributeType Field](creating-a-data-schema-for-amazon-ml.md#assigning-data-types).

 The following examples show the data before and after we changed the values in attribute **y** to the binary attributes 0 and 1. 

![CSV file showing euribor3m and nr_employed columns with y values transformed from yes/no to 1/0.](http://docs.aws.amazon.com/machine-learning/latest/dg/images/image2.png)


![Data transformation showing banking.csv file with columns euribor3m, nr_employed, and y displayed.](http://docs.aws.amazon.com/machine-learning/latest/dg/images/image3.png)


 The `banking-batch.csv` file doesn’t contain the **y** attribute. After you have created an ML model, you will use the model to predict **y** for each record in that file. 

 Next, upload the `banking.csv `and `banking-batch.csv` files to Amazon S3. 

**To upload the files to an Amazon S3 location**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1.  In the **All Buckets** list, create a bucket or choose the location where you want to upload the files.

1. In the navigation bar, choose **Upload**. 

1. Choose **Add Files**. 

1.  In the dialog box, navigate to your desktop, choose `banking.csv` and `banking-batch.csv`, and then choose **Open**. 

 Now you are ready to [create your training datasource](step-2-create-a-datasource.md). 