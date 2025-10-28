# Working with Nielsen watermarking

Nielsen is a company that tracks how often video assets are watched by viewers. One form
of that tracking uses tones in a media asset's audio that are audible to machines but not
humans. These tones are encoded directly in the audio stream and can also be cued in the
metadata. To use this Nielsen
audio
watermarking with MediaConvert, you must first establish a relationship
with Nielsen.

MediaConvert supports Nielsen audio watermarking in these ways:

- _PCM to ID3 watermarking_: With PCM to ID3
  watermarking, MediaConvert translates watermarking that already exists in your
  input audio stream to markers in your output's ID3 metadata.
- _Non-linear watermarking_: With non-linear
  watermarking, MediaConvert inserts integers, called _TICs_, into the PCM audio stream of the asset. At the locations of
  these TICs, MediaConvert also encodes audio tones.

With non-linear watermarking, your input must start without watermarking.
AWS Elemental MediaConvert receives the TICs from a Nielsen SID/TIC server that you set up in
the AWS Cloud.

###### Note

If you want both types of watermarking, you must run your job twice. First create an
output with non-linear watermarking, and then use that output as input to the next job
to add ID3 watermarking from your PCM stream. You can't enable both kinds of
watermarking in a single job.

###### Topics

- [Configuring
  PCM to ID3 metadata](setting-up-pcm-to-id3-metadata.md "setting-up-pcm-to-id3-metadata.md")
- [Configuring Nielsen non-linear watermarking](setting-up-non-linear-watermarking.md "setting-up-non-linear-watermarking.md")
- [Nielsen SID/TIC server requirements in the AWS
  Cloud](how-mediaconvert-interacts-with-your-nielsen-sid-tic-server-in-the-aws-cloud.md "how-mediaconvert-interacts-with-your-nielsen-sid-tic-server-in-the-aws-cloud.md")
