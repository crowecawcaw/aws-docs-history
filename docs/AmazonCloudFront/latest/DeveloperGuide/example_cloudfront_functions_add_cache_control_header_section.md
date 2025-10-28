# Add a cache control header to a CloudFront Functions viewer response event

The following code example shows how to add a cache control header to a CloudFront Functions viewer response event.

JavaScript

**JavaScript runtime 2.0 for CloudFront Functions**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[CloudFront Functions examples](https://github.com/aws-samples/amazon-cloudfront-functions/tree/main/add-cache-control-header "https://github.com/aws-samples/amazon-cloudfront-functions/tree/main/add-cache-control-header")
repository.

```
async function handler(event) {
    var response = event.response;
    var headers = response.headers;

    if (response.statusCode >= 200 && response.statusCode < 400) {
        // Set the cache-control header
        headers['cache-control'] = {value: 'public, max-age=63072000'};
    }

    // Return response to viewers
    return response;
}


```

For a complete list of AWS SDK developer guides and code examples, see
[Using CloudFront with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
