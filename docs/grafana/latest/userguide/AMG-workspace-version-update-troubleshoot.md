# Troubleshooting issues

with updated workspaces

Your updated workspace should continue to work after updating. This section can
help you track down possible issues after you update.

- **Differences between versions.**

Some functionality has changed between versions.

    + For a list of major changes between versions, including changes
     that may cause issues in functionality, see [Differences between Grafana versions](version-differences.md "version-differences.md").
    + For documentation of version 9 specific functionality, see [Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").
     For version 10, see [Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

- **PostgreSQL TLS issue**

If your **TLS/SSL Mode** was set to `require`
in version 8, and you were only using a root certificate, you could
experience TLS or certificate issues with the PostgreSQL data source after
updating. Modify your TLS settings for your PostgreSQL data source
(available in your Grafana workspace side menu, by choosing the
**Configuration** icon, then **Data
Sources**).

    + Change the **TLS/SSL Mode** to
     `verify-ca`.
    + Set **TLS/SSL Method** to `Certificate
     content`.
    + Set the **Root Certificate** to the root
     certificate for your PostgreSQL database server. This is the only
     field in which you should enter a certificate.
