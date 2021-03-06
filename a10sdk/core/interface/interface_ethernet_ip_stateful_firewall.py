from a10sdk.common.A10BaseClass import A10BaseClass


class StatefulFirewall(A10BaseClass):
    
    """Class Description::
    Configure Stateful Firewall direction.

    Class stateful-firewall supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param access_list: {"default": 0, "optional": true, "type": "number", "description": "Access-list for traffic from the outside", "format": "flag"}
    :param inside: {"default": 0, "optional": true, "type": "number", "description": "Inside (private) interface for stateful firewall", "format": "flag"}
    :param acl_id: {"description": "ACL id", "format": "number", "type": "number", "maximum": 199, "minimum": 1, "optional": true}
    :param outside: {"default": 0, "optional": true, "type": "number", "description": "Outside (public) interface for stateful firewall", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/ethernet/{ifnum}/ip/stateful-firewall`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "stateful-firewall"
        self.a10_url="/axapi/v3/interface/ethernet/{ifnum}/ip/stateful-firewall"
        self.DeviceProxy = ""
        self.access_list = ""
        self.inside = ""
        self.acl_id = ""
        self.outside = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


