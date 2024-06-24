from random import shuffle

from bgpy.as_graphs import CAIDAASGraphConstructor
from bgpy.simulation_engine import ROV
from bgpy.enums import ASGroups
from bgpy.simulation_framework import (
    Simulation,
    SubprefixHijack,
    ScenarioConfig,
)
from frozendict import frozendict

from .sim_kwargs import DIR, ROVPP_CLASSES, get_rovpp_metric_keys, default_kwargs


# NOTE: When using hardcoded ASes, you __must__ use an AS class that is not
# also used the AdoptPolicyCls
class ForcedROV(ROV):
    name = "Forced ROV"


def run_50_percent():
    """Runs a subprefix hijack when 50% of ASes use ROV"""

    bgp_dag = CAIDAASGraphConstructor(tsv_path=None).run()
    ases = list(bgp_dag)
    shuffle(ases)
    hardcoded_asn_cls_dict = frozendict(
        {x.asn: ForcedROV for x in ases[: len(ases) // 2]}
    )

    sim = Simulation(
        scenario_configs=tuple(
            [
                ScenarioConfig(
                    ScenarioCls=SubprefixHijack,
                    AdoptPolicyCls=Cls,
                    hardcoded_asn_cls_dict=hardcoded_asn_cls_dict,
                    # Removed the input clique from this list
                    adoption_subcategory_attrs=(
                        ASGroups.STUBS_OR_MH.value,
                        ASGroups.ETC.value,
                    ),
                )
                for Cls in ROVPP_CLASSES
            ]
        ),
        output_dir=DIR / "subprefix_hijack_50_percent_adopt_rov",
        metric_keys=tuple(list(get_rovpp_metric_keys())),
        **default_kwargs,  # type: ignore
    )
    sim.run()
