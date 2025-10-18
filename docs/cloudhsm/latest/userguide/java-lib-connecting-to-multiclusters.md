# Connect to multiple AWS CloudHSM clusters

Each `CloudHsmProvider` represents a connection to your AWS CloudHSM Cluster. If you want to talk to another cluster from the same application, you 
 can create another object of `CloudHsmProvider` with configurations for your other cluster and you can interact with this other cluster either using the provider object 
 or using the provider name, as shown in the following example.


```
CloudHsmProviderConfig config = CloudHsmProviderConfig.builder()  
                                    .withCluster(  
                                        CloudHsmCluster.builder()  
                                            .withHsmCAFilePath(hsmCAFilePath)
                                            .withClusterUniqueIdentifier("CloudHsmCluster1")
        .withServer(CloudHsmServer.builder().withHostIP(hostName).build())  
                        .build())  
        .build();
CloudHsmProvider provider1 = new CloudHsmProvider(config);

if (Security.getProvider(provider1.getName()) == null) {
    Security.addProvider(provider1);
}

CloudHsmProviderConfig config2 = CloudHsmProviderConfig.builder()  
                                    .withCluster(  
                                        CloudHsmCluster.builder()  
                                            .withHsmCAFilePath(hsmCAFilePath2)
                                            .withClusterUniqueIdentifier("CloudHsmCluster2")
        .withServer(CloudHsmServer.builder().withHostIP(hostName2).build())  
                        .build())  
        .build();
CloudHsmProvider provider2 = new CloudHsmProvider(config2);

if (Security.getProvider(provider2.getName()) == null) {
    Security.addProvider(provider2);
}
```
Once you have configured both the providers (both the clusters) above, you can interact with them either using the provider object or using the provider name. 
 

Expanding upon this example that shows how to talk to `cluster1`, you could use the following sample for a AES/GCM/NoPadding operation:


```
Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding", provider1);
```
And in the same application to do "AES" Key generation on the second cluster using the provider name, you could also use the following sample:


```
Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding", provider2.getName());
```
