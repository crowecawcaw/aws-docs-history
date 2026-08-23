# Recovery by rolling back unwanted writes in-place

To keep the original table in service, you can roll back unwanted writes directly rather
than restoring a full table. You can roll back all the writes or only those writes that you
identify as mistakes.

Before you begin, make sure that PITR is enabled on the table and that the time period
of the unwanted writes falls within the PITR recovery window.

This approach uses the incremental export to Amazon Simple Storage Service (Amazon S3) feature. An incremental export
writes the changed items to Amazon S3. The export includes each item's old and new images. The time
period can be as short as 15 minutes or as long as 24 hours. The time period must be contained
within the PITR recovery window.

###### To roll back unwanted writes

1. Perform an incremental export to Amazon S3. Specify the time period during which the erroneous
   writes were happening to the table. Select an export view of "new and old images". If the time
   period exceeds 24 hours, do multiple incremental export jobs that together cover the full time
   period exactly.
2. Drive a bulk job off the Amazon S3 data to reverse the changes listed in the export by writing
   the old item value back. Optionally apply a transformation to control exactly what gets undone
   and how (such as to correct minor mistakes on the items).
   This approach provides the following advantages:

- More cost effective, especially for large tables. Instead of restoring a full table to
  undo a small number of mistaken writes, you focus on just the mistakes.
- Faster, especially for large tables. Only a subset of table data must be
  processed.
- Live, in-place correction. The original table remains active during the correction. No
  need to adjust a new table's metadata, settings, and external references.
