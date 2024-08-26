from homeassistant import config_entries
from homeassistant.core import callback
import voluptuous as vol

from .const import DOMAIN

class EInkDisplayConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        if user_input is None:
            return self.async_show_form(
                step_id="user",
                data_schema=vol.Schema({
                    vol.Required("device_mac"): str,
                })
            )

        return self.async_create_entry(title="Your BLE Device", data=user_input)
