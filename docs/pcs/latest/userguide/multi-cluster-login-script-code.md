

# AWS PCS multi-cluster login node configuration script code
<a name="multi-cluster-login-script-code"></a>

Save the following source code to a file with the following name:

```
pcs-multi-cluster-login-configure.sh
```

## Script source code
<a name="multi-cluster-login-script-code-content"></a>

```
#!/bin/bash
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

# AWS PCS Multi-Cluster Standalone Login Node Configuration Script
# 
# This script configures AWS Parallel Computing Service (PCS) multi-cluster stand alone login nodes
# by setting up the Slurm authentication and credential kiosk daemon (sackd)
# for connecting to remote PCS clusters. Run once for each cluster; clusters might
# be in different Regions.
#
#   ./pcs-multi-cluster-login-configure.sh --cluster-identifier <id> --region us-west-2 --fetch-secret
#   ./pcs-multi-cluster-login-configure.sh --cluster-identifier <id> --region us-east-1 --fetch-secret
#
# Prerequisites:
# - AWS CLI configured with appropriate permissions
# - Slurm version 25.05 or later
# - Root privileges for system configuration
# - Network connectivity to the AWS PCS control-plane API, used by this script to
#   look up the cluster
# - Network connectivity from this host to the cluster's slurmctld endpoint (TCP
#   6817 by default), used by sackd at runtime. This is a separate network path
#   from the preceding API path, and reaching one does not imply reaching the
#   other. The API might be served over a public endpoint, whereas slurmctld is
#   private to the cluster's VPC. For a cluster in another VPC or Region,
#   slurmctld needs peering or a transit gateway plus the matching routes and
#   security group rules.
# - For --fetch-secret: secretsmanager:GetSecretValue permission on the cluster's auth key
#
# Two clusters in different Regions can share a name. Use --alias to give each one a
# distinct local identifier, so their services and files do not collide:
#
#   ./pcs-multi-cluster-login-configure.sh --cluster-identifier <id> --region us-west-2 --alias prod-west
#   ./pcs-multi-cluster-login-configure.sh --cluster-identifier <id> --region us-east-1 --alias prod-east
#
# --cluster-name, --cluster-id, --slurm-version and --endpoints override what the AWS
# PCS API reports. Supply all four and the script makes no API call, which suits a host
# with no route to the API. Supply some and the call fills in the rest. --fetch-secret
# always calls the API to read the secret ARN, so it is an exception.
#
# The script checks the Slurm build before it changes anything. It does not probe
# controller reachability, because sackd itself is the authority on that. The script
# therefore starts sackd last and reports any failure to start with a pointer to
# its logs.


set -eo pipefail

# Function to display usage
usage() {
    echo "Usage: $0 --cluster-identifier <cluster-identifier> [--region <aws-region>] [--fetch-secret] [--endpoint-url <endpoint-url>] [--alias <name>]"
    echo "       $0 --cluster-identifier <id> --cluster-name <name> --cluster-id <id> --slurm-version <ver> --endpoints <host:port>"
    echo "       $0 -h|--help"
}

# Function to display help
help() {
    echo "AWS PCS Multi-Cluster Standalone Login Node Configuration Script"
    echo "==============================================="
    echo
    echo "This script configures multi-cluster standalone login node for AWS Parallel Computing Service (PCS)"
    echo "by setting up the Slurm authentication and credential kiosk daemon (sackd)."
    echo
    echo "Supports clusters across multiple AWS Regions. Run the script once for each cluster."
    echo
    usage
    echo
    echo "Options:"
    echo "  --cluster-identifier <id>    AWS PCS cluster identifier (required)"
    echo "  --region <region>            AWS Region of the cluster (optional, defaults to instance Region via IMDS)"
    echo "  --fetch-secret               Automatically retrieve the Slurm auth key from AWS Secrets Manager"
    echo "                               (requires secretsmanager:GetSecretValue permission on the cluster's auth key)"
    echo "  --endpoint-url <url>         Custom PCS endpoint URL (optional, applies only when"
    echo "                               the script calls the API)"
    echo "  --alias <name>               Local identifier for this cluster (default: the cluster's"
    echo "                               own name). Use it when two clusters in different Regions"
    echo "                               share a name. Letters, digits, dot, underscore, hyphen."
    echo "  -h, --help                   Show this help message"
    echo
    echo "Overrides for what the AWS PCS API reports. Supply all four and the script makes no"
    echo "API call; supply some and the call fills in the rest. --fetch-secret reads the secret"
    echo "ARN from that call, so it always requires one:"
    echo "  --cluster-name <name>        Cluster name"
    echo "  --cluster-id <id>            Cluster ID, used as the Slurm JWKS key ID"
    echo "  --slurm-version <version>    Slurm version, selects /opt/aws/pcs/scheduler/slurm-<version>"
    echo "  --endpoints <host:port>      slurmctld endpoints, comma separated"
    echo
    echo "Examples:"
    echo "  # Configure for a cluster in the same Region as this instance"
    echo "  $0 --cluster-identifier my-pcs-cluster"
    echo
    echo "  # Configure for clusters in multiple Regions"
    echo "  $0 --cluster-identifier cluster-west --region us-west-2"
    echo "  $0 --cluster-identifier cluster-east --region us-east-1"
    echo
    echo "  # Auto-fetch the auth key from Secrets Manager (no manual paste needed)"
    echo "  $0 --cluster-identifier my-pcs-cluster --fetch-secret"
    echo
    echo "  # Two clusters that share a name, told apart by alias"
    echo "  $0 --cluster-identifier cluster-west --region us-west-2 --alias prod-west"
    echo "  $0 --cluster-identifier cluster-east --region us-east-1 --alias prod-east"
    echo
    echo "  # No API call: every cluster detail supplied on the command line"
    echo "  $0 --cluster-identifier pcs_abc123 --cluster-name pcs-prod \\"
    echo "     --cluster-id pcs_abc123 --slurm-version 25.05 \\"
    echo "     --endpoints 10.0.1.157:6817 --region us-west-2"
    echo
    echo "Note: This script requires root privileges and Slurm version 25.05 or later."
    echo "      Cross-Region clusters require VPC peering or a transit gateway to the cluster's VPC."
}

# Function to retrieve authentication key
get_auth_key() {
    if [ "$ALTERNATE_SECRET_RETRIEVAL" = "true" ]; then
        echo "Retrieving authentication key from AWS Secrets Manager..." >&2
        local auth_key_arn=$(echo "$CLUSTER_INFO" | jq -r '.cluster.slurmConfiguration.authKey.secretArn')
        local auth_key_version=$(echo "$CLUSTER_INFO" | jq -r '.cluster.slurmConfiguration.authKey.secretVersion')
        
        if [ "$auth_key_arn" = "null" ] || [ "$auth_key_version" = "null" ]; then
            echo "Error: Auth key information not found in cluster configuration" >&2
            exit 1
        fi
        
        if ! aws secretsmanager get-secret-value --secret-id "$auth_key_arn" --version-id "$auth_key_version" --query SecretString --output text --region "$REGION" 2>/dev/null; then
            echo "Error: Failed to retrieve auth key from Secrets Manager" >&2
            exit 1
        fi
    else
        echo "Please enter the base64-encoded Slurm authentication key:" >&2
        echo -n "Base64 of the Slurm secret key: " >&2
        local key
        read -rs key
        echo >&2
        echo "$key"
    fi
}

# Function to get the instance Region from IMDS
get_imds_region() {
    # Try IPv6 IMDS endpoint first (fd00:ec2::254) with fast timeout (1s connect, 2s total)
    # If IPv6 fails, fall back to IPv4 IMDS endpoint (169.254.169.254)
    local imds_endpoint="http://[fd00:ec2::254]"
    local token
    if ! token=$(curl -s -X PUT "${imds_endpoint}/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600" --connect-timeout 1 --max-time 2 2>/dev/null); then
        imds_endpoint="http://169.254.169.254"
        if ! token=$(curl -s -X PUT "${imds_endpoint}/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600" --max-time 5); then
            echo "Error: Failed to retrieve IMDS token. Ensure this script is running on an EC2 instance." >&2
            exit 1
        fi
    fi

    local doc region
    # Capture the document first so a curl or timeout failure is reported here instead of
    # aborting silently under set -e. jq then prints the literal "null" (exit 0) when
    # .region is absent, so the extracted value is also checked explicitly.
    if ! doc=$(curl -s -H "X-aws-ec2-metadata-token: $token" "${imds_endpoint}/latest/dynamic/instance-identity/document" --max-time 5); then
        echo "Error: Failed to retrieve instance identity document from IMDS" >&2
        exit 1
    fi
    region=$(echo "$doc" | jq -r '.region')
    if [ -z "$region" ] || [ "$region" = "null" ]; then
        echo "Error: Failed to retrieve AWS Region from instance metadata" >&2
        exit 1
    fi
    echo "$region"
}

# Function to get next available SACKD port
get_next_sackd_port() {
    local exclude_file="$1"
    local port=6918
    local used_ports=()
    
    # Get all currently used SACKD ports into an array
    while IFS= read -r line; do
        used_ports+=("$line")
    done < <(find /etc/sysconfig -name "sackd-pcs-*" ! -path "$exclude_file" \
             -exec grep SACKD_PORT= '{}' ';' 2>/dev/null | \
             sed 's/.*SACKD_PORT=//' | sort -n)
    
    # Loop through used ports to find first available port
    for used_port in "${used_ports[@]}"; do
        if [ "$port" -lt "$used_port" ]; then
            break
        elif [ "$port" -eq "$used_port" ]; then
            ((port++))
        fi
    done
    
    echo "$port"
}

# Function to configure cluster
configure_cluster() {
    # The mode is explicit because a restrictive umask would otherwise leave this
    # directory untraversable by the slurm user, which sackd runs as.
    install -d -m 0755 /etc/slurm
    SLURM_JWKS_FILE="/etc/slurm/slurm-${CLUSTER_LOCAL}.jwks"
    # Create the file with restrictive permissions before writing the secret, so the
    # base64 Slurm key is never briefly readable by other users. The truncating redirect
    # below preserves this mode and ownership, so no later chmod/chown is needed.
    install -m 0600 -o slurm -g slurm /dev/null "${SLURM_JWKS_FILE}"
    echo '{"keys":[{"alg":"HS256","kty":"oct","kid":"key-'"${CLUSTER_ID}"'","k":"'"${BASE64_SLURM_KEY}"'"}]}' | jq -c '.' > "${SLURM_JWKS_FILE}"
    
    # main() sets and validates SLURM_INSTALL_PATH before it calls this function.
    
    SACKD_RUNTIME_DIRECTORY="/run/slurm-${CLUSTER_LOCAL}"
    mkdir -p "${SACKD_RUNTIME_DIRECTORY}"
    chown slurm:slurm "${SACKD_RUNTIME_DIRECTORY}"
    
    mkdir -p /etc/sysconfig
    SACKD_SERVICE_NAME="sackd-pcs-${CLUSTER_LOCAL}"
    SACKD_SERVICE_ENV="/etc/sysconfig/${SACKD_SERVICE_NAME}"
    SACKD_PORT=$(get_next_sackd_port "$SACKD_SERVICE_ENV")
    cat > "${SACKD_SERVICE_ENV}" << EOF
SACKD_OPTIONS='--conf-server=$ENDPOINTS'
SLURM_SACK_JWKS='$SLURM_JWKS_FILE'
RUNTIME_DIRECTORY='$SACKD_RUNTIME_DIRECTORY'
SACKD_PORT=$SACKD_PORT
EOF
    
    SACKD_SERVICE_PATH="/etc/systemd/system/${SACKD_SERVICE_NAME}.service"
    
    cat << EOF > "$SACKD_SERVICE_PATH"
[Unit]
Description=Slurm auth and cred kiosk daemon (${CLUSTER_LOCAL} - ${REGION})
After=network-online.target remote-fs.target
Wants=network-online.target
ConditionPathExists=${SACKD_SERVICE_ENV}

[Service]
Type=notify
EnvironmentFile=${SACKD_SERVICE_ENV}
User=slurm
Group=slurm
RuntimeDirectory=slurm-${CLUSTER_LOCAL}
RuntimeDirectoryMode=0755
ExecStart=${SLURM_INSTALL_PATH}/sbin/sackd --systemd \$SACKD_OPTIONS
ExecReload=/bin/kill -HUP \$MAINPID
KillMode=process
LimitNOFILE=131072
LimitMEMLOCK=infinity
LimitSTACK=infinity

[Install]
WantedBy=multi-user.target
EOF
    
    chown root:root "$SACKD_SERVICE_PATH"
    chmod 0644 "$SACKD_SERVICE_PATH"
    
    ACTIVATE_SCRIPT="activate-pcs-${CLUSTER_LOCAL}"
    cat > "$ACTIVATE_SCRIPT" << EOF
# Activate script for Slurm cluster ${CLUSTER_NAME} as ${CLUSTER_LOCAL} (Region: ${REGION})

# Add Slurm paths
export PATH="${SLURM_INSTALL_PATH}/bin:\$PATH"
export MANPATH="${SLURM_INSTALL_PATH}/share/man:\$MANPATH"
export LD_LIBRARY_PATH="${SLURM_INSTALL_PATH}/lib:\$LD_LIBRARY_PATH"
ldconfig

# Set Slurm configuration
export SLURM_CONF="/run/slurm-${CLUSTER_LOCAL}/conf/slurm.conf"

# Slurm clients otherwise derive the socket path from the cluster's own name, which
# an alias does not match.
export SLURM_SACK_SOCKET="/run/slurm-${CLUSTER_LOCAL}/sack.socket"

export PCS_CLUSTER_NAME="${CLUSTER_LOCAL}"
export PCS_CLUSTER_ACTUAL_NAME="${CLUSTER_NAME}"
export PCS_CLUSTER_IDENTIFIER="${CLUSTER_IDENTIFIER}"
export PCS_CLUSTER_ID="${CLUSTER_ID}"
export PCS_CLUSTER_REGION="${REGION}"

echo "Activated PCS cluster environment: ${CLUSTER_LOCAL} (${REGION})"

# Deactivate function
function deactivate-pcs-${CLUSTER_LOCAL}() {
    export PATH="\$(echo "\$PATH" | sed -e "s|${SLURM_INSTALL_PATH}/bin:||g" -e "s|:${SLURM_INSTALL_PATH}/bin||g" -e "s|^${SLURM_INSTALL_PATH}/bin\$||")"
    export MANPATH="\$(echo "\$MANPATH" | sed -e "s|${SLURM_INSTALL_PATH}/share/man:||g" -e "s|:${SLURM_INSTALL_PATH}/share/man||g" -e "s|^${SLURM_INSTALL_PATH}/share/man\$||")"
    export LD_LIBRARY_PATH="\$(echo "\$LD_LIBRARY_PATH" | sed -e "s|${SLURM_INSTALL_PATH}/lib:||g" -e "s|:${SLURM_INSTALL_PATH}/lib||g" -e "s|^${SLURM_INSTALL_PATH}/lib\$||")"
    unset SLURM_CONF
    unset SLURM_SACK_SOCKET
    unset PCS_CLUSTER_NAME
    unset PCS_CLUSTER_ACTUAL_NAME
    unset PCS_CLUSTER_IDENTIFIER
    unset PCS_CLUSTER_ID
    unset PCS_CLUSTER_REGION
    unset -f deactivate-pcs-${CLUSTER_LOCAL}
    ldconfig
    echo "Deactivated PCS cluster environment: ${CLUSTER_LOCAL} (${REGION})"
}

export -f deactivate-pcs-${CLUSTER_LOCAL}

EOF

    # Start sackd last, after everything else is on disk. If it fails, the cluster is
    # still fully configured and the activate script exists, so the fix is to correct
    # whatever the logs point at and run 'systemctl restart'. There is no need to
    # re-run this script.
    systemctl daemon-reload && systemctl enable "$SACKD_SERVICE_NAME"
    if ! systemctl restart "$SACKD_SERVICE_NAME"; then
        cat >&2 << MSG

========================================
Configuration written, but sackd did not start
========================================
Service: ${SACKD_SERVICE_NAME}
Cluster: ${CLUSTER_NAME} as ${CLUSTER_LOCAL} (${REGION})
Endpoint: ${ENDPOINTS}

Check what went wrong:
  journalctl -xeu ${SACKD_SERVICE_NAME}
  systemctl status ${SACKD_SERVICE_NAME}

A start that hangs for ~90 seconds and then times out usually means this host
cannot open a TCP connection to the endpoint listed earlier. Look for:

  error: Failed to load configs from slurmctld. Retrying in 10 seconds.

For a cluster in another VPC or Region, confirm that VPC peering or transit
gateway routes exist on both sides and that security groups allow the traffic.
Being able to call the AWS PCS API does not imply the controller is reachable.

The configuration itself is complete. After you fix the cause, run:
  systemctl restart ${SACKD_SERVICE_NAME}

sackd might still be retrying in the background. To stop it:
  systemctl disable --now ${SACKD_SERVICE_NAME}

MSG
        exit 1
    fi
}

# Main function
main() {
    # Parse arguments
    CLUSTER_IDENTIFIER=""
    PCS_ENDPOINT_URL=""
    REGION=""
    ALTERNATE_SECRET_RETRIEVAL="false"
    # Local identifier for this cluster. Defaults to the cluster's own name once the
    # script knows it; set it explicitly to tell apart two clusters that share a name.
    CLUSTER_ALIAS=""
    CLUSTER_ALIAS_SET="false"
    # Overrides for what the AWS PCS API reports. All four set means the script skips
    # the call; any one unset means it makes the call and takes that value from it.
    ARG_CLUSTER_NAME=""
    ARG_CLUSTER_ID=""
    ARG_SLURM_VERSION=""
    ARG_ENDPOINTS=""
    
    while [ "$1" != "" ]; do
        case $1 in
            --cluster-identifier)
                shift
                CLUSTER_IDENTIFIER="$1"
                ;;
            --region)
                shift
                REGION="$1"
                ;;
            --fetch-secret)
                ALTERNATE_SECRET_RETRIEVAL="true"
                ;;
            --endpoint-url)
                shift
                PCS_ENDPOINT_URL="--endpoint-url $1"
                ;;
            --alias)
                shift
                CLUSTER_ALIAS="$1"
                CLUSTER_ALIAS_SET="true"
                ;;
            --cluster-name)
                shift
                ARG_CLUSTER_NAME="$1"
                ;;
            --cluster-id)
                shift
                ARG_CLUSTER_ID="$1"
                ;;
            --slurm-version)
                shift
                ARG_SLURM_VERSION="$1"
                ;;
            --endpoints)
                shift
                ARG_ENDPOINTS="$1"
                ;;
            -h|--help)
                help
                exit 0
                ;;
            *)
                echo "Invalid argument: $1" >&2
                usage >&2
                exit 1
                ;;
        esac
        shift
    done
    
    # Validate required arguments
    if [ -z "$CLUSTER_IDENTIFIER" ]; then
        echo "Error: --cluster-identifier is required" >&2
        usage >&2
        exit 1
    fi
    
    # The alias becomes a filename, a systemd unit name and a bash function name.
    if [ "$CLUSTER_ALIAS_SET" = "true" ]; then
        case "$CLUSTER_ALIAS" in
            *[!A-Za-z0-9._-]*|"")
                echo "Error: --alias accepts only letters, digits, dot, underscore and hyphen" >&2
                exit 1
                ;;
        esac
    fi
    
    # Validate running as root
    if [ "$EUID" -ne 0 ]; then
        echo "Error: This script must be run as root" >&2
        exit 1
    fi
    
    # Validate required commands are available
    for cmd in aws jq curl; do
        if ! command -v "$cmd" &> /dev/null; then
            echo "Error: Required command '$cmd' not found" >&2
            exit 1
        fi
    done
    
    # Get Region: use --region if provided, otherwise detect from IMDS
    if [ -z "$REGION" ]; then
        echo "No --region specified, detecting from instance metadata..."
        REGION=$(get_imds_region)
    fi
    echo "Using AWS Region: $REGION"

    # The API call answers whatever the command line did not, and it is the only source
    # of the secret ARN that --fetch-secret needs, so the script skips it only when
    # nothing remains to ask for.
    if [ -n "$ARG_CLUSTER_NAME" ] && [ -n "$ARG_CLUSTER_ID" ] &&
       [ -n "$ARG_SLURM_VERSION" ] && [ -n "$ARG_ENDPOINTS" ] &&
       [ "$ALTERNATE_SECRET_RETRIEVAL" = "false" ]; then
        echo "Every cluster detail was supplied; skipping the AWS PCS API call"
    else
        # Retrieve cluster information from AWS PCS
        echo "Retrieving cluster information for: $CLUSTER_IDENTIFIER (Region: $REGION)"
        # shellcheck disable=SC2086
        if ! CLUSTER_INFO=$(aws pcs get-cluster --region "$REGION" --cluster-identifier "$CLUSTER_IDENTIFIER" $PCS_ENDPOINT_URL 2>/dev/null); then
            echo "Error: Failed to retrieve cluster information. Check cluster identifier, Region, and AWS permissions." >&2
            exit 1
        fi
        
        CLUSTER_ID=$(echo "$CLUSTER_INFO" | jq -r '.cluster.id')
        CLUSTER_NAME="$(echo "$CLUSTER_INFO" | jq -r '.cluster.name')"
        SLURM_VERSION=$(echo "$CLUSTER_INFO" | jq -r '.cluster.scheduler.version')
        SLURM_VERSION=${SLURM_VERSION#Slurm_}
        ENDPOINTS=$(echo "$CLUSTER_INFO" | jq -r '.cluster.endpoints[] | select(.type == "SLURMCTLD") | (if .privateIpAddress != "" then .privateIpAddress else "[" + .ipv6Address + "]" end) + ":" + .port' | tr '\n' ',' | sed 's/,$//')
    fi
    
    # A command-line value wins over whatever the call returned. When the script skips
    # the call, all four are set and the fallbacks never apply.
    CLUSTER_ID="${ARG_CLUSTER_ID:-$CLUSTER_ID}"
    CLUSTER_NAME="${ARG_CLUSTER_NAME:-$CLUSTER_NAME}"
    SLURM_VERSION="${ARG_SLURM_VERSION:-$SLURM_VERSION}"
    ENDPOINTS="${ARG_ENDPOINTS:-$ENDPOINTS}"
    
    # Local identifier for every file, directory, unit and function the script creates.
    CLUSTER_LOCAL="${CLUSTER_ALIAS:-$CLUSTER_NAME}"
    # CLUSTER_LOCAL becomes a filename, a systemd unit name and a bash function name, so it
    # must be validated whether it came from --alias or from an unvalidated --cluster-name.
    case "$CLUSTER_LOCAL" in
        *[!A-Za-z0-9._-]*|"")
            echo "Error: cluster local name '$CLUSTER_LOCAL' must contain only letters, digits, dot, underscore and hyphen" >&2
            exit 1
            ;;
    esac
    
    # Check if Slurm version is >= 25.05
    # shellcheck disable=SC2072
    if [[ "$SLURM_VERSION" < "25.05" ]]; then
        echo "Error: This script requires Slurm version 25.05 or later. Found version: $SLURM_VERSION" >&2
        exit 1
    fi

    # The following Slurm paths come from the cluster's version rather than from
    # local discovery, so confirm that build is actually present before writing
    # anything. Without this guard, the script writes the JWKS, env file, and unit,
    # then dies on 'systemctl restart' with a bare 203/EXEC, leaving secrets on
    # disk and an enabled service that can never start, with nothing to say why.
    SLURM_INSTALL_PATH="/opt/aws/pcs/scheduler/slurm-${SLURM_VERSION}"
    if [ ! -x "${SLURM_INSTALL_PATH}/sbin/sackd" ]; then
        echo "Error: cluster $CLUSTER_IDENTIFIER runs Slurm ${SLURM_VERSION}, but no such" >&2
        echo "build is installed on this host (expected ${SLURM_INSTALL_PATH}/sbin/sackd)." >&2
        echo "Slurm versions available here:" >&2
        # The glob only ever matches PCS Slurm install directories, whose names are
        # version strings, so rewriting this with find gains nothing here. ls -1d
        # keeps the listing sorted and readable.
        # shellcheck disable=SC2012
        ls -1d /opt/aws/pcs/scheduler/slurm-* 2>/dev/null | sed 's|.*/slurm-|  |' >&2 \
            || echo "  (none found under /opt/aws/pcs/scheduler)" >&2
        exit 1
    fi
    
    if [ -z "$ENDPOINTS" ]; then
        echo "Error: cluster $CLUSTER_IDENTIFIER reports no SLURMCTLD endpoint." >&2
        echo "The cluster might still be provisioning. Check 'aws pcs get-cluster'." >&2
        exit 1
    fi
    
    # Get BASE64_SLURM_KEY
    BASE64_SLURM_KEY=$(get_auth_key)
    
    if [ -z "$BASE64_SLURM_KEY" ]; then
        echo "Error: base64 Slurm key cannot be empty" >&2
        exit 1
    fi
    
    configure_cluster
    
    # Final configuration summary
    echo "========================================"
    echo "Configuration completed successfully!"
    echo "========================================"
    echo "Cluster Name: $CLUSTER_NAME"
    echo "Local Alias: $CLUSTER_LOCAL"
    echo "Cluster ID: $CLUSTER_ID"
    echo "Region: $REGION"
    echo "Slurm Version: $SLURM_VERSION"
    echo "Service Name: $SACKD_SERVICE_NAME"
    echo "SACKD Port: $SACKD_PORT"
    echo
    echo "To activate this cluster environment, run:"
    echo "  source ./$ACTIVATE_SCRIPT"
    echo
    echo "To deactivate this cluster environment, run:"
    echo "  deactivate-pcs-${CLUSTER_LOCAL}"
    echo
    echo "To check service status:"
    echo "  systemctl status $SACKD_SERVICE_NAME"
    echo
    echo "To view service logs:"
    echo "  journalctl -u $SACKD_SERVICE_NAME -f"
}

# Exit if being sourced for testing
[[ "${BASH_SOURCE[0]}" != "${0}" ]] && return

# Execute main function
main "$@"
```