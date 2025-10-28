# Switch from a custom SSL/TLS

certificate with dedicated IP addresses to SNI

If you configured CloudFront to use a custom SSL/TLS certificate with dedicated IP addresses, you
can switch to using a custom SSL/TLS certificate with SNI instead and eliminate the
charge that is associated with dedicated IP addresses.

###### Important

This update to your CloudFront configuration has no effect on viewers that support SNI. Viewers
can access your content before and after the change, as well as while the change
is propagating to CloudFront edge locations. Viewers that don't support SNI can't
access your content after the change. For more information, see [Choose how CloudFront serves HTTPS
requests](cnames-https-dedicated-ip-or-sni.md "cnames-https-dedicated-ip-or-sni.md").

## Switch from a custom certificate to SNI

The following procedure shows you how to switch from a custom SSL/TLS certificate with dedicated IP addresses to SNI.

###### To switch from a

custom SSL/TLS certificate with dedicated IP addresses to SNI

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Choose the ID of the distribution that you want to view or update.
3. Choose **Distribution Settings**.
4. On the **General** tab, choose
   **Edit**.
5. Under **Custom SSL certification –
   _optional_**, deselect **Legacy clients support**.
6. Choose **Yes, Edit**.
