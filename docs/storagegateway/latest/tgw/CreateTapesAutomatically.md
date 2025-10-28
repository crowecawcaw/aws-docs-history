# Allowing Automatic Tape Creation

The Tape Gateway can automatically create new virtual tapes to maintain the minimum
number of available tapes that you configure. It then makes these new tapes available
for import by the backup application so that your backup jobs can run without
interruption. Allowing automatic tape creation removes the need for custom scripting in
addition to the manual process of creating new virtual tapes.

The Tape Gateway spawns a new tape automatically when it has fewer tapes than the
minimum number of available tapes specified for automatic tape creation. A new tape is
spawned when:

- A tape is imported from an import/export slot.
- A tape is imported to the tape drive.
  The gateway maintains a minimum number of tapes with the barcode prefix specified in
  the automatic tape creation policy. If there are fewer tapes than the minimum number of
  tapes with the barcode prefix, the gateway automatically creates enough new tapes to
  equal the minimum number of tapes specified in the automatic tape creation
  policy.

When you eject a tape and it goes into the import/export slot, that tape does not
count toward the minimum number of tapes specified in your automatic tape creation
policy. Only tapes in the import/export slot are counted as being "available." Exporting
a tape does not initiate automatic tape creation. Only imports affect the number of
available tapes.

Moving a tape from the import/export slot to a tape drive or storage slot reduces the
number of tapes in the import/export slot with the same barcode prefix. The gateway
creates new tapes to maintain the minimum number of available tapes for that barcode
prefix.

###### To allow automatic tape creation

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. In the navigation pane, choose the **Gateways** tab.
3. Choose the gateway that you want to automatically create tapes for.
4. In the **Actions** menu, choose **Configure tape
   auto-create**.

The **Tape auto-create** page appears. You can add, change,
or remove tape auto-create options here. 5. To allow automatic tape creation, choose **Add new item**
then configure the settings for automatic tape creation. 6. For **Tape type**, choose **Standard** to
create standard virtual tapes. Choose **WORM** to create
_write-once-read-many_ (WORM) virtual
tapes. For more information, see [Write
Once, Read Many (WORM) Tape Protection](GettingStartedCreateTapes.md#WORM "GettingStartedCreateTapes.md#WORM") . 7. For **Minimum number of tapes**, enter the minimum number of
virtual tapes that should be available on the Tape Gateway at all times. The
valid range for this value is a minimum of 1 and a maximum of 10. 8. For **Capacity**, enter the size, in bytes, of the virtual
tape capacity. The valid range is a minimum of 100 GiB and a maximum of 15
TiB. 9. For **Barcode prefix**, enter the prefix that you want to
prepend to the barcode of your virtual tapes.

###### Note

Virtual tapes are uniquely identified by a barcode, and you can add a
prefix to the barcode. The prefix is optional, but you can use it to help
identify your virtual tapes. The prefix must be uppercase letters (A–Z) and
must be one to four characters long. 10. For **Pool**, choose **Glacier Pool**,
**Deep Archive Pool**, or a custom pool that you have
created. The pool determines the storage class in which your tape is stored when
it is ejected by your backup software.

    * Choose **Glacier Pool** if you want to archive the
     tape in the S3 Glacier Flexible Retrieval storage class. When your backup
     software ejects the tape, it is automatically archived in
     S3 Glacier Flexible Retrieval. You use S3 Glacier Flexible Retrieval for more
     active archives, where you can retrieve a tape typically within 3-5
     hours. For more information, see [Storage classes for archiving objects](../../../AmazonS3/latest/dev/storage-class-intro.md#sc-glacier "../../../AmazonS3/latest/dev/storage-class-intro.md#sc-glacier") in the *Amazon Simple Storage Service User Guide*.
    * Choose **Deep Archive Pool** if you want to archive
     the tape in the S3 Glacier Deep Archive storage class. When your
     backup software ejects the tape, the tape is automatically archived in
     S3 Glacier Deep Archive. You use S3 Glacier Deep Archive
     for long-term data retention and digital preservation, where data is
     accessed once or twice a year. You can retrieve a tape archived in
     S3 Glacier Deep Archive typically within 12 hours. For more
     information, see [Storage classes for archiving objects](../../../AmazonS3/latest/dev/storage-class-intro.md#sc-glacier "../../../AmazonS3/latest/dev/storage-class-intro.md#sc-glacier") in the *Amazon Simple Storage Service User Guide*.
    * Choose a custom pool, if any are available. You configure custom tape
     pools to use either **Deep Archive Pool** or
     **Glacier Pool**. Tapes are archived to the
     configured storage class when they are ejected by your backup software.

If you archive a tape in S3 Glacier Flexible Retrieval, you can move it to
S3 Glacier Deep Archive later. For more information, see [Moving tapes to S3 Glacier Deep Archive
storage class](moving-tapes-vtl.md "moving-tapes-vtl.md").

###### Note

Tapes created before March 27, 2019, are archived directly in
S3 Glacier Flexible Retrieval when your backup software ejects them. 11. When finished configuring settings, choose **Save
changes**. 12. In the navigation pane, choose **Tape Library > Tapes** to
see your tapes. By default, this list displays up to 1,000 tapes at a time, but
the searches that you perform apply to all of your tapes. You can use the search
bar to find tapes that match a specific criteria, or to reduce the list to less
than 1,000 tapes. When your list contains 1,000 tapes or fewer, you can then
sort your tapes in ascending or descending order by various properties.

The status of available virtual tapes is initially set to
**CREATING** when the tapes are being created. After the
tapes are created, their status changes to **AVAILABLE**. For
more information, see [Understanding Tape Status](understand-tapes-status.md "understand-tapes-status.md").

For more information about changing automatic tape creation policies, or
deleting automatic tape creation from a Tape Gateway, see [Managing Automatic Tape
Creation](managing-automatic-tape-creation.md "managing-automatic-tape-creation.md").
