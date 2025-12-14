**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# CAPTCHA JavaScript API

specification

This section lists the specification for the methods and properties of the CAPTCHA JavaScript APIs. Use the
CAPTCHA JavaScript APIs to run custom CAPTCHA puzzles in your client applications.

This API builds on the intelligent threat APIs, which you use to configure and manage AWS WAF token
acquisition and use. See [Intelligent threat API
specification](waf-js-challenge-api-specification.md "waf-js-challenge-api-specification.md"). .

**`AwsWafCaptcha.renderCaptcha(container,
 configuration)`**

Presents an AWS WAF CAPTCHA puzzle to the end user and, upon success, updates the
client token with the CAPTCHA validation. This is available only
with the CAPTCHA integration. Use this call along with the
intelligent threat APIs to manage token retrieval and to provide the
token in your `fetch` calls. See the intelligent threat
APIs at [Intelligent threat API
specification](waf-js-challenge-api-specification.md "waf-js-challenge-api-specification.md").

Unlike the CAPTCHA interstitial that AWS WAF sends, the CAPTCHA puzzle rendered by this method displays the puzzle immediately, without an initial title screen.

**`container`**

The `Element` object for the target
container element on the page. This is commonly
retrieved by calling
`document.getElementById()` or
`document.querySelector()`.

Required: Yes

Type: `Element`

**configuration**

An object containing CAPTCHA configuration settings, as follows:

**`apiKey`**

The encrypted API key that enables
permissions for the client's domain. Use the AWS WAF
console to generate your API keys for your client
domains. You can use one key for up to five
domains. For information, see [Managing API keys for the JS CAPTCHA API](waf-js-captcha-api-key.md "waf-js-captcha-api-key.md").

Required: Yes

Type: `string`

**`onSuccess:
 (wafToken: string) => void;`**

Called with a valid AWS WAF token when the end
user successfully completes a CAPTCHA puzzle.
Use the token in the requests that you send to the
endpoints that you protect with an AWS WAF protection pack (web ACL).
The token provides proof and the timestamp of the
latest successful puzzle completion.

Required: Yes

**`onError?: (error:
 CaptchaError) => void;`**

Called with an error object when an error
occurs during the CAPTCHA operation.

Required: No

**`CaptchaError` class
definition** – The
`onError` handler supplies an error
type with the following class definition.

```
CaptchaError extends Error {
    kind: "internal_error" | "network_error" | "token_error" | "client_error";
    statusCode?: number;
}
```

- `kind` – The kind of error
  returned.
- `statusCode` – The HTTP
  status code, if available. This is used by
  `network_error` if the error is due to
  an HTTP error.

**`onLoad?: () =>
 void;`**

Called when a new CAPTCHA puzzle
loads.

Required: No

**`onPuzzleTimeout?:
 () => void;`**

Called when a CAPTCHA puzzle isn't
completed before it expires.

Required: No

**`onPuzzleCorrect?:
 () => void;`**

Called when a correct answer is provided to
a CAPTCHA puzzle.

Required: No

**`onPuzzleIncorrect?: () =>
 void;`**

Called when an incorrect answer is provided
to a CAPTCHA puzzle.

Required: No

**`defaultLocale`**

The default locale to use for the CAPTCHA puzzle.
The written instructions for CAPTCHA puzzles are available in Arabic (ar-SA), simplified Chinese (zh-CN), Dutch (nl-NL), English (en-US), French (fr-FR), German (de-DE), Italian (it-IT), Japanese (ja-JP), Brazilian Portuguese (pt-BR), Spanish (es-ES), and Turkish (tr-TR).
Audio instructions are available for all of the written languages except Chinese and Japanese, which default to English. To
change the default language, provide the
international language and locale code, for
example, `ar-SA`.

Default: The language currently in use in
the end user's browser

Required: No

Type: `string`

**`disableLanguageSelector`**

If set to `true`, the CAPTCHA
puzzle hides the language selector.

Default: `false`

Required: No

Type: `boolean`

**`dynamicWidth`**

If set to `true`, the CAPTCHA
puzzle changes width for compatibility with the
browser window width.

Default: `false`

Required: No

Type: `boolean`

**`skipTitle`**

If set to `true`, the CAPTCHA
puzzle doesn't display the puzzle title heading
**Solve the puzzle**.

Default: `false`

Required: No

Type: `boolean`
