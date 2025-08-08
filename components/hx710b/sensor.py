import esphome.codegen as cg
from esphome.components import sensor
from . import CONF_ID, CONF_DOUT_PIN, CONF_CLK_PIN, HX710BSensor

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)
    
    dout = await cg.gpio_pin_expression(config[CONF_DOUT_PIN])
    clk = await cg.gpio_pin_expression(config[CONF_CLK_PIN])
    cg.add(var.set_dout_pin(dout))
    cg.add(var.set_clk_pin(clk))