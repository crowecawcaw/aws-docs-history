# Best practice 7.2 – Monitor for data quality anomalies

Data quality is critical for organizations to accurately measure important business metrices, bad data can impact the accuracy of analytics insights and ML predictions. Monitor data quality and detect data anomalies as early as possible.

For more details, see AWS Glue: [Getting started with AWS Glue Date Quality](https://aws.amazon.com/blogs/big-data/getting-started-with-aws-glue-data-quality-from-the-aws-glue-data-catalog/ "https://aws.amazon.com/blogs/big-data/getting-started-with-aws-glue-data-quality-from-the-aws-glue-data-catalog/").

## Suggestion 7.2.1 – Include a data quality check stage in the ETL pipeline as early as possible

A data quality check helps ensure that bad data is
identified and fixed as soon as possible to prevent bad data
from propagating downstream.

## Suggestion 7.2.2 – Understand the nature of your data and determine the types of data anomalies that must be monitored and fixed based on the business requirements

The analytics workload can process various types of data,
such as structured, unstructured, picture, audio, and
video formats. Some data might arrive to the workload
periodically, or some might constantly arrive in real
time. It is pragmatic to assume that data does not always
arrive to the analytics workload in perfect shape, and
only a portion – not the whole set – of data matters to
your workload.

Understand the characteristics of data, and determine what forms of data anomalies you want to remediate. For example, if you expect the data always contains an important attribute like customer ID, you can deﬁne that a datum is abnormal if it doesn’t contain the `customer_id` attribute. Common data anomalies include duplicate data, missing data, incomplete data, incorrect data format, and diﬀerent measurement units.

## Suggestion 7.2.3 – Select an existing data quality solution or develop your own based on the requirements

There are data quality solutions that can only detect single ﬁeld data quality issues. Other solutions can handle complex stateful data quality issues related to multiple ﬁelds.
