from django.test import TestCase
from app import models
from datetime import date

# Create your tests here.
class TestLeaveRequest(TestCase):
    # def test_create(self):
    #     LeaveRequest.create_request("Luis Ortiz", True, False, True, True, "Joe Trott")
    #     request = LeaveRequest.objects.get(employee_name="Luis Ortiz")
    #     self.assertEqual(request.date_requested, date.today())

    # def test_approve_request(self):
    #     LeaveRequest.create_request(
    #         "Luis Ortiz",
    #         True,
    #         False,
    #         True,
    #         False,
    #         "Joe Trott",
    #     )

    #     requests = LeaveRequest.approve_request("Luis Ortiz")
    #     self.assertTrue(requests.is_approved, True)

    def test_search_by_date(self):
        models.create_request(
           "2023-07-07", "Luis Ortiz", True, False, True, True, "Joe Trott"
        )
        models.create_request(
            None,"Armando", True, False, True, True, "Luis", "2023-04-04"
        )
        requests = models.search_by_date("2023-07-07")
        self.assertIsNotNone(requests)

        self.assertEqual(len(requests),1)


    def test_filter_by_sick(self):
        models.create_request(
           "2023-07-07", "Luis Ortiz", False, False, True, True, "Joe Trott"
        )
        models.create_request(
            None,"Armando", False, False, True, True, "Luis", "2023-04-04"
        )
        requests = models.filter_by_sick()
        self.assertEqual(len(requests),0)

    def test_filter_by_approval(self):
        models.create_request(
           "2023-07-07", "Luis Ortiz", False, False, True, True, "Joe Trott"
        )
        models.create_request(
            None,"Armando", False, False, True, True, "Luis", "2023-04-04"
        )
        requests = models.filter_by_approval()
        self.assertEqual(len(requests),2)

    def test_filter_by_paid(self):
        models.create_request(
           "2023-07-07", "Luis Ortiz", False, False, True, True, "Joe Trott"
        )
        models.create_request(
            None,"Armando", False, False, False, True, "Luis", "2023-04-04"
        )

        requests = models.filter_by_paid()
        self.assertEqual(len(requests),1)

    

