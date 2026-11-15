

# Service role
<a name="playground-service-role"></a>

The console creates `ElementalInferencePlaygroundServiceRole` when you choose **Create service role** on the **Create job** page, after you enter the input and output locations. AWS Elemental MediaConvert assumes the role (`sts:AssumeRole`), and its permissions are scoped to your buckets:
+ Elemental Inference – `CreateFeed`, `AssociateFeed`, `PutMedia`, `GetMetadata`, `DeleteFeed`, and `TagResource`
+ Amazon S3 – `GetObject` on the input bucket and `PutObject` on the output bucket

For a preview, the role runs only the MediaConvert job. The console creates the feed with your own permissions. For more information, see [User permissions](playground-user-permissions.md).

If a later job uses other buckets, choose **Update role permissions**. The update adds those buckets and keeps the ones that the role already covers. If you created the role yourself, the console can't update it. Make sure that it can read your input bucket, write to your output bucket, and call Elemental Inference.

If your output bucket uses SSE-KMS with a customer managed AWS KMS key, add a policy to the role that allows `kms:GenerateDataKey` and `kms:Decrypt` on that key, only through Amazon S3 in the bucket's Region (`kms:ViaService`, for example `s3.us-east-1.amazonaws.com`). Otherwise, the job fails with an access denied error.