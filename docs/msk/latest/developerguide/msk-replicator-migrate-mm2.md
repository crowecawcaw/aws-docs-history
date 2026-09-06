

# Migrate from MirrorMaker 2 to Amazon MSK Replicator
<a name="msk-replicator-migrate-mm2"></a>

To migrate from MirrorMaker (MM2) to MSK Replicator, follow these steps:

1. Stop the producer that is writing to your source Amazon MSK cluster.

1. Allow MM2 to replicate all the messages on your source cluster's topics. You can monitor the consumer lag for the MM2 consumer on your source MSK cluster to determine when all data has been replicated.

1. Create a new Replicator with starting position set to *Latest* and topic name configuration set to `IDENTICAL` (**Keep the same topics name** in console).

1. Once your Replicator is in the RUNNING state, you can start the producers writing to the source cluster again.