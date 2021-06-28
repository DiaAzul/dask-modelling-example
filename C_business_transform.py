from Cb_business_transform_base import business_transform_base
from A_data_import import assumptions_data
from B_forecast_activity import acute_forecast, community_forecast


class business_transform(business_transform_base):
    def __init__(self) -> None:
        self.data = self._business_transform(
            acute_forecast=acute_forecast().data,
            community_forecast=community_forecast().data,
            assumptions_data=assumptions_data().data,
        )
