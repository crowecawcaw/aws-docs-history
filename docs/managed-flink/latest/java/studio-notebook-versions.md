Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Use the correct Studio notebook Runtime

version

With Amazon Managed Service for Apache Flink Studio, you can query data streams in real time and build and run
stream processing applications using standard SQL, Python, and Scala in an interactive
notebook. Studio notebooks are powered by [Apache Zeppelin](https://zeppelin.apache.org/ "https://zeppelin.apache.org/") and use [Apache
Flink](https://flink.apache.org/ "https://flink.apache.org/") as the stream processing engine.

###### Note

We will deprecate Studio Runtime with **Apache Flink version
1.11 on November 5, 2024**. Starting from this date, you will not be
able to run new notebooks or create new applications using this version. We
recommend that you upgrade to the latest runtime (Apache Flink 1.15 and Apache
Zeppelin 0.10) before that time. For guidance on how to upgrade your notebook, see
[Upgrade Studio Runtime](upgrading-studio-runtime.md "upgrading-studio-runtime.md").

| Studio Runtime | Apache Flink version | Apache Zeppelin version | Python version                   |     |
| -------------- | -------------------- | ----------------------- | -------------------------------- | --- |
| 1.15           | 0.1                  | 3.8                     | Recommended                      |
| 1.13           | 0.9                  | 3.8                     | Supported until October 16, 2024 |
| 1.11           | 0.9                  | 3.7                     | Deprecating on February 24, 2025 |
