import threading
import time

from cozify import hub, cloud
from cozify.Error import APIError

class CozifyDevices(object):
    def __init__(self, interval=600):
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        try:
            # Check connectivity and have it auto-renewed if it's deemed time to do so.
            cloud.ping()
            hub.ping()
            # Get and cache all devices.
            self.devicecache = hub.devices()
        except APIError as e:
            if e.status_code == 401: # auth failed
                logging.warning('Auth failed, this should not happen.')
            else:
                raise # we ignore all other APIErrors and let it burn to the ground
        time.sleep(self.interval)
