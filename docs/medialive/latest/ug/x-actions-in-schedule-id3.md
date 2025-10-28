# How ID3 metadata actions work

You can set up an action to insert ID3 data in the channel.
You can set up
an action to insert ID3 data in each segment in the following types of
outputs:

- CMAF Ingest
- HLS
- MediaPackage
  Before you add ID3 metadata actions to the schedule, read [Inserting ID3 metadata using the
  schedule](insert-id3-metadata-via-schedule.md "insert-id3-metadata-via-schedule.md").

**Insert ID3 metadata with fixed start**

When you create the action, you include a start time. The start time for the
action must be at least 15 seconds in the future but not more than 14 days in the
future. After that cutoff, MediaLive rejects the request to create the action.

After you have created the action, the action sits in the schedule. Approximately
15 seconds before the start time, the schedule passes the action to the channel. At
the start time, the channel inserts the data into the channel.

**Insert ID3 metadata with immediate start**

When you create the action, you set the start type to _immediate_.

The schedule immediately passes the action to the channel. The channel immediately
inserts the data into the channel.
