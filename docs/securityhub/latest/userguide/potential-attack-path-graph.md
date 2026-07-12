# Viewing exposures in Security Hub with the potential attack path graph

The potential attack path graph is an interactive visualization that shows how
potential attackers can access and take control of resources associated with an exposure
finding. You can access this graph only in the Security Hub console from the
**Exposures** page. When you view details for an exposure finding,
the **Overview** tab includes a section called **Potential
attack path and Blast radius**.

The attack path graph shows the primary resource where the exposure was generated,
the network path (if applicable), and the downstream resources that an attacker could
reach by escalating permissions. When Security Hub identifies concrete privilege escalation
paths from the primary resource to other resources in your environment, it displays
them as the blast radius portion of the graph. Each node represents a resource, and
the connections between nodes show the permissions that enable an attacker to move
from one resource to the next.

In this section of the **Overview** tab, you can choose and drag
AWS resources in the potential attack path graph. You can focus on specific areas of
the attack path graph with the zoom-in and zoom-out icons. You can expand the attack
path graph in and out of fullscreen mode through the fullscreen icon. The legend codes
the primary resource, involved resource, blast radius resources, and contributing trait
count by color and shows the trait categories and number of traits in the attack path
graph. You can view details for a resource by choosing a resource and choosing
**View resource details**. You can also copy the ID and AWS account
number associated with a resource. Exposure findings with a reachability trait show the
public internet and collapsed network path in the attack path graph. You can view this
detail by choosing the collapsed network path node.

To view the downstream resources and the privilege escalation paths
that connect them, choose the **Impact assessment** tab. Each path
shows the chain of resources an attacker could traverse and the specific permissions
at each step. For more information about impact traits and effective permissions, see
[Impact and effective permissions](exposure-findings-supported-traits.md#exposure-findings-impact-analysis "exposure-findings-supported-traits.md#exposure-findings-impact-analysis").
