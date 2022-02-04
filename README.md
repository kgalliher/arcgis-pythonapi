# Parcel Fabric Python API Utils
## Helper functions for simplifying parcel fabric workflows with the ArcGIS Python API

** Install arcgis module **

`conda install -c esri arcgis`

### Utils
Basic functions to write json to a file, get a server token and a simple timer decorator

### Features
#### features/feature_utils
Functions for getting and querying FeatureLayer and FeatureLayerCollection objects. Simplifies and shortens return values for basic feature layer info.

### Versioning
#### versioning/versioning_utils
Functions for creating and deleting versions. Start and stop edit sessions for branch versioned editing.

### Parcels
#### parcels/parcels_utils
Functions to query parcel features returning dicts with correct format for subission to Parcel Fabric REST methods.  Create parcel records for record driven workflows. Copy external line features into a parcel type.
