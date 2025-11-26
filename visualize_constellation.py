# MIT License
#
# Copyright (c) 2020 Debopam Bhattacherjee
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# from astropy import units as u
# from poliastro.bodies import Earth
# from poliastro.twobody import Orbit
# from astropy.time import Time
# from extractor import CZMLExtractor
import math
try:
    from . import util
except (ImportError, SystemError):
    import util

# Generate static visualizations for entire constellation (multiple shells).

EARTH_RADIUS = 6378135.0 # WGS72 value; taken from https://geographiclib.sourceforge.io/html/NET/NETGeographicLib_8h_source.html

# CONSTELLATION GENERATION GENERAL CONSTANTS
ECCENTRICITY = 0.0000001  # Circular orbits are zero, but pyephem does not permit 0, so lowest possible value
ARG_OF_PERIGEE_DEGREE = 0.0
PHASE_DIFF = True
EPOCH = "2000-01-01 00:00:00"

# Shell wise color codes
# COLOR = [[255, 0, 0, 200], [32, 128, 46, 200], [0, 0, 255, 200], [245, 66, 242, 200], [245, 126, 66, 200]]
COLOR = [
    'CRIMSON', 'FORESTGREEN', 'DODGERBLUE', 'PERU', 'BLUEVIOLET', 'DARKMAGENTA',
    'CORAL', 'TEAL', 'GOLD', 'INDIGO', 'SALMON', 'OLIVE',
    'TURQUOISE', 'ORANGE', 'PURPLE', 'LIME', 'CYAN', 'MAGENTA'
]
# CONSTELLATION SPECIFIC PARAMETERS


# STARLINK
NAME = "Starlink"

SHELL_CNTR = 8

MEAN_MOTION_REV_PER_DAY = [None]*SHELL_CNTR
ALTITUDE_M = [None]*SHELL_CNTR
NUM_ORBS = [None]*SHELL_CNTR
NUM_SATS_PER_ORB = [None]*SHELL_CNTR
INCLINATION_DEGREE = [None]*SHELL_CNTR
BASE_ID = [None]*SHELL_CNTR
ORB_WISE_IDS = [None]*SHELL_CNTR

# Shell 1 (id=0): 72x22, 550km, 53.05 deg
MEAN_MOTION_REV_PER_DAY[0] = 15.05  # 550km
ALTITUDE_M[0] = 550000
NUM_ORBS[0] = 72
NUM_SATS_PER_ORB[0] = 22
INCLINATION_DEGREE[0] = 53.05
BASE_ID[0] = 0
ORB_WISE_IDS[0] = []

# Shell 2 (id=1): 36x20, 570km, 70.0 deg
MEAN_MOTION_REV_PER_DAY[1] = 14.99  # 570km
ALTITUDE_M[1] = 570000
NUM_ORBS[1] = 36
NUM_SATS_PER_ORB[1] = 20
INCLINATION_DEGREE[1] = 70.0
BASE_ID[1] = BASE_ID[0] + NUM_ORBS[0] * NUM_SATS_PER_ORB[0] # 1584
ORB_WISE_IDS[1] = []

# Shell 3 (id=2): 6x58, 560km, 97.6 deg
MEAN_MOTION_REV_PER_DAY[2] = 15.02  # 560km
ALTITUDE_M[2] = 560000
NUM_ORBS[2] = 6
NUM_SATS_PER_ORB[2] = 58
INCLINATION_DEGREE[2] = 97.6
BASE_ID[2] = BASE_ID[1] + NUM_ORBS[1] * NUM_SATS_PER_ORB[1] # 2304
ORB_WISE_IDS[2] = []

# Shell 4 (id=3): 72x22, 540km, 53.22 deg
MEAN_MOTION_REV_PER_DAY[3] = 15.09  # 540km
ALTITUDE_M[3] = 540000
NUM_ORBS[3] = 72
NUM_SATS_PER_ORB[3] = 22
INCLINATION_DEGREE[3] = 53.22
BASE_ID[3] = BASE_ID[2] + NUM_ORBS[2] * NUM_SATS_PER_ORB[2] # 2652
ORB_WISE_IDS[3] = []

# Shell 5 (id=4): 4x43, 560km, 97.6 deg
MEAN_MOTION_REV_PER_DAY[4] = 15.02  # 560km
ALTITUDE_M[4] = 560000
NUM_ORBS[4] = 4
NUM_SATS_PER_ORB[4] = 43
INCLINATION_DEGREE[4] = 97.6
BASE_ID[4] = BASE_ID[3] + NUM_ORBS[3] * NUM_SATS_PER_ORB[3] # 4236
ORB_WISE_IDS[4] = []

# Gen 2 Shells

