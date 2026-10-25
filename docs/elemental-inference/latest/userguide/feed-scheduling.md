

# Scheduling changes to Elemental Inference feeds
<a name="feed-scheduling"></a>

With feed scheduling, you can set up a change to a feed's configuration ahead of time, and Elemental Inference applies the change at the time that you specify. You don't need to build your own automation, such as an AWS Lambda function that's triggered by Amazon EventBridge.

You add *schedule actions* to a feed. Each schedule action specifies when to run and which configuration changes to make. At the scheduled time, Elemental Inference applies the changes to the feed on your behalf, in the same way as an `UpdateFeed` request.

**Topics**
+ [Use cases for feed scheduling](feed-scheduling-use-cases.md)
+ [How schedule actions work](feed-scheduling-how-it-works.md)
+ [Operations that you can schedule](feed-scheduling-operations.md)
+ [Creating a schedule action](feed-scheduling-create.md)
+ [Viewing schedule actions](feed-scheduling-list.md)
+ [Deleting a schedule action](feed-scheduling-delete.md)
+ [Lifecycle of a schedule action](feed-scheduling-lifecycle.md)
+ [Best practices for editing feeds that have schedule actions](feed-scheduling-best-practices.md)
+ [Troubleshooting schedule action requests](feed-scheduling-errors.md)