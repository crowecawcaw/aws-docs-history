# Create the SRT caller output

group

After you have designed the contents of the output and you have coordinated delivery
of the output with the downstream system, you can create the SRT caller output
group.

1. On the **Create channel** page, under **Output
   groups**, choose **Add**.
2. In the **Add output group** section, choose
   **SRT**, and then choose **Confirm**. More
   sections appear.

The form for this output group is broken down into the following
sections:

    * **SRT settings**: Features that apply at the output
     group level, not in individual outputs.
    * **SRT outputs**: Outputs in the output group.
    * **Output > Destinations**: The URL and encryption
     fields for each output.
    * **Output > Output settings**: Networking and
     transport stream settings, and configure individual PIDs.
    * **Output > Stream settings**: Configuration of the
     video, audio, and captions in each output.

For information about each section, see the topics listed after this
procedure. 3. After you have finished setting up this output group and its outputs, you can
create another output group (of any type), if your plan requires it. Otherwise,
go to [Save the channel](creating-a-channel-step9.md "creating-a-channel-step9.md")

## SRT settings

In the **SRT settings** sections, complete the fields:

- **Name**: Enter a name for the output group. This name is
  internal to MediaLive; it doesn't appear in the output. For example,
  `Sports Game`.
- **Input loss action**: Choose a value. For details,
  choose the **Info** link. For detailed information about
  input loss handling for all output groups in the channel, see [Handling loss of video input](feature-input-loss.md "feature-input-loss.md").

## SRT outputs

The **SRT outputs** section shows the single output that is added
by default.
Choose
**Add
output**
if you want to send the content to more
destinations.

In each output, choose the **Settings** link to show
three subsections:

- Destinations. See [Output > Destinations](#srt-caller-destinations "#srt-caller-destinations").
- Output settings. See [Output > Output settings](#srt-caller-output-settings "#srt-caller-output-settings")
- Stream settings: See [Output > Stream settings](#srt-caller-streams "#srt-caller-streams") .

## Output > Destinations

In each output, you must specify one destination (for a single-pipeline channel)
or two destinations (for a standard channel). You must also configure encryption for
each destination.

- Enter the destination URL or URLs, including the port number. You obtained
  this information when you [discussed
  your requirements](downstream-system-srt.md "downstream-system-srt.md") with the downstream system. For example:

`srt://203.0.113.22:5000`

`srt://203.0.113.88:5001`

- Stream ID:
  Optional.
- In each destination, select the
  secret
  that [you obtained from the
  operator of Secrets Manager](srt-output-encryption-asm.md "srt-output-encryption-asm.md").
  You can
  select the secret by its ARN or its name.

## Output > Output settings

Enter a user-friendly name for the output, or leave the default. This name is
internal to MediaLive and doesn't appear in the output.

The remainder of this section contains fields that let you configure the
following:

- Network behavior.
- Characteristics of the transport stream (in the
  **Container** section).
- PID values (in the **PID Settings** section).

These fields cover the SI/PSI and other data. For each of the SI/PSI PIDs,
you can specify a custom value or you can let MediaLive use the default value.

For other data, complete the fields as appropriate. With some of these
fields, the behavior is different for fields that you leave empty. MediaLive
might omit the data from the transport stream. Or MediaLive might use default
values.

Change any values as appropriate. For details about a field, choose the
**Info** link next to the field in the MediaLive console.

## Output > Stream settings

The fields in this section relate to the encoding of the video, audio, and
captions streams (encodes) in the output.

For information about creating encodes, see the following sections:

- [Set up the video encode](creating-a-channel-step6.md "creating-a-channel-step6.md")
- [Set up the audio encodes](creating-a-channel-step7.md "creating-a-channel-step7.md")
- [Set up the captions encodes](creating-a-channel-step8.md "creating-a-channel-step8.md")
