from bgpy.simulation_framework import (
    Simulation,
    NonRoutedSuperprefixPrefixHijack,
    ScenarioConfig,
)

from .sim_kwargs import DIR, ROVPP_CLASSES, get_rovpp_metric_keys, default_kwargs


def run_fig10():
    """Runs fig10 from ROV++ paper with policies that are implemented in BGPy

    for this fig, adopting_is_False, and from stubs or multihomed

    CAVEAT - in the ROV++ paper we simulated non-lite versions, but BGPy has only
    the recommended lite versions
    """

    sim = Simulation(
        scenario_configs=tuple(
            [
                ScenarioConfig(
                    ScenarioCls=NonRoutedSuperprefixPrefixHijack,
                    AdoptPolicyCls=Cls,
                )
                for Cls in ROVPP_CLASSES
            ]
        ),
        output_dir=DIR / "fig10",
        metric_keys=tuple(list(get_rovpp_metric_keys())),
        **default_kwargs,  # type: ignore
    )
    sim.run()
