

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Parameter Group Characteristics
<a name="parameter-group-characteristics"></a>


**Parameter Group Characteristics**  

| Characteristic | Description | 
| --- | --- | 
| Immutability | Parameter groups are immutable once created. You cannot modify the parameters after creation. | 
| Cloning | You can create a new parameter group by cloning an existing one and modifying the parameters during the cloning process. This is a AWS Management Console only feature. Note: When cloning, gen1-duration, compaction-gen2-duration, compaction-multipliers, and gen1-lookback-duration must be copied unchanged — see [Detailed Parameter Reference](detailed-parameter-reference.md) for details on parameters that must not change after initial setup. | 
| Deletion | Parameter groups cannot be deleted. | 
| Default Groups | Amazon Timestream provides default parameter groups with pre-configured settings optimized for common use cases. | 
| Edition Specificity | Enterprise parameter groups can only be used with Enterprise clusters; Core parameter groups can only be used with Core clusters. | 