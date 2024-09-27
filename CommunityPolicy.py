class CommunityActivity:
    def __init__(self, activity_id, name, description):
        self.activity_id = activity_id
        self.name = name
        self.description = description

    def __str__(self):
        return f"FID: {self.activity_id}, Name: {self.name}, Description: {self.description}"

class CommunityPolicing:
    def __init__(self):
        self.activities = {}
        self.meetings = {}
        self.feedback = {}

    def add_activity(self, activity_id, name, description):
        if activity_id in self.activities:
            raise ValueError("Activity ID already exists.")
        self.activities[activity_id] = CommunityActivity(activity_id, name, description)

    def remove_activity(self, activity_id):
        if activity_id in self.activities:
            del self.activities[activity_id]
        else:
            raise KeyError("Activity not found.")

    def update_activity(self, activity_id, name=None, description=None):
        if activity_id in self.activities:
            activity = self.activities[activity_id]
            if name:
                activity.name = name
            if description:
                activity.description = description
        else:
            raise KeyError("Activity not found.")

    def get_activity(self, activity_id):
        if activity_id in self.activities:
            return self.activities[activity_id]
        else:
            raise KeyError("Activity not found.")

    def schedule_community_meeting(self, meeting_id, details):
        if meeting_id in self.meetings:
            raise ValueError("Meeting ID already exists.")
        self.meetings[meeting_id] = details

    def track_community_feedback(self, feedback_id, feedback_details):
        if feedback_id in self.feedback:
            raise ValueError("Feedback ID already exists.")
        self.feedback[feedback_id] = feedback_details

    def get_meeting_details(self, meeting_id):
        if meeting_id in self.meetings:
            return self.meetings[meeting_id]
        else:
            raise KeyError("Meeting not found.")

    def get_feedback_details(self, feedback_id):
        if feedback_id in self.feedback:
            return self.feedback[feedback_id]
        else:
            raise KeyError("Feedback not found.")

# Unit testing the classes
import unittest

class TestCommunityPolicing(unittest.TestCase):
    def setUp(self):
        self.cp = CommunityPolicing()
        self.cp.add_activity(1, "Neighborhood Watch", "Residents keep an eye out for suspicious activities.")
        self.cp.schedule_community_meeting(1, "Community Engagement on 2023-11-01 at Main Hall")

    def test_add_activity(self):
        self.cp.add_activity(2, "Youth Engagement", "Activities for local youth.")
        self.assertIn(2, self.cp.activities)
        self.assertEqual(self.cp.activities[2].name, "Youth Engagement")

    def test_remove_activity(self):
        self.cp.remove_activity(1)
        self.assertNotIn(1, self.cp.activities)

    def test_update_activity(self):
        self.cp.update_activity(1, name="Updated Neighborhood Watch")
        self.assertEqual(self.cp.activities[1].name, "Updated Neighborhood Watch")

    def test_schedule_meeting(self):
        self.cp.schedule_community_meeting(2, "Safety Workshop on 2023-12-01")
        self.assertIn(2, self.cp.meetings)
        self.assertEqual(self.cp.meetings[2], "Safety Workshop on 2023-12-01")

    def test_get_activity_exception(self):
        with self.assertRaises(KeyError):
            self.cp.get_activity(3)

if __name__ == "__main__":
    unittest.main()
