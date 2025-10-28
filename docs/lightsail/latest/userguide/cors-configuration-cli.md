# Configure CORS using the AWS CLI

You can configure CORS for your Lightsail bucket using the AWS CLI with the `--cors` parameter. This parameter accepts a JSON file that contains your CORS configuration.
For more information about the elements of a CORS configuration, see [Elements of a CORS configuration](cors-how-evaluation-works.md#cors-configuration-elements "cors-how-evaluation-works.md#cors-configuration-elements").

###### Topics

- [Apply a CORS configuration](#cors-configuration-apply "#cors-configuration-apply")
- [Example CORS configurations](#cors-configuration-examples "#cors-configuration-examples")
- [Remove CORS configurations](#cors-remove-configuration "#cors-remove-configuration")

## Apply a CORS configuration

The following procedure shows how a CORS configuration can be applied to a bucket by specifying a JSON file. For more example configurations, see [Example CORS configurations](#cors-configuration-examples "#cors-configuration-examples").

###### To configure CORS for a bucket using the AWS CLI

1. Create a JSON file containing your CORS configuration. For example, create a file named `cors-config.json` with the following content:

```
{
  "CORSRules": [
    {
      "AllowedOrigins": ["https://example.com"],
      "AllowedMethods": ["GET", "PUT", "POST"],
      "AllowedHeaders": ["*"],
      "MaxAgeSeconds": 3000
    }
  ]
}
```

2. Use the AWS CLI to apply the CORS configuration to your bucket:

```
aws lightsail update-bucket --bucket-name `amzn-s3-demo-bucket` --cors file://`cors-config.json`
```

3. Verify the CORS configuration was applied successfully:

```
aws lightsail get-buckets --bucket-name `amzn-s3-demo-bucket` --include-cors
```

###### Note

Replace `amzn-s3-demo-bucket` with the name of your Lightsail bucket.

## Example CORS configurations

The following examples show common CORS configurations for different use cases.

###### Example 1: Allow all origins and methods

This configuration allows all origins to access your bucket using any HTTP method:

```
{
    "CORSRules": [
      {
        "AllowedOrigins": ["*"],
        "AllowedMethods": ["GET", "PUT", "POST", "DELETE", "HEAD"],
        "AllowedHeaders": ["*"],
        "MaxAgeSeconds": 3000
      }
    ]
  }
```

###### Example 2: Restrict to specific domain

This configuration allows only requests from `https://mywebsite.com`:

```
{
    "CORSRules": [
      {
        "AllowedOrigins": ["https://mywebsite.com"],
        "AllowedMethods": ["GET", "PUT"],
        "AllowedHeaders": ["Authorization", "Content-Type"],
        "ExposeHeaders": ["ETag"],
        "MaxAgeSeconds": 3600
      }
    ]
  }
```

###### Example 3: Multiple rules for different origins

This configuration defines different rules for different origins:

```
{
    "CORSRules": [
      {
        "AllowedOrigins": ["https://mywebsite.com"],
        "AllowedMethods": ["GET", "PUT", "POST"],
        "AllowedHeaders": ["*"],
        "MaxAgeSeconds": 3600
      },
      {
        "AllowedOrigins": ["https://cdn.mywebsite.com"],
        "AllowedMethods": ["GET"],
        "AllowedHeaders": ["Authorization"],
        "MaxAgeSeconds": 86400
      }
    ]
  }
```

## Remove CORS configurations

To remove the CORS configuration from your bucket, use the following AWS CLI command:

```
aws lightsail update-bucket --bucket-name `amzn-s3-demo-bucket` --cors '{"rules":[]}'
```

###### Note

Replace `amzn-s3-demo-bucket` with the name of your Lightsail bucket.

After removing the CORS configuration, cross-origin requests to your bucket will be blocked by browsers.
