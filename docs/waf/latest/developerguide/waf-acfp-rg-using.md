**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Adding the ACFP managed rule group to your web

ACL

This section explains how to add and configure the `AWSManagedRulesACFPRuleSet` rule group.

To configure the ACFP managed rule group to recognize account creation fraud activities in
your web traffic, you provide information about how clients access your registration page and
send account creation requests to your
application. For protected Amazon CloudFront distributions, you also provide information about how
your application responds to account creation requests. This configuration is in addition to the
normal configuration for a managed rule group.

For the rule group description and rules listing, see [AWS WAF Fraud Control account creation fraud prevention (ACFP) rule group](aws-managed-rule-groups-acfp.md "aws-managed-rule-groups-acfp.md").

###### Note

The ACFP stolen credentials database only contains usernames in email format.

This guidance is intended for users who know generally how to create and manage
AWS WAF protection packs (web ACLs), rules, and rule groups. Those topics are covered in prior sections
of this guide. For basic information about how to add a managed rule group to your protection pack (web ACL), see [Adding a managed rule group to a protection pack (web ACL) through
the console](waf-using-managed-rule-group.md "waf-using-managed-rule-group.md").

###### Follow best practices

Use the ACFP rule group in accordance with the best practices at [Best practices for intelligent
threat mitigation in AWS WAF](waf-managed-protections-best-practices.md "waf-managed-protections-best-practices.md").

###### To use the `AWSManagedRulesACFPRuleSet` rule group in your protection pack (web ACL)

1. Add the AWS managed rule group, `AWSManagedRulesACFPRuleSet` to your protection pack (web ACL), and
   **Edit** the rule group settings before saving.

###### Note

