

# PipeTargetKinesisStreamParameters
<a name="API_PipeTargetKinesisStreamParameters"></a>

The parameters for using a Kinesis stream as a target.

## Contents
<a name="API_PipeTargetKinesisStreamParameters_Contents"></a>

 ** PartitionKey **   <a name="eventbridge-Type-PipeTargetKinesisStreamParameters-PartitionKey"></a>
Determines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis Data Streams uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: Yes

## See Also
<a name="API_PipeTargetKinesisStreamParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/PipeTargetKinesisStreamParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetKinesisStreamParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetKinesisStreamParameters) 