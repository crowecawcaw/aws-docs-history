#

BOOTSTRAP_FAILURE_HIVE_METASTORE_CONNECTION_ERROR_PRIMARY

## Overview

The `BOOTSTRAP_FAILURE_HIVE_METASTORE_CONNECTION_ERROR_PRIMARY` error indicates that
the primary instance is unable to establish a connection to the configured external Hive Metastore.

## Resolution

To resolve this error, confirm that your external Hive Metastore is configured properly and the
primary instance is allowed to connect to it.

To troubleshoot the failed EMR cluster, refer to the `ErrorDetail` information returned from the `DescribeCluster` and `ListClusters` APIs. For more information, see [Error codes with ErrorDetail
information in Amazon EMR](emr-troubleshoot-error-errordetail.md "emr-troubleshoot-error-errordetail.md"). The `ErrorData` array within `ErrorDetail` returns the following information for this error code:

**`primary-instance-id`**

The ID of the primary instance unable to establish a connection to the configured external Hive Metastore.

**`public-doc`**

The public URL of the documentation for the error code.

## Steps to complete

1. Review the best practices for for configuring an external metastore for Hive.
   See [Configuring an external metastore for Hive](../ReleaseGuide/emr-metastore-external-hive.md "../ReleaseGuide/emr-metastore-external-hive.md").
2. Launch a new cluster with your updated cluster configuration.
