"""Forecast the impact of business transformation on baseline activity for 
acute hospitals and community services across different service lines.
"""

from dask import delayed
from dask.delayed import Delayed

from .A_data_import import assumptions_data
from .B_forecast_activity import acute_forecast, community_forecast
from .Cb_business_transform_base import business_transform_base


class business_transform(business_transform_base):
    """Apply the anticipated impact of the business transformation to acute hospital and
    community services activity"""

    @property
    def data(self) -> Delayed:
        """Acute hospital and community activity."""
        return delayed(self._business_transform)(
            acute_forecast=acute_forecast().data,
            community_forecast=community_forecast().data,
            assumptions_data=assumptions_data().data,
        )
