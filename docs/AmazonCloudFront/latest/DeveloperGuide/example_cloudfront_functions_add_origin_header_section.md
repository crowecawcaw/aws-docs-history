# Add an origin header to a CloudFront Functions viewer request event

The following code example shows how to add an origin header to a CloudFront Functions viewer request event.


JavaScript


**JavaScript runtime 2.0 for CloudFront Functions**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [CloudFront Functions examples](https://github.com/aws-samples/amazon-cloudfront-functions/tree/main/add-origin-header "https://github.com/aws-samples/amazon-cloudfront-functions/tree/main/add-origin-header")
 repository.
 



```
async function handler(event) {
    var request = event.request;
    var headers = request.headers;
    var host = request.headers.host.value;
   
   // If origin header is missing, set it equal to the host header.
   if (!headers.origin)
       headers.origin = {value:`https://${host}`};
       
   return request;
}


```




For a complete list of AWS SDK developer guides and code examples, see
 [Using CloudFront with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
