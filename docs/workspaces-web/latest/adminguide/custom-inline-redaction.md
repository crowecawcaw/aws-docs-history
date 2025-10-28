# Custom inline redaction in Amazon WorkSpaces Secure Browser

Customers can define their own patterns using regular expression, such as custom internal
application IDs. To create your custom inline redaction pattern, follow these steps:

1. Go to your data protection setting.
2. Choose **Custom inline redaction** and **add**.
3. Enter a name for the custom data type.
4. Enter your regular expression value.
   - Regular expression values must match the JavaScript regular expression literal syntax.
     For more information, see [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions"). An example regular expression is
     `/ex[am]+ple/i`.
   - Make sure to test your custom patterns on the websites that you plan on supporting. If
     custom patterns are written with errors, they can introduce unintended performance
     issues.

5. Specify the replacement value.
6. Choose **More options** for more optional customizations, including the
   following:
   - Add **keywords** to fine tune the redaction logic. Keywords can
     increase the accuracy of enforcement. Add keywords in the Javascript regular expression
     literal syntax. For more information, see [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions").

   For example, if you are creating a custom redaction pattern for client IDs used in an
   internal system, you can add `/client name/i` to the keyword field to inform the
   scanning and detection logic.
   - Apply **URL enforcement overrides** to fine-tune the way redaction is
     applied across URLs, without changing the default configuration.

   For example, you can set use URL overrides to enforce email address redaction in your
   customer relationship management system, without breaking user access to email addresses in
   the company directory website or web-based email.
   - Enter a **description** (optional) for the data type.
