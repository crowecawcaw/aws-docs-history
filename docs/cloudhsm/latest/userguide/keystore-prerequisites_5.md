# Prerequisites for integrating AWS CloudHSM with Java
 Keytool and Jarsigner using Client SDK 5

To use the AWS CloudHSM key store, you must first initialize and configure the AWS CloudHSM JCE SDK. Use
 the following steps to do so. 


## Step 1: Install the JCE


To install the JCE, including the AWS CloudHSM client prerequisites, follow the steps for
 [installing the Java library](java-library-install_5.md "java-library-install_5.md"). 


## Step 2: Add HSM login credentials to environment
 variables


Set up environment variables to contain your HSM login credentials.
 



Linux

```
`$` export HSM_USER=`<HSM user name>`
```


```
`$` export HSM_PASSWORD=`<HSM password>`
```


Windows

```
`PS C:\>` $Env:HSM_USER=`<HSM user name>`
```


```
`PS C:\>` $Env:HSM_PASSWORD=`<HSM password>`
```



###### Note

The AWS CloudHSM JCE offers various login options. To use the AWS CloudHSM key store with
 third-party applications, you must use implicit login with environment
 variables. If you want to use explicit login through application code, you must
 build your own application using the AWS CloudHSM key store. For additional
 information, see the article on [Using AWS CloudHSM Key
 Store](alternative-keystore_5.md "alternative-keystore_5.md"). 


## Step 3: Registering the JCE provider


To register the JCE provider in the Java CloudProvider configuration, follow these steps: 



1. Open the `java.security` configuration file in your Java installation for editing.
2. In the `java.security` configuration file, add `com.amazonaws.cloudhsm.jce.provider.CloudHsmProvider`
 as the last provider. For example, if there are nine providers in the `java.security` file, add the following
 provider as the last provider in the section:


`security.provider.10=com.amazonaws.cloudhsm.jce.provider.CloudHsmProvider`

###### Note

Adding the AWS CloudHSM provider as a higher priority may negatively impact your system's performance because the AWS CloudHSM provider 
 will be prioritized for operations that may be safely offloaded to software. As a best practice, **always** specify the provider 
 you wish to use for an operation, whether it is the AWS CloudHSM or a software-based provider.


###### Note

Specifying `-providerName`, `-providerclass`, and `-providerpath` command line options when generating
 keys using **keytool** with the AWS CloudHSM key store may cause errors.
