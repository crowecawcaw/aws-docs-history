# Connecting to multiple AWS CloudHSM clusters with the JCE
 provider

This configuration allows a single client instance to communicate to multiple AWS CloudHSM
 clusters. Compared to having a single instance only communicate with a single cluster, this
 can be a cost-savings feature for some use cases. The
 `CloudHsmProvider` class is AWS CloudHSM's implementation of [Java
 Security's Provider class](https://docs.oracle.com/javase/8/docs/api/java/security/Provider.html "https://docs.oracle.com/javase/8/docs/api/java/security/Provider.html"). Each instance of this class represents a connection
 to your entire AWS CloudHSM cluster. You instantiate this class and add it to Java Security
 provider's list so that you can interact with it using standard JCE classes.

The following example instantiates this class and adds it to Java Security provider’s list:


```
if (Security.getProvider(CloudHsmProvider.PROVIDER_NAME) == null) {
    Security.addProvider(new CloudHsmProvider());
}
```
`CloudHsmProvider` can be configured in two ways:


1. Configure with file (default configuration)
2. Configure using code
The following topics describe these configurations, and how to connect to multiple clusters.

###### Topics

* [Configure the AWS CloudHSMCloudHsmProvider class with a file (Default
 configuration)](java-lib-configs-default.md "java-lib-configs-default.md")
* [Configure the AWS CloudHSMCloudHsmProvider class using code](java-lib-configs-using-code.md "java-lib-configs-using-code.md")
* [Connect to multiple AWS CloudHSM clusters](java-lib-connecting-to-multiclusters.md "java-lib-connecting-to-multiclusters.md")
