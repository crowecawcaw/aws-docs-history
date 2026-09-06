

# Coordinate with the MediaPackage operator
<a name="origin-server-emp"></a>

You and the operator of the AWS Elemental MediaPackage service must agree about the destination for the output of your MediaPackage output group.

**Note**  
You can send to AWS Elemental MediaPackage by creating a MediaPackage output group or by creating an HLS output group. See [Delivering to MediaPackage](delivering-to-mediapackage.md) for a description of the differences.

## MediaPackage v1 (HLS) coordination
<a name="coordinate-emp-v1"></a>

**To arrange setup of the MediaPackage v1 destination**

1. Ask the MediaPackage user to create one channel. Even if the MediaLive channel is a [standard channel](plan-redundancy.md) (with two pipelines), you need only one MediaPackage channel.

1. Obtain the ID of the MediaPackage channel. For example, `curling-live`. The channel ID is case sensitive. 

## MediaPackage v2 (CMAF Ingest) coordination
<a name="coordinate-emp-v2"></a>

**To arrange setup of the MediaPackage v2 destination**

1. Ask the MediaPackage user to create MediaPackage v2 channels in the required regions. Obtain the following information for each destination:
   + AWS region name (for example, `us-east-1` or `eu-west-1`)
   + MediaPackage channel group name
   + MediaPackage channel name
   + Which ingest endpoint (ENDPOINT\_1 or ENDPOINT\_2) is the preferred input for the MediaPackage channel

1. If you plan to use additional destinations for redundancy or cross-region delivery, coordinate the setup of additional MediaPackage v2 channels as needed.

**Note**  
You don't need user credentials to send a MediaPackage output group to MediaPackage. MediaLive has permission to write to MediaPackage via the trusted entity. Someone in your organization should have already set up these permissions. For more information, see [Access requirements for the trusted entity](trusted-entity-requirements.md).