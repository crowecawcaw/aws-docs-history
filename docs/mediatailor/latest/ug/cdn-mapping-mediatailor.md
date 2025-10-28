# Set up CDN mapping in MediaTailor

This section explains how to configure AWS Elemental MediaTailor to use your content delivery network
(CDN) domain names. After setting up your CDN routing behaviors, you need to update your
MediaTailor configuration to ensure that manifests reference your CDN domain instead of directly
referencing origin servers.

Configuring CDN mapping in MediaTailor ensures that all content and ad segment URLs in your
manifests point to your CDN rather than directly to origin servers. This step is essential
for creating a complete CDN delivery chain and maximizing the benefits of your CDN
integration.

## CDN mapping configuration in MediaTailor

After setting up your CDN routing behaviors, configure MediaTailor to use your CDN domain
names:

1. Open the [MediaTailor
   console](https://console.aws.amazon.com/mediatailor/home "https://console.aws.amazon.com/mediatailor/home").
2. Select the configuration you want to update.
3. In the **Advanced settings** of the **CDN
   configuration** section, enter your CDN domain name in the
   **CDN content segment prefix** field.
4. If you're using a separate CDN domain for ad segments, enter it in the
   **CDN ad segment prefix** field.
5. Save your changes.

This configuration ensures that MediaTailor generates manifests with URLs that point to your
CDN instead of directly to the origin or ad segment storage.

### Understanding base URL behavior

MediaTailor determines base URLs in manifests based on your CDN prefix configuration:

- **CDN ad segment prefix configured**: Ad segments use the CDN prefix as the base URL.
- **CDN ad segment prefix not configured**: Ad segments use the direct MediaTailor location as the base URL.
- **CDN content segment prefix configured**: Content segments use the CDN prefix as the base URL.
- **CDN content segment prefix not configured**: Content segments reference the original content origin.

#### DASH BaseURL handling

For DASH manifests, MediaTailor manages `BaseURL` settings differently for content and ad segments:

**Content segments:**

- **With CDN content segment prefix**: MediaTailor sets exactly one `BaseURL` at the `MPD` level using your specified prefix.
- **Without CDN content segment prefix**: MediaTailor preserves existing `BaseURL` settings from the origin manifest, or adds one based on the origin `MPD` URL if none exist.

**Ad segments:**

- **With CDN ad segment prefix**: Each ad period gets exactly one `BaseURL` using the configured prefix.
- **Without CDN ad segment prefix**: Each ad period gets exactly one `BaseURL` pointing to the MediaTailor ad content server.

###### Example CDN mapping example

If your content origin is `http://origin.com/contentpath/` and
your CDN content segment prefix is `https://cdn.example.com/`,
then a content segment that would normally be referenced as
`http://origin.com/contentpath/subdir/content.ts` will appear
in the manifest as
`https://cdn.example.com/subdir/content.ts`.

## Important considerations

When configuring CDN mapping in MediaTailor, keep the following important considerations in
mind:

**Use HTTPS for CDN prefixes**

Always use HTTPS URLs for your CDN prefixes to ensure secure content
delivery.

**Match CDN behavior paths**

Ensure that the CDN prefixes you configure in MediaTailor match the path
patterns you configured in your CDN behaviors.

**Consider regional CDNs**

If you're using different CDN domains for different regions, you'll need
to create separate MediaTailor configurations for each region.

**Verify domain ownership**

Ensure that you have control over the CDN domains you configure in
MediaTailor.

## Verify CDN mapping configuration

After configuring CDN mapping in MediaTailor, verify that your configuration is working
correctly:

1. Request a manifest through your CDN.
2. Examine the manifest content to verify that segment URLs reference your CDN
   domain.
3. Check that content segment URLs in the manifest point to your CDN
   domain.
4. Check that ad segment URLs in the manifest point to your CDN domain.

For comprehensive testing and validation procedures, see [Testing and validation
for CDN and MediaTailor integrations](cdn-integration-testing.md "cdn-integration-testing.md").

## Next steps

After configuring CDN mapping in MediaTailor, the next step is to implement security best
practices for your CDN integration. See [CDN integration security best practices for
MediaTailor](cdn-security-best-practices.md "cdn-security-best-practices.md") for instructions.
