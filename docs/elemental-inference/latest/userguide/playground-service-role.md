

# Service role
<a name="playground-service-role"></a>

The console creates the service role `ElementalInferencePlaygroundServiceRole` when you choose **Create service role** on the **Create job** page. You can create the role after you enter both the input and output locations, because its permissions are scoped to those buckets. Its trust policy allows AWS Elemental MediaConvert to assume the role (`sts:AssumeRole`). Its permissions are limited to the following:
+ Elemental Inference – `CreateFeed`, `AssociateFeed`, `PutMedia`, `GetMetadata`, `DeleteFeed`, and `TagResource`
+ Amazon S3 – `GetObject` on the input bucket and `PutObject` on the output bucket

If a later job uses input or output buckets that the role doesn't cover, the console prompts you to choose **Update role permissions**. Updating the role scopes it to the buckets that you selected for the new job, and removes access to the buckets it covered before. A queued job, or a duplicate of an earlier job, that uses those earlier buckets then needs the role updated again.