# Shell 6 (id=5): 28x120, 530km, 43.0 deg
MEAN_MOTION_REV_PER_DAY[5] = 15.12  # 计算值 (530km)
ALTITUDE_M[5] = 530000
NUM_ORBS[5] = 28
NUM_SATS_PER_ORB[5] = 120
INCLINATION_DEGREE[5] = 43.0
BASE_ID[5] = BASE_ID[4] + NUM_ORBS[4] * NUM_SATS_PER_ORB[4] # 4408
ORB_WISE_IDS[5] = []

# Shell 7 (id=6): 28x120, 525km, 53.0 deg
MEAN_MOTION_REV_PER_DAY[6] = 15.14  # 计算值 (525km)
ALTITUDE_M[6] = 525000
NUM_ORBS[6] = 28
NUM_SATS_PER_ORB[6] = 120
INCLINATION_DEGREE[6] = 53.0
BASE_ID[6] = BASE_ID[5] + NUM_ORBS[5] * NUM_SATS_PER_ORB[5] # 7768
ORB_WISE_IDS[6] = []

# Shell 8 (id=7): 28x120, 535km, 53.0 deg
MEAN_MOTION_REV_PER_DAY[7] = 15.10  # 计算值 (535km)
ALTITUDE_M[7] = 535000
NUM_ORBS[7] = 28
NUM_SATS_PER_ORB[7] = 120
INCLINATION_DEGREE[7] = 53.0
BASE_ID[7] = BASE_ID[6] + NUM_ORBS[6] * NUM_SATS_PER_ORB[6] # 11128
ORB_WISE_IDS[7] = []


"""
# OneWeb
NAME = "OneWeb"
SHELL_CNTR = 2

MEAN_MOTION_REV_PER_DAY = [None]*SHELL_CNTR
ALTITUDE_M = [None]*SHELL_CNTR
NUM_ORBS = [None]*SHELL_CNTR
NUM_SATS_PER_ORB = [None]*SHELL_CNTR
INCLINATION_DEGREE = [None]*SHELL_CNTR
BASE_ID = [None]*SHELL_CNTR
ORB_WISE_IDS = [None]*SHELL_CNTR

# Shell 1 (id=0): 12x49, 1200km, 87.9 deg
# Calculation: 1200km -> ~13.16 revs/day
MEAN_MOTION_REV_PER_DAY[0] = 13.16
ALTITUDE_M[0] = 1200000
NUM_ORBS[0] = 12
NUM_SATS_PER_ORB[0] = 49
INCLINATION_DEGREE[0] = 87.9
BASE_ID[0] = 0
ORB_WISE_IDS[0] = []

# Shell 2 (id=1): 8x16, 1200km, 55.0 deg
# Calculation: 1200km -> ~13.16 revs/day
MEAN_MOTION_REV_PER_DAY[1] = 13.16
ALTITUDE_M[1] = 1200000
NUM_ORBS[1] = 8
NUM_SATS_PER_ORB[1] = 16
INCLINATION_DEGREE[1] = 55.0
BASE_ID[1] = BASE_ID[0] + NUM_ORBS[0] * NUM_SATS_PER_ORB[0] # 588
ORB_WISE_IDS[1] = []
"""

""""
# KUIPER
NAME = "kuiper"

NAME = "Kuiper"
SHELL_CNTR = 3

MEAN_MOTION_REV_PER_DAY = [None]*SHELL_CNTR
ALTITUDE_M = [None]*SHELL_CNTR
NUM_ORBS = [None]*SHELL_CNTR
NUM_SATS_PER_ORB = [None]*SHELL_CNTR
INCLINATION_DEGREE = [None]*SHELL_CNTR
BASE_ID = [None]*SHELL_CNTR
ORB_WISE_IDS = [None]*SHELL_CNTR

# Shell 1 (id=0): 28x28, 590km, 33 deg
# Calculation: 590km -> ~14.93 revs/day
MEAN_MOTION_REV_PER_DAY[0] = 14.93
ALTITUDE_M[0] = 590000
NUM_ORBS[0] = 28
NUM_SATS_PER_ORB[0] = 28
INCLINATION_DEGREE[0] = 33
BASE_ID[0] = 0
ORB_WISE_IDS[0] = []

# Shell 2 (id=1): 36x36, 610km, 42 deg
# Calculation: 610km -> ~14.86 revs/day
MEAN_MOTION_REV_PER_DAY[1] = 14.86
ALTITUDE_M[1] = 610000
NUM_ORBS[1] = 36
NUM_SATS_PER_ORB[1] = 36
INCLINATION_DEGREE[1] = 42.0
BASE_ID[1] = BASE_ID[0] + NUM_ORBS[0] * NUM_SATS_PER_ORB[0] # 784
ORB_WISE_IDS[1] = []

# Shell 3 (id=2): 34x34, 630km, 51.9 deg
# Calculation: 630km -> ~14.80 revs/day
MEAN_MOTION_REV_PER_DAY[2] = 14.80
ALTITUDE_M[2] = 630000
NUM_ORBS[2] = 34
NUM_SATS_PER_ORB[2] = 34
INCLINATION_DEGREE[2] = 51.9
BASE_ID[2] = BASE_ID[1] + NUM_ORBS[1] * NUM_SATS_PER_ORB[1] # 2080
ORB_WISE_IDS[2] = []
"""


