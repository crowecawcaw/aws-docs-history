# Amazon Application Recovery Controller (ARC) in AWS GovCloud (US)

You can use ARC zonal shift to quickly isolate and recover from single Availability Zone (AZ) impairments.
Zonal shift temporarily shifts traffic for a supported resource away from an impaired AZ to healthy AZs in the same AWS Region.
Starting a zonal shift helps your application recover quickly, for example, from a developer's bad code deployment or from an AWS impairment in a single AZ.
Shifting traffic away from the impaired AZ reduces the impact for clients who are using your application in the impaired AZ.

You can start a zonal shift for any supported resource in your account in an AWS Region. Zonal shifts are manual and temporary. When you start a zonal shift, you must specify an (extendable) expiration of up to three days.

## How Amazon Application Recovery Controller (ARC) differs for

AWS GovCloud (US)

The AWS GovCloud (US-West) implementation of ARC is unique in the following way:

- The Region switch, routing control, and readiness check features of the ARC service are not available in AWS GovCloud (US-West).

## Documentation for Amazon Application Recovery Controller (ARC)

[Amazon Application Recovery Controller (ARC) Developer Guide﻿](../../../r53recovery/latest/dg/what-is-route53-recovery.md "../../../r53recovery/latest/dg/what-is-route53-recovery.md")

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- All customer parameters provided as input to ARC through the console, APIs, or other mechanisms, are not
  permitted to contain export-controlled data. Examples include comments entered by the user, and the resource name and Amazon
  Resource Name (ARN) for registered resources.
