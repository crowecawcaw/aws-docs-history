

# How AWS Panorama uses Secrets Manager
<a name="integrating_how-services-use-secrets_PAN"></a>

AWS Panorama is a service that brings computer vision to your on-premises camera network. You use AWS Panorama to register an appliance, update its software, and deploy applications to it. When you register a video stream as a data source for your application, if the stream is password protected, AWS Panorama stores the credentials for it in a Secrets Manager secret. For more information, see [Managing camera streams in AWS Panorama](https://docs.aws.amazon.com/panorama/latest/dev/appliance-cameras.html) in the *AWS Panorama Developer Guide*.