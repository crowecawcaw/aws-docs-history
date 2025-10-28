# Getting started prerequisites

The following steps are prerequisites for the getting started exercises.

1. Set up permissions so Amazon Personalize can access your resources on your behalf. This involves creating a service role for Amazon Personalize
   and granting it access to Amazon Personalize resources with an IAM policy.
   For more information, see [Giving Amazon Personalize permission to access your resources](set-up-required-permissions.md "set-up-required-permissions.md").
2. Prepare your training data and upload the data to your Amazon S3 bucket:
   - For Domain dataset group tutorials, see [Creating the training data (Domain dataset group)](#gs-data-prep-domain "#gs-data-prep-domain").
   - For Custom dataset group tutorials, see [Creating the training data (Custom dataset group)](#gs-upload-to-bucket "#gs-upload-to-bucket").

3. Give your Amazon Personalize service role permission to access your Amazon S3 resources, as specified in [Giving Amazon Personalize access to Amazon S3 resources](granting-personalize-s3-access.md "granting-personalize-s3-access.md").

## Creating the training data (Domain dataset group)

To create training data, download, modify, and save the movie ratings data to an Amazon Simple Storage Service
(Amazon S3) bucket. Then give Amazon Personalize permission to read from the bucket.

###### To create the training data

1. Download and unzip the movie ratings zip file, [ml-latest-small.zip](http://files.grouplens.org/datasets/movielens/ml-latest-small.zip "http://files.grouplens.org/datasets/movielens/ml-latest-small.zip") from [MovieLens](https://grouplens.org/datasets/movielens "https://grouplens.org/datasets/movielens") under _recommended for education and
   development_ (F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context.
   ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19. https://doi.org/10.1145/2827872).
2. Open the `ratings.csv` file. This file contains the interactions data for this tutorial.
   1. Delete the _rating_ column.
   2. Rename the `userId` and `movieId` columns to `USER_ID` and `ITEM_ID` respectively.
   3. Add an EVENT_TYPE column and set the value for every record to `watch`. If you're using Microsoft Excel, you can set the EVENT_TYPE for
      every record by entering `watch` in the first cell in the column and then double-clicking the bottom-right corner of the cell.
      Your header should be the following:

   `USER_ID,ITEM_ID,TIMESTAMP,EVENT_TYPE`

   These columns must be exactly as shown for Amazon Personalize to recognize the
   data. The first few rows of your data should look as follows:

   ````
   USER_ID,ITEM_ID,TIMESTAMP,EVENT_TYPE
   1,1,964982703,watch
   1,3,964981247,watch
   1,6,964982224,watch
   1,47,964983815,watch
   1,50,964982931,watch
   ....
   ....
   ```Save the `ratings.csv` file.
   ````

3. Upload `ratings.csv` to your Amazon S3 bucket. For more information, see
   [Uploading files and folders by using drag and drop](../../../AmazonS3/latest/user-guide/upload-objects.md "../../../AmazonS3/latest/user-guide/upload-objects.md") in the
   Amazon Simple Storage Service User Guide.
4. Give Amazon Personalize permission to read the data in the bucket. For more information,
   see [Giving Amazon Personalize access to Amazon S3 resources](granting-personalize-s3-access.md "granting-personalize-s3-access.md").

## Creating the training data (Custom dataset group)

To create training data, download, modify, and save the movie ratings data to an Amazon Simple Storage Service
(Amazon S3) bucket. Then give Amazon Personalize permission to read from the bucket.

1. Download and unzip the movie ratings zip file, [ml-latest-small.zip](http://files.grouplens.org/datasets/movielens/ml-latest-small.zip "http://files.grouplens.org/datasets/movielens/ml-latest-small.zip") from [MovieLens](https://grouplens.org/datasets/movielens "https://grouplens.org/datasets/movielens") under _recommended for education and
   development_ (F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context.
   ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19. https://doi.org/10.1145/2827872).
2. Open the `ratings.csv` file. This file contains the interactions data for this tutorial.
   1. Delete the _rating_ column.
   2. Replace the header row with the following:

   `USER_ID,ITEM_ID,TIMESTAMP`

   These headers must be exactly as shown for Amazon Personalize to recognize the
   data.Save the `ratings.csv` file.

3. Upload `ratings.csv` to your Amazon S3 bucket. For more information, see
   [Uploading files and folders by using drag and drop](../../../AmazonS3/latest/user-guide/upload-objects.md "../../../AmazonS3/latest/user-guide/upload-objects.md") in the
   Amazon Simple Storage Service User Guide.
4. Give Amazon Personalize permission to read the data in the bucket. For more information,
   see [Giving Amazon Personalize access to Amazon S3 resources](granting-personalize-s3-access.md "granting-personalize-s3-access.md").
