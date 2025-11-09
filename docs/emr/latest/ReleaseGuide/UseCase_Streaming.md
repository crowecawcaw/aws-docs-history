# Process data with streaming

Hadoop streaming is a utility that comes with Hadoop that enables you to develop MapReduce
executables in languages other than Java. Streaming is implemented in the form of a JAR
file, so you can run it from the Amazon EMR API or command line just like a standard
JAR file.

This section describes how to use streaming with Amazon EMR.

###### Note

Apache Hadoop streaming is an independent tool. As such, all of its functions and parameters
are not described here. For more information about Hadoop streaming, go to [http://hadoop.apache.org/docs/stable/hadoop-streaming/HadoopStreaming.html](http://hadoop.apache.org/docs/stable/hadoop-streaming/HadoopStreaming.html "http://hadoop.apache.org/docs/stable/hadoop-streaming/HadoopStreaming.html").

## Using the Hadoop streaming utility

This section describes how use to Hadoop's streaming utility.

Hadoop process| 1 | Write your mapper and reducer executable in the programming language of<br>your choice.<br>Follow the directions in Hadoop's documentation to write your<br>streaming executables. The programs should read their input from standard<br>input and output data through standard output. By default, each line of<br>input/output represents a record and the first tab on each line is used as a<br>separator between the key and value. |
| 2 | Test your executables locally and upload them to Amazon S3. |
| 3 | Use the Amazon EMR command line interface or Amazon EMR console to run your application. |

Each mapper script launches as a separate process in the cluster. Each reducer executable
turns the output of the mapper executable into the data output by the job flow.

The `input`, `output`,
`mapper`, and `reducer` parameters are
required by most streaming applications. The following table describes these and other,
optional parameters.

| Parameter     | Description                                                                                                                                                                                                                                   | Required |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| -input        | Location on Amazon S3 of the input data.<br>Type: String<br>Default: None<br>Constraint: URI. If no protocol is specified then it uses the<br>cluster's default file system.                                                                  | Yes      |
| -output       | Location on Amazon S3 where Amazon EMR uploads the processed<br>data.<br>Type: String<br>Default: None<br>Constraint: URI<br>Default: If a location is not specified, Amazon EMR uploads<br>the data to the location specified by<br>`input`. | Yes      |
| -mapper       | Name of the mapper executable.<br>Type: String<br>Default: None                                                                                                                                                                               | Yes      |
| -reducer      | Name of the reducer executable.<br>Type: String<br>Default: None                                                                                                                                                                              | Yes      |
| -cacheFile    | An Amazon S3 location containing files for Hadoop to copy into your local working directory<br>(primarily to improve performance).<br>Type: String<br>Default: None<br>Constraints: [URI]#[symlink name to create in working directory]       | No       |
| -cacheArchive | JAR file to extract into the working directory<br>Type: String<br>Default: None<br>Constraints: [URI]#[symlink directory name to create in working<br>directory                                                                               | No       |
| -combiner     | Combines results<br>Type: String<br>Default: None<br>Constraints: Java class name                                                                                                                                                             | No       |

The following code sample is a mapper executable written in Python. This script is part of the WordCount sample application.

```
#!/usr/bin/python
import sys

def main(argv):
  line = sys.stdin.readline()
  try:
    while line:
      line = line.rstrip()
      words = line.split()
      for word in words:
        print "LongValueSum:" + word + "\t" + "1"
      line = sys.stdin.readline()
  except "end of file":
    return None
if __name__ == "__main__":
  main(sys.argv)
```
