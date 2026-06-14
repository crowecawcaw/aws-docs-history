# POST Object restore

## Description

This operation performs the following types of requests:

- `select` – Perform a select query on an archived object
- `restore an archive` – Restore an archived object

To use this operation, you must have permissions to perform the
`s3:RestoreObject` and `s3:GetObject` actions. The bucket
owner has this permission by default and can grant this permission to others. For more
information about permissions, see [Permissions Related to Bucket Subresource Operations](../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources "../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources") and [Managing Access Permissions to Your Amazon S3
Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md") in the _Amazon Simple Storage Service User Guide_.

## Querying Archives with Select Requests

You use a select type of request to perform SQL queries on archived objects. The archived
objects that are being queried by the select request must be formatted as uncompressed
comma-separated values (CSV) files. You can run queries and custom analytics on your
archived data without having to restore your data to a hotter Amazon S3 tier. For an overview
about select requests, see [Querying Archived Objects](../userguide/querying-glacier-archives.md "../userguide/querying-glacier-archives.md") in the
_Amazon Simple Storage Service User Guide_.

When making a select request, do the following:

- Define an output location for the select query's output. This must be an Amazon S3 bucket in
  the same AWS Region as the bucket that contains the archive object that is being
  queried. The AWS account that initiates the job must have permissions to write
  to the S3 bucket. You can specify the storage class and encryption for the
  output objects stored in the bucket. For more information about output, see
  [Querying Archived
  Objects](../userguide/querying-glacier-archives.md "../userguide/querying-glacier-archives.md") in the _Amazon Simple Storage Service User Guide_.

For more information about the `S3` structure in the request body, see the
following:

    + [PutObject](../API/API_PutObject.md "../API/API_PutObject.md")
    + [Managing Access with
     ACLs](../userguide/S3_ACLs_UsingACLs.md "../userguide/S3_ACLs_UsingACLs.md") in the *Amazon Simple Storage Service User Guide*
    + [Protecting Data
     Using Server-Side Encryption](../userguide/serv-side-encryption.md "../userguide/serv-side-encryption.md") in the
     *Amazon Simple Storage Service User Guide*

- Define the SQL expression for the `SELECT` type of restoration for your query
  in the request body's `SelectParameters` structure. You can use
  expressions like the following examples.

  - The following expression returns all records from the specified object.

  ```
  SELECT * FROM Object
  ```
  - Assuming that you are not using any headers for data stored in the object, you can
    specify columns with positional headers.

  ```
  SELECT s._1, s._2 FROM Object s WHERE s._3 > 100
  ```
  - If you have headers and you set the `fileHeaderInfo` in the `CSV`
    structure in the request body to `USE`, you can specify
    headers in the query. (If you set the `fileHeaderInfo` field
    to `IGNORE`, the first row is skipped for the query.) You
    cannot mix ordinal positions with header column names.

  ```
  SELECT s.Id, s.FirstName, s.SSN FROM S3Object s
  ```

For more information about using SQL with Amazon Glacier Select restore, see [SQL Reference for Amazon S3 Select and
Amazon Glacier Select](../userguide/s3-glacier-select-sql-reference.md "../userguide/s3-glacier-select-sql-reference.md") in the _Amazon Simple Storage Service User Guide_.

When making a select request, you can also do the following:

- To expedite your queries, specify the `Expedited` tier. For more information
  about tiers, see "Restoring Archives," later in this topic.
- Specify details about the data serialization format of both the input object that is being
  queried and the serialization of the CSV-encoded query results.

The following are additional important facts about the select feature:

- The output results are new Amazon S3 objects. Unlike archive retrievals, they are stored until
  explicitly deleted—manually or through a lifecycle policy.
- You can issue more than one select request on the same Amazon S3 object. Amazon S3 doesn't
  deduplicate requests, so avoid issuing duplicate requests.
- Amazon S3 accepts a select request even if the object has already been restored. A select
  request doesn’t return error response `409`.

## Restoring Archives

Objects in the GLACIER
and DEEP_ARCHIVE
storage
classes
are archived. To access an archived object, you must first initiate a restore request.
This restores a
temporary
copy of the archived object.
In
a restore request, you specify the number of days that you want the restored copy to
exist. After the specified period, Amazon S3 deletes the temporary copy but the object
remains archived in the GLACIER or DEEP_ARCHIVE storage class that object was restored
from.

To restore a specific object version, you can provide a version ID. If you don't
provide a version ID, Amazon S3 restores the current version.

The time it takes restore jobs to finish depends on which
storage class the
object is being restored from and which data access tier you
specify.

When restoring an archived object (or using a select request), you can specify one of
the following data
access tier options in the `Tier` element of the request
body:

- **`Expedited`** - Expedited retrievals
  allow you to quickly access your data stored in the GLACIER storage class when
  occasional urgent requests for a subset of archives are required. For all but
  the largest archived objects (250 MB+), data accessed using Expedited retrievals
  are typically made available within 1–5 minutes. Provisioned capacity ensures
  that retrieval capacity for Expedited retrievals is available when you need it.
  Expedited retrievals and provisioned capacity are not available for the
  DEEP_ARCHIVE storage class.
- **`Standard`** - Standard retrievals
  allow you to access any of your archived objects within several hours. This is
  the default option for the GLACIER and DEEP_ARCHIVE retrieval requests that do
  not specify the retrieval option.
  Standard
  retrievals typically complete within 3-5 hours from the GLACIER storage class
  and typically complete within 12 hours from the DEEP_ARCHIVE storage
  class.
- **`Bulk`** - Bulk retrievals are
  Amazon Glacier’s lowest-cost retrieval option, enabling you to retrieve large amounts,
  even petabytes, of data inexpensively in a day.
  Bulk
  retrievals typically complete within 5-12 hours from the GLACIER storage class
  and typically complete within 48 hours from the DEEP_ARCHIVE storage
  class.

For more information about archive retrieval options and provisioned capacity for
`Expedited` data access, see [Restoring Archived Objects](../userguide/restoring-objects.md "../userguide/restoring-objects.md") in the
_Amazon Simple Storage Service User Guide_.

You can use Amazon S3 restore speed upgrade to change the restore speed to a faster speed
while it is in progress. You upgrade the speed of an in-progress restoration by issuing
another restore request to the same object, setting a new `Tier` request
element. When issuing a request to upgrade the restore tier, you must choose a tier that
is faster than the tier that the in-progress restore is using. You must not change any
other parameters, such as the `Days` request element. For more information,
see [Upgrading the Speed of an In-Progress Restore](../userguide/restoring-objects.md#restoring-objects-upgrade-tier.title.html "../userguide/restoring-objects.md#restoring-objects-upgrade-tier.title.html") in the
_Amazon Simple Storage Service User Guide_.

To get the status of object restoration, you can send a `HEAD` request.
Operations return the `x-amz-restore` header, which provides information
about the restoration status, in the response. You can use Amazon S3 event notifications to
notify you when a restore is initiated or completed. For more information, see [Configuring Amazon S3 Event
Notifications](../userguide/NotificationHowTo.md "../userguide/NotificationHowTo.md") in the _Amazon Simple Storage Service User Guide_.

After restoring an archived object, you can update the restoration period by reissuing
the request with a new period. Amazon S3 updates the restoration period relative to the
current time and charges only for the request—there are no data transfer charges.

You cannot update
the restoration period when Amazon S3 is actively processing your current restore request for
the object.

If your bucket has a lifecycle configuration with a rule that includes an expiration
action, the object expiration overrides the life span that you specify in a restore
request. For example, if you restore an object copy for 10 days, but the object is
scheduled to expire in 3 days, Amazon S3 deletes the object in 3 days. For more information
about lifecycle configuration, see [PutBucketLifecycleConfiguration](../API/API_PutBucketLifecycleConfiguration.md "../API/API_PutBucketLifecycleConfiguration.md") and [Object Lifecycle Management](../userguide/object-lifecycle-mgmt.md "../userguide/object-lifecycle-mgmt.md") in
_Amazon Simple Storage Service User Guide_.

## Requests

### Syntax

```
POST /`ObjectName`?restore&versionId=`VersionID` HTTP/1.1
Host: `BucketName`.s3.amazonaws.com
Date: `date`
Authorization: `authorization string` (see Authenticating Requests (AWS Signature Version 4))
Content-MD5: `MD5`

 `request body`

```

###### Note

The syntax shows some of the request headers. For a complete list, see
"Request Headers," later in this topic.

### Request Parameters

This implementation of the operation does not use request parameters.

### Request Headers

| Name          | Description                                                                                                                                                                                                                                                                                                                       | Required |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `Content-MD5` | The base64-encoded 128-bit MD5 digest of the data. You must use this header as a<br>message integrity check to verify that the request body was not<br>corrupted in transit. For more information, see [RFC<br>1864](http://www.ietf.org/rfc/rfc1864.txt "http://www.ietf.org/rfc/rfc1864.txt").<br>Type: String<br>Default: None | Yes      |

### Request Elements

The following is an XML example of a request body for restoring an archive.

```
<RestoreRequest>
   <Days>2</Days>
   <GlacierJobParameters>
     <Tier>Bulk</Tier>
   </GlacierJobParameters>
</RestoreRequest>

```

The following table explains the XML for archive restoration in the request body.

| Name                   | Description                                                                                                                                                                                                                                                                                                                                                                                                      | Required                     |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | ----------------------------------------------- | --- |
| `RestoreRequest`       | Container for restore information.<br>Type: Container                                                                                                                                                                                                                                                                                                                                                            | Yes                          |
| `Days`                 | Lifetime of the restored (active) copy. The minimum number of days that you can<br>restore an object from Amazon Glacier is 1. After the object copy reaches<br>the specified lifetime, Amazon S3 removes it from the bucket. If you<br>are restoring an archive, this element is required.<br>Do not use this element with a `SELECT` type of request.<br>Type: Positive integer<br>Ancestors: `RestoreRequest` | Yes, if restoring an archive |
| `GlacierJobParameters` | Container for S3 Glacier storage class job parameters.<br>Do not use this element with a `SELECT` type of request.<br>Type: Container<br>Ancestors: `RestoreRequest`                                                                                                                                                                                                                                             | No                           |
| `Tier`                 | The data access tier to use when restoring the archive. `Standard` is the<br>default.<br>Type: Enum<br>Valid values: `Expedited`                                                                                                                                                                                                                                                                                 | `Standard`                   | <br>`Bulk`<br>Ancestors: `GlacierJobParameters` | No  |

The following XML is the request body for a select query on an archived object:

```
<RestoreRequest>
    <Type>SELECT</Type>
    <Tier>Expedited</Tier>
    <Description>Job description</Description>
    <SelectParameters>
          <Expression>Select * from Object</Expression>
          <ExpressionType>SQL</ExpressionType>
          <InputSerialization>
              <CSV>
                  <FileHeaderInfo>IGNORE</FileHeaderInfo>
                  <RecordDelimiter>\n</RecordDelimiter>
                  <FieldDelimiter>,</FieldDelimiter>
                  <QuoteCharacter>"</QuoteCharacter>
                  <QuoteEscapeCharacter>"</QuoteEscapeCharacter>
                  <Comments>#</Comments>
              </CSV>
           </InputSerialization>
         <OutputSerialization>
             <CSV>
                 <QuoteFields>ASNEEDED</QuoteFields>
                 <RecordDelimiter>\n</RecordDelimiter>
                 <FieldDelimiter>,</FieldDelimiter>
                 <QuoteCharacter>"</QuoteCharacter>
                 <QuoteEscapeCharacter>"</QuoteEscapeCharacter>
             </CSV>
         </OutputSerialization>
    </SelectParameters>
    <OutputLocation>
        <S3>
	     <BucketName>Name of bucket</BucketName>
            <Prefix>Key prefix</Prefix>
	      <CannedACL>Canned ACL string</CannedACL>
	      <AccessControlList>
		    <Grantee>
		        <Type>Grantee Type</Type>
			 <ID>Grantee identifier</ID>
			 <URI>Grantee URI</URI>
		       <Permission>Granted permission</Permission>
                    <DisplayNmae>Display Name</DisplayName>
                    <EmailAddress>email</EmailAddress>
		    </Grantee>
	      </AccessControlList>
	      <Encryption>
	            <EncryptionType>Encryption type</EncryptionType>
		     <KMSKeyId>KMS Key ID</KMSKeyId>
		     <KMSContext>Base64-encoded JSON<KMSContext>
            </Encryption>
	     <UserMetadata>
               <MetadataEntry>
                   <Name>Key</Name>
                   <Value>Value</Value>
               </MetadataEntry>
            </UserMetadata>
            <Tagging>
                <TagSet>
                    <Tag>
                        <Key>Tag name</Key>
                        <Value>Tag value</Value>
                    </Tag>
               </TagSet>
            </Tagging>
            <StorageClass>Storage class</StorageClass>
	 </S3>
    </OutputLocation>
</RestoreRequest>
```

The following tables explain the XML for a `SELECT` type of restoration in the
request body.

| Name               | Description                                                                                                                                     | Required                         |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ----------------------------------------- | --- |
| `RestoreRequest`   | Container for restore information.<br>Type: Container                                                                                           | Yes                              |
| `Tier`             | The data access tier to use when restoring the archive. `Standard` is the<br>default.<br>Type: Enum<br>Valid values: `Expedited`                | `Standard`                       | <br>`Bulk`<br>Ancestors: `RestoreRequest` | No  |
| `Description`      | The optional description for the request.<br>Type: String<br>Ancestors: `RestoreRequest`                                                        | No                               |
| `SelectParameters` | Describes the parameters for the select job request.<br>Type: Container<br>Ancestors: `RestoreRequest`                                          | Yes, if request type is `SELECT` |
| `OutputLocation`   | Describes the location that receives the results of the select restore request.<br>Type: Container for Amazon S3<br>Ancestors: `RestoreRequest` | Yes, if request type is `SELECT` |

| The `SelectParameters` container element contains the following elements. | Name                                                                                                                                                                                                                                                                                                                                  | Description | Required |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------- |
| `Expression`                                                              | The SQL expression. For example:<br>• The following SQL expression retrieves the first column of the data from the object<br>stored in CSV format:<br>`SELECT s._1 FROM Object s`<br>• The following SQL expression returns everything from the object:<br>`SELECT<br>• FROM Object`<br>Type: String<br>Ancestors: `SelectParameters` | Yes         |
| `ExpressionType`                                                          | Identifies the expression type.<br>Type: String<br>Valid values: `SQL`<br>Ancestors: `SelectParameters`                                                                                                                                                                                                                               | Yes         |
| `InputSerialization`                                                      | Describes the serialization format of the object.<br>Type: Container for CSV<br>Ancestors: `SelectParameters`                                                                                                                                                                                                                         | Yes         |
| `OutputSerialization`                                                     | Describes how the results of the select job are serialized.<br>Type: Container for CSV<br>Ancestors: `SelectParameters`                                                                                                                                                                                                               | Yes         |

| The CSV container element in the `InputSerialization` element contains the following elements. | Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description | Required                    |
| ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | --------------------------- | --- |
| `RecordDelimiter`                                                                              | A single character used to separate individual records in the input. Instead of the<br>default value, you can specify an arbitrary delimiter.<br>Type: String<br>Default: `\n`<br>Ancestors: `CSV`                                                                                                                                                                                                                                                                                                                                           | No          |
| `FieldDelimiter`                                                                               | A single character used to separate individual fields in a record. You can specify an<br>arbitrary delimiter.<br>Type: String<br>Default: `,`<br>Ancestors: `CSV`                                                                                                                                                                                                                                                                                                                                                                            | No          |
| `QuoteCharacter`                                                                               | A single character used for escaping when the field delimiter is part of the<br>value.<br>Consider this example in a CSV file:<br>`"a, b"`<br>Wrapping the value in quotation marks makes this value a single field. If you don't<br>use the quotation marks, the comma is a field delimiter (which<br>makes it two separate field values, a and b).<br>Type: String<br>Default: `"`<br>Ancestors: `CSV`                                                                                                                                     | No          |
| `QuoteEscapeCharacter`                                                                         | A single character used for escaping the quotation mark character inside an already<br>escaped value. For example, the value `""" a , b """`<br>is parsed as `" a , b "`.<br>Type: String<br>Default: `"`<br>Ancestors: `CSV`                                                                                                                                                                                                                                                                                                                | No          |
| `FileHeaderInfo`                                                                               | Describes the first line in the input data. It is one of the ENUM values.<br>• `NONE`: First line is not a header.<br>• `IGNORE`: First line is a header, but you can't use the header values to<br>indicate the column in an expression. You can use column<br>position (such as \_1, \_2, …) to indicate the column<br>(`SELECT s._1 FROM OBJECT s`).<br>• `Use`: First line is a header, and you can use the header value to<br>identify a column in an expression (`SELECT "name"<br>FROM OBJECT`).<br>Type: Enum<br>Valid values: `NONE | USE         | IGNORE`<br>Ancestors: `CSV` | No  |
| `Comments`                                                                                     | A single character used to indicate that a row should be<br>ignored when the character is present at the start of that row.<br>You can specify any character to indicate a comment line.<br>Type: String<br>Ancestors: `CSV`                                                                                                                                                                                                                                                                                                                 | No          |

| The CSV container element (in the `OutputSerialization` elements) contains the following elements. | Name                                                                                                                                                                                                                                                                 | Description                                          | Required |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | -------- |
| `QuoteFields`                                                                                      | Indicates whether to use quotation marks around output fields.<br>• `ALWAYS`: Always use quotation marks for output fields.<br>• `ASNEEDED`: Use quotation marks for output fields when needed.<br>Type: Enum<br>Valid values: `ALWAYS                               | ASNEEDED`<br>Default: `AsNeeded`<br>Ancestors: `CSV` | No       |
| `RecordDelimiter`                                                                                  | A single character used to separate individual records in the output. Instead of the<br>default value, you can specify an arbitrary delimiter.<br>Type: String<br>Default: `\n`<br>Ancestors: `CSV`                                                                  | No                                                   |
| `FieldDelimiter`                                                                                   | A single character used to separate individual fields in a record. You can specify an<br>arbitrary delimiter.<br>Type: String<br>Default: `,`<br>Ancestors: `CSV`                                                                                                    | No                                                   |
| `QuoteCharacter`                                                                                   | A single character used for escaping when the field delimiter is part of the value.<br>For example, if the value is `a, b`, Amazon S3 wraps this<br>field value in quotation marks, as follows: `" a , b<br>"`.<br>Type: String<br>Default: `"`<br>Ancestors: `CSV`  | No                                                   |
| `QuoteEscapeCharacter`                                                                             | A single character used for escaping the quotation mark character inside an already<br>escaped value. For example, if the value is `" a , b<br>"`, Amazon S3 wraps the value in quotation marks, as<br>follows: `""" a , b """`.<br>Type: String<br>Ancestors: `CSV` | No                                                   |

| The S3 container element (in the `OutputLocation` element) contains the following elements. | Name                                                                                                                                                                                                            | Description          | Required          |
| ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------- | ------------------------------- | ---------------------- | ----------------- | --------------------------------------------- | --- |
| `AccessControlList`                                                                         | A list of grants that control access to the staged results.<br>Type: Container for Grant<br>Ancestors: `S3`                                                                                                     | No                   |
| `BucketName`                                                                                | The name of the S3 bucket where the select restore results are stored. The bucket must<br>be in the same AWS Region as the bucket that contains the input<br>archive object.<br>Type: String<br>Ancestors: `S3` | Yes                  |
| `CannedACL`                                                                                 | The canned access control list (ACL) to apply to the select restore results.<br>Type: String<br>Valid values: `private                                                                                          | public-read          | public-read-write | aws-exec-read                   | <br>authenticated-read | bucket-owner-read | bucket-owner-full-control`<br>Ancestors: `S3` | No  |
| `Encryption`                                                                                | Contains encryption information for the stored results.<br>Type: Container for Encryption<br>Ancestors: `S3`                                                                                                    | No                   |
| `Prefix`                                                                                    | The prefix that is prepended to the select restore results. The maximum length for the<br>prefix is 512 bytes.<br>Type: String<br>Ancestors: `S3`                                                               | Yes                  |
| `StorageClass`                                                                              | The class of storage used to store the select request<br>results.<br>Type: String<br>Valid values: `STANDARD`                                                                                                   | `REDUCED_REDUNDANCY` | `STANDARD_IA`     | `ONEZONE_IA`<br>Ancestors: `S3` | No                     |
| `Tagging`                                                                                   | Container for tag information.<br>Type: Tag structure<br>Ancestors: `S3`                                                                                                                                        | No                   |
| `UserMetadata`                                                                              | Contains a list of metadata to store with the select restore results.<br>Type: MetadataEntry structure<br>Ancestors: `S3`                                                                                       | No                   |

| The Grantee container element (in the `AccessControlList` element) contains the following elements. | Name                                                                          | Description | Required |
| --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------- | -------- |
| `DisplayName`                                                                                       | The screen name of the grantee.<br>Type: String<br>Ancestors: `Grantee`       | No          |
| `EmailAddress`                                                                                      | The email address of the grantee.<br>Type: String<br>Ancestors: `Grantee`     | No          |
| `ID`                                                                                                | The canonical user ID of the grantee.<br>Type: String<br>Ancestors: `Grantee` | No          |
| `Type`                                                                                              | The type of the grantee.<br>Type: String<br>Ancestors: `Grantee`              | No          |
| `URI`                                                                                               | The URI of the grantee group.<br>Type: String<br>Ancestors: `Grantee`         | No          |
| `Permission`                                                                                        | Granted permission.<br>Type: String<br>Ancestors: `Grantee`                   | No          |

| The `Encryption` container element (in S3) contains the following elements. | Name                                                                                                                                                                                   | Description                        | Required |
| --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | -------- |
| `EncryptionType`                                                            | The server-side encryption algorithm used when storing job results.<br>The default is no encryption.<br>Type: String<br>Valid Values `aws:kms                                          | AES256`<br>Ancestors: `Encryption` | No       |
| `KMSContext`                                                                | Optional. If the encryption type is `aws:kms`, you can use this value to<br>specify the encryption context for the select restore<br>results.<br>Type: String<br>Ancestors: Encryption | No                                 |
| `KMSKeyId`                                                                  | The AWS Key Management Service (AWS KMS) key ID to use for object encryption.<br>Type: String<br>Ancestors: `Encryption`                                                               | No                                 |

| The `TagSet` container element (in the `Tagging` element) contains the following element. | Name                                                     | Description | Required |
| ----------------------------------------------------------------------------------------- | -------------------------------------------------------- | ----------- | -------- |
| `Tag`                                                                                     | Contains tags.<br>Type: Container<br>Ancestors: `TagSet` | No          |

| The Tag container element (in the `TagSet` element) contains the following elements. | Name                                                  | Description | Required |
| ------------------------------------------------------------------------------------ | ----------------------------------------------------- | ----------- | -------- |
| `Key`                                                                                | Name of the tag.<br>Type: String<br>Ancestors: `Tag`  | No          |
| `Value`                                                                              | Value of the tag.<br>Type: String<br>Ancestors: `Tag` | No          |

| The `MetadataEntry` container element (in the `UserMetadata` element) contains the following key-value pair elements to store with an object. | Name                                              | Description | Required |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ----------- | -------- |
| `MetadataKey`                                                                                                                                 | The metadata key.<br>Type: String<br>Ancestors:   | No          |
| `MetadataEntry`                                                                                                                               | The metadata value.<br>Type: String<br>Ancestors: | No          |

## Responses

A successful operation returns either the `200 OK` or `202 Accepted`
status code.

- If the object copy is not previously restored, then Amazon S3 returns `202
Accepted` in the response.
- If the object copy is previously restored, Amazon S3 returns `200 OK` in the
  response.

### Response Headers

This implementation of the operation uses only response headers that are common to most
responses. For more information, see [Common Response Headers](RESTCommonResponseHeaders.md "RESTCommonResponseHeaders.md").

### Response Elements

This operation does not return response elements.

### Special Errors

| Error Code                              | Description                                                                                                                                                                                                                                                                            | HTTP Status Code | SOAP Fault Code Prefix |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------------------- |
| `RestoreAlreadyInProgress`              | Object restore is already in progress. (This error does not apply to SELECT type<br>requests.)                                                                                                                                                                                         | 409 Conflict     | Client                 |
| `GlacierExpeditedRetrievalNotAvailable` | S3 Glacier storage class expedited retrievals are currently not available. Try again later.<br>(Returned if there is insufficient capacity to process the<br>`Expedited` request. This error applies only to<br>`Expedited` retrievals and not to<br>`Standard` or `Bulk` retrievals.) | 503              | N/A                    |

## Examples

### Restore an Object for Two Days Using the Expedited Retrieval Option

The following restore request restores a copy of the `photo1.jpg` object from
Amazon Glacier for a period of two days using the expedited retrieval option.

```
POST /photo1.jpg?restore HTTP/1.1
Host: examplebucket.s3.amazonaws.com
Date: Mon, 22 Oct 2012 01:49:52 GMT
Authorization: `authorization string`
Content-Length: `content length`

<RestoreRequest>
  <Days>2</Days>
  <GlacierJobParameters>
    <Tier>Expedited</Tier>
  </GlacierJobParameters>
</RestoreRequest>
```

If the `examplebucket` does not have a restored copy of the object, Amazon S3
returns the following `202 Accepted` response.

```
HTTP/1.1 202 Accepted
x-amz-id-2: GFihv3y6+kE7KG11GEkQhU7/2/cHR3Yb2fCb2S04nxI423Dqwg2XiQ0B/UZlzYQvPiBlZNRcovw=
x-amz-request-id: 9F341CD3C4BA79E0
Date: Sat, 20 Oct 2012 23:54:05 GMT
Content-Length: 0
Server: AmazonS3
```

If a copy of the object is already restored, Amazon S3 returns a `200 OK` response,
and updates only the restored copy's expiry time.

### Query an Archive with a SELECT Request

The following is an example select restore request.

```
POST /object-one.csv?restore HTTP/1.1
Host: examplebucket.s3.amazonaws.com
Date: Date: Sat, 20 Oct 2012 23:54:05 GMT
Authorization: `authorization string`
Content-Length: `content length`

<RestoreRequest xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Type>SELECT</Type>
  <Tier>Expedited</Tier>
  <Description>this is a description</Description>
  <SelectParameters>
    <InputSerialization>
      <CSV>
        <FileHeaderInfo>IGNORE</FileHeaderInfo>
        <Comments>#</Comments>
        <QuoteEscapeCharacter>"</QuoteEscapeCharacter>
        <RecordDelimiter>\n</RecordDelimiter>
        <FieldDelimiter>,</FieldDelimiter>
        <QuoteCharacter>"</QuoteCharacter>
      </CSV>
    </InputSerialization>
    <ExpressionType>SQL</ExpressionType>
    <Expression>select * from object</Expression>
    <OutputSerialization>
      <CSV>
        <QuoteFields>ALWAYS</QuoteFields>
        <QuoteEscapeCharacter>"</QuoteEscapeCharacter>
        <RecordDelimiter>\n</RecordDelimiter>
        <FieldDelimiter>\t</FieldDelimiter>
        <QuoteCharacter>\'</QuoteCharacter>
      </CSV>
    </OutputSerialization>
  </SelectParameters>
  <OutputLocation>
    <S3>
      <BucketName>example-output-bucket</BucketName>
      <Prefix>test-s3</Prefix>
      <AccessControlList>
        <Grant>
          <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="AmazonCustomerByEmail">
            <EmailAddress>jane-doe@example.com</EmailAddress>
          </Grantee>
          <Permission>FULL_CONTROL</Permission>
        </Grant>
      </AccessControlList>
      <UserMetadata>
        <MetadataEntry>
          <Name>test</Name>
          <Value>test-value</Value>
        </MetadataEntry>
        <MetadataEntry>
          <Name>other</Name>
          <Value>something else</Value>
        </MetadataEntry>
      </UserMetadata>
      <StorageClass>STANDARD</StorageClass>
    </S3>
  </OutputLocation>
</RestoreRequest>
```

Amazon S3 returns the following `202 Accepted` response.

```
HTTP/1.1 202 Accepted
x-amz-id-2: GFihv3y6+kE7KG11GEkQhU7/2/cHR3Yb2fCb2S04nxI423Dqwg2XiQ0B/UZlzYQvPiBlZNRcovw=
x-amz-request-id: 9F341CD3C4BA79E0
x-amz-restore-output-path: js-test-s3/qE8nk5M0XIj-LuZE2HXNw6empQm3znLkHlMWInRYPS-Orl2W0uj6LyYm-neTvm1-btz3wbBxfMhPykd3jkl-lvZE7w42/
Date: Sat, 20 Oct 2012 23:54:05 GMT
Content-Length: 0
Server: AmazonS3
```

## More Info

- [GetBucketLifecycleConfiguration](../API/API_GetBucketLifecycleConfiguration.md "../API/API_GetBucketLifecycleConfiguration.md")
- [PutBucketLifecycleConfiguration](../API/API_PutBucketLifecycleConfiguration.md "../API/API_PutBucketLifecycleConfiguration.md")
- [SQL Reference for Amazon S3
  Select and Amazon Glacier Select](../userguide/s3-glacier-select-sql-reference.md "../userguide/s3-glacier-select-sql-reference.md") in the _Amazon Simple Storage Service User Guide_
