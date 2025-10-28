# SSO – SAP Cloud Identity Services and Microsoft Entra

Microsoft Entra (previously Azure AD) or other IdPs can be integrated to SAP Cloud Identity Services directly. This support a direct authentication with Single Sign-On (SSO), when you do not need AWS IAM Identity Center (i.e. no requirement to run a multi account strategy that utilizes AWS Organizations).

![SAP Cloud Identity Services with Microsoft Entra](images/rise-security-entra.png)

**Authentication flow**

1. User accesses SAP Fiori via an Internet browser.
2. SAP Fiori will redirect SAML request back to the internet browser.
3. Internet Browser relays the SAML request to SAP Cloud Identity Services.
4. SAP Cloud Identity Service delegate authentication request to IdPs.
5. User is authenticated by IdP and SAML response is provided to the internet browser with user identity information.
6. User can access to SAP S/4HANA in RISE with SAP VPC.
   For more information on how to do this, you can refer to [Enable SSO between Azure AD and SAP Cloud Platform using Identity Authentication Service](https://developers.sap.com/mission.cp-azure-ias-single-signon.html "https://developers.sap.com/mission.cp-azure-ias-single-signon.html").
