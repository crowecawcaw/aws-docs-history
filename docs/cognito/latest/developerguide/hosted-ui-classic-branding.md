# Customizing hosted UI (classic)

branding

You can use the AWS Management Console, or the AWS CLI or API, to specify classic customization
settings for the hosted UI. You can upload a custom logo image to be displayed in the
app. You can also apply some cascading style sheets (CSS) options to the look and feel
of the UI.

You can customize the UI defaults and override individual [app clients](cognito-terms.md#term-appclient "cognito-terms.md#term-appclient") with specific settings. Amazon Cognito applies
the default configuration to every app client that doesn't have client-level
settings.

In the Amazon Cognito console and in API requests, the request that sets your UI customization
must not exceed 135 KB in size. In rare cases, the sum of request headers, your CSS
file, and your logo might exceed 135KB. Amazon Cognito encodes the image file to Base64. This
increases the size of a 100 KB image to 130 KB, keeping five KB for request headers and
your CSS. If the request is too large, the AWS Management Console or your
`SetUICustomization` API request returns a `request parameters too
 large` error. Adjust your logo image to be no greater than 100KB and your CSS
file to be no larger than 3 KB. You can't set CSS and logo customization
separately.

###### Note

To customize your UI, you must set up a domain for your user pool.

## Specifying a custom

logo in classic branding

Amazon Cognito centers your custom logo above the input fields at the [Login endpoint](login-endpoint.md "login-endpoint.md").

Choose a PNG, JPG, or JPEG file that can scale to 350 by 178 pixels for your
custom hosted UI logo. Your logo file can be no larger than 100 KB in size, or 130
KB after Amazon Cognito encodes to Base64. To set an `ImageFile` in [SetUICustomization](../../../cognito-user-identity-pools/latest/APIReference/API_SetUICustomization.md "../../../cognito-user-identity-pools/latest/APIReference/API_SetUICustomization.md") in the API, convert your file to
a Base64-encoded text string or, in the AWS CLI, provide a file path and let Amazon Cognito
encode it for you.

## Specifying CSS

customizations in classic branding

You can customize the CSS for the hosted app pages, with the following
restrictions:

- You can use any of the following CSS class names:
  - `background-customizable`
  - `banner-customizable`
  - `errorMessage-customizable`
  - `idpButton-customizable`
  - `idpButton-customizable:hover`
  - `idpDescription-customizable`
  - `inputField-customizable`
  - `inputField-customizable:focus`
  - `label-customizable`
  - `legalText-customizable`
  - `logo-customizable`
  - `passwordCheck-valid-customizable`
  - `passwordCheck-notValid-customizable`
  - `redirect-customizable`
  - `socialButton-customizable`
  - `submitButton-customizable`
  - `submitButton-customizable:hover`
  - `textDescription-customizable`

- Property values can contain HTML, except for the following values:
  `@import`, `@supports`, `@page`, or
  `@media` statements, or Javascript.

You can customize the following CSS properties.

**Labels**

- **font-weight** is a multiple of 100 from 100
  to 900.
- **color** is the text color. Must be a [legal CSS color value](https://www.w3schools.com/cssref/css_colors_legal.php "https://www.w3schools.com/cssref/css_colors_legal.php").

**Input fields**

- **width** is the width of the containing
  block as a percentage.
- **height** is the height of the input field
  in pixels (px).
- **color** is the text color. It can be any
  standard CSS color value.
- **background-color** is the background color
  of the input field. It can be any standard CSS color
  value.
- **border** is a standard CSS border value
  that specifies the width, transparency, and color of the border
  of your app window. Width can be any value from 1px to 100px.
  Transparency can be solid or none. Color can be any standard
  color value.

**Text descriptions**

- **padding-top** is the amount of padding
  above the text description.
- **padding-bottom** is the amount of padding
  below the text description.
- **display** can be `block` or
  `inline`.
- **font-size** is the font size for text
  descriptions.
- **color** is the text color. Must be a [legal CSS color value](https://www.w3schools.com/cssref/css_colors_legal.php "https://www.w3schools.com/cssref/css_colors_legal.php").

**Submit button**

- **font-size** is the font size of the button
  text.
- **font-weight** is the font weight of the
  button text: `bold`, `italic`, or
  `normal`.
- **margin** is a string of four values
  indicating the top, right, bottom, and left margin sizes for the
  button.
- **font-size** is the font size for text
  descriptions.
- **width** is the width of the button text in
  percent of the containing block.
- **height** is the height of the button in
  pixels (px).
- **color** is the button text color. It can be
  any standard CSS color value.
- **background-color** is the background color
  of the button. It can be any standard color value.

**Banner**

- **padding** is a string of four values
  indicating the top, right, bottom, and left padding sizes for
  the banner.
- **background-color** is the banner's
  background color. It can be any standard CSS color value.

**Submit button hover**

- **color** is the foreground color of the
  button when you hover over it. It can be any standard CSS color
  value.
- **background-color** is the background color
  of the button when you hover over it. It can be any standard CSS
  color value.

**Identity provider button hover**

- **color** is the foreground color of the
  button when you hover over it. It can be any standard CSS color
  value.
- **background-color** is the background color
  of the button when you hover over it. It can be any standard CSS
  color value.

**Password check not valid**

- **color** is the text color of the
  `"Password check not valid"` message. It can be
  any standard CSS color value.

**Background**

- **background-color** is the background color
  of the app window. It can be any standard CSS color
  value.

**Error messages**

- **margin** is a string of four values
  indicating the top, right, bottom, and left margin sizes.
- **padding** is the padding size.
- **font-size** is the font size.
- **width** is the width of the error message
  as a percentage of the containing block.
- **background** is the background color of the
  error message. It can be any standard CSS color value.
- **border** is a string of three values
  specifying the width, transparency, and color of the
  border.
- **color** is the error message text color. It
  can be any standard CSS color value.
- **box-sizing** is used to indicate to the
  browser what the sizing properties (width and height) should
  include.

**Identity provider buttons**

- **height** is the height of the button in
  pixels (px).
- **width** is the width of the button text as
  a percentage of the containing block.
- **text-align** is the text alignment setting.
  It can be `left`, `right`, or
  `center`.
- **margin-bottom** is the bottom margin
  setting.
- **color** is the button text color. It can be
  any standard CSS color value.
- **background-color** is the background color
  of the button. It can be any standard CSS color value.
- **border-color** is the color of the button
  border. It can be any standard CSS color value.

**Identity provider descriptions**

- **padding-top** is the amount of padding
  above the description.
- **padding-bottom** is the amount of padding
  below the description.
- **display** can be `block` or
  `inline`.
- **font-size** is the font size for
  descriptions.
- **color** is the text color for IdP section
  headers for example **Sign in with your corporate
  ID**. Must be a [legal CSS color value](https://www.w3schools.com/cssref/css_colors_legal.php "https://www.w3schools.com/cssref/css_colors_legal.php").

**Legal text**

- **color** is the text color. It can be any
  standard CSS color value.
- **font-size** is the font size.

###### Note

When you customize **Legal text**, you are
customizing the message **We won't post to any of your
accounts without asking first** that is displayed under
social identity providers in the sign-in page.

**Logo**

- **max-width** is the maximum width as a
  percentage of the containing block.
- **max-height** is the maximum height as a
  percentage of the containing block.
- **background-color** is the color of the
  background for logs with transparent sections. Must be a [legal CSS color value](https://www.w3schools.com/cssref/css_colors_legal.php "https://www.w3schools.com/cssref/css_colors_legal.php").

**Input field focus**

- **border-color** is the color of the input
  field. It can be any standard CSS color value.
- **outline** is the border width of the input
  field, in pixels.

**Social button**

- **height** is the height of the button in
  pixels (px).
- **text-align** is the text alignment setting.
  It can be `left`, `right`, or
  `center`.
- **width** is the width of the button text as
  a percentage of the containing block.
- **margin-bottom** is the bottom margin
  setting.

**Password check valid**

- **color** is the text color of the
  `"Password check valid"` message. It can be any
  standard CSS color value.

## Customizing the

hosted UI with classic branding in the AWS Management Console

You can use the AWS Management Console to specify UI customization settings for your
app.

###### Note

You can view the hosted UI with your customizations by constructing the
following URL, with the specifics for your user pool, and typing it into a
browser: `https://<`your_domain`>/login?response_type=code&client_id=<`your_app_client_id`>&redirect_uri=<`your_callback_url`>`
You may have to wait up to one minute to refresh your browser before changes
made in the console appear.

Your domain is shown on the **App integration** tab under
**Domain**. Your app client ID and callback URL are shown
under **App clients**.

###### To specify app UI customization settings

1. Sign in to the [Amazon Cognito
   console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home").
2. In the navigation pane, choose **User Pools**, and choose
   the user pool you want to edit.
3. [Create a domain](cognito-user-pools-assign-domain.md "cognito-user-pools-assign-domain.md")
   from the **Domain** tab, or update your existing domain.
   Under **Branding version**, set your domain to use
   **Hosted UI (classic)**.
4. Choose the **Managed login** menu.
5. To customize UI settings for all app clients, locate
   **Style** under **Hosted UI settings**
   and select **Edit**.
6. To customize UI settings for one app client, go to the **App
   clients** menu and select the app client you want to modify,
   then locate **Hosted UI (classic) style** and select
   **Override**. Select **Edit**.
7. To upload your own logo image file, choose **Choose
   file** or **Replace current file**.
8. To customize hosted UI CSS, download **CSS template.css**
   and modify the template with the values you want to customize. Only the keys
   that are included in the template can be used with the hosted UI. Added CSS
   keys will not be reflected in your UI. After you have customized the CSS
   file, choose **Choose file** or **Replace current
   file** to upload your custom CSS file.

## Customizing the

hosted UI with classic branding in the user pools API and with the AWS CLI

Use the following commands to specify app UI customization settings for your user
pool.

###### To get the UI customization settings for a user pool's built-in app UI, use

the following API operations.

- AWS CLI: `aws cognito-idp get-ui-customization`
- AWS API: [GetUICustomization](../../../cognito-user-identity-pools/latest/APIReference/API_GetUICustomization.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetUICustomization.md")

###### To set the UI customization settings for a user pool's built-in app UI, use

the following API operations.

- AWS CLI from image file: `aws cognito-idp set-ui-customization
--user-pool-id `<your-user-pool-id>`--client-id`<your-app-client-id>`
--image-file
fileb://"`<path-to-logo-image-file>`"
--css ".label-customizable{ color:
`<color>`;}"`
- AWS CLI with image encoded as Base64 binary text: `aws cognito-idp
set-ui-customization --user-pool-id
`<your-user-pool-id>`--client-id`<your-app-client-id>`--image-file`<base64-encoded-image-file>`--css
".label-customizable{ color:`<color>`;}"`
- AWS API: [SetUICustomization](../../../cognito-user-identity-pools/latest/APIReference/API_SetUICustomization.md "../../../cognito-user-identity-pools/latest/APIReference/API_SetUICustomization.md")
