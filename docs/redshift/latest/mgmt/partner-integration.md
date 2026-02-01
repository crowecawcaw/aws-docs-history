Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Integrate Amazon Redshift with an AWS Partner

By working with Amazon Redshift, you can integrate with AWS Partners on the Amazon Redshift console. From
the **Cluster details** page, you can speed up your data onboarding into
your Amazon Redshift data warehouse with AWS Partner applications. You can also join and analyze data
from different sources together with existing data in your cluster. Before completing
integration with Informatica, you must add the partner's IP addresses to the allowlist of
inbound traffic. The following AWS Partners can integrate with Amazon Redshift:

- [Datacoral](https://www.datacoral.com/aws-partnership/ "https://www.datacoral.com/aws-partnership/")
- [Etleap](https://etleap.com/aws "https://etleap.com/aws")
- [Fivetran](https://fivetran.com/partners/aws "https://fivetran.com/partners/aws")
- [SnapLogic](https://www.snaplogic.com/partners/amazon-web-services "https://www.snaplogic.com/partners/amazon-web-services")
- [Stitch](https://www.stitchdata.com/data-warehouses/amazon-redshift/ "https://www.stitchdata.com/data-warehouses/amazon-redshift/")
- [Upsolver](https://www.upsolver.com/integrations/redshift "https://www.upsolver.com/integrations/redshift")
- [Matillion (preview)](https://www.matillion.com/technology/cloud-data-warehouse/amazon-redshift/ "https://www.matillion.com/technology/cloud-data-warehouse/amazon-redshift/")
- [Sisense (preview)](https://www.sisense.com/ "https://www.sisense.com/")
- [Thoughtspot](https://www.thoughtspot.com/partners/aws "https://www.thoughtspot.com/partners/aws")
  AWS Partners can integrate with Amazon Redshift using the AWS CLI or Amazon Redshift API operations. For more
  information, see the _AWS CLI Command Reference_ or the
  _Amazon Redshift API Reference_.

Use the following procedure to integrate a cluster with an AWS Partner.

###### To integrate an Amazon Redshift cluster with an AWS Partner

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**.
3. Choose the cluster that you want to integrate.
4. Choose **Add partner integration**. The **Choose
   partner** page opens with details about the available AWS Partners.
5. Choose an AWS Partner, then choose **Next**.

More details about the chosen AWS Partner appear, along with details about the
cluster that you are integrating. The **Cluster details** section
includes information that you provide on the AWS Partner website such as the
**Cluster identifier**, **Endpoint**,
**Database name**, and **User name** (which is
a database user name). This information is sent to the partner that you chose. 6. Choose **Add partner** to open the AWS Partner's
website. 7. Configure the integration with your Amazon Redshift cluster on the partner's website. On the
partner's website, you can select and configure the data sources that are loaded to
your Amazon Redshift cluster. You can also define additional extract, load, and transform (ELT)
transformations to process your business data, join it with other datasets, and
build consolidated views for analysis and reporting.
You can view and manage AWS Partner integrations from the cluster details
**Properties** tab. The **Integrations** section lists
the **Partner** name that you can use to link to the AWS Partner website,
the **Status** of the integration, the **Database** that
receives the data, and the **Last successful connection** that might have
updated the cluster.

The possible status values are as follows:

- Active – The AWS Partner can connect to the cluster and complete
  configured tasks.
- Inactive – The AWS Partner integration doesn't exist.
- Runtime failure – The AWS Partner can connect to the cluster but
  can't complete configured tasks.
- Connection failure – The AWS Partner can't connect to the cluster.
  After you delete an AWS Partner integration from Amazon Redshift, data continues to flow into your
  cluster. Complete the delete on the partner's website.
