

# Data retrieval APIs for Amazon QLDB
<a name="amazonqldb"></a>

Amazon QLDB provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="qldb-DescribeJournalKinesisStream"></a>[DescribeJournalKinesisStream](https://docs.aws.amazon.com/qldb/latest/developerguide/API_DescribeJournalKinesisStream.html) | Describe information about a journal kinesis stream | Read | 
| <a name="qldb-DescribeJournalS3Export"></a>[DescribeJournalS3Export](https://docs.aws.amazon.com/qldb/latest/developerguide/API_DescribeJournalS3Export.html) | Describe information about a journal export job | Read | 
| <a name="qldb-DescribeLedger"></a>[DescribeLedger](https://docs.aws.amazon.com/qldb/latest/developerguide/API_DescribeLedger.html) | Describe a ledger | Read | 
| <a name="qldb-GetBlock"></a>[GetBlock](https://docs.aws.amazon.com/qldb/latest/developerguide/API_GetBlock.html) | Retrieve a block from a ledger for a given BlockAddress | Read | 
| <a name="qldb-GetDigest"></a>[GetDigest](https://docs.aws.amazon.com/qldb/latest/developerguide/API_GetDigest.html) | Retrieve a digest from a ledger for a given BlockAddress | Read | 
| <a name="qldb-GetRevision"></a>[GetRevision](https://docs.aws.amazon.com/qldb/latest/developerguide/API_GetRevision.html) | Retrieve a revision for a given document ID and a given BlockAddress | Read | 
| <a name="qldb-ListJournalKinesisStreamsForLedger"></a>[ListJournalKinesisStreamsForLedger](https://docs.aws.amazon.com/qldb/latest/developerguide/API_ListJournalKinesisStreamsForLedger.html) | List journal kinesis streams for a specified ledger | List | 
| <a name="qldb-ListJournalS3Exports"></a>[ListJournalS3Exports](https://docs.aws.amazon.com/qldb/latest/developerguide/API_ListJournalS3Exports.html) | List journal export jobs for all ledgers | List | 
| <a name="qldb-ListJournalS3ExportsForLedger"></a>[ListJournalS3ExportsForLedger](https://docs.aws.amazon.com/qldb/latest/developerguide/API_ListJournalS3ExportsForLedger.html) | List journal export jobs for a specified ledger | List | 
| <a name="qldb-ListLedgers"></a>[ListLedgers](https://docs.aws.amazon.com/qldb/latest/developerguide/API_ListLedgers.html) | List existing ledgers | List | 
| <a name="qldb-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/qldb/latest/developerguide/API_ListTagsForResource.html) | List tags for a resource | Read | 
| <a name="qldb-PartiQLHistoryFunction"></a>[PartiQLHistoryFunction](https://docs.aws.amazon.com/qldb/latest/developerguide/working.history.html) | Use the history function on a table | Read | 
| <a name="qldb-PartiQLSelect"></a>[PartiQLSelect](https://docs.aws.amazon.com/qldb/latest/developerguide/ql-reference.select.html) | Select documents from a table | Read | 