# Seller delivery data feeds in AWS Marketplace

AWS Marketplace provides data feeds as a mechanism to send structured, up-to-date product and
customer information from AWS Marketplace systems to seller Amazon S3 buckets for ETL (extract, transform, and
load) between seller-owned business intelligence tools. Data feeds collect and deliver
comma-separated value (CSV) files to an encrypted Amazon S3 bucket that you provide. Data feeds are
generated within a day, and contain 24 hours of data from the previous day. The following
sections provide an overview of data feeds and explain how to access and use them. Subsequent
sections describe each data feed.

The transactional data is delivered and appended in a bi-temporal structure so sellers can
store and query data along two timelines with timestamps for both

- valid time: when a fact occurred in the real world (“what you knew”)
- system time: when that fact was recorded to the database (“when you knew it”).
  Data feeds are delivered daily at midnight UTC following an update from the prior
  day containing 24 hours of data from the previous day. An update can be defined by a customer
  subscribing, a customer being invoiced, or AWS disbursing payment.

###### Topics

- [Storage and structure of AWS Marketplace data feeds](data-feed-details.md "data-feed-details.md")
- [Accessing data feeds](data-feed-accessing.md "data-feed-accessing.md")
- [Collecting and analyzing data with data feeds](data-feed-using.md "data-feed-using.md")
- [Data feed tables overview](data-feed-joining.md "data-feed-joining.md")
- [Data feed query examples](data-feed-full-examples.md "data-feed-full-examples.md")
- [Data feeds](data-feeds.md "data-feeds.md")
