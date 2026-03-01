# Creating and monitoring a feed

You must create a feed and enable at least one AI feature in that feed. After you have
created the feed, you must associate one resource, which represents the media source that
Elemental Inference will work on.

###### Topics

- [Prepare the source media](#prepare-resource "#prepare-resource")
- [Create the feed in Elemental Inference](#create-feed "#create-feed")
- [Deliver the source media](#deliver-source-media "#deliver-source-media")

## Prepare the source media

### Stream requirements

The source that you deliver to Elemental Inference must meet the follow requirements of the
DASH-IF live media ingest protocol
specification, as follows.

- Media fragments: Fragmented CMAF Ingest containerized media fragments.
- Initialization segment: Include an initialization segment with each
  stream, as follows:

For video: Streams(default-video.cmfv)/InitializationSegment

For audio: Streams(default-audio.cmfa)/InitializationSegment

- Futher media segments must following this naming pattern:

`Streams
 default-<`type`>.<`ext`>/Segment(<`sequence-number`>)`

Where:

<type> is video or audio

<ext> is cmfv or cmfa

<sequence-number> must increase monotonically, although it doesn't have
to be contiguous. Each sequence number must match the sequence number in the
MovieFragmentHeader box.

For example:

`Streams
 default-video.cmfv/Segment(<`sequence-number`>)`

- Elemental Inference will ingest all media segments (audio and video) for a given
  sequence number before proceeding to the next sequence number.
- MovieFragmentBox: One per segment.
- Media segment duration: 0-2 seconds.
- Last media segment in the session: A media segment with the
  `lmsg` brand included in the compatible brands under the
  SegmentTypeBox.

If you are using FFMPG, note that currently FFMPG doesn't set the
`lmsg` brand to signal end-of-stream, which means that
`Elemental Inference` will retain the final buffer it
receives. As a workaround, you could send up to 10 seconds of slate, in
order to flush the internal buffer.

- Manifest: Not supported.

### Media requirements for video

- Codec: H.264 or H.265
- Framerate: 30 frames per second
- Resolution: 1280x720

### Media requirements for audio

Codec: AAC

## Create the feed in Elemental Inference

1. Open the Elemental Inference console at [https://console.aws.amazon.com/elemental-inference/](https://console.aws.amazon.com/elemental-inference/ "https://console.aws.amazon.com/elemental-inference/").
2. In the left navigation bar, choose **Feeds**. On the
   **Feeds** page, choose **Create**.
3. Complete the fields:
   - Enter the name for the feed. The name should help you to identify the
     media source that you will send to Elemental Inference.
   - Enter an optional description
   - Enable at least one feature in the **AI features**
     section.
   - Optionally, associate tags with the feed.

4. Choose **Create feed**. The **Feeds** page
   appears showing a list with one line for each feed. After a few moments, the
   status of the feed you just created will be
   **Available**.
5. Make a note of the feed ARN that Elemental Inference generates. This is the unique
   _data endpoint_ for the feed. You need this
   endpoint when you deliver the source media, in the next step.
6. Choose the feed by name. The details about the feed appear.
7. In **Feed association**, enter a friendly name for the
   resource for this feed.

The resource is the source media that Elemental Inference will work on.

Each feed has only one resource. All the AI features that you enable will work
on this single source. 8. In the **Feed association** section, choose
**Save** to confirm the association. The
**Feed** information on the page is updated:

    * In **General details**, the status of the feed
     changes to
     **Active**.
    * In **Outputs**, the status of each output changes to
     **Enabled**.


    If you want to disable an output or change any other information for
     the output, select the **Edit** button (a pencil) on
     the right.

## Deliver the source media

You must format the source media using an encoding application of your choice. You
must then use PUTMEDIA on the Elemental Inference feed endpoint to deliver the source media to the
data endpoint on the Elemental Inference feed. You can then use the GETMETADATA on the Elemental Inference feed
endpoint to obtain the metadata that Elemental Inference generates.

### Format the media

The following code shows how to use FFMPG to format the media to follow the
requirements in [Prepare the source media](#prepare-resource "#prepare-resource"). The commands demux, segment, and containerizes the video and
audio.

```
$ mkdir 'Streams(default-video.cmfv)'
$ ffmpeg -i input.mp4 \
-map 0:v:0 -c:v libx264 \
    -profile:v main -pix_fmt yuv420p \
    -g 30 -keyint_min 30 -sc_threshold 0 \
    -force_key_frames 'expr:gte(t,n_forced*1)' \
    -f dash -seg_duration 1 -use_timeline 0 \
    -use_template 1 -remove_at_exit 0  \
    -init_seg_name 'Streams(default-video.cmfv)/InitializationSegment' \
    -media_seg_name 'Streams(default-video.cmfv)/Segment($Number%09d$)' \
    'video.mpd'

$ mkdir 'Streams(default-audio.cmfa)'$ ffmpeg -i input.mp4 \
    -map 0:a:0 -c:a aac -ar 48000 -ac 2 \
    -f dash -seg_duration 1 -use_timeline 0 \
    -use_template 1 -remove_at_exit 0 \
    -init_seg_name 'Streams(default-audio.cmfa)/InitializationSegment' \
    -media_seg_name 'Streams(default-audio.cmfa)/Segment($Number%09d$)' \
    'audio.mpd'
```

### Deliver the content

The following code shows how to use CURL to use the PUT command to send the
content to the data endpoint of a feed.

You can obtain the data endpoint of a feed by using one of the Elemental Inference APIs or
SDKs. For example, use the CreateEndpoint or GetEndpoint operations of the REST API.
The endpoint is returned in the response.

Make signed requests to the data endpoint of the Elemental Inference feed. This example assumes
that you have exported credentials as environment variables.

```
# Initialization
$ awscurl --region <`region`> --service elemental-inference -X PUT \
  'https://<`data-endpoint`>/v1/feed/<`feed-id`>/input/0/media/Streams(default-audio.cmfa)/InitializationSegment' \
  --data-binary -d '@Streams(default-audio.cmfa)/InitializationSegment'

$ awscurl --region <`region`> --service elemental-inference -X PUT \
  'https://<data-endpoint>/v1/feed/<`feed-id`>/input/0/media/Streams(default-video.cmfv)/InitializationSegment' \
  --data-binary -d '@Streams(default-video.cmfv)/InitializationSegment'

# Media
$ awscurl --region <`region`> --service elemental-inference -X PUT \
 'https://<`data-endpoint`>/v1/feed/<`feed-id`>/input/0/media/Streams(default-audio.cmfa)/Segment(<`sequence`>)' \
 --data-binary -d '@Streams(default-audio.cmfa)/Segment(<`sequence`>)'

$ awscurl --region <`region`> --service elemental-inference -X PUT \
  'https://<`data-endpoint`>/v1/feed/<`feed-id`>/input/0/media/Streams(default-video.cmfv)/Segment(<`sequence`>)' \
  --data-binary -d '@Streams(default-video.cmfv)/Segment(<`sequence`>)'

```

### Query the output media

This following CURL code shows how use to the POST command to query the first
second of metadata that is generated by Elemental Inference. After the first frame, the PTS
increments by 42 in each metadata
returned.

This example shows the metadata returned for the smart crop feature.
See below for
more information about the metadata for a smart crop.

```
# Query the first second of metadata
$ awscurl --service "elemental-inference" --region <`region`> \
  -X POST 'https://<`data-endpoint`>/v1/feed/<`feed-id`>/input/0/metadata' \
  -H "Content-Type: application/json" \
  -d '{"outputName": "testOutput", "timeSpecification": { "ptsBased": { "startPts":0, "endPts": 1001, "timescale": 1000 } }, "parameters": {"smartCropping": {"frameRate": { "numerator": 24, "denominator": 1}}}}'
{
    "items": [
        {
            "metadata": {
                "smartCropping": {
                    "crop": {
                        "centerPoint": {
                            "scale": 10000,
                            "xPosition": 2176,
                            "yPosition": 6250
                        }
                    }
                }
            },
            "pts": 0,
            "timecode": null
        },
        {
            "metadata": {
                "smartCropping": {
                    "crop": {
                        "centerPoint": {
                            "scale": 10000,
                            "xPosition": 2176,
                            "yPosition": 6250
                        }
                    }
                }
            },
            "pts": 41,
            "timecode": null
        },
        },
        {
            "metadata": {
                "smartCropping": {
                    "crop": {
                        "centerPoint": {
                            "scale": 10000,
                            "xPosition": 2208,
                            "yPosition": 6238
                        }
                    }
                }
            },
            "pts": 83,
            "timecode": null
        },
.
.
.
        {
            "metadata": {
                "smartCropping": {
                    "crop": {
                        "centerPoint": {
                            "scale": 10000,
                            "xPosition": 2873,
                            "yPosition": 5781
                        }
                    }
                }
            },
            "pts": 1000,
            "timecode": null
        }
    ]
}

```

#### Metadata for a smart crop

For each frame, Elemental Inference creates metadata that identifies a point in that region
of interest. This is the point of interest. You can develop a solution that
crops and scales the video. The point of interest provides you with a reference
point for the cropping and scaling algorithms that you develop.

The point of interest is an x,y coordinate.

- The y coordinate is always the halfway point (the 50% mark) on the y
  axis. It is not the true y position of the point of interest.
- The x coordinate is the true position (as a percentage) on the x axis.
