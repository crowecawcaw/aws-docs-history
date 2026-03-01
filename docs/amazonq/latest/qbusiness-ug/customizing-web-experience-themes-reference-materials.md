# Reference materials for customizing the visual theme

###### Topics

- [Color considerations for accessibility](#customizing-web-experience-themes-color-format "#customizing-web-experience-themes-color-format")
- [Choosing Color Values for Your Theme](#reference-materials-color-values "#reference-materials-color-values")
- [Supported Root CSS Variables](#customizing-web-experience-themes-reference-materials-supported-css-variables "#customizing-web-experience-themes-reference-materials-supported-css-variables")
- [Example](#customizing-web-experience-themes-examples "#customizing-web-experience-themes-examples")

## Color considerations for accessibility

When customizing your Amazon Q web experience, it's crucial to prioritize
accessibility. Ensure sufficient contrast is there between the text and background
colors. Use tools like the [WebAIM Contrast
Checker](https://webaim.org/resources/contrastchecker/ "https://webaim.org/resources/contrastchecker/") to verify your color choices meet Web Content Accessibility
Guidelines (WCAG) 2.x standards.

For comprehensive accessibility guidelines, refer to the [Web Content Accessibility Guidelines
(WCAG)](https://www.w3.org/TR/WCAG21/ "https://www.w3.org/TR/WCAG21/").

## Choosing Color Values for Your Theme

Amazon Q supports the following color value formats:

- Hexadecimal colors (with and without transparency)
- RGB and RGBA colors
- HSL and HSLA colors
- Predefined/Cross-browser color names

###### Note

Amazon Q Business doesn't support `currentcolor`. For a comprehensive list
of supported CSS color values, see [W3Schools CSS
Colors](https://www.w3schools.com/cssref/css_colors_legal.php "https://www.w3schools.com/cssref/css_colors_legal.php")

## Supported Root CSS Variables

Only the following root CSS variables are supported:

```
--black
--white
--foreground
--primary
--primary-foreground
--secondary
--secondary-foreground
--card
--card-foreground
--popover
--popover-foreground
--tooltip
--tooltip-foreground
--muted
--muted-foreground
--accent
--accent-foreground
--info
--info-foreground
--success
--success-foreground
--warning
--warning-foreground
--error
--error-foreground
--destructive
--destructive-foreground
--border
--input
--ring
--radius

--background
--qbusiness-webexperience-title-color
--qbusiness-webexperience-font-typeface
--qbusiness-webexperience-chat-user-background-color
--qbusiness-webexperience-chat-user-text-color
--qbusiness-webexperience-chat-agent-background-color
--qbusiness-webexperience-chat-agent-text-color
--qbusiness-webexperience-chat-logo-visibility
--qbusiness-webexperience-logo-url
--qbusiness-webexperience-font-url
--qbusiness-webexperience-favicon-url

```

## Example

### CSS

The following is an example of a valid CSS file setting the visual theme for
Amazon Q Business.

```

:root {
  --background: #FFFFFF;
  --qbusinesness-webexperience-title-color: #9013FE;
  --qbusiness-webexperience-font-typeface: Custom Font;
  --qbusiness-webexperience-chat-user-background-color: #7ED321;
  --qbusiness-webexperience-chat-user-text-color: #344054;
  --qbusiness-webexperience-chat-agent-background-color: #FFFFFF;
  --qbusiness-webexperience-chat-agent-text-color: #344054;
  --qbusiness-webexperience-chat-logo-visibility: hidden;
  --qbusiness-webexperience-logo-url: "https://<bucket_name>.s3.<region>.amazonaws.com/<logo_name>.png";
  --qbusiness-webexperience-font-url: "https://<bucket_name>.s3.<region>.amazonaws.com/<font_name>.ttf";
  --qbusiness-webexperience-favicon-url: "https://<bucket_name>.s3.<region>.amazonaws.com/<favicon_name>.ico";
}

```
