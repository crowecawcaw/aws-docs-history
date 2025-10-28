# AOSOPS01-BP02 Configure index templates to automate index

configuration upon creation

Use templates to automate index creation and maintain consistent
settings.

**Level of risk exposed if this best practice
is not established:** Medium

**Desired outcome:** Index templates
are configured to inherit settings and mapping, allowing unified
structure across similar indices.

**Benefits of establishing this best
practice:**

- **Automate index configuration:**
  Configuring index templates allows you to automate the
  configuration of indexes upon creation, eliminating the need for
  manual configuration and reducing errors.
- **Consistent index settings:** By
  specifying settings and mappings in an index template, you can
  verify that newly created indexes inherit consistent settings
  and mappings, which improves data management.
- **Simplified index management:**
  With index templates, you can simplify the process of creating
  new indexes by automating configuration tasks, making it easier
  to manage your OpenSearch Service domain.

## Implementation guidance

Index templates can instruct OpenSearch on configuring an index
upon creation. Configure these templates before creating indexes,
which verifies that newly created indexes inherit the specified
settings and mappings.

For samples and full details about implementing templates, see
[Index
templates](https://opensearch.org/docs/latest/im-plugin/index-templates/ "https://opensearch.org/docs/latest/im-plugin/index-templates/").

### Implementation steps

- Open OpenSearch Dashboards for your domain.
- From the left sidebar, select **Index Management**, then
  **Templates**, then **Create template**.
- Define basic template settings:
  - **Template name:** Enter
    a unique name for the template (like
    `log-index-template`).
  - **Template type:** Choose
    **Indexes**
  - **Index patterns:**
    Specify one or more patterns to match indexes that the
    template will apply to. For example, `logs-*` for all
    indexes that begin with `logs-<something>`.
  - **Priority:** Set the
    template priority. Higher priority templates override
    lower ones when multiple templates match an index
    pattern.
  - Under Choose a method to define your templates, choose
    **Simple template** for simpler creation options.
  - If you're using aliases for your indices, then select an
    alias or create a new one.
  - Under Index settings box, specify the Number of
    primary shards. If you don't specify any number, then
    the default of one is going to be used.
  - Configure Number of replicas and the Refresh
    interval values.
  - If you are using a static mapping for your indices, then
    you can configure that as well under the Index mapping
    section.
  - Review and create the template.

## Resources

- [Index
  templates](https://opensearch.org/docs/latest/im-plugin/index-templates/ "https://opensearch.org/docs/latest/im-plugin/index-templates/")
