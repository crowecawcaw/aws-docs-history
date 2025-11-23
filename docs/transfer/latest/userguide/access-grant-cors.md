# Set up Cross-origin resource sharing (CORS) for your

bucket

You must set up cross-origin resource sharing (CORS) for all buckets that are used by
your web app. A _CORS configuration_ is a document that
defines rules that identify the origins that you will allow to access your bucket. For
more information about CORS, see [Configuring cross-origin resource sharing (CORS)](../../../AmazonS3/latest/userguide/enabling-cors-examples.md "../../../AmazonS3/latest/userguide/enabling-cors-examples.md").

###### Important

If you don't set up CORS, your end users receive an error when they attempt to
access a location on your web app.

###### To set up Cross-origin

resource sharing (CORS) for your Amazon S3 bucket

1.  Sign in to the AWS Management Console and open the Amazon S3 console at
    [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2.  Choose **Buckets** from the left navigation panel and search
    for your bucket in the search dialog, then choose the
    **Permissions** tab.
3.  In **Cross-origin resource sharing (CORS)**, choose
    **Edit** and paste in the following code. Replace
    `WebAppEndpoint` with the actual access endpoint
    for your web app. This can be either the VPC hosted or public access endpoint that's created when the
    web app is created, or a custom access endpoint, if you create one. Make sure
    not to enter trailing slashes, because doing so causes errors when users attempt
    to log on to your web app.

        * Incorrect example:
         `https://webapp-c7bf3423.transfer-webapp.us-east-2.on.aws/`
        * Correct examples:




        	+ `https://webapp-c7bf3423.transfer-webapp.us-east-2.on.aws`
        	+ `https://vpce-05668789767a-fh45z079.vpce-mq.transfer-webapp.us-east-1.on.aws`

    If you are reusing a bucket for multiple web apps, append their endpoints to
    the `AllowedOrigins` list.

```
[
  {
    "AllowedHeaders": [
      "*"
    ],
    "AllowedMethods": [
      "GET",
      "PUT",
      "POST",
      "DELETE",
      "HEAD"
    ],
    "AllowedOrigins": [
      "https://`WebAppEndpoint`"
    ],
    "ExposeHeaders": [
      "last-modified",
       "content-length",
      "etag",
      "x-amz-version-id",
      "content-type",
      "x-amz-request-id",
      "x-amz-id-2",
      "date",
      "x-amz-cf-id",
      "x-amz-storage-class",
      "access-control-expose-headers"
     ],
    "MaxAgeSeconds": 3000
  }
]
```

4. Choose **Save changes** to update the CORS.
   To test your CORS configuration, see [Testing CORS](../../../AmazonS3/latest/userguide/testing-cors.md "../../../AmazonS3/latest/userguide/testing-cors.md").
