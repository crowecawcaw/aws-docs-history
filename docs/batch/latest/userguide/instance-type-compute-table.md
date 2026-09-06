

# Instance type compute table
<a name="instance-type-compute-table"></a>

The following table lists the AWS Region, instance family keyword, and available instance families. AWS Batch will try to allocate an instance from the latest family but because instance family availability varies by AWS Region you may get an earlier instance family generation. 


**default\_x86\_64**  

| Region | Instance families | 
| --- | --- | 
| All AWS Regions that support [AWS Batch](https://docs.aws.amazon.com/general/latest/gr/batch.html) | m6i, c6i, r6i<br />c7i | 


**default\_arm64**  

| Region | Instance families | 
| --- | --- | 
| All AWS Regions that support [AWS Batch](https://docs.aws.amazon.com/general/latest/gr/batch.html) | m6g, c6g, r6g<br />c7g | 


**optimal**  

| Region | Instance families | 
| --- | --- | 
| All AWS Regions that support [AWS Batch](https://docs.aws.amazon.com/general/latest/gr/batch.html) | Modern m, c, and r instance families based on regional availability. AWS Batch periodically updates the pool with newer generations within these families. | 