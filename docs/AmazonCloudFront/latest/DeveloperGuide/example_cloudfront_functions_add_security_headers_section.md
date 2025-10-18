# Add HTTP security headers to a CloudFront Functions viewer response event

The following code example shows how to add HTTP security headers to a CloudFront Functions viewer response event.


JavaScript


**JavaScript runtime 2.0 for CloudFront Functions**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [CloudFront Functions examples](https://github.com/aws-samples/amazon-cloudfront-functions/tree/main/add-security-headers "https://github.com/aws-samples/amazon-cloudfront-functions/tree/main/add-security-headers")
 repository.
 



```
async function handler(event) {
    var response = event.response;
    var headers = response.headers;

    // Set HTTP security headers
    // Since JavaScript doesn't allow for hyphens in variable names, we use the dict["key"] notation 
    headers['strict-transport-security'] = { value: 'max-age=63072000; includeSubdomains; preload'}; 
    headers['content-security-policy'] = { value: "default-src 'none'; img-src 'self'; script-src 'self'; style-src 'self'; object-src 'none'; frame-ancestors 'none'"}; 
    headers['x-content-type-options'] = { value: 'nosniff'}; 
    headers['x-frame-options'] = {value: 'DENY'}; 
    headers['x-xss-protection'] = {value: '1; mode=block'};
    headers['referrer-policy'] = {value: 'same-origin'};
    
    // Return the response to viewers 
    return response;
}


```




For a complete list of AWS SDK developer guides and code examples, see
 [Using CloudFront with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
