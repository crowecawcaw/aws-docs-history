# Ensure correct setup on the upstream

system

You must make sure that the upstream system pushes content to the correct
locations in MediaLive.

###### To set up for a standard channel

Follow this procedure if the MediaLive channel is a [standard channel](plan-redundancy.md "plan-redundancy.md").

1.  Provide the operator with this information:
    - The two endpoints (URLs) that MediaLive generated when you created the
      RTP input. These endpoints are the addresses in the blue boxes in
      [the diagram after this
      procedure](setup-result-rtp-push.md "setup-result-rtp-push.md"). The URLs include port 5000. For example:

    `198.51.100.99:5000`

    `192.0.2.18:5000`

2.  Make sure that the operator sets up properly for a standard channel. They
    must:
    - Deliver two sources that are identical in terms of video
      resolution and bitrate.
    - Make sure that the sources appear on the agreed IP addresses on
      the public network. For example:

          + For one source: `203.0.113.19, 203.0.113.58,
           203.0.113.25`
          + For the other source: `198.51.100.19, 198.51.100.59,
           198.51.100.21`

      You used these addresses when you created the input security
      group. If the upstream system doesn't use these addresses, MediaLive
      will refuse the push.

    - Push to the correct URLs on MediaLive. For example, they must push
      to:

    `198.51.100.99:5000`

    `192.0.2.18:5000`
    - Send over RTP, not UDP. The UDP protocol is not supported for an
      input into MediaLive.

###### To set up for a single-pipeline channel

Follow this procedure if the MediaLive channel is a [single-pipeline channel](plan-redundancy.md "plan-redundancy.md").

1. Provide the operator with this information:
   - Only the first of the two endpoints (URLs) that MediaLive generated
     when you created the RTP input. This endpoint is one of the
     addresses in the blue boxes in [the diagram after this procedure](setup-result-rtp-push.md "setup-result-rtp-push.md"). The URL includes port
   5000. For example:

   `198.51.100.99:5000`

2. Make sure that the operator sets up properly for a single-pipeline
   channel. They must:
   - Make sure that the source appears on the agreed IP addresses on
     the public network. For example:

   `203.0.113.19, 203.0.113.58, 203.0.113.25`

   You used these addresses when you created the input security
   group. If the upstream system doesn't use these addresses, MediaLive
   will refuse the push.
   - Push to the correct URL on MediaLive. For example, they must push
     to:

   `198.51.100.99:5000`
   - Send over RTP, not UDP. The UDP protocol is not supported for an
     input into MediaLive.
