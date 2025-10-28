# Creating a harvest job

Create a harvest job to extract a live-to-VOD asset from an encrypted or clear (unencrypted) live HLS or DASH stream.

###### Important

To run a harvest job and save the live-to-VOD asset, MediaPackage must have
permissions to access and write to the Amazon S3 bucket where the asset will be stored.
To create a role that gives MediaPackage the right permissions, see [Allowing AWS Elemental MediaPackage to access other
AWS services](setting-up-create-trust-rel.md "setting-up-create-trust-rel.md").

You can use the MediaPackage console, the AWS CLI, or the MediaPackage API to create a
harvest job. For information about creating a job through the AWS CLI or MediaPackage
API, see the [AWS Elemental MediaPackage API Reference](../apireference.md "../apireference.md").

When you're creating a harvest job, don't put sensitive identifying information like customer account numbers
into free-form fields, such as the **ID** field. This applies when you're using the MediaPackage console,
MediaPackage API, AWS CLI, or AWS SDKs. Any data that you enter into MediaPackage might get picked up for inclusion in diagnostic logs or Amazon CloudWatch Events.

###### To create a harvest job (console)

1. Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage/ "https://console.aws.amazon.com/mediapackage/").
2. In the navigation pane, under **Live**, choose **Harvest
   jobs**.
3. On the **Harvest jobs** page, choose **Create harvest job**.
4. On the **Create harvest job** page, complete the fields as described in the following topics:
   - [Basic details fields](#hj-create-basic "#hj-create-basic")
   - [Start and end date and time fields](#hj-create-time "#hj-create-time")
   - [Destination fields](#hj-create-destination "#hj-create-destination")

5. Choose **Create**.

## Basic details fields

The basic details of a harvest job define its identifier and the source for the
live-to-VOD asset.

1. For **ID**, enter a name that describes the harvest
   job. The ID is the primary identifier for the harvest job. You can reuse
   the ID when the harvest job expires from your account. Supported
   characters are letters, numbers, underscores (\_), and dashes (-).
2. For **Origin endpoint**, select the endpoint that
   serves the live stream that you're harvesting the live-to-VOD asset
   from.

Note the following considerations.

    * Your harvest job must fall within your MediaPackage endpoint's **startover window**. The startover window determines the time frame that assets can be harvested from your endpoint. For example, if your endpoint has a startover window of three days, you can harvest your asset anytime within that time frame.



     A MediaPackage endpoint can have a startover window between zero and 14 days. To adjust your endpoint's startover window, see [Viewing a single endpoint](endpoints-view-one.md "endpoints-view-one.md").
    * Your harvested live-to-VOD asset can have a maximum duration of 24 hours. To set the live-to-VOD asset duration, see [Start and end date and time fields](#hj-create-time "#hj-create-time") in
     this chapter.
    * Your endpoint must serve either clear (unencrypted) or encrypted DASH or HLS content.
    * MediaPackage VOD doesn't currently support the ingestion of encrypted assets. If you're using your harvested assets in an MediaPackage video on demand workflow and your endpoint is encrypted, create an unencrypted shadow endpoint on the same channel. To do this, deselect **allow
     origination** so that the new endpoint can't be used for playback.
     MediaPackage creates the URL for endpoints that don't have origination enabled,
     but MediaPackage responds with an error to playback requests sent to this
     endpoint. For more information, see [Creating live-to-VOD assets with AWS Elemental MediaPackage](ltov.md "ltov.md").

## Start and end date and time fields

The start and end date and time information defines the time range for the
harvest job. The maximum duration of the harvest job is 24 hours. Times are
based on the program date time (PDT) from the encoder. To ensure synchronization
between the encoder and the playback device, be sure to include
`EXT-X-PROGRAM-DATE-TIME` tags in the endpoint that you're
harvesting from. For instructions, see [Packager settings fields](endpoints-hls-packager.md "endpoints-hls-packager.md").

###### Note

The live-to-VOD asset timing is accurate up to the segment. This means that if
you indicate a start or end time that falls within a segment, MediaPackage
includes the entire segment in the asset. If you have a 3-second segment and
that start time falls on the third second in the segment, the asset will begin
two seconds earlier, at the start of the segment.

1. For **Date and time format**, choose the format that
   you're using to indicate the start and end times of the live-to-VOD asset.
   - **Local time** - the date and time is formatted
     according to the settings of your current browser session. Local
     time uses a 24-hour clock.
   - **Epoch seconds** - the date and time is formatted
     in seconds since the epoch.
   - **ISO-8601** - the date and time is formatted
     according to the ISO-8601 standard.

2. For **When the live-to-VOD asset begins**, enter when the
   live-to-VOD asset begins. The asset's begin time must be at the same
   time or after the live event started. The start time must also be within
   the startover window on the endpoint. If the endpoint has a window of 5
   hours and the start time is 6 hours ago, the harvest job fails.
3. For **When the live-to-VOD asset ends**, enter when the
   live-to-VOD asset ends. The length of the asset can't exceed the
   startover window on the endpoint. If the endpoint has a window of 5
   hours and your start time is 2019/07/29 07:15:00, the end time can't be
   after 2019/07/29 12:15:00. The end time must also be in the past.

## Destination fields

The destination information defines how MediaPackage saves the live-to-VOD asset
after it has been harvested from the live stream.

1. For **IAM role ARN**, enter the ARN for the IAM role that provides MediaPackage access to read and
   write from your Amazon S3 bucket where the live-to-VOD asset will be stored.
   This is the role that you created in [Allowing AWS Elemental MediaPackage to access other
   AWS services](setting-up-create-trust-rel.md "setting-up-create-trust-rel.md").
2. For **Amazon S3 bucket name**, enter the bucket where you want
   MediaPackage to store the live-to-VOD asset. The Amazon S3 bucket name must be in the same region
   MediaPackage is harvesting from.
3. For **Manifest key**, enter the path within the
   bucket to the live-to-VOD asset, including the file name for the parent
   manifest of the asset. If the directory structure doesn't already exist
   in the bucket, MediaPackage creates it.

###### Important

The manifest key must be unique. When you use the same manifest
key for multiple harvest jobs, the newest playlist for the asset
overwrites existing playlists. The only time you should reuse a
manifest key is when you are harvesting the same content, such as if
there was a problem with a previous harvest of the content.
