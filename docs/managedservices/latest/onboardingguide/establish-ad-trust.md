# Establish an Active Directory (AD) trust

Before you begin to establish an Active Directory (AD) trust for your AWS Managed Services (AMS) account, make sure that the appropriate firewall ports are open.

The trust from the AMS-managed Active Directory and your corporate directory service allows you to use your corporate-managed credentials
to access AMS-managed instances to perform development, test, or administrative functions.

Creating a trust connection is a two-part exercise:

First, configure a conditional forward, a DNS configuration so DNS queries know which DNS server to go to.

Second, configure a trust, an Active Directory (AD) construct to allow access from users in one domain to use resources in another domain.
