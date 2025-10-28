# Disabling Neptune Streams

You can turn Neptune Streams off any time that it is running.

To turn Streams off, update the DB Cluster parameter group so that the value of
the `neptune_streams` parameter is set to 0.

###### Important

As soon as Streams is turned off, you can't access the change-log
data any more. Be sure to read what you are interested in _before_
turning Streams off.
