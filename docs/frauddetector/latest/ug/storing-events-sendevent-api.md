Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Store event data using the SendEvent API operation

You can use the `SendEvent` API operation to store events in Amazon Fraud Detector without generating fraud predictions for those events. For example,
you can use the `SendEvent` operation to upload a historical dataset, which you can later use to train a model.

**Event Timestamp formats for SendEvent API**

When storing event data using `SendEvent` API, you must ensure that your event timestamp is in the required format. Amazon Fraud Detector supports
the following date/timestamp formats:

- %yyyy-%mm-%ddT%hh:%mm:%ssZ (ISO 8601 standard in UTC only with no milliseconds)

Example: 2019-11-30T13:01:01Z

- %yyyy/%mm/%dd %hh:%mm:%ss (AM/PM)

Examples: 2019/11/30 1:01:01 PM, or 2019/11/30 13:01:01

- %mm/%dd/%yyyy %hh:%mm:%ss

Examples: 11/30/2019 1:01:01 PM, 11/30/2019 13:01:01

- %mm/%dd/%yy %hh:%mm:%ss

Examples: 11/30/19 1:01:01 PM, 11/30/19 13:01:01
Amazon Fraud Detector makes the following assumptions when parsing date/timestamp formats for event timestamps:

- If you are using the ISO 8601 standard, it must be an exact match of the preceding specification
- If you are using one of the other formats, there is additional flexibility:

      + For months and days, you can provide single or double digits. For example, 1/12/2019 is a valid date.
      + You do not need to include hh:mm:ss if you do not have them (that is, you can simply provide a date). You can also provide a subset
       of just the hour and minutes (for example, hh:mm). Just providing hour is not supported. Milliseconds are also not supported.
      + If you provide AM/PM labels, a 12-hour clock is assumed. If there is no AM/PM information, a 24-hour clock is assumed.
      + You can use “/” or “-” as delimiters for the date elements. “:” is assumed for the timestamp elements.

  The following is an example `SendEvent` API call.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.send_event(
            eventId        = '802454d3-f7d8-482d-97e8-c4b6db9a0428',
            eventTypeName  = 'sample_registration',
            eventTimestamp = '2020-07-13T23:18:21Z',
            eventVariables =  {
    			'email_address' : 'johndoe@exampledomain.com',
    			'ip_address' : '1.2.3.4'},
            assignedLabel  = ‘legit’,
            labelTimestamp = '2020-07-13T23:18:21Z',
            entities       = [{'entityType':'sample_customer', 'entityId':'12345'}],
)


```
