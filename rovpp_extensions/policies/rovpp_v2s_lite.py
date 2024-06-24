from typing import TYPE_CHECKING

from bgpy.enums import Relationships
from bgpy.simulation_engine import ROVPPV2ImprovedLite

if TYPE_CHECKING:
    from bgpy.simulation_engine import Announcement as Ann


class ROVPPV2ShortenedLite(ROVPPV2ImprovedLite):
    """Shortens the path as much as possible

    NOTE: this would be incompatible with some path defense
    mechanisms, but these are not deployed lol
    """

    name: str = "ROV++V2s Lite"

    def _add_blackholes_to_local_rib(self, blackholes: tuple["Ann", ...]) -> None:
        """Shorten the paths as much as possible"""

        new_blackholes = list()
        for blackhole in blackholes:
            new_blackholes.append(
                # Shorten the AS path of all blackholes as much as possible
                blackhole.copy({"as_path": (self.as_.asn,), "traceback_end": True})
            )
        super()._add_blackholes_to_local_rib(new_blackholes)
