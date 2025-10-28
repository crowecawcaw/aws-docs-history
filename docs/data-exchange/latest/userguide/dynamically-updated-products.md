# Publishing a new data set revision in

AWS Data Exchange

AWS Data Exchange supports dynamically updated products. Subscribers subscribe to the product for a
certain duration and access all of the published data sets as long as their subscription is
active. For example, a provider might want to provide a product that contains daily closing
stock prices for US equities, which would be updated every day with the day’s closing prices.
You can create and finalize new revisions that will be available in your product’s data sets,
or add new data sets to your product.

Your product includes some or all historical and future revisions as part of a
subscription. For more information, see [Revision access rules in AWS Data Exchange](best-practices-revisions.md "best-practices-revisions.md").

In the following procedure, you create and finalize a new revision for a data set that has
already been published using the AWS Data Exchange console. The data set revision is then automatically
published to all products the data set belongs to. For more information, see [Revisions](data-sets.md#revisions "data-sets.md#revisions").

###### Important

A provider can revoke subscriber access to a revision and then delete the assets of the
revision using the console or the AWS Data Exchange API. For more information, see [Revoking access to revisions in AWS Data Exchange](revoking-revisions.md "revoking-revisions.md").

###### To publish a new data set revision to a product

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. On the left side navigation pane, under **Publish data**, choose
   **Owned data sets**.
3. In **Owned data sets**, choose the data set you want to update.
4. Navigate to the **Products** tab to make sure that the data set is
   associated with a published product.
5. From the **Revisions** tab, choose **Create
   revision** to open the **Create revision** page.
   1. (Optional) Under **Revision settings**, provide an optional
      comment for your revision that describes the purpose of the revision.
   2. (Optional) Under **Add tags – optional**, add tags associated
      with the resource.
   3. Choose **Create revision**.

   Your new revision is created.

6. Under the **Jobs** section, choose either **Import from
   Amazon S3** or **Upload** (to upload from your computer),
   depending on if the assets you want to include are stored in an Amazon S3 bucket you own or on
   your local computer.
   1. Follow the prompts, depending on your selection. A job is started to import your
      asset into your data set.
   2. After the job is finished, the **State** field in the
      **Jobs** section is updated to
      **Completed**.

7. Under **Revision overview**, review your revision and its assets, and
   then choose **Finalize**.
   The revision has been published to the product and is now available to subscribers.

## Suggested approach for historical data published

with the Files delivery type

Some dynamic products contain historical content that subscribers can access. For
example, if your product includes a 30-year history of daily closing stock price for US
equities, subscribers would get access to that data in addition to the dynamic updates every
day.

For these kinds of products that contain a historical record of data, a best practice is
to publish all historical data in a single revision of the data set. You can use the
optional comment for the revision to indicate that this revision is a single upload of all
data history from a specific date.

If the single historical revision contains a time series of multiple objects, you might
consider labeling your object names to describe the underlying data periodicity. For
example, if your single revision of history contains 200 files each with a week of
historical data, you can name each file with a date for the week the data history
begins.

## Suggested approaches for updates

You can dynamically update your data sets in a number of ways. Here are three example
approaches, all of which create a new revision for each update, but the content of the new
revision is different.

- **Use a new revision for each update that contains only the
  items that have changed since the last revision** – Your revision size
  would be smaller because only those items that have changed are updated. This approach
  is suitable for data sets for which the updates affect only a small subset of the data
  and subscribers are focused only on the items that have changed.
- **Use a new revision for each update that contains the updated
  data** – The new revision contains a full updated file. All items are
  included in the new revision, including those that have not changed since the last
  revision. This approach is convenient for subscribers who want to maintain a single
  up-to-date file for your data. Subscribers export the latest revision's asset or assets
  to the same destination and override the previous file or files.
- **Use a new revision for each update that contains the full
  history and updated data** – The new revision contains the full history
  of the data, including the latest state of the data and the history of the previous
  revisions. This approach is more storage-heavy. It's suitable for data sets for which
  subscribers are interested in the latest comprehensive view of the data's history,
  including any potential past corrections or adjustments. In this approach, each revision
  is self-suﬃcient and provides a full view of the data set history with no dependency on
  previous revisions.
