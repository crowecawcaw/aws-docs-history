# Creating using the CLI

This section describes how to use the AWS CLI to create an Elemental Inference feed.

You must set up a fully-configured feed: resource - feed - output or outputs,
where the MediaLive channel is the resource and each output represents one Elemental Inference
feature.

1. Use `create-feed` to create a new feed.

Include one output for each feature you want to implement. Set the status
to `ENABLED` in each output.

(Optional) Specify an **access role**
(`accessRoleArn`), the ARN of an IAM role that Elemental Inference assumes
on your behalf to access the resources a feed needs. An access role is
required when a smart crop output uses graphic composition, so that Elemental Inference
can read your template images from Amazon S3. 2. The response includes the following information that you should make a
note of:

    * `id`: The feed ID, which you will need for CLI commands
     on this feed.
    * `arn`: The feed ARN. You can also obtain the ARN using
     `get-feed`.
    * `dataEndpoints`: The ARN of the data endpoint for this
     feed. You will use this ARN when you send source media to Elemental Inference for
     processing, and when you retrieve the metadata that is the result of
     this processing.

3. After the feed is created, the status of the feed will eventually change
to `AVAILABLE`, indicating that it is ready to have a resource
(source media) associated with it. 4. Use `associate-feed` to associate the source media with the
feed. The source media is the resource for the feed.

You now have a useable feed: resource - feed - output.
