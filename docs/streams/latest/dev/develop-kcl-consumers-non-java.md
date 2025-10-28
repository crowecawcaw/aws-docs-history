# Develop consumers with KCL in non-Java languages

This section covers the implementation of consumers using Kinesis Client Library
(KCL) in Python, Node.js, .NET, and Ruby.

KCL is a Java library. Support for languages other than Java is provided
using a multi-language interface called the `MultiLangDaemon`. This daemon is
Java-based and runs in the background when you are using a KCL with a language
other than Java. Therefore, if you install KCL for non-Java languages and write
your consumer app entirely in non-Java languages, you still need Java installed on your
system because of the `MultiLangDaemon`. Further,
`MultiLangDaemon` has some default settings you might need to customize
for your use case (for example, the AWS region that it connects to). For more
information about the `MultiLangDaemon` on GitHub, see [KCL MultiLangDaemon project](https://github.com/awslabs/amazon-kinesis-client/tree/v1.x/src/main/java/com/amazonaws/services/kinesis/multilang "https://github.com/awslabs/amazon-kinesis-client/tree/v1.x/src/main/java/com/amazonaws/services/kinesis/multilang").

While the core concepts remain the same across languages, there are some
language-specific considerations and implementations. For the core concepts about the
KCL consumer development, see [Develop consumers with KCL in
Java](develop-kcl-consumers-java.md "develop-kcl-consumers-java.md"). For more detailed information about
how to develop KCL consumers in Python, Node.js, .NET, and Ruby and latest
updates, please refer to the following GitHub repositories:

- Python: [amazon-kinesis-client-python](https://github.com/awslabs/amazon-kinesis-client-python "https://github.com/awslabs/amazon-kinesis-client-python")
- Node.js: [amazon-kinesis-client-nodejs](https://github.com/awslabs/amazon-kinesis-client-nodejs "https://github.com/awslabs/amazon-kinesis-client-nodejs")
- .NET: [amazon-kinesis-client-net](https://github.com/awslabs/amazon-kinesis-client-net "https://github.com/awslabs/amazon-kinesis-client-net")
- Ruby: [amazon-kinesis-client-ruby](https://github.com/awslabs/amazon-kinesis-client-ruby "https://github.com/awslabs/amazon-kinesis-client-ruby")

###### Important

Don't use the following non-Java KCL library versions if you're using JDK 8. These versions contain a dependency (logback) that is incompatible with JDK 8.

- KCL Python 3.0.2 and 2.2.0
- KCL Node.js 2.3.0
- KCL .NET 3.1.0
- KCL Ruby 2.2.0
  We recommend that you use versions released either before or after these affected versions when working with JDK 8.
