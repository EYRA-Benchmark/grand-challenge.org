from rest_framework.permissions import BasePermission, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from grandchallenge.eyra_algorithms.models import Algorithm, Job
from grandchallenge.eyra_algorithms.serializers import AlgorithmSerializer, JobSerializer


class AlgorithmViewSet(ModelViewSet):
    queryset = Algorithm.objects.exclude(output_type__name__exact='OutputMetrics')
    serializer_class = AlgorithmSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        # Add the logged in user as the challenge creator
        serializer.save(creator=self.request.user)


class JobViewSet(ReadOnlyModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)