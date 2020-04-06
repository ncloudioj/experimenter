from django.test import TestCase
from django.core.management import call_command

from experimenter.experiments.models import Experiment
from experimenter.experiments.constants import ExperimentConstants


class TestInitialData(TestCase):
    def test_load_dummy_experiments(self):
        self.assertFalse(Experiment.objects.exists())
        call_command("load-dummy-experiments")
        self.assertTrue(Experiment.objects.exists())

    def test_load_dummy_experiments_with_specified_values(self):
        call_command(
            "load-dummy-experiments",
            num_of_experiments=20,
            status=ExperimentConstants.STATUS_DRAFT,
        )
        self.assertTrue(Experiment.objects.exists())
        self.assertEqual(Experiment.objects.count(), 20)
        self.assertEqual(
            Experiment.objects.filter(status=ExperimentConstants.STATUS_DRAFT).count(), 20
        )
