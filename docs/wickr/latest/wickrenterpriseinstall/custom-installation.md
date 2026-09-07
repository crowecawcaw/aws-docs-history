

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html) or [AWS Wickr User Guide](https://docs.aws.amazon.com/wickr/latest/userguide/what-is-wickr.html).

# Custom installation
<a name="custom-installation"></a>

In the **Custom installation** section, you will learn how to install Wickr Enterprise.

**Topics**
+ [Requirements](requirements.md)
+ [Architecture](architecture.md)
+ [Installation](installation.md)
+ [Ingress settings](ingress-settings.md)
+ [Database settings](database-settings.md)
+ [S3 File storage](s3-file-storage.md)
+ [Persistent volume claim settings](persistent-volume-claim-settings.md)
+ [TLS certificate settings](tls-certificate-settings.md)
+ [Calling settings](calling-settings.md)
+ [Calling ingress settings](calling-ingress-settings.md)
+ [Kubernetes cluster autoscaler (optional)](kubernetes-cluster-autoscaler.md)
+ [Backups](backups.md)
+ [Airgap installation](airgap-installation.md)
+ [Wickr admin console](#wickr-admin-console)
+ [Security settings](security-settings.md)
+ [FAQ](faq.md)

## Wickr admin console
<a name="wickr-admin-console"></a>

The Wickr Admin Console interface is used for administering the Wickr Enterprise application itself. It can be used to set up networks, users, federation, and more. It's accessible over HTTPS at the DNS name that you configured to point to your Load Balancer. The default username is admin, with the password Password123. You will be required to change this password on first log in.

![Wickr Enterprise console sign in image.](http://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/images/wickr-enterprise-console.png)
