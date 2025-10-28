For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# AWS account federation in

Okta

The Timestream for LiveAnalytics JDBC driver supports AWS Account Federation in Okta. To set up AWS Account
Federation in Okta, complete the following steps:

1. Sign in to the Okta Admin dashboard using the following URL:

```
https://<company-domain-name>-admin.okta.com/admin/apps/active
```

###### Note

Replace **<company-domain-name>** with
your domain name. 2. Upon successful sign-in, choose **Add Application** and
search for **AWS Account Federation**. 3. Choose **Add** 4. Change the Login URL to the appropriate URL. 5. Choose **Next** 6. Choose **SAML 2.0** As the **Sign-On**
method 7. Choose **Identity Provider metadata** to open the
metadata XML file. Save the file locally. 8. Leave all other configuration options blank. 9. Choose **Done**
Now that you have completed AWS Account Federation in Okta, you may proceed to
[Setting up Okta for SAML](aws-setting-up-okta-for-saml.md "aws-setting-up-okta-for-saml.md").
