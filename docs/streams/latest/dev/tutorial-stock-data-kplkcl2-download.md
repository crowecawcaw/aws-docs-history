# Download and build the

code

This topic provides sample implementation code for the sample stock trades ingestion
into the data stream (_producer_) and the processing of
this data (_consumer_).

###### To download and build the code

1. Download the source code from the [https://github.com/aws-samples/amazon-kinesis-learning](https://github.com/aws-samples/amazon-kinesis-learning "https://github.com/aws-samples/amazon-kinesis-learning") GitHub repo
   to your computer.
2. Create a project in your IDE with the source code, adhering to the provided
   directory structure.
3. Add the following libraries to the project:
   - Amazon Kinesis Client Library (KCL)
   - AWS SDK
   - Apache HttpCore
   - Apache HttpClient
   - Apache Commons Lang
   - Apache Commons Logging
   - Guava (Google Core Libraries For Java)
   - Jackson Annotations
   - Jackson Core
   - Jackson Databind
   - Jackson Dataformat: CBOR
   - Joda Time

4. Depending on your IDE, the project might be built automatically. If not, build
   the project using the appropriate steps for your IDE.
   If you complete these steps successfully, you are now ready to move to the next
   section, [Implement the producer](tutorial-stock-data-kplkcl2-producer.md "tutorial-stock-data-kplkcl2-producer.md").

## Next steps

[Implement the producer](tutorial-stock-data-kplkcl2-producer.md "tutorial-stock-data-kplkcl2-producer.md")
