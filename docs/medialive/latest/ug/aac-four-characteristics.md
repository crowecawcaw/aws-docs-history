

# Supported sampling rate and bitrate for AAC output
<a name="aac-four-characteristics"></a>

This section explains how to set the following four properties of the AAC audio codec when you are setting up an audio encode in MediaLive:
+ Profile
+ Coding mode
+ Sample rate
+ Bitrate

In the console, these properties are in four fields in the **Codec configuration** section for the AAC codec. To get here, go to the **Create channel** page and choose the appropriate output in the output group. In **Output settings**, go to the **Audio** section. In Codec settings, choose Aac, then expand **Codec configuration**. To review the step where you complete these fields, see [Set up the audio encodes](creating-a-channel-step7.md). 

**Note**  
You can set all four fields. Or you can leave all the fields with their defaults.  
If you change only one or two fields, you might create a combination that is not valid. See the tables in the following sections to verify that the combination you have created is valid.

**To set these four fields**

1. Choose a **Coding mode**.

1. Choose a **Profile** that is valid with that profile. See the tables that follow this procedure.

1. Choose a **Sample rate** that is valid for that combination of profile and coding mode.

1. Choose a **Bitrate** that falls within the range that is supported for that sample rate.

## Coding mode 1.0
<a name="aac_mode_10_combinations"></a>

In this table, read down the rows to find the profile that you want. Then read across to find a valid combination of sample rate and bitrate. 



- **HEv1**
  - **Sample rate (Hz):** 22050 / **Minimum valid bitrate (bits/sec):** 8000 / **Maximum valid bitrate (bits/sec):** 12000
  - **Sample rate (Hz):** 24000 / **Minimum valid bitrate (bits/sec):** 8000 / **Maximum valid bitrate (bits/sec):** 12000
  - **Sample rate (Hz):** 32000 / **Minimum valid bitrate (bits/sec):** 12000 / **Maximum valid bitrate (bits/sec):** 64000
  - **Sample rate (Hz):** 44100 / **Minimum valid bitrate (bits/sec):** 18000 / **Maximum valid bitrate (bits/sec):** 64000
  - **Sample rate (Hz):** 48000 / **Minimum valid bitrate (bits/sec):** 18000 / **Maximum valid bitrate (bits/sec):** 64000

- **LC**
  - **Sample rate (Hz):** 8000 / **Minimum valid bitrate (bits/sec):** 8000 / **Maximum valid bitrate (bits/sec):** 14000
  - **Sample rate (Hz):** 12000 / **Minimum valid bitrate (bits/sec):** 8000 / **Maximum valid bitrate (bits/sec):** 14000
  - **Sample rate (Hz):** 16000 / **Minimum valid bitrate (bits/sec):** 8000 / **Maximum valid bitrate (bits/sec):** 28000
  - **Sample rate (Hz):** 22050 / **Minimum valid bitrate (bits/sec):** 24000 / **Maximum valid bitrate (bits/sec):** 28000
  - **Sample rate (Hz):** 24000 / **Minimum valid bitrate (bits/sec):** 24000 / **Maximum valid bitrate (bits/sec):** 28000
  - **Sample rate (Hz):** 32000 / **Minimum valid bitrate (bits/sec):** 32000 / **Maximum valid bitrate (bits/sec):** 192000
  - **Sample rate (Hz):** 44100 / **Minimum valid bitrate (bits/sec):** 56000 / **Maximum valid bitrate (bits/sec):** 256000
  - **Sample rate (Hz):** 48000 / **Minimum valid bitrate (bits/sec):** 56000 / **Maximum valid bitrate (bits/sec):** 288000
  - **Sample rate (Hz):** 88200 / **Minimum valid bitrate (bits/sec):** 288000 / **Maximum valid bitrate (bits/sec):** 288000
  - **Sample rate (Hz):** 96000 / **Minimum valid bitrate (bits/sec):** 128000 / **Maximum valid bitrate (bits/sec):** 288000



## Coding mode 1\+1
<a name="aac_mode_11_combinations"></a>

In this table, read down the rows to find the profile that you want. Then read across to find a valid combination of sample rate and bitrate. 



- **HEv1**
  - **Sample rate (Hz):** 32000 / **Minimum valid bitrate (bits/sec):** 24000 / **Maximum valid bitrate (bits/sec):** 128000
  - **Sample rate (Hz):** 44100 / **Minimum valid bitrate (bits/sec):** 40000 / **Maximum valid bitrate (bits/sec):** 192000
  - **Sample rate (Hz):** 48000 / **Minimum valid bitrate (bits/sec):** 40000 / **Maximum valid bitrate (bits/sec):** 192000
  - **Sample rate (Hz):** 96000 / **Minimum valid bitrate (bits/sec):** 224000 / **Maximum valid bitrate (bits/sec):** 256000

