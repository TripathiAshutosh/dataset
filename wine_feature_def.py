from datetime import timedelta
from feast import Entity, FeatureService, FeatureView, Field, FileSource, ValueType
from feast.types import Float64, Int64

wine_entity = Entity(name = "wine_id",
                     value_type = ValueType.INT64,
                 description = "ID of the wine")

## Predictors Feature View
file_source = FileSource(path = r"wine.parquet",timestamp_field = "event_timestamp")

wine_fv = FeatureView(
    name = "wine_fv",
    ttl = timedelta(seconds = 86400*2),
    entities = ['wine_id'],
    schema = [
    Field(name = "fixed acidity", dtype = Float64),
    Field(name = "volatile acidity", dtype = Float64),
        Field(name = "citric acid", dtype = Float64),
        Field(name = "residual sugar", dtype = Float64),
        Field(name = "chlorides", dtype = Float64),
        Field(name = "free sulfur dioxide", dtype = Float64),
        Field(name = "total sulfur dioxide", dtype = Float64),
        Field(name = "density", dtype = Float64),
        Field(name = "pH", dtype = Float64),
        Field(name = "sulphates", dtype = Float64),
        Field(name = "alcohol", dtype = Float64),
        Field(name = "quality", dtype = Int64),
        Field(name = "wine_type", dtype = Int64),
    ],
    source = file_source,
    online = True,
    tags= {},
)