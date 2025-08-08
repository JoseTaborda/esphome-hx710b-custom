import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from . import HX710BSensor, CONF_HX710B

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)
    
    dout_pin = await cg.gpio_pin_expression(config['dout_pin'])
    clk_pin = await cg.gpio_pin_expression(config['clk_pin'])
    cg.add(var.set_dout_pin(dout_pin))
    cg.add(var.set_clk_pin(clk_pin))