

# Requirements
<a name="requirements"></a>

Before integrating as a provider service with AWS Entity Resolution, complete the following requirements. 

**Topics**
+ [List a provider service on AWS Data Exchange](#list-provider-service)
+ [Identify your attributes](#provider-create-schema-mapping)
+ [Request the AWS Entity Resolution OpenAPI specification](#request-openapi-spec)

## List a provider service on AWS Data Exchange
<a name="list-provider-service"></a>

As a third-party provider, you must list your product on the [AWS Data Exchange (ADX)](https://aws.amazon.com/data-exchange/) Product Catalog. After your product is listed on the AWS Data Exchange Product Catalog, subscribers can subscribe to your product through either a public or private offer.

**To list a provider service on AWS Data Exchange**

1. If you are a new data product provider on AWS Data Exchange, complete the steps in the section titled [Getting started as a provider](https://docs.aws.amazon.com/data-exchange/latest/userguide/provider-getting-started.html) in the *AWS Data Exchange User Guide*.

1. Create a REST API data set and publish a new product that contains APIs on AWS Data Exchange by following the steps in the section titled [How to publish a product containing APIs](https://docs.aws.amazon.com/data-exchange/latest/userguide/publishing-products.html#publish-API-product) in the *AWS Data Exchange User Guide*. You can complete the process by using either the AWS Data Exchange console or the AWS Command Line Interface. 

   If you've set the product visibility **Public**, the public offer is available to all subscribers.

   If you've set the product visibility **Private**, complete the steps in the section titled [Create custom offers](https://docs.aws.amazon.com/data-exchange/latest/userguide/create-custom-offers.html) in the *AWS Data Exchange User Guide*, depending on your use case. 

   The following image shows an example of an available product in the AWS Data Exchange Product Catalog.

    ![An example of a published product in the AWS Data Exchange Product Catalog.](http://docs.aws.amazon.com/entityresolution/latest/userguide/images/ADX-catalog-example.png)

1. After the product is available on the AWS Data Exchange Product Catalog, the subscriber can subscribe to the product in the following ways.
   + Subscribe the public product.
   + Use a [private offer ](https://docs.aws.amazon.com/data-exchange/latest/userguide/subscribe-to-private-offer.html)(custom offer) that has been issued by the provider service.
   + Use a [Bring Your Own Subscription (BYOS)](https://docs.aws.amazon.com/data-exchange/latest/userguide/subscribe-to-byos-offer.html) offer. 

   For more information, see [Subscribe to and access a product containing APIs](https://docs.aws.amazon.com/data-exchange/latest/userguide/subscribing-to-product.html#subscribing-to-API-product) in the *AWS Data Exchange User Guide*.

## Identify your attributes
<a name="provider-create-schema-mapping"></a>

*Attributes* of the input data are the type definitions of the entities to be resolved in a workflow. Some examples of attributes are `FirstName`, `LastName`, `Email`, or `Custom String`.

When you identify your attributes, you should note any requirements or guidelines. 

**Example**  
The following is an example of validations for identifying provider attributes.  
+ Either the `FirstName` or `LastName` attribute is mandatory.
+ If the `Email` attribute is present, it must be hashed.

As a provider, you must identify the attributes in your provider service product and then communicate these attributes to the AWS Entity Resolution Business Development team at aws-entity-resolution-bd@amazon.com for additional validation before proceeding.

## Request the AWS Entity Resolution OpenAPI specification
<a name="request-openapi-spec"></a>

AWS Entity Resolution has an OpenAPI specification that you as a provider can use as a handshake that contains the APIs involved in the integration. For more information, see [Using the AWS Entity Resolution OpenAPI specification](entity-resolution-open-api.md).

To request the OpenAPI definition, contact the AWS Entity Resolution Business Development team at aws-entity-resolution-bd@amazon.com. 