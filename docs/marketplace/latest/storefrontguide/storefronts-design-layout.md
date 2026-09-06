

# Design and layout
<a name="storefronts-design-layout"></a>

Choose a layout type and customize your storefront's design, branding, and content sections.

## Layout types
<a name="layout-types"></a>

When you create a storefront, you choose a layout type that determines the structure, appearance, and deployment model. Each layout type is designed for a specific use case.

### Available layout types
<a name="layout-types-available"></a>

Under **Layout Style**, the following options are available:

#### Standalone
<a name="layout-types-standalone"></a>

A full-page storefront deployed on a dedicated domain or subdomain. Use this layout when you want an independent storefront that functions as its own web destination.

#### Embedded
<a name="layout-types-embedded"></a>

A storefront designed to integrate within an existing web page through an iframe. This layout preserves your current website architecture while adding commerce capabilities to a designated section.

#### Ecommerce
<a name="layout-types-ecommerce"></a>

A product-grid layout with a shopping-style browsing experience. This layout includes a banner section and optimized product tiles for high-volume catalogs.

#### Campaign
<a name="layout-types-campaign"></a>

A landing-page layout optimized for demand generation and targeted marketing. This layout includes hero sections, featured product highlights, resource sections, and value proposition elements.

### Changing the layout type
<a name="layout-types-changing"></a>

You can change the layout type at any time before or after deployment. When you change the layout type, the storefront restructures to match the new layout. Product selections and tag configurations are preserved.

1. Open the storefront and choose the **Design** tab.

1. Under **Layout Style**, choose a different layout option.

1. Choose **Save**.

### Filter panel styles
<a name="layout-types-filter-panel"></a>

Under **Options**, the **Filters** control offers **Compact** and **Accordion**. The **Products Size** control offers **Small**, **Medium**, and **Large**.

### Product tile sizes
<a name="layout-types-tile-sizes"></a>

You can control the size of product tiles on the storefront home page:
+ **Small** - Compact tiles, more products visible per row.
+ **Medium** - Balanced tile size (default).
+ **Large** - Prominent tiles with more detail visible.

