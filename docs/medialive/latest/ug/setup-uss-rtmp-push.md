# Ensure correct setup on the upstream

system

You must make sure that the upstream system pushes content to the correct
locations in MediaLive.

###### To set up for a standard channel

Follow this procedure if the MediaLive channel is a [standard channel](plan-redundancy.md "plan-redundancy.md").

1. Provide the operator with this information:
   - The two endpoints (URLs) that MediaLive generated when you created the
     RTMP input. These endpoints are the addresses in the blue boxes in
     [the diagram after this
     procedure](setup-result-rtmp-push.md "setup-result-rtmp-push.md"). The URLs include port 1935. For example:

   `198.51.100.99:1935/live/curling`

   `192.0.2.18:1935/live/curling`

2. Make sure that the operator sets up properly for a single-pipeline channel
   or a standard channel.

If your channel is a single-pipeline channel, the operator delivers only
one source, even though the input is a standard (dual-pipeline) input. The
operator must do the following:

    * Deliver one source.
    * Make sure that the sources appear on the agreed IP addresses on
     the public network. For example:




    	+ The sources could appear on these addresses:
    	 `203.0.113.19, 203.0.113.58, 203.0.113.25`
    	+ The operator can ignore the other addresses:
    	 `198.51.100.19, 198.51.100.59, 198.51.100.21`
    You used these addresses when you created the input security
     group. If the upstream system doesn't use these addresses, MediaLive
     will refuse the push.
    * Push to one URL on MediaLive, and use the agreed application name and
     instance name. For example:


    Push to this URL:
     `198.51.100.99:1935/live/curling`


    Ignore the other URL:
     `192.0.2.18:1935/live/curling`

If your channel is a standard channel, the operator must do the
following:

    * Deliver two sources that are identical in terms of video
     resolution and bitrate.
    * Make sure that the sources appear on the agreed IP addresses on
     the public network. For example:




    	+ For one source: `203.0.113.19, 203.0.113.58,
    	 203.0.113.25`
    	+ For the other source: `198.51.100.19, 198.51.100.59,
    	 198.51.100.21`
    You used these addresses when you created the input security
     group. If the upstream system doesn't use these addresses, MediaLive
     will refuse the push.
    * Push to the correct URLs on MediaLive, and use the agreed application
     name and instance name. For example, they must push to:


    `198.51.100.99:1935/live/curling`


    `192.0.2.18:1935/live/curling`
