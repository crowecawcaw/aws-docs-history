# Creating Tapes Manually

You can create new virtual tapes manually using either the AWS Storage Gateway console or the
Storage Gateway API. The console offers a convenient interface for tape creation with the
flexibility to specify a prefix for a randomly-generated tape barcode. If you need to
fully customize your tape barcodes (for example, to match the serial number of a
corresponding physical tape), you must use the API. For more information on creating
tapes using the Storage Gateway API. see [CreateTapeWithBarcode](../APIReference/API_CreateTapeWithBarcode.md "../APIReference/API_CreateTapeWithBarcode.md") in the _Storage Gateway API
Reference_.

###### To create virtual tapes manually using the Storage Gateway console

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. In the navigation pane, choose the **Gateways** tab.
3. Choose **Create tapes** to open the **Create
   tapes** pane.
4. For **Gateway**, choose a gateway. The tape is created for
   this gateway.
5. For **Tape type**, choose **Standard** to
   create standard virtual tapes. Choose **WORM** to create
   _write once read many_ (WORM) virtual
   tapes. For more information, see [Write
   Once, Read Many (WORM) Tape Protection](GettingStartedCreateTapes.md#WORM "GettingStartedCreateTapes.md#WORM") .
6. For **Number of tapes**, choose the number of tapes that you
   want to create. For more information about tape quotas, see [AWS Storage Gateway quotas](resource-gateway-limits.md "resource-gateway-limits.md").
7. For **Capacity**, enter the size of the virtual tape that you
   want to create. Tapes must be larger than 100 GiB. For information about
   capacity quotas, see [AWS Storage Gateway quotas](resource-gateway-limits.md "resource-gateway-limits.md").
8. For **Barcode prefix**, enter the prefix that you want to
   prepend to the barcode of your virtual tapes.

###### Note

Virtual tapes are uniquely identified by a barcode, and you can add a
prefix to the barcode. You can use a prefix to help identify your virtual
tapes. The prefix must be uppercase letters (A–Z) and must be one to four
characters long. 9. For **Pool**, choose **Glacier Pool**,
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
S3 Glacier Flexible Retrieval when your backup software ejects them. 10. (Optional) For **Tags**, choose **Add new
tag** and enter a key and value to add tags to your tape. A tag is
a case-sensitive key-value pair that helps you manage, filter, and search for
your tapes. 11. Choose **Create tapes**. 12. In the navigation pane, choose **Tape Library > Tapes** to
see your tapes. By default, this list displays up to 1,000 tapes at a time, but
the searches that you perform apply to all of your tapes. You can use the search
bar to find tapes that match a specific criteria, or to reduce the list to less
than 1,000 tapes. When your list contains 1,000 tapes or fewer, you can then
sort your tapes in ascending or descending order by various properties.
The status of the virtual tapes is initially set to **CREATING** when
the virtual tapes are being created. After the tapes are created, their status changes
to **AVAILABLE**. For more information, see [Understanding Tape Status](understand-tapes-status.md "understand-tapes-status.md").
