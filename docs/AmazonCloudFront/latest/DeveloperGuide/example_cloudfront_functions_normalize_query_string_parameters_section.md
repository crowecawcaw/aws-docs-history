# Normalize query string parameters in a CloudFront Functions viewer request

The following code example shows how to normalize query string parameters in a CloudFront Functions viewer request.


JavaScript


**JavaScript runtime 2.0 for CloudFront Functions**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [CloudFront Functions examples](https://github.com/aws-samples/amazon-cloudfront-functions/tree/main/normalize-query-string-parameters "https://github.com/aws-samples/amazon-cloudfront-functions/tree/main/normalize-query-string-parameters")
 repository.
 



```
function handler(event) {
     var qs=[];
     for (var key in event.request.querystring) {
         if (event.request.querystring[key].multiValue) {
             event.request.querystring[key].multiValue.forEach((mv) => {qs.push(key + "=" + mv.value)});
         } else {
             qs.push(key + "=" + event.request.querystring[key].value);
         }
     };
     
     event.request.querystring = qs.sort().join('&');
     
      
     return event.request;
}


```




For a complete list of AWS SDK developer guides and code examples, see
 [Using CloudFront with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
