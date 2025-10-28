# Internetwork Traffic Privacy

This topic describes how Amazon SageMaker AI secures connections from the service to other locations.

Internetwork communications support TLS 1.2 encryption between all components and clients. We recommend TLS 1.3.

Instances can be connected to Customer VPC, providing access to S3 VPC endpoints or customer repositories. Internet egress can be
managed through this interface by the customer if service platform internet egress is
disabled for notebooks. For training and hosting, egress through the service platform is not
available when connected to the customer's VPC.

By default, API calls made to published endpoints traverse the public network to the
request router.
SageMaker AI supports Amazon Virtual Private Cloud interface endpoints powered by AWS PrivateLink for
private connectivity between the customer's VPC and the request router to access hosted
model endpoints. For information about Amazon VPC, see [Connect to SageMaker AI Within your VPC](interface-vpc-endpoint.md "interface-vpc-endpoint.md")