- **LC**
  - **Sample rate (Hz):** 8000 / **Minimum valid bitrate (bits/sec):** 16000 / **Maximum valid bitrate (bits/sec):** 28000
  - **Sample rate (Hz):** 12000 / **Minimum valid bitrate (bits/sec):** 16000 / **Maximum valid bitrate (bits/sec):** 28000
  - **Sample rate (Hz):** 16000 / **Minimum valid bitrate (bits/sec):** 16000 / **Maximum valid bitrate (bits/sec):** 56000
  - **Sample rate (Hz):** 22050 / **Minimum valid bitrate (bits/sec):** 48000 / **Maximum valid bitrate (bits/sec):** 56000
  - **Sample rate (Hz):** 24000 / **Minimum valid bitrate (bits/sec):** 48000 / **Maximum valid bitrate (bits/sec):** 56000
  - **Sample rate (Hz):** 32000 / **Minimum valid bitrate (bits/sec):** 64000 / **Maximum valid bitrate (bits/sec):** 384000
  - **Sample rate (Hz):** 44100 / **Minimum valid bitrate (bits/sec):** 112000 / **Maximum valid bitrate (bits/sec):** 512000
  - **Sample rate (Hz):** 48000 / **Minimum valid bitrate (bits/sec):** 112000 / **Maximum valid bitrate (bits/sec):** 576000
  - **Sample rate (Hz):** 88200 / **Minimum valid bitrate (bits/sec):** 256000 / **Maximum valid bitrate (bits/sec):** 576000
  - **Sample rate (Hz):** 96000 / **Minimum valid bitrate (bits/sec):** 256000 / **Maximum valid bitrate (bits/sec):** 576000



## Coding mode 2.0
<a name="aac_mode_20_combinations"></a>

In this table, read down the rows to find the profile that you want. Then read across to find a valid combination of sample rate and bitrate. 



- **HEv1**
  - **Sample rate (Hz):** 32000 / **Minimum valid bitrate (bits/sec):** 16000 / **Maximum valid bitrate (bits/sec):** 128000
  - **Sample rate (Hz):** 44100 / **Minimum valid bitrate (bits/sec):** 16000 / **Maximum valid bitrate (bits/sec):** 96000
  - **Sample rate (Hz):** 48000 / **Minimum valid bitrate (bits/sec):** 16000 / **Maximum valid bitrate (bits/sec):** 128000
  - **Sample rate (Hz):** 96000 / **Minimum valid bitrate (bits/sec):** 96000 / **Maximum valid bitrate (bits/sec):** 128000

- **HEv2**
  - **Sample rate (Hz):** 22050 / **Minimum valid bitrate (bits/sec):** 8000 / **Maximum valid bitrate (bits/sec):** 12000
  - **Sample rate (Hz):** 24000 / **Minimum valid bitrate (bits/sec):** 8000 / **Maximum valid bitrate (bits/sec):** 12000
  - **Sample rate (Hz):** 32000 / **Minimum valid bitrate (bits/sec):** 12000 / **Maximum valid bitrate (bits/sec):** 64000
  - **Sample rate (Hz):** 44100 / **Minimum valid bitrate (bits/sec):** 20000 / **Maximum valid bitrate (bits/sec):** 64000
  - **Sample rate (Hz):** 48000 / **Minimum valid bitrate (bits/sec):** 20000 / **Maximum valid bitrate (bits/sec):** 64000

- **LC**
  - **Sample rate (Hz):** 8000 / **Minimum valid bitrate (bits/sec):** 16000 / **Maximum valid bitrate (bits/sec):** 20000
  - **Sample rate (Hz):** 12000 / **Minimum valid bitrate (bits/sec):** 16000 / **Maximum valid bitrate (bits/sec):** 20000
  - **Sample rate (Hz):** 16000 / **Minimum valid bitrate (bits/sec):** 16000 / **Maximum valid bitrate (bits/sec):** 32000
  - **Sample rate (Hz):** 22050 / **Minimum valid bitrate (bits/sec):** 32000 / **Maximum valid bitrate (bits/sec):** 32000
  - **Sample rate (Hz):** 24000 / **Minimum valid bitrate (bits/sec):** 32000 / **Maximum valid bitrate (bits/sec):** 32000
  - **Sample rate (Hz):** 32000 / **Minimum valid bitrate (bits/sec):** 40000 / **Maximum valid bitrate (bits/sec):** 384000
  - **Sample rate (Hz):** 44100 / **Minimum valid bitrate (bits/sec):** 96000 / **Maximum valid bitrate (bits/sec):** 512000
  - **Sample rate (Hz):** 48000 / **Minimum valid bitrate (bits/sec):** 64000 / **Maximum valid bitrate (bits/sec):** 576000
  - **Sample rate (Hz):** 88200 / **Minimum valid bitrate (bits/sec):** 576000 / **Maximum valid bitrate (bits/sec):** 576000
  - **Sample rate (Hz):** 96000 / **Minimum valid bitrate (bits/sec):** 256000 / **Maximum valid bitrate (bits/sec):** 576000



