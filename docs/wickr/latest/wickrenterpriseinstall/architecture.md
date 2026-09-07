

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html) or [AWS Wickr User Guide](https://docs.aws.amazon.com/wickr/latest/userguide/what-is-wickr.html).

# Architecture
<a name="architecture"></a>

**Recommended Production Architecture**

The diagram below shows Wickr Enterprise configured as recommended for production, with both MySQL and Object Storage services situated outside of the Kubernetes cluster.

![The architecture diagram.](http://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/images/wickr-enterprise-ha.png)


**Internal or Test Architecture**

The diagram below displays the configuration of Wickr Enterprise, utilizing the internal MYSQL and Object Storage services. Although it may satisfy the specific needs of certain deployments, it is not recommended for general production use.

![The architecture diagram.](http://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/images/wickr-enterprise-ha-mysql.png)
