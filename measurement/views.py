from django.db.models import Prefetch
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, RetrieveUpdateAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, SensorSerializer, MeasureAddSerializer


class SensorView(RetrieveUpdateDestroyAPIView):
    # ПОЛУЧЕНИЕ ИНФО ПО ДАТЧИКУ С ИЗМЕРЕНИЯМИ
    queryset = Sensor.objects.prefetch_related('measurements').all()
    serializer_class = SensorDetailSerializer

    # ИЗМЕНЯЕМ(частично) ДАННЫЕ ПО ДАТЧИКУ
    def patch(self, request, pk):
        # Подсмотрел решение сокурсника из вопроса в Дискорде, ВООБЩЕ НЕ ПОНЯЛ как работает
        sensor = Sensor.objects.get(pk=pk)
        serializer = self.serializer_class(sensor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # УДАЛЕНИЕ ДАТЧИКА ПО pk
    def delete(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        sensor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SensorsView(ListCreateAPIView):
    # ВСЕ ДАТЧИКИ
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    # СОЗДАЕМ ДАТЧИК
    def post(self, request, *args, **kwargs):
        # Подсмотрел решение на stackoverflow, не совсем понял как работает
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ДОБАВЛЯЕМ ИЗМЕРЕНИЕ ДАТЧИКУ ПО НОМЕРУ
class MeasureView(CreateAPIView):
    # Сделал как смог... через сериализатор ничего не вышло... примеров не нашел.
    def post(self, request, *args, **kwargs):
        sensor = Sensor.objects.get(id=request.data['sensor'])
        Measurement.objects.create(
            sensor=sensor,
            temperature=request.data['temperature'],
        )
        return Response(status=status.HTTP_201_CREATED)
