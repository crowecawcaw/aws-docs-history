# Migrating from Amazon Mobile Analytics to Amazon Pinpoint

On April 30, 2018, the features of Amazon Mobile Analytics were migrated to Amazon Pinpoint.

As with Mobile Analytics, you can use Amazon Pinpoint to measure app usage and revenue. Amazon Pinpoint adds more
analytics capabilities by allowing you to segment users based on your data. You can also run
targeted messaging campaigns through push notifications, email, and SMS to increase user
engagement. For more information, see [Amazon Pinpoint](https://aws.amazon.com/pinpoint/ "https://aws.amazon.com/pinpoint/").

With Amazon Pinpoint, you can also export your data in real time through [Amazon Data Firehose](https://aws.amazon.com/kinesis "https://aws.amazon.com/kinesis"), which provides additional features to
transform, encrypt, and deliver raw analytics data. With Firehose _delivery streams_, you can choose various destinations for your data like
Amazon Simple Storage Service (Amazon S3), Amazon Redshift, or Amazon OpenSearch Service.

If you're new to Mobile Analytics, use Amazon Pinpoint instead. If you're currently using Mobile Analytics, migrate from
Mobile Analytics to Amazon Pinpoint by April 30, 2018. Your existing Mobile Analytics apps are supported by Amazon Pinpoint, but certain
Mobile Analytics workflows require you to switch to the corresponding Amazon Pinpoint features:

| Workflow                                        | Migration details                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mobile Analytics REST API for events submission | Is automatically redirected to the Amazon Pinpoint API. No action is required.                                                                                                                                                                                                                                            |
| Mobile Analytics in the AWS Mobile SDKs.        | Is supported via Amazon Pinpoint in the AWS Mobile SDKs or JavaScript library. Versions of the Mobile Analytics client in the SDKs will continue to report events, but with limited support for issues. See [Migrating to Amazon Pinpoint in the AWS Mobile SDKs or JavaScript Library](migrate-sdk.md "migrate-sdk.md"). |
| Mobile Analytics console                        | Is replaced by the Amazon Pinpoint console. See [Migrating to the Amazon Pinpoint Console](migrate-console.md "migrate-console.md").                                                                                                                                                                                      |
| Mobile Analytics querying API                   | Isn't available after April 30, 2018. You can calculate Mobile Analytics KPIs from raw data from event streams.                                                                                                                                                                                                           | ###### Topics <br>• [Migrating to Amazon Pinpoint in the AWS Mobile SDKs or JavaScript Library](migrate-sdk.md "migrate-sdk.md") <br>• [Migrating to the Amazon Pinpoint API](migrate-api.md "migrate-api.md") <br>• [Migrating to the Amazon Pinpoint Console](migrate-console.md "migrate-console.md") |
