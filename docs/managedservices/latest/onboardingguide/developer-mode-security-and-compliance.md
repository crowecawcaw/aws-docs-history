# Security and compliance in Developer mode

Security and compliance is a shared responsibility between AMS Advanced and you as our customer. AMS Advanced Developer mode shifts the shared responsibility to you for
resources provisioned outside of the change management process or provisioned through change management but updated with Developer mode permissions.
For more information about shared responsibility, see
[AWS Managed Services](https://aws.amazon.com/managed-services/ "https://aws.amazon.com/managed-services/").

**Cautions:**

- DevMode allows you and your authorized team to bypass the deny-by-default principles at the core of AMS security.
  The advantages, self-service, less time waiting for AMS must be weighed against the disadvantages, anyone can perform unexpected and
  destructive actions without the knowledge of their security team. Automated change types to enable Dev mode and Direct Change mode are exposed, and
  any authorized person in your org can run these CTs and enable these modes.
- You are responsible for managing the permissions of CT execution from your user base.
- AMS doesn’t manage CT execution permissions
  **Recommendations:**

- **Protect**
  - Customers can prevent access to this CT via permissioning, see
    [Restrict permissions with IAM role policy statements](../userguide/request-iam-user.md "../userguide/request-iam-user.md")
  - Prevent access to this CT by implementing a proxy such as an ITSM system
  - Utilize service control policies (SCPs) that prevent policies and behaviors as needed, see
    [AMS Preventative and Detective Controls Library](../userguide/scp-library.md "../userguide/scp-library.md")

- **Detect**
  - Monitor your RFC’s for these CTs (Enable developer mode ct-1opjmhuddw194 and Direct change mode, Enable ct-3rd4781c2nnhp)
    being executed and respond accordingly
  - Review and/or audit your accounts for the presence of the IAM resources to identify those accounts where Developer mode or Direct Change mode
    have been deployed

- **Respond**
  - Remove accounts in Developer mode as needed

## Security in Developer mode

AMS Advanced offers additional value with a prescriptive landing zone, a change management system, and access management. When
using Developer mode the security value of AMS Advanced is persisted by using the same account configuration of standard AMS Advanced
accounts that establishes the baseline AMS Advanced security hardened network. The network is protected by the permissions boundary enforced in the role
(`AWSManagedServicesDevelopmentRole` for **MALZ**, `customer_developer_role` for **SALZ**),
which restricts the user from breaking down the parameter protections established when the account is set up.

For example, users with the role can access Amazon Route 53 but AMS Advanced internal hosted zone is restricted. The same permissions boundaries
are enforced on an IAM role created by the `AWSManagedServicesDevelopmentRole`,
enforcing permissions boundaries on the `AWSManagedServicesDevelopmentRole` that
restricts the user from breaking down the parameter protections established when the account is onboarded to AMS Advanced.

## Compliance in Developer mode

Developer mode is compatible with both production and non-production workloads. It's your responsibility to ensure adherence to any
compliance standards (for example, PHI, HIPAA, PCI), and to ensure that the use of Developer mode complies with your internal control frameworks and standards.
