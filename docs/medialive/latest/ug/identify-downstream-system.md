# Identify the output group types for the

downstream system

The first step in planning any AWS Elemental MediaLive workflow is to determine which types of [output groups](what-is-terminology.md "what-is-terminology.md") you need
to produce, based on the requirements and capabilities of the systems that are downstream of
MediaLive.

Perform this work with the downstream system before you assess the [upstream system](evaluate-upstream-system.md "evaluate-upstream-system.md"). Decision making in a workflow
starts with the downstream system, then works back to the upstream system.

###### Important

You should have already identified the downstream system or systems that you are going to
send MediaLive output to, for this workflow.
If
you have not yet identified the downstream system, you must do some research before continuing
with preparing your workflow. This guide can't help you to identify your downstream system.
When you know what your downstream systems are, return to this section.

###### To identify the output group

1. Obtain the following information from your downstream system.
   - The required output formats. For example, HLS.
   - The application protocol for each. For example, HTTP.

2. Decide on the delivery mode for your outputs.
   - You might have an output that is on a server that is on your EC2 instance in your
     VPC. Or you might have an output that is in Amazon S3. If one or both of these situations
     apply, you might want to set up for delivery via your VPC. For more information, see
     [Delivering outputs via your VPC](delivery-out-vpc.md "delivery-out-vpc.md").
   - If you don't have any of these types of outputs, you will deliver in the regular
     way.

3. Make sure that MediaLive includes an _output group_ that
   supports the output format and protocol that the downstream system requires. See [Output types supported in MediaLive](outputs-supported-containers.md "outputs-supported-containers.md").
4. If your preferred downstream system is another AWS media service, [read this for information about choosing the service](dss-compare-elemental-services.md#dss-choose-service "dss-compare-elemental-services.md#dss-choose-service").
5. If you are
   delivering to a Microsoft Smooth Streaming server, the setup depends on whether you want to
   protect your content with a digital rights management (DRM) solution. DRM prevents
   unauthorized people from accessing the content.
   - If you don't want to implement DRM, then create a Microsoft Smooth output group.
   - If you do want to implement DRM, you can create an HLS or MediaPackage output group
     to send the output to AWS Elemental MediaPackage, then use AWS Elemental MediaPackage to add DRM. You will then set up
     AWS Elemental MediaPackage to deliver to the Microsoft Smooth origin server.

6. Decide if you want to create an Archive output group in order to produce an archive file
   of the content. An archive file is a supplement to streaming; it isn't itself a streaming
   output. Typically, you create an archive file as a permanent file version of the streaming
   output.
7. Decide if you want to create a Frame capture output group in order to produce a frame
   capture output. A Frame capture output is a supplement to streaming; it isn't itself a
   streaming output. This type of output might be useful for your workflow. For example, you
   might use a Frame capture output to create thumbnails of the content.
8. Make a note of the output groups that you decide to create.

For example, after you have followed these steps, you might have this list of output
groups:

    * One HLS output group with AWS Elemental MediaPackage as the downstream system.
    * One RTMP output group sending to the downstream system of a social media
     site.
    * One Archive output group as a record.
