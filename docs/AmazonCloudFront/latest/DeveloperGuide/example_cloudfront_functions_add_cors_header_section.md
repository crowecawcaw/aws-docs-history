# Add a CORS header to a CloudFront Functions viewer response event

The following code example shows how to add a CORS header to a CloudFront Functions viewer response event.


JavaScript


**JavaScript runtime 2.0 for CloudFront Functions**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [CloudFront Functions examples](https://github.com/aws-samples/amazon-cloudfront-functions/tree/main/add-cors-header "https://github.com/aws-samples/amazon-cloudfront-functions/tree/main/add-cors-header")
 repository.
 



```
async function handler(event)  {
    var request = event.request;
    var response  = event.response;
 
    // If Access-Control-Allow-Origin CORS header is missing, add it.
    // Since JavaScript doesn't allow for hyphens in variable names, we use the dict["key"] notation.
    if (!response.headers['access-control-allow-origin'] && request.headers['origin']) {
        response.headers['access-control-allow-origin'] = {value: request.headers['origin'].value};
        console.log("Access-Control-Allow-Origin was missing, adding it now.");
    }

    return response;
}



```




For a complete list of AWS SDK developer guides and code examples, see
 [Using CloudFront with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
