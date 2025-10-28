Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Load data in sort key order

Load your data in sort key order to avoid needing to vacuum.

If each batch of new data follows the existing rows in your table, your data is
properly stored in sort order, and you don't need to run a vacuum. You don't need to
presort the rows in each load because COPY sorts each batch of incoming data as it
loads.

For example, suppose that you load data every day based on the current day's
activity. If your sort key is a timestamp column, your data is stored in sort order.
This order occurs because the current day's data is always appended at the end of the
previous day's data. For more information, see [Load your data in sort key order](vacuum-managing-vacuum-times.md#vacuum-load-in-sort-key-order "vacuum-managing-vacuum-times.md#vacuum-load-in-sort-key-order"). For more information about vacuum operations, see [Vacuuming tables](t_Reclaiming_storage_space202.md "t_Reclaiming_storage_space202.md").
