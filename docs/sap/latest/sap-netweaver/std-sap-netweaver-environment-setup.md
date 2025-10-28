# SAP NetWeaver Environment Setup for Linux on AWS

_SAP specialists, Amazon Web Services_

_Last updated: August 2022_

This guide describes the prerequisites and procedures for setting up an environment on Amazon Web Services prior to installing and running SAP NetWeaver for Linux in the AWS Cloud.

This guide is intended for SAP architects, SAP engineers, IT architects, and IT administrators who want to deploy SAP NetWeaver on AWS.

## About this Guide

This guide is part of a content series that provides detailed information about hosting, configuring, and using SAP technologies in the AWS Cloud. For the other guides in the series, ranging from overviews to advanced topics, see the [SAP on AWS Technical Documentation home page](https://aws.amazon.com/sap/docs/ "https://aws.amazon.com/sap/docs/").

## Overview

Amazon Web Services provides various services and tools for deploying SAP products on the AWS Cloud platform. This guide discusses the steps required to use the AWS Command Line Interface (AWS CLI) and Linux commands to set up and configure AWS resources such as Amazon Elastic Compute Cloud (Amazon EC2) instances, Amazon Elastic File System (Amazon EFS), and Amazon Elastic Block Store (Amazon EBS) volumes to install a new SAP instance.

The guide also explains how to configure the SLES or RHEL operating systems for new SAP NetWeaver installations. By the end of this document, you will have the AWS infrastructure ready to install an SAP NetWeaver instance.

## Costs and Licenses

You are responsible for all costs related to your use of any AWS services while following this guide. Prices are subject to change. For full details, see the pricing pages for the AWS services that you intend to use.

You must already own a license for the SAP software and have access to download the SAP software from the SAP Software Download Center (requires access to [SAP Support](https://support.sap.com/en/index.html "https://support.sap.com/en/index.html")).
