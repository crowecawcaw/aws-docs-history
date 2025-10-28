# Blackbaud Raiser's Edge NXT limitations

The following are limitations or notes for Blackbaud Raiser's Edge NXT:

- The SaaS only supports the `EQUAL_TO` operator, which returns results created or modified on or after the specified date. Additionally, the "id" field is a String data type. There is also no identification of non-nullable fields. Therefore, field-based partitioning is not supported.
- Incremental pull is only supported by the `Event` entity with daily, monthly and weekly frequencies.
- The Constituent Fundraiser Assignment entity returns a maximum of 20 records.
- Record-based partitioning:
  - Not supported by the `Action`, `Constituent Fundraiser Assignment` or `Gift Batch` entities.
  - Record-based partitioning with the filter predicate is only supported by the `Event` and `Event Participant` entities. If a filter predicate is used with any other record-based supported entities, an exception will be thrown.

- In the `Gift Custom Field` entity, the field 'value' must be used in conjunction with the field 'category', which otherwise leads to an unfiltered response. Thus, to compel the user to plug in the 'category' field while filtering with the 'value' field, an exception will be thrown if the aforementioned requirement has not been followed.
- The `date_added` and `last_modified` fields for all applicable entities do not support any comparative operators. They only support the equal to operator. Also, there is no field that can be paired with the aforementioned fields to provide a range of records. Hence, these fields are only queryable and cannot support incremental transfer.
- The `added_by` field in the `Gift Batch` entity will not be considered as filterable as it might not emit the correct results.
- There is a latency of approximately 30 minutes for records to be retrieved via the `/GET Gift List` endpoint upon insertion of data in the `Gift` entity.
- Support for incremental transfer has been dropped for the Gift entity due to limitations from the data source's end.
- There exists a 10 minute latency for the status field in the Opportunity entity.
- The `Fundraiser Assignment` entity has `Constituent` as the dependent entity. The connector loads at most 5,000 IDs to choose from, to avoid the response size exceeding the maximum allowed payload size.
