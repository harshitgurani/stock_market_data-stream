import logging
from kiteconnect import KiteTicker,KiteConnect

logging.basicConfig(level=logging.DEBUG)


kws = KiteTicker("api_key", "request_token")

def on_ticks(ws, ticks):
    # Callback to receive ticks.
    print("Ticks: {}".format(ticks))

def on_connect(ws, response):
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
    ws.subscribe([35415, 35089])
    ws.set_mode(ws.MODE_FULL,[35415, 35089])

    # Set RELIANCE to tick in `full` mode.
    ws.set_mode(ws.MODE_FULL, [35415, 35089])

def on_close(ws, code, reason):
    # On connection close stop the main loop
    # Reconnection will not happen after executing `ws.stop()`
    ws.stop()

kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

kws.connect()

