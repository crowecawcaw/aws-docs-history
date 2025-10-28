AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Tutorial: Getting started with

AWS Mainframe Modernization File Transfer

AWS Mainframe Modernization File Transfer lets you transfer and convert mainframe data sets for mainframe modernization,
migration, and augmentation use cases.

Follow the steps in this tutorial to understand how AWS Mainframe Modernization File Transfer works.

## Overview

File Transfer consists of the following:

1. An agent to be installed on the source mainframe.
2. Access to dataset discovery, transfer, and conversion capabilities directly from the AWS Mainframe Modernization
   management service console.

As a user, you can transfer datasets from the mainframe to your Amazon S3 bucket.

###### Topics

- [Step 1: Transfer the agent binaries tar package
  from AWS to the mainframe logical partition](#filetransfer-agent-binaries "#filetransfer-agent-binaries")
- [Step 2: Configure the File Transfer agent on the source
  mainframe](#filetransfer-configure "#filetransfer-configure")
- [Step 3: Create a data transfer
  endpoint](#filetransfer-data-transfer-endpoint "#filetransfer-data-transfer-endpoint")
- [Step 4: Create a transfer task](#filetransfer-create-transfer-tasks "#filetransfer-create-transfer-tasks")
- [Step 5: View transfer task progress](#view-transfer-tasks "#view-transfer-tasks")

## Step 1: Transfer the agent binaries tar package

from AWS to the mainframe logical partition

Download tar files from the [M2-agent tar](https://drm0z31ua8gi7.cloudfront.net/filetransfer/m2-agent-v1.0.0.tar "https://drm0z31ua8gi7.cloudfront.net/filetransfer/m2-agent-v1.0.0.tar")
link.

## Step 2: Configure the File Transfer agent on the source

mainframe

In this step, you configure and start the AWS Mainframe Modernization File Transfer agent on the source mainframe.
The agent is required to facilitate communications between the File Transfer service feature and the source mainframe.
At least one agent is required per mainframe. More than one agent can be started for high availability and enhanced scalability.

Follow the instructions in [Configure a File Transfer agent](m2-agent-configuration.md "m2-agent-configuration.md") guide to complete File Transfer
agent installation on the mainframe.

## Step 3: Create a data transfer

endpoint

Follow steps on [Create data transfer endpoints for
File Transfer](filetransfer-data-transfer-endpoints.md "filetransfer-data-transfer-endpoints.md") page to create a new
data transfer endpoint.

## Step 4: Create a transfer task

Follow steps on [Create transfer tasks in File Transfer](filetransfer-transfer-tasks.md "filetransfer-transfer-tasks.md") page to create and manage your
transfer tasks.

## Step 5: View transfer task progress

You can view your transfer task's progress in the AWS Mainframe Modernization console. For more details, refer [View transfer tasks](filetransfer-transfer-tasks.md#filetransfer-console-view-task "filetransfer-transfer-tasks.md#filetransfer-console-view-task") section.
