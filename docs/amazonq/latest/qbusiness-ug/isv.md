# Amazon Q index for independent software vendors (ISVs)

As an ISV, you can leverage Amazon Q index to access and integrate your
customers' enterprise data into your applications. This integration enables you to enhance
your applications with generative AI capabilities powered by your customers' data, without
having to directly connect to or index individual data sources. Your customers simply need
to add you as a data accessor and provide you with the configuration details, allowing you
to retrieve relevant content through the `SearchRelevantContent` API operation.

Alternatively, you can create a Amazon Q application environment on behalf of the
customer and add their data sources yourself. The Amazon Q index will then be
able to retrieve the relevant content through the `SearchRelevantContent` API
operation. For more information, see [Creating an
Amazon Q index on behalf of a customer](isv-creating-index.md "isv-creating-index.md").

###### Topics

- [Key concepts](isv-key-concepts.md "isv-key-concepts.md")
- [Prerequisites](isv-prerequisites.md "isv-prerequisites.md")
- [Information to be provided to the Amazon Q Business team](isv-info-to-provide.md "isv-info-to-provide.md")
- [Getting access to your customer's Amazon Q index](isv-getting-access.md "isv-getting-access.md")
- [Accessing a customer's Amazon Q index as a data accessor using cross-account access](#isv-accessing-cross-account "#isv-accessing-cross-account")
- [Creating an Amazon Q index on behalf of a customer](isv-creating-index.md "isv-creating-index.md")
- [Troubleshooting](isv-troubleshooting.md "isv-troubleshooting.md")

## Accessing a customer's Amazon Q index as a data accessor using cross-account access

After Amazon Q Business customers give an independent software provider or vendor's (ISV)
_data accessor_ permissions to retrieve data from their Amazon Q
index, the customer or the ISV must connect with one another to get the following
configuration details. These configuration parameters are required inputs when they use
the `SearchRelevantContent` API operation to perform cross-account access to
relevant data from the customer's Amazon Q index. These parameters are accessed from the
customer's Amazon Q console in the **Information for data
accessor** tab in the **data accessor details** page which
is accessed by choosing the accessor **Name** from the **Data
accessors** table on the **Data accessors** page of their
application environment.

1. Amazon Q Business application ID — This is unique identifier of the Amazon Q Business
   application environment. It tells the ISV what Amazon Q application environment is associated with the
   Amazon Q index.
2. The Amazon Q Business application Region — This is the AWS Region where the
   Amazon Q Business application environment is created.
3. Amazon Q Business retriever ID — This is unique identifier for the retriever. The
   retriever gets the data from the Amazon Q index configured by the Amazon Q
   customer.
4. Data accessor application ARN — This is the ISV Amazon Resource Name (ARN). It
   is used to identify the ISV when it is accessing a customer's Amazon Q
   index.
5. The Region for the Identity and Access Management (IAM) Identity Center (IDC)
   instance — This is the AWS Region where the IDC instance of the customer has
   been created.

With these parameters, the ISV can begin retrieving content from the Amazon Q index by
calling the `SearchRelevantContent` API operation. The
`SearchRelevantContent` API operation follows Amazon Q Business access control
standards by only retrieving data that the customer's end users have been given access
to.

### Retrieving data from a customer's Amazon Q index as a data accessor using the SearchRelevantContent API

With valid configuration parameters from the customer, the ISV can use the
`SearchRelevantContent` API operation to retrieve user-specific
content from the customer's Amazon Q index.

The following are examples of how to use either Auth Code or Trusted Token Issuer
based authentication (TTI) to complete this task:

The following tabs provide a procedure to boost document attributes using the
console and code examples for the AWS CLI.

Auth code
Use the Authentication code method to retrieve user-specific content
from the customer's Amazon Q index.

1. The Amazon Q index customer's end user will login to the ISV's
   application using the existing user login flow.

###### Note

The ISV doesn't need to change their existing login
flow. 2. After the end user successfully logs in, the ISV instructs the
user to authenticate to their Amazon Q index through their OIDC
providers. For more information, see [Creating an Amazon Q Business application using AWS
IAM Identity Center](create-application.md "create-application.md").

    1. `https://oidc.${idc_region}.amazonaws.com/authorize?response_type=code&redirect_uri=${isv_redirect_url}&state={oauth_state}&client_id=${idc_application_arn}`
    2. `isv_redirect_uri` — This is the
     *redirect URL* that's registered
     at the ISV registration process. For more information,
     see [Information to be provided to the Amazon Q Business
     team](isv-info-to-provide.md "isv-info-to-provide.md").
    3. `oauth_state` — This random string prevents
     cross-site request forgery (CSRF) attack. For more
     detail about state parameters in oauth, see [Prevent Attacks and Redirect Users with OAuth 2.0
     State Parameters](https://auth0.com/docs/secure/attack-protection/state-parameters "https://auth0.com/docs/secure/attack-protection/state-parameters") in the auth by Okta
     guide.
    4. `idc_application_arn` — This is the
     Amazon Q Business DataAccessor IAM Identity Center application ID that's
     provided by the customer to the ISV.

3. The end user logs in using the method configured by the
   customer's Amazon Q administrator. For example, the user's company
   SSO.
4. The ISV application receives an _auth code_
   in their _redirect URL_.
5. The ISV application calls the `CreateTokenWithIAM`
   API operation to get a token with an authorization code. The ISV
   needs to use the AWS Identity and Access Management (IAM) role that they created
   during the onboarding process with `tenantId`
   information in the tags like the following:

```

aws sts assume-role \
      --role-arn ${your_iam_role} \
      --role-session-name test-session \
      --tags Key=qbusiness-dataaccessor:ExternalId,Value=${isv tenantId}

aws sso-oidc create-token-with-iam --client-id "${idc_application_arn}" \
      --redirect-uri "{your_redirect_uri}" \
      --grant-type "authorization_code" \
      --code "${CODE}" --region ${idc_region}

```

6. Get
   the `idToken` field from the
   response of `CreateTokenWithIAM`. Then, decode the
   `idToken` and extract
   `"sts:identity_context"` field from it.

Using command line:

```

export ID_TOKEN_I = "${response_json_of_create-token-with-iam}"
export ID_CONTEXT=`jq -R 'split(".") | .[1] | @base64d | fromjson' <<< "$ID_TOKEN_I" | jq -r '."sts:identity_context"'`
echo "ID_CONTEXT=$ID_CONTEXT\n"
```

Using Python:

```
import json
import base64

body = "${response_json_of_create-token-with-iam}"
body_json = base64.urlsafe_b64decode(body.split(".")[1] + '==')
data = json.loads(body_json)
print(f"{data['sts:identity_context']}")

```

7. Call the [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") API with the extracted
   `sts:identity_context` and the ISV
   `tenantId` information.

```

aws sts assume-role \
      --role-arn ${your_iam_role} \
      --role-session-name test-session \
      --provided-contexts '[{"ProviderArn": "arn:aws:iam::aws:contextProvider/IdentityCenter", "ContextAssertion": "${value from sts:identity_context}"}]' \
      --tags Key=qbusiness-dataaccessor:ExternalId,Value=${isv tenantId}

```

8. Use the AWS Sig V4 credentials returned from the previous
   step to call `SearchRelevantContent` API.

```

aws qbusiness search-relevant-content \
      --application-id ${qbusiness_application_id} \
      --query-text "What is Amazon Q?" \
      --content-source '{"retriever": {"retrieverId": "${retriever_id}"}}'

```

TTI
Use the Trusted Token Issuer based authentication (TTI) method to
retrieve user-specific content from the customer's Amazon Q index.

1. The Amazon Q index customer's end user will log in to the ISV's
   application using the existing user login flow.
2. After the end user successfully logs in, ISV issues a token
   for the end user using the OIDC client as audience, provided
   during the onboarding process.
3. The ISV application calls the `CreateTokenWithIAM`
   API operation with the token from step 2. The ISV needs to use
   the AWS Identity and Access Management (IAM) role that they
   created during the onboarding process with `tenantId`
   information in the tags like the following:

```


aws sts assume-role \
      --role-arn ${your_iam_role} \
      --role-session-name test-session \
      --tags Key=qbusiness-dataaccessor:ExternalId,Value=${isv tenantId}

aws sso-oidc create-token-with-iam --client-id "${idc_application_arn}" \
      --grant-type "urn:ietf:params:oauth:grant-type:jwt-bearer" \
      --assertion "${isv token generated using oidc client provided during onboarding}" --region ${idc_region}


```

4. Retrieve the `idToken`field from the response of
   `CreateTokenWithIAM`. Then, decode the
   `idToken` and extract
   `sts:identity_context` field from it.
   1. Using command line:

   ```

   export ID_TOKEN_I = "${response_json_of_create-token-with-iam}"
   export ID_CONTEXT=`jq -R 'split(".") | .[1] | @base64d | fromjson' <<< "$ID_TOKEN_I" | jq -r '."sts:identity_context"'`
   echo "ID_CONTEXT=$ID_CONTEXT\n"

   ```

   2. Using Python:

   ```

                                               import json
   import base64

   body = "${response_json_of_create-token-with-iam}"
   body_json = base64.urlsafe_b64decode(body.split(".")[1] + '==')
   data = json.loads(body_json)
   print(f"{data['sts:identity_context']}")

   ```

5. Call the `AssumeRole` API with the extracted
   `sts:identity_context` and the ISV
   `tenantId` information.

```


aws sts assume-role \
      --role-arn ${your_iam_role} \
      --role-session-name test-session \
      --provided-contexts '[{"ProviderArn": "arn:aws:iam::aws:contextProvider/IdentityCenter", "ContextAssertion": "${value from sts:identity_context}"}]' \
      --tags Key=qbusiness-dataaccessor:ExternalId,Value=${isv tenantId}

```

Use the AWS Sig V4 credentials returned from the previous
step to call `SearchRelevantContent` API.

```

aws qbusiness search-relevant-content \
      --application-id ${qbusiness_application_id} \
      --query-text "What is Amazon Q?" \
      --content-source '{"retriever": {"retrieverId": "${retriever_id}"}}'

```
