# Grant Your Users Permissions to Upload Local

Files

If your users are uploading files from their local machines to SageMaker Canvas, you must attach a
CORS (cross-origin resource sharing) configuration to the Amazon S3 bucket that they're using. When
setting up or editing the SageMaker AI domain or user profile, you can specify either a custom
Amazon S3 location or the default location, which is a SageMaker AI created Amazon S3 bucket with a name that
uses the following pattern:
`s3://sagemaker-`{Region}`-`{your-account-id}``.
SageMaker Canvas adds your users' data to the bucket whenever they upload a file.

To grant users permissions to upload local files to the bucket, you can attach a CORS
configuration to it using either of the following procedures. You can use the first method
when editing the settings of your domain, where you opt in to allow SageMaker AI to attach the
CORS configuration to the bucket for you. You can also use the first method for editing a user
profile within a domain. The second method is the manual method, where you can attach the
CORS configuration to the bucket yourself.

## SageMaker AI domain settings method

To grant your users permissions to upload local files, you can edit the Canvas
application configuration in the domain settings. This attaches a Cross-Origin Resource
Sharing (CORS) configuration to the Canvas storage configuration's Amazon S3 bucket and
grants all users in the domain permission to upload local files into SageMaker Canvas. By default,
the permissions option is turned on when you set up a new domain, but you can turn this
option on and off as needed.

###### Note

If you have an existing CORS configuration on the storage configuration Amazon S3 bucket,
turning on the local file upload option overwrites the existing configuration with the new
configuration.

The following procedure shows how you can turn on this option by editing the domain
settings in the SageMaker AI console.

1. Go to the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the left navigation pane, choose **Domains**.
3. From the list of domains, choose your domain.
4. On the domain details page, select the **App Configurations**
   tab.
5. Go to the **Canvas** section and choose
   **Edit**.
6. Turn on the **Enable local file upload** toggle. This attaches the
   CORS configuration and grants local file upload permissions.
7. Choose **Submit**.

Users in the specified domain should now have local file upload permissions.

You can also grant permissions to specific user profiles in a domain by following
the preceding procedure and going into the user profile settings instead of the overall
domain settings.

## Amazon S3 bucket method

If you want to manually attach the CORS configuration to the SageMaker AI Amazon S3 bucket, use the
following procedure.

1. Sign in to [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose your bucket. If your domain uses the default SageMaker AI created bucket, the
   bucket’s name uses the following pattern:
   `s3://sagemaker-`{Region}`-`{your-account-id}``.
3. Choose **Permissions**.
4. Navigate to **Cross-origins resource sharing (CORS)**.
5. Choose **Edit**.
6. Add the following CORS policy:

```

[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "POST"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]

```

7. Choose **Save changes**.

In the preceding procedure, the CORS policy must have `"POST"` listed under
`AllowedMethods`.

After you've gone through the procedure, you should have:

- An IAM role assigned to each of your users.
- Amazon SageMaker Studio Classic runtime permissions for each of your users. SageMaker Canvas uses Studio Classic to
  run the commands from your users.
- If the users are uploading files from their local machines, a CORS policy attached
  to their Amazon S3 bucket.

If your users still can't upload the local files after you update the CORS policy, the
browser might be caching the CORS settings from a previous upload attempt. If they're
running into issues, instruct them to clear their browser cache and try again.
