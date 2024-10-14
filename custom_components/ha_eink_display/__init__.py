from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType
from .const import *

# manifest.json[requirements] should contain all the used pip packages. See 
# https://developers.home-assistant.io/docs/creating_integration_manifest/

# See integration documentation here:
# https://developers.home-assistant.io/docs/creating_component_index

# This integration should not interface with the device directly, but rather
# with a 3rd-party python 3 library. This is then published to PyPi
# --> Need to create a new repo for this?

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.data[DOMAIN] = entry.data
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    await hass.config_entries.async_forward_entry_unload(entry, "sensor")
    hass.data.pop(DOMAIN)
    return True
