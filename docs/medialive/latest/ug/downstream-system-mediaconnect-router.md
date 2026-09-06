

# Coordinate with the downstream system for a MediaConnect Router output group
<a name="downstream-system-mediaconnect-router"></a>

One advantage of MediaConnect Router is that you don't need to create any AWS Elemental MediaConnect resources before creating the MediaLive output. When you create a MediaLive channel with a MediaConnect Router output group, the outputs automatically appear as options in the MediaConnect Router API.

MediaConnect Router outputs support encryption for data in transit. You can choose one of the following encryption modes:
+ **AUTOMATIC** – The services handle encryption seamlessly using a service-managed secret. This is the recommended option.
+ **SECRETS\_MANAGER** – You provide the ARN of an AES-256 secret stored in AWS Secrets Manager. The secret must exist before you create the MediaLive channel.

You must specify the Availability Zones for the output group. For a single-pipeline channel, specify one Availability Zone. For a standard channel, specify two different Availability Zones to provide zonal resiliency.

**Important**  
If a MediaConnect Router resource has already been created, the Availability Zones you specify must match those of the existing resource. If the MediaConnect Router resource has not been created yet, the resource must be configured to match the Availability Zones you specify here.

You can use a MediaConnect Router input with a MediaConnect Router output to process video in MediaLive (for example, to normalize frame rate) and then pass the video back into MediaConnect Router. By design, when you use MediaConnect Router inputs and outputs, your entire transport workflow is end-to-end encrypted.