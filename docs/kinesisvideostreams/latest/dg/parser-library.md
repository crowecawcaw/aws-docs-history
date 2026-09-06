

# Watch output from cameras using parser library
<a name="parser-library"></a>

The Kinesis video stream parser library is a set of tools that you can use in Java applications to consume the MKV data in a Kinesis video stream.

The library includes the following tools:
+ [StreamingMkvReader](parser-library-write.md#parser-library-write-SMSR): This class reads specified MKV elements from a video stream.
+ [FragmentMetadataVisitor](parser-library-write.md#parser-library-write-FMV): This class retrieves metadata for fragments (media elements) and tracks (individual data streams containing media information, such as audio or subtitles).
+ [OutputSegmentMerger](parser-library-write.md#parser-library-write-OSM): This class merges consecutive fragments or chunks in a video stream.
+ [KinesisVideoExample](parser-library-write.md#parser-library-write-example): This is a sample application that shows how to use the Kinesis video stream parser library.

The library also includes tests that show how the tools are used.

## Prerequisites
<a name="parser-library-prerequisites"></a>

You must have the following to examine and use the Kinesis video stream parser library:
+ An Amazon Web Services (AWS) account. If you don't already have an AWS account, see [Sign up for an AWS account](gs-account.md#sign-up-for-aws).
+ A Java integrated development environment (IDE), such as [Eclipse Java Neon](https://www.eclipse.org/downloads/packages/release/neon/3/eclipse-jee-neon-3) or [JetBrains IntelliJ Idea](https://www.jetbrains.com/idea/download/).
+ Java 11, such as [Amazon Corretto 11](https://docs.aws.amazon.com/corretto/latest/corretto-11-ug/what-is-corretto-11.html).