# Add a data accessor (ISV) to connect to your Amazon Q index

After setting up your application environment and connecting your data source(s), Amazon Q Business
begins indexing your enterprise data. You still need to add the software providers
(ISVs) as a data accessor and provide configuration details to the ISV to retrieve
content from your Amazon Q index. By adding a data accessor, you grant their AWS account
to access the Amazon Q index via the `SearchRelevantContent` API
operation.

You can grant data accessor permissions to your Amazon Q index using either the
Amazon Q Business console or the Amazon Q Business API. The following procedures show how to do this
using the Amazon Q Business console or the AWS CLI.

###### Important

You must provide the setup details generated when adding your ISV as a data
accessor to your ISV so they can access your Amazon Q index. You can find
this information at any time in the **Information for data
accessor** tab in the **data accessor details** page
which is accessed by choosing the accessor **Name** from the
**Data accessors** table on the **Data
accessors** page.

The following tabs provide the instructions for how to retrieve your `Tenant
 ID` for each ISV. In data accessors, the `External Id` is the same
as `Tenant Id`.

Asana
In Asana, the Tenant ID in Amazon Q Business Data Accessor is called the
`domain ID`. You can use the following instructions to
retrieve the Asana Tenant ID

1. Choose your account profile picture and select Admin Console.

2. Select Settings.

3. Scroll to Domain Settings to retrieve the Tenant ID.

PagerDuty
In PagerDuty, the tenant ID in Amazon Q Business Data Accessor is called the
tenant ID. You can use the following instructions to retrieve the PagerDuty
the Tenant ID

1. Select the User Icon.

2. Select Account Settings.

3. Select the PagerDuty Advance tab.

4. Toggle Enable Amazon Q to the on position.

5. The PagerDuty Tenant ID is now available from the Amazon Q Business
   Configuration Values modal.

Kore.ai (AIforWork)
In AIforWork, the Tenant ID is displayed directly in the
setup form. You can use the following instructions to retrieve the
Kore.ai Tenant ID:

1. Navigate to AIforWork platform.

2. When setting up an Enterprise Knowledge or Search Agent, choose
   **Q for Business**.

3. In the setup form that opens, the Tenant ID is displayed and ready to
   copy.

Revinova
The Portal ID in Revinova is the Tenant ID for Amazon Q
Business Data Accessor. You can use the instructions below to retrieve the
Portal ID from Revinova.

1. Log in to the admin console.
2. Navigate to the portals dashboard using the
   **Portals** menu under the settings menu
   collection.
3. In the portal's grid, hover on the header of any of the columns
   and click on the hamburger menu shown in the column to open the
   column options context menu.
4. Click on the grid icon available on the top right corner of the
   column options context menu.
5. Select **ID** from the list of columns available
   for display, and it will show the portal IDs in the grid.
6. You can get the ID for the portal from the corresponding
   row.

Planview
Your Planview Tenant ID is a unique identifier in UUID/GUID format (e.g., 12345678-1234-1234-1234-123456789abc).

For Planview, the Tenant ID information can be found in their integration
documentation. You can use the following resource to retrieve the Tenant ID
for Planview Viz integration with Amazon Q Business.

