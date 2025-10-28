End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Example CORS policy: Read access for a specific domain

The following policy allows a webpage from `https://www.example.com` to retrieve content from your AWS Elemental MediaStore
container. The request includes all HTTP headers from `https://www.example.com`, and the service responds only to HTTP GET
and HTTP HEAD requests from `https://www.example.com`. The results are cached for 3,000 seconds before a new set of results
is delivered.

```
[
  {
    "AllowedHeaders": [
      "*"
    ],
    "AllowedMethods": [
      "GET",
      "HEAD"
    ],
    "AllowedOrigins": [
      "https://www.example.com"
    ],
    "MaxAgeSeconds": 3000
  }
]
```
