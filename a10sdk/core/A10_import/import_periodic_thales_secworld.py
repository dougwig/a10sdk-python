from a10sdk.common.A10BaseClass import A10BaseClass


class ThalesSecworld(A10BaseClass):
    
    """Class Description::
    import Thales security world files.

    Class thales-secworld supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param remote_file: {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}
    :param period: {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}
    :param thales_secworld: {"description": "import Thales security world files - in .tgz format that has all files needed by AX", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param overwrite: {"default": 0, "optional": true, "type": "number", "description": "Overwrite existing file", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/import-periodic/thales-secworld/{thales_secworld}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "thales_secworld"]

        self.b_key = "thales-secworld"
        self.a10_url="/axapi/v3/import-periodic/thales-secworld/{thales_secworld}"
        self.DeviceProxy = ""
        self.uuid = ""
        self.remote_file = ""
        self.period = ""
        self.thales_secworld = ""
        self.use_mgmt_port = ""
        self.overwrite = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


