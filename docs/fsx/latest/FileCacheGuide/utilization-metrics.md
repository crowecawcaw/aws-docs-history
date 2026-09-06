

# Cache utilization metrics
<a name="utilization-metrics"></a>

The following metrics report cache-level storage information. These metrics take one dimension (`FileCacheId`) and are published into the `AWS/FSx` namespace in CloudWatch.


| Metric | Description | 
| --- | --- | 
| `FreeDataStorageCapacity` | The amount of available data storage capacity.<br />The `Sum` statistic is the total number of bytes available in the cache The `Minimum` statistic is the total number bytes available in the fullest disk. The `Maximum` statistic is the total number of bytes available in the disk with the most remaining available storage. The `Average` statistic is the average number of bytes available per disk. The `SampleCount` statistic is the number of disks.<br />Units:+  Bytes for `Sum`, `Minimum`, `Maximum`. <br />+  Count for `SampleCount`. <br />Valid statistics: `Sum`, `Minimum`, `Maximum`, `Average`, `SampleCount`. | 
| `FreeMetadataStorageCapacity` | The amount of available metadata storage capacity.<br />The `Sum` statistic is the total number of bytes of metadata storage available in the cache. The `Minimum` statistic is the total number of bytes available in the fullest metadata target (MDT) disk. The `Maximum` statistic is the total number of bytes available in the MDT disk with the most remaining storage. The `Average` statistic is the average number of bytes available per MDT disk. The `SampleCount` statistic is the number of MDT disks.<br />Units:+  Bytes for `Sum`, `Minimum`, `Maximum`, `Average`. <br />+  Count for `SampleCount`. <br />Valid statistics: `Sum`, `Minimum`, `Maximum`, `Average`, `SampleCount`. | 