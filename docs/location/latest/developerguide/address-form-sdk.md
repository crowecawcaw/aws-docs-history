# Address Form SDK

The Address Form SDK streamlines building smart address-entry forms. Address forms built with the SDK provide relevant address suggestions as users begin typing. When a user selects a suggestion, an address form automatically fills in fields such as city, state, and postal code. This reduces errors and speeds up data entry by minimizing manual input. Users can also preview the selected address on a map and adjust its location pin to indicate specific entrances or pick-up locations, significantly improving accuracy.

![Address Form SDK demonstration showing autocomplete functionality](/images/location/latest/developerguide/images/address-form-demo.gif)

## Try It

### Demo

Try the fully functional [address form demo](https://aws-geospatial.github.io/address-form-sdk-js/ "https://aws-geospatial.github.io/address-form-sdk-js/").

### Build It Yourself

Jump to [Getting Started](#address-form-getting-started "#address-form-getting-started") to begin implementing address forms using the Address Form SDK, or try the no-code approach with the Location Service’s WYSIWYG [Address Form Builder wizard](https://console.aws.amazon.com/location/solution-builder/home#/address-form "https://console.aws.amazon.com/location/solution-builder/home#/address-form"), powered by this SDK and accessible in the Amazon Location Service console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/ "https://console.aws.amazon.com/location/"). This interactive wizard lets you create customized forms with predictive suggestions, automatic field population, and flexible layouts. Developers can download ready-to-use packages in React JavaScript, React TypeScript, or standalone HTML/JavaScript for easy integration without writing any code.

## Key Features

Key features of the Address Form SDK include:

- Provides built-in typeahead suggestions for addresses and POIs, speeding up data entry.
- Enables configurable place-type search (e.g., postal codes, localities) for more precise results.
- Offers automatic browser location detection to quickly center users on their current area.
- Displays built-in map visualizations for greater clarity and context.
- Allows address locations to be adjusted on the map without losing the system-provided location, ensuring both accuracy and control.
- Includes a WYSIWYG builder tool that requires no coding, saving time and effort.
- Implements debouncing and caching for typeahead APIs to optimize performance and reduce costs.
- Supports style customization to match your application's brand and user experience.

It uses the following Amazon Location Service API operations to provide address information to address forms:

**[GetTile](../APIReference/API_geomaps_GetTile.md "../APIReference/API_geomaps_GetTile.md")**

Retrieves map tiles for rendering the interactive map to visualize the location of the address and adjust the position of an address.

**[Autocomplete](../APIReference/API_geoplaces_Autocomplete.md "../APIReference/API_geoplaces_Autocomplete.md")**

Provides real-time address suggestions as users type.

**[Suggest](../APIReference/API_geoplaces_Suggest.md "../APIReference/API_geoplaces_Suggest.md")**

Provides real-time address and POI suggestions as users type.

**[ReverseGeocode](../APIReference/API_geoplaces_ReverseGeocode.md "../APIReference/API_geoplaces_ReverseGeocode.md")**

Converts a user's current location to the nearest known address address if they choose to auto-fill their address based on their current location.

**[GetPlace](../APIReference/API_geoplaces_GetPlace.md "../APIReference/API_geoplaces_GetPlace.md")**

Retrieves detailed place information for selected addresses after selecting an address from the results of the Autocomplete or Suggest API.

## Pricing

The SDK is free and [open sourced](https://github.com/aws-geospatial/address-form-sdk-js "https://github.com/aws-geospatial/address-form-sdk-js") under the Apache-2.0 license. You only pay for API usage. Please consult the [Amazon Location Service pricing page](https://aws.amazon.com/location/pricing/ "https://aws.amazon.com/location/pricing/").

## Getting Started

The Address Form SDK can be used within a React app or in a standalone HTML and JavaScript page. Get started by following the instructions below.

### Prerequisites

###### Note

The Address Form SDK requires an API key with the required permissions to work properly. Create an API key with the following permissions using the [Address Form SDK Builder wizard](https://console.aws.amazon.com/location/solution-builder/home#/address-form "https://console.aws.amazon.com/location/solution-builder/home#/address-form") in Amazon Location Service console, or follow the instructions below to create it manually.

Use of the Address Form SDK requires the following actions to be allowed in the API key policy:

- `geo-maps:GetTile` - This is required when displaying the map component. See the [GetTile](../APIReference/API_geomaps_GetTile.md "../APIReference/API_geomaps_GetTile.md") API reference.
- `geo-places:Autocomplete` - This is required when using the `Autocomplete` operation for typeahead functionality. See the [Autocomplete](../APIReference/API_geoplaces_Autocomplete.md "../APIReference/API_geoplaces_Autocomplete.md") API reference.
- `geo-places:Suggest` - This is required when using the `Suggest` operation for typeahead functionality. See the [Suggest](../APIReference/API_geoplaces_Suggest.md "../APIReference/API_geoplaces_Suggest.md") API reference.
- `geo-places:ReverseGeocode` - This is required when allowing users to provide their current location using browsers' geolocation API. See the [ReverseGeocode](../APIReference/API_geoplaces_ReverseGeocode.md "../APIReference/API_geoplaces_ReverseGeocode.md") API reference.
- `geo-places:GetPlace` - This is required when using the typeahead functionality. See the [GetPlace](../APIReference/API_geoplaces_GetPlace.md "../APIReference/API_geoplaces_GetPlace.md") API reference.

Follow the [Use API Keys to authenticate](using-apikeys.md "using-apikeys.md") guide to create an Amazon Location Service API key with the necessary permissions.

Example key policy for the [CreateKey](../APIReference/API_geotags_CreateKey.md "../APIReference/API_geotags_CreateKey.md") API with required permissions:

```

{
  "KeyName": "ExampleKey",
  "ExpireTime": "YYYY-MM-DDThh:mm:ss.sss",
  "Restrictions": {
    "AllowActions": [
      "geo-maps:GetTile",
      "geo-places:Autocomplete",
      "geo-places:Suggest",
      "geo-places:GetPlace",
      "geo-places:ReverseGeocode"
    ],
    "AllowResources": [
      "arn:aws:geo-maps:<Region>::provider/default",
      "arn:aws:geo-places:<Region>::provider/default"
    ]
  }
}

```

### Installation

#### HTML/JavaScript

Include the following CSS and JavaScript for the SDK in your HTML code

```

...
<head>
...
<link
rel="stylesheet"
href="https://cdn.jsdelivr.net/npm/@aws/address-form-sdk-js/dist/standalone/address-form-sdk.css"
/>
...
</head>
...
<body>
...
<script src="https://cdn.jsdelivr.net/npm/@aws/address-form-sdk-js/dist/standalone/address-form-sdk.umd.js"></script>
</body>
...

```

#### React

Install the SDK from npm: `npm install @aws/address-form-sdk-js`

### Use the SDK

Add the following code to your React app. Update `AMAZON_LOCATION_API_KEY` with your API key and `AMAZON_LOCATION_REGION` with the region where the API key was created. When the form is submitted, the `onSubmit` callback provides a `getData` async function. Call this function with an `intendedUse` value to retrieve the form data.

```

onSubmit: async (getData) => {
  const data = await getData({
    intendedUse: "SingleUse", // or "Storage"
  });
};

```

###### Note

Use `"Storage"` if you need to store or cache the results. This ensures compliance with Amazon Location Service [intended use requirements](places-intended-use.md "places-intended-use.md").

HTML/JavaScript

```

<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Address Form</title>
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/@aws/address-form-sdk-js/dist/standalone/address-form-sdk.css"
    />
  </head>
  <body>
    <form
      id="amazon-location-address-form"
      class="address-form flex-row flex-1"
    >
      <div class="flex-column">
        <input
          data-type="address-form"
          name="addressLineOne"
          data-api-name="suggest"
          data-show-current-location="true"
        />
        <input data-type="address-form" name="addressLineTwo" />
        <input data-type="address-form" name="city" />
        <input data-type="address-form" name="province" />
        <input data-type="address-form" name="postalCode" />
        <input data-type="address-form" name="country" />
        <div class="flex-row">
          <button data-type="address-form" type="submit">Submit</button>
          <button data-type="address-form" type="reset">Reset</button>
        </div>
      </div>
      <div data-type="address-form" data-map-style="Standard,Light"></div>
    </form>
    <></script>
script src="https://cdn.jsdelivr.net/npm/@aws/address-form-sdk-js/dist/standalone/address-form-sdk.umd.js"
    <script>
      AddressFormSDK.render({
        root: "#amazon-location-address-form",
        apiKey: "AMAZON_LOCATION_API_KEY",
        region: "AMAZON_LOCATION_REGION",
        showCurrentCountryResultsOnly: true,
        onSubmit: async (getData) => {
          // Get form data with intendedUse parameter
          // Use "SingleUse" for one-time display only
          // Use "Storage" if you plan to store/cache the results - makes an extra API call to grant storage rights
          const data = await getData({ intendedUse: "SingleUse" });
          console.log(data);
        },
      });
    </script>
  </body>
</html>

```

React

```

import React from 'react';
import { AddressForm, Flex } from "@aws/address-form-sdk-js";

export default function App() {
  return (
    <AddressForm
      apiKey="AMAZON_LOCATION_API_KEY"
      region="AMAZON_LOCATION_REGION"
      onSubmit={async (getData) => {
        // Get form data with intendedUse parameter
        // Use "SingleUse" for one-time display only
        // Use "Storage" if you plan to store/cache the results - makes an extra API call to grant storage rights
        const data = await getData({ intendedUse: "SingleUse" });
        console.log(data);
      }}
    >
      <Flex
        direction="row"
        flex
      >
        <Flex direction="column">
          <input
            data-api-name="autocomplete"
            data-type="address-form"
            name="addressLineOne"
            placeholder="Enter address"
          />
          <input
            data-type="address-form"
            name="addressLineTwo"
          />
          <input
            data-type="address-form"
            name="city"
            placeholder="City"
          />
          <input
            data-type="address-form"
            name="province"
            placeholder="State/Province"
          />
          <input
            data-type="address-form"
            name="postalCode"
          />
          <input
            data-type="address-form"
            name="country"
            placeholder="Country"
          />
          <Flex direction="row">
            <button address-form="submit">
              Submit
            </button>
            <button address-form="reset">
              Reset
            </button>
          </Flex>
        </Flex>
        <AddressFormMap
          mapStyle={[
            'Standard',
            'Light'
          ]}
         />
      </Flex>
    </AddressForm>
  );
}

```

## Supported Countries

The Address Form SDK supports auto-filling addresses globally using Amazon Location Service. The following countries have full support with address field parsing, where each address component is populated into its respective field:

- Australia (AU)
- Canada (CA)
- France (FR)
- Hong Kong (HK)
- Ireland (IE)
- New Zealand (NZ)
- Philippines (PH)
- Singapore (SG)
- United Kingdom (GB)
- United States (US)

All other countries are in Preview status. Preview countries display the complete address in `addressLineOne` field without country-specific formatting. Future releases will improve this behavior and you can access these improvements by using the latest version of the SDK.

## Supported AWS Regions

The Address Form SDK and Address Form Builder wizard are available in all AWS regions where Amazon Location Service operates, using the `Current` version of its APIs. View the complete list of supported regions in [Amazon Location supported regions](location-regions.md "location-regions.md").

## API Reference

Refer to [README API Reference](https://github.com/aws-geospatial/address-form-sdk-js#api-reference "https://github.com/aws-geospatial/address-form-sdk-js#api-reference").
