# Develop a Kinesis Client Library

consumer in Ruby

###### Important

Amazon Kinesis Client Library (KCL) versions 1.x and 2.x are outdated. KCL 1.x will reach end-of-support on January 30, 2026. We **strongly recommend** that you migrate your KCL applications using version 1.x to the latest KCL version before January 30, 2026. To find the latest KCL version, see [Amazon Kinesis Client Library page on GitHub](https://github.com/awslabs/amazon-kinesis-client "https://github.com/awslabs/amazon-kinesis-client"). For information about the latest KCL versions, see [Use Kinesis Client Library](kcl.md "kcl.md"). For information about migrating from KCL 1.x to KCL 3.x, see [Migrating from KCL 1.x to KCL
3.x](kcl-migration-1-3.md "kcl-migration-1-3.md").

You can use the Kinesis Client Library (KCL) to build applications that process data
from your Kinesis data streams. The Kinesis Client Library is available in multiple languages. This
topic discusses Ruby.

The KCL is a Java library; support for languages other than Java is provided using a
multi-language interface called the _MultiLangDaemon_. This daemon is
Java-based and runs in the background when you are using a KCL language other than Java. Therefore, if you install the KCL for Ruby and write your consumer app
entirely in Ruby, you still need Java installed on your system because of the MultiLangDaemon.
Further, MultiLangDaemon has some default settings you may need to customize for your use
case, for example, the AWS Region that it connects to. For more information about the
MultiLangDaemon on GitHub, go to the
[KCL MultiLangDaemon project](https://github.com/awslabs/amazon-kinesis-client/tree/v1.x/src/main/java/com/amazonaws/services/kinesis/multilang "https://github.com/awslabs/amazon-kinesis-client/tree/v1.x/src/main/java/com/amazonaws/services/kinesis/multilang") page.

To download the Ruby KCL from GitHub, go to [Kinesis Client Library (Ruby)](https://github.com/awslabs/amazon-kinesis-client-ruby "https://github.com/awslabs/amazon-kinesis-client-ruby"). To download
sample code for a Ruby KCL consumer application, go to the [KCL for Ruby sample project](https://github.com/awslabs/amazon-kinesis-client-ruby/tree/master/samples "https://github.com/awslabs/amazon-kinesis-client-ruby/tree/master/samples") page on GitHub.

For more information about the KCL Ruby support library, see
[KCL Ruby Gems Documentation](http://www.rubydoc.info/gems/aws-kclrb "http://www.rubydoc.info/gems/aws-kclrb").
