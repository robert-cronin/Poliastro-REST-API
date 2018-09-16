import numpy as np
import matplotlib.pyplot as plt

from poliastro.plotting import plot
from astropy import units as u

from poliastro.bodies import Earth, Mars, Sun
from poliastro.twobody import Orbit

from io import BytesIO
import base64

plt.style.use("seaborn")  # Recommended

# Data for Mars at J2000 from JPL HORIZONS
a = 1.523679 * u.AU
ecc = 0.093315 * u.one
inc = 1.85 * u.deg
raan = 49.562 * u.deg
argp = 286.537 * u.deg
nu = 23.33 * u.deg

ss = Orbit.from_classical(Sun, a, ecc, inc, raan, argp, nu)

# Plot and save to variable
plot(ss)
ploteBytes = BytesIO()
plt.savefig(ploteBytes, format='png')
plotBase64 = base64.encodestring(ploteBytes.getvalue())

# Create a handler for our read (GET) people
# def returnOrbitAs(coordinateSystemType = "vectors"):
def returnOrbitAsVectors():
    """
    This function responds to a request for /api/twobody.orbit
    with the orbit object

    :return:        orbit object
    """
    ORBIT_FROM_VECTORS = {
        "orbitstring": str(ss),
        "attractor": str(ss.attractor),
        "r": {
            "x": ss.r.value[0],
            "y": ss.r.value[1],
            "z": ss.r.value[2],
        },
        "v": {
            "x": ss.v.value[0],
            "y": ss.v.value[1],
            "z": ss.v.value[2],
        },
        "epoch": ss.epoch.iso,
        "plotbase64": plotBase64.decode('ascii')
    };
    return ORBIT_FROM_VECTORS
