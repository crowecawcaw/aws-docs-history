# Step 8: Prevent Undesired

Content and Viewers (Recommended)

Malicious users may try to re-stream undesirable content (e.g., professional sports)
on your platform, or try to embed your platform’s streams on another website without
permission. This kind of streaming can dramatically increase the amount of live-streamed
video that your application is serving as well as the costs associated with it, without
adding value to your business. In addition to providing you with controls to stop active
streams, Amazon IVS provides resources to help detect and prevent this kind of behavior
in the first place; see [Undesired Content and Viewers
in IVS](undesired-content.md "undesired-content.md").

To constrain playback to specific origins and/or countries, use a playback restriction
policy. Note that these policies can be used only with public channels. [Undesired Content and Viewers in IVS](undesired-content.md "undesired-content.md") also
discusses the use of private channels to control undesired content.

Note that playback restriction policies (such as geo-blocking) cannot be used simultaneously
with playback authorization. If playback authorization is enabled for a channel, any configured playback
restriction policies will be ignored. To enforce geo-restrictions on a private channel, validate the
user's location within your token generation logic before issuing a playback token.
