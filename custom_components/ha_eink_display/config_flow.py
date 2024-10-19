#"""Config flow for E-Ink Display integration."""
#from __future__ import annotations
#
#import logging
#from typing import Any
#
#from bleak import BleakScanner
#import voluptuous as vol
#
#from homeassistant import config_entries
#from homeassistant.components.bluetooth import (
#    BluetoothServiceInfoBleak,
#    async_discovered_service_info,
#)
#from homeassistant.const import CONF_ADDRESS
#from homeassistant.data_entry_flow import FlowResult
#
#from .const import DOMAIN
#
#_LOGGER = logging.getLogger(__name__)
#
#SERVICE_UUID = "6ff79d5c-e899-4531-90d8-5cc8adcf65a2"
#
#class EInkDisplayConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
#    """Handle a config flow for E-Ink Display."""
#
#    VERSION = 1
#
#    async def async_step_bluetooth(self, discovery_info: BluetoothServiceInfoBleak) -> FlowResult:
#        """Handle the bluetooth discovery step."""
#        if SERVICE_UUID not in discovery_info.service_uuids:
#            return self.async_abort(reason="not_supported")
#        
#        await self.async_set_unique_id(discovery_info.address)
#        self._abort_if_unique_id_configured()
#        return await self.async_step_user()
#
#    async def async_step_user(
#        self, user_input: dict[str, Any] | None = None
#    ) -> FlowResult:
#        """Handle the initial step."""
#        if user_input is None:
#            return self.async_show_form(
#                step_id="user",
#                data_schema=vol.Schema(
#                    {
#                        vol.Required(CONF_ADDRESS): str,
#                    }
#                ),
#            )
#
#        address = user_input[CONF_ADDRESS]
#        
#        # Validate the address by attempting to connect
#        scanner = BleakScanner()
#        devices = await scanner.discover()
#        device = next((d for d in devices if d.address == address), None)
#        
#        if not device:
#            return self.async_show_form(
#                step_id="user",
#                data_schema=vol.Schema({vol.Required(CONF_ADDRESS): str}),
#                errors={"base": "device_not_found"},
#            )
#
#        return self.async_create_entry(title=f"E-Ink Display {address}", data=user_input)