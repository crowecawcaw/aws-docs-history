

# Search and filter Amazon SES API v2 resources using an AWS SDK
<a name="sesv2_example_sesv2_SearchFilterBasics_section"></a>

The following code example shows how to:
+ Create multiple configuration sets, email identities, and tenants.
+ List all configuration sets (unfiltered).
+ Filter configuration sets by name substring.
+ List all email identities (unfiltered).
+ Filter email identities by name substring.
+ List all tenants (unfiltered).
+ Filter tenants by name substring.
+ Demonstrate pagination with filters.
+ Clean up all created resources.

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/sesv2/search_filter_scenario#code-examples). 
Run the Search and Filter SES resources scenario.  

```
class SearchFilterBasicsScenario:
    """Runs the SES v2 Search and Filter Basics scenario."""

    def __init__(self, sesv2_wrapper: SearchFilterWrapper):
        """
        :param sesv2_wrapper: An instance of SearchFilterWrapper that provides
            the Amazon SES v2 operations used in this scenario.
        """
        self.sesv2_wrapper = sesv2_wrapper

    def run_scenario(self) -> None:
        """Orchestrates the full scenario."""
        print("-" * 88)
        print("Welcome to the Amazon SES v2 Search and Filter Basics scenario.")
        print("-" * 88)
        print(
            "This demo shows how to use the new filter parameters on\n"
            "ListConfigurationSets, ListEmailIdentities, and ListTenants to\n"
            "narrow results server-side."
        )
        print()

        created_config_sets = list()
        created_identities = list()
        created_tenants = list()

        try:
            # --- Setup ---
            # Each setup helper adds resources to its list as they're created,
            # so cleanup can delete them even if setup fails partway through.
            print("--- Setup: Creating resources ---")
            self._setup_configuration_sets(created_config_sets)
            self._setup_email_identities(created_identities)
            self._setup_tenants(created_tenants)
            self._wait_for_filtered_results(
                created_config_sets, created_identities, created_tenants
            )
            print()

            # --- Step 1: Unfiltered configuration sets ---
            print("--- Step 1: List ALL configuration sets (unfiltered) ---")
            all_config_sets = self.sesv2_wrapper.list_configuration_sets()
            print(f"Found {len(all_config_sets)} configuration set(s):")
            for name in all_config_sets:
                print(f"  - {name}")
            print()

            # --- Step 2: Filtered configuration sets ---
            print(
                "--- Step 2: Filter configuration sets "
                f'(name contains "{CONFIG_SET_FILTER}") ---'
            )
            filtered_config_sets = self.sesv2_wrapper.list_configuration_sets(
                filter_params={"CONFIGURATION_SET_NAME_CONTAINS": CONFIG_SET_FILTER}
            )
            print(
                f"Found {len(filtered_config_sets)} of {len(all_config_sets)} "
                "configuration set(s):"
            )
            for name in filtered_config_sets:
                print(f"  - {name}")
            print()

            # --- Step 3: Unfiltered email identities ---
            print("--- Step 3: List ALL email identities (unfiltered) ---")
            all_identities = self.sesv2_wrapper.list_email_identities()
            print(f"Found {len(all_identities)} email identity(ies):")
            for identity in all_identities:
                print(
                    f"  - {identity.get('IdentityName', 'N/A')} "
                    f"({identity.get('IdentityType', 'N/A')}, "
                    f"verification={identity.get('VerificationStatus', 'N/A')})"
                )
            print()

            # --- Step 4: Filtered email identities ---
            print(
                "--- Step 4: Filter email identities "
                f'(name contains "{IDENTITY_FILTER}") ---'
            )
            filtered_identities = self.sesv2_wrapper.list_email_identities(
                filter_params={"IDENTITY_NAME_CONTAINS": IDENTITY_FILTER}
            )
            print(
                f"Found {len(filtered_identities)} of {len(all_identities)} "
                "email identity(ies):"
            )
            for identity in filtered_identities:
                print(
                    f"  - {identity.get('IdentityName', 'N/A')} "
                    f"({identity.get('IdentityType', 'N/A')})"
                )
            print()

            # --- Step 5: Unfiltered tenants ---
            print("--- Step 5: List ALL tenants (unfiltered) ---")
            all_tenants = self.sesv2_wrapper.list_tenants()
            print(f"Found {len(all_tenants)} tenant(s):")
            for tenant in all_tenants:
                print(
                    f"  - {tenant.get('TenantName', 'N/A')} "
                    f"(ID: {tenant.get('TenantId', 'N/A')})"
                )
            print()

            # --- Step 6: Filtered tenants ---
            print(f'--- Step 6: Filter tenants (name contains "{TENANT_FILTER}") ---')
            filtered_tenants = self.sesv2_wrapper.list_tenants(
                filter_params={"TENANT_NAME_CONTAINS": TENANT_FILTER}
            )
            print(f"Found {len(filtered_tenants)} of {len(all_tenants)} tenant(s):")
            for tenant in filtered_tenants:
                print(
                    f"  - {tenant.get('TenantName', 'N/A')} "
                    f"(ID: {tenant.get('TenantId', 'N/A')})"
                )
            print()

            # --- Step 7: Pagination with filters ---
            print("--- Step 7: Page through filtered configuration sets ---")
            print(
                "Listing configuration sets whose name contains "
                f'"{CONFIG_SET_FILTER}" with PageSize=1.\n'
                "Each response holds one result and a NextToken that requests "
                "the next page."
            )
            page_number = 0
            next_token = None
            while True:
                page, next_token = self.sesv2_wrapper.list_configuration_sets_page(
                    {"CONFIGURATION_SET_NAME_CONTAINS": CONFIG_SET_FILTER},
                    page_size=1,
                    next_token=next_token,
                )
                page_number += 1
                print(f"  Page {page_number}: {', '.join(page) or '(empty)'}")
                if not next_token:
                    break
            print()

            print("-" * 88)
            print("Scenario demonstration complete!")
            print("-" * 88)

        finally:
            # --- Cleanup ---
            print()
            print("--- Cleanup: Removing resources created during setup ---")
            self._cleanup(created_config_sets, created_identities, created_tenants)
            print("-" * 88)

    # ------------------------------------------------------------------
    # Setup helpers
    # ------------------------------------------------------------------

    def _setup_configuration_sets(self, created: list) -> None:
        """
        Creates configuration sets for the scenario and adds each new one to
        created. A configuration set that already exists isn't added, so
        cleanup won't delete it.
        """
        for name in CONFIGURATION_SET_NAMES:
            if self.sesv2_wrapper.create_configuration_set(name):
                created.append(name)
                print(f"  Created configuration set: {name}")
            else:
                print(f"  Configuration set {name} already exists. Using it as is.")

    def _setup_email_identities(self, created: list) -> None:
        """Creates email identities and adds each new one to created."""
        for identity in EMAIL_IDENTITIES:
            try:
                response = self.sesv2_wrapper.create_email_identity(identity)
                created.append(identity)
                identity_type = response.get("IdentityType", "UNKNOWN")
                verified = response.get("VerifiedForSendingStatus", False)
                print(
                    f"  Created email identity: {identity} "
                    f"(type={identity_type}, verified={verified})"
                )
            except ClientError:
                logger.warning("Could not create identity '%s'. Continuing.", identity)

    def _setup_tenants(self, created: list) -> None:
        """Creates tenants and adds each new one to created."""
        for name in TENANT_NAMES:
            try:
                response = self.sesv2_wrapper.create_tenant(name)
                created.append(name)
                tenant_id = response.get("TenantId", "N/A")
                print(f"  Created tenant: {name} (ID: {tenant_id})")
            except ClientError:
                logger.warning("Could not create tenant '%s'. Continuing.", name)

    def _wait_for_filtered_results(
        self, config_set_names: list, identity_names: list, tenant_names: list
    ) -> None:
        """
        Repeats the scenario's filtered list calls until each one includes the
        new resources that match its filter. Each resource type is checked
        with its own filtered call, because one list operation being up to
        date doesn't mean the others are.
        """
        expected_config_sets = {n for n in config_set_names if CONFIG_SET_FILTER in n}
        expected_identities = {i for i in identity_names if IDENTITY_FILTER in i}
        expected_tenants = {n for n in tenant_names if TENANT_FILTER in n}

        print("Waiting for the new resources to appear in filtered results...")
        for attempt in range(1, FILTER_WAIT_ATTEMPTS + 1):
            config_sets = set(
                self.sesv2_wrapper.list_configuration_sets(
                    filter_params={"CONFIGURATION_SET_NAME_CONTAINS": CONFIG_SET_FILTER}
                )
            )
            identities = {
                i["IdentityName"]
                for i in self.sesv2_wrapper.list_email_identities(
                    filter_params={"IDENTITY_NAME_CONTAINS": IDENTITY_FILTER}
                )
            }
            tenants = {
                t["TenantName"]
                for t in self.sesv2_wrapper.list_tenants(
                    filter_params={"TENANT_NAME_CONTAINS": TENANT_FILTER}
                )
            }
            if (
                expected_config_sets <= config_sets
                and expected_identities <= identities
                and expected_tenants <= tenants
            ):
                print("  The new resources are available in filtered results.")
                return
            if attempt < FILTER_WAIT_ATTEMPTS:
                time.sleep(FILTER_WAIT_DELAY_SECONDS)
        print(
            "  Some new resources still aren't in filtered results. "
            "The filter steps may show fewer results than expected."
        )

    # ------------------------------------------------------------------
    # Cleanup
    # ------------------------------------------------------------------

    def _cleanup(
        self,
        config_set_names: list,
        identity_names: list,
        tenant_names: list,
    ) -> None:
        """
        Deletes all resources created during setup. Each delete is attempted
        on its own, so one failure doesn't leave the rest in the account.
        """
        not_deleted = list()
        for kind, names, delete in (
            (
                "configuration set",
                config_set_names,
                self.sesv2_wrapper.delete_configuration_set,
            ),
            (
                "email identity",
                identity_names,
                self.sesv2_wrapper.delete_email_identity,
            ),
            ("tenant", tenant_names, self.sesv2_wrapper.delete_tenant),
        ):
            for name in names:
                try:
                    delete(name)
                    print(f"  Deleted {kind}: {name}")
                except ClientError as err:
                    print(
                        f"  Couldn't delete {kind} {name}: "
                        f"{err.response['Error']['Message']}"
                    )
                    not_deleted.append(f"{kind} {name}")

        if not_deleted:
            print("These resources weren't deleted. Delete them manually:")
            for item in not_deleted:
                print(f"  - {item}")
        else:
            print("Cleanup complete.")
```
A wrapper class for the Amazon SES API v2 search-and-filter operations.  

