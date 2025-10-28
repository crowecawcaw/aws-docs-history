# Neptune Streams API Exceptions

The following table describes Neptune Streams exceptions.

| Error Code                       | HTTP Code | OK to Retry? | Message                                                                                                        |
| -------------------------------- | --------- | ------------ | -------------------------------------------------------------------------------------------------------------- |
| `InvalidParameterException`      | 400       | No           | An invalid or out-of-range value was supplied as an input parameter.                                           |
| `ExpiredStreamException`         | 400       | No           | All of the requested records exceed the maximum age allowed and have expired.                                  |
| `ThrottlingException`            | 500       | Yes          | Rate of requests exceeds the maximum throughput.                                                               |
| `StreamRecordsNotFoundException` | 404       | No           | The requested resource could not be found. The stream may not be specified correctly.                          |
| `MemoryLimitExceededException`   | 500       | Yes          | The request processing did not succeed due to lack of memory, but can be retried when the server is less busy. |