### Related topics
<a name="layout-types-related"></a>
+ Creating a storefront
+ [Color and theme customization](#color-and-theme-customization)
+ [Campaign layout](#campaign-layout)
+ [E-Commerce layout](#ecommerce-layout)

## Campaign layout
<a name="campaign-layout"></a>

The Campaign layout creates a landing-page style storefront optimized for demand generation, product launches, and marketing campaigns. It includes configurable sections for hero content, featured products, video, value propositions, and resources.

### Campaign layout sections
<a name="campaign-layout-sections"></a>

A Campaign storefront is composed of the following sections, each independently configurable:

#### Hero section
<a name="campaign-layout-hero"></a>

The top banner area that provides the first impression for visitors.
+ **Headline** - Primary message
+ **Sub headline** - Supporting text
+ **Banner url** - Upload or provide a URL for the banner image
+ **Favicon url** - Upload or provide a URL for the favicon

#### Logo
<a name="campaign-layout-logo"></a>

The logo configuration for the Campaign layout header. See [Logo and home button](#logo-and-home-button) for field details.

#### Home button
<a name="campaign-layout-home-button"></a>

The home button configuration for the Campaign layout header. See [Logo and home button](#logo-and-home-button) for field details.

#### Product section
<a name="campaign-layout-product"></a>

The Product section has a **Section header** field; the default value is Featured Products.

#### Video and value proposition
<a name="campaign-layout-video"></a>

An optional section to communicate key benefits through video and structured messaging.
+ **Video embed URL** - Embed a video (YouTube, Vimeo, or direct URL)
+ **Value Proposition** - Up to 4 benefit statements with icons or short descriptions

For more information, see [Video and value propositions](#video-and-value-propositions).

#### Resources section
<a name="campaign-layout-resources"></a>

A section to link external content such as whitepapers, case studies, or documentation. Each resource card has the following fields:
+ **Title**
+ **Description**
+ **Link label**
+ **Link URL**

### To configure a Campaign layout
<a name="campaign-layout-configure"></a>

1. Open the storefront and choose the **Design** tab.

1. Choose **Campaign** as the layout style.

1. Configure each section using the form panels that appear:
   + Complete the **Hero section** fields
   + Configure the **Product section**
   + (Optional) Add a **Video embed URL** and **Value Proposition** entries
   + (Optional) Add **Resources**

1. Choose **Save**.

1. Preview the storefront to verify the layout before deploying.

### Related topics
<a name="campaign-layout-related"></a>
+ [Layout types](#layout-types)
+ [Video and value propositions](#video-and-value-propositions)
+ [Color and theme customization](#color-and-theme-customization)

## E-Commerce layout
<a name="ecommerce-layout"></a>

The E-Commerce layout provides a product-grid browsing experience with a banner section, optimized for storefronts with large catalogs where buyers compare and evaluate multiple products.

### E-Commerce layout features
<a name="ecommerce-layout-features"></a>
+ **Banner Section** - A configurable header area with branding and messaging
+ **Product grid** - A responsive grid of product tiles with filtering and sorting
+ **Filter sidebar** - Category and tag-based filtering for quick navigation
+ **Search** - Full-text search across product titles and descriptions

### To configure an E-Commerce layout
<a name="ecommerce-layout-configure"></a>

1. Open the storefront and choose the **Design** tab.

1. Choose **Ecommerce** as the layout style.

1. Configure the **Banner Section**:
   + **Main headline** - The primary heading text for the banner
   + **Welcome message** - Supporting text displayed below the headline
   + **Headline overlay size (%)** - The percentage of banner width the headline occupies
   + **Headline alignment** - Position the headline to the left, center, or right

1. Configure **Product grid settings**:
   + Choose the default product tile size (Small, Medium, or Large)
   + Configure the number of products per row
   + Enable or disable price display on tiles

1. Choose **Save**.

### When to use E-Commerce layout
<a name="ecommerce-layout-when"></a>

Use this layout when:
+ Your catalog contains many products
+ Buyers need to browse, compare, and filter across categories
+ You want a familiar shopping experience with minimal custom content sections

For storefronts with fewer products or where marketing messaging is more important, consider the Campaign layout or Standalone layout.

### Related topics
<a name="ecommerce-layout-related"></a>
+ [Layout types](#layout-types)
+ Importing products
+ Categories and badges

## Color and theme customization
<a name="color-and-theme-customization"></a>

You can customize the color palette of your storefront to match your organization's branding. Access the **Colors** section on the Design tab to configure your storefront colors.

### Configurable color elements
<a name="color-and-theme-elements"></a>

The following color elements are configurable:
+ **Primary Color**
+ **Button Color**
+ **Headline Color**

### To customize colors
<a name="color-and-theme-customize"></a>

1. Open the storefront and choose the **Design** tab.

1. Scroll to the **Colors** section.

1. For each color element, choose the color square to open the color picker. The color picker provides an HSV gradient and a hue slider.

1. Choose **Save** to apply the color.

### Best practices
<a name="color-and-theme-best-practices"></a>
+ Maintain sufficient contrast between text and background colors for readability.
+ Use your organization's primary brand color for the Primary Color setting.
+ Test colors on both desktop and mobile viewports.

### Related topics
<a name="color-and-theme-related"></a>
+ [Layout types](#layout-types)
+ [Logo and home button](#logo-and-home-button)

## Logo and home button
<a name="logo-and-home-button"></a>

You can configure a custom logo and home button for your storefront header. The logo represents your organization's brand, and the home button provides navigation back to the storefront's main page or an external URL.

### To configure the logo
<a name="logo-and-home-button-logo"></a>

1. Open the storefront and choose the **Design** tab.

1. In the **Logo** section, enter the **Logo url**. Paste the URL or choose **Upload** to upload an image.

1. Choose **Save**.

The logo appears in the top-left corner of the storefront header.

### Logo requirements
<a name="logo-and-home-button-requirements"></a>
+ Format: PNG, SVG, or JPEG
+ Suggested size: 50-200 x 50 px.
+ Must be hosted on a publicly accessible URL (HTTPS)

### To configure the home button
<a name="logo-and-home-button-home"></a>

The home button appears in the storefront header and provides a click-through destination.

1. Open the storefront and choose the **Design** tab.

1. In the **Home Button** section, configure the following fields:
   + **Redirect logo URL** - The destination URL when buyers choose the logo
   + **Open in existing tab** - When enabled, the link opens in the current browser tab instead of a new tab

1. Choose **Save**.

### Related topics
<a name="logo-and-home-button-related"></a>
+ [Color and theme customization](#color-and-theme-customization)
+ [Layout types](#layout-types)
+ [Privacy policy](#privacy-policy)

## Privacy policy
<a name="privacy-policy"></a>

The Privacy Policy section has an enable toggle and three fields: **Privacy Policy URL**; **Footer Disclaimer**; **Form Disclaimer**.

### To configure the privacy policy
<a name="privacy-policy-configure"></a>

1. Open the storefront and choose the **Design** tab.

1. In the **Privacy Policy** section, use the toggle to enable the feature, then complete the following fields:
   + **Privacy Policy URL** - Enter a link to your organization's privacy policy page.
   + **Footer Disclaimer** - Enter disclaimer text for the storefront footer.
   + **Form Disclaimer** - Enter disclaimer text displayed on forms.

1. Choose **Save**.

### Notes
<a name="privacy-policy-notes"></a>
+ Providing a privacy policy is recommended for all storefronts that collect buyer information or use cookies.
+ The Privacy Policy URL must be publicly accessible (HTTPS).
+ The link opens in a new browser tab when buyers choose it.

### Related topics
<a name="privacy-policy-related"></a>
+ [Logo and home button](#logo-and-home-button)
+ Deployment

## Video and value propositions
<a name="video-and-value-propositions"></a>

You can add video content and structured value proposition statements to your storefront. These elements help communicate benefits to buyers and are available in the Campaign and Standalone layout types.

### Value Proposition Section
<a name="video-and-value-propositions-video"></a>

Use the toggle on the right to enable or disable this section.

1. Open the storefront and choose the **Design** tab.

1. In the **Value Proposition Section**, enter the **Video embed URL**.

   Supported sources:
   + YouTube (embed URL format)
   + Vimeo
   + Direct video file URL (MP4)

1. Choose **Save**.

The video appears as an embedded player in the designated section of the storefront.

### Adding value propositions
<a name="video-and-value-propositions-vp"></a>

Value propositions are short benefit statements displayed alongside the video or in a dedicated section. They communicate why buyers should use your storefront.

1. Open the storefront and choose the **Design** tab.

1. In the **Value Proposition** section, add up to 4 entries. For each entry:
   + **Title** - A short headline
   + **Description** - One to two sentences explaining the benefit

1. Choose **Save**.

### Display behavior
<a name="video-and-value-propositions-display"></a>
+ On Campaign layouts, value propositions appear in a dedicated section below the hero and video.
+ On Standalone layouts, value propositions appear below the product catalog section.
+ On Embedded and E-Commerce layouts, value propositions are not displayed.

### Related topics
<a name="video-and-value-propositions-related"></a>
+ [Campaign layout](#campaign-layout)
+ [Layout types](#layout-types)