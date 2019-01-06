import geoalchemy2
from geoalchemy2.functions import GenericFunction
from shapely.geometry import shape
from sqlalchemy import func

from flask_admin.form import JSONField

from .widgets import LeafletWidget

class AsGeoJSON(GenericFunction):
    name = 'AsGeoJSON'
    identifier = 'ST_AsGeoJSON'

class GeoJSONField(JSONField):
    widget = LeafletWidget()

    def __init__(self, label=None, validators=None, geometry_type="GEOMETRY",
                 srid='-1', session=None, **kwargs):
        super(GeoJSONField, self).__init__(label, validators, **kwargs)
        self.web_srid = 4326
        self.srid = srid
        if self.srid is -1:
            self.transform_srid = self.web_srid
        else:
            self.transform_srid = self.srid
        self.geometry_type = geometry_type.upper()
        self.session = session

    def _value(self):
        # Putting this directly under the file imports doesn't work.
        if self.raw_data:
            print("self.raw_data")
            return self.raw_data[0]
        if type(self.data) is geoalchemy2.elements.WKBElement:
            print("self.data is WKBElement")
            if self.srid is -1:
                return self.session.scalar(AsGeoJSON(self.data))
            else:
                return self.session.scalar(
                    AsGeoJSON(
                        func.ST_Transform(self.data, self.web_srid)
                    )
                )
        else:
            print("not raw_data or self.data is WKBElement")
            return ''

    def process_formdata(self, valuelist):
        super(GeoJSONField, self).process_formdata(valuelist)
        if str(self.data) is '':
            self.data = None
        if self.data is not None:
            print(repr(self.data))
            web_shape = self.session.scalar(
                func.ST_AsText(
                    func.ST_Transform(
                        func.ST_GeomFromText(
                            shape(self.data).wkt,
                            self.web_srid
                        ),
                        self.transform_srid
                    )
                )
            )
            self.data = 'SRID=' + str(self.srid) + ';' + str(web_shape)
