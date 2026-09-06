

After careful consideration, we have decided to discontinue Amazon Kinesis Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md).

# Step 1: Prepare the Data
<a name="tworecordtypes-prepare"></a>

In this section, you create a Kinesis data stream, and then populate order and trade records on the stream. This is your streaming source for the application that you create in the next step.

**Topics**
+ [Step 1.1: Create a Streaming Source](#tworecordtypes-prepare-create-stream)
+ [Step 1.2: Populate the Streaming Source](#tworecordtypes-prepare-populate-stream)

## Step 1.1: Create a Streaming Source
<a name="tworecordtypes-prepare-create-stream"></a>

You can create a Kinesis data stream using the console or the AWS CLI. The example assumes `OrdersAndTradesStream` as the stream name. 
+ **Using the console** – Sign in to the AWS Management Console and open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis). Choose **Data Streams**, and then create a stream with one shard. For more information, see [Create a Stream](https://docs.aws.amazon.com/streams/latest/dev/learning-kinesis-module-one-create-stream.html) in the *Amazon Kinesis Data Streams Developer Guide*.
+ **Using the AWS CLI** – Use the following Kinesis `create-stream` AWS CLI command to create the stream:

  ```
  $ aws kinesis create-stream \
  --stream-name {{OrdersAndTradesStream}} \
  --shard-count 1 \
  --region us-east-1 \
  --profile adminuser
  ```

## Step 1.2: Populate the Streaming Source
<a name="tworecordtypes-prepare-populate-stream"></a>

Run the following Python script to populate sample records on the `OrdersAndTradesStream`. If you created the stream with a different name, update the Python code appropriately. 

1. Install Python and `pip`.

   For information about installing Python, see the [Python](https://www.python.org/) website. 

   You can install dependencies using pip. For information about installing pip, see [Installation](https://pip.pypa.io/en/stable/installing/) on the pip website.

1. Run the following Python code. The `put-record` command in the code writes the JSON records to the stream.

   ```
    
   import json
   import random
   import boto3
   
   STREAM_NAME = "OrdersAndTradesStream"
   PARTITION_KEY = "partition_key"
   
   
   def get_order(order_id, ticker):
       return {
           "RecordType": "Order",
           "Oid": order_id,
           "Oticker": ticker,
           "Oprice": random.randint(500, 10000),
           "Otype": "Sell",
       }
   
   
   def get_trade(order_id, trade_id, ticker):
       return {
           "RecordType": "Trade",
           "Tid": trade_id,
           "Toid": order_id,
           "Tticker": ticker,
           "Tprice": random.randint(0, 3000),
       }
   
   
   def generate(stream_name, kinesis_client):
       order_id = 1
       while True:
           ticker = random.choice(["AAAA", "BBBB", "CCCC"])
           order = get_order(order_id, ticker)
           print(order)
           kinesis_client.put_record(
               StreamName=stream_name, Data=json.dumps(order), PartitionKey=PARTITION_KEY
           )
           for trade_id in range(1, random.randint(0, 6)):
               trade = get_trade(order_id, trade_id, ticker)
               print(trade)
               kinesis_client.put_record(
                   StreamName=stream_name,
                   Data=json.dumps(trade),
                   PartitionKey=PARTITION_KEY,
               )
           order_id += 1
   
   
   if __name__ == "__main__":
       generate(STREAM_NAME, boto3.client("kinesis"))
   ```



**Next Step**  
 [Step 2: Create the Application](tworecordtypes-create-app.md)