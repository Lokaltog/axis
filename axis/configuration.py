"""Python library to enable Axis devices to be integrated in to Home Assistant."""

class Configuration(object):
    """Device configuration."""

    def __init__(self, loop, host, username, password, **kwargs):
        """All config params available to the device."""
        self.loop = loop
        self.web_proto = kwargs.get('web_proto', 'http')
        self.host = host
        self.port = kwargs.get('port', 80)
        self.username = username
        self.password = password
        self.event_types = kwargs.get('events', None)
        self.signal = kwargs.get('signal', None)
        self.kwargs = kwargs
