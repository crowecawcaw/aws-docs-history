# Output key template

For Amazon S3 general purpose buckets, the output key template controls the S3 object key (path and file name) of each delivered object. At runtime it is concatenated with the output prefix to form the final S3 key. Use it to organize delivered objects — for example, to partition by Kafka partition, by time, or by topic.

The template is optional. If you don't provide one, the Channel applies a default key layout similar to:

```
!{channel-id}/!{topic-name}/year=!{yyyy}/month=!{MM}/day=!{dd}/hour=!{HH}/!{topic-name}+!{partition-id}+!{kafka-offset}
```

An example S3 object key produced by the default template:

```
myprefix/8309b825-8a2c-4120-9367-6ce96fbd2537-2/kafka-topic-49be6b2117ae746bd1ec6d17be0640cd/year=2026/month=07/day=14/hour=00/kafka-topic-49be6b2117ae746bd1ec6d17be0640cd+0+000000000000000000-000000-105a4e6efaa
```

###### Note

A unique identifier (for example, `-000000-105a4e6efaa` in the example above) is automatically appended to the object key.

If you provide your own template, it must follow the rules below.

###### Topics

- [Variables](msk-data-delivery-s3-template-variables.md "msk-data-delivery-s3-template-variables.md")
- [Partitioning](msk-data-delivery-s3-template-partitioning.md "msk-data-delivery-s3-template-partitioning.md")
- [Rules](msk-data-delivery-s3-template-rules.md "msk-data-delivery-s3-template-rules.md")
- [Examples](msk-data-delivery-s3-template-examples.md "msk-data-delivery-s3-template-examples.md")
