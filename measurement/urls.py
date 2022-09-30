from django.urls import path, include
from measurement.views import SensorView, SensorsView, MeasureView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', MeasureView.as_view()),

]
