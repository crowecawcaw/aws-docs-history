# Call user-defined functions from Pig

Pig provides the ability to call user-defined functions (UDFs) from within Pig
scripts. You can do this to implement custom processing to use in your Pig scripts. The
languages currently supported are Java, Python/Jython, and JavaScript (though JavaScript
support is still experimental.)

The following sections describe how to register your functions with Pig so you can
call them either from the Pig shell or from within Pig scripts. For more information
about using UDFs with Pig, see [Pig documentation](http://pig.apache.org/docs/ "http://pig.apache.org/docs/") for your version of Pig.

## Call JAR files from Pig

You can use custom JAR files with Pig using the `REGISTER`
command in your Pig script. The JAR file is local or a remote file system such as
Amazon S3. When the Pig script runs, Amazon EMR downloads the JAR file automatically to the
master node and then uploads the JAR file to the Hadoop distributed cache. In this
way, the JAR file is automatically used as necessary by all instances in the
cluster.

###### To use JAR files with Pig

1. Upload your custom JAR file into Amazon S3.
2. Use the `REGISTER` command in your Pig script to
   specify the bucket on Amazon S3 of the custom JAR file.

```
REGISTER `s3://amzn-s3-demo-bucket/path/mycustomjar.jar`;
```

## Call Python/Jython scripts from Pig

You can register Python scripts with Pig and then call functions in those scripts
from the Pig shell or in a Pig script. You do this by specifying the location of the
script with the `register` keyword.

Because Pig in written in Java, it uses the Jython script engine to parse Python
scripts. For more information about Jython, go to [http://www.jython.org/](http://www.jython.org/ "http://www.jython.org/").

###### To call a Python/Jython script from Pig

1. Write a Python script and upload the script to a location in Amazon S3. This
   should be a bucket owned by the same account that creates the Pig cluster,
   or that has permissions set so the account that created the cluster can
   access it. In this example, the script is uploaded to
   s3://amzn-s3-demo-bucket/pig/python.
2. Start a Pig cluster. If you are accessing Pig from the Grunt shell, run an
   interactive cluster. If you are running Pig commands from a script, start a
   scripted Pig cluster. This example starts an interactive cluster. For more
   information about how to create a Pig cluster, see [Submit Pig work](emr-pig-launch.md "emr-pig-launch.md").
3. For an interactive cluster, use SSH to connect into the master node and
   run the Grunt shell. For more information, see [SSH into the master node](../DeveloperGuide/EMR_SetUp_SSH.md "../DeveloperGuide/EMR_SetUp_SSH.md").
4. Run the Grunt shell for Pig by typing `pig` at the command
   line:

```
pig
```

5. Register the Jython library and your Python script with Pig using the
   `register` keyword at the Grunt command prompt, as shown in
   the following command, where you would specify the location of your script
   in Amazon S3:

```
grunt> register 'lib/jython.jar';
grunt> register '`s3://amzn-s3-demo-bucket/pig/python/myscript.py`' using jython as myfunctions;
```

6. Load the input data. The following example loads input from an Amazon S3
   location:

```
grunt> input = load '`s3://amzn-s3-demo-bucket/input/data.txt`' using TextLoader as (line:chararray);
```

7. You can now call functions in your script from within Pig by referencing
   them using `myfunctions`:

```
grunt> output=foreach input generate myfunctions.myfunction($1);
```
