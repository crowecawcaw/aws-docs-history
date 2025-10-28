# Export route tables to Amazon S3 in AWS Transit Gateway

You can export the routes in your transit gateway route tables to an Amazon S3 bucket. The
routes are saved to the specified Amazon S3 bucket in a JSON file.

###### To export transit gateway route tables using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit Gateway Route
   Tables**.
3. Choose the route table that includes the routes to export.
4. Choose **Actions**, **Export routes**.
5. On the **Export routes** page, for **S3 bucket
   name**, type the name of the S3 bucket.
6. To filter the routes exported, specify filter parameters in the
   **Filters** section of the page.
7. Choose **Export routes**.
   To access the exported routes, open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/"), and navigate
   to the bucket that you specified. The file name includes the AWS account ID, AWS
   Region, route table ID, and a timestamp. Select the file and choose
   **Download**. The following is an example of a JSON file that
   contains information about two propagated routes for VPC attachments.

```
{
  "filter": [
    {
      "name": "route-search.subnet-of-match",
      "values": [
        "0.0.0.0/0",
        "::/0"
      ]
    }
  ],
  "routes": [
    {
      "destinationCidrBlock": "10.0.0.0/16",
      "transitGatewayAttachments": [
        {
          "resourceId": "vpc-0123456abcd123456",
          "transitGatewayAttachmentId": "tgw-attach-1122334455aabbcc1",
          "resourceType": "vpc"
        }
      ],
      "type": "propagated",
      "state": "active"
    },
    {
      "destinationCidrBlock": "10.2.0.0/16",
      "transitGatewayAttachments": [
        {
          "resourceId": "vpc-abcabc123123abca",
          "transitGatewayAttachmentId": "tgw-attach-6677889900aabbcc7",
          "resourceType": "vpc"
        }
      ],
      "type": "propagated",
      "state": "active"
    }
  ]
}
```
