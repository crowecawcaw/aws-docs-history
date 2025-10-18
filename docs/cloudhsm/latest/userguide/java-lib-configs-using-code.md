# Configure the AWS CloudHSM`CloudHsmProvider` class using code

As of Client SDK version 5.8.0, you can also configure the AWS CloudHSM `CloudHsmProvider` class using Java code. 
 The way to do this is using an object of `CloudHsmProviderConfig` class. You can build this object using `CloudHsmProviderConfigBuilder`. 
 

`CloudHsmProvider` has another constructor which takes the `CloudHsmProviderConfig` object, as the following sample shows.


```
CloudHsmProviderConfig config = CloudHsmProviderConfig.builder()  
                                    .withCluster(  
                                        CloudHsmCluster.builder()  
                                            .withHsmCAFilePath(hsmCAFilePath)
                                            .withClusterUniqueIdentifier("CloudHsmCluster1")
        .withServer(CloudHsmServer.builder().withHostIP(hostName).build())  
                        .build())  
        .build();
CloudHsmProvider provider = new CloudHsmProvider(config);
```
In this example, the name of the JCE provider is `CloudHsmCluster1`. This is the name that application can then use to interact with JCE:


```
Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding", "CloudHsmCluster1");
```
Alternatively, applications can also use the provider object created above to let JCE know to use that provider for the operation:


```
Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding", provider);
```
If a unique identifier is not specified with the `withClusterUniqueIdentifier` method, a randomly generated provider name is created for you. 
 To get this randomly generated identifier, applications can call `provider.getName()` to get the identifier.
