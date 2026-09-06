

# Types of certificates in AWS Certificate Manager
<a name="certificate-types"></a>

AWS Certificate Manager (ACM) supports three types of certificates. Each type serves different use cases depending on your security requirements and infrastructure needs.

Public certificates  
Publicly trusted across the internet. Public certificates issued by ACM are trusted by all major browsers and operating systems, making them suitable for securing public-facing websites and applications.

Private certificates  
Not publicly trusted. Private certificates are primarily used internal to an organization, such as for encrypting internal traffic, authenticating services, or implementing mutual TLS (mTLS) between microservices.

Imported certificates  
Customer-owned certificates imported into ACM. You can import certificates obtained from third-party certificate authorities for use with ACM integrated services or for export.