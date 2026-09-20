

# Create an delivery stream
<a name="firehose-redshift-create-akf-delivery-stream"></a>

**To create an Firehose delivery stream for delivering Amazon SNS notifications to Amazon Redshift**

1. Start by following the procedures in [Creating an Firehose delivery stream](https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html) in the *Amazon Data Firehose Developer Guide*. 

1. On the **Choose a destination** page in Firehose, choose **Amazon Redshift**. 

1. Using the [Choose Amazon Redshift for your destination](https://docs.aws.amazon.com/firehose/latest/dev/create-destination.html#create-destination-redshift) section for reference, complete the fields up to the **COPY** fields. 

1. For **COPY options**, paste the following:

   ```
   {
     "jsonpaths": [
       "$.Type",
       "$.MessageId",
       "$.TopicArn",
       "$.Subject",
       "$.Timestamp",
       "$.UnsubscribeURL"
     ]
   }
   ```

1. Choose **Next** and finish creating the delivery stream.

You've created the Firehose delivery stream. To continue, return to the [Task overview](firehose-redshift-destinations.md).