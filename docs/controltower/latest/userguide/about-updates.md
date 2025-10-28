# About landing zone updates

Updates are required to correct governance drift, or to move to a new version of AWS Control Tower.
To perform a complete update of AWS Control Tower, you must update your landing zone first and then update
the enrolled accounts individually. You may need to perform three types of updates at
different times.

- **A landing zone update:** Most often this type of update
  is performed by choosing **Update** on the **Landing zone
  settings** page. You may need to perform a landing zone update to resolve certain
  types of drift, and you can choose **Reset** when necessary.
- **An update of one or more individual accounts:** You
  must update accounts if the associated information changes, or if certain types of drift
  have occurred. If an account requires an update, the account's status will show
  **Update available** on the **Accounts** page.

To update a single account, navigate to the account detail page and select
**Update account**. Accounts also may be updated by a manual process,
by choosing **Re-register OU**, or with an automated scripting approach,
described in a later section of this page.

- **A full update:** A full update includes an update of
  your landing zone, followed by an update of all the enrolled accounts in your registered OUs.
  Full updates are required with a new release of AWS Control Tower such as 3.0, 3.2, and so forth.
  To make the full update process easier, for OUs with 1000 or fewer accounts, you can choose **Re-register OU**
  to update all of the accounts within that OU, and repeat the **Re-register
  OU** command for each OU.
  For more information about landing zone updates, see [Best practices for landing zone updates](lz-update-best-practices.md "lz-update-best-practices.md").

###### Note

After completing a landing zone update, you cannot undo the update or downgrade to a
previous version.
