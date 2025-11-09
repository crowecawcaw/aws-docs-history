Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Restricting IP access with third-party repository providers

You can restrict access to your GitHub repositories, Bitbucket repositories, or GitLab project repositories
based on IP addresses by setting up rules or configurations. You can do this through the third-party provider's
settings or access control features.

Depending on which third-party repository provider you're using, see one of the following:

- The Amazon CodeCatalyst **GitHub repositories** extension is compatible with
  [GitHub Enterprise Cloud IP access restrictions](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization "https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization"). When configuring a GitHub Enterprise Cloud
  organization to restrict access to specific IP addresses, you can also
  [enable GitHub apps to configure the allow list](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps "https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps"),
  which will let CodeCatalyst register its IP addresses automatically with GitHub. Alternatively, you can
  [manually add the CodeCatalyst IP addresses](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#adding-an-allowed-ip-address "https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#adding-an-allowed-ip-address").
- The Amazon CodeCatalyst **Bitbucket repositories** extension is compatible with
  [Bitbucket Cloud Premium access restrictions](https://support.atlassian.com/bitbucket-cloud/docs/control-access-to-your-private-content/ "https://support.atlassian.com/bitbucket-cloud/docs/control-access-to-your-private-content/"). When configuring a Bitbucket Cloud Premium workspace
  to restrict access to specific IP addresses, you can also
  [add
  IP addresses or network blocks for a set of IP addresses to an allowlist](https://support.atlassian.com/bitbucket-cloud/docs/control-access-to-your-private-content/#Allowlisting-IP-addresses "https://support.atlassian.com/bitbucket-cloud/docs/control-access-to-your-private-content/#Allowlisting-IP-addresses").
- The Amazon CodeCatalyst **GitLab repositories** extension is compatible with
  [GitLab IP address restrictions](https://docs.gitlab.com/ee/administration/reporting/ip_addr_restrictions.html "https://docs.gitlab.com/ee/administration/reporting/ip_addr_restrictions.html"). When configuring a GitLab Premium or Ultimate group
  to restrict access to specific IP addresses, you can also
  [add
  IP addresses or network blocks for a set of IP addresses to an allowlist](https://docs.gitlab.com/ee/user/group/access_and_permissions.html "https://docs.gitlab.com/ee/user/group/access_and_permissions.html").
  If the CodeCatalyst IP addresses aren't in a third-party repository's allowlist, the Amazon CodeCatalyst app won't
  be able to access your third-party repositories. For more information, see
  [IP addresses used by third-party repositories extension](#codecatalyst-ip-address "#codecatalyst-ip-address").

## IP addresses used by third-party repositories extension

The following IP addresses are used by the third-party extensions to access your third-party resources:

- **GitHub repositories**:

```
us-west-2
  52.32.242.246
  54.148.176.49
  35.164.118.94
eu-west-1
  34.241.64.10
  34.246.255.80
  3.248.38.7
```

- **Bitbucket repositories** and **GitLab repositories**:

```
us-west-2
  35.160.210.199
  54.71.206.108
  54.71.36.205
eu-west-1
  34.242.64.82
  52.18.37.201
  54.77.75.62
```
