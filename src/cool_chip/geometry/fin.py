"""Fin geometry."""

import cadquery as cq
from cadquery.occ_impl import geom
import cool_chip

from cool_chip.utils.io import out_geom_path


class Fin:
    """Fin object."""

    geom = None
    is_geom_init = False

    def __init__(self) -> None:
        raise BaseException("Unimplemented")

    def export_geom(self, filename, filetype="STEP"):
        if self.geom is not None:
            cq.exporters.export(
                self.geom,
                f"{out_geom_path()}/{filename}.{filetype.lower()}",
                exportType=filetype,
            )
        else:
            raise BaseException("Geometry not created.")


class CylindricalFin(Fin):
    """Cylindrical fin object."""

    def __init__(self, bottom_radius=5.0, top_radius=0.1, height=100, concavity=2):
        """Create cylindrical fin."""

        self.FIN_BOTTOM_RADIUS = bottom_radius
        self.FIN_TOP_RADIUS = top_radius
        self.FIN_HEIGHT = height
        self.CONCAVITY = concavity

        fin = cq.Workplane("XY")
        radius_array = self.create_intermediate_radius()
        for i, radius in enumerate(radius_array):
            fin.workplane(offset=((self.FIN_HEIGHT / 20) * i)).circle(radius=radius)
        fin = fin.loft(combine=True)
        self.geom = fin
        self.is_geom_init = True

    def create_intermediate_radius(self):
        intermediate_radius = [
            (
                self.FIN_TOP_RADIUS
                + (self.FIN_BOTTOM_RADIUS - self.FIN_TOP_RADIUS)
                * (1 - (((self.FIN_HEIGHT / 20) * r) / self.FIN_HEIGHT))
                ** self.CONCAVITY
            )
            for r in range(20)
        ]
        return intermediate_radius
