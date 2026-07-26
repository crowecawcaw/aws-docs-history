# Change the instance launch option

You can change the instance launch option for a host resource group at any time, even when hosts are
present in the group. With this setting, you can convert between license-tracking and
non-license-tracking modes without migrating hosts to a new group.

###### Considerations

- Changing the instance launch option and updating license configurations must be done
  in the same update call. When converting to **License configuration not
  required**, remove all license configurations in the same request. When
  converting to **License configuration required**, provide license
  configurations in the same request.

###### Converting from License configuration required (default) to License configuration not required

When you convert to **License configuration not required**:

- Existing license state on hosts (license reservations, resource associations) is
  preserved. Future instance launches targeting the host resource group will not require license
  configurations and can use any AMI.
- Running instances are unaffected.
- License consumption counts in your license configurations remain until hosts are
  released.

###### Converting from License configuration not required to License configuration required (default)

When you convert to **License configuration required**:

- Existing hosts in the group that have no license associations are not affected.
  Only new operations (adding hosts, launching instances) enforce license
  requirements.
- New instances launched into the group must have license configurations associated
  with their AMI that match the license configurations configured in the host resource group.

###### To change the instance launch option

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the left navigation pane, choose **Host resource groups**.
3. Select the host resource group and choose **Actions**,
   **Edit**.
4. For **Instance launch option**, select the new option.
5. If converting to **License configuration not required**, remove all
   associated self-managed licenses. If converting to **License configuration
   required**, select one or more core- or socket-based self-managed
   licenses.
6. Choose **Save changes**.
