# Overview of LDAP with Amazon EMR

Lightweight Directory Access Protocol (LDAP) is a software protocol that network
administrators use to manage and control access to data by authenticating users within a
company’s network. The LDAP protocol stores information in a hierarchical, tree
directory structure. For more information, see [Basic LDAP Concepts](https://ldap.com/basic-ldap-concepts/ "https://ldap.com/basic-ldap-concepts/") on
_LDAP.com_.

Within a company’s network, many applications might use the LDAP protocol to
authenticate users. With the Amazon EMR LDAP integration, EMR clusters can natively use the
same LDAP protocol with an added security configuration.

There are two major implementations of the LDAP protocol that Amazon EMR supports:
**Active Directory** and **OpenLDAP**. While other implementations are possible, most fit the same
authentication protocols as Active Directory or OpenLDAP.

## Active Directory (AD)

Active Directory (AD) is a directory service from Microsoft for Windows domain
networks. AD is included on most Windows Server operating systems, and can
communicate with clients over the LDAP and LDAPS protocols. For authentication,
Amazon EMR attempts a user-bind with your AD instance with the User Principal Name (UPN)
as the distinguished name and password. The UPN uses the standard format
`username@domain_name`.

## OpenLDAP

OpenLDAP is a free, open-source implementation of the LDAP protocol. For
authentication, Amazon EMR attempts a user-bind with your OpenLDAP instance with the
fully qualified domain name (FQDN) as the distinguished name and password. The FQDN
uses the standard format
`username_attribute=username,LDAP_user_search_base`. Commonly, the
`username_attribute` value is `uid`, and the
`LDAP_user_search_base` value contains the attributes of the tree
that leads to the user. For example,
`ou=People,dc=example,dc=com`.

Other free and open-source implementations of the LDAP protocol typically follow a
similar FQDN as OpenLDAP for the distinguished names of their users.
