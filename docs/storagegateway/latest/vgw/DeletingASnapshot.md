# Deleting snapshots of your storage volumes

You can delete a snapshot of your storage volume. For example, you might want to do
this if you have taken many snapshots of a storage volume over time and you don't need
the older snapshots. Because snapshots are incremental backups, if you delete a
snapshot, only the data that is not needed in other snapshots is deleted.

###### Topics

- [Deleting Snapshots by Using the AWS
  SDK for Java](#DeletingSnapshotsUsingJava "#DeletingSnapshotsUsingJava")
- [Deleting Snapshots by Using the AWS
  SDK for .NET](#DeletingSnapshotsUsingDotNet "#DeletingSnapshotsUsingDotNet")
- [Deleting Snapshots by Using the
  AWS Tools for Windows PowerShell](#DeletingSnapshotsUsingPowerShell "#DeletingSnapshotsUsingPowerShell")
  On the Amazon EBS console, you can delete snapshots one at a time. For information about
  how to delete snapshots using the Amazon EBS console, see [Deleting an Amazon EBS
  Snapshot](../../../AWSEC2/latest/UserGuide/ebs-deleting-snapshot.md "../../../AWSEC2/latest/UserGuide/ebs-deleting-snapshot.md") in the _Amazon EC2 User Guide._

To delete multiple snapshots at a time, you can use one of the AWS SDKs that
supports Storage Gateway operations. For examples, see [Deleting Snapshots by Using the AWS
SDK for Java](#DeletingSnapshotsUsingJava "#DeletingSnapshotsUsingJava"),
[Deleting Snapshots by Using the AWS
SDK for .NET](#DeletingSnapshotsUsingDotNet "#DeletingSnapshotsUsingDotNet"), and [Deleting Snapshots by Using the
AWS Tools for Windows PowerShell](#DeletingSnapshotsUsingPowerShell "#DeletingSnapshotsUsingPowerShell").

## Deleting Snapshots by Using the AWS

SDK for Java

To delete many snapshots associated with a volume, you can use a programmatic
approach. The example following demonstrates how to delete snapshots using the AWS
SDK for Java. To use the example code, you should be familiar with running a Java
console application. For more information, see [Getting
Started](../../../AWSSdkDocsJava/latest/DeveloperGuide/java-dg-setup.md "../../../AWSSdkDocsJava/latest/DeveloperGuide/java-dg-setup.md") in the _AWS SDK for Java Developer Guide_.
If you need to just delete a few snapshots, use the console as described in [Deleting snapshots of your storage volumes](DeletingASnapshot.md "DeletingASnapshot.md").

###### Example : Deleting Snapshots by Using the AWS SDK for Java

The following Java code example lists the snapshots for each volume of a
gateway and whether the snapshot start time is before or after a specified date.
It uses the AWS SDK for Java API for Storage Gateway and Amazon EC2. The Amazon EC2 API includes
operations for working with snapshots.

Update the code to provide the service endpoint, your gateway Amazon Resource
Name (ARN), and the number of days back you want to save snapshots. Snapshots
taken before this cutoff are deleted. You also need to specify the Boolean value
`viewOnly`, which indicates whether you want to view the
snapshots to be deleted or to actually perform the snapshot deletions. Run the
code first with just the view option (that is, with `viewOnly` set to
`true`) to see what the code deletes. For a list of AWS service
endpoints you can use with Storage Gateway, see [AWS Storage Gateway Endpoints and Quotas](../../../general/latest/gr/sg.md "../../../general/latest/gr/sg.md") in
the _AWS General Reference_.

```
import java.io.IOException;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Collection;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.List;

import com.amazonaws.auth.PropertiesCredentials;
import com.amazonaws.services.ec2.AmazonEC2Client;
import com.amazonaws.services.ec2.model.DeleteSnapshotRequest;
import com.amazonaws.services.ec2.model.DescribeSnapshotsRequest;
import com.amazonaws.services.ec2.model.DescribeSnapshotsResult;
import com.amazonaws.services.ec2.model.Filter;
import com.amazonaws.services.ec2.model.Snapshot;
import com.amazonaws.services.storagegateway.AWSStorageGatewayClient;
import com.amazonaws.services.storagegateway.model.ListVolumesRequest;
import com.amazonaws.services.storagegateway.model.ListVolumesResult;
import com.amazonaws.services.storagegateway.model.VolumeInfo;

public class ListDeleteVolumeSnapshotsExample {

    public static AWSStorageGatewayClient sgClient;
    public static AmazonEC2Client ec2Client;
    static String serviceURLSG = "https://storagegateway.us-east-1.amazonaws.com";
    static String serviceURLEC2 = "https://ec2.us-east-1.amazonaws.com";

    // The gatewayARN
    public static String gatewayARN = "*** provide gateway ARN ***";

    // The number of days back you want to save snapshots. Snapshots before this cutoff are deleted
    // if viewOnly = false.
    public static int daysBack = 10;

    // true = show what will be deleted; false = actually delete snapshots that meet the daysBack criteria
    public static boolean viewOnly = true;

    public static void main(String[] args) throws IOException {

        // Create a Storage Gateway and amazon ec2 client
        sgClient = new AWSStorageGatewayClient(new PropertiesCredentials(
                ListDeleteVolumeSnapshotsExample.class.getResourceAsStream("AwsCredentials.properties")));
        sgClient.setEndpoint(serviceURLSG);

        ec2Client = new AmazonEC2Client(new PropertiesCredentials(
                ListDeleteVolumeSnapshotsExample.class.getResourceAsStream("AwsCredentials.properties")));
        ec2Client.setEndpoint(serviceURLEC2);

        List<VolumeInfo> volumes = ListVolumesForGateway();
        DeleteSnapshotsForVolumes(volumes, daysBack);

    }
    public static List<VolumeInfo> ListVolumesForGateway()
    {
        List<VolumeInfo> volumes = new ArrayList<VolumeInfo>();

        String marker = null;
        do {
            ListVolumesRequest request = new ListVolumesRequest().withGatewayARN(gatewayARN);
            ListVolumesResult result = sgClient.listVolumes(request);
            marker = result.getMarker();

            for (VolumeInfo vi : result.getVolumeInfos())
            {
                volumes.add(vi);
                System.out.println(OutputVolumeInfo(vi));
            }
        } while (marker != null);

        return volumes;
    }
    private static void DeleteSnapshotsForVolumes(List<VolumeInfo> volumes,
            int daysBack2) {

        // Find snapshots and delete for each volume
        for (VolumeInfo vi : volumes) {

            String volumeARN = vi.getVolumeARN();
            String volumeId = volumeARN.substring(volumeARN.lastIndexOf("/")+1).toLowerCase();
            Collection<Filter> filters = new ArrayList<Filter>();
            Filter filter = new Filter().withName("volume-id").withValues(volumeId);
            filters.add(filter);

            DescribeSnapshotsRequest describeSnapshotsRequest =
                new DescribeSnapshotsRequest().withFilters(filters);
            DescribeSnapshotsResult describeSnapshotsResult =
                ec2Client.describeSnapshots(describeSnapshotsRequest);

            List<Snapshot> snapshots = describeSnapshotsResult.getSnapshots();
            System.out.println("volume-id = " + volumeId);
            for (Snapshot s : snapshots){
                StringBuilder sb = new StringBuilder();
                boolean meetsCriteria = !CompareDates(daysBack, s.getStartTime());
                sb.append(s.getSnapshotId() + ", " + s.getStartTime().toString());
                sb.append(", meets criteria for delete? " + meetsCriteria);
                sb.append(", deleted? ");
                if (!viewOnly & meetsCriteria) {
                    sb.append("yes");
                    DeleteSnapshotRequest deleteSnapshotRequest =
                        new DeleteSnapshotRequest().withSnapshotId(s.getSnapshotId());
                    ec2Client.deleteSnapshot(deleteSnapshotRequest);
                }
                else {
                    sb.append("no");
                }
                System.out.println(sb.toString());
            }
        }
    }

    private static String OutputVolumeInfo(VolumeInfo vi) {

        String volumeInfo = String.format(
                 "Volume Info:\n" +
                 "  ARN: %s\n" +
                 "  Type: %s\n",
                 vi.getVolumeARN(),
                 vi.getVolumeType());
        return volumeInfo;
     }

    // Returns the date in two formats as a list
    public static boolean CompareDates(int daysBack, Date snapshotDate) {
        Date today = new Date();
        Calendar cal = new GregorianCalendar();
        cal.setTime(today);
        cal.add(Calendar.DAY_OF_MONTH, -daysBack);
        Date cutoffDate = cal.getTime();
        return (snapshotDate.compareTo(cutoffDate) > 0) ? true : false;
    }

}

```

## Deleting Snapshots by Using the AWS

SDK for .NET

To delete many snapshots associated with a volume, you can use a programmatic
approach. The following example demonstrates how to delete snapshots using the AWS
SDK for .NET version 2 and 3. To use the example code, you should be familiar with
running a .NET console application. For more information, see [Getting Started](../../../sdk-for-net/v4/developer-guide/net-dg-config.md "../../../sdk-for-net/v4/developer-guide/net-dg-config.md") in the _AWS SDK for .NET Developer
Guide_. If you need to just delete a few snapshots, use the console as
described in [Deleting snapshots of your storage volumes](DeletingASnapshot.md "DeletingASnapshot.md").

###### Example : Deleting Snapshots by Using the AWS SDK for .NET

In the following C# code example, an AWS Identity and Access Management user can list the snapshots for
each volume of a gateway. The user can then determine whether the snapshot start
time is before or after a specified date (retention period) and delete snapshots
that have passed the retention period. The example uses the AWS SDK for .NET
API for Storage Gateway and Amazon EC2. The Amazon EC2 API includes operations for working with
snapshots.

The following code example uses the AWS SDK for .NET version 2 and 3. You
can migrate older versions of .NET to the newer version. For more information,
see [Migrating your
project for the AWS SDK for .NET](../../../sdk-for-net/v4/developer-guide/net-dg-migrating.md "../../../sdk-for-net/v4/developer-guide/net-dg-migrating.md").

Update the code to provide the service endpoint, your gateway Amazon Resource
Name (ARN), and the number of days back you want to save snapshots. Snapshots
taken before this cutoff are deleted. You also need to specify the Boolean value
`viewOnly`, which indicates whether you want to view the
snapshots to be deleted or to actually perform the snapshot deletions. Run the
code first with just the view option (that is, with `viewOnly` set to
`true`) to see what the code deletes. For a list of AWS service
endpoints you can use with Storage Gateway, see [AWS Storage Gateway Endpoints and Quotas](../../../general/latest/gr/sg.md "../../../general/latest/gr/sg.md") in
the _AWS General Reference_.

First, you create an user and attach the minimum IAM policy to the user. Then
you schedule automated snapshots for your gateway.

The following code creates the minimum policy that allows an user to delete
snapshots. In this example, the policy is named
`sgw-delete-snapshot`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "StmtEC2Snapshots",
 "Effect": "Allow",
 "Action": [
 "ec2:DeleteSnapshot",
 "ec2:DescribeSnapshots"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "StmtSgwListVolumes",
 "Effect": "Allow",
 "Action": [
 "storagegateway:ListVolumes"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
 }`

```

The following C# code finds all snapshots in the specified gateway that match
the volumes and the specified cut-off period and then deletes them.

```
using System;
using System.Collections.Generic;
using System.Text;
using Amazon.EC2;
using Amazon.EC2.Model;
using Amazon.StorageGateway.Model;
using Amazon.StorageGateway;

namespace DeleteStorageGatewaySnapshotNS
{
    class Program
    {
        /*
         * Replace the variables below to match your environment.
         */

         /* IAM AccessKey */
        static String AwsAccessKey = "AKIA................";

        /* IAM SecretKey */
        static String AwsSecretKey = "*******************************";

        /* Account number, 12 digits, no hyphen */
        static String OwnerID = "123456789012";

        /* Your Gateway ARN. Use a Storage Gateway ID, sgw-XXXXXXXX* */
        static String GatewayARN = "arn:aws:storagegateway:ap-southeast-2:123456789012:gateway/sgw-XXXXXXXX";

        /* Snapshot status: "completed", "pending", "error" */
        static String SnapshotStatus = "completed";

        /* Region where your gateway is activated */
        static String AwsRegion = "ap-southeast-2";

        /* Minimum age of snapshots before they are deleted (retention policy) */
        static int daysBack = 30;

        /*
         * Do not modify the four lines below.
         */
        static AmazonEC2Config ec2Config;
        static AmazonEC2Client ec2Client;
        static AmazonStorageGatewayClient sgClient;
        static AmazonStorageGatewayConfig sgConfig;

        static void Main(string[] args)
        {
            // Create an EC2 client.
            ec2Config = new AmazonEC2Config();
            ec2Config.ServiceURL = "https://ec2." + AwsRegion + ".amazonaws.com";
            ec2Client = new AmazonEC2Client(AwsAccessKey, AwsSecretKey, ec2Config);

            // Create a Storage Gateway client.
            sgConfig = new AmazonStorageGatewayConfig();
            sgConfig.ServiceURL = "https://storagegateway." + AwsRegion + ".amazonaws.com";
            sgClient = new AmazonStorageGatewayClient(AwsAccessKey, AwsSecretKey, sgConfig);

            List<VolumeInfo> StorageGatewayVolumes = ListVolumesForGateway();
            List<Snapshot> StorageGatewaySnapshots = ListSnapshotsForVolumes(StorageGatewayVolumes,
                                                     daysBack);
            DeleteSnapshots(StorageGatewaySnapshots);
        }

        /*
         * List all volumes for your gateway
         * returns: A list of VolumeInfos, or null.
         */
        private static List<VolumeInfo> ListVolumesForGateway()
        {
            ListVolumesResponse response = new ListVolumesResponse();
            try
            {
                ListVolumesRequest request = new ListVolumesRequest();
                request.GatewayARN = GatewayARN;
                response = sgClient.ListVolumes(request);

                foreach (VolumeInfo vi in response.VolumeInfos)
                {
                    Console.WriteLine(OutputVolumeInfo(vi));
                }
            }
            catch (AmazonStorageGatewayException ex)
            {
                Console.WriteLine(ex.Message);
            }
            return response.VolumeInfos;
        }

        /*
         * Gets the list of snapshots that match the requested volumes
         * and cutoff period.
         */
        private static List<Snapshot> ListSnapshotsForVolumes(List<VolumeInfo> volumes, int snapshotAge)
        {
            List<Snapshot> SelectedSnapshots = new List<Snapshot>();
            try
            {
                foreach (VolumeInfo vi in volumes)
                {
                    String volumeARN = vi.VolumeARN;
                    String volumeID = volumeARN.Substring(volumeARN.LastIndexOf("/") + 1).ToLower();

                    DescribeSnapshotsRequest describeSnapshotsRequest = new DescribeSnapshotsRequest();

                    Filter ownerFilter = new Filter();
                    List<String> ownerValues = new List<String>();
                    ownerValues.Add(OwnerID);
                    ownerFilter.Name = "owner-id";
                    ownerFilter.Values = ownerValues;
                    describeSnapshotsRequest.Filters.Add(ownerFilter);

                    Filter statusFilter = new Filter();
                    List<String> statusValues = new List<String>();
                    statusValues.Add(SnapshotStatus);
                    statusFilter.Name = "status";
                    statusFilter.Values = statusValues;
                    describeSnapshotsRequest.Filters.Add(statusFilter);

                    Filter volumeFilter = new Filter();
                    List<String> volumeValues = new List<String>();
                    volumeValues.Add(volumeID);
                    volumeFilter.Name = "volume-id";
                    volumeFilter.Values = volumeValues;
                    describeSnapshotsRequest.Filters.Add(volumeFilter);

                    DescribeSnapshotsResponse describeSnapshotsResponse =
                      ec2Client.DescribeSnapshots(describeSnapshotsRequest);

                    List<Snapshot> snapshots = describeSnapshotsResponse.Snapshots;
                    Console.WriteLine("volume-id = " + volumeID);
                    foreach (Snapshot s in snapshots)
                    {
                        if (IsSnapshotPastRetentionPeriod(snapshotAge, s.StartTime))
                        {
                            Console.WriteLine(s.SnapshotId + ", " + s.VolumeId + ",
                               " + s.StartTime + ", " + s.Description);
                            SelectedSnapshots.Add(s);
                        }
                    }
                }
            }
            catch (AmazonEC2Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            return SelectedSnapshots;
        }

        /*
         * Deletes a list of snapshots.
         */
        private static void DeleteSnapshots(List<Snapshot> snapshots)
        {
            try
            {
                foreach (Snapshot s in snapshots)
                {

                    DeleteSnapshotRequest deleteSnapshotRequest = new DeleteSnapshotRequest(s.SnapshotId);
                    DeleteSnapshotResponse response = ec2Client.DeleteSnapshot(deleteSnapshotRequest);
                    Console.WriteLine("Volume: " +
                              s.VolumeId +
                              " => Snapshot: " +
                              s.SnapshotId +
                              " Response: "
                              + response.HttpStatusCode.ToString());
                }
            }
            catch (AmazonEC2Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }

        /*
         * Checks if the snapshot creation date is past the retention period.
         */
        private static Boolean IsSnapshotPastRetentionPeriod(int daysBack, DateTime snapshotDate)
        {
            DateTime cutoffDate = DateTime.Now.Add(new TimeSpan(-daysBack, 0, 0, 0));
            return (DateTime.Compare(snapshotDate, cutoffDate) < 0) ? true : false;
        }

        /*
         * Displays information related to a volume.
         */
        private static String OutputVolumeInfo(VolumeInfo vi)
        {
            String volumeInfo = String.Format(
                "Volume Info:\n" +
                "  ARN: {0}\n" +
                "  Type: {1}\n",
                vi.VolumeARN,
                vi.VolumeType);
            return volumeInfo;
        }
    }
}
```

## Deleting Snapshots by Using the

AWS Tools for Windows PowerShell

To delete many snapshots associated with a volume, you can use a programmatic
approach. The example following demonstrates how to delete snapshots using the
AWS Tools for Windows PowerShell. To use the example script, you should be familiar with running a
PowerShell script. For more information, see [Getting
Started](../../../powershell/latest/userguide/pstools-getting-started.md "../../../powershell/latest/userguide/pstools-getting-started.md") in the _AWS Tools for Windows PowerShell_. If you need to delete
just a few snapshots, use the console as described in [Deleting snapshots of your storage volumes](DeletingASnapshot.md "DeletingASnapshot.md").

###### Example : Deleting Snapshots by Using the AWS Tools for Windows PowerShell

The following PowerShell script example lists the snapshots for each volume of
a gateway and whether the snapshot start time is before or after a specified
date. It uses the AWS Tools for Windows PowerShell cmdlets for Storage Gateway and Amazon EC2. The Amazon EC2 API
includes operations for working with snapshots.

You need to update the script and provide your gateway Amazon Resource Name
(ARN) and the number of days back you want to save snapshots. Snapshots taken
before this cutoff are deleted. You also need to specify the Boolean value
`viewOnly`, which indicates whether you want to view the
snapshots to be deleted or to actually perform the snapshot deletions. Run the
code first with just the view option (that is, with `viewOnly` set to
`true`) to see what the code deletes.

```
<#
.DESCRIPTION
    Delete snapshots of a specified volume that match given criteria.

.NOTES
    PREREQUISITES:
    1) AWS Tools for Windows PowerShell from https://aws.amazon.com/powershell/
    2) Credentials and AWS Region stored in session using Initialize-AWSDefault.
    For more info see, https://docs.aws.amazon.com/powershell/latest/userguide/specifying-your-aws-credentials.html

.EXAMPLE
    powershell.exe .\SG_DeleteSnapshots.ps1
#>

# Criteria to use to filter the results returned.
$daysBack = 18
$gatewayARN = "*** provide gateway ARN ***"
$viewOnly = $true;

#ListVolumes
$volumesResult = Get-SGVolume -GatewayARN $gatewayARN
$volumes = $volumesResult.VolumeInfos
Write-Output("`nVolume List")
foreach ($volumes in $volumesResult)
  { Write-Output("`nVolume Info:")
    Write-Output("ARN:  " + $volumes.VolumeARN)
    write-Output("Type: " + $volumes.VolumeType)
  }

Write-Output("`nWhich snapshots meet the criteria?")
foreach ($volume in $volumesResult)
  {
    $volumeARN = $volume.VolumeARN

    $volumeId = ($volumeARN-split"/")[3].ToLower()

    $filter = New-Object Amazon.EC2.Model.Filter
    $filter.Name = "volume-id"
    $filter.Value.Add($volumeId)

    $snapshots = get-EC2Snapshot -Filter $filter
    Write-Output("`nFor volume-id = " + $volumeId)
    foreach ($s in $snapshots)
    {
       $d = ([DateTime]::Now).AddDays(-$daysBack)
       $meetsCriteria = $false
       if ([DateTime]::Compare($d, $s.StartTime) -gt 0)
       {
            $meetsCriteria = $true
       }

       $sb = $s.SnapshotId + ", " + $s.StartTime + ", meets criteria for delete? " + $meetsCriteria
       if (!$viewOnly -AND $meetsCriteria)
       {
           $resp = Remove-EC2Snapshot -SnapshotId $s.SnapshotId
           #Can get RequestId from response for troubleshooting.
           $sb = $sb + ", deleted? yes"
       }
       else {
           $sb = $sb + ", deleted? no"
       }
       Write-Output($sb)
    }
  }
```
