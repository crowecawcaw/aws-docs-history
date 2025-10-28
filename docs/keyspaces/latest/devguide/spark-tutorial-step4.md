# Step 4: Prepare the source data and the target

table in Amazon Keyspaces

In this step, you create a source file with sample data and an Amazon Keyspaces table.

1. Create the source file. You can choose one of the following options:
   - For this tutorial, you use a comma-separated values (CSV) file with
     the name `keyspaces_sample_table.csv` as the source
     file for the data migration. The provided sample file contains a few
     rows of data for a table with the name
     `book_awards`.
     1. Download the sample CSV file
        (`keyspaces_sample_table.csv`) that is
        contained in the following archive file [samplemigration.zip](samples/samplemigration.md "samples/samplemigration.md"). Unzip the archive and take
        note of the path to
        `keyspaces_sample_table.csv`.

   - If you want to follow along with your own CSV file to write data to
     Amazon Keyspaces, make sure that the data is randomized. Data that is read directly
     from a database or exported to flat files is typically ordered by the
     partition and primary key. Importing ordered data to Amazon Keyspaces can cause it
     to be written to smaller segments of Amazon Keyspaces partitions, which results in
     an uneven traffic distribution. This can lead to slower performance and
     higher error rates.

   In contrast, randomizing data helps to take advantage of the built-in
   load balancing capabilities of Amazon Keyspaces by distributing traffic across
   partitions more evenly. There are various tools that you can use for
   randomizing data. For an example that uses the open-source tool [Shuf](https://en.wikipedia.org/wiki/Shuf "https://en.wikipedia.org/wiki/Shuf"), see [Step 2: Prepare the data to upload using DSBulk](dsbulk-upload-prepare-data.md "dsbulk-upload-prepare-data.md") in the data migration
   tutorial. The following is an example that shows how to shuffle data as
   a `DataFrame`.

   ```
   import org.apache.spark.sql.functions.randval
   shuffledDF = dataframe.orderBy(rand())
   ```

2. Create the target keyspace and table in Amazon Keyspaces.
   1. Connect to Amazon Keyspaces using the `cqlsh-expansion`. For `cqlsh-expansion` installation
      instructions, see [Using the cqlsh-expansion to connect
      to Amazon Keyspaces](programmatic.md#using_cqlsh "programmatic.md#using_cqlsh").

   Replace the service
   endpoint in the following example with your own
   value.

   ```
   cqlsh-expansion cassandra.`us-east-1`.amazonaws.com 9142 --ssl
   ```

   2. Create a new keyspace with the name `catalog` as
      shown in the following example.

   ```
   CREATE KEYSPACE `catalog` WITH REPLICATION = {'class': 'SingleRegionStrategy'};
   ```

   3. After the new keyspace has a status of available, use the following
      code to create the target table `book_awards`. To
      learn more about asynchronous resource creation and how to check if a
      resource is available, see [Check keyspace creation status in Amazon Keyspaces](keyspaces-create.md "keyspaces-create.md").

   ```
   CREATE TABLE `catalog.book_awards` (
      year int,
      award text,
      rank int,
      category text,
      book_title text,
      author text,
      publisher text,
      PRIMARY KEY ((year, award), category, rank)
      );
   ```
