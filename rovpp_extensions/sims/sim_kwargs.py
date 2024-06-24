from multiprocessing import cpu_count
from pathlib import Path
import sys
from typing import Iterable

from bgpy.enums import ASGroups, Plane, Outcomes, SpecialPercentAdoptions
from bgpy.simulation_engine import ROV
from bgpy.simulation_framework.metric_tracker.metric_key import MetricKey

from ..policies import (
    ROVPPV1LiteRenamed,
    ROVPPV2LiteRenamed,
    ROVPPV2iLiteRenamed,
    ROVPPV2ShortenedLite,
)

DIR = Path.home() / "Desktop" / "rovpp_reproduction"

default_kwargs = {
    "percent_adoptions": (.5,) if "quick" in sys.argv else (
        SpecialPercentAdoptions.ONLY_ONE,
        0.1,
        0.2,
        0.5,
        0.8,
        0.99,
    ),
    "num_trials": 1 if "quick" in str(sys.argv) else 50,
    "parse_cpus": cpu_count() - 2,
}


ROVPP_CLASSES = (
    ROVPPV2ShortenedLite,
    ROVPPV2iLiteRenamed,
    ROVPPV2LiteRenamed,
    ROVPPV1LiteRenamed,
    ROV
)


# NOTE: Normally you don't need custom metric keys
# but ROV++ paper looked specifically at the edge ASes
# So I've modified this to track the edge ASes (stubs or multihomed)
# for most papers, looking at the internet as a whole is good enough
# Additionally, adding these significantly slows down the simulations,
# so best to stick to the defaults when you can
def get_rovpp_metric_keys() -> Iterable[MetricKey]:
    """Returns all possible metric key combos for ROV++

    Modified from the utils file within the sim framework"""

    for plane in [Plane.DATA]:
        for as_group in [ASGroups.ALL_WOUT_IXPS, ASGroups.STUBS_OR_MH]:
            for outcome in [x for x in Outcomes if x != Outcomes.UNDETERMINED]:
                yield MetricKey(plane=plane, as_group=as_group, outcome=outcome)
