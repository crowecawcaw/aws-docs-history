# Add index.html to request URLs without a file name in a CloudFront Functions viewer request event

The following code example shows how to add index.html to request URLs without a file name in a CloudFront Functions viewer request event.

JavaScript

**JavaScript runtime 2.0 for CloudFront Functions**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[CloudFront Functions examples](https://github.com/aws-samples/amazon-cloudfront-functions/tree/main/url-rewrite-single-page-apps "https://github.com/aws-samples/amazon-cloudfront-functions/tree/main/url-rewrite-single-page-apps")
repository.

```
async function handler(event) {
    var request = event.request;
    var uri = request.uri;

    // Check whether the URI is missing a file name.
    if (uri.endsWith('/')) {
        request.uri += 'index.html';
    }
    // Check whether the URI is missing a file extension.
    else if (!uri.includes('.')) {
        request.uri += '/index.html';
    }

    return request;
}


```

For a complete list of AWS SDK developer guides and code examples, see
[Using CloudFront with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