## Coding mode 5.1
<a name="aac_mode_51_combinations"></a>

In this table, read down the rows to find the profile that you want. Then read across to find a valid combination of sample rate and bitrate. 



- **HEv1**
  - **Sample rate (Hz):** 32000 / **Minimum valid bitrate (bits/sec):** 64000 / **Maximum valid bitrate (bits/sec):** 320000
  - **Sample rate (Hz):** 44100 / **Minimum valid bitrate (bits/sec):** 64000 / **Maximum valid bitrate (bits/sec):** 224000
  - **Sample rate (Hz):** 48000 / **Minimum valid bitrate (bits/sec):** 64000 / **Maximum valid bitrate (bits/sec):** 320000
  - **Sample rate (Hz):** 96000 / **Minimum valid bitrate (bits/sec):** 240000 / **Maximum valid bitrate (bits/sec):** 320000

- **LC**
  - **Sample rate (Hz):** 32000 / **Minimum valid bitrate (bits/sec):** 160000 / **Maximum valid bitrate (bits/sec):** 768000
  - **Sample rate (Hz):** 44100 / **Minimum valid bitrate (bits/sec):** 256000 / **Maximum valid bitrate (bits/sec):** 640000
  - **Sample rate (Hz):** 48000 / **Minimum valid bitrate (bits/sec):** 256000 / **Maximum valid bitrate (bits/sec):** 768000
  - **Sample rate (Hz):** 96000 / **Minimum valid bitrate (bits/sec):** 640000 / **Maximum valid bitrate (bits/sec):** 768000



## Coding mode ad receiver mix
<a name="aac_mode_ad_receiver_mix_combinations"></a>

Choose this coding mode if you have an AD (audio description) audio track that you want to include in the output.

In this table, read down the rows to find the profile that you want. Then read across to find a valid combination of sample rate and bitrate. 



- **HEv1**
  - **Sample rate (Hz):** 22050
  - **Minimum valid bitrate (bits/sec):** 8000
  - **Maximum valid bitrate (bits/sec):** 12000

- **HEv1**
  - **Sample rate (Hz):** 24000 / **Minimum valid bitrate (bits/sec):** 8000 / **Maximum valid bitrate (bits/sec):** 12000
  - **Sample rate (Hz):** 32000 / **Minimum valid bitrate (bits/sec):** 12000 / **Maximum valid bitrate (bits/sec):** 64000
  - **Sample rate (Hz):** 44100 / **Minimum valid bitrate (bits/sec):** 20000 / **Maximum valid bitrate (bits/sec):** 64000
  - **Sample rate (Hz):** 48000 / **Minimum valid bitrate (bits/sec):** 20000 / **Maximum valid bitrate (bits/sec):** 64000

- **LC**
  - **Sample rate (Hz):** 8000 / **Minimum valid bitrate (bits/sec):** 8000 / **Maximum valid bitrate (bits/sec):** 14000
  - **Sample rate (Hz):** 12000 / **Minimum valid bitrate (bits/sec):** 8000 / **Maximum valid bitrate (bits/sec):** 14000
  - **Sample rate (Hz):** 16000 / **Minimum valid bitrate (bits/sec):** 8000 / **Maximum valid bitrate (bits/sec):** 28000
  - **Sample rate (Hz):** 22050 / **Minimum valid bitrate (bits/sec):** 24000 / **Maximum valid bitrate (bits/sec):** 28000
  - **Sample rate (Hz):** 24000 / **Minimum valid bitrate (bits/sec):** 24000 / **Maximum valid bitrate (bits/sec):** 28000
  - **Sample rate (Hz):** 32000 / **Minimum valid bitrate (bits/sec):** 32000 / **Maximum valid bitrate (bits/sec):** 192000
  - **Sample rate (Hz):** 44100 / **Minimum valid bitrate (bits/sec):** 56000 / **Maximum valid bitrate (bits/sec):** 256000
  - **Sample rate (Hz):** 48000 / **Minimum valid bitrate (bits/sec):** 56000 / **Maximum valid bitrate (bits/sec):** 288000
  - **Sample rate (Hz):** 88200 / **Minimum valid bitrate (bits/sec):** 288000 / **Maximum valid bitrate (bits/sec):** 288000
  - **Sample rate (Hz):** 96000 / **Minimum valid bitrate (bits/sec):** 128000 / **Maximum valid bitrate (bits/sec):** 288000

