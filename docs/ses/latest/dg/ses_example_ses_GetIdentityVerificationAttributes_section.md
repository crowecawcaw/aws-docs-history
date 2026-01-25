# Use `GetIdentityVerificationAttributes` with an AWS SDK or CLI

The following code examples show how to use `GetIdentityVerificationAttributes`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Verify an email identity and send messages](ses_example_ses_Scenario_SendEmail_section.md "ses_example_ses_Scenario_SendEmail_section.md")

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/SES#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/SES#code-examples").

```

    /// <summary>
    /// Get identity verification status for an email.
    /// </summary>
    /// <returns>The verification status of the email.</returns>
    public async Task<VerificationStatus> GetIdentityStatusAsync(string email)
    {
        var result = VerificationStatus.TemporaryFailure;
        try
        {
            var response =
                await _amazonSimpleEmailService.GetIdentityVerificationAttributesAsync(
                    new GetIdentityVerificationAttributesRequest
                    {
                        Identities = new List<string> { email }
                    });

            if (response.VerificationAttributes.ContainsKey(email))
                result = response.VerificationAttributes[email].VerificationStatus;
        }
        catch (Exception ex)
        {
            Console.WriteLine("GetIdentityStatusAsync failed with exception: " + ex.Message);
        }

        return result;
    }



```

- For API details, see
  [GetIdentityVerificationAttributes](../../../goto/DotNetSDKV3/email-2010-12-01/GetIdentityVerificationAttributes.md "../../../goto/DotNetSDKV3/email-2010-12-01/GetIdentityVerificationAttributes.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To get the Amazon SES verification status for a list of identities**

The following example uses the `get-identity-verification-attributes` command to retrieve the Amazon SES verification status for a list of identities:

```
`aws ses get-identity-verification-attributes --identities `"user1@example.com"` `"user2@example.com"``

```

Output:

```
{
   "VerificationAttributes": {
       "user1@example.com": {
           "VerificationStatus": "Success"
       },
       "user2@example.com": {
           "VerificationStatus": "Pending"
       }
   }
}
```

If you call this command with an identity that you have never submitted for verification, that identity won't appear in the output.

For more information about verified identities, see Verifying Email Addresses and Domains in Amazon SES in the _Amazon Simple Email Service Developer Guide_.

- For API details, see
  [GetIdentityVerificationAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-identity-verification-attributes.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-identity-verification-attributes.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ses#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ses#code-examples").

```
class SesIdentity:
    """Encapsulates Amazon SES identity functions."""

    def __init__(self, ses_client):
        """
        :param ses_client: A Boto3 Amazon SES client.
        """
        self.ses_client = ses_client


    def get_identity_status(self, identity):
        """
        Gets the status of an identity. This can be used to discover whether
        an identity has been successfully verified.

        :param identity: The identity to query.
        :return: The status of the identity.
        """
        try:
            response = self.ses_client.get_identity_verification_attributes(
                Identities=[identity]
            )
            status = response["VerificationAttributes"].get(
                identity, {"VerificationStatus": "NotFound"}
            )["VerificationStatus"]
            logger.info("Got status of %s for %s.", status, identity)
        except ClientError:
            logger.exception("Couldn't get status for %s.", identity)
            raise
        else:
            return status



```

- For API details, see
  [GetIdentityVerificationAttributes](../../../goto/boto3/email-2010-12-01/GetIdentityVerificationAttributes.md "../../../goto/boto3/email-2010-12-01/GetIdentityVerificationAttributes.md")
  in _AWS SDK for Python (Boto3) API Reference_.

Ruby

**SDK for Ruby**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/ses/v1#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/ses/v1#code-examples").

```

require 'aws-sdk-ses' # v2: require 'aws-sdk'

# Create client in us-west-2 region
# Replace us-west-2 with the AWS Region you're using for Amazon SES.
client = Aws::SES::Client.new(region: 'us-west-2')

# Get up to 1000 identities
ids = client.list_identities({
                               identity_type: 'EmailAddress'
                             })

ids.identities.each do |email|
  attrs = client.get_identity_verification_attributes({
                                                        identities: [email]
                                                      })

  status = attrs.verification_attributes[email].verification_status

  # Display email addresses that have been verified
  puts email if status == 'Success'
end


```

- For API details, see
  [GetIdentityVerificationAttributes](../../../goto/SdkForRubyV3/email-2010-12-01/GetIdentityVerificationAttributes.md "../../../goto/SdkForRubyV3/email-2010-12-01/GetIdentityVerificationAttributes.md")
  in _AWS SDK for Ruby API Reference_.

SAP ABAP

**SDK for SAP ABAP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples").

```
    DATA lt_identities TYPE /aws1/cl_sesidentitylist_w=>tt_identitylist.
    APPEND NEW /aws1/cl_sesidentitylist_w( iv_value = iv_identity ) TO lt_identities.

    TRY.
        DATA(lo_result) = lo_ses->getidentityverificationattrs(
          it_identities = lt_identities
        ).

        DATA(lt_attrs) = lo_result->get_verificationattributes( ).
        IF lt_attrs IS NOT INITIAL.
          LOOP AT lt_attrs ASSIGNING FIELD-SYMBOL(<ls_attr>).
            ov_status = <ls_attr>-value->get_verificationstatus( ).
            EXIT.
          ENDLOOP.
        ELSE.
          ov_status = 'NotFound'.
        ENDIF.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_ex).
        DATA(lv_error) = |An error occurred: { lo_ex->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex.
    ENDTRY.


```

- For API details, see
  [GetIdentityVerificationAttributes](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon SES with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
