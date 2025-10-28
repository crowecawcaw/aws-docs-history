Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Returning the Snowball Edge device

After you are finished using the Snowball Edge and have powered
it off, a shipping carrier will return it to AWS. The carrier automatically provides a
tracking number for the shipment of the device. The tracking number appears in the
AWS Snow Family Management Console. You can access the tracking number and a link to the carrier's tracking
website by viewing the job's status details in the console. For more information, see
[Return shipping for
Snowball Edge devices](mailing-storage.md "mailing-storage.md").

The carrier delivers the device to an AWS sorting
facility and the device is forwarded to the AWS data center. At the data
center, AWS will ensure the device has not been tampered with during shipping and that
the device is healthy. If the device contains data to import into Amazon S3, AWS will begin
importing it. Otherwise, the data on the device will be securely erased. You can track
the status changes as AWS processes the device in the AWS Snow Family Management Console. You will receive
Amazon SNS notifications of status changes if you selected that option when you created the
job to order the device. For more information, see [Monitoring the Import
Status](monitor-status.md "monitor-status.md").

The final status values include when the AWS Snowball Edge device has been received by AWS, when data import begins, and when the job is completed.

###### Note

If the device contains data you intended to import into Amazon S3 and you do not want
the data on the device to be imported, contact Support to request to cancel the Snow
job. If you cancel the job, we will skip the data transfer and securely erase the
device following the established processes. We are not able to hold a device
containing your data at our facilities due to our strict chain of custody and
operating procedures.

###### To prepare an AWS Snowball Edge device for return shipping

1. Power off the device. For more information, see [Powering off the Snowball Edge](turnitoff.md "turnitoff.md").
2. Disconnect any network cables connected to the device.
3. Disconnect the power cable. Stow it in the cable nook on top of the
   AWS Snowball Edge device.
4. Close the doors on the back, top, and front of the AWS Snowball Edge device. Press each
   door in until you hear and feel a click.
   **Next:**
   [Return shipping for Snowball Edge](mailing-storage.md "mailing-storage.md")
