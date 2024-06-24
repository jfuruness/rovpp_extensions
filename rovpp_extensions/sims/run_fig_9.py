from bgpy.simulation_framework import (
    Simulation,
    SubprefixHijack,
    ScenarioConfig,
)

from .sim_kwargs import DIR, ROVPP_CLASSES, get_rovpp_metric_keys, default_kwargs


def run_fig678():
    """Runs fig6,7,8 from ROV++ paper with policies that are implemented in BGPy

    fig 6 looks at the adopting_is_any
    fig 7 looked at adopting_is_true from stubs or multihomed
    fig 8 looked at adopting_is_false from stubs or multihomed

    CAVEAT - in the ROV++ paper we simulated non-lite versions, but BGPy has only
    the recommended lite versions
    """

    sim = Simulation(
        scenario_configs=[
            ScenarioConfig(
                ScenarioCls=SubprefixHijack,
                AdoptPolicyCls=Cls,
            )
            for Cls in ROVPP_CLASSES
        ],
        output_dir=DIR / "fig678",
        metric_keys=tuple(list(get_rovpp_metric_keys())),
        **default_kwargs,  # type: ignore
    )
    sim.run()
