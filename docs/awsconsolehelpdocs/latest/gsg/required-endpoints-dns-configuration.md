

# Configuring VPC endpoints for accessing AWS Management Console
<a name="required-endpoints-dns-configuration"></a>

AWS Management Console Private Access supports operating in networks without access to the public internet. When you configure VPC endpoints for AWS Sign-In, AWS Management Console, and console static content, all browser traffic is routed through AWS PrivateLink. Internet connectivity is not required for the AWS Management Console itself.

AWS Management Console Private Access requires the following VPC endpoints. Replace {{region}} with your own Region information.

1. com.amazonaws.{{region}}.console – for AWS Management Console

1. com.amazonaws.{{region}}.signin – for AWS Sign-In

1. com.amazonaws.{{region}}.console-static – for static content and other console-specific APIs (required for network-isolated environments)

AWS Management Console calls AWS services through a combination of direct browser requests and requests that are proxied by web servers. You should also configure AWS PrivateLink VPC endpoints for all AWS services that you intend to use in your environment. If you access a service console that does not have a configured VPC endpoint, you might see errors for that functionality. This is expected behavior in a network-isolated environment.

**Note**  
Currently, AWS Management Console Private Access doesn't support endpoints such as `status.aws.amazon.com`, `health.aws.amazon.com`, and `docs.aws.amazon.com`. You will need to route these domains to the public internet, or accept that these features will be unavailable in a fully isolated environment.

**Note**  
The console-static VPC endpoint is required when you want to use the AWS Management Console in a network without access to the public internet. This endpoint handles static content (JavaScript, CSS, images) and console-specific APIs that were previously served over the public internet. If your network has internet connectivity, this endpoint is optional but recommended for full traffic control.

To use AWS Management Console Private Access in more than one AWS Region, create the `com.amazonaws.{{region}}.console` and `com.amazonaws.{{region}}.signin` endpoints in each Region where you want private access to the AWS Management Console. Also create VPC endpoints for the AWS services that you use in that Region. The `com.amazonaws.{{region}}.console-static` endpoint serves Region-agnostic static content and console-specific APIs, so you only need it in a single Region.