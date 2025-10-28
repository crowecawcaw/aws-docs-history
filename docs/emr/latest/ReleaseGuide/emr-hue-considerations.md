# Considerations

Consider the following limitations when you use [Hue](https://gethue.com "https://gethue.com") on Amazon EMR.

## Performance with large Hue metadata tables

If the Hue metadata database gets too big, performance might degrade. To check the size of the tables,
first connect to the primary node of the Amazon EMR on Amazon EC2 cluster with SSH and run the command `sudo mysql -u root`
to start the MySQL CLI. To get the size of your table, run the query `SELECT COUNT(*) FROM hue.`<table_name>``.
 See the following for what `<table_name>` can be:

- desktop_document
- desktop_document2
- oozie_job
- beeswax_savedquery
- beeswax_session
- beeswax_queryhistory

If running that query returns a count of more than 100000, you should run the following clean up command to delete
the old records.

```
cd /opt/cloudera/parcels/CDH/lib/hue # Hue home directory ./build/env/bin/hue desktop_document_cleanup
```

For more information about cleaning up your database, see the [reference page in the Hue documentation](https://docs.gethue.com/administrator/administration/reference/#general "https://docs.gethue.com/administrator/administration/reference/#general").

Hue doesn't automatically clean the tables, but Amazon EMR releases 5.12.0 and higher provide a method to delete old documents
in the tables. Create the following shell script and run it as a step in an Amazon EMR cluster with an integer parameter that represents the
maximum number of days of how long to keep documents in the metadata database.

```
#!/bin/bash
if grep isMaster /mnt/var/lib/info/instance.json | grep false;
then
  echo "This is not the primary node; do nothing, exiting"
  exit 0
fi
while [ ! -f /usr/lib/hue/desktop/core/src/desktop/management/commands/desktop_document_cleanup.py ]
do
  sleep 1
done
sudo systemctl stop hue.service
sudo sed -i 's+  LOG.warn+  # LOG.warn+g' /usr/lib/hue/desktop/core/src/desktop/management/commands/desktop_document_cleanup.py
sudo /usr/lib/hue/build/env/bin/hue desktop_document_cleanup --keep-days $1
sudo systemctl start hue.service
```

## Incompatibility between Hue versions

If you're using the same Hue metadata database across multiple Hue-enabled clusters, we recommend that
these clusters run the same version of Hue. Different versions of Hue can have different schemas for the Hue metadata database.
Using the same database for different versions can cause a Hue installation to fail. For example,
trying to use the same database for two clusters with 4.10.0 and 4.11.0 installed can cause login errors
for the users trying to log in to the 4.10.0 cluster.

For a list of Amazon EMR release labels and the corresponding installed versions of Hue, see [Hue release history](Hue-release-history.md "Hue-release-history.md").
