**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# AWS WAF token characteristics

Each token has the following characteristics:

- The token is stored in a cookie named `aws-waf-token`.
- The token is encrypted.
- The token fingerprints the client session with a sticky granular identifier
  that contains the following information:

      + The timestamp of the client's latest successful response to a silent challenge.
      + The timestamp of the end user's latest successful response to a CAPTCHA. This
       is only present if you use CAPTCHA in your protections.
      + Additional information about the client and client behavior that can help separate your
       legitimate clients from unwanted traffic. The information includes
       various client identifiers and client-side signals that can be used to
       detect automated activities. The information gathered is non-unique and
       can't be mapped to an individual human being.




      	- All tokens include data from client browser interrogation,
      	 such as indications of automation and browser setting
      	 inconsistencies. This information is retrieved by the scripts
      	 that are run by the Challenge action and by the client
      	 application SDKs. The scripts actively interrogate the browser
      	 and put the results into the token.
      	- Additionally, when you implement a client application integration SDK, the token
      	 includes passively collected information about the end user's
      	 interactivity with the application page. Interactivity includes
      	 mouse movements, key presses, and interactions with any HTML
      	 form that's present on the page. This information helps AWS WAF
      	 detect the level of human interactivity in the client, to
      	 challenge users that do not seem to be human. For information
      	 about client side integrations, see [Client application
      	 integrations in AWS WAF](waf-application-integration.md "waf-application-integration.md").

  For security reasons, AWS doesn't provide a complete description of the contents of
  AWS WAF tokens or detailed information about the token encryption process.
