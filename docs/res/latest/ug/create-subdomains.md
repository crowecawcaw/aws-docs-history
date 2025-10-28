# Creating subdomains

If you are using a custom domain, you will need to set up subdomains to support the web
and VDI portions of your portal.

###### Note

If you are deploying to a GovCloud Region, set up the web application
and VDI subdomains in the commercial partition account hosting the domain public hosted
zone.

1. Open the [Route 53 console](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. Find the domain you created and choose **Create record**.
3. Enter 'web' as the **Record name**.
4. Select **CNAME** as the **Record type**.
5. For **Value**, enter the link you received in the initial email.
6. Choose **Create records**.
7. To create a record for the VDC, retrieve the NLB address.
   1. Open the [AWS CloudFormation
      console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation").
   2. Choose `<environment-name>-vdc`.
   3. Choose **Resources** and open
      `<environmentname>-vdc-external-nlb`.
   4. Copy the DNS name from the NLB.

8. Open the [Route 53 console](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
9. Find your domain and choose **Create record**.
10. Under **Record name**, enter `vdc`.
11. Under **Record type**, select **CNAME**.
12. For the NLB, enter the DNS.
13. Choose **Create record**.
