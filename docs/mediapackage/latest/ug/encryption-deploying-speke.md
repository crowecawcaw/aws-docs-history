# Deploying SPEKE

Your digital rights management (DRM) solution provider can help you get set up to use DRM
encryption in MediaPackage. Generally, the provider gives you a SPEKE gateway to deploy in your
AWS account in the same AWS Region where MediaPackage is running. Along with configuring your
origin endpoints with the right encryption settings, you must [configure event notifications](cloudwatch-events-notification.md "cloudwatch-events-notification.md") for the [key provider events](cloudwatch-events-example.md#key-provider-state-events "cloudwatch-events-example.md#key-provider-state-events") that MediaPackage is generating as CloudWatch Events. For information about
configuring encryption settings for your endpoint, see the applicable section for your
protocol: [HLS
encryption fields](endpoints-hls-encryption.md "endpoints-hls-encryption.md"), [MSS encryption fields](endpoints-smooth-encryption.md "endpoints-smooth-encryption.md"), [CMAF
encryption fields](endpoints-cmaf-encryption.md "endpoints-cmaf-encryption.md"), and [DASH
encryption fields](endpoints-dash-encryption.md "endpoints-dash-encryption.md").

If you must build your own API Gateway to connect MediaPackage to your key service, you can use the
[SPEKE Reference
Server](https://github.com/awslabs/speke-reference-server "https://github.com/awslabs/speke-reference-server") available on GitHub as a starting point.
