

# Know and respect your cell's limit
<a name="known-and-respect-your-cells-limit"></a>

 Cell sizing is fully related with the limits of traffic that your cell can support without impact negatively the cell's customers. [Using load shedding to avoid overload](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/?did=ba_card&trk=ba_card) is fundamental and can reduce unknown behaviors in your workload, once you know how much traffic your cells can handle. You can determine this through load testing and chaos engineering. Some AWS services can help to do this control, such as [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html#apigateway-how-throttling-limits-are-applied), which supports rate limiting at the API level (by resource and method) and at stage-level. 

 If you are using a more customized approach for your cell router, you can implement algorithms like [token bucket](https://en.wikipedia.org/wiki/Token_bucket). An example of the use of token bucket is made by [Amazon EC2 API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/throttling.html#throttling-limits-rate-based). 