# Ways to compress the output of your Amazon EMR cluster

There are different ways to compress output that results from data processing. The compression tools you use depend on properties of your data. Compression can improve performance when you transfer
large amounts of data.

## Output data compression

This compresses the output of your Hadoop job. If you are using TextOutputFormat the result is a gzip'ed
text file. If you are writing to SequenceFiles then the result is a SequenceFile which is compressed
internally. This can be enabled by setting the configuration setting mapred.output.compress to true.

If you are running a streaming job you can enable this by passing the streaming job these arguments.

```

-jobconf mapred.output.compress=true

```

You can also use a bootstrap action to automatically compress all job outputs. Here is how to do that
with the Ruby client.

```

--bootstrap-actions s3://elasticmapreduce/bootstrap-actions/configure-hadoop \
--args "-s,mapred.output.compress=true"

```

Finally, if are writing a Custom Jar you can enable output compression with the following line when
creating your job.

```

FileOutputFormat.setCompressOutput(conf, true);

```

## Intermediate data compression

If your job shuffles a significant amount data from the mappers to the reducers,
you can see a performance improvement by enabling intermediate compression. Compress the
map output and decompress it when it arrives on the core node. The configuration
setting is mapred.compress.map.output. You can enable this similarly to output
compression.

When writing a Custom Jar, use the following command:

```

conf.setCompressMapOutput(true);

```

## Using the Snappy library with Amazon EMR

Snappy is a compression and decompression library that is optimized for speed. It is available on Amazon EMR AMIs version 2.0 and later
and is used as the default for intermediate compression. For more information about Snappy,
go to [http://code.google.com/p/snappy/](http://code.google.com/p/snappy/ "http://code.google.com/p/snappy/").
