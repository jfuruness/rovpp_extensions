from bgpy.simulation_engine import ROVPPV1Lite, ROVPPV2Lite, ROVPPV2ImprovedLite


class ROVPPV1LiteRenamed(ROVPPV1Lite):
    name = "ROV1"


class ROVPPV2LiteRenamed(ROVPPV2Lite):
    name = "ROV2"


class ROVPPV2iLiteRenamed(ROVPPV2ImprovedLite):
    name = "ROV2i"
