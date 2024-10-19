#"""Support for E-Ink Display sensors."""
#from __future__ import annotations
#
#import logging
#from typing import Any
#
#from bleak import BleakClient
#
#from homeassistant.components.sensor import SensorEntity
#from homeassistant.config_entries import ConfigEntry
#from homeassistant.core import HomeAssistant
#from homeassistant.helpers.entity_platform import AddEntitiesCallback
#
#from .const import DOMAIN, SERVICE_UUID
#
#_LOGGER = logging.getLogger(__name__)
#
#async def async_setup_entry(
#    hass: HomeAssistant,
#    entry: ConfigEntry,
#    async_add_entities: AddEntitiesCallback,
#) -> None:
#    """Set up E-Ink Display sensor based on a config entry."""
#    address = entry.data["address"]
#    async_add_entities([EInkDisplaySensor(address)], True)
#
#class EInkDisplaySensor(SensorEntity):
#    """Representation of an E-Ink Display sensor."""
#
#    def __init__(self, address: str) -> None:
#        """Initialize the sensor."""
#        self._address = address
#        self._attr_name = f"E-Ink Display {address}"
#        self._attr_unique_id = f"{DOMAIN}_{address}"
#        self._state: Any = None
#
#    async def async_update(self) -> None:
#        """Fetch new state data for the sensor."""
#        try:
#            async with BleakClient(self._address) as client:
#                services = await client.get_services()
#                service = next((s for s in services if s.uuid == SERVICE_UUID), None)
#                if service:
#                    for char in service.characteristics:
#                        if "read" in char.properties:
#                            data = await client.read_gatt_char(char.uuid)
#                            self._state = int.from_bytes(data, byteorder="little")
#                            break
#                else:
#                    _LOGGER.error("Service not found")
#        except Exception as error:
#            _LOGGER.error("Could not read state: %s", error)
#
#    @property
#    def state(self) -> Any:
#        """Return the state of the sensor."""
#        return self._state