1. Refer to the [Planview Amazon Q Business Integration FAQ](https://success.planview.com/Planview_Viz/FAQs/General/Planview_Amazon_Q_Business_Integration_FAQ "https://success.planview.com/Planview_Viz/FAQs/General/Planview_Amazon_Q_Business_Integration_FAQ") for detailed
   instructions on retrieving your Tenant ID.

###### Note

Planview data accessor is only available in the `us-west-2` region.

Amplience
For Amplience, the Tenant ID is the Hub ID. You can use the following instructions to retrieve the Amplience Tenant ID.

1. Within Amplience Dynamic Content, switch into the Hub you wish to connect.
2. Select the settings icon in the top right corner and select the **Properties** menu item.
3. The Hub ID will be displayed with a copy to clipboard option.

Saviynt
For Saviynt, the Tenant ID is the FQDN from the Saviynt Console. You can use the following instructions to retrieve the Saviynt FQDN.

The URL will look similar to this example https://ispm-dev.saviyntcloud.com/ and the tenant id from this example will be "ispm-dev.saviyntcloud.com"

Webex by CISCO
In Webex, the tenant ID in Amazon Q Business Data Accessor is called the Organization ID. You can use the following instructions to retrieve the Webex Tenant ID.

1. Login in Cisco Control Hub.

2. Go to Account->Info page.

3. Copy the Organization ID.

Fireflies.ai
When prompted for Tenant ID, please enter Team ID

Miro
For Miro, the Tenant ID is Organization ID. Organization admins can navigate to the 'Organization profile' page and get the id from the address bar.

SUSE Rancher for Amazon Web Services
For SUSE Rancher for Amazon Web Services, the Tenant ID is tenant-uid. The tenant-uid can be found within the application in the about info in the top right of the screen.

CXone Mpower
For CXone Mpower, the Tenant ID required for the Amazon Q Business Data Accessor is displayed on your My Profile page. To access this page,

- In the upper‑right corner of any page in the platform, click your initials.

- Select My Profile from the menu.

- On the General tab of the My Profile page, locate your Tenant ID.

###### Topics

- [Add a data accessor using the console](#data-accessors-granting-permissions-console "#data-accessors-granting-permissions-console")
- [Adding a data accessor using the AWS CLI](#data-accessors-granting-permissions-cli "#data-accessors-granting-permissions-cli")

## Add a data accessor using the console

Prerequisite for both Auth code and TTI configurations.

`tenantID`

The `tenantID` is a unique identifier for your application tenant. Each
application might have different terms for a tenant such as Workspace ID for Slack
or Domain ID for Asana. You can review the [Prerequisites](isv-prerequisites.md "isv-prerequisites.md")
page to see how to retrieve the `TenantId` for your application.

1. Sign in to the Amazon Q Business console.
2. Choose **Applications**, then select the name of your
   application environment from the list.
3. From the left navigation, choose **Data
   accessors**.
4. Choose the authentication method, **Auth Code** or
   **Trusted Token Issuer (TTI)** from the list of
   options.
5. Choose from the list of approved and supported data accessors
   (ISVs).
6. Choose a **Name** for this data accessor's instance, for
   example `<your
application-name>-<accessor-name>`.

If you chose TTI, follow these steps to configure the
authentication:

    1. Enter your  **External Id (same as Tenant Id)**,
     **Trust Token Issuer name**, **Identity
     provider attribute**, and **IAM Identity Center
     attribute**.
    2. Select, **Create trusted token issuer**.

7. Choose **Data source access** between **Allow
   all** or **Allow specific data sources**
   depending on whether you want to provide the ISV access to all or certain
   data sources from your Amazon Q index.
8. Choose the end **User access**. These are the end users
   that will connect with and use the Amazon Q index data from within the ISV's
   application. You can choose between all users that have access to the
   Amazon Q Business application environment or a subset of users and groups that you can
   define.
9. Choose **Add data accessor** to confirm your choices and
   add the data accessor.

###### Note

You must provide the setup details generated when adding your ISV as a
data accessor to your ISV so they can access your Amazon Q
index. You can find this information at any time in the
**Information for data accessor** tab in the
**data accessor details** page which is accessed by
choosing the accessor **Name** from the **Data
accessors** table on the **Data
accessors** page. 10. The data accessor you have added will now appear as an entry in the table
on the main **Data accessors** page.

## Adding a data accessor using the AWS CLI

In order to add an ISV as a data accessor you will need to call 3 APIs. First, the
`CreateDataAccessor` API operation will create a data accessor and
associate your application ID. `AssociatePolicy` operation API to attach
the resource based policy for cross account API calls. Finally, you will set your
user assignment for the Identity and Access Management (IAM) Identity Data Center
(IDC) application environment with `PutApplicationAssignment` API. For granular
user access control, use the Amazon Q Business console.

Prerequisite for both Auth code and TTI configurations.

`tenantID`

The `tenantID` is a unique identifier for your application tenant. Each
application might have different terms for a tenant such as Workspace ID for Slack
or Domain ID for Asana. You can review the [Prerequisites](isv-prerequisites.md "isv-prerequisites.md")
page to see how to retrieve the `TenantId` for your application.

### ISV data accessor principal role ARNs for the CreateDataAccessor API

The following are the `principal` role ARNs for the supported
ISVs:

- Asana —
  `arn:aws:iam::865993441991:role/autogen_role_customer-byoq-data-accessor_customer_q_biz_d-217f4f`
- Miro —
  `arn:aws:iam::380983552397:role/AwsQBusinessMiroRetriever`
- Zoom —
  `arn:aws:iam::796973485215:role/zoom-ai-amazon-q-business-retrieval-role`
- PagerDuty —
  `arn:aws:iam::748801462010:role/terraform/pagerduty-isv-qretriever-dataaccessor-role`
- Kore.ai —
  `arn:aws:iam::452460288037:role/Q4BTrustPolicyRole`
- Karini AI —
  `arn:aws:iam::891377073540:role/Karini-AmazonQ-Data-Accessor-Role`
- Revinova —
  `arn:aws:iam::833755663361:role/revinova_q_business_isv_role`
- Planview (available in `us-west-2` only) —
  `arn:aws:iam::431569694887:role/ep-copilot-production-us-west-2-q-index-role-tti`
- Amplience —
  `arn:aws:iam::123645302184:role/q-index-isv-role`
- Saviynt —
  `arn:aws:iam::249469748895:role/ispm-isv-qindex`
- Webex by CISCO —
  `arn:aws:iam::973559386291:role/WebexSuit-QIndex-role-prod`
- Fireflies.ai —
  `arn:aws:iam::466023587921:role/awsQAccessorRole`
- SUSE Rancher for Amazon Web Services —
  `arn:aws:iam::940482441539:role/mcm-q-data-accessor`
- CXone Mpower —
  `arn:aws:iam::765956972205:role/nice_csa_kh_qindex_retriever_trust_role`

### Action configuration (JSON) example for the CreateDataAccessor API

- `action` — Only
  `qbusiness:SearchRelevantContent` is supported now
- `filterConfiguration`: Specifies the data source id of the
  Amazon Q application environment. The ISV will only have access to the data from the
  specified data source id. If there is no data source id specified, the
  ISV will have access to all the data sources.

```

# CreateDataAccessor actionConfigurations example
[
   {
        "action": "qbusiness:SearchRelevantContent",
        "filterConfiguration": {
        "documentAttributeFilter": {
          "equalsTo": {
            "name": "_data_source_id",
            "value": {
              "stringValue": "your_datasource_id"
            }
          }
        }
      }
   }
]

```

### CLI example

The following CLI example shows how to create a data accessor and associate
the necessary permissions with all end users enabled for this data
accessor:

```

aws qbusiness create-data-accessor \
 --application-id ${qbusiness_application_id} \
 --principal ${isv_data_accessor_role_arn} \
 --action-configurations  ${action_configuration} \
 --display-name ${qbusiness_data_accessor_name} \
 --authentication-detail ${authentication_detail}

aws qbusiness associate-permission \
 --application-id ${qbusiness_application_id} \
 --statement-id ${statement_id} \
 --actions ${actions} \
 --principal ${isv_data_accessor_role_arn} \
 --conditions ${conditions}

aws sso-admin put-application-assignment-configuration \
 --application-arn ${qbusiness_data_accessor_idc_application_arn}\
 --no-assignment-required\
 --region ${idc_region}


```

The following CLI example shows how to add authentication details in your
request:

```

# For tti based dataaccessor
"authenticationDetail": {
    "authenticationType": "AWS_IAM_IDC_TTI",
    "authenticationConfiguration": {
        "idcTrustedTokenIssuerConfiguration": {
            "idcTrustedTokenIssuerArn": "${IDC trusted token issuer created using ISV issuer URL}"
        }
    },
    "externalIds": [
        "${ISV tenantId}"
    ]
}

# For Authcode based dataaccessor
"authenticationDetail": {
    "authenticationType": "AWS_IAM_IDC_AUTH_CODE",
    "externalIds": [
        "${ISV tenantId}"
    ]
}

```
