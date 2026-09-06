

# How to mark a key as trusted with the AWS CloudHSM Management Utility
<a name="cloudhsm_using_trusted_keys_control_key_wrap"></a>

The content in this section provides instructions on using the AWS CloudHSM management Utility (CMU) to mark a key as trusted.

1. Using the [loginHSM](cloudhsm_mgmt_util-loginLogout.md) command, log in as a crypto officer (CO).

1. Use the [Set the attributes of AWS CloudHSM keys using CMU](cloudhsm_mgmt_util-setAttribute.md) command with `OBJ_ATTR_TRUSTED` (value `134`) set to true (`1`).

   ```
   aws-cloudhsm > setAttribute {{<Key Handle>}} 134 1
   ```