# Domo limitations

The following are limitations or notes for Domo:

- Due to an SDK limitation, filtration does not work as expected for the queryable fields that starts with '\_' (for example: \_BATCH_ID ).
- Due to an API limitation, filtration works on the date prior to the date you provide. This also affects incremental pull. To overcome this limitation, select a date according to your time zone against UTC, for getting data for the required date.