```
class SearchFilterWrapper:
    """Encapsulates Amazon SES v2 search-and-filter operations."""

    def __init__(self, sesv2_client: boto3.client):
        """
        Initializes the SearchFilterWrapper with an Amazon SES v2 client.

        :param sesv2_client: A Boto3 Amazon SES v2 client.
        """
        self.sesv2_client = sesv2_client

    @classmethod
    def from_client(cls) -> "SearchFilterWrapper":
        """
        Creates a SearchFilterWrapper instance with a default Boto3 SES v2 client.

        :return: An initialized SearchFilterWrapper instance.
        """
        sesv2_client = boto3.client("sesv2")
        return cls(sesv2_client)


    def list_configuration_sets(
        self,
        filter_params: Optional[Dict[str, str]] = None,
        page_size: Optional[int] = None,
    ) -> List[str]:
        """
        Lists configuration sets associated with the account in the current
        region. Supports optional filter parameters and pagination.

        :param filter_params: Optional dictionary of filter key-value pairs
            (e.g., {"CONFIGURATION_SET_NAME_CONTAINS": "marketing"}).
        :param page_size: Optional number of results per page.
        :return: A list of configuration set name strings.
        """
        try:
            # ListConfigurationSets has no registered Boto3 paginator, so
            # pagination is handled manually using the NextToken field.
            configuration_sets = list()
            next_token = None
            while True:
                kwargs = dict()
                if filter_params is not None:
                    kwargs["Filter"] = filter_params
                if page_size is not None:
                    kwargs["PageSize"] = page_size
                if next_token is not None:
                    kwargs["NextToken"] = next_token

                response = self.sesv2_client.list_configuration_sets(**kwargs)
                configuration_sets.extend(response.get("ConfigurationSets", list()))
                next_token = response.get("NextToken")
                if not next_token:
                    break
            logger.info("Listed %d configuration sets.", len(configuration_sets))
            return configuration_sets
        except ClientError as err:
            if err.response["Error"]["Code"] == "BadRequestException":
                logger.error(
                    "Bad request when listing configuration sets: %s",
                    err.response["Error"]["Message"],
                )
            else:
                logger.error(
                    "Error listing configuration sets: %s",
                    err.response["Error"]["Message"],
                )
            raise


    def list_email_identities(
        self,
        filter_params: Optional[Dict[str, str]] = None,
        page_size: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """
        Lists email identities associated with the account. Supports optional
        filter parameters and pagination.

        :param filter_params: Optional dictionary of filter key-value pairs
            (e.g., {"IDENTITY_NAME_CONTAINS": "example"}).
        :param page_size: Optional number of results per page.
        :return: A list of identity info dictionaries.
        """
        try:
            # ListEmailIdentities has no registered Boto3 paginator, so
            # pagination is handled manually using the NextToken field.
            identities = list()
            next_token = None
            while True:
                kwargs = dict()
                if filter_params is not None:
                    kwargs["Filter"] = filter_params
                if page_size is not None:
                    kwargs["PageSize"] = page_size
                if next_token is not None:
                    kwargs["NextToken"] = next_token

                response = self.sesv2_client.list_email_identities(**kwargs)
                identities.extend(response.get("EmailIdentities", list()))
                next_token = response.get("NextToken")
                if not next_token:
                    break
            logger.info("Listed %d email identities.", len(identities))
            return identities
        except ClientError as err:
            if err.response["Error"]["Code"] == "BadRequestException":
                logger.error(
                    "Bad request when listing email identities: %s",
                    err.response["Error"]["Message"],
                )
            else:
                logger.error(
                    "Error listing email identities: %s",
                    err.response["Error"]["Message"],
                )
            raise


    def list_tenants(
        self,
        filter_params: Optional[Dict[str, str]] = None,
        page_size: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """
        Lists tenants associated with the account. Supports optional filter
        parameters and pagination.

        :param filter_params: Optional dictionary of filter key-value pairs
            (e.g., {"TENANT_NAME_CONTAINS": "customer"}).
        :param page_size: Optional number of results per page.
        :return: A list of tenant info dictionaries.
        """
        try:
            # Pagination is handled manually using the NextToken field to keep
            # the three list methods consistent. The sibling list operations
            # (configuration sets, email identities) have no registered Boto3
            # paginator, so the same manual approach is used here.
            tenants = list()
            next_token = None
            while True:
                kwargs = dict()
                if filter_params is not None:
                    kwargs["Filter"] = filter_params
                if page_size is not None:
                    kwargs["PageSize"] = page_size
                if next_token is not None:
                    kwargs["NextToken"] = next_token

                response = self.sesv2_client.list_tenants(**kwargs)
                tenants.extend(response.get("Tenants", list()))
                next_token = response.get("NextToken")
                if not next_token:
                    break
            logger.info("Listed %d tenants.", len(tenants))
            return tenants
        except ClientError as err:
            if err.response["Error"]["Code"] == "TooManyRequestsException":
                logger.error(
                    "Too many requests when listing tenants: %s",
                    err.response["Error"]["Message"],
                )
            else:
                logger.error(
                    "Error listing tenants: %s",
                    err.response["Error"]["Message"],
                )
            raise


    def create_configuration_set(self, configuration_set_name: str) -> bool:
        """
        Creates a configuration set with the specified name.

        :param configuration_set_name: The name for the new configuration set.
        :return: True if the configuration set was created, or False if a
            configuration set with that name already existed.
        """
        try:
            self.sesv2_client.create_configuration_set(
                ConfigurationSetName=configuration_set_name
            )
            logger.info("Created configuration set '%s'.", configuration_set_name)
            return True
        except ClientError as err:
            if err.response["Error"]["Code"] == "AlreadyExistsException":
                logger.warning(
                    "Configuration set '%s' already exists. Skipping creation.",
                    configuration_set_name,
                )
                return False
            else:
                logger.error(
                    "Error creating configuration set '%s': %s",
                    configuration_set_name,
                    err.response["Error"]["Message"],
                )
                raise


    def create_email_identity(self, email_identity: str) -> Dict[str, Any]:
        """
        Creates an email identity (email address or domain) for verification.

        :param email_identity: The email address or domain to verify.
        :return: A dictionary with identity type, verification status, and
            DKIM attributes.
        """
        try:
            response = self.sesv2_client.create_email_identity(
                EmailIdentity=email_identity
            )
            logger.info("Created email identity '%s'.", email_identity)
            return response
        except ClientError as err:
            if err.response["Error"]["Code"] == "TooManyRequestsException":
                logger.error(
                    "Too many requests when creating email identity '%s': %s",
                    email_identity,
                    err.response["Error"]["Message"],
                )
            else:
                logger.error(
                    "Error creating email identity '%s': %s",
                    email_identity,
                    err.response["Error"]["Message"],
                )
            raise

    def create_tenant(self, tenant_name: str) -> Dict[str, Any]:
        """
        Creates a tenant with the specified name.

        :param tenant_name: The name of the tenant to create.
        :return: A dictionary containing TenantName, TenantId, TenantArn, and
            CreatedTimestamp.
        """
        try:
            response = self.sesv2_client.create_tenant(TenantName=tenant_name)
            logger.info("Created tenant '%s'.", tenant_name)
            return response
        except ClientError as err:
            if err.response["Error"]["Code"] == "BadRequestException":
                logger.error(
                    "Bad request when creating tenant '%s': %s",
                    tenant_name,
                    err.response["Error"]["Message"],
                )
            else:
                logger.error(
                    "Error creating tenant '%s': %s",
                    tenant_name,
                    err.response["Error"]["Message"],
                )
            raise


    def delete_configuration_set(self, configuration_set_name: str) -> None:
        """
        Deletes a configuration set.

        :param configuration_set_name: The name of the configuration set to
            delete.
        """
        try:
            self.sesv2_client.delete_configuration_set(
                ConfigurationSetName=configuration_set_name
            )
            logger.info("Deleted configuration set '%s'.", configuration_set_name)
        except ClientError as err:
            if err.response["Error"]["Code"] == "NotFoundException":
                logger.warning(
                    "Configuration set '%s' not found. Skipping deletion.",
                    configuration_set_name,
                )
            else:
                logger.error(
                    "Error deleting configuration set '%s': %s",
                    configuration_set_name,
                    err.response["Error"]["Message"],
                )
                raise


    def delete_email_identity(self, email_identity: str) -> None:
        """
        Deletes an email identity.

        :param email_identity: The email address or domain to delete.
        """
        try:
            self.sesv2_client.delete_email_identity(EmailIdentity=email_identity)
            logger.info("Deleted email identity '%s'.", email_identity)
        except ClientError as err:
            if err.response["Error"]["Code"] == "NotFoundException":
                logger.warning(
                    "Email identity '%s' not found. Skipping deletion.",
                    email_identity,
                )
            else:
                logger.error(
                    "Error deleting email identity '%s': %s",
                    email_identity,
                    err.response["Error"]["Message"],
                )
                raise

    def delete_tenant(self, tenant_name: str) -> None:
        """
        Deletes a tenant.

        :param tenant_name: The name of the tenant to delete.
        """
        try:
            self.sesv2_client.delete_tenant(TenantName=tenant_name)
            logger.info("Deleted tenant '%s'.", tenant_name)
        except ClientError as err:
            if err.response["Error"]["Code"] == "NotFoundException":
                logger.warning(
                    "Tenant '%s' not found. Skipping deletion.",
                    tenant_name,
                )
            else:
                logger.error(
                    "Error deleting tenant '%s': %s",
                    tenant_name,
                    err.response["Error"]["Message"],
                )
                raise


    def list_configuration_sets_page(
        self,
        filter_params: Dict[str, str],
        page_size: int,
        next_token: Optional[str] = None,
    ) -> Tuple[List[str], Optional[str]]:
        """
        Gets one page of filtered configuration sets. Use this instead of
        list_configuration_sets to work with each page separately.

        :param filter_params: The filter to apply.
        :param page_size: The maximum number of results in the page.
        :param next_token: The NextToken from the previous page, or None for the
            first page.
        :return: The configuration set names in this page, and the NextToken for
            the next page, or None if this is the last page.
        """
        kwargs = {"Filter": filter_params, "PageSize": page_size}
        if next_token is not None:
            kwargs["NextToken"] = next_token
        try:
            response = self.sesv2_client.list_configuration_sets(**kwargs)
        except ClientError as err:
            logger.error(
                "Error listing configuration sets: %s",
                err.response["Error"]["Message"],
            )
            raise
        return response.get("ConfigurationSets", list()), response.get("NextToken")
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [CreateConfigurationSet](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/CreateConfigurationSet)
  + [CreateEmailIdentity](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/CreateEmailIdentity)
  + [CreateTenant](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/CreateTenant)
  + [DeleteConfigurationSet](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/DeleteConfigurationSet)
  + [DeleteEmailIdentity](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/DeleteEmailIdentity)
  + [DeleteTenant](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/DeleteTenant)
  + [ListConfigurationSets](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/ListConfigurationSets)
  + [ListEmailIdentities](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/ListEmailIdentities)
  + [ListTenants](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/ListTenants)

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon SES with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.