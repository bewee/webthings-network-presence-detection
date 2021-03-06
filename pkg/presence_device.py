"""Network presence adapter for WebThings Gateway."""

from gateway_addon import Device
from .presence_property import PresenceProperty



class PresenceDevice(Device):
    """network presence device type."""

    def __init__(self, adapter, _id, name, details):
        """
        Initialize the object.

        adapter -- the Adapter managing this device
        _id -- ID of this device
        name -- The name for this device
        index -- index inside parent device
        """

        
        #Device.__init__(self, adapter, 'presence-{}'.format(mac))
        Device.__init__(self, adapter, _id)

        self.adapter = adapter
        self.name = name
        self.description = "A device on the local network"
        self._type = ['BinarySensor']
        #self.properties = {}
        #print("device self.properties at init: " + str(self.properties))
        #self.connected_notify(True)

        self.properties['details'] = PresenceProperty(
            self,
            'details',
            {
                'label': 'Details',
                'type': 'string',
                'readOnly': True,
            },
            str(details))
            
        if self.adapter.DEBUG:
            print("+ Adding new device: " + str(name))


    def add_boolean_child(self, propertyID, new_description, new_value):
        if self.adapter.DEBUG:
            print("+ DEVICE.ADD_BOOLEAN_CHILD with id: " + str(propertyID))

        self.properties[propertyID] = PresenceProperty(
            self,
            propertyID,
            {
                '@type': 'BooleanProperty',
                'label': new_description,
                'type': 'boolean',
                'readOnly': True,
            },
            new_value)

        try:
            self.notify_property_changed(self.properties[propertyID])
            self.adapter.handle_device_added(self)
            #print("-All properties: " + str(self.get_property_descriptions()))

        except Exception as ex:
            print("Error in handle_device_added after adding property: " + str(ex))


    def add_integer_child(self, propertyID, new_description, new_value):
        if self.adapter.DEBUG:
            print("+ DEVICE.ADD_INTEGER_CHILD with id: " + str(propertyID))

        self.properties[propertyID] = PresenceProperty(
            self,
            propertyID,
            {
                'label': new_description,
                'type': 'integer',
                'readOnly': True,
            },
            new_value)

        try:
            self.notify_property_changed(self.properties[propertyID])
            self.adapter.handle_device_added(self)
            #print("-All properties: " + str(self.get_property_descriptions()))

        except Exception as ex:
            print("Handle_device_added after adding property error: " + str(ex))
