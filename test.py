import unittest
from unittest.mock import patch
from io import StringIO
# replace 'your_game_module' with the actual module name
from adventure import Adventure


class TestAdventureGame(unittest.TestCase):
    def setUp(self):
        # Set up an Adventure instance for testing
        self.game = Adventure("test.map")

    def test_navigation(self):
        # Test the navigation through rooms

        # Redirect standard output to capture printed messages
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            # Test going in an invalid direction
            with patch("builtins.input", side_effect=["go west"]):
                self.game.look()
                self.game.process_command(["go"])
                self.assertEqual(mock_stdout.getvalue().strip(),
                                 "There's no way to go west.")

            # Test not specifying a direction after 'go'
            with patch("builtins.input", side_effect=["go"]):
                self.game.process_command(["go"])
                self.assertEqual(mock_stdout.getvalue().strip(),
                                 "Sorry, you need to 'go' somewhere.")

            # Test valid navigation
            with patch("builtins.input", side_effect=["go north", "go south", "go east"]):
                self.game.process_command(["go", "north"])
                self.assertEqual(
                    mock_stdout.getvalue().strip(), "You go north.")

                self.game.look()  # Look in the new room
                self.game.process_command(["go", "south"])
                self.assertEqual(
                    mock_stdout.getvalue().strip(), "You go south.")

                self.game.look()  # Look in the new room
                self.game.process_command(["go", "east"])
                self.assertEqual(
                    mock_stdout.getvalue().strip(), "You go east.")

    def test_room_descriptions(self):
        # Test room descriptions

        # Redirect standard output to capture printed messages
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            # Look in the initial room
            self.game.look()
            expected_output = "> A white room\n\nYou are in a simple room with white walls.\n\nExits: north east"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

            # Test moving to another room
            with patch("builtins.input", side_effect=["go north"]):
                self.game.process_command(["go", "north"])
                self.game.look()  # Look in the new room
                expected_output = "> A blue room\n\nThis room is simple, too, but with blue walls.\n\nExits: east south"
                self.assertEqual(
                    mock_stdout.getvalue().strip(), expected_output)


if __name__ == "__main__":
    unittest.main()
