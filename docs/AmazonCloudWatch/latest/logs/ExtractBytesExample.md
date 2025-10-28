# Example: Extract fields from an Apache log and

assign dimensions

Sometimes, instead of counting, it is helpful to use values within individual log
events for metric values. This example shows how you can create an extraction rule
to create a metric that measures the bytes transferred by an Apache
webserver.

This example also shows how to assign dimensions to the metric that you are
creating.

###### To create a metric filter using the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Log groups**.
3. Choose the name of the log group for the Apache server.
4. Choose `Actions`, **Create metric
   filter**.
5. For **Filter pattern**, enter `[ip, id, user,
timestamp, request, status_code, size]`.
6. (Optional) To test your filter pattern, under **Test
   Pattern**, enter one or more log events to use to test the
   pattern. Each log event must be within one line, because line breaks are
   used to separate log events in the **Log event messages**
   box.
7. Choose **Next**, and then for **Filter
   name**, type `size`.
8. Under **Metric details**, for **Metric
   namespace**, enter `MyNameSpace`. Because
   this is a new namespace, be sure that **Create new** is
   selected.
9. For **Metric name**, enter
   `BytesTransferred`
10. For **Metric value**, enter
    `$size`.
11. For **Unit**, select **Bytes**.
12. For **Dimension Name**, type
    `IP`.
13. For **Dimension Value**, type `$ip`
    and then choose **Next**.
14. Choose **Create metric filter**.

###### To create this metric filter using the AWS CLI

At a command prompt, run the following command

```
`aws logs put-metric-filter \
--log-group-name MyApp/access.log \
 --filter-name BytesTransferred \
 --filter-pattern '[ip, id, user, timestamp, request, status_code, size]' \
 --metric-transformations \
 metricName=BytesTransferred,metricNamespace=MyNamespace,metricValue='$size'`
```

```
`aws logs put-metric-filter \
--log-group-name MyApp/access.log \
--filter-name BytesTransferred \
--filter-pattern '[ip, id, user, timestamp, request, status_code, size]' \
--metric-transformations \
metricName=BytesTransferred,metricNamespace=MyNamespace,metricValue='$size',unit=Bytes,dimensions='{{IP=$ip}}'`
```

###### Note

In this command, use this format to specify multiple dimensions.

```
`aws logs put-metric-filter \
--log-group-name `my-log-group-name` \
--filter-name `my-filter-name` \
--filter-pattern '`my-filter-pattern`' \
--metric-transformations \
metricName=`my-metric-name`,metricNamespace=`my-metric-namespace`,metricValue=`my-token`,unit=`unit`,dimensions='{dimension1=$dim,dimension2=$dim2,dim3=$dim3}'`
```

You can use the following data in put-log-event calls to test this rule. This
generates two different metrics if you did not remove monitoring rule in the
previous example.

```
127.0.0.1 - - [24/Sep/2013:11:49:52 -0700] "GET /index.html HTTP/1.1" 404 287
127.0.0.1 - - [24/Sep/2013:11:49:52 -0700] "GET /index.html HTTP/1.1" 404 287
127.0.0.1 - - [24/Sep/2013:11:50:51 -0700] "GET /~test/ HTTP/1.1" 200 3
127.0.0.1 - - [24/Sep/2013:11:50:51 -0700] "GET /favicon.ico HTTP/1.1" 404 308
127.0.0.1 - - [24/Sep/2013:11:50:51 -0700] "GET /favicon.ico HTTP/1.1" 404 308
127.0.0.1 - - [24/Sep/2013:11:51:34 -0700] "GET /~test/index.html HTTP/1.1" 200 3
```
