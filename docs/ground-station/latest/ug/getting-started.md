# Onboard satellite

Onboarding a satellite into AWS Ground Station is a multistep process involving data
collection, technical validation, spectrum licensing, with integration and testing. There are
also non-disclosure agreements (NDAs) required.

## Customer onboarding process overview

Satellite onboarding is a manual process that can be found on the
[Satellites and Resources](https://console.aws.amazon.com/groundstation/home#resources "https://console.aws.amazon.com/groundstation/home#resources")
section of the AWS Ground Station console page. The following describes the overall process.

1. Review the
   [AWS Ground Station Locations](aws-ground-station-antenna-locations.md "aws-ground-station-antenna-locations.md")
   section to determine if your satellite meets the geographical and radio frequency
   characteristics.
2. To start onboarding your satellite to AWS Ground Station, please email
   `<aws-groundstation@amazon.com>`
   with a brief summary of your mission and satellite needs,
   including your organization name, the frequencies required, when the satellites will be or
   were launched, the satellite's orbit type, and if you plan to use [Use the AWS Ground Station digital twin feature](digital-twin.md "digital-twin.md").
3. Once your request is reviewed and approved, AWS Ground Station will apply for regulatory licensing at
   the specific locations you plan to use. The duration of this step will vary depending on
   the locations and any existing regulations.
4. After this approval is obtained, your satellite will be visible for you to use. AWS Ground Station
   will send you a notification of the successful update.

## (Optional) Naming satellites

After onboarding, you may want to add a name to your satellite record to more easily recognize
it. The AWS Ground Station console has the ability to display a user defined name for a satellite along
with the Norad ID when using the Contacts page. Displaying the satellite name makes it much
easier to select the correct satellite when scheduling. To do this,
[tags](../../../whitepapers/latest/tagging-best-practices/what-are-tags.md "../../../whitepapers/latest/tagging-best-practices/what-are-tags.md")
can be used.

Tagging AWS Ground Station Satellites can be done via the
[tag-resource](../../../cli/latest/reference/groundstation/tag-resource.md "../../../cli/latest/reference/groundstation/tag-resource.md")
API with the AWS CLI or one of the AWS SDKs. This guide will cover using the AWS Ground Station CLI to tag
the public broadcast satellite Aqua (Norad ID 27424) in `us-west-2`.

**AWS Ground Station CLI**

The AWS CLI can be used to interact with AWS Ground Station. Before using AWS CLI to tag your satellites,
the following AWS CLI prerequisites must be fulfilled:

- Ensure that AWS CLI is installed. For information about installing AWS CLI, see
  [Installing the
  AWS CLI version 2](../../../cli/latest/userguide/install-cliv2.md "../../../cli/latest/userguide/install-cliv2.md").
- Ensure that AWS CLI is configured. For information about configuring AWS CLI, see
  [Configuring
  the AWS CLI version 2](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md").
- Save your frequently used configuration settings and credentials in files that are
  maintained by the AWS CLI. You need these settings and credentials to reserve and manage
  your AWS Ground Station contacts with AWS CLI. For more information about saving your configuration and
  credential settings, see
  [Configuration and credential file settings](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md") .

Once AWS CLI is configured and ready to use, review the
[AWS Ground
Station CLI Command Reference](../../../cli/latest/reference/groundstation/index.md "../../../cli/latest/reference/groundstation/index.md")
page to familiarize yourself with available commands. Follow the AWS CLI command structure when
using this service and prefix your commands with `groundstation` to specify AWS Ground Station
as the service you want to use. For more information on the AWS CLI command structure, see
[Command
Structure in the AWS CLI](../../../cli/latest/userguide/cli-usage-commandstructure.md "../../../cli/latest/userguide/cli-usage-commandstructure.md")
page. An example command structure is provided below.

```
aws groundstation <command> <subcommand> [options and parameters]
```

**Name a Satellite**

First you need to get the ARN for the satellite(s) you wish to tag. This can be done via the
[list-satellites](../../../cli/latest/reference/groundstation/list-satellites.md "../../../cli/latest/reference/groundstation/list-satellites.md")
API in the AWS CLI:

```
aws groundstation list-satellites --region us-west-2
```

Running the above CLI command will return an output similar to this:

```

{
    "satellites": [
        {
            "groundStations": [
                "Ohio 1",
                "Oregon 1"
            ],
            "noradSatelliteID": 27424,
            "satelliteArn": "arn:aws:groundstation::111111111111:satellite/11111111-2222-3333-4444-555555555555",
            "satelliteId": "11111111-2222-3333-4444-555555555555"
        }
    ]
}

```

Find the satellite you wish to tag and note down the `satelliteArn`. One important
caveat for tagging is that the
[tag-resource](../../../cli/latest/reference/groundstation/tag-resource.md "../../../cli/latest/reference/groundstation/tag-resource.md")
API requires a regional ARN, and the ARN returned by [list-satellites](../../../cli/latest/reference/groundstation/list-satellites.md "../../../cli/latest/reference/groundstation/list-satellites.md") is global. For the next step, you should augment the ARN with the region
you would like to see the tag in (likely the region you schedule in). For this example, we are
using `us-west-2`. With this change, the ARN will go from:

```
arn:aws:groundstation::111111111111:satellite/11111111-2222-3333-4444-555555555555
```

to:

```
arn:aws:groundstation:us-west-2:111111111111:satellite/11111111-2222-3333-4444-555555555555
```

In order to show the satellite name in the console, the satellite must have a tag with `“Name"` as the key. Additionally, because we are using the AWS CLI,
the quotation marks must be escaped with a backslash. The tag will look something like:

```
{\"Name\":\"AQUA\"}
```

Next, you will call the [tag-resource](../../../cli/latest/reference/groundstation/tag-resource.md "../../../cli/latest/reference/groundstation/tag-resource.md") API to tag the satellite. This can be done with the AWS CLI like so:

```
aws groundstation tag-resource --region us-west-2 --resource-arn arn:aws:groundstation:us-west-2:111111111111:satellite/11111111-2222-3333-4444-555555555555 --tags '{"Name":"AQUA"}'
```

After doing this, you'll be able to see the name you set for the satellite in the AWS Ground Station
console.

**Change the Name For a Satellite**

If you want to change the name for a satellite, you can simply call [tag-resource](../../../cli/latest/reference/groundstation/tag-resource.md "../../../cli/latest/reference/groundstation/tag-resource.md") with the satellite ARN again with the same `“Name”` key, but with a
different value in the tag. This will update the existing tag and show the new name in the
console. An example call for this looks like:

```
aws groundstation tag-resource --region us-west-2 --resource-arn arn:aws:groundstation:us-west-2:111111111111:satellite/11111111-2222-3333-4444-555555555555 --tags '{"Name":"NewName"}'
```

**Remove the Name For a Satellite**

The name set for a satellite can be removed with the [untag-resource](../../../cli/latest/reference/groundstation/untag-resource.md "../../../cli/latest/reference/groundstation/untag-resource.md") API. This API
needs the satellite ARN with the region the tag is in, and a list of tag keys. For the name,
the tag key is `“Name”`. An example call to this API using the AWS CLI looks like:

```
aws groundstation untag-resource --region us-west-2 --resource-arn arn:aws:groundstation:us-west-2:111111111111:satellite/11111111-2222-3333-4444-555555555555 --tag-keys Name
```

## Public broadcast satellites

In addition to onboarding your own satellites, you may request to onboard with supported
public broadcast satellites that provide a publicly accessible downlink communication path.
This enables you to use AWS Ground Station to downlink data from these satellites.

###### Note

You will not be able to uplink to these satellites. You will only be able to use the
publicly accessible downlink communication paths.

AWS Ground Station supports onboarding of the following satellites to downlink direct broadcast data:

- Aqua
- SNPP
- JPSS-1/NOAA-20
- Terra

Once onboarded, these satellites can be accessed for immediate use. AWS Ground Station maintains a
number of preconfigured AWS CloudFormation templates to make getting started with the service easier. See
[Example mission profile configurations](examples.md "examples.md")
for examples of how AWS Ground Station can be used.

For more information about these satellites and the kind of data they transmit, see [Aqua](https://aqua.nasa.gov/ "https://aqua.nasa.gov/"),
[JPSS-1/NOAA-20 and
SNPP](https://www.nesdis.noaa.gov/our-satellites/currently-flying/joint-polar-satellite-system "https://www.nesdis.noaa.gov/our-satellites/currently-flying/joint-polar-satellite-system"), and [Terra](https://terra.nasa.gov/ "https://terra.nasa.gov/").
