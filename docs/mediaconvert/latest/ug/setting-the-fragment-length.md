# Setting

the fragment length for streaming outputs

For all ABR streaming output groups other than
HLS
(CMAF, DASH, and Microsoft Smooth Streaming), the value that you
specify for **Fragment length** (`FragmentLength`) must
work with the other output settings that you specify. If you set **Fragment
length** incorrectly, when viewers watch the output video, their player
might crash. This can happen because the player expects additional segments at the
end of the video and requests segments that don't exist.

**Fragment length** is constrained by your values for
**Closed GOP cadence** (`GopClosedCadence`),
**GOP size** (`GopSize`), and **Frame
rate** (`FramerateNumerator`,
`FramerateDenominator`). For information about finding these settings
on the console and in your JSON job specification, see [Finding the
settings related to fragment length](#finding-the-settings-related-to-fragment-length "#finding-the-settings-related-to-fragment-length").

###### Note

When you set your output **Frame rate** to **Follow
source**, make sure that the frame rate of your input video file
works with the value that you specify for the output **Fragment
length**. The frame rate of your input video file functions as your
output frame rate.

###### Topics

- [Rule for fragment
  length](#rule-for-fragment-length "#rule-for-fragment-length")
- [Fragment length
  examples](#fragment-length-examples "#fragment-length-examples")
- [Finding the settings related to fragment length](#finding-the-settings-related-to-fragment-length "#finding-the-settings-related-to-fragment-length")

## Rule for fragment length

Fragment length must be a whole number and must be a multiple of this value:
**GOP size** x **Closed GOP cadence** ÷
**Frame rate**

## Fragment

length
examples

###### Example:

Correct settings

Closed GOP cadence = 1

Frame rate = 30

GOP size = 60 frames

Fragment length = 2

###### Example: Incorrect settings

Closed GOP Cadence = 1

Frame rate = 50

GOP size = 90 frames

Fragment length = 2

## Finding the

settings related to fragment length

When you set **Fragment length**, check your values for
**Closed GOP cadence**, **GOP size**, and
**Frame rate**.

### Fragment length

You can set the fragment length using either the console or the JSON job
specification. The **Fragment length** setting applies to
an output group and affects every output in the group.

###### To find the **Fragment length** setting

(console)

1. On the **Create job** page, in the **Job** pane on the left, under
   **Output groups**, choose the name of your CMAF,
   DASH ISO, or Microsoft Smooth Streaming output group.
2. In the group settings section on the right, find
   **Fragment length**.

The group settings section is
titled
**CMAF group settings**, **DASH ISO
group settings**, or **MS Smooth group
settings**.

###### To find the **Fragment length** setting (JSON job

specification)

- Find `FragmentLength` as a child of
  `OutputGroupSettings`, as in the following
  example.

```
{
  "Settings": {
    ...
    "Inputs": [
      ...
    ],
    "OutputGroups": [
      {
        "Name": "DASH ISO",
        "OutputGroupSettings": {
          "Type": "DASH_ISO_GROUP_SETTINGS",
          "DashIsoGroupSettings": {
            "SegmentLength": 30,
            **"FragmentLength": 2,**
            "SegmentControl": "SINGLE_FILE",
            "HbbtvCompliance": "NONE"
          }
        },
		...
```

### Closed GOP

cadence, GOP size, and frame rate

You can set **Closed GOP cadence**, **GOP
size**, and **Frame rate** using either the
console or the JSON job specification. These settings apply to each output
individually. Make sure that the values that you set for each output in the
output group work with the value that you specify for the output group's
**Fragment length**.

###### Note

Your ABR stack has multiple outputs. Make sure to set these values in
each output.

###### To find the encoding settings for an

output
(console)

1. On the **Create job** page, in the **Job** pane on the left, under **Output
   groups**,
   choose the name of your output, such as
   **Output 1**, **Output 2**,
   and so on.
2. In the **Encoding settings** section, the
   **Video** tab is selected automatically. Find
   **Closed GOP cadence**, **GOP
   size**, and **Frame rate** on this
   tab.

###### To find the encoding settings for an output (JSON job

specification)

- Find `GopClosedCadence`, `GopSize`,
  `FramerateNumerator`, and
  `FramerateDenominator` as children of the codec
  settings, as in the following example. In this example, the
  codec is `H_264`, so the parent of the codec settings
  is `H264Settings`.

```
{
  "Settings": {
    ...
    "Inputs": [
      ...
    ],
    "OutputGroups": [
      {
        "Name": "DASH ISO",
        ...
        },
        "Outputs": [
          {
            "VideoDescription": {
              ...
              "CodecSettings": {
                "Codec": "H_264",
                "H264Settings": {
                  "InterlaceMode": "PROGRESSIVE",
                  "NumberReferenceFrames": 3,
                  "Syntax": "DEFAULT",
                  "Softness": 0,
                  **"GopClosedCadence": 1,**
                  **"GopSize": 60,**
				  ...
                  **"FramerateNumerator": 60,**
                  **"FramerateDenominator": 1**
                }
              },
              ...
            },
```
