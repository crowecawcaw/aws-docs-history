

# Review
<a name="review"></a>


| CONTAINER\_BUILD\_PERF\_03: How do you make sure to get consistent results for your target images? | 
| --- | 
|   | 

 Using the `latest` tag for the parent image could potentially lead to issues because the latest version of the image might include breaking changes compared to the version that is currently used. 


| CONTAINER\_BUILD\_PERF\_04: How do you make sure to use updated versions for parent images? | 
| --- | 
|   | 

 **Implement a notification mechanism for updated parent images** 

 If you’re using a team- or enterprise-wide image, you should implement a notification mechanism based as part of your CI/CD chain to distribute the information about a new parent image to the teams. The teams should build target images with the new parent images and measure the performance impact of the changes by running a proper test suite. 