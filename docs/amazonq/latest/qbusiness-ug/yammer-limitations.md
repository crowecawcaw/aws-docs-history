

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Known limitations for the Microsoft Yammer connector
<a name="yammer-limitations"></a>

The Microsoft Yammer connector has the following known limitations:
+ Due to API limitations, an incremental sync will not update deleted **Messages**, **Attachments**, **Communities** and **Users**. To update deleted entities, you must run a full sync.