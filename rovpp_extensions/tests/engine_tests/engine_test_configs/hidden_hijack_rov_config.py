from frozendict import frozendict
from bgpy.tests.engine_tests.utils import EngineTestConfig

from bgpy.as_graphs.base.links import CustomerProviderLink as CPLink
from bgpy.as_graphs import ASGraphInfo
from bgpy.enums import ASNs

from bgpy.simulation_engine import BGP, ROV
from bgpy.simulation_framework import (
    ScenarioConfig,
    SubprefixHijack,
)


as_graph_info = ASGraphInfo(
    customer_provider_links=frozenset(
        [
            CPLink(provider_asn=3, customer_asn=ASNs.ATTACKER.value),
            CPLink(provider_asn=3, customer_asn=ASNs.VICTIM.value),
            CPLink(provider_asn=2, customer_asn=3),
            CPLink(provider_asn=1, customer_asn=2),
        ]
    ),
)


desc = "hidden hijack example against ROV"

hidden_hijack_rov_config = EngineTestConfig(
    name="hidden_hijack_rov_config",
    desc=desc,
    scenario_config=ScenarioConfig(
        ScenarioCls=SubprefixHijack,
        BasePolicyCls=BGP,
        override_attacker_asns=frozenset({ASNs.ATTACKER.value}),
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict(
            {
                2: ROV,
                ASNs.VICTIM.value: ROV,
            }
        ),
    ),
    as_graph_info=as_graph_info,
)
