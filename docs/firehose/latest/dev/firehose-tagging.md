# Tag a Firehose stream

You can assign your own metadata to Firehose streams that you create in Amazon Data Firehose in the form of
_tags_. A tag is a key-value pair that you define for a stream. Using
tags is a simple yet powerful way to manage AWS resources and organize data, including
billing data.

You can specify tags when you invoke [CreateDeliveryStream](../APIReference/API_CreateDeliveryStream.md "../APIReference/API_CreateDeliveryStream.md") to create a new Firehose stream. For existing Firehose streams,
you can add, list, and remove tags using the following three operations:

- [TagDeliveryStream](../APIReference/API_TagDeliveryStream.md "../APIReference/API_TagDeliveryStream.md")
- [ListTagsForDeliveryStream](../APIReference/API_ListTagsForDeliveryStream.md "../APIReference/API_ListTagsForDeliveryStream.md")
- [UntagDeliveryStream](../APIReference/API_UntagDeliveryStream.md "../APIReference/API_UntagDeliveryStream.md")
