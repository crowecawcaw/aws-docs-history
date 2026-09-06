

# Updating the bundle
<a name="sdk-without-package-manager-updating"></a>

When a new version of the SDK is released:

1. Navigate to your build project directory

1. Update the SDK packages:

   ```
   npm update @amazon-connect/core @amazon-connect/contact @amazon-connect/email
   ```

1. Rebuild the bundle:

   ```
   npm run build
   ```

1. Copy the new bundle to your website

1. Test your application to verify compatibility