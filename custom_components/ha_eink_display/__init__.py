# manifest.json[requirements] should contain all the used pip packages. See 
# https://developers.home-assistant.io/docs/creating_integration_manifest/

# See integration documentation here:
# https://developers.home-assistant.io/docs/creating_component_index

# This integration should not interface with the device directly, but rather
# with a 3rd-party python 3 library. This is then published to PyPi
# --> Need to create a new repo for this?
#"""The E-Ink Display integration."""
#from __future__ import annotations
#
#from homeassistant.config_entries import ConfigEntry
#from homeassistant.core import HomeAssistant
#from homeassistant.components import bluetooth
#
#from .const import DOMAIN
#
#PLATFORMS: list[str] = ["sensor"]
#
#async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
#    """Set up E-Ink Display from a config entry."""
#    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
#    
#    # Set up Bluetooth connection
#    address = entry.data["address"]
#    entry.async_on_unload(
#        bluetooth.async_register_callback(
#            hass,
#            lambda _, advertisement: process_advertisement(hass, entry, advertisement),
#            {bluetooth.SERVICE_UUID: "6ff79d5c-e899-4531-90d8-5cc8adcf65a2"},
#            bluetooth.BluetoothScanningMode.ACTIVE,
#        )
#    )
#    
#    return True

#async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
#    """Unload a config entry."""
#    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
#
#def process_advertisement(hass: HomeAssistant, entry: ConfigEntry, advertisement):
#    """Process a BLE advertisement."""
#    # Implement your advertisement processing logic here
#    pass

"""
The "hello world" custom component.

This component implements the bare minimum that a component should implement.

Configuration:

To use the hello_world component you will need to add the following to your
configuration.yaml file.

hello_world_async:
"""
from __future__ import annotations

import asyncio

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "ha_eink_display"

@asyncio.coroutine
def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Setup our skeleton component."""
    # States are in the format DOMAIN.OBJECT_ID.
    hass.states.async_set('ha_eink_display.Hello_World', 'Works!')

    # Return boolean to indicate that initialization was successfully.
    return True