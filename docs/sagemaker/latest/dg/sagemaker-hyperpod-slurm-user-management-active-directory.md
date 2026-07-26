# Integrate HyperPod clusters with Active Directory

In practical use cases, HyperPod clusters are typically used by multiple users:
machine learning (ML) researchers, software engineers, data scientists, and cluster
administrators. Instead of statically creating users on each instance, you can use [Lightweight
Directory Access Protocol (LDAP)](https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol "https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol") on Wikipedia and LDAP over TLS/SSL (LDAPS) to
integrate with
a directory service such as [AWS
Directory Service for Microsoft Active Directory](https://aws.amazon.com/directoryservice/ "https://aws.amazon.com/directoryservice/"). For more information, see the
blog post [Integrate HyperPod clusters with Active Directory for seamless multi-user
login](https://aws.amazon.com/blogs/machine-learning/integrate-hyperpod-clusters-with-active-directory-for-seamless-multi-user-login/ "https://aws.amazon.com/blogs/machine-learning/integrate-hyperpod-clusters-with-active-directory-for-seamless-multi-user-login/").