# General files needed to generate visualizations; Do not change for different simulations
topFile = "./static_html/top.html"
bottomFile = "./static_html/bottom.html"

# Output directory for creating visualization html files
OUT_DIR = "./CesiumApp/"
# JSON_NAME  = NAME+"_5shell.json"
# OUT_JSON_FILE = OUT_DIR + JSON_NAME
OUT_HTML_FILE = OUT_DIR + NAME + ".html"

# START = Time(EPOCH, scale="tdb")
# END = START + (10*60) * u.second
# sample_points = 10
# extractor = CZMLExtractor(START, END, sample_points)


def generate_satellite_trajectories():
    """
    Generates and adds satellite orbits to visualization.
    :return: viz_string
    """
    viz_string = ""
    for i in range(0, SHELL_CNTR):
        sat_objs = util.generate_sat_obj_list(
            NUM_ORBS[i],
            NUM_SATS_PER_ORB[i],
            EPOCH,
            PHASE_DIFF,
            INCLINATION_DEGREE[i],
            ECCENTRICITY,
            ARG_OF_PERIGEE_DEGREE,
            MEAN_MOTION_REV_PER_DAY[i],
            ALTITUDE_M[i]
        )
        for j in range(len(sat_objs)):
            sat_objs[j]["sat_obj"].compute(EPOCH)
            # viz_string += "var redSphere = viewer.entities.add({name : '', position: Cesium.Cartesian3.fromDegrees(" \
            #               + str(math.degrees(sat_objs[j]["sat_obj"].sublong)) + ", " \
            #               + str(math.degrees(sat_objs[j]["sat_obj"].sublat)) + ", " + str(
            #     sat_objs[j]["alt_km"] * 1000) + "), " \
            #               + "ellipsoid : {radii : new Cesium.Cartesian3(30000.0, 30000.0, 30000.0), " \
            #               + "material : Cesium.Color.BLACK.withAlpha(1),}});\n"

            viz_string += (
            "var sat = viewer.entities.add({"
            "position: Cesium.Cartesian3.fromDegrees("
            + str(math.degrees(sat_objs[j]["sat_obj"].sublong)) + ", "
            + str(math.degrees(sat_objs[j]["sat_obj"].sublat)) + ", "
            + str(sat_objs[j]["alt_km"] * 1000) + "), "
            "point: {"
            "pixelSize: 4, "
            "color: Cesium.Color.BLACK.withAlpha(1)"
            "}"
            "});\n"
            ) 
        orbit_links = util.find_orbit_links(sat_objs, NUM_ORBS[i], NUM_SATS_PER_ORB[i])
        for key in orbit_links:
            sat1 = orbit_links[key]["sat1"]
            sat2 = orbit_links[key]["sat2"]
            viz_string += "viewer.entities.add({name : '', polyline: { positions: Cesium.Cartesian3.fromDegreesArrayHeights([" \
                          + str(math.degrees(sat_objs[sat1]["sat_obj"].sublong)) + "," \
                          + str(math.degrees(sat_objs[sat1]["sat_obj"].sublat)) + "," \
                          + str(sat_objs[sat1]["alt_km"] * 1000) + "," \
                          + str(math.degrees(sat_objs[sat2]["sat_obj"].sublong)) + "," \
                          + str(math.degrees(sat_objs[sat2]["sat_obj"].sublat)) + "," \
                          + str(sat_objs[sat2]["alt_km"] * 1000) + "]), " \
                          + "width: 0.5, arcType: Cesium.ArcType.NONE, " \
                          + "material: new Cesium.PolylineOutlineMaterialProperty({ " \
                          + "color: Cesium.Color."+COLOR[i]+".withAlpha(0.4), outlineWidth: 0, outlineColor: Cesium.Color.BLACK})}});"
    return viz_string


def write_viz_files():
    """
    Writes JSON and TML files to the output folder
    :return: None
    """
    writer_html = open(OUT_HTML_FILE, 'w')
    with open(topFile, 'r') as fi:
        writer_html.write(fi.read())
    writer_html.write(viz_string)
    with open(bottomFile, 'r') as fb:
        writer_html.write(fb.read())
    writer_html.close()


viz_string = generate_satellite_trajectories()
write_viz_files()