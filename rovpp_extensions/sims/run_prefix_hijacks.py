from bgpy.simulation_framework import (
    Simulation,
    PrefixHijack,
    ScenarioConfig,
)

from .sim_kwargs import DIR, ROVPP_CLASSES, get_rovpp_metric_keys, default_kwargs


def run_prefix_hijacks():
    """Runs prefix hijacks, where ROV++ performs the same as ROV"""

    sim = Simulation(
        scenario_configs=tuple([
            ScenarioConfig(
                ScenarioCls=PrefixHijack,
                AdoptPolicyCls=Cls,
            )
            for Cls in ROVPP_CLASSES
        ]),
        output_dir=DIR / "prefix_hijack",
        metric_keys=tuple(list(get_rovpp_metric_keys())),
        **default_kwargs,  # type: ignore
    )
    sim.run()
