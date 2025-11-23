# Integrating router

outputs
with MediaLive inputs

You set up a router output in AWS Elemental MediaConnect so that it can send content to AWS Elemental MediaLive. With
this setup, your router output can serve as an upstream input for a MediaLive channel,
enabling MediaLive to process your video stream.

This setup is useful when you want to:

- Send routed content to MediaLive for processing
- Incorporate MediaLive channels into your routing workflow
- Maintain flexible routing control over MediaLive inputs

## Prerequisites

Before you start, ensure that:

- You have administrator permissions for MediaConnect
- You can coordinate with a MediaLive operator who has administrator permissions for MediaLive

###### Note

This page describes the process from the MediaConnect perspective, assuming
coordination with an operator managing MediaLive. One operator can perform both roles if
they have the necessary permissions.

Keep in mind the following important considerations when using this feature:

- You can't update or delete the MediaLive input while it's connected to a router
  output in MediaConnect
- The MediaLive input must not be already attached to another router output in
  MediaConnect

## Procedure

###### To connect a router output to a MediaLive input

1. **Verify MediaLive permissions**

Check with your MediaLive operator that they have the necessary permissions for
MediaLive to interact with MediaConnect. They can choose their preferred
approach:

    * **Simple option (recommended)**


    Use the `MediaLiveAccessRole`, which includes all necessary
     permissions for MediaLive to work with MediaConnect. For instructions, see
     [Create the trusted
     entity - simple option.](../../../medialive/latest/ug/setup-trusted-entity-simple.md "../../../medialive/latest/ug/setup-trusted-entity-simple.md")
    * **Complex option**


    Create your own IAM policy and role if you need more specific custom
     permissions. Alternatively, you can add these specific MediaConnect permissions
     to an existing custom IAM policy and role. For instructions, see [Create the trusted
     entity - complex option](../../../medialive/latest/ug/setup-trusted-entity-complex.md "../../../medialive/latest/ug/setup-trusted-entity-complex.md").

2. **Create an input in MediaLive**

Ask your MediaLive operator to create an input with the following
settings:

    * The input type must be **MediaConnect
     router**
    * They must specify an Availability Zone for each pipeline




    	+ For a single-pipeline input, specify one Availability Zone
    	+ For a standard (dual-pipeline) input, specify two Availability Zones
    * The pipeline ID must be either 0 or 1

After creation, the MediaLive input will appear in the MediaConnect console as
an an available destination for your router output. 3. **Create a router output in MediaConnect**

Create or update a router output with the following settings:

    * Choose **MediaLive input** as the output type.
    * Specify the ARN of the MediaLive input that was created in step 2.
    * Choose how to encrypt the content as it moves from the router output to the
     MediaLive input.




    	+ **Automatic encryption key** - Choose this if you want
    	 automatic key management (recommended in most cases). With this option,
    	 MediaConnect will privately provide the key to MediaLive.
    	+ **AWS Secrets Manager encryption key** - Choose this if your
    	 security requirements require you to use your own encryption keys. Then, do
    	 the following:




    		- For **Role ARN**, enter the ARN of the IAM role
    		 that allows MediaConnect to access your encryption keys.
    		- For Secret ARN, enter the ARN of the secret in Secrets Manager that
    		 contains your encryption key.


    		###### Important


    		 The content of the secret must be an AES-256 key in hexadecimal format.
    		 The key must have 64 digits.



    		###### Note

    		When using AWS Secrets Manager encryption, you'll need to coordinate with
    		 your MediaLive team:



    			* The MediaLive input must use a matching Key Type and Secret
    			 ARN
    			* Both MediaConnect and MediaLive services must have
    			 authorization to access the customer-managed secret

4. **Create a channel in MediaLive**

As the final step, the MediaLive operator must also create a MediaLive channel
and attach the MediaLive input that was created in step 2. With this setup in place,
you can now send video from the MediaConnect router to MediaLive.

## Troubleshooting

If you encounter issues with this workflow, use this checklist to identify and resolve
common problems:

- The MediaLive input that you specified exists in your AWS account
- You have permissions to view resources in both MediaConnect and MediaLive
- The MediaLive input is of the correct type (it must be a MediaConnect router input
  type)
- The MediaLive input and pipeline are not already attached to another router output
- The pipeline ID is 0 or 1

## Additional resources

Connection management is focused on the router. You use the router API operations to
select a flow output to feed into your router input, or a flow source to receive content
from your router output.

To connect flows to router I/Os programmatically, see the following pages in the _MediaConnect API Reference_:

- [CreateRouterInput](../api/API_CreateRouterInput.md "../api/API_CreateRouterInput.md")
- [CreateRouterOutput](../api/API_CreateRouterOutput.md "../api/API_CreateRouterOutput.md")
- [UpdateRouterInput](../api/API_UpdateRouterInput.md "../api/API_UpdateRouterInput.md")
- [UpdateRouterOutput](../api/API_UpdateRouterOutput.md "../api/API_UpdateRouterOutput.md")

This includes information about how to use thesee operations and parameters in one of the
language-specific AWS SDKs.
