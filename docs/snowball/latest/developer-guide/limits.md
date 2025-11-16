AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# AWS Snowball Edge quotas

Following, you can find information about limitations on using the AWS Snowball Edge device.

###### Important

When you transfer data into Amazon Simple Storage Service (Amazon S3) using a Snowball Edge, keep in mind that
individual Amazon S3 objects can range in size from a minimum of 0 bytes to a maximum of 5
terabytes (TB).

## Region availability for AWS Snowball Edge

The following table highlights the regions where AWS Snowball Edge is available.

| Region                    | Snowball Edge availability |
| ------------------------- | -------------------------- |
| US East (Ohio)            | ✓                          |
| US East (N. Virginia)     | ✓                          |
| US West (N. California)   | ✓                          |
| US West (Oregon)          | ✓                          |
| AWS GovCloud (US-East)    | ✓                          |
| AWS GovCloud (US-West)    | ✓                          |
| Canada (Central)          | ✓                          |
| Asia Pacific (Jakarta)    | ✓                          |
| Asia Pacific (Mumbai)     | ✓                          |
| Asia Pacific (Osaka)      | ✓                          |
| Asia Pacific (Seoul)      | ✓                          |
| Asia Pacific (Singapore)  | ✓                          |
| Asia Pacific (Sydney)     | ✓                          |
| Asia Pacific (Tokyo)      | ✓                          |
| Europe (Frankfurt)        | ✓                          |
| Europe (Ireland)          | ✓                          |
| Europe (London)           | ✓                          |
| Europe (Milan)            | ✓                          |
| Europe (Paris)            | ✓                          |
| Europe (Stockholm)        | ✓                          |
| Middle East (UAE)         | ✓                          |
| South America (São Paulo) | ✓                          |

For information about supported AWS Regions and endpoints,
see [AWS Snowball Edge endpoints and quotas](../../../general/latest/gr/snowball.md "../../../general/latest/gr/snowball.md") in
the AWS General Reference

## Limitations for AWS Snowball Edge jobs

The following limitations exist for creating AWS Snowball Edge device jobs:

- For security purposes, jobs using an AWS Snowball Edge device must be completed within 360 days of being prepared.
  If you need to keep one or more devices for longer than 360 days, see [Updating the SSL certificate on Snowball Edge devices](update-ssl-cert.md "update-ssl-cert.md").
  Otherwise, after 360 days, the device becomes locked, can no longer be accessed, and must be returned.
  If the AWS Snowball Edge device becomes locked during an import job, we can still transfer the existing data on the device into Amazon S3.
- AWS Snowball Edge supports server-side
  encryption with Amazon S3-managed encryption keys (SSE-S3) and server-side encryption
  with AWS Key Management Service managed keys (SSE-KMS). Amazon S3 compatible storage on Snowball Edge supports SSE-C for local compute and storage jobs. For more information, see [Protecting data using
  server-side encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md") in the
  _Amazon Simple Storage Service User Guide_.
- If you're using an AWS Snowball Edge device to import data, and you need to transfer more
  data than will fit on a single Snowball Edge Edge device, create additional jobs.
  Each export job can use multiple Snowball Edge Edge devices.
- The default service limit for the number of Snowball Edge Edge devices you can have
  at one time is 1 per account, per AWS Region. If you want to increase your service limit or create a cluster
  job, contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").
- Metadata for objects transferred to a device is not persisted. The only metadata that remains the same is
  `filename` and `filesize`. All other metadata is set
  as in the following example:

`-rw-rw-r-- 1 root root [filesize] Dec 31 1969
 [path/filename]`

## Rate limits on AWS Snowball Edge

The Rate Limiter is used to control the rate of requests in a server cluster
environment.

### Amazon Snow S3 Adapter connection limit

The maximum connection limit is 1000 for Snowball Edge on Amazon S3. Any connections
beyond 1000 are dropped.

## Limitations on transferring on-premises data with a

Snowball Edge Edge device

The following limitations exist for transferring data to or from an AWS Snowball Edge device
on-premises:

- Files must be in a static state while being written. Files that are modified
  while being transferred are not imported into Amazon S3.
- Jumbo frames are not supported—that is, Ethernet frames with more than
  1500 bytes of payload.
- When selecting what data to export, keep in mind that objects with trailing
  slashes in their names (`/` or `\`) are not transferred.
  Before exporting any objects with trailing slashes, update their names to remove
  the slash.
- When using multipart data transfer, the maximum part size is 2 GiB.

## Limitations on shipping a Snowball Edge Edge device

The following limitations exist for shipping an AWS Snowball Edge device:

- AWS will not ship a Snowball Edge Edge device to a post office
  box.
- AWS will not ship a Snowball Edge Edge device between non-US
  Regions—for example, from EU (Ireland) to EU (Frankfurt), or to Asia Pacific
  (Sydney).
- Moving a Snowball Edge Edge device to an address outside of the country specified
  when the job was created is not allowed and is a violation of the AWS service terms.

For more information about shipping, see [Shipping considerations for Snowball Edge](shipping.md "shipping.md").

## Limitations on processing a returned Snowball Edge Edge

for import

To import your data into AWS, the device must meet the following
requirements:

- The AWS Snowball Edge device must not be compromised. Except for opening the three doors
  on the front, back, and top, or to add and replace the optional air filter,
  don't open the AWS Snowball Edge device for any reason.
- The device must not be physically damaged. You can prevent damage by closing
  the three doors on the Snowball Edge Edge device until the latches make an audible
  clicking sound.
- The E Ink display on the Snowball Edge Edge device must be visible. It must also
  show the return label that was automatically generated when you finished
  transferring your data onto the AWS Snowball Edge device.

###### Note

All Snowball Edge Edge devices returned that don't meet these requirements are erased
without having any work performed on them.
