from unittest import TestCase

from resume import Resume

class TestResume(TestCase):
    def setUp(self) -> None:
        self.resume = Resume('test_data/resume.html', 'test_data/data.json')
        return super().setUp()
    
