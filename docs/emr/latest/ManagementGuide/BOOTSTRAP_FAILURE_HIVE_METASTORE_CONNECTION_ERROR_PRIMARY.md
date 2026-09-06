

# BOOTSTRAP\_FAILURE\_HIVE\_METASTORE\_CONNECTION\_ERROR\_PRIMARY
<a name="BOOTSTRAP_FAILURE_HIVE_METASTORE_CONNECTION_ERROR_PRIMARY"></a>

## Overview
<a name="BOOTSTRAP_FAILURE_HIVE_METASTORE_CONNECTION_ERROR_PRIMARY_overview"></a>

 The `BOOTSTRAP_FAILURE_HIVE_METASTORE_CONNECTION_ERROR_PRIMARY` error indicates that the primary instance is unable to establish a connection to the configured external Hive Metastore. 

## Resolution
<a name="BOOTSTRAP_FAILURE_HIVE_METASTORE_CONNECTION_ERROR_PRIMARY_resolution"></a>

 To resolve this error, confirm that your external Hive Metastore is configured properly and the primary instance is allowed to connect to it. 

To troubleshoot the failed EMR cluster, refer to the `ErrorDetail` information returned from the `DescribeCluster` and `ListClusters` APIs. For more information, see [Error codes with ErrorDetail information in Amazon EMR](emr-troubleshoot-error-errordetail.md). The `ErrorData` array within `ErrorDetail` returns the following information for this error code:

**`primary-instance-id`**  
The ID of the primary instance unable to establish a connection to the configured external Hive Metastore.

**`public-doc`**  
The public URL of the documentation for the error code.

## Steps to complete
<a name="BOOTSTRAP_FAILURE_HIVE_METASTORE_CONNECTION_ERROR_PRIMARY_stc"></a>

1.  Review the best practices for for configuring an external metastore for Hive. See [Configuring an external metastore for Hive](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-metastore-external-hive.html). 

1. Launch a new cluster with your updated cluster configuration.