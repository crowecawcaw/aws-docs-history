

# Creating subdomains
<a name="create-subdomains"></a>

If you are using a custom domain, you will need to set up subdomains to support the web and VDI portions of your portal.

**Note**  
If you are deploying to a GovCloud Region, set up the web application and VDI subdomains in the commercial partition account hosting the domain public hosted zone.

1. Open the [Route 53 console](https://console.aws.amazon.com/route53/).

1. Find the domain you created and choose **Create record**.

1. Enter 'web' as the **Record name**.

1. Select **CNAME** as the **Record type**.

1. For **Value**, enter the link you received in the initial email.

1. Choose **Create records**. 

1. To create a record for the VDC, retrieve the NLB address.

   1. Open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation).

   1. Choose `<environment-name>-vdc`.

   1. Choose **Resources** and open `<environmentname>-vdc-external-nlb`.

   1. Copy the DNS name from the NLB.

1. Open the [Route 53 console](https://console.aws.amazon.com/route53/).

1. Find your domain and choose **Create record**.

1. Under **Record name**, enter `vdc`.

1. Under **Record type**, select **CNAME**.

1. For the NLB, enter the DNS.

1. Choose **Create record**.