# How MediaLive performs channel maintenance

At some point during the maintenance window (red mark), MediaLive starts the maintenance.
There is no notification that maintenance is about to start on the channel.

There is no need to monitor the channel or to prepare for maintenance during the time
leading up to the maintenance window.

MediaLive performs maintenance as follows:

- If a channel is set up as a standard channel (with two pipelines), MediaLive always
  performs maintenance on one pipeline at a time. MediaLive stops one pipeline, performs the
  maintenance, and automatically restarts the pipeline. It then stops the second pipeline,
  performs the maintenance, and automatically restarts the second pipeline. In this way,
  there is typically no impact on the output from the channel.
- If a channel is set up as a single-line channel, MediaLive stops the pipeline, which stops
  the channel. MediaLive performs the maintenance and restarts the channel. There will be no
  output from the channel while maintenance is being performed.

###### Note

Setting up with standard channels is an effective way to mitigate the impact of
maintenance events. You might want to consider this mitigation for your most important 24x7
channels.

![Timeline showing a long bar spanning multiple days and shorter bars on specific dates.](images/maintenance.png)
