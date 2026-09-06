

# Plan your identity management in Connect Customer
<a name="connect-identity-management"></a>

Before you [set up your Connect Customer instance](amazon-connect-instances.md), you should decide how you want to manage your Connect Customer users. A user is anyone who needs a Connect Customer account: agents, call center managers, analysts, and more.

**You cannot change the option you select for identity management after you create an instance**. Instead, you must delete the instance and create a new one. However, if you delete an instance, you lose its configuration settings and metrics data.

When you create your instance, you can choose from one of the following identity management solutions:
+ **Store users with Connect Customer**—Choose this option if you want to create and manage user accounts within Connect Customer. 

  When you manage users in Connect Customer, the user name and password for each user is specific to Connect Customer. Users must remember a separate user name and password to log in to Connect Customer.
+ **Link to an existing directory**—Choose this option to use an existing Active Directory. Users will log in to Connect Customer using their corporate credentials.

  If you choose this option, the directory must be associated with your account, set up in Directory Service, and be active in the same Region in which you create your instance. If you plan to choose this option, you should prepare your directory before you create your Connect Customer instance. For more information, see [Use an existing directory for identity management in Connect Customer](directory-service.md).
+ **SAML 2.0-based authentication**—Choose this option if you want to use your existing network identity provider to federate users with Connect Customer. Users can only log in to Connect Customer by using the link configured through your identity provider. If you plan to choose this option, you should configure your environment for SAML before you create your Connect Customer instance. For more information, see [Configure SAML with IAM for Connect Customer](configure-saml.md).