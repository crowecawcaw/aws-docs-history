# Migrate from self-managed MirrorMaker2 to MSK Replicator

To migrate from MirrorMaker (MM2) to MSK Replicator, follow these steps:

1. Stop the producer that is writing to your source Amazon MSK cluster.
2. Allow MM2 to replicate all the messages on your source clusters’ topics. You can monitor the consumer lag for MM2 consumer on your source MSK cluster to determine when all data has been replicated.
3. Create a new Replicator with starting position set to _Latest_ and topic name configuration set to `IDENTICAL` (**Same topic names replication** in console).
4. Once your Replicator is in the RUNNING state, you can start the producers writing to the source cluster again.
