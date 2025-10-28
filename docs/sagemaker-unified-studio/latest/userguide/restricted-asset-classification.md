# Restricted asset classification

Amazon SageMaker Unified Studio

Restricted classification allows domain unit owners and glossary project owners to control
who can apply specific classification terms to assets in the Amazon SageMaker Catalog. This feature
helps maintain classification consistency and governance standards across your domain while
enabling controlled workflows based on governed classification terms.

Restricted classification provides the following benefits:

- Governance control - maintain consistent classification standards across your entire
  domain
- Access management - control which users can apply sensitive or restricted
  classification terms to the assets
- Workflow enablement - build automated workflows based on governed classification
  terms
- Clear separation - distinguish between open and restricted classification terms
  SageMaker catalog now separates classification terms into two categories:

- Unrestricted terms - available for all users to apply to their assets
- Restricted terms - only authorized users can apply these to assets they own
  This functionality uses the following authorization model:

- Restricted glossaries can be created and managed by glossary project owners and
  contributors. Project owners have the ability to grant usage permissions to specific
  domain units as well as to other project owners and contributors. If a restricted glossary
  is created by a contributor, only the project owner is granted permission to use it by
  default.
- Project owners are by default granted access to use the glossary for the assets in
  their projects.
- Authorized users are granted permissions to use the restricted terms for their
  projects by adding project specific grants.
- All users can filter and discover assets using restricted classification
  terms.
  When using restricted glossaries in Amazon SageMaker Unified Studio, you must abide by the following
  constraints:

- Scope of application – restricted glossary terms are currently supported only at the
  asset level. Column-level terms, metadata form–level terms and data product-level terms
  are not currently supported.
- Term relationships – restricted glossary terms cannot be related to other
  terms.
- Glossary usage permission conversion – once created, a restricted glossary cannot be
  converted into a regular glossary and a regular glossary cannot be converted into a
  restricted glossary.

## Creating restricted classification terms

As a project owner or contributor:

- Navigate to the catalog governance section
- [Create a new restricted
  classification glossary](create-maintain-business-glossary.md "create-maintain-business-glossary.md")
- Define terms within the glossary
- Set usage policies for the restricted glossary

## Applying restricted terms to assets

Complete the following procedure based on the configured usage permission for the
restricted glossary:

###### Apply restricted terms to assets

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the **Discover** menu in the top navigation bar.
3. Choose **Data catalog**.
4. Find the asset to which you want to assign restricted terms and on the asset's
   details page, choose **View inventory asset**.
5. Under **Glossary terms**, choose **Add terms**,
   then search for the restricted term that you want to assign to this asset, choose it,
   and then choose **Add term**.

Once the term is successfully added, you can identify it as a restricted term by the
presence of a lock icon next to its name.

You can associate or disassociate up to 5 restricted terms with/from an asset at any one
time.
