

# Integrating router I/Os with MediaLive
<a name="integrate-eml-with-router"></a>

You can integrate your AWS Elemental MediaLive channels with your router I/Os in AWS Elemental MediaConnect. This enables you to combine the flexibility of the router with the processing and encoding capabilities of MediaLive.

You can connect MediaLive to your router setup in two ways:

1. **Use a MediaLive input as a destination for a router output**

   When you connect a router output to a MediaLive input, you can send routed content to MediaLive for processing. This is useful when you want to:
   + Incorporate MediaLive channels into your routing workflow
   + Dynamically switch which routed content is sent to MediaLive for processing

1. **Use a MediaLive channel output as a source for a router input**

   When you connect a MediaLive channel output to a router input, you can route processed content for global distribution. This is useful when you want to:
   + Use MediaLive processing features like content normalization, SCTE-35 processing, and clip replay before routing
   + Distribute MediaLive output across regions using the router's cross-region capabilities

## Prerequisites
<a name="integrate-eml-with-router-prerequisites"></a>

Before you start, ensure that:
+ You have administrator permissions for MediaConnect
+ You can coordinate with a MediaLive operator who has administrator permissions for MediaLive
**Note**  
This page describes the process from the MediaConnect perspective, assuming coordination with an operator managing MediaLive. One operator can perform both roles if they have the necessary permissions.
+ Your MediaLive operator has configured the necessary permissions for MediaLive to interact with MediaConnect. They can choose their preferred approach:
  + **Simple option**

    Use the `MediaLiveAccessRole`, which includes all necessary permissions for MediaLive to work with MediaConnect. This is the simplest option, and we recommend it for most use cases. For instructions, see [Create the trusted entity - simple option](https://docs.aws.amazon.com/medialive/latest/ug/setup-trusted-entity-simple.html).
  + **Complex option**

    Create your own IAM policy and role if you need more specific custom permissions. For instructions, see [Create the trusted entity - complex option](https://docs.aws.amazon.com/medialive/latest/ug/setup-trusted-entity-complex.html).

Keep in mind the following important considerations when using this feature:
+ The router I/O and the MediaLive pipeline must be in the same Availability Zone and AWS Region.
+ The encryption scheme on the router side must match the encryption scheme on the MediaLive side.
+ You can't delete connected resources. You must disconnect them first.
+ A MediaLive resource (input or channel output) can only be connected to one router I/O at a time.
+ You need the appropriate MediaLive permission on the target resource (`medialive:UpdateInput` for inputs, `medialive:UpdateChannel` for channels).

## Encryption options
<a name="eml-router-encryption"></a>

You can use the following encryption options for content moving between MediaConnect and MediaLive:

Automatic encryption key  
MediaConnect and MediaLive handle encryption automatically with no manual key management required. This is the simplest option, and we recommend it for most use cases.

AWS Secrets Manager encryption key  
Use this option if you must manage your own encryption keys. To use this option, provide the following:  
+ **Role ARN** – The ARN of the IAM role that allows the service to access your encryption keys.
+ **Secret ARN** – The ARN of the secret in Secrets Manager that contains your encryption key.
The content of the secret must be an AES-256 key in hexadecimal format. The key must have 64 digits.
If you use AWS Secrets Manager encryption, make sure the encryption configuration matches on both the MediaConnect and MediaLive sides. Both services must be authorized to access the secret.

## Procedure
<a name="integrate-eml-with-router-procedure"></a>

Follow the steps for the direction of integration that you want to set up.

### Connecting a router output to a MediaLive input
<a name="integrate-eml-with-router-output-section"></a><a name="integrate-eml-with-router-output-procedure"></a>

**To connect a router output to a MediaLive input**

1. **Create an input in MediaLive**

   Ask your MediaLive operator to create an input with the following settings:
   + The input type must be **MediaConnect router**.
   + They must specify an Availability Zone for each pipeline.
     + For a single-pipeline input, specify one Availability Zone.
     + For a standard (dual-pipeline) input, specify two Availability Zones.
   + The pipeline ID must be either 0 or 1.
   + Choose the encryption type. For more information, see [Encryption options](#eml-router-encryption).

   After creation, the MediaLive input appears in the MediaConnect console as an available destination for your router output.

1. **Create a router output in MediaConnect**

   Create or update a router output with the following settings:
   + Choose **MediaLive input** as the output type.
   + Specify the ARN of the MediaLive input from step 1.
   + Specify the pipeline ID (0 or 1).
   + Choose the encryption type to match the MediaLive input. For more information, see [Encryption options](#eml-router-encryption).

1. **Create a channel in MediaLive**

   The MediaLive operator must create a MediaLive channel and attach the MediaLive input from step 1. With this setup in place, you can send video from the MediaConnect router to MediaLive.

### Connecting a MediaLive channel output to a router input
<a name="integrate-eml-with-router-input-section"></a><a name="integrate-eml-with-router-input-procedure"></a>

**To connect a MediaLive channel output to a router input**

1. **Create a MediaConnect Router output group in MediaLive**

   Ask your MediaLive operator to configure the channel with a MediaConnect Router output group with the following settings:
   + Specify an Availability Zone for each pipeline.
   + Add one or more outputs to the output group.
   + Choose the encryption type. For more information, see [Encryption options](#eml-router-encryption).

1. **Create a router input in MediaConnect**

   Create or update a router input with the following settings:
   + Choose **MediaLive channel** as the input type.
   + Specify the ARN of the MediaLive channel from step 1.
   + Specify the pipeline ID (0 or 1).
   + Specify the output name from the Router output group.
   + Choose the decryption type to match the MediaLive channel output. For more information, see [Encryption options](#eml-router-encryption).
**Note**  
You can create the router input in a disconnected state and connect it to the MediaLive channel output later.

1. **Start the channel and router input**

   Start both the MediaLive channel and the router input. With this setup in place, you can send processed content from MediaLive to the MediaConnect router.

## Troubleshooting
<a name="integrate-eml-with-router-troubleshoot"></a>

If you encounter issues with this workflow, use this checklist to identify and resolve common problems:
+ The MediaLive resource (input or channel) that you specified exists in your AWS account.
+ The MediaLive resource is the correct type (MediaConnect router input type for inputs, or a channel with a MediaConnect Router output group configured).
+ The router I/O and the MediaLive pipeline are in the same Availability Zone and AWS Region.
+ The encryption scheme on the router side matches the encryption scheme on the MediaLive side.
+ You have the appropriate MediaLive permission on the target resource (`medialive:UpdateInput` for inputs, `medialive:UpdateChannel` for channels).
+ The MediaLive resource is not already connected to another router I/O.

## Additional resources
<a name="integrate-eml-with-router-additional-resources"></a>

Connection management is focused on the router. You use the router API operations to create router inputs and outputs that connect to MediaLive channels and inputs.

To connect MediaLive resources to router I/Os programmatically, see the following pages in the *MediaConnect API Reference*:
+ [CreateRouterInput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_CreateRouterInput.html)
+ [CreateRouterOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_CreateRouterOutput.html)
+ [UpdateRouterInput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateRouterInput.html)
+ [UpdateRouterOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateRouterOutput.html)

This includes information about how to use these operations and parameters in one of the language-specific AWS SDKs.