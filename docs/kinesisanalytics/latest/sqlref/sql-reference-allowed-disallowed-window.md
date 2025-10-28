# Allowed and Disallowed Window Specifications

Amazon Kinesis Data Analytics supports nearly all windows that end with the current row.

You cannot define an infinite window, a negative-sized window, or use negative integers in the window specification. Offset windows are currently unsupported.

- Infinite windows are windows with no bounds. Typically these point into the future, which for streams is infinite. For example "ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING" is not supported, because in a streaming context such a query would not produce a result, since streams are continually expanding as new data arrives. All uses of UNBOUNDED FOLLOWING are unsupported.
- Negative windows . For example, "ROWS BETWEEN 0 PRECEDING AND 4 PRECEDING" is a window of negative size and is therefore illegal. Instead, you would use: "ROWS BETWEEN 4 PRECEDING AND 0 PRECEDING" in this case.

- Offset windows are windows that do not end with CURRENT ROW. These are not supported in the current release. For example, "ROWS BETWEEN UNBOUNDED PRECEDING AND 4 FOLLOWING" is not supported. (Window spans CURRENT ROW rather than starting or ending there.)

- Windows defined with negative integers. For example,  "ROWS BETWEEN -4 PRECEDING AND CURRENT ROW" is invalid because negative integers are disallowed.
  Also, the special case of ... 0 PRECEDING (and ... 0 FOLLOWING) cannot be used for windowed aggregation; instead, the synonym CURRENT ROW can be used.

For windowed aggregation, partitioned windows are allowed, but ORDER BY must not be present.

For windowed join, partitioned windows are NOT allowed, but ORDER BY can be present if it sorts by the ROWTIME column of one of the inputs.
