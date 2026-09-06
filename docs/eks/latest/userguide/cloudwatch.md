

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Monitor cluster data with Amazon CloudWatch
<a name="cloudwatch"></a>

Amazon CloudWatch is a monitoring service that collects metrics and logs from your cloud resources. CloudWatch provides some basic Amazon EKS metrics for free when using a new cluster that is version `1.28` and above. However, when using the CloudWatch Observability Operator as an Amazon EKS add-on, you can gain enhanced observability features.

## Basic metrics in Amazon CloudWatch
<a name="cloudwatch-basic-metrics"></a>

For clusters that are Kubernetes version `1.28` and above, you get CloudWatch vended metrics for free in the `AWS/EKS` namespace. The following table gives a list of the basic metrics that are available for the supported versions. Every metric listed has a frequency of one minute.


| Metric name | Description | 
| --- | --- | 
|  `apiserver_flowcontrol_current_executing_seats`  | The number of seats currently in use for executing API requests. Seat allocation is determined by the priority\_level and flow\_schema configuration in the Kubernetes API Priority and Fairness [feature](https://kubernetes.io/docs/concepts/cluster-administration/flow-control/).<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `scheduler_schedule_attempts_total`  | The number of total attempts by the scheduler to schedule Pods in the cluster for a given period. This metric helps monitor the scheduler’s workload and can indicate scheduling pressure or potential issues with Pod placement.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `scheduler_schedule_attempts_SCHEDULED`  | The number of successful attempts by the scheduler to schedule Pods to nodes in the cluster for a given period.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `scheduler_schedule_attempts_UNSCHEDULABLE`  | The number of attempts to schedule Pods that were unschedulable for a given period due to valid constraints, such as insufficient CPU or memory on a node.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `scheduler_schedule_attempts_ERROR`  | The number of attempts to schedule Pods that failed for a given period due to an internal problem with the scheduler itself, such as API Server connectivity issues.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `scheduler_pending_pods`  | The number of total pending Pods to be scheduled by the scheduler in the cluster for a given period.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `scheduler_pending_pods_ACTIVEQ`  | The number of pending Pods in activeQ, that are waiting to be scheduled in the cluster for a given period.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `scheduler_pending_pods_UNSCHEDULABLE`  | The number of pending Pods that the scheduler attempted to schedule and failed, and are kept in an unschedulable state for retry.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `scheduler_pending_pods_BACKOFF`  | The number of pending Pods in `backoffQ` in a backoff state that are waiting for their backoff period to expire.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `scheduler_pending_pods_GATED`  | The number of pending Pods that are currently waiting in a gated state as they cannot be scheduled until they meet required conditions.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `apiserver_request_total`  | The number of HTTP requests made across all the API servers in the cluster.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `apiserver_request_total_4XX`  | The number of HTTP requests made to all the API servers in the cluster that resulted in `4XX` (client error) status codes.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `apiserver_request_total_429`  | The number of HTTP requests made to all the API servers in the cluster that resulted in `429` status code, which occurs when clients exceed the rate limiting thresholds.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `apiserver_request_total_5XX`  | The number of HTTP requests made to all the API servers in the cluster that resulted in `5XX` (server error) status codes.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `apiserver_request_total_LIST_PODS`  | The number of `LIST` Pods requests made to all the API servers in the cluster.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `apiserver_request_duration_seconds_PUT_P99`  | The 99th percentile of latency for `PUT` requests calculated from all requests across all API servers in the cluster. Represents the response time below which 99% of all `PUT` requests are completed.<br /> **Units:** Seconds<br /> **Valid statistics:** Average | 
|  `apiserver_request_duration_seconds_PATCH_P99`  | The 99th percentile of latency for `PATCH` requests calculated from all requests across all API servers in the cluster. Represents the response time below which 99% of all `PATCH` requests are completed.<br /> **Units:** Seconds<br /> **Valid statistics:** Average | 
|  `apiserver_request_duration_seconds_POST_P99`  | The 99th percentile of latency for `POST` requests calculated from all requests across all API servers in the cluster. Represents the response time below which 99% of all `POST` requests are completed.<br /> **Units:** Seconds<br /> **Valid statistics:** Average | 
|  `apiserver_request_duration_seconds_GET_P99`  | The 99th percentile of latency for `GET` requests calculated from all requests across all API servers in the cluster. Represents the response time below which 99% of all `GET` requests are completed.<br /> **Units:** Seconds<br /> **Valid statistics:** Average | 
|  `apiserver_request_duration_seconds_LIST_P99`  | The 99th percentile of latency for `LIST` requests calculated from all requests across all API servers in the cluster. Represents the response time below which 99% of all `LIST` requests are completed.<br /> **Units:** Seconds<br /> **Valid statistics:** Average | 
|  `apiserver_request_duration_seconds_DELETE_P99`  | The 99th percentile of latency for `DELETE` requests calculated from all requests across all API servers in the cluster. Represents the response time below which 99% of all `DELETE` requests are completed.<br /> **Units:** Seconds<br /> **Valid statistics:** Average | 
|  `apiserver_current_inflight_requests_MUTATING`  | The number of mutating requests (`POST`, `PUT`, `DELETE`, `PATCH`) currently being processed across all API servers in the cluster. This metric represents requests that are in-flight and haven’t completed processing yet.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `apiserver_current_inflight_requests_READONLY`  | The number of read-only requests (`GET`, `LIST`) currently being processed across all API servers in the cluster. This metric represents requests that are in-flight and haven’t completed processing yet.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `apiserver_admission_webhook_request_total`  | The number of admission webhook requests made across all API servers in the cluster.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `apiserver_admission_webhook_request_total_ADMIT`  | The number of mutating admission webhook requests made across all API servers in the cluster.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `apiserver_admission_webhook_request_total_VALIDATING`  | The number of validating admission webhook requests made across all API servers in the cluster.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `apiserver_admission_webhook_rejection_count`  | The number of admission webhook requests made across all API servers in the cluster that were rejected.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `apiserver_admission_webhook_rejection_count_ADMIT`  | The number of mutating admission webhook requests made across all API servers in the cluster that were rejected.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `apiserver_admission_webhook_rejection_count_VALIDATING`  | The number of validating admission webhook requests made across all API servers in the cluster that were rejected.<br /> **Units:** Count<br /> **Valid statistics:** Sum | 
|  `apiserver_admission_webhook_admission_duration_seconds`  | The 99th percentile of latency for third-party admission webhook requests calculated from all requests across all API servers in the cluster. Represents the response time below which 99% of all third-party admission webhook requests are completed.<br /> **Units:** Seconds<br /> **Valid statistics:** Average | 
|  `apiserver_admission_webhook_admission_duration_seconds_ADMIT_P99`  | The 99th percentile of latency for third-party mutating admission webhook requests calculated from all requests across all API servers in the cluster. Represents the response time below which 99% of all third-party mutating admission webhook requests are completed.<br /> **Units:** Seconds<br /> **Valid statistics:** Average | 
|  `apiserver_admission_webhook_admission_duration_seconds_VALIDATING_P99`  | The 99th percentile of latency for third-party validating admission webhook requests calculated from all requests across all API servers in the cluster. Represents the response time below which 99% of all third-party validating admission webhook requests are completed.<br /> **Units:** Seconds<br /> **Valid statistics:** Average | 
|  `etcd_mvcc_db_total_size_in_bytes`  | Total size of the underlying database physically allocated in bytes. Note that this metric measures physical disk allocation and is not used for quota enforcement. (also known as apiserver\_storage\_size\_bytes)<br /> **Units:** Bytes<br /> **Valid statistics:** Maximum | 
|  `etcd_mvcc_db_total_size_in_use_in_bytes`  | The actual data size of the etcd database, excluding free space waiting for defragmentation. This metric indicates the current database usage and determines whether the cluster will exceed the database size quota and enter read-only mode.<br /> **Units:** Bytes<br /> **Valid statistics:** Maximum | 

## Amazon CloudWatch Observability Operator
<a name="cloudwatch-operator"></a>

Amazon CloudWatch Observability collects real-time logs, metrics, and trace data. It sends them to [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) and [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html). You can install this add-on to enable both CloudWatch Application Signals and CloudWatch Container Insights with enhanced observability for Amazon EKS. This helps you monitor the health and performance of your infrastructure and containerized applications. The Amazon CloudWatch Observability Operator is designed to install and configure the necessary components.

Amazon EKS supports the CloudWatch Observability Operator as an [Amazon EKS add-on](eks-add-ons.md). The add-on allows Container Insights on both Linux and Windows worker nodes in the cluster. To enable Container Insights on Windows, the Amazon EKS add-on version must be `1.5.0` or higher. Currently, CloudWatch Application Signals isn’t supported on Amazon EKS Windows.

The topics below describe how to get started using CloudWatch Observability Operator for your Amazon EKS cluster.
+ For instructions on installing this add-on, see [Install the CloudWatch agent with the Amazon CloudWatch Observability EKS add-on or the Helm chart](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.html) in the *Amazon CloudWatch User Guide*.
+ For more information about CloudWatch Application Signals, see [Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html) in the *Amazon CloudWatch User Guide*.
+ For more information about Container Insights, see [Using Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html) in the *Amazon CloudWatch User Guide*.