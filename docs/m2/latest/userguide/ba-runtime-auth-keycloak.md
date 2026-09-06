

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Configure Gapwalk OAuth2 authentication with Keycloak
<a name="ba-runtime-auth-keycloak"></a>

This topic describes how to configure OAuth2 authentication for Gapwalk applications using Keycloak as an identity provider (IdP). In this tutorial we use Keycloak 24.0.0.

## Prerequisites
<a name="ba-runtime-auth-keycloak-prereq"></a>
+ [Keycloak](https://www.keycloak.org/)
+ Gapwalk application

## Keycloak setup
<a name="keycloak-setup"></a>

1. Go to your Keycloak dashboard in your web browser. The default credentials are admin/admin. Go to the top left navigation bar, and create a realm with the name **demo**, as shown in the following image.  
![alt_text](http://docs.aws.amazon.com/m2/latest/userguide/images/ba-runtime-auth-keycloak_2.png)

1. Create a client with the name **app-demo**.  
![Clients list page with Create client button highlighted in the toolbar.](http://docs.aws.amazon.com/m2/latest/userguide/images/ba-runtime-auth-keycloak_3.jpg)

   Replace `localhost:8080` with the address of your Gapwalk application  
![alt_text](http://docs.aws.amazon.com/m2/latest/userguide/images/ba-runtime-auth-keycloak_4.png)  
![alt_text](http://docs.aws.amazon.com/m2/latest/userguide/images/ba-runtime-auth-keycloak_5.png)

1. To get your client secret, choose **Clients**, then **app-demo**, then **Credentials**.  
![alt_text](http://docs.aws.amazon.com/m2/latest/userguide/images/ba-runtime-auth-keycloak_6.jpg)

1. Choose **Clients**, then **Client scopes**, then **Add predefined mapper**. Choose **realm roles**.  
![alt_text](http://docs.aws.amazon.com/m2/latest/userguide/images/ba-runtime-auth-keycloak_7.jpg)

1. Edit your realm role with the configuration shown in the following image.  
![alt_text](http://docs.aws.amazon.com/m2/latest/userguide/images/ba-runtime-auth-keycloak_8.jpg)

1. Remember the defined **Token Claim Name**. You’ll need this value in the Gapwalk settings definition for the `gapwalk-application.security.claimGroupName` property.  
![alt_text](http://docs.aws.amazon.com/m2/latest/userguide/images/ba-runtime-auth-keycloak_9.jpg)

1. Choose **Realms roles**, and create 3 roles: **SUPER\_ADMIN**, **ADMIN**, and **USER**. These roles are later mapped to `ROLE_SUPER_ADMIN`, `ROLE_ADMIN`, and `ROLE_USER` by the Gapwalk application to be able to access some restricted API REST calls.  
![alt_text](http://docs.aws.amazon.com/m2/latest/userguide/images/ba-runtime-auth-keycloak_10.jpg)

## Integrate Keycloak into the Gapwalk application
<a name="gapwalk-setup"></a>

Edit your `application-main.yml` as follows:

```
gapwalk-application.security: enabled
gapwalk-application.security.identity: oauth
gapwalk-application.security.issuerUri: http://<KEYCLOAK_SERVER_HOSTNAME>/realms/<YOUR_REALM_NAME>
gapwalk-application.security.claimGroupName: "keycloak:groups"

gapwalk-application.security.userAttributeName: "preferred_username"
# Use "username" for cognito, 
#     "preferred_username" for keycloak
#      or any other string

spring:
  security:
    oauth2:
      client:
        registration:
          demo:
            client-id: <YOUR_CLIENT_ID>
            client-name: Demo App
            client-secret: <YOUR_CLIENT_SECRET>
            provider: keycloak
            authorization-grant-type: authorization_code
            scope: openid
            redirect-uri: "{baseUrl}/login/oauth2/code/{registrationId}"
        provider:
          keycloak:
            issuer-uri: ${gapwalk-application.security.issuerUri}
            authorization-uri: ${gapwalk-application.security.issuerUri}/protocol/openid-connect/auth
            jwk-set-uri: ${gapwalk-application.security.issuerUri}/protocol/openid-connect/certs
            token-uri: ${gapwalk-application.security.issuerUri}/protocol/openid-connect/token
            user-name-attribute: ${gapwalk-application.security.userAttributeName}
      resourceserver:
        jwt:
          jwk-set-uri: ${gapwalk-application.security.issuerUri}/protocol/openid-connect/certs
```

Replace {{<KEYCLOAK\_SERVER\_HOSTNAME>}}, {{<YOUR\_REALM\_NAME>}}, {{<YOUR\_CLIENT\_ID>}}, and {{<YOUR\_CLIENT\_SECRET>}} with your Keycloak server hostname, your realm name, your client ID, and your client secret.