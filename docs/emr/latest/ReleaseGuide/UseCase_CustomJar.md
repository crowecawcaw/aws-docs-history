# Process data with a custom JAR

A custom JAR runs a compiled Java program that you can upload to Amazon S3. You should compile
the program against the version of Hadoop you want to launch, and submit a
`CUSTOM_JAR` step to your Amazon EMR cluster. For more information about how to
compile a JAR file, see [Build binaries using Amazon EMR](emr-build-binaries.md "emr-build-binaries.md").

For more information about building a Hadoop MapReduce application, see the [MapReduce Tutorial](http://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html "http://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html") in the Apache Hadoop documentation.

###### Topics

- [Submit a custom JAR step](emr-launch-custom-jar-cli.md "emr-launch-custom-jar-cli.md")
