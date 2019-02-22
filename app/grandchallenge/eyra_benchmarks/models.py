import logging

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from grandchallenge.core.models import UUIDModel
from grandchallenge.eyra_algorithms.models import Job, Algorithm
from grandchallenge.eyra_data.models import DataFile

logger = logging.getLogger(__name__)


class Benchmark(UUIDModel):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    description = models.TextField(
        default="",
        blank=True,
        help_text="Description of this project in markdown.",
    )
    name = models.CharField(
        max_length=64,
        blank=False,
        help_text=(
            "The name of the benchmark"
        ),
    )
    evaluator = models.ForeignKey(Algorithm, on_delete=models.SET_NULL, null=True, related_name='benchmarks')
    training_datafile = models.ForeignKey(DataFile, on_delete=models.SET_NULL, null=True, related_name='+')
    test_datafile = models.ForeignKey(DataFile, on_delete=models.SET_NULL, null=True, related_name='+')
    ground_truth_datafile = models.ForeignKey(DataFile, on_delete=models.SET_NULL, null=True, related_name='+')

    def clean(self):
        if self.training_datafile and not self.training_datafile.is_public:
            raise ValidationError("Training dataset should be public.")

    def __str__(self):
        """ string representation for this object"""
        return self.name

    class Meta:
        verbose_name = "benchmark"
        verbose_name_plural = "benchmarks"


class Submission(UUIDModel):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name="submissions",
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=32, unique=True, null=True)
    benchmark = models.ForeignKey(Benchmark, on_delete=models.CASCADE)
    algorithm = models.ForeignKey(Algorithm, on_delete=models.CASCADE, related_name='submissions')
    algorithm_job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, related_name='+')
    evaluation_job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, related_name='+')