# Ingesting Dolby E input audio

You can set up AWS Elemental MediaLive to ingest Dolby E audio. The Dolby E audio
must be wrapped in a PCM streams tagged with SMPTE-337. The options for
handling this audio source are the following:

- Extract individual programs from the source audio, and then
  convert it or remix it in the output.
- Pass them through all the programs, with no conversion and no
  remixing.
- Set up the source for both types of handling—to extract
  programs and to pass through the entire source.

###### Topics

- [About Dolby E](#dolby-E-input-about "#dolby-E-input-about")
- [Getting ready](#dolby-E-input-get-ready "#dolby-E-input-get-ready")
- [Setting up the input to
  extract programs](#dolby-atmos-output-setup-extract "#dolby-atmos-output-setup-extract")
- [Setting up the
  input to pass through the audio](#dolby-atmos-output-setup-passthru "#dolby-atmos-output-setup-passthru")
- [Setting up
  the input to extract and pass through](#dolby-atmos-output-setup-combination "#dolby-atmos-output-setup-combination")

## About Dolby E

Dolby E wrapped in PCM can carry up to eight _Dolby E programs_ delivered in two
_audio tracks_. The two audio
tracks are a standard stereo pair (in other words, 2.0 coding
mode).

The two tracks contain the number of Dolby E programs required for
the coding mode of the audio. For example, if the audio is 7.1
audio, then all the Dolby E programs contains content. If the audio
is four stereo languages, then all the Dolby E programs contain
content. But if the audio is only three stereo languages, then only
six of the Dolby E programs contain content.

The supported coding modes for Dolby E audio are AD, 1.0 (mono),
1.1, 2.0 (stereo), 3.2, 4.0, 5.1, and 7.1. All these coding modes
are supported by MediaLive on the input side.

For information about the input types that support Dolby E, see
[Input codecs in MediaLive](inputs-supported-codecs.md "inputs-supported-codecs.md").

## Getting ready

Contact the content provider for this input to find out about the
programs that are included in the Dolby E audio. For example, it
might contain 7.1 audio in English. Or it might contain four sets of
stereo (English, French, Spanish, Punjabi) with English in Dolby E
programs 1 and 2, and so on, through to Punjabi in Dolby E programs
7 and 8.

## Setting up the input to

extract programs

You must identify each Dolby E program that you want to extract
and map it to a _MediaLive audio
selector_. Each MediaLive audio selector maps to one Dolby
E program.

###### Note

The information in this section assumes that you are familiar
with the general steps for creating a channel.

1. In the channel in MediaLive, select the **Input
   attachment** that contains the Dolby E audio
   that you want to decode or pass through.
2. In the **General input
   settings** section choose **Add audio selectors**. Fields for one audio
   selector (**Audio Selectors
   1**) appear.
3. Complete the fields as follows.

| Field                            | Description                                                                                                                                                      |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Audio selector<br>name**       | Assign a name to the Dolby E program. For<br>example, `DolbyE<br>program1`.                                                                                      |
| **Selector<br>settings**         | From the drop-down menu, choose<br>**Audio track<br>selection**.                                                                                                 |
| **Dolby E<br>decode**            | Choose **Audio Dolby E<br>decode**. The \*_Dolby E<br>program selection_<br>• field<br>appears. The drop-down menu shows the eight<br>possible Dolby E programs. |
| **Dolby E program<br>selection** | Select the Dolby E program that you want<br>to extract. For example,<br>**PROGRAM_1**.                                                                           |

Don't select the Add tracks field. This field doesn't
apply to Dolby E audio. 4. To extract more Dolby E programs, choose **Add audio selectors** as many times
as you need. Follow the steps above for each Dolby E program
that you want to extract.

When you have finished, there will be one audio selector for each
program to extract.

## Setting up the

input to pass through the audio

You can pass through the entire Dolby E audio source so that you
can then pass it through in the output.

###### Note

The information in this section assumes that you are familiar
with the general steps for creating a channel.

1. In the channel in MediaLive, select the **Input
   attachment** that contains the Dolby E audio
   that you want to decode or pass through.
2. In the **General input settings** section
   choose **Add audio selectors**. Fields for
   one audio selector (**Audio Selectors 1**)
   appear.
3. Complete the fields as follows.

| Field                            | Description                                                                                                                                                      |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Audio selector<br>name**       | Assign a name to the Dolby E program. For<br>example, `DolbyE<br>passthrough`.                                                                                   |
| **Selector<br>settings**         | From the drop-down menu, choose<br>**Audio track<br>selection**.                                                                                                 |
| **Dolby E<br>decode**            | Choose **Audio Dolby E<br>decode**. The \*_Dolby E<br>program selection_<br>• field<br>appears. The drop-down menu shows the eight<br>possible Dolby E programs. |
| **Dolby E program<br>selection** | Select the Dolby E program that you want<br>to extract. For example,<br>**ALL_CHANNELS**.                                                                        |

## Setting up

the input to extract and pass through

You can set up the source in both ways—to extract programs and to
pass through the entire source.

In the same input attachment, set up one selector for passthrough,
and set up several selectors to extract programs.