You are charged additional fees when you use this managed rule group. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/"). 2. In the **Rule group configuration** pane, provide the information that the
ACFP rule group uses to inspect account creation requests.

    1. For **Use regular expression in paths**, toggle this on if you
     want AWS WAF to perform regular expression matching for your registration and account
     creation page path specifications.


    AWS WAF supports the pattern syntax used by the PCRE library `libpcre` with some exceptions. The library is documented at [PCRE - Perl Compatible Regular Expressions](http://www.pcre.org/ "http://www.pcre.org/"). For information about AWS WAF support, see [Supported regular expression syntax in AWS WAF](waf-regex-pattern-support.md "waf-regex-pattern-support.md").
    2. For **Registration page path**, provide the path of the registration
     page endpoint for your application. This page must accept
     `GET` text/html requests. The rule group inspects only
     HTTP `GET` text/html requests to your specified registration page endpoint.


    ###### Note

    Matching for endpoints is case insensitive. Regex specifications must not contain the flag `(?-i)`, which disables case insensitive matching. String specifications must start with a forward slash `/`.


    For example, for the URL
     `https://example.com/web/registration`, you could provide
     the string path specification `/web/registration`. Registration page paths that
     start with the path that you provide are considered a match. For example
     `/web/registration` matches the registration paths
     `/web/registration`, `/web/registration/`,
     `/web/registrationPage`, and
     `/web/registration/thisPage`, but doesn't match the path
     `/home/web/registration` or
     `/website/registration`.


    ###### Note

    Ensure that your end users load the registration page before they submit an account creation request. This helps ensure that the account creation requests from the client include valid tokens.
    3. For **Account creation path**, provide the URI in your website that accepts
     completed new user details. This URI must accept `POST` requests.


    ###### Note

    Matching for endpoints is case insensitive. Regex specifications must not contain the flag `(?-i)`, which disables case insensitive matching. String specifications must start with a forward slash `/`.


    For example, for the URL
     `https://example.com/web/newaccount`, you could provide
     the string path specification `/web/newaccount`. Account creation paths that
     start with the path that you provide are considered a match. For example
     `/web/newaccount` matches the account creation paths
     `/web/newaccount`, `/web/newaccount/`,
     `/web/newaccountPage`, and
     `/web/newaccount/thisPage`, but doesn't match the path
     `/home/web/newaccount` or
     `/website/newaccount`.
    4. For **Request inspection**, specify how your application accepts
     account creation attempts by providing the request payload type and the
     names of the fields within the request body where the username,
     password, and other account creation details are provided.


    ###### Note

    For the primary address and phone number fields, provide the
     fields in the order in which they appear in the request
     payload.


    Your specification of the field names depends on the payload
     type.




    	* **JSON payload type** – Specify the field names in JSON
    	 pointer syntax. For information about the JSON Pointer
    	 syntax, see the Internet Engineering Task Force (IETF)
    	 documentation [JavaScript
    	 Object Notation (JSON) Pointer](https://tools.ietf.org/html/rfc6901 "https://tools.ietf.org/html/rfc6901").


    	For example, for the following example JSON payload, the username field specification
    	 is `/signupform/username` and the primary address
    	 field specifications are `/signupform/addrp1`,
    	 `/signupform/addrp2`, and
    	 `/signupform/addrp3`.



    	```
    	{
    	    "signupform": {
    	        "username": "THE_USERNAME",
    	        "password": "THE_PASSWORD",
    	        "addrp1": "PRIMARY_ADDRESS_LINE_1",
    	        "addrp2": "PRIMARY_ADDRESS_LINE_2",
    	        "addrp3": "PRIMARY_ADDRESS_LINE_3",
    	        "phonepcode": "PRIMARY_PHONE_CODE",
    	        "phonepnumber": "PRIMARY_PHONE_NUMBER"
    	    }
    	}
    	```
    	* **FORM\_ENCODED payload type** – Use the HTML form
    	 names.


    	For example, for an HTML form with user and password input elements named
    	 `username1` and `password1`, the
    	 username field specification is `username1` and the
    	 password field specification is `password1`.
    5. If you're protecting Amazon CloudFront distributions, then under **Response
     inspection**, specify how your application indicates
     success or failure in its responses to account creation attempts.


    ###### Note

    ACFP response inspection is available only in protection packs (web ACLs) that protect CloudFront distributions.


    Specify a single component in the account
     creation response that you want ACFP to inspect. For the
     **Body** and **JSON** component
     types, AWS WAF can inspect the first 65,536 bytes (64 KB) of the
     component.


    Provide your inspection criteria for the component type, as indicated by the interface.
     You must provide both success and failure criteria to inspect for in the component.


    For example, say your application indicates the status of an account creation attempt in
     the status code of the response, and uses `200 OK` for
     success and `401 Unauthorized` or `403 Forbidden`
     for failure. You would set the response inspection **Component
     type** to **Status code**, then in the
     **Success** text box enter `200` and in
     the **Failure** text box, enter `401` on the
     first line and `403` on the second.


    The ACFP rule group only counts responses that match your success or failure
     inspection criteria. The rule group rules act on clients while they have
     too high a success rate among the responses that are counted, in order
     to mitigate bulk account creation attempts. For accurate behavior by the
     rule group rules, be sure to provide complete information for both
     successful and failed account creation attempts.


    To see the rules that inspect account creation responses, look for
     `VolumetricIPSuccessfulResponse` and
     `VolumetricSessionSuccessfulResponse` in the rules
     listing at [AWS WAF Fraud Control account creation fraud prevention (ACFP) rule group](aws-managed-rule-groups-acfp.md "aws-managed-rule-groups-acfp.md").

3. Provide any additional configuration that you want for the rule group.

You can further limit the scope of requests that the rule group inspects by adding a
scope-down statement to the managed rule group statement. For example, you can
inspect only requests with a specific query argument or cookie. The rule group
will only inspect requests that match the criteria in your scope-down statement
and that are sent to the account registration and account creation paths that
you specified in the rule group configuration. For information about scope-down
statements, see [Using scope-down statements in AWS WAF](waf-rule-scope-down-statements.md "waf-rule-scope-down-statements.md"). 4. Save your changes to the protection pack (web ACL).
Before you deploy your ACFP implementation for production traffic, test and tune it in
a staging or testing environment until you are comfortable with the potential impact to
your traffic. Then test and tune the rules in count mode with your production traffic
before enabling them. See the section that follows for guidance.
