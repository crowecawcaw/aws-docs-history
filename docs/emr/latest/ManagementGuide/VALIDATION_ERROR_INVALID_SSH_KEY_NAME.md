# VALIDATION_ERROR_INVALID_SSH_KEY_NAME

## Overview

A cluster terminates with a `VALIDATION_ERROR_INVALID_SSH_KEY_NAME`
error when you use an Amazon EC2 key pair that isn't valid to SSH into the primary
instance. The key pair name might be incorrect, or the key pair might not exist
in the requested AWS Region. For more information about key pairs, see [Amazon EC2
key pairs and Linux instances](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md") in the
_Amazon EC2 User Guide_.

## Resolution

To resolve this error, create a new cluster with a valid SSH key pair
name.

To troubleshoot the failed EMR cluster, refer to the `ErrorDetail` information returned from the `DescribeCluster` and `ListClusters` APIs. For more information, see [Error codes with ErrorDetail
information in Amazon EMR](emr-troubleshoot-error-errordetail.md "emr-troubleshoot-error-errordetail.md"). The `ErrorData` array within `ErrorDetail` returns the following information for this error code:

**`ssh-key`**

The SSH key pair name that you provided when you created the
cluster.

**`public-doc`**

The public URL of the documentation for the error code.

## Steps to

complete

Perform the following steps to identify and fix the error:

1. Check your `keypair`.pem file and confirm
   that it matches the name of the SSH key that you see in the Amazon EMR
   console.
2. Navigate to the Amazon EC2 console. Verify that the SSH key name that you
   used is available in the AWS Region that your cluster uses. You can
   find your AWS Region next to your account ID at the top of the
   AWS Management Console.
3. Launch a new cluster with a valid SSH key name.
