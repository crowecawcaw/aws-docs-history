# Result of this procedure

The results of this setup are illustrated in the diagram that follows. There are three
main components:

- The upstream system (purple box)
- One or two MediaConnect flows (red boxes).
- One MediaConnect input in MediaLive.
  Each MediaConnect flows has a source that the upstream system is pushing to. Each flow also
  has one output for the use of MediaLive.

The MediaConnect input in MediaLive specifies the ARNs for those outputs.

The upstream system pushes the source content to the source on the AWS Elemental MediaConnect flow or
flows. The flows push the content to MediaLive. Keep in mind that with a push input, the
upstream system must be pushing the video source to the input when you start the
channel. The upstream system does not need to be pushing before then.

At runtime of the channel, MediaLive reacts to the content that is being pushed and
ingests it.

![Diagram showing two flows from upstream system to MediaConnect input in MediaLive.](/images/medialive/latest/ug/images\emx-push-uss-input.png)
