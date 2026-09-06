

# Combining BYOL and UBL
<a name="license-combine-byol-ubl"></a>

You can combine BYOL and UBL so that your workers use your existing licenses first and automatically fall back to Deadline Cloud usage-based licenses when your BYOL licenses are exhausted. This approach is useful when you have a limited number of existing licenses but need to scale beyond that capacity during peak workloads.

## How combined licensing works
<a name="license-combine-how-it-works"></a>

When you configure combined licensing, the queue environment sets up license environment variables so that the BYOL license server is listed before the UBL license endpoint. Most third-party applications check license servers in the order they appear in the environment variable. When a worker requests a license, the application first contacts your BYOL license server. If no BYOL license is available, the application falls back to the UBL license endpoint.

The BYOL queue environment template provided in [Connect service-managed fleets to a custom license server](smf-byol.md) configures this fallback behavior automatically. The Python script in the queue environment prepends your BYOL license server address to the existing UBL license environment variables. To use combined licensing, keep the UBL sections in the queue environment script for the products where you want fallback behavior.

To use only BYOL without UBL fallback for a specific product, remove the UBL section for that product from the script and add the license environment variable directly to the `variables` section of the queue environment. For example, to use only BYOL for Cinema 4D, remove the Cinema 4D section from the script and add `g_licenseServerRLM: 127.0.0.1:7057` to the `variables` section.

## Example: Using BYOL Cinema 4D licenses with UBL fallback
<a name="license-combine-example"></a>

Consider a studio that has existing Cinema 4D licenses on a license server in their on-premises network. The studio wants to use those licenses for Deadline Cloud rendering, but also wants to scale beyond their license count by falling back to UBL when all BYOL licenses are in use.

To configure this setup, follow the steps in [Connect service-managed fleets to a custom license server](smf-byol.md) and make the following changes to the queue environment template:

**To configure BYOL Cinema 4D licenses with UBL fallback**

1. Set the `LicenseInstanceId` parameter to the Amazon Elastic Compute Cloud (Amazon EC2) instance ID of the license server or proxy that has access to the Cinema 4D license server.

1. Set the `LicensePorts` parameter to include port `7057` (the Cinema 4D RLM license port).

1. In the Python script, keep the Cinema 4D section that prepends the BYOL server to the UBL configuration:

   ```
   # Cinema4D
   os.environ["g_licenseServerRLM"] = f"127.0.0.1:7057;{os.environ.get('g_licenseServerRLM', '')}"
   print(f"openjd_env: g_licenseServerRLM={os.environ['g_licenseServerRLM']}")
   ```

   This configuration sets `g_licenseServerRLM` to `127.0.0.1:7057;{{UBL_endpoint}}:7057`. Cinema 4D checks the BYOL server at `127.0.0.1:7057` first. If no license is available, Cinema 4D falls back to the UBL endpoint.

1. Remove the sections for products that you don't use (for example, Arnold, Nuke, or SideFX) to keep the configuration clean.

If you also have other products that use only BYOL without UBL fallback, add those license environment variables directly to the `variables` section of the queue environment and remove the corresponding sections from the Python script.

## Considerations for combined licensing
<a name="license-combine-considerations"></a>

Keep the following considerations in mind when you use combined licensing:
+ Some applications don't support multiple license servers in a single environment variable. For example, V-Ray uses an XML configuration file instead. The queue environment template handles V-Ray configuration separately. For more information, see the V-Ray section in the queue environment template in [Connect service-managed fleets to a custom license server](smf-byol.md).
+ The order of license servers in the environment variable determines the priority. List the BYOL server first so that your existing licenses are consumed before UBL licenses.
+ On Windows workers, separate license server entries in environment variables with a semicolon (`;`) instead of a colon (`:`). For more information about configuring license environment variables, see [Connect customer-managed fleets to a license endpoint](cmf-ubl.md).
+ To use UBL fallback with customer-managed fleets, set up a license endpoint. For more information, see [Connect customer-managed fleets to a license endpoint](cmf-ubl.md).